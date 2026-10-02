# QA plan

## Quality gates

1. Schema/static gate: JSON parse, Theme Check, locale parity, packaging allowlist.
2. Component gate: Liquid render/interaction tests where practical.
3. Preview-store gate: commerce, editor, app blocks and dynamic sources.
4. Accessibility gate: automated scan plus keyboard/screen-reader manual scripts.
5. Performance gate: budgets on realistic fixtures.
6. Release gate: required browser/webview matrix, regression and Theme Store checklist.

## Fixture matrix

- **Products:** one variant; many options/variants within platform limits; unavailable combinations; sold out; sale; unit price; long title/description; one/many/no media; image/video/3D; no structured content; complete structured content; selling-plan app block.
- **Collections:** 0, 1, 4, 24 and large paginated sets; filters on/off; no results; sorting; promo tiles; unusual ratios; long titles.
- **Cart:** empty/populated; add/remove; rapid quantity changes; server error; invalid/sold-out change; discount display; long properties; app content.
- **Content:** absent images, broken optional references, long unbroken strings, rich text, long translations, mixed aspect ratios.
- **Localization/Markets:** currencies with differing minor units, translated routes, long German-like expansion, CJK, bidirectional feasibility, country/language selectors and market context.

## Interaction/device coverage

Phone widths 320, 360, 390/393 and 430 px; common tablet portrait/landscape; 1280 and 1440+ desktop; zoom 200% and reflow at 400%. Test touch, coarse pointer, mouse and keyboard. Before execution, copy the exact current required browser versions and webviews from [Shopify requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#browser-compatibility); add current iOS Safari, Android Chrome, desktop Safari/Chrome/Firefox/Edge as product coverage.

## Critical journeys

Search → filter → product → select variant → add → update cart → checkout handoff; deep mobile navigation; gallery/video/zoom; quick add simple and complex products; predictive search keyboard flow; localization change; campaign CTA; app-block placement; failure/offline-ish response states.

## Editor coverage

For every section/block: add, remove, reorder, duplicate where supported, change each setting, reset/empty, connect/disconnect dynamic source, insert app block, use preview inspector, switch templates and viewport. Dispatch/test `shopify:section:load`, `:unload`, `:select`, `:deselect`, `:reorder`, block select/deselect and editor design mode. Confirm no duplicate listeners and accurate live preview.

## Accessibility scripts

Automated axe/Lighthouse cannot certify accessibility. Manually verify landmarks/headings; skip link; full keyboard path; visible focus; focus trapping/restoration; escape; form names/errors/status announcements; variant availability; filters; drawers/dialogs; carousel controls; media alternatives; zoom/reflow; contrast; forced colors where practical; reduced motion; 44×44 CSS-pixel target goal; screen-reader testing on at least VoiceOver/Safari and NVDA/Firefox or Chrome.

## Automation proposal

- Shopify CLI + Theme Check for theme correctness.
- Prettier/JSON validation only if it preserves Liquid safely.
- Playwright for critical journeys, screenshots and browser coverage.
- axe integration for repeatable rule detection.
- Lighthouse CI for reference routes and budget assertions.
- Visual regression with deterministic fixtures and reviewed baselines.

Credentials and a development store are required for meaningful end-to-end, editor, Markets, app-block and performance checks. Their absence blocks those checks.

## Defect policy

P0: checkout path/data loss/security/accessibility blocker; no release. P1: major journey or required-browser failure; no release. P2: workaround exists; product owner decision. P3: cosmetic. Every regression gets fixture, environment, steps, evidence and ownership.
