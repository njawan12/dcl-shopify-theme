# M2 production-build entry checklist

2026-10-05. Authority: accepted [ADR-001](adr/001-theme-foundation.md), [official-source register](post-m1-foundation-revalidation-2026-10-05.md), [engineering standard](engineering-compliance-standard.md), [performance budget](performance-budget.md), [M1 closure](m1-final-closure-verdict.md). **Fully original foundation; no Skeleton production pin.** M1 remains 12/12 PASS. This is an implementation contract, not evidence of completed production work.

This supersedes conditional foundation and pre-M1 composition assumptions in historical `theme-architecture.md` / `development-roadmap.md` only where they conflict with ADR-001 or accepted M1 direction. General engineering/milestone guidance remains useful. Retired variants are not authorized. First production code is a subsequent task.

Statuses begin **NOT IMPLEMENTED / NOT VALIDATED**. Evidence must identify owner, tested commit/store/context, command/manual protocol, fixture, result and exceptions. Missing infrastructure means BLOCKED, never PASS. Local fixtures/M1 frames cannot close live release gates.

## A. Required from the first M2 production commit

Foundation implementation plus explicit interfaces/ownership must exist immediately; complete later commerce features are not demanded in the first commit. Route skeletons must not be reported as finished merchant features.

| Check | First-commit artifact / acceptance | Owner |
|---|---|---|
| A1 Provenance | Original `theme/` root; author/source/dependency/asset ledger outside package, no upstream theme code. Record actual tool versions/licenses. Preserve M1 identities and source manifests. | Engineering |
| A2 Pre-code preflight | Engineering §15 review before Liquid: applicable current rules; accessibility, commerce, LCP/media, editor, apps, localization/resilience, provenance risks and planned tests. This checklist does not replace change-specific review. | Implementation owner |
| A3 Directory/layout | Supported directories only; layout with locale, main/landmarks/skip link, untouched `content_for_header`, `content_for_layout`, editable header/footer groups. Docs/tests/CI/provenance stay outside package. List resource templates/stages. | Engineering |
| A4 Initial schema/routes | Valid native index/page foundation templates/groups with no missing references; config schema/data and truthful theme_info/support metadata, defaults, logo/favicon. Full feature templates close under B1. | Engineering |
| A5 Tokens/settings | Original semantic colors/type/spacing/media/focus tokens, Shopify font-picker strategy and at least four paired color roles. Production control ledger separates presentation/content/bindings/platform/shopper inputs and preserves accepted ceilings. No coordinates/raw-CSS setting/device builder. | Design + engineering |
| A6 Localization | Storefront/schema locales from first user-facing string; `t` keys, labels/error/plural conventions, lang/routes/logical CSS. Record RTL commitment/ADR-005 dependency; no premature certification claim. | Internationalization |
| A7 Sources/truth | Manual schema baseline, typed optional bindings and invalid/disconnected omission/fallback interfaces. Native resource/variant/line data only; no theme judgment of claim credibility or required custom/app-owned default definitions. | Content + engineering |
| A8 Editor/apps | Declare bounded section-local blocks/app slots for main/featured product and evidence/story; snippet reuse, no mixed models. Foundation Custom Liquid capability; genuine extension/embeds test plan and store prerequisite. Only implemented/tested hosts may claim live support. | Engineering + integration |
| A9 Commerce/cart interfaces | One native product-form/variant/plan/line-key contract and cart-page authority before consumers; errors/native fallback defined. No mock transport, client prices or pretend atomicity. Skeleton routes navigate; purchase validation closes under B2/B3. | Commerce |
| A10 Accessible fallback | Native controls, unique IDs/labels/visible focus and useful DOM order without JS. No layout JS/duplicate mobile DOM. Keyboard/reflow/JS-off smoke on introduced routes. | Accessibility + engineering |
| A11 Media/performance | CDN responsive sizing/dimensions/alt/focal-point policy, one LCP-priority owner, lazy lower media; adopt existing numeric budgets, route-scoped asset ownership and measurement plan. | Performance |
| A12 SEO/social | Shared escaped title/description/canonical/page_image/OG/Twitter mechanism. Structured data requires real resources; no fake ratings. Social destinations default empty. | Engineering |
| A13 Lifecycle | Supported-browser inventory; scoped/idempotent modules with unload/reload cleanup, stale-request abort, block-selection/focus ownership. CSS-first/reduced-motion baseline, no gated dialect. | Engineering + QA |
| A14 CI/package | Real Theme Check against `theme/`, schema/locale/reference/static gzip checks, pinned tools/actions and reviewed suppressions. Allowlisted package smoke excludes docs/tests/credentials/submission exclusions. Preserve prototype hashes. Real-preview measurements explicitly BLOCKED until prerequisites exist. | Release engineering |
| A15 System migration map | Link all accepted systems to immutable proof contracts; shared truth/order/caps and production-output tests. No redesign/held-system promotion or prototype-code-only assertions. | Product + engineering |

Accepted presentation ceilings from Batch B `controls.json`: globals 19; media 5 initial / 3 conditional; purchase 6 / 4; Note, Pair, Process and collection card 5 / 3 each; cart 5 / 3; story 6 / 3. These are ceilings, not targets or promises that every policy becomes an editable setting. Inventory any production platform-required setting separately and reconcile its usability impact instead of silently expanding signature controls. Content caps remain Note 3, Pair 4, Process 4 and Guided 2–5. Shallow semantic controls must survive real editor execution.

No first-commit exception is implicit. Missing foundation capability must be identified before claiming completion; fake platform/demo UI is not a workaround.

## B. Incremental feature validation

| Check / feature stage | Evidence necessary for closure | Owner |
|---|---|---|
| B1 Full architecture/templates | Layout/config; 404/article/blog/cart/collection/index/list-collections/page/contact/password/product/search JSON; gift-card Liquid. Correct groups/sections/context, add/reorder/remove and install defaults. Platform-supported account/checkout behavior, no dummy commerce. [JSON contracts](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates). | Engineering + QA |
| B2 Product/variant/plans | Live same-product truth in all three PDPs: option tuples/deep links/unavailable/sold-out/missing; price/compare/unit/tax; quantity/properties/plans/allocation/pickup; real errors/cart. Platform accelerated checkout/installments, native JS-off browser purchase. [Product](https://shopify.dev/docs/storefronts/themes/architecture/templates/product/overview). | Commerce |
| B3 Cart | Live line-key update/removal, properties/plans, allocations/discounts, limits/stock corrections, errors/concurrency/note/accelerated checkout. Native cart remains usable; any drawer is progressive enhancement with focus/error lifecycle. Guided does not promise unproven atomicity. [Cart](https://shopify.dev/docs/storefronts/themes/architecture/templates/cart). | Commerce + QA |
| B4 Markets/language/currency | Native localization form/lists/routes; server money/taxes/unit formatting, identity across switches, no client exchange rates. Locale parity/long translations observed. [Localization](https://shopify.dev/docs/storefronts/themes/markets/country-language-ux). | Internationalization + commerce |
| B5 Apps/embeds | Install genuine test extension; main/featured product, evidence/story and wrapper add/reorder/remove. Absent/awkward/tall/wide/repeated guest, editor reload/selection; embed activation/deactivation/targets. Custom Liquid dispatch; named tested extensions and vendor limits. [Blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), [extension lifecycle](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions/configuration). | Integration + QA |
| B6 Dynamic sources/evidence | Real compatible resource-context bindings; manual baseline, valid connection/deletion/invalid/disconnect, omitted media/labels/qualification and maximum text. Genuine merchant metrics/source/claim/testimonial/certification/comparison and explicit before/after labels. No mandatory data install or mega-component. [Dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources). | Content + integration |
| B7 Preserved systems | Accepted hierarchy in production: three same-data PDPs; Anchor Cadence/Grid same cards; Rail Note/Pair/ordered Process in PDP/editorial; Guided 2–5 inclusion/variant/aggregate. Relevant neutral/cross-vertical/long/missing/mobile/isolation checks on real output; polish cannot introduce variants. | Product + engineering |
| B8 Merchant editor | Execute real merchant tasks: source-free add/reorder/remove/bind/reset, discoverability/saved state/instances/control ceilings. Note 3, Pair 4, Process 4, Guided 2–5; deterministic mobile order. Required platform controls tracked separately, not hidden from complexity. | Merchant research |
| B9 Discovery/navigation | Native cards/filter/sort/pagination/search/predictive, related/complementary, nested navigation/newsletter/Shop/account/localization; real empty/error/resource changes/gift-card handling. Conventional table stakes remain clear. | Discovery + QA |
| B10 Media | Real ordinary/awkward/no-media/focal-point/variant image, hosted/external video / 3D and alternatives. Responsive network/decode/layout measurements, native alt/keyboard/reduced motion, no exceptional-photo dependence. [Performance/media](https://shopify.dev/docs/storefronts/themes/best-practices/performance). | Engineering + performance |
| B11 Accessibility/localization | Automated semantic/axe plus manual keyboard/focus/errors, VoiceOver/NVDA, zoom/reflow/touch and committed RTL. App/editor/dialog/source-order tests; no certification from Lighthouse alone. [Accessibility](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility). | Accessibility + QA |
| B12 Performance | Existing internal gates unchanged:median Lighthouse 90/95; gzip global CSS 45 KB / JS 25 KB, page JS 20 KB / route total 45 KB, initial fonts 100 KB, zero theme-owned third-party requests. All existing LCP/INP-proxy/CLS/TBT/long-task limits; cold-cache realistic pages, 3+ repeats, app attribution/saved reports and owner/expiry for waivers. | Performance |
| B13 SEO/social | Real canonical/title/description/JSON-LD across locale/pagination/filter contexts; page_image sharing, configured social links, no fabricated rating markup or submission robots override. | Engineering + SEO QA |
| B14 Browser/editor | Real supported desktop/mobile/webview checks; section reload/remove/block select, instances, delayed/failed JS/network races, genuine native JS-off forms/navigation and reduced motion. Record versions/devices. | QA |
| B15 CI/provenance/preservation | Real Theme Check/static budgets and relevant truth/state/render tests, reviewed suppressions. Preserved-prototype diff/hash checks and every added asset/dependency license. No blanket upstream import. | Release engineering |

## C. Final release/submission gates

Owners record actual evidence; none is satisfied by M2 authorization or a planned test.

- [ ] **Eligibility/originality:** Product/engineering revalidate all official rules on submission date; assess completed whole-theme structural differentiation against incumbents and neutral content. Own source alone is insufficient.
- [ ] **Live integration:** Engineering/integration close applicable B checks on Shopify:templates/features/editor/apps/embeds/dynamic sources/Markets/plans/native cart. Evidence Rail engineering NARROW is not upgraded by ADR acceptance.
- [ ] **Accessibility/compatibility:** Accessibility/QA complete manual AT/zoom/reflow/contrast/keyboard/touch and committed RTL/locales; current official browser/webview matrix, precise support scope/residuals.
- [ ] **Measured performance:** Performance records populated home/PDP/collection desktop/mobile official averages separately from stricter internal realistic-page budgets, versioned reports and app ownership. Missing credentials/content remain BLOCKED.
- [ ] **Merchants/content/provenance:** Product/content/research validate real usability, licensed realistic demo catalog/media and genuine evidence/source permissions; testimonials distinguishable from verified reviews. M1 fictional fixtures are not production content approval.
- [ ] **Package/install:** Release packages `theme/` using [CLI package](https://shopify.dev/docs/api/shopify-cli/theme/theme-package), inspects supported contents/exclusions and installs clean-store ZIP. Check metadata/config/locales/defaults/preset-demo equivalence; no fixed demo IDs, unsupported directories or secrets.
- [ ] **Submission/support:** Product/support complete exclusive distribution, naming/version/releases, merchant docs/contact/FAQ/demo purchase setup/support ownership and [Partner workflow](https://shopify.dev/docs/storefronts/themes/store/review-process/submit-theme). Legal notices are not marketing credits; Shopify approval remains external.

## Entry disposition

**Architecture blocker: none.** Original foundation is eligible under checked policy, has no imported-theme license/pin dependency and preserves accepted systems. Store credentials/content/extensions, research participants, devices and measurements are named production execution prerequisites; arrange them before their gates rather than fabricate or count PASS.

A is the first-commit contract; B is incremental validation; C is submission. This task creates documents only and authorizes a subsequent M2 build, not another experiment.

**M2 AUTHORIZED — BEGIN PRODUCTION THEME IMPLEMENTATION**
