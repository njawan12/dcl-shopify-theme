# Engineering compliance standard

**Applies to:** every implementation milestone and implementation pull request from M2 onward.

**Baseline date:** 2 October 2026.

**Authority:** this standard governs engineering implementation and review. Product direction remains in the existing M0 documents; this document does not replace it.

## 1. Classification and gate policy

Every applicable rule in this standard uses one of these classifications:

- **SHOPIFY-REQUIRED** — a requirement verified in the dated `shopify-requirements.md` record against an official Shopify source. This label is not used for team preference. A volatile rule retains its official URL and must be revalidated at the milestone named below.
- **INTERNAL-HARD-GATE** — a DCL engineering or product constraint. It may deliberately exceed Shopify's minimum, but is never represented as a Shopify requirement.
- **BEST-PRACTICE** — platform, accessibility, or engineering guidance that should normally be followed. A deviation needs a documented reason and evidence that correctness, accessibility, maintainability, and performance are not weakened.

An applicable **SHOPIFY-REQUIRED** or **INTERNAL-HARD-GATE** item blocks implementation completion while it is knowingly failing. Unknown Shopify requirements are not assumed to pass. Record the affected rule, owner, official URL, last validation date, implementation mapping, and test evidence in the milestone traceability record.

### Volatile requirements and revalidation

The verified snapshot and source URLs live in [`shopify-requirements.md`](shopify-requirements.md). Revalidate applicable rules before the relevant implementation milestone starts, whenever Shopify publishes a material change, and during M16 before submission. In particular:

- Before M2, revalidate supported architecture, required templates, schema constraints, browser support, locales, and packaging rules.
- Before the first affected implementation (including M5), revalidate [`@app` block requirements and supported contexts](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), including applicable primary product surfaces.
- Before each measured performance gate and M16, revalidate the official [Theme Store performance requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance) and measurement method.
- Before M14, revalidate the official [browser compatibility matrix](https://shopify.dev/docs/storefronts/themes/store/requirements#browser-compatibility).
- Before M16, refresh the complete [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements) and [submission documentation](https://shopify.dev/docs/storefronts/themes/store/submission).

Items not already verified in the repository remain **REVALIDATE**, not **SHOPIFY-REQUIRED**, until checked against an accessible official source.

## 2. Accessibility

- **SHOPIFY-REQUIRED:** meet the verified Theme Store Lighthouse Accessibility floor: an average score of **90** across home, product, and collection pages, each measured on desktop and mobile under Shopify's current method. Revalidate the [performance requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance) before measurement and M16.
- **INTERNAL-HARD-GATE:** target WCAG 2.2 AA and ship no known applicable A/AA blocker. Lighthouse 90 is a submission metric, not WCAG conformance; neither Lighthouse nor axe alone can establish accessibility compliance.
- **INTERNAL-HARD-GATE:** render semantic HTML and use native elements where appropriate: buttons for actions, links for navigation, and no clickable `div`/`span` substitute when a native interactive element fits.
- **INTERNAL-HARD-GATE:** every interactive control has an accessible name. Form controls have programmatically associated labels and instructions, using native `<label>` elements where appropriate. Validation, errors, loading, completion, cart changes, and other meaningful dynamic status are announced accessibly.
- **INTERNAL-HARD-GATE:** headings reflect document structure. Do not manufacture visually hidden headings merely to force an artificial uninterrupted heading sequence.
- **INTERNAL-HARD-GATE:** all interactive functionality is keyboard operable, with visible focus, logical focus order, and no keyboard trap except correctly implemented deliberate modal containment. Dialogs, drawers, and popovers use behavior appropriate to the chosen native or custom implementation, support Escape where appropriate, move focus correctly on open, and restore focus to the trigger where appropriate on close.
- **INTERNAL-HARD-GATE:** prefer native semantics. Use ARIA only where native HTML is insufficient, and keep applicable state and relationship attributes (`aria-expanded`, `aria-controls`, `aria-current`, live regions, and equivalents) accurate.
- **INTERNAL-HARD-GATE:** provide a skip link; meaningful alternative text behavior; ignored decorative imagery; sufficient contrast; zoom/reflow; reduced-motion behavior; and usable touch targets.
- **INTERNAL-HARD-GATE:** product media, variants, quantity controls, filters, navigation, predictive search, cart operations, and every dynamic update must retain appropriate names, roles, states, keyboard behavior, focus behavior, alternatives, and announcements.
- **BEST-PRACTICE:** follow Shopify's current [theme accessibility guidance](https://shopify.dev/docs/storefronts/themes/best-practices/accessibility), while treating the internal WCAG target independently from Shopify's numeric floor.

Accessibility evidence must include Lighthouse, axe, keyboard-only testing, VoiceOver, NVDA, zoom/reflow, reduced-motion testing, and representative mobile/touch testing. Relevant journeys must be tested manually; an automated pass is never sufficient by itself.

## 3. HTML and Liquid

- **INTERNAL-HARD-GATE:** valid, semantic, server-rendered HTML is the baseline. Useful storefront content and core commerce paths exist before JavaScript enhancement; no business-critical experience exists only after client-side JavaScript runs unless Shopify functionality genuinely requires it.
- **INTERNAL-HARD-GATE:** use modern supported Liquid patterns: `{% render %}` rather than deprecated `{% include %}`, and `image_url` rather than deprecated `img_url`.
- **INTERNAL-HARD-GATE:** escape merchant-authored or user-controlled text for its actual output context. Never assume optional product, metafield, metaobject, or dynamic-source data exists; missing, empty, or deleted data must degrade gracefully.
- **INTERNAL-HARD-GATE:** extract duplicated rendering logic when a private snippet is the correct abstraction.
- **BEST-PRACTICE:** do not turn every fragment into a snippet. An abstraction must improve correctness, reuse, testability, or maintainability.

## 4. Images and media

- **BEST-PRACTICE:** prefer Shopify's responsive image pipeline, including `image_url` and `image_tag`, for merchant and Shopify CDN media. A bare `<img>` is not automatically a Shopify violation; document a legitimate exception.
- **INTERNAL-HARD-GATE:** provide responsive widths, accurate `sizes`, intrinsic dimensions or aspect-ratio reservation, correct alternative-text behavior, appropriate CDN transformations, and correct handling for product images, video, and model content.
- **INTERNAL-HARD-GATE:** choose loading behavior by rendering priority. The LCP candidate is not lazy-loaded by default; justified critical above-the-fold imagery may be eager; below-the-fold imagery is normally lazy; unnecessary media is not eager.
- **INTERNAL-HARD-GATE:** use `fetchpriority`, preload, or eager loading only when measurement justifies it. Page composition must prevent multiple independent sections from claiming high priority.

## 5. CSS

- **INTERNAL-HARD-GATE:** use a mobile-first responsive architecture, global semantic design tokens, and bounded component/section controls. Preserve the CSS payload and user-experience budgets in [`performance-budget.md`](performance-budget.md).
- **INTERNAL-HARD-GATE:** do not use arbitrary merchant-authored CSS as a normal customization mechanism, inaccessible hiding techniques, fragile fixed heights for merchant content, or an unnecessary CSS framework.
- **INTERNAL-HARD-GATE:** never remove focus styling without an accessible replacement; implement reduced-motion behavior.
- **BEST-PRACTICE:** use logical properties where they improve localization and RTL readiness. RTL remains a product commitment only if ADR-005 validates it.

## 6. JavaScript

- **INTERNAL-HARD-GATE:** no jQuery, Alpine, React, Vue, or Svelte runtime, and no external carousel/UI framework. This is DCL's architecture rule, not a blanket Shopify prohibition.
- **INTERNAL-HARD-GATE:** progressively enhance server-rendered behavior with small native ES modules. Load code only when its rendered page/component requires it, avoid global mutable state and duplicate initialization, and preserve the JavaScript budgets in [`performance-budget.md`](performance-budget.md).
- **INTERNAL-HARD-GATE:** support Shopify theme-editor lifecycle events. Clean up listeners, observers, and other resources when sections unload or re-render; abort stale network requests where relevant.
- **BEST-PRACTICE:** use Web Components/Custom Elements when lifecycle encapsulation genuinely helps. Do not force simple behavior into a custom element when a native implementation is clearer.

## 7. Sections, blocks, and the theme editor

- **INTERNAL-HARD-GATE:** every custom section contains valid `{% schema %}` where Shopify architecture requires it. Not every section needs blocks; blocks exist only when reorderable or repeatable child content has merchant meaning.
- **INTERNAL-HARD-GATE:** follow M0 merchant-operability rules: shallow hierarchy, semantic settings, strong defaults, bounded choices, progressive disclosure, minimal cognitive complexity, and the setting budgets in [`merchant-usability-principles.md`](merchant-usability-principles.md).
- **INTERNAL-HARD-GATE:** avoid unnecessary deep nesting, implementation-detail settings, arbitrary pixel controls when semantic choices suffice, enormous schemas, near-duplicate sections, and configuration required merely to make a section presentable.
- **INTERNAL-HARD-GATE:** sections/components work when added, removed, duplicated, reordered, selected, and re-rendered in the theme editor, as applicable, without leaked listeners or duplicate initialization.
- **BEST-PRACTICE:** Shopify's verified warning against unnecessarily deep nesting and confusing configuration supports the direction above; DCL's specific budgets and design constraints remain internal rules.

## 8. App blocks and app compatibility

- **SHOPIFY-REQUIRED:** core theme functionality must not depend on an app and the theme must not implement app-like functionality requiring API access for full functionality. See the dated V04 record and official [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).
- **REVALIDATE before affected implementation:** add `@app` support where Shopify currently requires it, including applicable primary product surfaces, after confirming the current official [app-block contexts](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks). Do not infer that every section must support `@app`.
- **INTERNAL-HARD-GATE:** add generic app-block positions elsewhere only where they provide real merchant value. App blocks must fail gracefully and must not break spacing, sticky behavior, hierarchy, or mobile usability. Apps are guests, not architectural owners.
- **INTERNAL-HARD-GATE:** do not create vendor-specific contracts for review, subscription, loyalty, or bundle apps unless a later documented compatibility decision explicitly approves one.

## 9. Performance

- **SHOPIFY-REQUIRED:** meet the verified Theme Store average Lighthouse floors of **60 Performance** and **90 Accessibility**, measured across home, product, and collection pages on desktop and mobile according to Shopify's current requirements. These 2 October 2026 values require revalidation from the official [performance requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance) before each formal gate and M16.
- **INTERNAL-HARD-GATE:** independently meet [`performance-budget.md`](performance-budget.md), including representative-page Lighthouse Performance ≥90, Accessibility ≥95, Core Web Vital/proxy limits, CSS/JavaScript payload limits, and route-specific limits. The detailed budget remains authoritative if it becomes stricter.
- **INTERNAL-HARD-GATE:** server render first; progressively enhance; load route/component-specific JavaScript; use responsive media; reserve layout space; minimize main-thread work; introduce no unnecessary dependency; and make no theme-owned third-party request without explicit review.
- **INTERNAL-HARD-GATE:** performance claims require repeatable measurements on realistic fixtures. Report theme-owned cost separately from merchant app/content payload outside DCL's control; outside payload is not a reason to conceal theme-owned regression.

## 10. Shopify commerce correctness

- **INTERNAL-HARD-GATE:** test all applicable states for product forms, variant selection, availability, sold-out products/variants, pricing, compare-at pricing, unit pricing, quantity rules, accelerated/dynamic checkout, pickup availability, cart add/update/remove, cart errors, inventory-derived states, recommendations, predictive search, collection filtering/sorting, pagination, localization, currency/Markets behavior, long translations, and empty states. “Where applicable/supported/implemented” must be recorded, not silently skipped.
- **SHOPIFY-REQUIRED:** never fabricate inventory, visitor activity, scarcity, countdowns, demand, or other misleading urgency. See dated V05 and the official [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).

## 11. Originality and provenance

- **SHOPIFY-REQUIRED:** the submission must be fundamentally different from existing Theme Store themes through meaningful design and functional innovation in its architecture and overall experience; superficial styling, settings, sections, or rearranged JSON are insufficient. See dated V01 and the official [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements).
- **SHOPIFY-REQUIRED:** ADR-001 must choose Skeleton Theme or fully original code before production implementation; Dawn- or Horizon-derived submissions are excluded. See dated V02, the official [requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), and [Skeleton Theme](https://github.com/Shopify/skeleton-theme).
- **INTERNAL-HARD-GATE:** architectural originality blocks M2. Do not copy competitor Liquid, CSS, or JavaScript, and do not build a competitor theme with only altered styling/settings/sections. Preserve ADRs, license review, design history, and code provenance.
- **INTERNAL-HARD-GATE:** each implementation review asks whether the accumulation of conventional components has weakened the architectural originality case. Familiar commerce and accessibility conventions are not defects, but the overall architecture must retain its defensible difference.

## 12. Localization and content resilience

- **INTERNAL-HARD-GATE:** make applicable merchant- and storefront-facing strings translatable; enforce locale parity; test long text and pseudo-localization; tolerate text expansion and non-English word lengths; and put no meaningful storefront text only in images.
- **BEST-PRACTICE:** use logical CSS properties where appropriate for localization readiness.
- **INTERNAL-HARD-GATE:** claim RTL support only after ADR-005 and the roadmap's validation work approve the commitment.

## 13. Security and robustness

- **INTERNAL-HARD-GATE:** escape merchant/user-controlled output for its rendering context; avoid unsafe HTML injection; do not use `eval` or equivalent dynamic code execution; and validate assumptions when serializing or reading JSON and `dataset` values.
- **INTERNAL-HARD-GATE:** tolerate missing/deleted dynamic-source references, provide resilient fetch error states, prevent duplicate submissions where appropriate, and keep secrets/API credentials out of theme source.
- **BEST-PRACTICE:** constrain this review to real theme attack/failure surfaces; do not invent backend controls for infrastructure the theme does not own.

## 14. Mandatory implementation PR gate (M2 onward)

Every implementation PR must include this checklist with **Pass**, **N/A + reason**, or **Blocked** and link its evidence. It may not be marked implementation-complete while an applicable hard gate knowingly fails.

- [ ] Which Shopify requirement is affected, what official source supports it, and is its validation current?
- [ ] Is semantic/native HTML used, with correct Liquid patterns and output escaping?
- [ ] Do keyboard operation, focus order/visibility/management, Escape, and restoration work?
- [ ] Are screen-reader names, roles, states, errors, and dynamic announcements correct?
- [ ] Do responsive/mobile/touch, zoom/reflow, and reduced-motion states pass?
- [ ] Do empty, missing/deleted, error, long-content, and long-translation states pass?
- [ ] Do theme-editor add/remove/duplicate/reorder/select/reload behaviors pass without duplicate initialization or leaks?
- [ ] Are app-block requirements/implications revalidated and generic integrations resilient?
- [ ] Is JavaScript necessary, progressively enhanced, scoped, idempotent, and within budget?
- [ ] Is CSS/settings complexity justified and within established budgets?
- [ ] Are responsive images, LCP selection, loading priority, dimensions, and media alternatives correct?
- [ ] Is measured performance within the official floor and stricter internal budget as applicable, with ownership attributed?
- [ ] Do localization/locale parity and applicable Markets/currency behavior pass?
- [ ] Do all affected commerce states and failure paths pass without fabricated claims?
- [ ] Which automated tests ran, and what manual QA ran on representative devices/assistive technologies?
- [ ] Does the change preserve the originality/provenance case and decision records?
- [ ] Are documentation, merchant guidance, release notes, and support impact addressed?

## 15. Pre-code compliance review

Before production Liquid is written for any M2+ milestone, its implementation owner adds a short preflight to the milestone or first implementation PR. Identify:

1. applicable verified Shopify requirements and any required live revalidation;
2. accessibility risks;
3. commerce-correctness risks;
4. performance, media-priority, and LCP risks;
5. theme-editor lifecycle risks;
6. app compatibility risks;
7. localization/content-resilience risks;
8. originality/provenance risks; and
9. planned automated and manual tests.

The preflight should be brief and risk-based. It is a required engineering decision aid, not a substitute for implementation evidence or a new product-strategy exercise.

## 16. Evidence and ownership

Use [`qa-plan.md`](qa-plan.md) for fixtures and manual/automated coverage, [`performance-budget.md`](performance-budget.md) for numeric internal budgets, [`theme-architecture.md`](theme-architecture.md) for system boundaries, and [`shopify-requirements.md`](shopify-requirements.md) for verified Shopify facts and official URLs. A milestone owner must keep classifications distinct in PRs and evidence: passing an internal target does not itself prove every Shopify requirement, and passing a Shopify numeric minimum does not waive an internal hard gate.
