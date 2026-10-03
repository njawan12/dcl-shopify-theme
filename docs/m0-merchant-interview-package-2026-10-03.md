# M0 merchant interview package — 2026-10-03

## Purpose

Validate or falsify the M0 problem hypothesis before M1. This is problem research plus a lightweight concept-comprehension check, not a sales pitch and not M1 usability testing.

M0 closes only with real merchant evidence. AI simulations, inferred opinions, DCL team members, theme professionals, or casual conversations without the required evidence do not count.

## Sample

Target: **8–12 valid interviews**.

Minimum composition:
- at least 8 valid target-merchant participants total;
- majority Beauty & Wellness;
- at least 3 participants across adjacent candidate verticals, prioritizing apparel/fashion and food/beverage/lifestyle;
- participant personally performs or directly owns Shopify merchandising/site publishing;
- participant has completed at least one product launch, campaign/landing-page change, PDP update, or collection merchandising change in the last 6 months.

Prefer variation in:
- catalog size inside/near the 20–500-product research assumption;
- internal developer access vs agency/freelance/no developer;
- current premium/free/custom theme;
- launch frequency;
- team size.

Exclude:
- DCL employees/contractors;
- Shopify theme developers/designers answering as experts rather than merchants;
- merchants who do not touch/own storefront publishing;
- participants whose relevant experience is too old to reconstruct concrete recent work.

Existing DCL clients may qualify, but relationship does not waive the criteria and the interviewer must explicitly invite criticism.

## Interview structure — 30 minutes

### 0. Qualification — 3 min

1. What is your role, and which parts of the Shopify storefront do you personally own or change?
2. Roughly how many products do you sell?
3. In the last six months, which have you personally been involved in: new-product launch, paid campaign/landing page, collection launch/merchandising, PDP education update, theme redesign/update?
4. What theme/setup are you using now? Free/premium/custom if known.
5. Who normally changes the storefront: you, marketing/ecommerce, developer, agency, or mixed?

If the participant cannot describe a recent relevant workflow they personally own, mark INVALID for the gate.

### 1. Recent-behavior reconstruction — 10 min

Ask for the **most recent real launch/change**, not opinions about themes.

6. Walk me through the last time you launched a product or meaningful campaign on the site, starting from “we need this live” until it was published.
7. What pages/surfaces did you have to touch?
8. What did you reuse versus rebuild or copy?
9. Where did you hesitate or have to decide how the page should be structured?
10. Did you need a developer, agency, theme support, documentation, or custom code? What specifically triggered that?
11. What took the most time?
12. What went wrong or needed rework?
13. What did you check on mobile before publishing?
14. If some content/data was missing, what happened?
15. Roughly how long did the storefront portion take, excluding photography/copy approval?

Follow-up rule: ask for concrete examples (“what happened next?”, “show/describe the decision”) before accepting abstract claims such as “Shopify is easy” or “the theme is limiting.”

### 2. Frequency and economic consequence — 5 min

16. How often do you do a change like this?
17. Which storefront tasks repeatedly require someone technical?
18. What happens when that person is unavailable?
19. Have you delayed, simplified, or abandoned a campaign/site idea because changing the theme was too much work? Give the most recent example.
20. If the workflow were faster/easier, what would actually change for the business: launch frequency, staff time, agency spend, campaign speed, experimentation, or nothing meaningful?

Do not suggest answers unless the participant is unable to understand the question; if examples are supplied, mark the response as prompted.

### 3. Current-theme strengths — 4 min

This section is mandatory counter-evidence.

21. What does your current theme make genuinely easy?
22. Which parts would you not want a new theme to change?
23. Do templates/presets already solve most of the setup problem for you?
24. If you could keep your current theme and improve only one workflow, what would it be?

### 4. Concept comprehension — 6 min

Only now describe the hypothesis neutrally:

> “Imagine a premium Shopify theme that still uses Shopify’s normal editor and normal sections, but when you need to do a recurring commercial job—such as launching a product or building a paid landing page—it gives you a strong starting composition with deliberate defaults, mobile behavior and safe missing-content states. You can still edit the normal Shopify sections; it is not a separate page builder.”

Then ask:

25. In your own words, what do you think that would do?
26. How is that different, if at all, from the templates/presets you already have?
27. Which part sounds useful?
28. Which part sounds unnecessary or worse than your current setup?
29. What would you expect “Product Launch” to set up for you automatically, and what would you still want to control?
30. What would make you distrust or avoid this approach?
31. Would this solve a problem you actually experience, or mostly make something already easy slightly nicer? Why?

Do **not** ask “would you buy it?” as primary validation. Hypothetical purchase intent is weak evidence.

### 5. Close — 2 min

32. Is there a storefront workflow we have completely misunderstood?
33. May we contact you for a short prototype test later? (Separate from M0 validity.)

## Evidence captured per participant

- participant ID, not unnecessary personal data;
- vertical;
- role;
- approximate catalog size;
- current theme/setup;
- developer/agency access;
- launch/change frequency;
- concrete recent workflow;
- surfaces touched;
- elapsed storefront time;
- consequential decisions described;
- repeated/duplicated work;
- developer/support/code dependencies;
- mobile problems/recovery;
- missing-data behavior;
- business consequence;
- current-theme strengths;
- concept paraphrase;
- concept-vs-template distinction;
- strongest objection;
- hypothesis support / contradiction / mixed;
- prompted answers flagged;
- validity status and reason.

## Coding rubric

### P1 Repeated launch/PDP workflow pain
YES only when participant describes a concrete recent recurring friction involving time, decisions, duplication, dependency, rework or delay. General dislike of Shopify does not count.

### P2 Technical dependency
YES when a routine target workflow required developer/agency/theme-support/custom-code intervention. Do not count custom business logic outside the proposed theme scope.

### P3 Decision-load signal
YES when participant describes uncertainty/effort choosing structure, sections, templates, responsive behavior or reuse—not merely typing content.

### P4 Cross-surface reconstruction
YES when campaign/product/collection story required material duplication or reconstruction across surfaces.

### P5 Mobile recovery friction
YES when ordinary content/media/responsive states required non-obvious repair, support or code.

### P6 Concept comprehension
PASS only if participant can explain the proposed job-oriented starting composition without being taught DCL's internal Reveal/Explain/Prove/Compare/Act grammar.

### P7 Incremental-vs-material value
MATERIAL only when participant connects the concept to a concrete current cost/delay/dependency or meaningfully improved commercial workflow. “Sounds nice” = INCREMENTAL.

### P8 Counter-evidence
STRONG when current templates/presets already solve the relevant job with low decision load and no meaningful technical dependency.

## M0 pass/fail interpretation

The existing repo gate requires at least 8 target-merchant interviews showing repeated launch/PDP maintenance pain and concept comprehension sufficient to prototype.

To prevent hand-waving, use this operational interpretation:

- **Minimum 8 valid participants.**
- A majority of valid participants must have P1=YES from concrete recent behavior.
- At least 5 valid participants must have P6=PASS.
- At least 4 valid participants should show P3=YES or P4=YES; otherwise the specific “bounded job composition” solution is weakly connected to the observed problem.
- Strong P8 counter-evidence in half or more of valid participants forces NARROW/RETHINK even if general pain exists.
- Adjacent-vertical participants must not require fundamentally different editor/schema concepts merely to understand the proposed workflow; otherwise narrow Beauty & Wellness first.
- P2 is informative but is **not required**: the opportunity should not depend on merchants currently hiring developers.
- Purchase-intent statements never override behavioral evidence.

These thresholds are M0 operationalization of the existing qualitative gate; they do not replace the stricter M1 usability thresholds.

## Interviewer anti-bias rules

1. Do not mention DCL's desired differentiation before behavior reconstruction.
2. Do not call the current workflow “painful,” “slow,” “confusing,” or “developer dependent.”
3. Do not defend the concept.
4. Ask for the last real example before accepting opinions.
5. Record strong incumbent/current-theme positives.
6. Do not count a problem outside theme scope as evidence.
7. Do not count participant politeness as concept value.
8. If a participant says the current setup is already easy, investigate it rather than persuading them otherwise.
9. Preserve contradictory evidence in the synthesis.
10. Do not change thresholds after seeing results.

## Recruitment message

> Hi — I’m researching how Shopify ecommerce teams actually handle product launches, landing pages, PDP updates and collection merchandising. I’m not selling anything. I’m looking for people who personally manage or own storefront changes for a 30-minute research conversation about their most recent real workflow. I’m specifically interested in what works well as much as what is frustrating. Would you be open to helping?

For existing relationships, personalize the opening but keep the research framing and questions unchanged.

## Output after interviews

Create:
1. participant evidence table;
2. anonymized behavior/problem coding;
3. contradiction/counter-evidence section;
4. Beauty & Wellness vs adjacent-vertical comparison;
5. M0 threshold result;
6. implications for G6 positioning;
7. explicit PROCEED / NARROW / RETHINK outcome for the founder G8 review.

Do not begin M1 prototypes merely because interviews are complete. G4 competitor tasks and G7 founder commitments must also close.
