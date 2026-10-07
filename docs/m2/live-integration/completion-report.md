# M2A live Shopify integration completion

Date checked: 2026-10-06 (America/Toronto; Actions artifacts use UTC timestamps on 2026-10-07).

**M2A LIVE GATE PASS — AUTHORIZE SIGNATURE PRODUCTION LAYERS**

This is the bounded M2A real-platform integration verdict. It is not Shopify Theme Store submission approval, accessibility certification, production performance certification or a claim that unavailable platform states passed. No next signature layer was begun.

## Source and destination

- Branch: `m2-production-theme`.
- Accepted foundation/report: `b8d10863e668d8660b8b509ff2416f52620a894a`.
- Existing uploaded development theme: `185844367583`, `m2a-live-gate-b8d1086`, `dcl-theme-dev.myshopify.com`.
- Initial upload was not repeated. The only implementation patch targets `assets/base.css` on that same development theme, with `--only assets/base.css --nodelete`, for the observed unbranded checkout contrast defect. Patch source: `35ed7291997af0dba09d717fb0425de226d54bd0`. Read-only pull confirms remote CSS equals local CSS.
- Initial upload exit 0 / Theme Check [] is retained in `upload-and-access.json`. Shopify CLI 4.8.4. No live or other unpublished theme was targeted.
- Other authored Liquid/schema/templates/JS remain identical to accepted M2A. Preserved prototypes remain unchanged. Native Theme Editor merchant configuration changes are recorded separately in `saved-editor-state.json`, not imported into production source.
- Public preview: https://dcl-theme-dev.myshopify.com/?preview_theme_id=185844367583 (store access still required). Editor: https://admin.shopify.com/store/dcl-theme-dev/themes/185844367583/editor.
- User authorized a temporary signed preview URL as encrypted repository secret solely for these Actions runs. Secret and local credential file were deleted; GitHub secret lookup returned zero matches. No signed URL, cookies or credentials are committed.

## Executed proof and evidence

| Contract area | Actual proof | Evidence |
|---|---|---|
| Catalog | Existing 17 safe sample products plus exactly one named native two-option test product; three saved combinations, 12 USD, native 6 USD/oz, no image or description. Large/Gloss does not exist. | `catalog-state-manifest.json`; `runs/catalog/live-results.json` |
| Storefront | Home, product, collection, cart, search, contact and 404 at 390, 1440 and 320 CSS px. All 21 observations render the expected heading, no Liquid error and no page overflow. Header/footer groups render on these layouts. Password/gift use separate layouts. | `runs/journeys-and-smoke/`; seven surfaces × three widths |
| JS on/off commerce | Separate actual Chromium contexts, 390×900. Dawn native link → quantity 2 → native Add form → cart; update to 3 and save note; native remove. JS-on Checkout reaches Shopify checkout boundary without submitting payment. | `runs/journeys-and-smoke/live-results.json`; product/cart on/off screenshots; checkout screenshot |
| Canonical truth | Product 15414509732063 / variant 67931960606943 / Color Dawn / 69995 USD minor units / qty 2 / line total 139990. Native line key begins with the actual variant. Read-only `/cart.js` independently verifies the browser-submitted cart; no API mutation replaces the journey. | Same JSON, both journeys |
| JS-off detail | `browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:900}})`, Chromium 151.0.7922.34 on Ubuntu 24.04. No script removal, CSP simulation, failure hook or request mocking. Page-authored scripts disabled; automation uses DevTools DOM inspection. Browser console observations in the off context are response-header Clear-Site-Data notices, not page script execution. | Harness `tests/m2/live-shopify.mjs`; journey JSON |
| Native adverse/advanced states | Sold-out action disabled; native compare-at 885.95 vs sale 785.95 USD; video/multiple media render; gift denominations and recipient fields render truthfully with sold-out action; real weekly selling-plan allocation submits at 21.21 USD. | Five original state frames; `native-selling-plan-390.jpg`, `native-selling-plan-cart-390.jpg` |
| Two-option/missing content | Native Large/Matte valid; Large/Gloss yields no price and disabled ID/purchase; Small/Gloss recovers and submits variant 67933304029407 / product 15414839476447 / qty 1 / 1200 USD minor units. Cart unit price 600 per oz with actual 2 oz measurement. No-media placeholder and empty optional description survive. This journey also uses JS disabled. | `runs/catalog/` |
| Settings/groups | Standard→Wide global setting saved; restored Standard. Header Main→Footer menu and footer Footer→Main menu saves exercised, then original menus restored. Live computed defaults: page width 78rem, foreground #202020, background #FFFFFF, LTR. Wide token was not independently measured while selected. | `interactive-observations.json`; baseline settings; final native config pull |
| Editor lifecycle | Description remove/save/add; Custom Liquid add/save/reorder/remove; two Custom Liquid blocks duplicated and rendered; core Vendor reordered before Title then restored; featured product added, changed to compare-at product, reordered below main and removed; Gift Card→Complete product context; home, gift-card and password contexts; mobile preview. Saves/re-renders exercised. | `interactive-observations.json`; `screenshots/`; `saved-editor-state.json` |
| Actual apps | Both main-product and featured-product native `@app` pickers expose installed Shop sign-in block. Actual block added/saved/rendered, featured app reordered after price, saved/rendered again, removed. Mobile visual containment observed. No app installed and no Shop sign-in/payment transaction attempted. | `main-product-app-affordance.png`, `main-product-app-mobile.png`, `featured-product-app-mobile.png` |
| App embeds | Native pane explicitly reports no apps with embeds installed. Execution remains unavailable, not PASS. | Interactive record |
| Markets/localization | Native Canada→United States selector submission works; actual Complete product changes from Canadian-context 664.95 USD/unavailable to US 699.95 USD/available. Both configured contexts present USD. Only English exposed. | Interactive journey; browser country selector and native cart USD assertions |
| Search/facets | Real search results and predictive suggestions from Shopify endpoint; native sort price-descending; native availability facet submission returns 10 products. Pagination controls are absent below 24 products; no fake page or extra catalog inflation. | Original JSON predictive/filter records |
| Password/gift | Unauthenticated native password gate responds 200 with password form; its public preview parameter does not prove uploaded-theme styling. Uploaded-theme password editor preview shows labeled field/Enter. Gift-card editor renders Shopify's supplied 100 USD sample/code/QR; no actual gift issued/redeemed. | Catalog password frame; `password-editor-mobile.png`; `gift-card-platform-sample-editor.png` |
| Accessibility/reflow | Actual keyboard tab traversal reaches variant links, quantity, Add, cart quantity/note/update/remove/Checkout with solid visible focus. Native quantity 0 is rejected with range-underflow message. Form labels observed; 320 px reflow plus controlled 200% root text-size feasibility on home/product/collection shows no overflow. Reduced motion media emulation verified. | Baseline keyboard/nativeValidation/textEnlargement JSON; stress screenshots |

Core editor/native app changes were cleaned up. Final main product keeps Title → Vendor → Price → Options → Plans → Quantity → Buy → Description → Pickup, no test Liquid or app blocks. Description received a new Shopify-generated ID during the exercise. Final cleanup restores the accepted native product-template JSON, including its original Description ID, via one scoped `--only templates/product.json --nodelete` operation. Native read-only pull confirms exact equality to the accepted source. Header/footer menus restored; Standard width restored. The home `frontpage` collection selection remains as the bounded populated preview catalog, containing one real product at measurement time. Temporary added featured section removed. No commerce state failure was observed. Undo briefly showed Title-first in the editor while the saved remote template still retained Vendor-first; that UI observation was not treated as durable restoration. The scoped cleanup above resolves the test configuration discrepancy. Full third-party/editor lifecycle certification remains open.

## Accessibility correction and limitations

Initial live axe identified white text on Shopify's observed legacy unbranded `Buy it now` fallback background #1990c6 (3.59:1). A scoped CSS rule now uses existing foreground/background tokens. No branded wallet internals or closed shadow DOM were modified. Current official Shopify documentation was checked on 2026-10-06: [accelerated checkout](https://shopify.dev/docs/storefronts/themes/pricing-payments/accelerated-checkout), [unbranded customization](https://help.shopify.com/en/manual/online-store/dynamic-checkout/customize-button). The correction targets only the fallback markup actually observed; future closed-shadow wallet styling remains platform-owned.

Affected real-product axe recheck has no contrast violation. All four rechecked surfaces retain one `frame-title` violation on Shopify's injected `PBarNextFrame` preview-toolbar iframe. This external preview artifact was neither hidden nor patched. Incomplete automated findings are retained in JSON. Shopify account/wallet/toolbar internals are not certified by theme-level focus checks. The 200% test is controlled text-size feasibility, not actual browser zoom or assistive-technology certification.

## First populated real-platform Lighthouse baseline

Lighthouse 13.5.0, Playwright 1.62.1 / Chromium 151.0.7922.34, Ubuntu 24.04; authenticated preview cookies retained, credential URL never used as the measurement target. Home: one real native collection card; product: Complete Snowboard; collection: real all-products catalog. Single runs, no warmed best-of selection. Includes Shopify development/preview scripts and toolbar.

| Surface | Mode | Performance | Accessibility | LCP seconds | CLS | TBT ms |
|---|---|---:|---:|---:|---:|---:|
| home | mobile | 96 | 96 | 2.632 | 0.000208 | 39.0 |
| product | mobile | 96 | 96 | 2.551 | 0.000208 | 49.1 |
| collection | mobile | 96 | 95 | 2.204 | 0.000208 | 143.1 |
| home | desktop | 100 | 96 | 0.501 | 0.002009 | 0.0 |
| product | desktop | 100 | 96 | 0.511 | 0.000000 | 0.0 |
| collection | desktop | 100 | 95 | 0.558 | 0.006786 | 0.0 |

INP is not available as a real-user field metric in these lab runs; TBT is the available lab responsiveness indicator. Scores do not certify full catalog/app/Markets performance. Six raw, credential-redacted Lighthouse JSON reports are in `runs/baseline/`.

## Commands, run provenance and results

- Real-store harness: `timeout 900s node tests/m2/live-shopify.mjs`, manual workflow input `live_integration=true`, phases `all`, `baseline`, `catalog`. Real native form/navigation assertions fail the job; optional store state scope is recorded separately.
- [Journeys/smoke run 37560197128](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37560197128): executed native functional checks PASS, 2 journeys, 30 surface observations plus checkout screenshot. Its six Lighthouse subprocesses timed out and produced no baseline; this is not the performance proof.
- [Corrected baseline run 37561606897](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37561606897): PASS, four actual-page axe rechecks, keyboard/native validation/text enlargement checks, six Lighthouse reports.
- [Catalog run 37562546883](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37562546883): PASS native two-option/invalid combination/unit pricing, JS-off cart, selling-plan cart and password observations.
- Artifacts: `m2a-live-shopify-<run source SHA>` on those runs, retention 30 days. Durable relevant JSON/screenshots copied under `runs/`; repetitive console observations consolidated with counts, raw originals remain workflow artifacts.
- Production CI after CSS patch: [37561572276](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37561572276) PASS. Theme Check [] (warnings fail), 1086/1086 structural/schema/locale/budget/preservation checks, 33/33 native-snippet/cart unit tests, 113 browser assertions/48 observations, distributable 66 files/source-identical package. These isolated checks are not counted as live Shopify journeys.
- Final test-harness source CI [37562546661](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37562546661) also PASS and preserves the same theme source. Early retries 37559516299 and 37559877778 used expired preview access; 37559996484 found ambiguous test selector, corrected to quantity input; catalog retries 37562034180 / 37562242843 demanded an h1 on the generic password gate, corrected to record the actual native gate and separately prove uploaded-theme editor rendering. No hidden theme functional FAIL was converted to PASS.
- Theme correction and measurement harness were committed/pushed on this branch. Final report/evidence commit and parent are supplied in the completion response. No PR or merge.

## Unavailable states and remaining production gates

No remaining blocker to this bounded M2A gate. Explicitly unexercised categories remain:

1. Real issued gift-card access/redemption, expired/disabled gift cards, and native gift-recipient cart submission (existing gift variants sold out; editor uses platform sample only).
2. Enabled pickup availability, non-default quantity rules/maxima, advanced B2B conditions, annual prepaid/subscription renewals and plan changes beyond the tested weekly allocation.
3. Actual next/previous collection pagination (native catalog remains below 24 items); larger-catalog search/filter coverage and third-party filtering integration.
4. Additional languages, currency changes, real RTL locale and complete Markets/tax/duties/pricing policy combinations. Static logical-property/direction checks are not live RTL validation.
5. Installed app-embed execution; broader vendor integrations, app sign-in/authentication flows and wallet/payment transactions. Shop block insertion does not certify every app.
6. Real browser zoom, screen readers/AT, full keyboard/error-state audit, contrast under every merchant palette, WCAG certification and external platform UI accessibility. Preview iframe findings retained.
7. Cross-browser Safari/Firefox, physical touch devices, external wallet/device conditions and browser/editor lifecycle endurance beyond the recorded operations.
8. Production performance/field INP/Core Web Vitals, larger realistic merchandising catalog, production cache/edge/network variation, installed-app budgets and final submission benchmark/certification.
9. Full merchant usability study, complete production art direction and final full-theme/system integration. Accepted signature production systems remain future authorized work, not implemented by this gate.
10. Paid checkout, actual payment capture, fulfillment and customer account transaction scenarios were not executed.

**M2A LIVE GATE PASS — AUTHORIZE SIGNATURE PRODUCTION LAYERS**

Durable evidence contains 63 screenshots across native browser runs and editor operations, plus six raw Lighthouse reports. The changed-file manifest records every evidence path.

Stop. No Compact, Editorial, Evidence Rail, Commerce Mosaic/Anchor Cadence or Guided Set production layer begins in this task.
