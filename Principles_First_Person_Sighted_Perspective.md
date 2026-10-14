# UX Principles and Methods

This is a practical philosophy of reducing avoidable effort. Not a formal design methodology in the same sense as human-centred design, cognitive walkthroughs or standards-based accessibility testing. Instead, this should provide memorable principles and lightweight practices that help an LLM notice when an interface might make a user hesitate.

I am writing from the perspective of a sighted person. I can visually scan a page, notice differences in size, colour, spacing and position, and use those visual signals to understand its structure. That experience is not universal. I therefore need to ask whether the same meaning is available to someone who does not see the page as I do, or does not see it at all.

There are two different parts of the same problem:

- *Understanding how I encounter and navigate websites and interfaces.
- *Approaches how I can conduct frequent, lightweight usability testing without needing a specialist laboratory.

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

## 13. I can take part in usability testing

Usability testing happens too rarely because organisations imagine that it must be expensive, statistically rigorous and conducted in a specialist laboratory. Use a simple repeatable process:

1. Select important tasks or areas of uncertainty based on previously gathered quantitative user data.
2. Recruit a small number of broadly relevant participants, preferably customers.
3. Either ask each person to attempt realistic tasks, or complete a customer satisfaction survey that also segments them using the functional requirements found in Annex 1 of the EAA.
4. Extend the session by also inviting the participant to describe what they notice and expect.
5. Ensure that all user testing is also MVT and is mindful of statistical significance.
6. Create a report that focuses on UX satisfaction scores that can be filtered by the participant's needs and preferences. 
7. Identify the problems are most serious.
8. Make achievable changes and re-run the MVT study to ensure the changes have a positive impact.
9. Identify any potential issues that need more detailed study or interventions, and flag these to the Product, Design, Research and Accessibility Teams.
10. Test again and repeat at regular intervals of no more than a month.

The value lies in the cycle rather than in producing a large research report.

## 14. I can test with a few people, but I must not over claim is the data is not statistically significant

It is a recommendation to test with customers and ensure the survey interface is fully accessible so no-one is denied a voice.

Regular segment-able surveys with customers may help me discover:

- an unclear navigation label;
- a missing next step;
- a misleading button;
- a form people cannot complete; 
- a service that excludes by design;
or
- a page whose purpose is unclear;
or
- how comparative a brand experience is for people with different abilities.

Usability surveys cannot enable me to:

- estimate success rates reliably;
- compare demographic populations by age, gender density, ethnicity, sexuality or other self-identity characteristics;
- establish prevalence;
- demonstrate legal compliance; or
- prove that a product is fully accessible.

But with satisfactions scores showing improvement, it demonstrates an intent that a brand values all its customers. 

I treat regularly repeated online testing as a diagnostic technique, similar to smoke testing, not evidence that quality or inclusion have conclusively been achieved.

At the end of a Likert scale customer satisfaction survey, ensure there is an optional text field for customers to leave comments for further analysis.

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

After the sessions, I debrief with the team while the observations are fresh. Rather than creating an exhaustive catalogue, I identify a small number of the most serious issues.

I consider:

- whether the problem blocks an important task;
- how severe its consequences are;
- whether it appeared repeatedly;
- whether it affects a common route;
- how confidently I understand it; and
- whether a practical improvement is available.

Fix the most serious and obvious problems before pursuing a wholesale redesign, and if this is in a live product, run a quantitative MVT study to measure the impact and outcome.

Accessibility adds a crucial qualification but do not treat that as a compliance issue, but rather as a lens of multimodal needs and preferences. Frequency is not the same as severity. A barrier experienced by one participant may completely exclude a wider group. I should not downgrade an accessibility defect simply because it appeared once in a small study, but I should also use the quantitative data to measure the combined impact on small issues on disabled customers.

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

Favour shared observation, a short list of agreed problems and immediate action over a long formal report, and if the problem is one that resolution has been well documented, allow the AI to autonomously spin up a multi-variant test to provide data that supports a quick fix.

I find this approach appropriate when:

- the product team attends the sessions;
- decisions can be made quickly;
- the findings are formative;
- the risks are limited; and
- responsibility for changes is clear.

I need more formal evidence when I am dealing with a regulated service, procurement, accessibility conformance, inclusive design, longitudinal research or accountable AI governance. In those situations, I need traceability between participants, tasks, observations, data, barriers, recommendations and decisions.

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

This is not a complete inclusive-design or accessibility methodology.

I need to combine it with:

- research involving disabled and neurodivergent participants;
- quantitative and statistically significant data that can be segmented using the EAA's functional requirements in Annex 1;
- assistive-technology testing;
- WCAG AA and platform-guideline evaluation;
- testing that includes inclusive design best practices.
- testing at high zoom and with text reflow;
- keyboard, switch, voice, touch screen and alternative-input testing;
- cognitive and communication accessibility;
- consideration of changes in capability and capacity from fatigue, pain, medication, environment and fluctuating ability;
- intersectional recruitment demographically as well as by user needs and preferences;
- analysis of exclusion rather than inconvenience alone; and
- documented accountability for barriers that remain unresolved.

Inclusive research sometimes requires deliberate recruitment because convenience samples systematically leave out the people most likely to encounter exclusion, or that the quantitative data has identified a particular group or groups that have provided low satisfaction scores;

I can use both approaches, but I must be clear that they answer different questions.

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

