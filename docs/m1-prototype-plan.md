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
3. Counterbalance order across participants to reduce learning effects. Use the same representative tasks, starting data, and completion definition.
4. Count every consequential merchant choice: selecting/adding/removing/reordering a section, selecting a data source/object, changing a default, or reversing an error. Do not count navigation clicks that make no design/content decision; record them separately.
5. Measure task time from reading the brief to a declared preview-ready state; pause only for moderator/equipment interruption. Record completion, assists, errors, backtracks, and confidence.
6. Blind-review shopper outputs without labels. Ask reviewers to order the intended shopper questions and identify the next action.
7. Compare medians and raw participant data; five users are directional, so report effect and observations, not statistical significance.

## Five-user moderated test

Recruit five marketing/ecommerce managers matching the target: responsible for routine launches/content, active Shopify theme-editor experience, not primarily developers, and spanning small teams/catalog complexity. Aim for three Beauty & Wellness and two adjacent-vertical participants if recruitment permits; record experience and accessibility needs. Do not substitute DCL staff for target users.

Each 60–75 minute remote or in-person session:

1. consent, background, and confidence calibration;
2. unaided starting-state choice for two counterbalanced workflows;
3. one matched B0/B1 build task using think-aloud only until stuck;
4. mobile preview and missing-data recovery;
5. cross-surface shopper-flow explanation without narrative vocabulary;
6. stripped-output recognition/comparison exercise;
7. short ease/confidence interview and debrief.

The moderator does not teach Reveal/Explain/Prove/Compare/Act. Assistance is recorded at the moment and classified as comprehension, navigation, data, content, or prototype limitation.

## Success criteria and stop rules

### Task success

- At least 80% of representative tasks are completed unassisted across the planned set, consistent with the roadmap gate.
- All five participants select the appropriate starting composition for the tested brief and at least four can explain its shopper flow without internal terminology.
- B1 improves median time **and** consequential decision count versus B0 for the matched tasks; report magnitude. A tie does not validate the operability claim.
- No participant needs code or a proprietary tool to complete a supported task.
- Zero-setup outputs are judged complete, and disconnecting structured data leaves a coherent result.
- No critical accessibility issue is designed in; no unresolved high-severity commerce ambiguity proceeds.

### Decision/time instrumentation

For each task record: start/end timestamps, completion state, decisions by category, navigation actions, reversals, errors, assists, sections/blocks/settings touched, preview checks, confidence (1–5), and final composition. Two researchers independently code one session and reconcile the counting rubric before the rest are analyzed.

### Originality evaluation

Run a dated teardown of Prestige, Impulse, Impact, Enterprise, Broadcast, Symmetry, Motion, and Pipeline using equivalent jobs. Evaluate start selection, decisions, cross-surface continuity, mobile priority, standard-data quality, structured enhancement, narrow section roles, and failure states—not section-count claims. A blind panel of product/design/theme experts reviews normalized stripped outputs and interaction maps.

The M1 blocking gate requires at least three competitor workflow gaps plus system/prototype evidence of meaningful architectural and overall-experience innovation. Reviewers must name the distinguishing behavior without relying on photography, fonts, copy, colors, motion, internal terminology, or preset names. If the result is explainable as reordered generic sections, M1 fails.

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
