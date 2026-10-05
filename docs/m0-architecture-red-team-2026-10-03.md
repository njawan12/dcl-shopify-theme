# M0 architecture red-team — 2026-10-03

## Decision being attacked

Can DCL create a job-oriented, bounded-decision premium theme without building a proprietary page builder, duplicating Shopify's editor mental model, violating Theme Store expectations, creating performance debt, or hiding complexity behind presets?

## Red-team verdict

**Potentially yes, but only under a constrained architecture.**

The dangerous version of the concept is an internal “Launch Narrative System” implemented as custom workflow state, deeply nested generic blocks, vertical modes, or a second editing abstraction. Reject that architecture.

The defensible version is Shopify-native:

- job-oriented **starting compositions/templates** for merchant intent;
- conventional, content/function-named sections and blocks underneath;
- semantic global design tokens;
- bounded section-level emphasis/layout choices;
- optional native dynamic sources/metafields/metaobjects;
- standard-data-first storefront states;
- app blocks at supported seams;
- server-rendered semantic HTML;
- minimal progressive-enhancement JavaScript.

The merchant may start from “Product Launch,” but once editing, they should encounter understandable Shopify-native concepts such as product information, image and text, product list, comparison, rich text, media, testimonials/proof where honest, and app blocks—not proprietary “Reveal/Explain/Prove/Act” controls.

## Architectural threats

### A1 — Proprietary workflow abstraction

**Failure mode:** Launch Narrative becomes merchant-facing infrastructure or hidden state controlling multiple pages.

**Why it fails:** It creates a second mental model, increases support, risks brittle cross-template coupling, and can make the theme feel app-like.

**Constraint:** Reveal/Explain/Prove/Compare/Act remains an internal design responsibility grammar. Merchant-facing names use Shopify-native/content-oriented terminology. Job names may exist at the starting-composition/template level when useful.

### A2 — Preset renaming masquerading as innovation

**Failure mode:** “Product Launch” is merely generic sections in a different JSON order.

**Why it fails:** It is commercially weak and likely insufficient for the originality thesis.

**Constraint:** A job composition must demonstrate a measurable difference in decision economy, defaults, omission behavior, mobile priority, cross-surface handoff, and recovery—not just order/naming.

### A3 — Complexity displacement

**Failure mode:** Fewer visible sections but each section has dozens of controls, conditional panels, modes, and exceptions.

**Why it fails:** Cognitive load has moved rather than disappeared.

**Constraint:** Maintain setting-count budgets, progressive disclosure, semantic global tokens, and bounded local controls. Every exception setting requires evidence.

### A4 — Universal-section architecture

**Failure mode:** one giant “content” section with arbitrary nested blocks tries to render everything.

**Why it fails:** poor semantics, hard accessibility, editor confusion, weak preview-inspector behavior, testing explosion, performance risk.

**Constraint:** Prefer purpose-specific sections with logical block flow. Use theme blocks only where reuse materially helps merchant editing. Do not optimize for theoretical composability.

### A5 — Deep nesting as flexibility

**Failure mode:** nested theme blocks become the primary differentiator.

**Why it fails:** Shopify warns against unnecessarily deep nesting/complicated configuration. Logical reading order and editor usability become harder.

**Constraint:** nesting is earned case-by-case. Default to shallow composition; cap depth by tested need, not platform maximum.

### A6 — Client-side rendering/state machine

**Failure mode:** JavaScript constructs primary page content or owns basic commerce state.

**Why it fails:** resilience, accessibility, editor lifecycle, SEO and performance degrade.

**Constraint:** meaningful content and primary commerce UI render server-side in Liquid. JS enhances interactions only. No SPA/framework runtime.

### A7 — Over-componentized Liquid

**Failure mode:** “clean architecture” becomes chains of tiny nested snippets/renders.

**Why it fails:** Shopify's current performance guidance explicitly warns that nested renders, especially inside loops, compound Liquid rendering cost.

**Constraint:** component boundaries follow meaningful complexity/reuse. Avoid nesting trivial renders. Measure collection/product-grid paths with Theme Inspector.

### A8 — Metafield dependence

**Failure mode:** premium appearance requires merchants to build structured content before the theme looks complete.

**Why it fails:** contradicts zero-setup quality and increases onboarding/support.

**Constraint:** standard Shopify product/collection/page data must render a polished complete state. Structured data only enhances. Deleted/disconnected sources fail safely.

### A9 — Fake cross-page synchronization

**Failure mode:** product launch content appears “connected everywhere” through unsupported magic.

**Why it fails:** theme architecture cannot honestly promise app-like content orchestration without merchant data modeling and platform constraints.

**Constraint:** use native references/dynamic sources and documented recipes. Cross-surface continuity is a design/content contract, not hidden synchronization.

### A10 — Vertical abstraction pollution

**Failure mode:** Beauty, apparel and food support creates “industry mode,” generic labels, schema forks, or dozens of conditional settings.

**Why it fails:** raises support/test burden and weakens art direction.

**Constraint:** architecture remains domain-neutral only where the underlying merchant job is genuinely shared. Otherwise narrow the product/preset strategy.

### A11 — Editor lifecycle bugs

**Failure mode:** JS works on page load but breaks when Shopify dynamically adds/removes/reorders/rerenders sections or blocks.

**Constraint:** every interactive module must survive Shopify editor lifecycle events, reinitialization and teardown without duplicate listeners/state. Section/block selection must remain visible and inspectable.

### A12 — Performance collapse under realistic catalogs

**Failure mode:** product grids, variants, metafields, nested loops, media and apps make a beautiful demo slow in real stores.

**Constraint:** avoid O(n²) Liquid patterns, variant over-fetching, metafield access inside loops, excessive nested renders and indiscriminate media loading. Performance fixtures must include realistic catalog/content density.

### A13 — Demo-store illusion

**Failure mode:** award-quality impression depends on perfect photography, short English copy, ideal product ratios and hand-curated data.

**Constraint:** design review must include ugly-but-real fixtures: mixed image ratios, long translations, no media, long titles, sold-out states, dense legal copy, missing structured data, uneven product counts and app insertion.

## Shopify alignment verified during red-team

Current official Shopify guidance supports the constrained direction:

- Theme editor customization should be clear, intuitive and merchant-first, balancing flexibility with opinionated settings.
- Settings should be logically grouped and use merchant-friendly language.
- Section names should describe function; preset names should relate to content type.
- Sections/blocks should follow logical reading flow regardless of sequence.
- Shopify editor actions dynamically rerender DOM fragments, so JS must handle editor lifecycle rather than only initial page load.
- Themes need required JSON templates, section support, product-page blocks and required app-block contexts.
- Current Theme Store Lighthouse floor remains average 60 performance and 90 accessibility across home/product/collection on desktop and mobile; DCL's internal targets remain stricter.
- Shopify performance guidance warns against nested Liquid loops, metafield work inside loops, variant over-fetching and deeply nested render chains.

## Architecture invariants proposed for eventual M2

These are candidate hard constraints pending M1 validation:

1. No proprietary editor or workflow state machine.
2. No merchant-facing Launch Narrative jargon.
3. Job intent exists at composition/template/onboarding level; primitives remain content/function named.
4. Standard Shopify data produces a complete premium storefront.
5. Structured data enhances; never unlocks baseline quality.
6. Server-render first; JS progressive enhancement only.
7. Shallow, purpose-driven section/block trees.
8. No universal catch-all section.
9. No vertical-mode setting.
10. No arbitrary per-block CSS/custom styling controls as normal workflow.
11. Global semantic tokens carry most brand expression.
12. Local controls change meaningful composition/emphasis, not compensate for weak defaults.
13. Interactive code is editor-lifecycle safe.
14. Commerce correctness outranks visual novelty.
15. Performance is tested with realistic density, not empty demo fixtures.
16. Every “flexibility” feature must justify its support/testing cost.

## What would make the architecture genuinely distinctive

Originality should emerge from the **system behavior**, not exotic code:

- excellent job-specific defaults;
- intentional omission as well as inclusion;
- coherent mobile priority encoded in compositions;
- standard-data states that already look designed;
- predictable handoff between campaign/collection/product surfaces;
- semantic brand roles that propagate safely;
- bounded recovery choices for common content failures;
- fewer consequential merchant decisions without losing the capabilities the target segment actually uses.

If those cannot outperform a strong incumbent premium-theme baseline in M1, do not compensate by adding more settings or engineering novelty. Narrow or stop.
