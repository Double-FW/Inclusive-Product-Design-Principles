# GitHub to Hugging Face dataset sync

Source repository: https://github.com/Double-FW/Inclusive-Product-Design-Principles  
Destination dataset: https://huggingface.co/datasets/GarethFW/Inclusive_Product_Design_Principles

## One-time owner setup

The workflow needs a Hugging Face access token with write access to this dataset. Do not share the token in chat or put it in a file.

1. Open [Hugging Face token settings](https://huggingface.co/settings/tokens).
2. Create a fine-grained token. Give it read and write access to the single dataset repository **GarethFW/Inclusive_Product_Design_Principles**. A token restricted to another dataset will not work.
3. Copy the token once. Keep it private; do not paste it into a GitHub file, issue, workflow log, or chat.
4. Open the source repository's [New repository secret page](https://github.com/Double-FW/Inclusive-Product-Design-Principles/settings/secrets/actions/new). Sign in to GitHub if requested.
5. In the **Name** field, enter exactly: `HF_TOKEN`.
6. In the **Secret** field, paste the Hugging Face token. Click **Add secret**.
7. Confirm the sync workflow has been merged into the repository's default branch, `main`.
8. Open the [Actions page](https://github.com/Double-FW/Inclusive-Product-Design-Principles/actions), choose **Sync Inclusive Product Design Principles dataset**, click **Run workflow**, select branch **main**, and click the green **Run workflow** button.
9. Open the new run and confirm the **publish** job succeeds. Then open the destination dataset's [Files and versions](https://huggingface.co/datasets/GarethFW/Inclusive_Product_Design_Principles/tree/main) page and check for the new sync commit and exported files.

The destination dataset already exists. The workflow is restricted to that fixed dataset ID and preserves unrelated destination files and dataset visibility.

## Ongoing sync behaviour

- A push to `main` that changes an approved source document, exporter configuration, setup documentation, README, licence, or workflow starts a sync.
- A scheduled sync also runs every Monday at 07:41 UTC. GitHub may delay scheduled runs.
- You can start a manual run from the Actions page.
- Pull requests do not publish. The workflow publishes only from the default branch.
- If generated files have not changed, no Hugging Face commit is created.
- The export includes full source-document records and heading-level section records. Those views overlap by design. Context files are included for interpretation but are not chunked as guidance sections.
- The workflow copies the repository's MIT licence and records source commit, file hashes, line ranges, and provenance.
- The workflow does not publish audit or test reports.
- The destination's existing `README.md` is empty at setup time; the first successful run replaces it with the dataset card.
- The GitHub source must remain public and declare the MIT licence. The Hugging Face token is exposed only to the publishing step.

If a run fails, open the run, expand the failed step, and read its error. Common causes include a missing secret, a token without write access to this exact dataset, or a changed source allowlist. Never paste credentials into a log, issue, commit, or chat.
