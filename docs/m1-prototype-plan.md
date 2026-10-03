# M1 prototype plan

## Purpose and boundary

The next M1 work is a grayscale, mobile-first, clickable **experience and editor simulation**. It tests the originality architecture, workflow comprehension, surface handoff, mobile priority, and decision economy before production implementation. It must not contain production Liquid, CSS, JavaScript, JSON templates/schemas, or a proprietary editor. Prototype labels and data may be disposable; decisions and evidence are versioned.

ADR-001 recommends an audited Skeleton foundation for eventual implementation, but no starter code is fetched or scaffolded during this prototype.

## Prototype set

### Shopper screens

| Surface | Required screens/states | Question tested |
|---|---|---|
| Home | Default wayfinding; one active launch; no campaign content; long navigation/title | Can a shopper find the current decision path without home becoming every workflow at once? |
| Campaign/landing | Product Launch; short Paid Landing; Product Education; text-first/no-media; long proof/legal content | Are jobs compositionally different through order and omission, not styling? |
| PDP | Standard-data product; structured education/proof; multi-variant; sold out; one/no/many media; long title; app inserted/removed | Does the factual purchase core remain clear while narrative resolves campaign promises? |
| Collection | Standard grid; Collection Launch interruption; filters active; no results; empty collection; long titles/mixed media | Does editorial rhythm preserve product/filter/pagination semantics? |
| Editorial | Story with contextual product; no commerce reference; long article; missing media/reference | Is reading primary while commerce handoff stays useful and honest? |
| Handoffs | Paid page → PDP; campaign → collection → PDP; editorial/education → product | Does each surface continue the argument without repeating the page? |

Every primary path has a stripped grayscale view using the same content, neutral system type, no motion, and normalized media placeholders. Include an equivalent blank/default baseline assembled from generic hero, text/media, product grid, and CTA components.

### Merchant-editor journeys

Simulate Shopify's native mental model rather than inventing editor mechanics:

1. Choose the appropriate start for each of the five jobs from merchant-facing names/descriptions.
2. Launch a product using only existing standard product data.
3. Convert the launch into a shorter paid destination by removing/reprioritizing content, not rebuilding it.
4. Launch a collection and add one editorial explanation without changing product counts.
5. Publish an editorial story and attach a contextual product reference.
6. Enhance product education with structured benefits/steps/evidence, then disconnect one source.
7. Insert and remove a generic app block at an allowed seam.
8. Change global brand roles and one bounded section emphasis without repairing every section.
9. Preview mobile, diagnose a collision/long-title state, and choose the supported resolution.
10. Recover from missing media, deleted product reference, empty collection, and unavailable variant.

The clickable editor simulation shows native concepts—template, section, block, setting, dynamic source, preview—but does not promise exact Shopify editor UI until current behavior is validated.

## Mobile states

Prototype at minimum:

- narrow viewport with 200% zoom/reflow reasoning;
- long localized header/menu, two navigation depths, country/language controls;
- PDP purchase core before secondary narrative, sold-out and validation error states;
- collection filter open/closed, active filters, no results, and editorial interruption;
- campaign with/without sticky action and with an app insertion to prove one-sticky-owner resolution;
- long product title, long CTA translation, unbroken ingredient/spec term, CJK sample, and bidirectional feasibility sample (not an RTL support claim);
- reduced-motion alternative for every proposed transition;
- keyboard/focus order annotations even when a touch-sized frame is shown;
- virtual-keyboard/form state and browser safe-area collision annotation;
- one/no/many media and portrait/landscape/square ratios.

## Empty, error, and long-content matrix

Include: missing hero/media; missing description; empty optional block; deleted dynamic-source reference; unavailable/sold-out product/variant; failed/removed app; empty collection; no filter results; invalid form selection; long title/copy/legal text/translation; dense comparison; absent evidence; video without autoplay; and a slow-media placeholder. Annotate expected omission, fallback, status announcement, focus destination, and layout response.

## Reference content fixtures

### Beauty & Wellness deep fixture

Use an original or clearly licensed fictional brand with:

- a 6–12 product skin/body-care catalog including single- and multi-variant products;
- factual titles, descriptions, prices, availability, compare-at and unit-price examples where legitimate;
- portrait/square/landscape product and editorial media with alt-text briefs and license/provenance records;
- a new-product launch, a routine/collection, ingredient/material education, usage steps, cautions, evidence with attributable source placeholders, and honest comparison dimensions;
- standard-data-only and structured-enhancement versions;
- sold-out, no-media, long-title, missing-evidence, and deleted-reference cases;
- no medical, sustainability, certification, review, scarcity, or efficacy claim without support.

Copy must be realistic enough to expose hierarchy and wrapping. Placeholder rectangles and repeated lorem ipsum are insufficient for task testing.

### Apparel probe

Use the same contracts with 12–24 products, size/color options, unavailable combinations, mixed ratios, materials/care, fit guidance, a capsule collection launch, and an editorial origin story. Test whether variant facts, comparison, collection interruption, and mobile media priorities work without an “apparel mode” or new generic controls.

### Food/beverage probe

Use the same contracts with 8–16 products, size/pack variants, unit pricing where applicable, ingredients/allergens, preparation/serving steps, dietary claims only when substantiated, a range launch, and an origin story. Test dense labels, repeat-purchase context, and education without a “food mode.”

These are fitness probes, not launch presets. If either requires unique section taxonomies, unclear toggles, or setting-budget expansion, ADR-007 should narrow the market rather than generalize the system.

## Baseline comparison method

1. Build two content-equivalent grayscale prototypes: **B0**, a blank/default native-style assembly using generic sections; and **B1**, the intent-led system.
2. Normalize viewport, copy, media placeholders, product data, typography, color, motion, and participant instructions.
3. Use the repeated-measures assignment and arm order below to control workflow coverage, learning, and order effects. Use equivalent content, the same starting data quality, and one completion definition for both arms.
4. Count every consequential merchant choice: selecting/adding/removing/reordering a section, selecting a data source/object, changing a default, or reversing an error. Do not count navigation clicks that make no design/content decision; record them separately.
5. Measure task time from reading the brief to a declared preview-ready state; pause only for moderator/equipment interruption. Record completion, assists, errors, backtracks, and confidence.
6. Keep merchant-flow explanation as a merchant mental-model measure; use the separate representative-shopper study below for shopper comprehension.
7. Pre-register these B1 median time ceilings before testing: **Product Launch 12 minutes; Paid Landing Page 8 minutes; Collection Launch 10 minutes; Editorial Story 9 minutes; Product Education 12 minutes.** Timing starts when the participant finishes reading the task brief and begins work, and ends at the declared preview-ready state; only moderator/equipment interruptions pause the clock. Scope is the complete representative workflow task defined by the assigned brief, not a partial subtask.
8. Compare workflow-level paired medians and raw participant data. Each workflow must meet **both** its absolute B1 median ceiling and a below-zero paired median change versus B0. These small samples provide directional product evidence only; do not calculate or claim statistical significance.

## Five-user moderated test

Recruit five marketing/ecommerce managers matching the target: responsible for routine launches/content, active Shopify theme-editor experience, not primarily developers, and spanning small teams/catalog complexity. Aim for three Beauty & Wellness and two adjacent-vertical participants if recruitment permits; record experience and accessibility needs. Do not substitute DCL staff for target users.

Each merchant completes **four paired workflow tasks**—eight short builds total, because every assigned workflow is attempted once in B0 and once in B1—plus one scored B1 mobile/missing-data recovery task. Split the work into two sessions of at most 60 minutes, with two workflow pairs per session, rather than trading coverage for fatigue. Use equivalent content variants between arms and rotate them with arm order so the second build is not a copy exercise.

The balanced assignment produces exactly four paired observations for every workflow:

| Merchant | Session/order positions 1–4 | Omitted workflow |
|---|---|---|
| M1 | Product Launch **B0-first**; Paid Landing **B1-first**; Collection Launch **B0-first**; Editorial Story **B1-first** | Product Education |
| M2 | Paid Landing **B0-first**; Collection Launch **B1-first**; Editorial Story **B0-first**; Product Education **B1-first** | Product Launch |
| M3 | Collection Launch **B0-first**; Editorial Story **B1-first**; Product Education **B0-first**; Product Launch **B1-first** | Paid Landing |
| M4 | Editorial Story **B0-first**; Product Education **B1-first**; Product Launch **B0-first**; Paid Landing **B1-first** | Collection Launch |
| M5 | Product Education **B0-first**; Product Launch **B1-first**; Paid Landing **B0-first**; Collection Launch **B1-first** | Editorial Story |

This rotated incomplete-block schedule gives each workflow two B0-first and two B1-first pairs while also placing each workflow exactly once in each ordinal position across the valid schedule. Use the listed workflow order unchanged for all participants; do not reverse within-session positions ad hoc, because that would break the position balance and reintroduce session/fatigue as a workflow confound. If an alternate ordering is ever introduced, it must be pre-specified as a complete replacement schedule and must independently preserve both the two-B0-first/two-B1-first balance and the one-per-ordinal-position balance for every workflow. A valid workflow-level median requires at least four completed pairs from four different merchants. Calculate each merchant's within-pair change (`B1 − B0`) for time and consequential decisions, then take the median of the four changes; improvement requires both medians to be below zero. If withdrawal or prototype failure leaves fewer than four valid pairs, recruit a targeted replacement for the missing workflow pair and assign that replacement to the exact missing schedule cell so first-arm and ordinal-position balance are preserved; report the shortfall and make no workflow pass, median-improvement claim, or M1 decision until the fourth valid pair exists.

Each session includes consent/check-in, the two assigned paired tasks, an unaided starting-state choice, and a short debrief. Across the two sessions, each merchant also completes the one scored B1 mobile/missing-data recovery task and explains the composed shopper flow without being taught the narrative vocabulary.

The moderator does not teach Reveal/Explain/Prove/Compare/Act. Any hint, corrective direction, demonstrated step, or answer needed to continue counts as moderator assistance and makes that scored task **not unassisted**, even if the participant later finishes. Record it at the moment and classify it as comprehension, navigation, data, content, or prototype/tooling limitation.

A genuine prototype/tooling failure is a broken link, unavailable control, corrupted state, or fidelity limitation that prevents the intended action despite correct participant intent. Mark that attempt **invalid**, fix the prototype, and rerun the **complete B0/B1 pair** with equivalent unseen content variants so one-arm practice cannot bias the result; never score it as success or comprehension failure. Confusing labels, undiscoverable controls, incorrect starting-state choice, or inability to decide what to do are product/comprehension failures, not tooling exclusions.

## Success criteria and stop rules

### Task success

- **Every merchant must complete at least four of their five scored B1 representative tasks (80%) unassisted**: the four assigned workflow builds plus the mobile/missing-data recovery task. The recovery task is also a mandatory independent gate: every merchant must complete it unassisted, so success on four workflow builds cannot compensate for failure to recover from a missing/error state. Aggregate success cannot compensate for a participant below either threshold.
- Report B0 and B1 completion, assistance, time, and decisions separately for every workflow. With four valid B1 observations, meeting the existing ≥80% workflow threshold requires **four of four unassisted completions**; three of four is 75% and fails.
- For every workflow, B1 must satisfy its pre-registered absolute median time ceiling **and** improve the paired median time **and** paired median consequential-decision count versus B0. The absolute and paired time gates are independently blocking. Report magnitude and all raw pairs; exceeding the ceiling, a tie, or a regression fails that workflow.
- All five participants select appropriate starts for their assigned briefs and explain their composed shopper flows without internal terminology; this is merchant comprehension, not shopper-comprehension evidence.
- No participant needs code or a proprietary tool to complete a supported task.
- The blocking token/schema specimen in [`m1-token-schema-specimen.md`](m1-token-schema-specimen.md) is exercised in the editor simulation: proposed versus observed setting counts, initially visible controls, reveal paths, workflow compositions, global-token propagation, vertical reuse, and developer-dependence evidence are recorded. Any independent control-architecture failure blocks M1.
- Zero-setup outputs are judged complete, and disconnecting structured data leaves a coherent result.
- No critical accessibility issue is designed in; no unresolved high-severity commerce ambiguity proceeds.

If any merchant finishes fewer than four of five scored B1 tasks unassisted **or does not complete the recovery task unassisted**, stop the overall pass decision, diagnose the affected contracts, redesign, and retest that participant-level risk with a replacement or follow-up target merchant. If any workflow has fewer than four valid pairs, fewer than four of four unassisted B1 completions, or no improvement on either paired median, that workflow fails and must be narrowed, redesigned, and retested; it cannot disappear inside the overall average.

### Decision/time instrumentation

For each arm and the recovery task record: participant, workflow, arm order, content variant, start/end timestamps, valid/invalid reason, completion state, decisions by category, navigation actions, reversals, errors, assists, sections/blocks/settings touched, preview checks, confidence (1–5), and final composition. Two researchers independently code one session and reconcile the counting rubric before the rest are analyzed.

### Originality evaluation

Run a dated teardown of Prestige, Impulse, Impact, Enterprise, Broadcast, Symmetry, Motion, and Pipeline using equivalent jobs. Evaluate start selection, decisions, cross-surface continuity, mobile priority, standard-data quality, structured enhancement, narrow section roles, and failure states—not section-count claims. A blind panel of product/design/theme experts reviews normalized stripped outputs and interaction maps.

The M1 blocking gate requires at least three competitor workflow gaps plus system/prototype evidence of meaningful architectural and overall-experience innovation. Reviewers must name the distinguishing behavior without relying on photography, fonts, copy, colors, motion, internal terminology, or preset names. If the result is explainable as reordered generic sections, M1 fails.

Expert review tests architectural comparison, feasibility, and whether the stripped system is distinguishable from competitor patterns. Experts are not evidence that representative shoppers understand it and cannot satisfy the shopper-comprehension gate.

### Separate shopper-comprehension validation

Recruit **six representative shoppers**, separate from the five merchants and expert panel. Each must have bought online in Beauty & Wellness or an adjacent probe category within the previous six months; include a mix of mobile-first shoppers, familiarity levels, and accessibility needs where recruitment permits. Exclude DCL staff, theme professionals, ecommerce implementers, and anyone who participated in the merchant study.

Use four stripped, neutral shopper flows: (A) Product Launch campaign → PDP; (B) Paid Landing → Product Education/PDP; (C) Collection Launch campaign → collection → PDP; and (D) Editorial Story → referenced PDP. Assign S1 to A/B, S2 to A/C, S3 to A/D, S4 to B/C, S5 to B/D, and S6 to C/D; reverse presentation order for S2, S4, and S6. This balanced incomplete-block assignment yields **three independent observations per flow** and 12 observations total. Do not show B0/B1 labels, branded photography, distinctive fonts, color, motion, internal narrative terms, or merchant-editor UI.

For each surface, ask the shopper to think aloud and answer without prompts: “What is this page helping you understand?”, “What question would you expect it to answer next?”, and “What would you do next?” After each transition, ask what carried forward, what felt repeated, and what became confusing. Do not teach Reveal → Explain → Prove → Compare → Act or reveal the intended route before the task.

A flow passes directional comprehension only when at least two of its three shoppers independently identify a materially correct surface purpose, logical next question, and intended next action, and describe the handoff as continuous without material repetition or confusion. Any repeated material confusion reported by two shoppers blocks that flow even if the other answers pass. If a tooling failure prevents exposure, replace that observation; if fewer than three valid observations remain, collect a top-up and make no claim meanwhile. A failed flow is redesigned and retested, and the cross-surface originality claim does not pass while the campaign → collection → PDP flow fails.

This study tests the shopper-facing decision path, not merchant editor operability, build time, or setting decisions. Its small sample is directional qualitative evidence, not statistical proof. Preserve raw responses and report dissent rather than converting the result into an aggregate conversion claim.

### Accessibility design review

Before usability sessions, an accessibility specialist reviews annotated semantics, headings, landmarks, reading/focus order, names/roles/states, dialogs/disclosures, errors/status, media alternatives, contrast-token assumptions, touch targets, zoom/reflow, reduced motion, sticky collisions, tables/comparisons, and localization expansion. After revisions, test key flows with keyboard plus VoiceOver and NVDA at prototype fidelity where meaningful; log prototype limitations rather than claiming conformance.

## Foundation and compliance preflight

Apply the classification discipline of [`engineering-compliance-standard.md`](engineering-compliance-standard.md) without pretending design evidence is implementation evidence.

| Risk area | Preflight question/evidence | Gate before implementation |
|---|---|---|
| Shopify requirements | Are foundation eligibility, directories/templates, schemas/nesting, app contexts, exclusivity, demos/support, browsers, locales, and performance rules current? | Refresh official sources, assign owner/status/test mapping; unknown mandatory rules block M2. |
| Accessibility | Do composition and mobile priority preserve semantics, focus, reflow, alternatives, status, contrast, and reduced motion? | Specialist review; no designed critical issue; WCAG 2.2 AA remains implementation gate. |
| Commerce correctness | Does every narrative handoff retain accurate variants, prices, availability, quantity/selling-plan/pickup/cart and legitimate claims? | State matrix and interaction annotations; factual purchase core cannot be overridden. |
| Performance/LCP | Is there one intended LCP candidate, reserved media space, bounded initial media, and no unjustified app/video payload? | Per-screen media/payload hypothesis mapped to the internal budget; validate later with code. |
| Theme-editor lifecycle | Can sections be add/remove/duplicate/reorder/select/re-render safely without hidden workflow state? | Prototype every lifecycle operation conceptually; production test plan before M2. |
| App compatibility | Are apps optional guests at current supported seams, with removal/failure/collision states? | Revalidate `@app` contexts and test generic representative categories, not vendors. |
| Localization | Are all strings localizable and layouts resilient to expansion, CJK, currencies, Markets, and bidirectional feasibility? | Pseudo-localized screens and long content; no RTL claim before ADR-005. |
| Originality/provenance | Is the stripped decision-path system distinct and is every reference/asset/foundation source recorded? | Competitor task evidence, provenance ledger, Skeleton pin/license/diff, originality red-team. |

## Deliverables and decision outputs

- clickable grayscale shopper and editor simulations;
- screen/state inventory and mobile-priority annotations;
- B0/B1 study materials, raw measures, findings, and recordings/consent handling;
- competitor task teardowns and stripped comparison;
- accessibility design-review log;
- requirements traceability refresh and risk owners;
- ADR-002 through ADR-007 evidence inputs;
- explicit build, narrow, redesign, or stop recommendation.

Stop after the M1 review. Do not begin production implementation or M2 until every blocking gate is approved.

## Blocking M1 design deliverables

The token/schema specimen and setting-count/progressive-disclosure inventory in [`m1-token-schema-specimen.md`](m1-token-schema-specimen.md) are separate blocking deliverables. They must be updated with observed counts and evidence from the prototype sessions; missing inventory, exceeded ceilings, displaced complexity, token-propagation failures, vertical schema forks, or routine developer dependence block M1 regardless of other usability/originality results.
