# M0 product-thesis reconciliation — 2026-10-03

## Decision

**NARROW AND PROCEED WITH PRODUCT DEFINITION.**

The prior M0 thesis centered too heavily on merchant difficulty completing named commercial jobs such as Product Launch. Direct operator evidence from DCL contradicts that premise: routine product creation, product-data entry, template assignment, and publishing are generally handled successfully by merchants with Shopify's native tools.

The product thesis is therefore changed before production implementation.

## Evidence incorporated

This reconciliation combines:

1. the dated official Shopify requirements refresh;
2. the 50-review coded competitor evidence;
3. the current competitor listing and public-demo research;
4. DCL founder/operator evidence drawn from repeated client work across Shopify brands.

The founder evidence is **operator evidence, not ten independent merchant interviews**. It must not be represented as independent market research.

## What the operator evidence says

Across DCL client work:

- Routine product launches are usually merchant-operated through native Shopify product creation and template assignment.
- Brands **constantly** request additional merchant control so routine changes do not require a developer.
- The dominant reasons are not total feature absence. More commonly, an existing theme offers something similar but lacks sufficient control, or its implementation does not fit the brand's design/business requirement.
- Recurring examples include new/reworked buy boxes, new functionality, complete visual refreshes, new page sections, cart redesigns, product-specific badges and merchant controls around purchase/subscription presentation.
- Metafields are frequently the data/control mechanism, but merchants often need developers to create definitions and wire them to storefront components.
- Once DCL creates an appropriate merchant-facing control, merchants generally operate it themselves rather than repeatedly returning for the same change.
- These requests are mostly common patterns across brands rather than wholly unique requests.
- Representative customization work can consume roughly 2–3 developer days, depending on scope.
- When a design exceeds the theme's native capability, common implementation work is: create a new section, change structural markup/composition, and write CSS.
- Premium-theme customization is sometimes possible with existing primitives, but not consistently.
- From the agency developer perspective, theme structure and code quality are recurring customization pain points.
- A strong theme would reduce, not eliminate, custom development. Truly bespoke art direction and functionality remain valid agency work.
- Observed theme-purchase priorities are led by visual quality and features, followed by reviews and industry fit.
- Visual appeal is holistic: art direction, composition, typography, imagery, motion/interactions, PDP quality and storytelling all matter.
- Design refreshes still require design expertise and often development; the product must not promise to replace designers or developers.

## Hypotheses explicitly killed or demoted

### K1 — Product Launch is the primary merchant pain
**REJECTED.** Routine product launches are generally already handled by merchants using Shopify-native workflows.

### K2 — Named job workflows are the primary differentiation
**DEMOTED.** Product Launch / Paid Landing / Collection Launch labels may be useful as documentation, presets, recipes or onboarding examples, but they are not the core product architecture or validated market gap.

### K3 — Launch Narrative System is the product
**REJECTED AS MERCHANT-FACING PRODUCT ARCHITECTURE.** Reveal → Explain → Prove → Compare → Act may remain an internal design/CRO review lens only. It must not dictate merchant-facing schemas, section names or a proprietary workflow.

### K4 — Developer independence is absolute
**REJECTED.** The theme should materially extend the range of work achievable without development. It should not pretend custom design, custom functionality, integrations or business logic disappear.

### K5 — More features/settings equals differentiation
**REJECTED.** Public competitor evidence already shows large section libraries and dense feature sets. Unbounded settings create complexity displacement.

### K6 — Metafields themselves are the differentiator
**REJECTED.** Dynamic sources/metafields are platform primitives. Differentiation can come from exceptionally designed components and control contracts that use them well.

### K7 — Rollouts is the core moat
**REJECTED AS CORE POSITIONING.** Testability is an architectural requirement. High-value presentation variables should be exposed through native theme customization where sensible, but a Shopify-native experimentation capability is not by itself a defensible theme identity.

## Revised target

**Primary launch target:** design-conscious health, beauty and wellness DTC brands, especially focused catalogs where PDP quality, product education, merchandising and repeated visual iteration matter.

Initial design/reference work should be Beauty & Wellness first. Do not encode vertical-specific mode switches into architecture. Adjacent vertical expansion is deferred until the system proves it can travel without abstraction bloat.

## Revised product thesis

Build a **visually exceptional, health/beauty/wellness-first Shopify theme informed by recurring agency customization work**.

The theme should give merchants and designers unusually strong control over the high-value storefront surfaces that repeatedly become custom-development tickets, while remaining Shopify-native and bounded enough to stay understandable, fast, accessible and supportable.

When custom development is genuinely required, the theme should be unusually clean and predictable to extend.

### Working product promise

> Agency-grade visual quality and useful control over the storefront changes growing DTC brands repeatedly ask developers to build.

This is a working internal promise, not approved Theme Store listing copy.

## Product value hierarchy

### 1. Visual desirability — acquisition gate
A merchant must want the storefront before reading architecture claims. Demo quality, art direction, typography, composition, media treatment, interaction quality and PDP/cart polish are first-class product work.

### 2. Useful native capability — purchase justification
The theme needs a strong but curated set of commerce and storytelling capabilities relevant to the target vertical. Feature count is not the goal; recurring paid customization patterns determine priority.

### 3. Merchant/design-team control — retention and operating leverage
Expose meaningful structural and presentation choices through native Shopify settings, blocks, dynamic sources and compositions so ordinary iteration does not immediately become source-code work.

### 4. Clean extensibility — agency/developer leverage
When the boundary is reached, architecture should make a new section, structural variant or style treatment straightforward without fighting hidden coupling, global side effects or brittle JavaScript.

### 5. Testability — architecture property
High-value variables that brands reasonably experiment with should be exposed through native theme customization when doing so remains coherent and supportable. Do not build a custom experimentation layer or augment Shopify admin/editor behavior.

## Core design problem

The product must solve:

> **How do we productize a high-value subset of recurring agency customization work without turning the Shopify editor into an airplane cockpit?**

The answer is not a universal section.

Use:

- strong defaults;
- multiple purpose-built composition variants where the shopper experience is materially different;
- conventional merchant-facing names;
- shallow blocks;
- semantic global tokens;
- bounded local controls;
- dynamic-source compatibility;
- optional structured data with complete zero-setup fallbacks;
- app-block insertion points where appropriate;
- progressive enhancement;
- clean developer contracts.

Do not use:

- arbitrary per-block CSS as a normal workflow;
- dozens of cosmetic toggles to simulate structural flexibility;
- vertical-mode switches;
- proprietary editor state;
- merchant-facing CRO jargon;
- deep nesting without a demonstrated need;
- a catch-all "build anything" section.

## Initial product surfaces to investigate

These are **candidate productization areas**, not an approved feature checklist.

1. **PDP purchase area / buy box**
   - materially different purchase compositions rather than cosmetic variants;
   - variant and selling-plan correctness;
   - merchant-controlled supporting messages/content;
   - mobile purchase behavior;
   - app-block compatibility.

2. **Product media**
   - polished gallery compositions;
   - objective/product-specific badges;
   - mixed-media resilience;
   - mobile media behavior.

3. **Product education**
   - benefits, ingredients/materials, usage, specifications, FAQs, proof/results and comparison;
   - standard-data fallback plus optional dynamic sources;
   - honest-claims guardrails.

4. **Cart**
   - excellent cart page/drawer presentation;
   - correct native cart behavior;
   - legitimate progress/messaging based on factual thresholds;
   - complementary merchandising without app-like discount logic.

5. **Content/storytelling sections**
   - enough composition range for designers to produce meaningfully different pages;
   - not a giant generic section catalog.

6. **Collection merchandising**
   - strong product cards;
   - promotional/story tiles;
   - flexible collection headers;
   - filtering/sorting correctness.

7. **Design system**
   - enough control for meaningful brand refreshes;
   - constrained enough to preserve coherence;
   - structural variation should not be faked with hundreds of micro-settings.

## Explicit non-goals

The theme is not:

- a replacement for designers;
- a replacement for developers;
- a proprietary page builder;
- a generic "works for every industry" theme;
- an app replacement;
- a custom discount/bundle engine;
- a review/subscription/loyalty platform;
- a quiz/data-collection product;
- a fake urgency system;
- a promise that every design can be built without code.

## Originality strategy

Originality must emerge from the combination of:

- distinctive Beauty/Wellness-first art direction;
- recognizable product-card and commerce-surface design;
- materially useful composition systems;
- thoughtful high-value control contracts;
- coherent mobile behavior;
- unusually polished zero-setup states;
- clean system behavior under real catalog/content stress.

Extra sections, extra settings, renamed presets, metafields, Rollouts compatibility or CRO terminology alone do not establish originality.

## Foundation direction

ADR-001 remains provisional until its revalidation point. If current Shopify eligibility continues to permit the audited Skeleton foundation, use it only as a thin primitive base with recorded provenance and a strict inheritance ceiling. Otherwise use fully original code.

Dawn/Horizon-derived code remains prohibited for this project.

## Revised validation approach

The prior requirement for ten 30-minute interviews is not treated as completed by founder evidence, but it is also not allowed to create research theater or indefinitely block a time-bounded founder-led product.

Before production code, validate the **highest-risk assumptions**, not an arbitrary interview count:

1. **Customization-demand inventory:** extract at least 15 recurring DCL requests from real historical work and group them into reusable patterns.
2. **Incumbent capability challenge:** for the highest-value patterns, determine whether current strong premium themes already solve them well. Mark solved patterns as table stakes or remove them.
3. **Complexity test:** proposed controls must demonstrate that added merchant power does not simply move developer complexity into giant settings panels.
4. **Visual originality review:** establish a distinctive Beauty/Wellness art direction and surface system before production implementation.
5. **Commercial founder gate:** explicitly accept Theme Store exclusivity, support obligations, demo investment and product ownership.
6. **Official-requirements revalidation:** repeat at the documented architecture/implementation gates.

Independent merchant evidence remains valuable and should be collected opportunistically, but the project must not fabricate it or claim the founder interview is equivalent to ten merchants.

## M1 must now answer

M1 is no longer a five-workflow "job composition" experiment.

It must answer:

- Which recurring DCL customization patterns are worth productizing?
- What are the minimum useful structural variants for PDP, media, cart, collections and storytelling?
- Which controls belong globally, locally, in blocks, or in product data?
- Can a designer create materially different polished outcomes without source edits?
- Can a merchant safely operate those outcomes afterward?
- Does the system remain understandable with realistic settings counts?
- Does zero-setup content still look premium?
- Can developers extend it without fighting architecture?
- Does the Beauty/Wellness reference direction look fundamentally distinct from incumbent themes?
- Does the system stay within current Theme Store requirements and internal performance/accessibility budgets?

## Commercial decision

**BUILD DIRECTION: YES, CONDITIONALLY.**

Proceed to revised M1 product definition/prototyping once the remaining finite M0 reconciliation tasks are completed. Do not start production Liquid/CSS/JS merely because the thesis is stronger.

The commercial bet is not "merchants cannot launch products." It is:

> Growing DTC brands repeatedly pay for design and storefront flexibility beyond what their current themes expose. DCL can productize a meaningful portion of those recurring requests into a visually exceptional, merchant-operable theme while keeping the implementation clean enough for the custom work that remains.

That is the thesis future work must prove or kill.
