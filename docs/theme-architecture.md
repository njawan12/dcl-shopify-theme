# Theme architecture

## Prototype disposition

Repository inspection on 2 October 2026 found an empty Git tree: no prototype, configuration, assets, or tests.

| Category | Result |
|---|---|
| KEEP | Nothing |
| REWRITE | Nothing |
| DELETE | Nothing |
| NEEDS INVESTIGATION | Git remote/history and intended packaging/CI remain unknown |

Decision: start an original foundation only after the approved-starting-code rule and product hypothesis are validated. There is nothing to preserve.

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
- `page.campaign.json` is a reusable landing canvas; merchants assign it rather than duplicate Liquid.
- Product flexibility comes from blocks in the main product section and dynamic sources, not dozens of alternate templates.
- Section groups own announcement/header/footer surfaces.
- Preset JSON is treated as product UX and versioned/tested.

## JavaScript strategy

Server-render useful HTML. ES modules enhance only present components; use custom elements when lifecycle encapsulation is valuable, not as a framework substitute. Modules are idempotent under theme-editor reload/reorder events. Shared utilities cover focus, abortable fetch, pub/sub and section lifecycle. Cart, variant and filter states retain form/link fallbacks wherever Shopify permits.

## CSS strategy

Native cascade layers and custom properties: reset → base → tokens → components → utilities. Component selectors remain shallow. Section-scoped variables carry schema choices; no generated utility framework. Color schemes own foreground/background/accent pairs. Logical properties prepare for localization and RTL feasibility.

## App and data contracts

Main product, featured product and selected content surfaces accept `@app`. Wrappers must not impose destructive widths. Native recommendations and complementary-product APIs are used where supported. No theme-owned reviews, subscriptions, loyalty, bundle engine or analytics.

## Architecture decision gates

- ADR-001: approved starting foundation after official revalidation.
- ADR-002: theme-block adoption/nesting based on current support and editor test.
- ADR-003: structured-content namespaces/recipes and portability.
- ADR-004: cart page first; drawer only if usability/performance evidence supports it.
- ADR-005: RTL product commitment versus feasibility-only support.
