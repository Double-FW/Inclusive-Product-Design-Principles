# UX Principles and Methods

This is a practical philosophy of reducing avoidable effort. Not a formal design methodology in the same sense as human-centred design, cognitive walkthroughs or standards-based accessibility testing. Instead, this should provide memorable principles and lightweight practices that help an LLM notice when an interface might make a user hesitate.

I am writing from the perspective of a sighted person. I can visually scan a page, notice differences in size, colour, spacing and position, and use those visual signals to understand its structure. That experience is not universal. I therefore need to ask whether the same meaning is available to someone who does not see the page as I do, or does not see it at all.

There are two different parts of the same problem:

- How I encounter and navigate websites and interfaces.
- Lightweight usability testing approaches.

## 1. Invisible usability

I may need to compare products, understand information or make an important decision. Those are meaningful parts of my task.

The problem arises when the interface makes me ask unnecessary questions:

- Is this clickable?
- What does this label mean?
- Which option applies to me?
- Where am I in the site?
- Is this the main navigation?
- Did my action work?
- How do I go back?
- Are these two links different?
- is that a button or a link?

Each unanswered question uses some of my attention. One moment of uncertainty may be minor, but repeated uncertainty creates friction, fatigue and loss of confidence.

> Do not make me spend attention understanding the interface when I need that attention for my actual task.

I see a clear connection with cognitive accessibility here, although this is primarily used as a broad usability principle rather than a complete account of disability.

## 2. I want an interface to be self-evident or self-explanatory

If an interface is self-evident, I can understand it almost immediately. Its controls, structure and language behave as I expect.

Where that is not possible, I want it to be self-explanatory. I may have to look briefly, but I should be able to work it out without consulting instructions, experimenting repeatedly or possessing specialist knowledge.

This leads me to expect that:

- links and controls will look interactive;
- labels will use language I recognise;
- similar things will look and behave similarly;
- different things will be distinguishable;
- the visual hierarchy will show me what matters most;
- the result of my action will be apparent; and
- instructions will appear where and when I need them.

Novelty that is not aligned with a UX or branding system often comes with a business cost. If a design asks me to learn an unfamiliar interaction, the value of that interaction should justify the additional effort.

## 3. I do not use interfaces as designers may imagine

I may be an attentive and thoughtful person, but I do not approach every page as if I were studying it.

### I scan before I read

I often scan a page for words, shapes and options that appear relevant to my immediate goal. I do not necessarily begin at the top, read every sentence and build a complete understanding before I act.

Because I am sighted, I am likely to notice:

- familiar words;
- headings;
- short blocks of text;
- visually prominent controls;
- language related to my task; and
- familiar patterns such as navigation bars and search fields.

This supports concise writing and a strong visual hierarchy, but I would not turn it into the claim that I never read. I read closely when the content matters. Scanning helps me decide what deserves that closer attention.

My way of scanning is also specifically visual. A blind person using a screen reader may scan through headings, landmarks, links or form controls instead. Someone using magnification may see only a small part of the page at a time. The broader requirement is therefore not merely to make a page visually scannable, but to make its structure efficiently navigable in different ways.

### I satisfice

I often choose the first option that seems likely to work rather than evaluating every possibility to identify the ideal one.

I may do this because:

- evaluating every choice takes time;
- the consequences of a wrong click appear small;
- I expect to be able to go back; or
- I am focused on completing my task rather than understanding the entire system.

A label therefore does not need to describe an organisation’s internal structure perfectly. It needs to be recognisable enough for me to choose it with reasonable confidence.

### I muddle through

I frequently use products without fully understanding how they work. I form partial explanations, remember routes that succeeded previously and repeat actions that appear effective.

I do not regard this as my failure. A design should not depend on me constructing the correct mental model before I can succeed.

At the same time, “I can probably muddle through” should never be used to excuse a preventable barrier, an inaccessible interaction or misleading content. My ability to recover as a sighted mouse user does not demonstrate that everyone else can recover.

## 4. I use visual hierarchy to infer meaning

As a sighted person, I use visual design as part of the communication. Before I read every word, I look for clues about:

- what the page is about;
- which elements belong together;
- what is most important;
- what I can act upon; and
- what is secondary or supplementary.

I rely on conventions I already understand. I generally interpret larger headings as introducing broader sections, underlined text as a link and controls that look like buttons as things I can activate.

Conventions reduce the amount I need to learn. A designer can depart from them, but the departure should be deliberate and should remain understandable.

However, visual hierarchy is only one representation of structure. If a heading merely looks like a heading, or a region is communicated only through visual position, the structure I perceive may be absent for someone using a screen reader. I therefore need the same relationships to be represented through headings, landmarks, lists, labels and control semantics.

## 5. I want pages divided into clearly defined areas

I find a page easier to understand when its major regions are distinct. I want to recognise the navigation, primary content, supplementary information and page-level actions without inspecting every item.

This supports:

- meaningful headings;
- page regions and landmarks;
- grouping related controls;
- consistent layouts;
- separation of primary and secondary actions; and
- progressive disclosure.

Because I am sighted, colour, whitespace, borders and position may help me recognise those areas. I cannot assume those visual divisions are sufficient. Someone navigating through a screen reader, keyboard, magnification or voice control needs equivalent structural clarity.

## 6. I want interactive things to be unmistakable

I do not want to test an object merely to discover whether it is interactive.

I experience ambiguity when:

- clickable and non-clickable text look alike;
- buttons are styled as plain text;
- links are styled as buttons;
- a furniture image look like an interactive object;
- a decorative-looking card unexpectedly acts as a link;
- hover is the only indication of interactivity;
- an icon has no visible understandable label; or
- a disabled control looks active.

I do not interpret this principle as “make every control look like an old-fashioned button.” I interpret it as a requirement for reliable signifiers. Appearance, wording, placement, focus behaviour and response should collectively tell me what I can do.

I also need to remember that some signals available to me, such as visual shape, colour and hover feedback, may be absent or different for another person. The control’s accessible name, role, state and keyboard behaviour must carry equivalent meaning.

## 7. I am affected by visual noise

I find it harder to understand a page when:

- everything competes for my attention;
- too many elements are emphasised;
- the grouping is unclear;
- decoration resembles functionality;
- too much content is presented at once; or
- visual elements resemble controls but do nothing.

When everything is prominent, nothing feels prominent. I have to do the work of deciding what matters.

I do not equate this with a demand for minimalism. A visually sparse page can still be confusing. If labels, instructions, boundaries or persistent navigation are removed in pursuit of visual simplicity, the effort may simply be transferred back to me. My objective is clarity, not aesthetic emptiness.

## 8. I value the removal of needless words

Remove words that do not contribute to understanding or action. I find pages harder to use when they contain:

- introductory waffle;
- self-congratulatory marketing copy;
- unnecessary instructions;
- explanations of things that should already be apparent; or
- institutional language or jargon that does not match the words I would use.

Removing needless words can help me:

- scan more efficiently;
- find useful information;
- notice important instructions;
- move through a page; and
- feel more confident that I have understood it.

However, I do not confuse concision with comprehension. Very short labels can be ambiguous, particularly when I am unfamiliar with a service. “Submit,” “Continue” and “Learn more” may use few words while telling me too little.

My interpretation is therefore: remove words that do no useful work, but retain the words I need to understand the choice, its consequences and what will happen next.

## 9. I expect navigation to answer persistent questions

Website navigation should feel similar to finding my way through a physical environment. As I move through a site or service, I want to know:

- What site or service is this?
- Where am I?
- What are the main sections?
- What can I do here?
- Where have I already been?
- How can I search?
- How can I return to a known point?

I therefore value:

- a visible and understandable site identity;
- persistent primary navigation;
- a clear page name;
- an indication of the current section;
- useful local navigation;
- breadcrumbs where the hierarchy justifies them; and
- consistent placement, presentation and terminology.

If I were dropped into an internal page without seeing how I arrived, could I quickly identify the site, page, section, available navigation and route back towards the top?

As a sighted person, I may answer those questions through the whole visual composition of the page. To extend the test inclusively, I should also attempt it at high zoom, with keyboard navigation, with styles removed and through a screen reader’s headings and landmarks list.

## 10. I recognise that a homepage or portal page have competing jobs

I expect a homepage or portal page to do several things at once. They may need to:

- identify the organisation or service;
- explain its purpose;
- expose important content;
- provide navigation;
- support search;
- promote current priorities;
- establish credibility; and
- help both new and returning customers.

When every internal stakeholder fights for visual prominence, I may encounter a page where everything is emphasised and the overall purpose becomes unclear.

The questions I want a homepage to answer quickly are:

- What is this?
- What does it offer me?
- What can I do here?
- Why might I choose it?

I apply the same reasoning to landing pages, app dashboards and service start pages.

## 11. I distrust universal claims about what users like

I am cautious when I hear claims such as:

- I do not like scrolling;
- I prefer dropdown menus;
- everything should be within three clicks;
- I never read instructions; or
- I will understand a familiar-looking icon.

My preferences and behaviour depend on my context, task, experience and the quality of the particular implementation. I would rather see a representative design tested than settle the matter through abstract argument, or through using data that does not come from customers and is not statistically significant.

Replace opinion about users with observation of use, and evidence vale for customers through segmental quantitative data.

Observation still requires interpretation. Watching three participants struggle may show me that a problem exists. It does not tell me how prevalent that problem is across a population.

Four users from the same demographic do not represent that demographic in your customer base, so use the qualitative insights to inform design choices and then use quantitative customer data to optimise them.

## 12. I have a limited reservoir of goodwill

Good experiences may preserve or replenish it; frustrating experiences consume it.

My goodwill is drained when a service:

- hides information I need;
- asks me for unnecessary personal information;
- makes a common action difficult;
- punishes me for a minor formatting error;
- uses language built around its organisation rather than my task;
- appears deceptive;
- does not use common labelling conventions;
- presents me with double negative options;
- does not use the pop out effect to signpost key messaging or functionality;
- fails to explain important consequences; or
- provides inadequate help.

My goodwill is supported when a service:

- anticipates my likely questions;
- makes key information easy to find;
- lets me recover from mistakes;
- is transparent about effort and consequences;
- explains failures clearly; and
- offers practical assistance.

I find the metaphor useful, but it can conceal differences between people. I may arrive with ample attention and energy on one day and very little on another. Someone experiencing pain, fatigue, anxiety, cognitive overload or repeated accessibility barriers may begin with less capacity available. Inclusive design should not assume that I—or anyone else—has an unlimited reserve.

## 13. I can choose a research method that fits the question

Usability research can be proportionate without being casual. I first decide what uncertainty or decision the work needs to address.

1. Define the person's task, context, stakes, and the decision the research will inform.
2. Choose a method suited to the question: task observation for how an interaction works, interviews for reported experience, a survey for structured self-report, analytics for behavioural patterns, or a controlled experiment for a defined comparison.
3. Recruit people whose experience is relevant to the question. Make participation accessible, voluntary, and privacy-conscious.
4. Use realistic tasks and the person's usual interaction methods where possible. Avoid teaching the intended route if discovery is what I am evaluating.
5. Record what happened separately from what participants said and from my interpretation.
6. Report the method, context, evidence, limitations, unresolved questions, and proposed next action.
7. Repeat or deepen the research when the stakes, change, uncertainty, or new evidence justify it.

A/B or multivariate testing is one possible method, not a requirement for every usability study. Use an experiment only when the question, alternatives, outcome measure, design, sample, and ethical context support a meaningful comparison. There is no universal monthly testing cadence.

## 14. I can learn from a few people without overstating the evidence

A small formative study can reveal possible barriers, misunderstandings, and recovery problems. It does not, by itself, show how common an issue is in a customer population.

Surveys can collect reported confidence, effort, or satisfaction when the questions, recruitment, accessibility, and analysis fit the purpose. A survey score is not a substitute for observing task performance or understanding why people responded as they did. Any population estimate or group comparison needs a design and sample that support that claim.

Research findings do not by themselves demonstrate legal compliance or prove that a product is fully accessible. Use relevant standards evaluation, assistive-technology checks, and research with people for the questions each can answer.

If I use a satisfaction score, I treat it as one signal and interpret it alongside task outcomes, access barriers, and participants' explanations. A higher score may be encouraging; it does not prove that a brand values all customers or that everyone had a good experience.

Optional open-text comments can add context when the survey is accessible and privacy is protected. I should explain how comments will be used and avoid collecting personal information that is not needed.

## 15. I can test early and test unfinished work

I do not need to wait for a finished product. I can use qualitative research to test:

- sketches;
- paper prototypes;
- wireframes;
- competitor products;
- partially implemented interfaces; or
- live services.

Even an unfinished design can show me whether small varied or specific groups of people understand the proposition, terminology, structure and intended route.

This moves testing from final validation or ongoing optimisation into design. If I wait until the product is complete, my team may be emotionally and financially invested in defending it. When I test earlier, change is usually cheaper and politically easier.

An early visual prototype still has limitations. If I show a sighted participant a static image, I cannot infer how the eventual experience will work with a keyboard, screen reader, voice control or reflow. I need prototypes appropriate to the questions I am asking.

## 16. I write realistic tests without revealing the route

When I write a qualitative test task, I describe the participant’s goal rather than prescribing the interaction, and where appropriate I use the quantitative satisfaction score data to identify what tasks need investigation and for what group of users.

Instead of telling someone to select “Manage account” and change their postal address, I give them a believable reason to update the address and ask them to show me how they would do it.

I try to make each task:

- clear about the goal;
- plausible in context;
- free from the exact words used by the intended control;
- neutral about the route;
- open enough for the participant to decide where to begin; and
- safe from unnecessary disclosure of sensitive personal information.

I also test my task wording. If my instructions are ambiguous, I may wrongly attribute the resulting confusion to the interface.

## 17. I facilitate neutrally, but I do not have to remain silent

As a facilitator, I am trying to understand what the participant notices, interprets and expects.

I may ask:

- What are you looking at?
- What do you think that means?
- What do you expect to happen?
- What are you trying to do?
- What would you do next?

I avoid:

- teaching the interface;
- defending design decisions;
- signalling approval or disappointment;
- leading the participant towards the intended route; and
- treating the participant as if I were examining them.

I am testing the product, not the person.

I also recognise that a conventional “think aloud” method may not suit everyone. Continuous verbalisation can change behaviour and may disadvantage someone who processes language differently. I should offer alternative ways for participants to communicate what they notice and experience.
Make notes of emotional changes as well as functional approaches and outcomes. Frustration, surprise, relief and other responses are all useful indicators.

## 18. I learn by observing directly

I want designers, developers and decision-makers to observe sessions directly. Seeing the difference between what my team expected and what a participant actually experiences can be more persuasive than reading a long report.

While I observe, I record problems rather than trying to redesign the product during the session. I watch for:

- where the participant hesitates;
- what they overlook;
- what they misinterpret;
- what they expect;
- whether they can recover; and
- what prevents completion.

Because I am sighted, I must be careful not to record only visible behaviour. A participant may be exerting considerable cognitive effort without displaying it. A screen-reader user may be navigating effectively through information I cannot infer from looking at the screen. I need to listen to the participant, understand their interaction method and capture the barrier rather than merely its visible symptoms.

A visible struggle is evidence of a problem, but the participant’s suggested solution is not automatically the right design solution. Research reveals needs and barriers; I still need to exercise design judgement.

## 19. I debrief promptly and prioritise carefully

After the sessions, I debrief while observations are fresh. I prioritise issues by the task they affect, the consequence of failure, the evidence available, and the uncertainty that remains.

I consider:

- whether the issue blocks an important task or creates avoidable dependence;
- the severity and reversibility of its consequences;
- which contexts, people, and interaction methods may be affected;
- how well the observation and interpretation are supported; and
- what follow-up evidence or change would be useful.

Frequency is not the same as severity. A barrier seen once may have serious consequences, but one observation does not establish its population prevalence. I should neither dismiss a serious barrier because it appeared once nor infer its scale without suitable evidence.

Accessibility includes applicable obligations as well as user experience. I distinguish standards conformance, functional outcomes, and reported experience, then choose proportionate follow-up. A quantitative experiment may be useful for a specific comparison when its design supports that question; it is not mandatory for every live issue.

## 20. I look for the smallest effective change

I do not assume that every usability finding requires a redesign. I first look for the smallest change that adequately addresses the observed problem.

This can support:

- quicker iteration;
- clearer cause and effect;
- reduced implementation risk;
- more frequent retesting; and
- less organisational resistance.

However, I do not use incrementalism to avoid structural problems. If repeated local defects originate in an inaccessible design system, weak AI governance or flawed information architecture, I may need to address the underlying system.

## 21. I keep reporting proportionate

For formative work, I can share observations, a short prioritised issue list, and clear actions instead of producing a long report. I record enough context and evidence for another person to understand how a conclusion was reached.

I need stronger traceability when decisions concern a regulated service, procurement, accessibility conformance, longitudinal research, or accountable AI governance. In those cases, I connect the relevant tasks and methods to evidence, findings, recommendations, decisions, owners, and unresolved risks.

An AI may help draft a research proposal or compare options. A human must authorise participant contact, live-user experiments, access to identifiable research data, live service changes, and acceptance of material risk.

## 22. This approach helps me or the AI:

- make usability understandable to non-specialists;
- replace opinion with observation;
- test early and frequently;
- focus on serious barriers;
- reduce unnecessary documentation;
- involve the delivery team;
- provide fixes quickly before they become business issues;
- provide more robust evidence;
- treat confusion as a design problem; and
- use ordinary language.

This approach is operational because it makes it easier for me to begin testing instead of waiting for ideal conditions.

## 23. Where I need to extend this methodology

This is not a complete inclusive-design or accessibility methodology. I need to combine it with relevant work such as:

- research with disabled and neurodivergent participants whose experiences relate to the question;
- assistive-technology and platform testing, including WCAG evaluation where applicable;
- testing at high zoom, with text reflow, keyboard, switch, voice, touch, and other relevant input methods;
- consideration of cognitive and communication access;
- attention to changes in capacity related to fatigue, pain, medication, environment, or fluctuating conditions;
- recruitment that reflects relevant intersections of access needs, identities, and circumstances;
- analysis of exclusion and consequential barriers, not inconvenience alone; and
- named accountability for barriers that remain unresolved.

The EAA's Annex I describes functional performance criteria for determining accessibility requirements in its legal context. It is not, by itself, a population segmentation scheme or a requirement that every research study use statistical significance testing. Use demographic or functional grouping only when it is relevant, lawful, privacy-conscious, and supported by the research design.

Qualitative and quantitative methods answer different questions. Qualitative work can explain how or why an experience unfolds; quantitative methods can estimate patterns or compare defined outcomes when sampling, measurement, and analysis justify those claims. Neither method automatically determines product direction or proves impact.

## A deeper philosophy that applies to all human beings:

1. **My attention is limited.** An interface should not waste it on unnecessary interpretation.
2. **Observation is more reliable than speculation.** I should watch people attempt meaningful tasks.
3. **Qualitative research informs design approaches, whereas quantitative research provides evaluation.** I should use an appropriate research methodology for the research test, and ensure impact, optimisation, AI autonomy and the direction for future research is determined by quantitative customer research data.
4. **Iteration is more useful than delayed perfection.** I should find serious problems, improve them and test again.

From my sighted perspective, it would be easy to apply these principles only to what I can see. That would preserve one of the assumptions inclusive design needs to challenge. I therefore extend the central question. I do not ask only whether the interface makes me stop and puzzle over it. I also ask:

- Who has the design assumed its user to be?
- Is my sighted way of scanning the page being treated as the default?
- Whose effort is being regarded as acceptable?
- Can everyone perceive the information needed to make the decision?
- Does “simple” for me create ambiguity or exclusion for someone else?
- Does the interface merely make me hesitate, or does it prevent another person from acting?
- Have we tested with people whose ways of perceiving, processing and interacting differ from mine?

