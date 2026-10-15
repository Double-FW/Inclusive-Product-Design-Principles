# From principles to people: a practical guide to visual-first and nonvisual-first UX

## Purpose

UX teams inherit many useful ideas: learn from people, make tasks understandable, reduce needless effort, design for recovery, and take emotion seriously. This guide brings those ideas together with two first-person perspectives supplied for this work: *UX Principles and Methods* from a sighted perspective, and *Don’t Make Me Construct the Interface* from a congenitally blind perspective.

It also carries forward the related work on Dieter Rams’s ten principles, indifference as a cardinal design failure, brand experience outcomes, and accessible typography. The aim is to put those ideas to work in everyday UX decisions: what to notice, what to ask, what to prototype, how to test, and how to decide what to change.

The two lenses are called **visual-first** and **nonvisual-first**. They describe ways of encountering a service, not fixed types of people. The visual-first perspective may use visual scanning, hierarchy, grouping and appearance to form an overview. The nonvisual-first perspective may use speech, Braille, keyboard commands, touch, voice input or combinations of these. It is not synonymous with audio-only use. The supplied nonvisual perspective is specifically written from the experience of congenital blindness; its insights are valuable, but should not be treated as a profile of every blind person.

A first-person perspective is a way to generate questions, not a substitute for research with people. Preferences and strategies vary with task, technology, experience, language, fatigue, context and individual choice. Use the perspectives to widen what the team notices, then test decisions with the people who will use the product.

## The central UX question

Start with the outcome a person needs. Then ask whether the product makes that outcome understandable, achievable and recoverable in the person’s real circumstances.

This question holds together several ideas from the companion work:

- Rams’s principles ask whether a product is useful, understandable, honest, enduring and considerate of resources.
- The warning against indifference asks whose reality the design assumes and who pays for a decision.
- The brand outcome lens asks whether people feel **seen, capable, confident, safe and valued** through the experience.
- The UX perspectives ask how people actually scan, navigate, choose, recover and learn.
- Typography matters because it carries both brand character and reading effort; type is one part of a complete communication system.

These ideas strengthen one another. Functional success is evidence of care. Emotional response is part of the experience people interpret. Brand is shaped by what the service repeatedly enables and how it treats people, not only by what it says about itself. Repeated small uncertainties also consume attention and goodwill. People may respond by choosing the first plausible option, relying on a remembered route or muddling through without a complete model. These are adaptive behaviours, not proof that the design is clear.

---

## Why affordances, signifiers and conventions belong at the foundation

These terms are often treated as specialist vocabulary or as a visual styling discussion. They are more fundamental: they explain how a person discovers what a product makes possible, decides what an action means and learns how to use the system.

### Affordance: what action is possible in this relationship?

An affordance is an action possibility arising from the relationship between an actor and an environment. A screen-mediated system may let a person touch, point or click, but that alone does not tell them which action is detected, meaningful or useful in a particular product. Don Norman distinguishes the action possibilities from the cues that help people discover them; in screen interfaces, designers often control the cues and feedback more directly than the underlying physical possibilities ([Affordances and Design](https://jnd.org/affordances-and-design/)).

For UX work, ask what a person can actually do, with the device, input method and context they have. A control that looks actionable but does nothing offers a false promise. A task that is possible only with a mouse is not possible for the person using a keyboard or another input method.

### Signifier: what tells someone what can be done?

A signifier is a perceivable cue about an action, object, state or relationship. It may be visual, spoken, tactile, spatial, textual or based on a familiar interaction. A label such as “Change delivery address” can be a signifier. So can a button’s shape, a visible focus indicator, a spoken name and role, a Braille label, or a clear announcement that a panel has opened.

A cue can mislead as well as guide. A decorative card that behaves like a link, an icon without a useful name, or a screen-reader announcement that calls a link a button makes the product harder to predict. Norman’s point is useful here: people need clues about what a product is for, what is happening and what alternatives are available ([Signifiers, not affordances](https://jnd.org/signifiers-not-affordances/)).

### Convention: what has a community learned to expect?

A convention is a learned, shared pattern. Examples include the familiar behaviour of links and buttons, the placement of primary navigation, the meaning of common symbols, or the use of a heading to introduce a section. Conventions reduce the amount a person has to learn, but they are not universal or natural laws. They vary across cultures, products, devices and levels of experience. Norman describes screen conventions as learned cultural constraints that can help people navigate unfamiliar systems ([Affordance, Conventions and Design](https://jnd.org/affordance-conventions-and-design-part-2/)).

A brand can create its own patterns, but a new pattern asks people to learn. Give that learning a reason, preserve familiar behaviour where it matters, and make the new pattern understandable in every mode. A departure from convention may be appropriate, especially in expert tools or expressive experiences, but should be tested rather than defended as self-evidently better.

### Mapping, feedback and constraints complete the picture

- **Mapping** connects a control or choice to its effect. The relationship should make sense: changing the delivery date should affect the delivery date, not silently change the order.
- **Feedback** tells the person what the system did. A save, error, selection, loading state or completed action should be perceptible in the modes people use.
- **Constraints** guide action by making invalid or dangerous paths less likely. They should prevent mistakes without creating unnecessary dead ends.
- **A conceptual model** is the person’s working understanding of how the product is organised and what will happen. Consistent labels, patterns, structure and feedback help that model form.

These are not separate from brand and emotion. A clear signifier can make someone feel capable. Predictable conventions can build confidence. Honest feedback can support trust. A misleading signifier can make the same brand feel manipulative. Functional design is one of the main ways an emotional promise becomes believable.

### One example, viewed in two modes

Imagine a person changing a recurring order.

| UX question | Visual-first experience | Nonvisual-first experience |
| --- | --- | --- |
| What can I do? | Controls look interactive and are distinguished from supporting text. | Controls have meaningful names, roles and states; familiar keyboard or touch operation is available. |
| What does this action mean? | The label, grouping and surrounding information make the consequence clear. | The control name and nearby context explain what changes, including whether the order repeats. |
| What happened? | A visible confirmation identifies the saved change. | A concise status message confirms the change and the new order details can be reviewed. |
| Can I recover? | The person can edit or undo the change from a clear route. | Focus and reading position remain predictable; the person can return to the changed field or reverse the action. |
| What does the brand communicate? | The hierarchy makes terms and choices feel clear rather than pressured. | The sequence presents the same terms before action and does not make refusal or reversal harder to find. |

A visually obvious action is not automatically understandable nonvisually. A concise spoken label is not automatically enough context. The job is to make the action, meaning, consequence and result discoverable in the mode the person is using.

Visual-first people often scan before reading closely, satisfice when an option seems likely to work, and muddle through with partial understanding. These are useful hypotheses about behaviour, not universal traits. They make clear hierarchy, familiar language and recoverable actions valuable. Nonvisual-first people may build an overview from headings, regions, labels and state, then jump directly to an item rather than listening from beginning to end. The goal is to support both overview and direct navigation.

---

## Two UX lenses: related questions, different evidence

| Practice area | Visual-first questions | Nonvisual-first questions |
| --- | --- | --- |
| First impression | Can I identify the service, purpose and main route at a glance? | Do I hear or reach the service name, purpose and first useful action without travelling through unnecessary content? |
| Overview | Do hierarchy, grouping, headings and visual emphasis make the page scannable? | Do headings, regions, lists and control signposts create an overview I can navigate directly? |
| Interaction | Are interactive objects distinguishable and do their appearance and behaviour agree? | Does each object identify itself, behave according to its role and communicate its current state? |
| Content | Can I find the information I need without wading through unnecessary copy? | Are the important words first, the context sufficient and the sequence navigable without forced listening? |
| Choice | Are options and consequences visible before I choose? | Do I encounter the relevant terms and consequences before the choice in the order I use? |
| Progress | Can I tell what is selected, loading, complete or still to come? | Are state, progress, result counts, boundaries and important changes announced proportionately? |
| Recovery | Can I see what went wrong and where to correct it? | Can I locate the problem, move to it, understand it, correct it and retain the rest of my work? |
| Brand character | Does the visual system help me recognise the brand without obscuring purpose? | Do language, voice, rhythm, naming and interaction behaviour carry the brand’s character without narrating visual decoration? |
| Confidence | Can I predict an action from its placement, label and appearance? | Can I predict it from its name, role, state, sequence and familiar behaviour? |

These are complementary probes. Neither is a simulation of the other. A static screenshot can help test a visual hierarchy, but it cannot answer how the flow behaves with a keyboard or screen reader. A sighted person temporarily using a screen reader can find obvious issues, but cannot reproduce the strategies, fluency or preferences of someone who uses that technology every day.

---

## Typography is part of interaction design

Typography carries brand character, but it also affects how people identify, scan and read information. The typeface, size, line length, spacing, contrast, hierarchy and responsive behaviour can make a page feel considered or tiring. Type is also a signifier: headings show structure, emphasis signals priority, and consistent styles help people recognise what kind of information they are encountering.

A type choice that is expressive in a campaign may be difficult for sustained reading or small controls. A clean visual system may still make distinctions hard to find if everything uses the same weight and scale. In a nonvisual-first experience, the shape of a typeface may not be received through a screen reader, but the underlying structure still matters: semantic headings, labels, grouping, language and sequence determine whether the person can navigate the content. A person may also switch between speech, Braille and visual display, so typography and structure can both affect the same task.

Treat typography as three related questions:

- **Character:** Does the type express the intended brand tone?
- **Reading function:** Can people identify, read and understand the content in its intended contexts?
- **Delivery:** Does the system preserve the experience as text is enlarged, spaced, translated, reflowed or rendered on different devices?

No named typeface or category is universally easy to read. Evaluate the complete typographic system with realistic content and relevant readers. The [Accessible Typography for UX and Brand Systems guide](https://github.com/Double-FW/Accessible-Typography-for-UX-and-Brand-Systems/blob/main/Accessible_Typography_for_UX_and_Brand_Systems.md) explores these relationships in depth.

**Try:** Take a real content page and compare its visual hierarchy with its heading and region structure. Test at normal and enlarged text, with longer content and a second language if relevant. Ask readers what is clear, tiring, distinctive or difficult; record functional performance and emotional response separately.

---

## A practical UX cycle

The cycle below is deliberately lightweight. It provides a repeatable way to notice problems early and test whether a change helps. Scale the method to the task’s importance, uncertainty, reach and risk.

### 1. Frame the human outcome

Before debating a screen, write down:

- **Person and context:** Who is trying to do this, where, on what device and under what conditions?
- **Purpose:** What are they trying to achieve, decide, understand or refuse?
- **Functional outcome:** What will they be able to do or know when the task is complete?
- **Emotional outcome:** What should the experience help them feel—capable, confident, safe, valued, or something else?
- **Cost of failure:** What happens if the task is misunderstood, delayed, duplicated or lost?
- **Open assumptions:** What are we currently guessing about the person, the context or the interaction?

Keep functional and emotional outcomes distinct enough to test. A person completing a task does not prove that they felt confident; a high satisfaction score does not prove that the task was completed accurately.

### 2. Map the interaction as a story

Describe the journey in plain language before drawing the final interface:

1. How does the person arrive, and what do they need to know first?
2. What are the main actions and alternatives?
3. What information or consequence must be understood before a choice?
4. What does the system do after each action?
5. How can the person pause, cancel, go back or change their mind?
6. What happens on error, delay, empty state or interruption?
7. How does the person know the outcome occurred?
8. If they leave and return, what should be remembered?

This sequence is especially useful for nonvisual-first UX, where the person may build an overview by moving among signposts rather than seeing the whole screen. It also helps visual-first design because a compelling page composition cannot compensate for a broken task sequence. A useful arrival check is: can someone identify the service, page purpose, current section, main actions, search route and way back? On homepages and portals, also ask whether the page explains what the service is, what it offers, what a person can do and why it may be useful, despite competing organisational priorities.

### 3. Audit actions, cues and expectations

For every consequential action, record four things:

| Element | Ask |
| --- | --- |
| Action possibility | What can the person actually do here? |
| Signifier | What tells them that action is available and what it means? |
| Convention | What learned pattern will they expect? Is it shared by this audience and context? |
| Feedback | How will they know the action worked, failed or changed the state? |

Then look for mismatches. Does a link look like a button? Does a button take the person somewhere? Does a card appear clickable but do nothing? Does a visual selected state have a meaningful nonvisual state? Does the cursor or focus location move with the interaction? Do the words remain clear when heard in a list without nearby visual context?

### 4. Prototype to answer a question

Choose a prototype that can answer the question you have.

- Use a sketch or static frame to ask whether the page purpose and visual hierarchy are understood.
- Use a clickable prototype to explore navigation, sequence, signifiers and expected outcomes.
- Use working code when keyboard movement, focus, state, timing, reflow or assistive technology interaction matters.
- Use representative content when testing labels, images, data, comparisons, forms or brand voice.
- Use the participant’s usual device and interaction method when that is central to the question.

A high-fidelity visual prototype cannot answer questions about a screen reader’s sequence. A spoken script cannot answer questions about the actual product’s control behaviour. Avoid asking participants to infer aspects that the prototype cannot represent.

### 5. Observe realistic tasks

Write tasks around a believable goal, not the route you expect someone to follow. For example:

> You are going away next week and the order is due to arrive while you are out. Change the delivery so it arrives when you can receive it, then check whether the recurring schedule has changed too.

This leaves room to notice how people interpret the product. It does not tell them to select a specific menu, button or label.

Invite a small, varied set of relevant participants for formative testing. Include people who use the product and people whose interaction methods or circumstances are relevant to the question. For nonvisual-first work, recruit people who use their preferred combination of speech, Braille, keyboard, touch or voice; do not require everyone to use the same setup. For visual-first work, consider scanning, high zoom, contrast preferences, small screens and distraction as appropriate to the context.

Ask participants what they notice and expect, but do not make continuous “think aloud” narration a condition of participation. It can change behaviour or add effort. Offer pauses, retrospective questions and other ways to share an experience. Facilitate neutrally: do not teach, defend the design or signal a preferred answer. If clarification is needed, ask about the participant’s goal rather than directing them to the route.

### 6. Record what happened and what it meant

For each task, capture separately:

- completion and accuracy;
- time or interaction effort where relevant;
- hesitation, backtracking, errors and requests for help;
- whether the person understood the choices and consequences;
- whether work and position were retained;
- whether the person could recover;
- the participant’s explanation of what they expected;
- reported confidence, frustration, relief or uncertainty; and
- the mode, device and context used.

Do not infer emotion solely from a pause, expression or task success. Ask the person. Do not interpret one participant’s preferred solution as a universal requirement. Research helps the team understand needs and barriers; design judgement still matters.

A few formative sessions can reveal a serious issue and help the team explore why it occurs. They cannot establish how common that issue is across a population. Surveys, analytics and controlled experiments answer different questions and need appropriate samples, measures and interpretation. A survey can tell you what respondents report; it does not by itself show why a control was confusing. An A/B or multivariate test can compare outcomes when the sample and instrumentation support it; it does not replace observation or establish that an experience works for every group.

### 7. Prioritise by consequence, not only frequency

When reviewing findings, consider:

- Does the issue block a meaningful task or compromise a decision?
- Could it cause financial, privacy, safety or emotional harm?
- Can the person understand and recover from it?
- Which people, devices or contexts are affected?
- Did it arise from a repeated pattern or a single severe failure?
- Is the cause local, or does it point to a shared design-system or content problem?

A problem seen once in a small study may still be severe if it completely blocks a group from acting. A frequently repeated minor hesitation may deserve attention too, especially if it accumulates across a long service. Do not treat frequency in a small sample as prevalence.

### 8. Make the smallest effective change

Change the design at the level where the problem originates. If a control has an unclear name, a label may solve it. If every step assumes a two-dimensional overview, changing labels one at a time may not be enough; the information architecture or interaction model may need work.

The smallest effective change is not always the smallest code change. It is the smallest change that addresses the cause without creating a new burden elsewhere. Preserve what people have learned when possible, but do not use familiarity to defend a pattern that repeatedly fails them.

### 9. Retest the changed experience

Retest the task or uncertainty that motivated the change, using a prototype or live product that can reveal the relevant behaviour. Check that the improvement works in both lenses and does not remove meaning, choice or recovery. For a significant live change, combine qualitative evidence with suitable quantitative measurement where it can answer a real question.

There is no universal requirement to test on a fixed monthly cadence or to run an experiment after every change. Retest when evidence, risk, change size or user feedback makes it valuable. The useful discipline is to close the loop: make a change, learn whether it helped, and revise if it did not.

---

## Ten principles translated into UX practice

Each principle below connects a design intention with a practical way to inspect it. Use the questions as prompts, not as a scorecard.

### 1. Innovation should create meaningful capability

**UX practice:** Explain what new action or reduced effort the innovation provides. Prototype the discovery and recovery as well as the ideal use.

**Visual-first probe:** Can a person recognise the new action without relying on an animation that disappears or an unexplained icon?

**Nonvisual-first probe:** Can someone discover the action from names, structure and familiar behaviour? Can they check what the system understood and undo a mistake?

**Try:** Give a participant the goal but not the feature instructions. Observe whether the new interaction helps or adds a learning burden.

### 2. Usefulness is the primary test

**UX practice:** Start with the task and its value to the person. Do not let feature exposure or conversion become a substitute for task success.

**Visual-first probe:** Can someone find the main task in a page where business priorities compete?

**Nonvisual-first probe:** Can someone find, complete and verify the same task independently and privately?

**Try:** Follow one task from arrival through result, including error and return paths. Record where effort is created and who carries it.

### 3. Aesthetic quality should support use

**UX practice:** Treat brand expression as a way to make an experience coherent and meaningful, not as decoration pasted over function.

**Visual-first probe:** Does type, hierarchy, contrast, imagery and motion express character while helping people understand?

**Nonvisual-first probe:** Do language, voice, timing, naming and interaction rhythm carry a considered character without turning visual detail into unnecessary speech?

**Try:** Remove the logo and campaign copy from a prototype. Ask what character remains in the service’s behaviour. Then examine whether the visual and nonvisual experiences tell a compatible story.

### 4. The product should make itself understandable

**UX practice:** Design the person’s mental model through consistent names, groupings, sequence, mappings and feedback.

**Visual-first probe:** Do visual signifiers agree with what happens when an element is activated?

**Nonvisual-first probe:** Does each object identify itself, its purpose, current state and relationship to the task? Can a person obtain an overview without hearing every detail?

**Try:** Ask a participant to predict what a control will do before using it. Compare the prediction with the actual result.

### 5. The product should respect attention

**UX practice:** Remove needless interruption and repetition while preserving meaningful alerts, status and orientation.

**Visual-first probe:** Is everything competing for attention, or does hierarchy help someone scan and decide?

**Nonvisual-first probe:** Can someone bypass repeated navigation, move directly among useful signposts and hear changes in proportion to their importance?

**Try:** Review a common route for every prompt, announcement, modal, repeated label and required wait. For each one, ask what person-centred job it performs.

### 6. The service should be honest

**UX practice:** Put the real terms, costs, uncertainty and consequences before the choice. Make refusal, cancellation and correction understandable.

**Visual-first probe:** Are visual emphasis and order helping people compare choices or steering them towards the organisation’s preferred outcome?

**Nonvisual-first probe:** Are options, preselection, terms and consequences equally clear in the order a person receives them?

**Try:** Read the journey only in order—without looking back. Can someone make an informed decision before acting?

### 7. The product should preserve useful familiarity over time

**UX practice:** Treat people’s learned language, routes and shortcuts as part of the experience. Change them when evidence justifies it, and help people adapt.

**Visual-first probe:** Does a redesign move or restyle familiar controls in a way that disrupts recognition?

**Nonvisual-first probe:** Have names, sequence, keyboard commands or object roles changed in ways that invalidate learned routes?

**Try:** Compare a familiar task before and after a change. Ask returning users what knowledge carried over and what they had to relearn.

### 8. Care should reach every detail

**UX practice:** Design empty, loading, error, timeout, confirmation and recovery states as deliberately as the ideal journey.

**Visual-first probe:** Can someone see what failed, where to act and whether work remains saved?

**Nonvisual-first probe:** Does attention move to new content, is the error located and explained, and does the person return to a sensible point after closing it?

**Try:** Interrupt the journey at a consequential point, then return. Observe what is retained and what the person must reconstruct.

### 9. The product should consider its environmental cost

**UX practice:** Consider performance, data, battery, device lifespan and attention as part of the experience.

**Visual-first probe:** Do heavy assets, motion and automatic playback slow or distract from the task?

**Nonvisual-first probe:** Do downloads, repeated announcements, background activity or long unbounded sequences impose avoidable time and energy costs?

**Try:** Test the key journey on an older capable device or constrained connection. Identify which costs provide value to the person and which are avoidable.

### 10. Use as little design as possible

**UX practice:** Remove friction and duplication without removing meaning, context, choice or recovery.

**Visual-first probe:** Does the desire for a sparse page remove useful labels, boundaries or wayfinding?

**Nonvisual-first probe:** Does concise language remain clear when a control is heard independently? Are visual states translated into meaningful state rather than omitted?

**Try:** For each element proposed for removal, ask what work it currently does for the person and what will replace that work.

---

## Practical stems for briefs, research and design review

These sentence starters make it easier to apply the ideas without turning them into slogans.

### Brief and outcome stems

- “The person is trying to **[goal]** while **[context or constraint]**.”
- “A successful outcome means the person can **[observable result]** without **[avoidable effort, risk or dependency]**.”
- “The experience should help the person feel **[emotion]** because **[specific behaviour of the product]**.”
- “The assumption we need to test is **[assumption]**; it matters because **[consequence if wrong]**.”
- “This design decision is easiest for **[who]** and may transfer effort to **[who or which situation]**.”
- “The person should be able to recover by **[route]**, without losing **[work, time, privacy or context]**.”

### Task stems for usability sessions

- “Imagine you need to **[goal]** because **[plausible context]**. Show me how you would approach it.”
- “You are comparing **[options]**. Decide which one fits **[need]**, and tell me what information affected your choice.”
- “Something has changed: **[situation]**. Find out what happened and decide what you would do next.”
- “You made a mistake in **[low-risk scenario]**. Correct it and continue without starting again.”
- “You have reached this page from a message. Work out where you are, what service this is and what you can do here.”
- “Use the device and interaction method you would normally choose. Tell me if the prototype prevents you from doing that.”

Do not put the expected label or route into the task unless the study is specifically measuring recognition of that label. Test the task wording with a colleague before using it; unclear instructions can create false findings.

### Neutral follow-up question stems

- “What were you expecting to happen?”
- “What made you choose that?”
- “What did that message mean to you?”
- “What would you do if I were not here?”
- “How would you know the change had been saved?”
- “What information would you still need before deciding?”
- “Was there a point where you were unsure, and what were you unsure about?”
- “What, if anything, made this feel easier or harder?”
- “Would you prefer to listen, use Braille, or move between them for this task?”

Avoid “Was that easy?” as the only follow-up. It encourages a simple judgement without exposing the cause. Do not ask a participant to justify why they did not follow the intended path; ask what they were trying to achieve and what the design communicated.

### Design-review stems

- “The action this element affords is **[action]**; the signifier that communicates it is **[cue]**.”
- “We are relying on the convention **[pattern]**. Which users or contexts might not share it?”
- “The visual cue is **[cue]**. What communicates the same meaning nonvisually?”
- “The product changes from **[state]** to **[state]**. What feedback tells the person this happened?”
- “The brand wants to communicate **[character or promise]**. What does the interaction itself communicate?”
- “This element adds **[time, decision, distraction or data]**. What value does it provide to the person?”
- “If we remove this, the person may have to **[infer, remember, ask, repeat or recover]**. Is that acceptable?”
- “This works for the person using **[mode/device]**. What evidence do we have for **[other relevant mode/context]**?”

---

## AI-assisted UX review: useful analysis with visible limits

An AI system can help teams inspect a journey, compare wording, identify inconsistent names, draft realistic task prompts, map actions to cues, and organise observations. It can make a review easier to repeat. It cannot infer what a participant felt from a screenshot, establish how common a barrier is from a few sessions, or stand in for people who use speech, Braille, magnification, voice control or other methods in daily life.

Give an AI the journey, task, intended outcomes, available evidence and known limits. Ask it to separate direct observations from interpretations and recommendations. Require a human to check consequential design changes and any claims about user preferences or group impact.

A reusable prompt:

> Review this UX journey for the task **[task]** in the context **[device, setting, constraints]**. The intended functional outcome is **[outcome]** and the intended emotional outcome is **[outcome]**. Examine it from visual-first and nonvisual-first perspectives. For each finding, report: (1) the specific screen, step or content; (2) evidence supplied versus assumption; (3) what action is possible; (4) the visual and nonvisual signifiers; (5) the conventions relied on; (6) mapping, feedback and recovery; (7) the likely functional and emotional consequence; and (8) the smallest useful test or change. Do not infer a participant’s emotion, disability, preference or the prevalence of a problem. Mark missing evidence and questions for user research.

Treat the output as a set of hypotheses. Verify it against the actual product, implementation and participant evidence before changing a decision.

---

## A 45-minute multimodal design exercise

Use this exercise when a team is stuck debating taste, conventions or whether an interaction is “obvious.” It works with a real flow, a prototype or a service already in use.

### 1. Choose a consequential task — 5 minutes

Write a single task people need to complete. Choose one where a misunderstanding, delay or error has a meaningful consequence.

### 2. Map the person’s story — 10 minutes

On one page, describe arrival, purpose, choices, consequences, action, result and recovery. Mark what the person needs to know at each point.

### 3. Mark the cues — 10 minutes

For each action, name:

- the action possibility;
- its visual signifier;
- its nonvisual signifier;
- the convention it relies on; and
- the feedback after activation.

Circle any place where the cue, actual behaviour and expected outcome disagree.

### 4. Run two walkthroughs — 10 minutes

One person walks the flow from a visual-first perspective, describing what they scan, notice and infer. Another walks it from a nonvisual-first perspective, describing what they need to hear, navigate or understand. Neither should imitate a disability. The second walkthrough is a hypothesis-generating exercise, not a substitute for testing with nonvisual participants.

### 5. Identify the indifference risk — 5 minutes

Ask: “Whose reality did we assume? Who carries the cost if this assumption is wrong? What would make the experience feel considered?”

### 6. Choose an evidence-gathering action — 5 minutes

Decide what to do next: recruit a participant, change the prototype, inspect content, test a different input method, review a convention with customers, or measure a live outcome. Assign an owner and record what evidence would change the decision.

---

## Evidence, interpretation and limits

The supplied sighted UX perspective is useful for generating hypotheses about scanning, visual hierarchy, satisficing, muddling through, visual noise, goodwill and lightweight testing. These are not universal traits of all sighted users. Treat them as questions to investigate in a particular task and context.

The supplied nonvisual perspective is especially useful for designing purpose before detail, meaningful signposts, stable sequence, object names, state, attention movement, proportionate announcements, direct routes, finite sets, meaningful descriptions, comparison, recovery and choice of speech or Braille. It is written from one first-person experience. Other blind people may use different strategies, tools and preferences, and people may switch modes over time.

Use research methods for the claims they can support:

- **Formative task observation** can reveal how a design is interpreted, where people hesitate and what helps them recover. Small samples do not establish prevalence.
- **Interviews and open comments** can explain experiences and expectations but should not be treated as a measure of how often they occur.
- **Surveys** can capture reported confidence, effort or satisfaction when questions and recruitment are sound. They need to be usable by the people whose experiences they represent.
- **Analytics** can show patterns in product behaviour, but do not explain why those patterns occur or reveal every person who abandoned the task.
- **A/B or multivariate experiments** can compare defined alternatives on selected outcomes when the design, sample, data quality and analysis support that comparison. They do not prove that a design works for everyone or explain the whole experience.
- **Assistive-technology and interaction testing** can expose problems in real behaviour. It should include people who use the relevant methods, particularly when decisions depend on their experience.

Keep observation, interpretation and decision separate in notes. For example:

| What happened | What the participant said | Possible interpretation | What we will test next |
| --- | --- | --- | --- |
| The person returned to the previous section twice. | “I wasn’t sure whether the date applied to one order or all future orders.” | The scope of the change is unclear. | Test revised wording and confirmation with recurring and one-time orders. |

This makes it harder for a team to turn a single reaction into an unsupported universal rule, while ensuring that a serious barrier is not dismissed because it appeared infrequently.

---

## The standard of care

UX practice is not improved by asking whether the interface is merely usable in the ideal setting. Ask whether people can understand and act in the settings they actually inhabit; whether the service respects their chosen methods; and whether the interaction earns the emotional response the brand claims to value.

Conventions help people bring knowledge with them. Affordances define what actions are possible. Signifiers make those possibilities discoverable. Feedback and mapping help people understand the result. Brand and emotion shape what the repeated interaction means to them. Research keeps the team from treating its own assumptions as the user’s reality.

Taken together, these practices make good UX less dependent on guesswork. They help a team turn human attention into concrete design decisions, then check whether those decisions improve the experience for people using the product in different ways.

## Related work

The guide is informed by the supplied *UX Principles and Methods* (sighted perspective) and *Don’t Make Me Construct the Interface* (congenitally blind perspective), alongside the related Rams and brand-experience work.

- *Ten principles for good digital product design: Reframing Dieter Rams for multimodal human experience*
- *Indifference: the cardinal sin in design*
- [POUR reframed as brand experience outcomes](https://github.com/Double-FW/POUR-for-Branding-Systems-and-CX/blob/main/The%20WCAG%20POUR%20principles%20reframed%20through%20emotional%20outcomes%20for%20branding%20systems.md)
- [Accessible Typography for UX and Brand Systems](https://github.com/Double-FW/Accessible-Typography-for-UX-and-Brand-Systems/blob/main/Accessible_Typography_for_UX_and_Brand_Systems.md)

## Sources for UX concepts

- Don Norman, [“Signifiers, not affordances”](https://jnd.org/signifiers-not-affordances/).
- Don Norman, [“Affordances and Design”](https://jnd.org/affordances-and-design/).
- Don Norman, [“Affordance, Conventions and Design (Part 2)”](https://jnd.org/affordance-conventions-and-design-part-2/).
- Don Norman, [Preface to *The Design of Everyday Things*, revised edition](https://jnd.org/preface-design-of-everyday-things-revised-edition/).
