# M2A foundation and core commerce completion report

Checked 2026-10-06. Overall engineering disposition: **NARROW**. Original production source is implemented and packaged; actual Shopify-store execution remains unverified. This is not Theme Store compliance or accessibility certification.

## Identity and scope

Branch: `m2-production-theme`. Foundation base: `5d7396fdd4b4e5fbaa61334852bfc5a37775255e`, whose parent is accepted M1 closure `da7da33153648575f53bcf088d32dd7bedc1ceea`. Initial production commit: `93b86fa90f3ab36f277817af1034d6f5373df9ba`. Production root: `theme/`. Final report commit is identified by Git history; this file cannot embed its own commit hash. See changed-file-manifest.json for the complete baseline-relative manifest.

No preserved prototype, M1 workflow, original controlling document or ADR was modified. No imported theme source, framework, Sass, minified first-party asset or config/markets.json. No merge or PR.

## Major-area dispositions

| Area | Disposition | Evidence and limitation |
|---|---|---|
| Original distributable foundation | PASS | Real Liquid, schemas, groups, locales and 66-file supported-directory ZIP; package-source identity verified. Store installation not executed. |
| Globals/document/navigation | PASS | settings_schema.json, theme-tokens, layouts, header/footer groups, native nested disclosures, shopify-account, skip link and untouched content_for_header. Actual platform-generated account UI untested. |
| Balanced/shared product truth | NARROW | Shared product-surface, native forms and 33 focused tests; actual Shopify rendering/purchase/plan execution untested. |
| Standard Grid/product card | NARROW | main-collection, filters, pagination and product-card; native filters tested through explicit adapters, not a real catalog. |
| Native cart | NARROW | Real Shopify POST/update/remove/checkout semantics and optional native module, key-based unit contracts; live mutation/checkout untested. |
| Ancillary templates | NARROW | All required templates exist and pass Theme Check; platform form/media/gift behavior requires real store execution. |
| App/editor foundation | NARROW | main/featured @app and apps wrapper, normal-flow guest containment and cleanup architecture. No installed app extension or Theme Editor test. |
| Localization/Markets | NARROW | localization forms, country/language lists, locale keys, currency-safe filters and logical CSS. Only English base strings shipped; actual Markets/RTL untested. |
| Accessibility/responsiveness | NARROW | Semantic/focus/labels/target/reduced-motion foundations; component browser/axe results below. No certification, AT/zoom or complete-platform audit. |
| Performance | NARROW | Static asset budgets PASS; populated-store Lighthouse, media/font/LCP and third-party impact unmeasured. |
| CI/local tooling | See execution record below | Real CLI Theme Check plus structural/unit/browser/package checks, explicit test-adapter limits. |

## Required template inventory

JSON: `404`, `article`, `blog`, `cart`, `collection`, `index`, `list-collections`, `page`, `page.contact`, `password`, `product`, `search`. Liquid: `gift_card`. Both theme and password layouts. Header/footer JSON section groups. Custom Liquid is available across section-supported contexts; generic apps wrapper dispatches actual Shopify app blocks.

## Merchant controls and blocks

19 editable globals: 17 presentation controls plus logo/favicon. Two font roles and type scale; four paired foreground/background roles, accent, width, rhythm, radius, border and motion. Focus is enforced by CSS, not an optional merchant toggle. No arbitrary coordinates, raw CSS, per-device builder or duplicated content.

Main product has zero section settings; featured product has one product selector. Both share title/vendor/price/options/plans/quantity/buy/description/pickup/Custom Liquid/@app block architecture. Nine default blocks; maximum15. Individual core blocks limit1; Custom Liquid limit3. Buy block has two platform controls: accelerated checkout and gift recipient, both default true. Header one menu; footer menu/social URL/social label (3); homepage heading/collection (2); Custom Liquid section one content control; generic apps section none. Platform app-owned controls are external to this budget. Block reordering is implemented, not live merchant-usability certified.

## Commerce/native fallback

Server-native selected_or_first_available_variant initializes truth. Deep links and option-value URLs preserve null/nonexistent tuples and sold-out identities. Native full-page variant navigation refreshes price/compare/unit/availability/media/form together; no bulk variant blob or client money model. Swatch image/color uses Shopify values. Compare-at requires greater price. Variable cards label from-price and representative unit identity explicitly.

Selling-plan GET selection refreshes allocation before purchase. Required allocation cannot fall back silently to one-time; missing/invalid allocation blocks purchase. Variant quantity min/max/increment and external form association are maintained; removing quantity block submits rule minimum. Gift recipients use official properties/limits and suppress incompatible dynamic checkout. Payment button/terms and cart accelerated checkout are Shopify-generated.

Product/cart remain native HTML forms without JS. Option links and plan GET remain navigable; cart supports native updates/removal/notes/checkout. Optional cart enhancement uses unique line keys, abort/timeouts, pending-action locking and localized/server errors. Tests include duplicate property/plan identity, invalid quantity and retry. Predictive search failure retains native search. No local test is claimed as an actual Shopify product→cart journey.

## Media, accessibility and budgets

Shopify image_url/image_tag responsive widths240–1600, sizes, dimensions and aspect ratios; primary selected media eager, remaining/featured lazy. Native video/external-video/model architecture; model platform runtime and QR vendor asset are conditional. No first-party raster/font binary or third-party theme runtime dependency. Fonts use Shopify font_picker/font_face with swap.

CSS uses logical properties, visible focus,44px target design, reduced motion and one semantic DOM source. Navigation is native disclosure with Escape/focus restoration. Guest app width is contained without page-level overflow; this is not proof of third-party app accessibility. Test-only rendering adapters and explicit mocked error responses are excluded from theme ZIP.

Gzip bytes: base.css2275; global navigation467; cart1002 + cart-state412; search895; media363; gift-card282. All owned JS3421 bytes gzip in aggregate. Internal ceilings: CSS45KB, globalJS25KB, routeJS20KB, totalJS45KB. All static ceilings pass. Lighthouse internal targets90 performance/95 accessibility and Shopify floors are separate unmeasured production gates.

## Execution boundaries and exceptions

Local actual Shopify CLI4.8.4 Theme Check with --fail-level warning returns []: zero errors/warnings, recommended rules without suppressions. Missing-render negative control detects MissingTemplate. Local structural checks1086/1086 PASS (including baseline preservation hashes; these are not1086 functional scenarios). Node unit tests33/33 PASS using actual authored snippets/pure cart code with explicitly test-only platform adapters. Actual CLI package verifies66 files/source identity; local ZIP SHA256691d62a62875302099c30ab9f5833c610807529b7e9a108a5adb1c588139c6b1,38982 bytes. ZIP timestamps can change archive hash across executions.

Local Chromium launch was blocked by macOS bootstrap_check_in permission error; browser-local-attempt.json records environmental failure without functional verdict. Git push credential lacked workflow scope; established GitHub connector published the exact uploaded commit/ref. First Actions run37510255337 rejected job-scope runner.temp expression before jobs; fixed to bounded Ubuntu /tmp path in4350553d786a358e4ab210f88910f32c9727d6e1. This was a CI configuration defect, not a theme functional result.

## Known untested production gates

Authorized Shopify development store upload/clean install and full product→cart→checkout journey, including JS off; actual Shopify Liquid/platform output, high-variant/combined-listing catalogs, selling plans/quantity rules/server errors/discount and property concurrency; real gift recipient delivery/QR/wallet, video/external-video/3D playback, pickup, accelerated checkout/Shop Pay/account/Shop-follow controls; actual Theme Editor load/unload/reorder/block selection and merchant usability; installed @app/app embeds, real dynamic sources/metafields/metaobjects and external app isolation; real native filtering/predictive search catalog; Markets/presentment currencies/language switching, translations/RTL; accessibility certification including AT, zoom/reflow and third-party controls; cross-browser/touch/mobile device testing; populated-store Lighthouse and measured media/font/LCP/third-party performance; SEO/social crawl verification; complete full-theme/submission requirements and demo/provenance review. Native interfaces and local adapter assertions do not close these gates.

## Next production systems — not implemented

Compact PDP, Editorial PDP, Evidence Rail, Commerce Mosaic/Anchor Cadence, Split Tension/Guided Set. No signature production layer started. Stop for M2A foundation review.

## Ubuntu CI execution record

**PASS**: [M2 Production Theme run37510381753](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37510381753), source commit4350553d786a358e4ab210f88910f32c9727d6e1. Ubuntu24.04, Shopify CLI4.8.4, Playwright1.62.1, Chromium151.0.7922.34. Theme Check zero errors/warnings; structural1086/1086 PASS; unit33/33 PASS; browser113 assertions PASS. Browser matrix:3 component routes ×8 widths ×2 JS settings =48 observations; widths320/375/390/430/768/1024/1280/1440,900px height. Actual browser contexts use javaScriptEnabled true/false and verify script execution accordingly.12 full-page JPG screenshots: product/cart/guest ×390/1440 ×js-on/js-off. Paths: docs/m2/evidence/ci/{product,cart,guest}-{390,1440}-js-{on,off}.jpg.

Axe component checks: product/cart zero recorded violations; incomplete checks retained in browser-results.json and do not constitute certification. Native form association, navigation Escape/focus, mocked422 cart retry, predictive failure, reduced motion and custom-element reconnect checks pass. Guest layout uses test-only tall/wide content; it is not a real app extension. No native Shopify purchase was submitted.

Machine artifacts: docs/m2/evidence/ci/browser-results.json, structural-results.json, theme-check.json, unit-output.log, browser-output.log, package-results.json, workflow-output.log; run metadata at docs/m2/evidence/ci-run.json. GitHub artifact: m2a-production-4350553d786a358e4ab210f88910f32c9727d6e1 (30-day retention). Package66 files/source-identical. Downloaded ZIP excluded from Git. CI emitted upload-artifact v5 Node20 deprecation warning with forced Node24 execution; job completed successfully. No theme source changed after this passing run. Final documentation/evidence-only commit is excluded by workflow path filters.

Executed commands: shopify theme check --path theme --fail-level warning --output json; python3 tests/m2/validate.py; npm --prefix tests/m2 test; npx playwright install --with-deps --only-shell chromium; timeout180s npm --prefix tests/m2 run test:browser; shopify theme package --path theme; python3 tests/m2/package-check.py.

Final state: implementation committed/published, completion evidence recorded, working tree clean after final report commit. Overall NARROW remains because actual store/integration/performance gates above have not executed. Stop for foundation review.
