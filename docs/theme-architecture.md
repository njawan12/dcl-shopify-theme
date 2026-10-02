# Theme architecture

## Prototype disposition

Repository inspection on 2 October 2026 found an empty Git tree: no prototype, configuration, assets, or tests.

| Category | Result |
|---|---|
| KEEP | Nothing |
| REWRITE | Nothing |
| DELETE | Nothing |
| NEEDS INVESTIGATION | Git remote/history and intended packaging/CI remain unknown |

Verified foundation constraint as of 2 October 2026: use **Skeleton Theme or fully original code only**. Dawn and Horizon are excluded from new Theme Store submissions. ADR-001 will choose between the two eligible paths before production implementation; there is nothing in this repository to preserve.

## Proposed distributable tree

```text
assets/       CSS, small progressive-enhancement modules, icons
blocks/       reusable merchant-facing theme blocks
config/       settings_schema.json and generated settings_data.json
layout/       theme and password shells
locales/      storefront and schema translations
sections/     page/section-group compositions
snippets/     private rendering primitives and utilities
templates/    JSON/Liquid templates required by Shopify
```

Development-only documentation, tests and tooling live outside the packaged archive (`docs/`, `tests/`, configuration files). A packaging allowlist prevents unsupported files from shipping.

## Layer model

1. **Data:** Shopify objects first; optional metafields/metaobjects via dynamic sources.
2. **Primitives:** price, media, responsive image, icon, focus trap, disclosure, product form.
3. **Merchant blocks:** grouped purchase info, benefit list, story media, accordion group, app block.
4. **Sections:** compositions such as Product core, Narrative chapter, Collection grid, Campaign reveal.
5. **Templates/groups:** thin JSON ordering and defaults.
6. **Tokens:** color schemes, type roles, spacing/density, widths, surfaces, radii and motion.

Business logic belongs in one snippet/module. Blocks express merchant intent, not implementation fragments.

## Template strategy

- One excellent default per required resource.
- Native JSON templates and section presets provide five intent-led starts: Product Launch, Paid Landing Page, Collection Launch, Editorial Story, and Product Education. Exact template count/names are an M1 decision; do not create one template per permutation.
- A campaign/landing template is a bounded native canvas; merchants assign it rather than duplicate Liquid. It is not a proprietary page builder.
- Product flexibility comes from blocks in the main product section and dynamic sources, not dozens of alternate templates.
- Section groups own announcement/header/footer surfaces.
- Preset JSON is treated as product UX and versioned/tested.

## Composition contracts

**Reveal → Explain → Prove → Compare → Act** is responsibility metadata used in briefs, schemas, defaults, and QA—not a runtime funnel or mandatory sequence. Sections have one primary responsibility and can serve more than one job context without becoming universal containers. PDPs preserve a factual purchase core; collections preserve product/filter semantics; landing pages choose only the stages needed; mobile priority may reorder or condense supporting content while preserving meaning.

Shared contracts describe durable intent (hero/reveal, benefit/explanation, evidence/proof, comparison, purchase/CTA), while preset copy and default content express Beauty & Wellness. A proposed adjacent preset must reuse these contracts with no vertical-mode switch, no unexplained generic settings, and no material increase above setting budgets. Otherwise an ADR must recommend narrowing.

## JavaScript strategy

Server-render useful HTML. ES modules enhance only present components; use custom elements when lifecycle encapsulation is valuable, not as a framework substitute. Modules are idempotent under theme-editor reload/reorder events. Shared utilities cover focus, abortable fetch, pub/sub and section lifecycle. Cart, variant and filter states retain form/link fallbacks wherever Shopify permits.

## CSS strategy

Native cascade layers and custom properties: reset → base → tokens → components → utilities. Component selectors remain shallow. Section-scoped variables carry schema choices; no generated utility framework. Color schemes own foreground/background/accent pairs. Logical properties prepare for localization and RTL feasibility.

## App and data contracts

Main product, featured product and selected content surfaces accept `@app`. Wrappers must not impose destructive widths. Native recommendations and complementary-product APIs are used where supported. No theme-owned reviews, subscriptions, loyalty, bundle engine or analytics.

Core storefront behavior must not depend on an app or API-backed app-like theme functionality. App blocks are optional extension surfaces: removing or never installing an app cannot make the theme's promised core experience incomplete.

## Architecture decision gates

- ADR-001: choose Skeleton Theme or fully original code, with provenance, licensing, originality, maintenance, and delivery trade-offs; Dawn and Horizon are excluded.
- ADR-002: theme-block adoption/nesting based on current support and editor test.
- ADR-003: structured-content namespaces/recipes and portability.
- ADR-004: cart page first; drawer only if usability/performance evidence supports it.
- ADR-005: RTL product commitment versus feasibility-only support.
- ADR-006: intent-led native template/preset map and merchant naming after editor prototype tests.
- ADR-007: multi-vertical fitness decision after Beauty & Wellness, apparel, and food/beverage content stress tests; narrowing is an acceptable result.

Theme Store approval is a hard architecture constraint. Supported directories, Online Store 2.0 templates/sections/blocks, shallow configuration, editor lifecycle, optional app blocks, performance, accessibility, responsiveness, localization, required commerce behavior, per-preset demo quality, support obligations, and prohibited-function boundaries enter ADR acceptance criteria. The dated verified baseline and remaining unknowns live in `shopify-requirements.md`; no unchecked implementation item is compliance.
