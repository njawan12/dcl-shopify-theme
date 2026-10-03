# M0 Shopify requirements refresh — 2026-10-03

## Source policy

Refreshed against current official Shopify developer documentation on 2026-10-03. This is an M0 architecture/eligibility snapshot, not a claim that the future theme complies. Revalidate again at the M1 foundation decision, before affected implementation, and before submission.

## Blocking/current facts confirmed

### Eligibility and originality
- Theme Store distribution is exclusive to the Shopify Theme Store.
- A submission must be fundamentally different from other Theme Store themes across the overall experience and core templates/elements.
- Identity/capabilities must not be easily reproducible through settings, superficial styling, or a few additional sections/options.
- Shopify Skeleton Theme is the only approved codebase for Theme Store development; otherwise use fully original code.
- New themes derived from Dawn or Horizon are not eligible.

### Design/UX
- Theme Store requirements explicitly demand intentional, distinctive visual design targeted to a specific merchant type/industry and professional-quality visual execution.
- Merchant usability and high-quality UX are explicit acceptance concerns, not optional polish.

### Performance/accessibility
- Minimum average Lighthouse performance: 60 across home/product/collection, separately for desktop and mobile.
- Minimum average Lighthouse accessibility: 90 across home/product/collection, separately for desktop and mobile.
- Tests must use populated sections with real content/images; empty demo sections cannot be used to game scores.
- DCL internal targets remain stricter and separate.

### Functionality/integrity
- No app-dependent theme functionality.
- No app-like API-dependent features such as wishlists, scheduling, cart-level discount-code systems or Instagram feeds.
- No fake urgency/scarcity such as fictitious countdowns, stock or viewer activity.
- Theme JS must not interfere with or augment native Shopify admin/theme-editor functionality.
- Third-party assets/plugins/images require appropriate licenses.
- Sass/SCSS is prohibited; use native CSS.
- Shopify imposes additional asset/HTML/accessibility requirements including valid HTML, labeled form controls, contrast and focus-order requirements.

### Browser/webview matrix
Desktop:
- Safari: latest 2 releases on Mac
- Chrome: latest 3 releases on Mac and PC
- Firefox: latest 3 releases on Mac and PC
- Edge: latest 2 releases on PC

Mobile:
- Mobile Safari: latest 2 releases on iOS
- Chrome Mobile: latest 3 releases on Android and iOS
- Samsung Internet: latest 2 releases on Android

Webviews:
- Instagram: latest Android/iOS
- Facebook: latest Android/iOS
- Pinterest: latest Android/iOS

### App blocks
- Sections in JSON-template contexts should support `@app` where appropriate.
- App blocks are not supported in statically rendered sections.
- A theme can provide an `apps.liquid` wrapper; its schema must support `@app` and include a preset.
- App insertion must be treated as an antifragility/layout problem, not merely a schema checkbox.

### Current platform limits relevant to architecture
- JSON templates per theme: 1,000.
- Sections per JSON template: 25.
- Section groups per theme: 20.
- Sections per section group: 25.
- Theme blocks are platform-limited; current block documentation states at most 300 theme block files.
These are platform ceilings, not design targets. DCL should operate far below them where possible.

### Testing/review
- Shopify recommends Theme Check during development and Lighthouse CI to prevent regressions.
- Navigation and product forms should be tested with JavaScript disabled.
- Mandatory-feature testing must run in both theme editor and storefront.
- Shopify's official review checklist includes deliberately stressful repeated-section/product scenarios; DCL fixtures must test comparable density rather than ideal demo-only states.
- Common rejection reasons include missing mandatory features, technical failures, insufficient testing, terminology/settings problems, performance/accessibility misses, incomplete listings, weak/outdated demo stores, unlicensed content, and third-party intellectual property.

### Presets/listings/demos
- Each preset receives its own listing form/page.
- Each preset needs a complete, functioning corresponding demo store tailored to its merchant segment.
- Listing/demo assets have explicit screenshot and content requirements.
This reinforces the commercial decision to avoid premature preset proliferation.

## Architecture consequences

1. Originality must be proven through system/experience behavior plus visual identity; section count, renamed presets, styling and JSON order cannot carry the case.
2. The job-oriented idea must remain Shopify-native and cannot augment/replace the editor.
3. Skeleton remains provisional only after provenance/eligibility revalidation at implementation entry.
4. Browser/webview QA is a real cost and belongs in staffing/budget decisions.
5. App compatibility requires resilient insertion seams and failure testing.
6. Demo content and licensing are submission-critical product work, not marketing afterthoughts.
7. Performance testing must use realistic content and density.
8. Internal accessibility target remains WCAG 2.2 AA even though Shopify's numeric Lighthouse acceptance floor is 90.

## G1 decision

**G1 — current official Shopify requirements: PASS FOR M0 WITH REVALIDATION OBLIGATION.**

The M0 product/architecture decision now has enough current official-source information to proceed to the remaining empirical gates. This does not waive future requirement refreshes. Revalidation remains mandatory:
- at M1 foundation/ADR acceptance;
- before first implementation of affected architecture;
- before browser/performance/accessibility release gates;
- before Theme Store submission.

Any newly discovered mandatory rule can reopen the relevant gate.
