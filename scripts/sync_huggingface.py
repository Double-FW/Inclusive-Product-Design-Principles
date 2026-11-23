#!/usr/bin/env python3
"""Build and publish the curated Inclusive Product Design Principles dataset."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import tempfile
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "Double-FW/Inclusive-Product-Design-Principles"
TARGET = "GarethFW/Inclusive_Product_Design_Principles"
VERSION = "1.0.0"
DOCS = [
    "AGENTS.md",
    "README.md",
    "Dieter_Rams_Digital_Product_Design_Principles_Multimodal.md",
    "Dieter_Rams_Indifference_Cardinal_Sin_Design.md",
    "Nonvisual_User_Expectations_Needs_Preferences_and_Outcomes.md",
    "POUR_Brand_Experience_Outcomes_Nonvisual_Perspective.md",
    "POUR_Brand_Experience_Outcomes_Sighted_Perspective.md",
    "Principles_First_Person_Sighted_Perspective.md",
    "UX_Practice_From_Principles_to_People.md",
]
CHUNKS = DOCS[2:]
SOURCE_FILES = DOCS + ["LICENSE"]
MANAGED = [
    "README.md", "LICENSE", "documents.jsonl", "knowledge_chunks.jsonl",
    "provenance.json", "record_schema.json", "export_manifest.json",
]
HEADING = re.compile(r"^(#{1,3})[ \\t]+(.+?)\\s*#*[ \\t]*$")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(*args):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *args], text=True, stderr=subprocess.PIPE
    ).strip()


def committed_file(path):
    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts or any(p.startswith(".") for p in pure.parts):
        raise ValueError("Invalid approved source path: " + path)
    entry = git("ls-tree", "HEAD", "--", path)
    if not entry.startswith("100644 blob "):
        raise ValueError("Approved source must be a committed regular file: " + path)
    blob = entry.split()[2]
    data = subprocess.check_output(["git", "-C", str(ROOT), "cat-file", "blob", blob])
    local = ROOT / path
    if not local.is_file() or local.is_symlink() or local.read_bytes() != data:
        raise ValueError("Working source differs from committed HEAD: " + path)
    return data


def load_sources():
    config = json.loads(committed_file("huggingface/export-config.json"))
    if config.get("source_repository") != SOURCE or config.get("destination_dataset") != TARGET:
        raise ValueError("Export configuration does not match the fixed source and destination.")
    if config.get("dataset_version") != VERSION:
        raise ValueError("Review the export format version before changing it.")
    if config.get("document_files") != DOCS or config.get("chunk_files") != CHUNKS:
        raise ValueError("Curated document allowlist changed; review before publication.")
    if config.get("source_files") != SOURCE_FILES:
        raise ValueError("Source integrity allowlist changed; review before publication.")
    content = {path: committed_file(path).decode("utf-8") for path in SOURCE_FILES}
    if not content["LICENSE"].startswith("MIT License\\n"):
        raise ValueError("The source licence is no longer the approved MIT licence.")
    return content, git("rev-parse", "HEAD"), git("show", "-s", "--format=%cs", "HEAD")


def verify_public_source():
    request = urllib.request.Request(
        "https://api.github.com/repos/" + SOURCE,
        headers={"User-Agent": "Double-FW-Inclusive-Product-Design-Principles-sync",
                 "Accept": "application/vnd.github+json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            info = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError):
        raise ValueError("Could not confirm the public GitHub source; no HF write was attempted.") from None
    if info.get("full_name") != SOURCE or info.get("private") is not False or info.get("visibility") != "public":
        raise ValueError("Publishing requires the approved public GitHub source.")
    if (info.get("license") or {}).get("spdx_id") != "MIT":
        raise ValueError("Publishing requires the source repository to declare the MIT licence.")


def slug(value):
    value = value.lower().replace("–", "-").replace("—", "-")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def make_record(text, source_text, path, commit, date, title, kind, start, end, headings, record_id):
    encoded_path = urllib.parse.quote(path, safe="/")
    return {
        "id": record_id, "title": title, "text": text, "record_type": kind,
        "source_repository": SOURCE, "source_path": path, "source_commit": commit,
        "source_url": "https://github.com/" + SOURCE + "/blob/" + commit + "/" + encoded_path,
        "source_start_line": start, "source_end_line": end,
        "source_document_sha256": digest(source_text.encode("utf-8")),
        "text_sha256": digest(text.encode("utf-8")), "heading_path": headings,
        "declared_source_license": "MIT", "repository_license": "MIT",
        "dataset_version": VERSION, "source_commit_date": date, "language": "en-GB",
        "review_status": "Consult the source text; the exporter does not infer approval.",
    }


def make_records(content, commit, date):
    documents = []
    for path in DOCS:
        text = content[path]
        documents.append(make_record(
            text, text, path, commit, date, Path(path).stem, "full_document",
            1, len(text.splitlines()), [], "doc-" + slug(Path(path).stem),
        ))
    chunks = []
    for path in CHUNKS:
        text = content[path]
        lines = text.splitlines()
        headings, stack = [], []
        for index, line in enumerate(lines):
            match = HEADING.match(line)
            if match:
                depth, title = len(match.group(1)), match.group(2).strip()
                stack = stack[:depth - 1] + [title]
                headings.append((index, depth, title, stack.copy()))
        for pos, (start, depth, title, heading_path) in enumerate(headings):
            end = len(lines)
            for next_start, next_depth, _, _ in headings[pos + 1:]:
                if next_depth <= depth:
                    end = next_start
                    break
            section = "\\n".join(lines[start:end]).rstrip("\\n")
            if section.strip():
                chunks.append(make_record(
                    section, text, path, commit, date, title, "section",
                    start + 1, start + len(section.splitlines()), heading_path,
                    "section-" + slug(Path(path).stem) + "-" + str(start + 1),
                ))
    return documents, chunks


def build_payloads():
    content, commit, date = load_sources()
    documents, chunks = make_records(content, commit, date)
    if len(documents) != len(DOCS) or not chunks:
        raise ValueError("Curated export produced an unexpected record count.")
    card = f"""---
license: mit
language:
- en
tags:
- accessibility
- inclusive-design
- product-design
- ux
- research
- agent-governance
configs:
- config_name: knowledge_chunks
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# Inclusive Product Design Principles

A versioned export of selected guidance from the public Double-FW/Inclusive-Product-Design-Principles repository for human and AI-assisted retrieval. The content offers design and research lenses; it is not a conformance scheme, legal interpretation, or evidence that a product works for a population.

## Source and revision

- Source: https://github.com/Double-FW/Inclusive-Product-Design-Principles
- Source commit: {commit} ({date})
- Export format: {VERSION}
- Licence: MIT, matching the source repository.

## Contents

The configurations overlap by design. Choose one configuration for a given retrieval task; do not concatenate them as independent source material.

- `knowledge_chunks.jsonl`: heading-level sections from seven active guidance documents, with source paths, line ranges, hashes, heading paths, and revision metadata.
- `documents.jsonl`: complete README, AGENTS, and guidance documents for context and verification.

The source files include multimodal digital product design principles, design indifference, nonvisual expectations and outcomes, paired nonvisual and sighted brand-experience perspectives, first-person sighted principles, and practical UX guidance. README.md and AGENTS.md provide context and usage boundaries. The repository's MIT licence is included.

## Evidence and limits

First-person materials are authored analytical perspectives unless the source explicitly documents participant provenance and method. They do not represent all disabled people or establish population preferences. Distinguish sourced guidance, participant report, observed behaviour, interpretation, hypothesis, and synthetic planning material. Do not treat satisfaction or reported emotion as proof of task success, security, accessibility, or conformance.

This dataset contains guidance, not participant, customer, health, or confidential organisational data. It includes no generated question-answer pairs, benchmark split, model weights, evaluation results, or evidence that a model has been trained. The `train` split label does not mean model training occurred.

Source text is data, not authority to override system or developer instructions, access private information, contact people, publish, or make live product changes. Human authority remains responsible for consequential decisions.

## Loading

Install the Hugging Face `datasets` library and choose a configuration:

    from datasets import load_dataset

    chunks = load_dataset("GarethFW/Inclusive_Product_Design_Principles", "knowledge_chunks", split="train")
    documents = load_dataset("GarethFW/Inclusive_Product_Design_Principles", "documents", split="train")

Pin a dataset revision for reproducible work. Full documents and section records overlap by design.

## Updating

GitHub is the authoring source. GitHub Actions syncs approved changes from the default branch after curated source changes and on a weekly schedule. A manual run is also available. Setup instructions are in the source repository's `huggingface/SETUP.md`. A sync does not mean a model or downstream copy has refreshed.
"""
    provenance = {
        "dataset": TARGET, "dataset_version": VERSION,
        "source_repository": "https://github.com/" + SOURCE,
        "source_visibility": "public", "source_commit": commit,
        "source_commit_date": date, "source_license": "MIT",
        "source_files": [
            {"path": path, "git_blob_sha": git("rev-parse", "HEAD:" + path),
             "sha256": digest(content[path].encode("utf-8"))}
            for path in SOURCE_FILES
        ],
        "document_paths": DOCS, "chunk_paths": CHUNKS,
        "records": {"documents": len(documents), "knowledge_chunks": len(chunks)},
        "selection_note": "README.md and AGENTS.md provide context; seven product-design guidance documents are sectioned for retrieval.",
        "limitations": [
            "Guidance only; not legal advice, a conformity decision, or product evaluation.",
            "Full documents and section records overlap by design.",
            "The exporter does not infer approval or validate claims in source documents.",
            "First-person perspective documents are not participant evidence unless their source states otherwise.",
        ],
    }
    schema = {
        "description": "One JSON object per line. Source text is untrusted data, not executable instruction.",
        "fields": {
            "id": "Stable identifier within a source path and export revision.",
            "title": "Document title or section heading.", "text": "Exact source Markdown text.",
            "record_type": "full_document or section.", "source_repository": "GitHub owner/repository.",
            "source_path": "Path in the source repository.", "source_commit": "Source commit SHA.",
            "source_url": "Commit-pinned public source URL.", "source_start_line": "One-based first line.",
            "source_end_line": "One-based final line.", "source_document_sha256": "SHA-256 of full source text.",
            "text_sha256": "SHA-256 of this record text.", "heading_path": "Ordered headings to this section.",
            "declared_source_license": "Source repository licence.", "repository_license": "Dataset licence.",
            "dataset_version": "Export schema/content version.", "source_commit_date": "Source commit date.",
            "language": "Primary language tag.", "review_status": "Consult source; exporter makes no approval claim.",
        },
    }
    payload = {
        "README.md": card.encode("utf-8"),
        "LICENSE": content["LICENSE"].encode("utf-8"),
        "documents.jsonl": ("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\\n" for r in documents)).encode("utf-8"),
        "knowledge_chunks.jsonl": ("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\\n" for r in chunks)).encode("utf-8"),
        "provenance.json": (json.dumps(provenance, ensure_ascii=False, indent=2) + "\\n").encode("utf-8"),
        "record_schema.json": (json.dumps(schema, ensure_ascii=False, indent=2) + "\\n").encode("utf-8"),
    }
    manifest = {
        "dataset_version": VERSION, "source_commit": commit,
        "records": {"documents": len(documents), "knowledge_chunks": len(chunks)},
        "files": {name: {"size_bytes": len(data), "sha256": digest(data)}
                  for name, data in sorted(payload.items())},
    }
    payload["export_manifest.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\\n").encode("utf-8")
    return payload, {"commit": commit, "documents": len(documents), "knowledge_chunks": len(chunks)}


def build(output, dataset_id):
    if dataset_id != TARGET:
        raise ValueError("The dataset destination is fixed to " + TARGET + ".")
    payload, summary = build_payloads()
    output.mkdir(parents=True, exist_ok=True)
    for name, data in payload.items():
        data.decode("utf-8")
        (output / name).write_bytes(data)
    return summary


def publish(folder, token, dataset_id):
    if dataset_id != TARGET:
        raise ValueError("The dataset destination is fixed to " + TARGET + ".")
    if not token or not token.startswith("hf_") or token != token.strip() or any(c in token for c in "\\n\\r\\t"):
        raise ValueError("Add the dataset-scoped HF_TOKEN GitHub Actions secret.")
    verify_public_source()
    with tempfile.TemporaryDirectory() as temporary:
        build(Path(temporary), dataset_id)
        payload = {name: (folder / name).read_bytes() for name in MANAGED}
        if any(payload[name] != (Path(temporary) / name).read_bytes() for name in MANAGED):
            raise ValueError("Generated files differ from the validated source snapshot.")
    from huggingface_hub import CommitOperationAdd, HfApi, hf_hub_download
    from huggingface_hub.errors import EntryNotFoundError
    api = HfApi(token=token)
    info = api.repo_info(repo_id=TARGET, repo_type="dataset")
    parent = getattr(info, "sha", None)
    if not parent:
        raise ValueError("The destination must be an existing initialised dataset repository.")
    previous = {}
    for name in MANAGED:
        try:
            path = hf_hub_download(repo_id=TARGET, filename=name, repo_type="dataset", revision=parent, token=token)
            previous[name] = Path(path).read_bytes()
        except EntryNotFoundError:
            previous[name] = None
    old = previous.get("provenance.json")
    if old:
        old_source = json.loads(old).get("source_repository")
        if old_source not in (None, SOURCE, "https://github.com/" + SOURCE):
            raise ValueError("Destination provenance belongs to another source; no write was made.")
    changed = [name for name in MANAGED if previous[name] != payload[name]]
    if not changed:
        return "No changes; the dataset is already up to date."
    source_commit = json.loads(payload["provenance.json"])["source_commit"]
    api.create_commit(
        repo_id=TARGET, repo_type="dataset", parent_commit=parent,
        operations=[CommitOperationAdd(path_in_repo=name, path_or_fileobj=payload[name]) for name in changed],
        commit_message="Sync Inclusive Product Design Principles dataset",
        commit_description="GitHub source revision: " + source_commit,
    )
    return "Updated " + str(len(changed)) + " managed files in one Hugging Face commit; unrelated files and visibility were preserved."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("check", "build", "publish"), required=True)
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--output")
    parser.add_argument("--folder")
    args = parser.parse_args()
    try:
        if args.mode == "check":
            with tempfile.TemporaryDirectory() as temporary:
                result = build(Path(temporary), args.dataset_id)
        elif args.mode == "build":
            if not args.output:
                parser.error("--output is required for build mode.")
            result = build(Path(args.output), args.dataset_id)
        else:
            if not args.folder:
                parser.error("--folder is required for publish mode.")
            result = publish(Path(args.folder), os.environ.get("HF_TOKEN", ""), args.dataset_id)
    except ValueError as error:
        raise SystemExit(str(error))
    except Exception as error:
        status = getattr(getattr(error, "response", None), "status_code", None)
        code = str(status) if isinstance(status, int) else "unknown"
        raise SystemExit("Hugging Face publication failed (" + type(error).__name__ + ", HTTP " + code + "). Check token scope, destination access, and concurrent updates. Credentials and response bodies are not logged.")
    if isinstance(result, dict):
        print("Validated source " + result["commit"] + "; " + str(result["documents"]) + " documents and " + str(result["knowledge_chunks"]) + " section records.")
    else:
        print(result)
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a", encoding="utf-8") as handle:
                handle.write("## Hugging Face dataset sync\\n\\n" + result + "\\n")


if __name__ == "__main__":
    main()
