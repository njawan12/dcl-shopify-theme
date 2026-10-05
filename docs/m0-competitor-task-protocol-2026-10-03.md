# M0 controlled competitor task protocol — 2026-10-03

## Objective

Determine whether at least three proposed DCL workflow gaps survive hands-on testing against strong current premium-theme baselines. This is a falsification exercise, not a feature checklist or aesthetic ranking.

## Competitors

Primary strong-baseline set:
- Broadcast
- Symmetry
- Motion
- Impulse

Coverage set:
- Prestige
- Impact
- Enterprise
- Pipeline

The primary set is intentionally difficult: current review evidence includes strong merchant praise for usability, templates, flexibility and self-management. If DCL's hypothesis only survives against weaker baselines, it is not strong enough.

## Access levels

Record one of:
- L0 listing only
- L1 public demo storefront
- L2 Shopify Theme Store preview/editor experience available to evaluator
- L3 licensed/full editor

Never infer L2/L3 behavior from L0/L1. An inaccessible editor task is **UNTESTED**, not a competitor failure.

## Standard merchant persona

Marketing/ecommerce manager at a design-conscious DTC brand:
- comfortable with Shopify admin/editor concepts;
- not a Liquid/CSS/JS developer;
- routinely launches products/campaigns;
- can prepare normal copy/images/product data;
- may use metafields if setup is understandable;
- should not require vendor support for routine supported jobs.

## Standard fixture

Use one fictional Beauty & Wellness brand/content pack for all competitors:
- one new multi-variant product;
- 5 product images with mixed portrait/square ratios;
- title long enough to wrap on mobile;
- standard description, price, compare-at price where legitimate, availability;
- 3 factual benefits;
- 3 usage steps;
- ingredient/material education;
- one evidence/proof item with neutral attribution;
- one collection of 8 products;
- one editorial story;
- one missing optional image;
- one intentionally long CTA/localized string;
- no reviews/subscription/bundle dependency;
- no unsupported medical/scarcity claims.

If editor access does not permit injecting identical content, record the mismatch and test only observable behavior.

## Five controlled tasks

### T1 Product Launch

Goal: create/publish-ready product-launch destination using existing product data plus supplied launch content.

Record:
- starting template/composition choices;
- number of consequential composition decisions;
- number of sections/blocks manually selected/added/reordered;
- settings searched/opened;
- duplicate content entry;
- custom code/support need;
- mobile repair decisions;
- elapsed time where access permits;
- output coherence.

Candidate gap tested: section/template decision load.

### T2 Paid Landing Page

Goal: turn the same launch proposition into a shorter paid-traffic destination with one clear action and no unnecessary navigation/story repetition.

Record:
- whether a relevant starting template exists;
- amount of deletion/reordering/reconstruction;
- product handoff behavior;
- repeated data entry;
- mobile CTA/sticky conflicts;
- code/support need.

Candidate gaps: decision load; cross-surface continuity.

### T3 Collection Launch

Goal: launch the 8-product collection with one editorial interruption/explanation while preserving filters/product count/pagination semantics.

Record:
- available collection templates;
- editorial insertion capability;
- whether merchandising breaks collection semantics;
- filter/quick-add interactions;
- mobile hierarchy;
- custom implementation need.

Candidate gaps: coherent merchandising; bounded composition.

### T4 Product Education

Goal: add benefits, usage and evidence to the PDP, then remove/disconnect one optional item while keeping the PDP polished.

Record:
- standard-data baseline quality;
- native metafield/dynamic-source affordance;
- setup steps;
- what happens when optional data is absent/deleted;
- empty gaps/labels;
- duplication across products;
- code/support need.

Candidate gap: structured-but-optional education.

### T5 Mobile Recovery

Goal: diagnose and fix a long-title/mixed-media/missing-media/sticky-action state at 390px without custom code.

Record:
- whether problem is visible in preview;
- bounded native control available;
- number of settings inspected;
- image focal/crop behavior;
- sticky collision ownership;
- safe omission/fallback;
- whether fix harms desktop;
- support/code dependency.

Candidate gap: mobile recovery without developer intervention.

## Consequential-decision definition

Count a decision when the merchant must choose among materially different storefront structures/behaviors and the correct answer is not already implied by the task/content.

Examples that count:
- choose among several plausible templates;
- decide which generic section type can represent supplied content;
- choose ordering that changes shopper argument;
- choose sticky/mobile behavior;
- choose between manual duplication and structured source.

Do not count:
- typing supplied copy;
- selecting the supplied product;
- uploading the supplied image;
- obvious save/publish actions.

This definition must be applied consistently to incumbents and later DCL B1.

## Gap pass/fail rules

### Gap A — decision economy
SURVIVES only if strong incumbents require materially more consequential composition decisions for at least two of T1–T3 than the proposed DCL bounded composition is designed to require. Final proof belongs in M1 paired testing.

### Gap B — cross-surface continuity
SURVIVES only if strong incumbents require meaningful reconstruction/duplication to maintain one campaign argument across landing/collection/PDP and do not provide an equivalent native job-level handoff.

### Gap C — structured-but-optional education
SURVIVES only if strong incumbents either make structured setup burdensome, degrade materially without it, or handle missing/disconnected optional education poorly. Mere metafield support disproves no gap and proves no gap.

### Gap D — mobile recovery
SURVIVES only if common content failures cannot be resolved predictably through bounded native controls/fallbacks without code/support in multiple strong incumbents.

### Gap E — complexity displacement
SURVIVES only if observed incumbent workflows repeatedly move complexity into template/section/setting selection despite broad flexibility. Large section count alone is insufficient evidence.

## Disproof rule

If Broadcast/Symmetry/Motion/Impulse already solve a candidate gap comparably well through native editor workflows, mark the gap **DISPROVEN or NARROWED**. Do not invent a subtler distinction simply to preserve DCL's concept.

M0 requires at least three defensible gaps after this process. Fewer than three means **do not advance the current originality/product thesis to M1 unchanged**.

## Evidence sheet per run

For each theme/task:
- theme/preset/version if visible;
- date/time;
- access level;
- desktop browser/viewport;
- mobile viewport;
- starting state;
- exact task;
- completion yes/no/partial/untested;
- elapsed time;
- consequential decisions;
- section/block additions;
- settings inspected;
- duplicated data;
- custom code/support required;
- mobile repair;
- missing-data behavior;
- screenshots/recording references where permitted;
- evaluator notes;
- uncertainty;
- candidate gap result: supports / contradicts / neutral / untested.

## Bias controls

- Run the strong-baseline themes first.
- Do not read DCL's proposed solution while scoring incumbent task completion.
- Record positive incumbent behavior with the same specificity as failures.
- Never convert lack of public access into a failure.
- Do not score visual taste as workflow failure.
- Do not penalize a competitor for intentionally different target positioning.
- Re-run surprising failures once before accepting them.
- Separate “feature absent” from “workflow difficult.”

## G4 closure rule

G4 closes only when:
1. all five tasks have been attempted across the four strong-baseline themes at the highest legitimately available access level;
2. coverage themes are used to challenge any gap that appears to survive;
3. evidence is captured consistently;
4. at least three candidate workflow gaps remain defensible, **or** the current thesis is explicitly rejected/narrowed.

A truthful finding of fewer than three gaps is a successful research outcome even though it blocks the current product direction.
