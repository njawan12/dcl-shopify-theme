# Merchant usability principles

## Product rules

1. **A useful default is a feature.** Inserted sections must look complete after content replacement.
2. **Jobs, not implementation.** Say “Product spacing: Compact / Comfortable / Spacious,” never expose grid-gap pixels.
3. **Progressive disclosure.** Put the five-to-eight frequent decisions first; conditionally reveal advanced controls.
4. **Presets over knobs.** Presets encode art direction and remain editable, but do not expose every CSS possibility.
5. **Shallow structure.** Section → meaningful block → optional child only when the child is independently reusable/reorderable.
6. **Normal Shopify data first.** Product title, media, description, price and variants always produce a polished page.
7. **Structured data enhances.** Metafields/metaobjects add chapters; absence creates no blank headings or gaps.
8. **Safe boundaries.** Tokenized choices prevent unreadable widths, tiny targets and chaotic spacing.
9. **Honest preview.** Editor behavior matches storefront behavior and responds to editor lifecycle events.
10. **Apps are guests.** Generic app-block positions are visible and resilient; no vendor lock-in.

## Task acceptance criteria

| Merchant task | Success without code |
|---|---|
| Rebrand | Logo, favicon, schemes, two font roles, density, buttons/cards/corners changed globally in ≤10 minutes |
| Homepage | Start from a complete preset, reorder sections, replace content; no blank canvas required |
| Polished PDP | Reorder purchase/story blocks, select gallery mode, connect optional sources without creating Liquid templates |
| New product | Standard product data launches acceptably; enhancements are optional |
| Campaign page | Assign one campaign template, add job-named presets, publish without template duplication |
| Collection merchandising | Configure hero, filters, card quick add and promotion modules with legitimate data |
| Promotions | Use announcement, offer callout and promo tiles; no fake urgency |
| Product information | Reorder grouped blocks and accordions; no fragment-per-block clutter |
| Apps | Add `@app` blocks at documented surfaces |
| Product-specific content | Connect compatible section settings to dynamic sources |
| Reusable content | Reference documented metaobject recipes where Shopify supports the connection |
| Distinct pages | Combine bounded compositions while inheriting brand tokens |

## Setting budgets

- Typical section: ≤12 visible settings initially and ≤8 advanced settings.
- Typical block: ≤8 visible settings.
- No numeric range when a semantic 3–5 option choice suffices.
- One global control owns a visual rule unless a strong content-specific exception exists.
- Every new setting needs an observed merchant job, default, empty state, localization string and support-risk assessment.

## No-developer test

For every common scenario: give a marketing manager representative content, observe without coaching, and require ≥80% task completion, no code use, no critical accessibility defect, and median completion within the task target. Uncommon failures do not justify global complexity; document the workaround or app boundary.

## Structured content onboarding

Ship documentation recipes, not required definitions. Use namespaced definitions only after confirming Theme Store rules and portability. Demonstrate a zero-setup PDP, then optional benefits/usage/ingredients/FAQ enhancement. Never hide critical purchase information solely in a metaobject.
