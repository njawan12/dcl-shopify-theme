# Post-M1 official foundation revalidation

**Checked:** 2026-10-05. **Baseline:** `da7da33153648575f53bcf088d32dd7bedc1ceea`. Only official Shopify documentation/Shopify-owned source establish external requirements. Product judgments are in [ADR-001](adr/001-theme-foundation.md). Historical snapshots are context, not this check. No production code, upload, execution certification or Shopify approval occurred.

## Current policy findings

[Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), checked 2026-10-05: Skeleton or fully original foundation; no new Dawn/Horizon-derived submissions; structural whole-experience differentiation. JSON resource templates, header/footer groups, block-based main product, main/featured `@app` and Custom Liquid are required. Exclude `config/markets.json`; metaobject-setting types use standard definitions. Populated home/product/collection desktop/mobile Lighthouse averages:Performance 60 / Accessibility 90. Additional semantic/keyboard/contrast/target criteria apply. Font picker, paired color roles, account/Shop controls, commerce/discovery features, realistic demos, exclusive distribution and support/package obligations remain applicable. M1 acceptance establishes none of these as production compliance.

## Dated official-source register

Every row opened/rechecked **2026-10-05**. Policy, platform contracts and best-practice advice are separate; advice is not a certification.

| ID | Official URL | Role / foundation consequence |
|---|---|---|
| S01 | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) | Submission policy; final artifact must satisfy the complete current page, not just this summary. |
| S02 | [Skeleton repository](https://github.com/Shopify/skeleton-theme) | Active official source; not a compliance certificate. |
| S03 | [Main commit](https://github.com/Shopify/skeleton-theme/commit/a7a655e79b21e68316c228dc7e437b0b32550888), [README](https://github.com/Shopify/skeleton-theme/blob/a7a655e79b21e68316c228dc7e437b0b32550888/README.md) | Direct blocks/gated partials; unsuitable dependency for chosen architecture. |
| S04 | [Stable release](https://github.com/Shopify/skeleton-theme/releases/tag/v1.0.0), [stable tree](https://github.com/Shopify/skeleton-theme/tree/8b8a1f4d2ef437d4d60df7a9cc4770f85a2f1b76) | Latest published stable considered independently of main. |
| S05 | [Stable license](https://github.com/Shopify/skeleton-theme/blob/8b8a1f4d2ef437d4d60df7a9cc4770f85a2f1b76/LICENSE.md), [main license](https://github.com/Shopify/skeleton-theme/blob/a7a655e79b21e68316c228dc7e437b0b32550888/LICENSE.md) | Actual restricted license overrides badge shorthand; ADR records obligations. |
| S06 | [Architecture](https://shopify.dev/docs/storefronts/themes/architecture) | Supported assets/blocks/config/layout/locales/sections/snippets/templates, permitted template subdirectories. Upload minimum is not submission completeness. |
| S07 | [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) | Serialization/section composition; platform caps are outer limits, not our control target. |
| S08 | [Section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) | Editable layout header/footer groups. |
| S09 | [Section schema](https://shopify.dev/docs/storefronts/themes/architecture/sections/section-schema) | Settings/presets/caps/context restrictions/editor validity. |
| S10 | [Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks) | Local blocks do not nest or mix with theme blocks in a section; shared snippets do not require extra editor controls. |
| S11 | [App blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) | Generic dispatch/wrapper; theme cannot substitute static app insertion. Test real extensions. |
| S12 | [Extension configuration](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration) | App embeds have separate activation/target/lifecycle. |
| S13 | [Dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources) | Compatible setting types/resource context; manual baseline is our product decision. |
| S14 | [Product template](https://shopify.dev/docs/storefronts/themes/architecture/templates/product/overview) | Native purchase/resource contract, not prototype transport. |
| S15 | [Cart template](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart) | Lines/native update/checkout/server totals. |
| S16 | [Country/language UX](https://shopify.dev/docs/storefronts/themes/markets/country-language-ux) | Native localization and store-supported countries/locales. |
| S17 | [Accessibility](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility) | Semantic/focus/keyboard/media alternatives/manual tests; Lighthouse alone insufficient. |
| S18 | [Performance](https://shopify.dev/docs/storefronts/themes/best-practices/performance) | HTML-first, restrained JS, responsive CDN media and priority; measure real populated preview. |
| S19 | [Theme Check](https://shopify.dev/docs/storefronts/themes/tools/theme-check) | Actual Liquid/schema diagnostics; review suppressions, no full-certification inference. |
| S20 | [CLI package](https://shopify.dev/docs/api/shopify-cli/theme/theme-package) | Supported-directory ZIP, not repository archive. |
| S21 | [Submission](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme) | Partner/ZIP review, licensing and external approval. |

## Inspection scope and identity

Read-only reference retrieved from `https://github.com/Shopify/skeleton-theme.git`; none copied into this repository. Repository/release metadata and immutable commits were inspected. Main is the current head observed; v1.0.0 is the latest published non-prerelease release observed, not a permanent guarantee.

Stable manifest: 53 files. Decision-bearing reads: README/license, layout/theme, image/meta-tags/css-variables snippets, critical CSS, group/text blocks, header/product/cart sections, header/footer groups and product template, settings schema, default storefront locale and schema labels, Theme Check config and CI. Main README/actual license checked for dialect/gate. No live Shopify execution or comparative performance measurement on either candidate.

Stable's inspected product/cart/header/group code supplies scaffold rather than the required system. Current main's documented gate conflicts with our general-storefront dependency policy. Official foundation eligibility is not interpreted as submission approval of main unchanged. Fully original public-contract implementation resolves the mismatch without importing or repairing a starter.

## Build accountability

[M2 checklist](m2-production-entry-checklist.md) separates initial foundations, incremental evidence and submission. Batch B `shopify-register.md` retains detailed thirty-row product traceability; this refresh confirms foundation facts without overwriting accepted M1 findings. Owners must add new official changes and actual production evidence to the production register rather than treating old notes as current compliance.

No independent foundation/licensing blocker found for option B. Production/integration/certification work is deferred, not PASS. Recheck relevant pages at implementation and every submission requirement before release.
