# M1 surface-system prototype plan

## Status

This document supersedes the prior workflow-led M1 prototype plan.

The old plan was built around Product Launch, Paid Landing Page, Collection Launch, Editorial Story and Product Education as the primary differentiation hypothesis. M0 evidence rejected routine Product Launch pain as the core problem and demoted named commercial-job workflows from product architecture.

Reveal → Explain → Prove → Compare → Act is not merchant-facing architecture. It may remain an internal CRO/content-review lens only.

No production Liquid, CSS, JavaScript, JSON templates or schemas are created in M1.

## M1 question

Can DCL create a visually exceptional Beauty/Wellness-first theme that productizes a meaningful portion of recurring agency customization demand through **bounded structural flexibility on high-value surfaces**, while remaining easy for merchants to operate and clean for developers to extend?

## Prototype systems

M1 prototypes six systems before broad theme design.

### S1 — PDP purchase area / buy box

Test materially different purchase compositions, not cosmetic skins.

Required states:
- single and multi-variant;
- available/sold out/unavailable;
- quantity;
- compare-at/unit price where legitimate;
- selling-plan/native subscription presentation where applicable;
- generic app-block insertion/removal;
- long title/price/supporting copy;
- sticky/non-sticky mobile behavior;
- validation/error state.

Prototype at least three structurally meaningful compositions. Every composition uses the same commerce truth and form contract.

### S2 — Product media + badges

Test:
- stacked/gallery-led/other justified composition variants;
- one/no/many media;
- portrait/square/landscape/mixed ratios;
- image/video/3D compatibility assumptions;
- objective product badge overlay;
- mobile media priority;
- zoom/lightbox only if it improves the tested experience.

Badges and galleries are table stakes; the test is composition quality and resilience.

### S3 — Product education

Use conventional merchant language and narrow content responsibilities:
- benefits/features;
- ingredients/materials/specifications;
- usage/process;
- FAQ/disclosure;
- honest comparison;
- proof/results/testimonial host;
- app-block host where appropriate.

Standard product content must produce a complete experience. Structured data is optional enhancement.

### S4 — Cart

Prototype correct cart behavior plus bounded visual/composition variants.

Include:
- add/update/remove;
- quantity/errors;
- line properties;
- selling-plan display;
- notes if supported;
- factual free-shipping/progress messaging only when based on real configured thresholds;
- complementary merchandising;
- generic app seams;
- mobile drawer/page behavior.

No custom discount engine, fake urgency or app-like business logic.

### S5 — General storytelling/content composition

Test whether a deliberately small set of primitives can support premium Beauty/Wellness storytelling without a 40-section arms race.

Candidate primitives:
- rich media + copy;
- benefit/feature group;
- comparison;
- process/timeline;
- FAQ/disclosure;
- proof/results;
- promotional/story tile;
- CTA/action group;
- contextual product reference.

Reject a universal "anything" section.

### S6 — Global design system + local structural controls

Define:
- semantic typography roles;
- color schemes;
- width/density/spacing roles;
- radius/border/elevation policy;
- media treatment;
- button/link/control system;
- card system;
- motion policy;
- structural variants at the owning surface;
- bounded local presentation controls.

Do not expose arbitrary CSS, raw breakpoint controls or hundreds of pixel settings.

## Three-composition proof

Using the same fictional Beauty/Wellness catalog and the same six systems, create at least three clearly different storefront directions.

Normalize or strip photography, copy, fonts, colors and motion during one comparison pass. The structural identity must still differ through composition, hierarchy, product-card treatment, purchase-area structure, media rhythm, content relationships and mobile priority.

If the difference disappears when decorative art direction is removed, the architecture is not providing meaningful range.

## Control-budget proof

For every prototype surface, inventory every merchant-facing decision as one of:

1. global semantic token;
2. surface structural variant;
3. block composition/order;
4. dynamic product/content data;
5. bounded local presentation setting;
6. developer-only extension point.

Every setting needs:
- merchant question it answers;
- default;
- consequence;
- whether initially visible;
- conditions;
- mobile effect;
- interaction with other settings.

Reject a setting when its value is primarily "more flexibility" without a repeated merchant/design need.

## Designer test

A designer receives the supported primitives and must be able to specify three materially different Beauty/Wellness storefront outcomes without inventing unsupported CSS/layout behavior.

This is not a claim that every design is implementable without development.

Failure signals:
- repeated request for arbitrary positioning;
- one-off breakpoint controls;
- duplicate mobile content;
- per-block CSS;
- universal sections;
- structural requirements that force source edits for ordinary supported variation.

## Merchant-operability test

After a supported composition exists, test whether a Shopify operator can safely:

- change product-specific badges/content;
- connect/disconnect dynamic sources;
- reorder allowed blocks;
- choose among structural variants;
- update content;
- change global brand roles;
- recover from missing media/data;
- preview mobile and understand the supported behavior.

The test is not "can a merchant design a new art direction from scratch?"

## Developer-extension test

Give an experienced Shopify developer two constrained tasks:

1. add one justified purchase-area structural variant;
2. add one narrow storytelling section using existing primitives.

Measure:
- files/contracts touched;
- global side effects;
- duplicated logic;
- JS coupling;
- CSS leakage;
- editor lifecycle risk;
- commerce/accessibility regression surface.

The architecture fails if ordinary extension requires rewriting unrelated systems or understanding proprietary workflow machinery.

## Zero-setup and structured-data pairs

Every relevant surface is shown twice:

- standard Shopify data only;
- optional structured enhancement.

Disconnecting a source must restore a coherent omission/fallback state. No empty cards, invented proof, invented ingredients, fake ratings or fabricated urgency.

## Mobile/resilience matrix

At minimum test:
- 390px viewport;
- 200% zoom/reflow reasoning;
- long product titles and translations;
- CJK and bidirectional feasibility samples;
- one/no/many media;
- mixed ratios;
- sold-out/unavailable variant;
- missing dynamic source;
- removed app block;
- virtual keyboard/form state;
- browser safe area;
- reduced motion;
- keyboard/focus order annotations.

One sticky owner at a time.

## Incumbent comparison

Compare the stripped prototype system against the strongest accessible incumbent evidence.

Do not score competitors from listing omissions. If editor depth is not legitimately observable, mark it UNTESTED.

The M1 originality case must rest on the combined system:
- target-vertical visual identity;
- high-value structural flexibility;
- agency-informed control selection;
- polished standard-data defaults;
- merchant operability;
- clean developer extensibility;
- mobile/accessibility/performance quality.

No single feature is expected to be unique.

## M1 blocking decision

Proceed to M2 only if:

- all six systems have bounded contracts and setting budgets;
- three materially different Beauty/Wellness compositions are achievable;
- merchant operation does not require code for the supported controls;
- developer extension is clean;
- zero-setup is premium;
- no universal/catch-all architecture is required;
- current Shopify requirements remain satisfied in the design;
- the founder approves the visual/product direction and operating commitments.

If the thesis fails, narrow or stop. Do not rescue it by adding more features.
