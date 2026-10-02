# Shopify Theme Store requirements baseline

**Verified-current snapshot:** 2 October 2026. The requirements explicitly marked **VERIFIED 2026-10-02** below were independently checked against Shopify's official [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission), and linked official guidance. Other unchecked details remain **REVALIDATE**. Because requirements change, refresh the complete snapshot before M1's foundation ADR and again before submission.

Theme Store approval is a product and architecture constraint from the first ADR, not a submission cleanup exercise. A verified requirement is a current input, not a claim that this product complies or will be approved.

## Verified current requirements and traceability

| ID | Verified fact as of 2026-10-02 | M1 implication / evidence required | Official source |
|---|---|---|---|
| V01 | A submitted theme must be fundamentally different from existing Theme Store themes. Meaningful design and functional innovation must exceed cosmetic changes, more settings or sections, and superficial styling; uniqueness must exist in the architecture and overall experience. | **Blocking M1 gate:** demonstrate architectural and overall-experience originality through prototypes, interaction/system comparisons, and provenance. Intent-led templates, Launch Narrative terminology, semantic settings, presets, or different JSON ordering alone do not pass. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) |
| V02 | Skeleton Theme is the only approved codebase for Theme Store development; otherwise the code must be fully original. New submissions built on or derived from Dawn or Horizon are ineligible. | ADR-001 must choose **Skeleton Theme or fully original code only** before production implementation, with provenance and license review. Dawn and Horizon are excluded. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), [Skeleton Theme](https://github.com/Shopify/skeleton-theme) |
| V03 | Lighthouse minimums are average scores of **60 Performance** and **90 Accessibility** across home, product, and collection pages, on desktop and mobile. | Record all six page/device results and their averages. Internal budgets remain deliberately stricter and separate. | [Performance requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance) |
| V04 | A theme cannot depend on an app for functionality and cannot contain app-like functionality that requires API access for full functionality. | Every core flow must work without an app; app blocks are optional extensions. Audit features and architecture boundaries in M1. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) |
| V05 | Misleading or fake urgency and scarcity mechanisms are prohibited. | Continue rejecting fake countdowns, inventory claims, visitor/activity counters, and similar coercive UI; test that claims come from legitimate Shopify data. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) |
| V06 | Shopify warns against unnecessarily deep block nesting and complicated configuration structures that make primary controls difficult to understand. | M1 schema specimens must show shallow structures, primary-control visibility, setting budgets, and merchant comprehension. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) |
| V07 | Theme Store themes must be exclusive to the Shopify Theme Store and cannot be distributed through other marketplaces. | Founder approval must accept the distribution constraint before M1 investment. Record the commercial decision in the gate evidence. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) |
| V08 | Every preset requires at least one demo store, corresponding to that preset's primary industry and catalog positioning. | Treat every future preset as a content, QA, documentation, and support commitment; M1 must recommend only presets DCL can demonstrate credibly. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission) |
| V09 | Public theme documentation and a public support contact form must be available for the listing; Theme Partners are responsible for support and bug fixes. | M1 support/business approval must identify ownership, public surfaces, staffing, and maintenance budget; release planning must include per-preset documentation. | [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission) |

## Eligibility and submission

- [ ] Confirm partner account, Theme Store eligibility, submission route, review stages and fees in the [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission).
- [x] **VERIFIED 2026-10-02:** accept Theme Store exclusivity and no other-marketplace distribution; founder commercial approval remains open. See V07.
- [x] **VERIFIED 2026-10-02:** meet architectural/overall-experience originality, not superficial variation. Product evidence remains open. See V01.
- [x] **VERIFIED 2026-10-02:** eligible foundations are Skeleton Theme or fully original code; Dawn and Horizon are excluded. ADR-001 choice remains open. See V02.
- [ ] Prepare accurate listings and at least one industry/catalog-appropriate demo store per preset, plus public documentation, public support contact form, version and release notes. See V08–V09 and [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission).

## Architecture and merchant features

- [ ] Use only supported [theme architecture](https://shopify.dev/docs/storefronts/themes/architecture) directories in the distributable artifact.
- [ ] Supply all required templates and use [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) where required.
- [ ] Use [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) for supported header/footer areas and [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) with valid schemas/presets.
- [ ] Use [theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks) only where reusable merchant components improve editing; keep nesting shallow and primary controls understandable. See V06; exact schema limits remain **REVALIDATE**.
- [ ] Support [`@app` blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) in appropriate main and featured surfaces.
- [ ] Include a safe Custom Liquid section/block only if currently required/allowed, with clear merchant warnings.
- [ ] Support [dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources), standard product data, and graceful missing-data behavior.
- [ ] Ensure settings follow [input settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings) and [sidebar settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/sidebar-settings) conventions.
- [ ] Verify intent-led starts are implemented only with supported native templates, sections, blocks, and presets; no proprietary builder or editor replacement.
- [ ] Verify all core functionality works without an app or external API; app blocks enhance rather than complete the theme. See V04.

## Commerce completeness

- [ ] Confirm required home, product, collection, cart, search, page, blog/article, list-collections, 404, password, gift-card, and customer-account surfaces against current requirements.
- [ ] Correctly render price, compare-at price, unit price, taxes context, availability, variants, quantity rules, selling plans where exposed, pickup availability, cart errors, and localization.
- [x] **VERIFIED 2026-10-02:** misleading/fake urgency and scarcity are prohibited. Use only legitimate Shopify inventory/price data and reject fabricated activity mechanisms. Implementation evidence remains open. See V05.
- [ ] Use native predictive search, filtering, recommendations, and app extension points where applicable rather than duplicating platform/app responsibilities.

## Performance, accessibility and compatibility

- [x] **VERIFIED 2026-10-02:** average Lighthouse minimums are Performance 60 and Accessibility 90 across home, product, and collection pages for desktop and mobile. Implementation results remain open. See V03 and [performance requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance).
- [ ] Implement Shopify’s [theme accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility); passing the verified Lighthouse minimum does not establish accessibility conformance.
- [ ] Record current desktop/mobile browsers, versions, embedded webviews and testing obligations from [browser support](https://shopify.dev/docs/storefronts/themes/store/requirements#browser-compatibility).
- [ ] Test keyboard, zoom/reflow, contrast, names/roles/states, errors, media alternatives and reduced motion; target WCAG 2.2 AA even if Shopify’s minimum differs.
- [ ] Run [Theme Check](https://shopify.dev/docs/storefronts/themes/tools/theme-check), Shopify CLI validation, Lighthouse and browser automation on realistic demo data.

## Assets, content and localization

- [ ] Use responsive hosted theme images, explicit dimensions/aspect ratios, suitable lazy/eager loading and no unnecessary third-party payloads; follow [performance best practices](https://shopify.dev/docs/storefronts/themes/best-practices/performance).
- [ ] Confirm font licensing, Shopify-hosted font selection, system fallbacks and asset-size rules.
- [ ] Implement Shopify-compatible color schemes and contrast-safe defaults; merchants remain responsible for changed combinations, but editor choices should reduce failure.
- [ ] Put storefront/editor strings in locales and meet the current translation-language requirement; follow [locales architecture](https://shopify.dev/docs/storefronts/themes/architecture/locales).
- [ ] Do not ship copyrighted demo media without licenses; keep listing claims factual.

## Prohibited or displaced functionality

**VERIFIED 2026-10-02:** themes cannot depend on an app and cannot include app-like functionality requiring API access for full functionality; misleading/fake urgency and scarcity are prohibited. Reject theme-owned reviews, loyalty ledgers, subscriptions, bundle engines, advanced upsell rules, analytics, consent management, back-in-stock services, fabricated countdowns, and activity counters. Optional app blocks are extension points, never dependencies. See V04–V05 and the [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).

## Compliance evidence package

Maintain a dated requirements export, URL, exact text summary, owner, implementation mapping, test evidence and status. A reviewer should be able to trace every requirement to code and a result. Unknown requirements block release; they are not silently waived.
