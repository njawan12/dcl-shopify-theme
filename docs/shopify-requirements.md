# Shopify Theme Store requirements baseline

**Mandatory revalidation gate:** Requirements change. The links below are authoritative; every checkbox and numeric threshold must be confirmed against the live pages immediately before M1 and submission. Network access was blocked during this snapshot, so no volatile threshold is asserted as current.

## Eligibility and submission

- [ ] Confirm partner account, Theme Store eligibility, submission route, review stages and fees in the [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission).
- [ ] Confirm Theme Store exclusivity/distribution obligations in the [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).
- [ ] Demonstrate substantive originality in design and code; do not submit a superficial variant of a Shopify or third-party theme. Re-read [requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) and [best practices](https://shopify.dev/docs/storefronts/themes/best-practices).
- [ ] Confirm the currently approved starting-code policy. Do not select Dawn, Horizon, Skeleton Theme, or a custom foundation based on memory; record the exact official rule and decision in an ADR.
- [ ] Prepare a complete demo store, accurate listing, documentation, support contact, version and release notes per [submission](https://shopify.dev/docs/storefronts/themes/store/submission).

## Architecture and merchant features

- [ ] Use only supported [theme architecture](https://shopify.dev/docs/storefronts/themes/architecture) directories in the distributable artifact.
- [ ] Supply all required templates and use [JSON templates](https://shopify.dev/docs/storefronts/themes/architecture/templates/json-templates) where required.
- [ ] Use [section groups](https://shopify.dev/docs/storefronts/themes/architecture/section-groups) for supported header/footer areas and [sections](https://shopify.dev/docs/storefronts/themes/architecture/sections) with valid schemas/presets.
- [ ] Use [theme blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/theme-blocks) only where reusable merchant components improve editing; confirm current schema/nesting requirements.
- [ ] Support [`@app` blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks) in appropriate main and featured surfaces.
- [ ] Include a safe Custom Liquid section/block only if currently required/allowed, with clear merchant warnings.
- [ ] Support [dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources), standard product data, and graceful missing-data behavior.
- [ ] Ensure settings follow [input settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings) and [sidebar settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/sidebar-settings) conventions.

## Commerce completeness

- [ ] Confirm required home, product, collection, cart, search, page, blog/article, list-collections, 404, password, gift-card, and customer-account surfaces against current requirements.
- [ ] Correctly render price, compare-at price, unit price, taxes context, availability, variants, quantity rules, selling plans where exposed, pickup availability, cart errors, and localization.
- [ ] Use real Shopify inventory/price data; no fake scarcity, fabricated activity, or misleading urgency. Check [requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).
- [ ] Use native predictive search, filtering, recommendations, and app extension points where applicable rather than duplicating platform/app responsibilities.

## Performance, accessibility and compatibility

- [ ] Record current Lighthouse test pages, device/profile, data set, and minimum scores directly from [performance requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance).
- [ ] Record current accessibility score/criteria and implement Shopify’s [theme accessibility best practices](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility).
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

Reject app-like business logic: reviews, loyalty ledgers, subscriptions, bundles engines, advanced upsell rules, analytics, consent management, back-in-stock messaging services, and fabricated urgency. Expose app blocks instead. Reconfirm exact prohibited-feature language in current [requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).

## Compliance evidence package

Maintain a dated requirements export, URL, exact text summary, owner, implementation mapping, test evidence and status. A reviewer should be able to trace every requirement to code and a result. Unknown requirements block release; they are not silently waived.
