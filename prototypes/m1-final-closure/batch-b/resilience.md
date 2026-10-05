# B6 resilience reconciliation
2026-10-05. **B6 PARTIAL: actual JS-disabled browser journey remains missing.** No redesign authorized or performed.

`tests/evidence/reflow.json` reconfirms Balanced, Compact, Editorial, populated cart and story at320 CSS pixels, then the same five at32px root font (200% text). All10 document widths320; every observed visible main control stays within the page; no non-input clipped element is observed; source headings/content retained. No ordinary two-dimensional exception is required. Native number inputs have internal scroll widths beyond client widths at200% (three62px client fields); this is not page scrolling or evidence of lost numeric value. Their single-digit values remain readable/editable; the browser action changes first quantity2→3 and submits successfully (`text-resize-action.json`). Native controls inherently scroll/edit long values; AT/zoom certification is not inferred.

The [W3C reflow condition](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) for vertically scrolling content is equivalent320 CSS pixels.1280 at400% browser zoom approximately yields320. Existing normal320 evidence and this reconfirmation support layout feasibility; actual native browser zoom is not claimed. [Text resize](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html) is separately checked up to200%. Five200% observations fit and preserve content/function. Batch A's artificial64px root at320 is an extra extreme text-only stress: widths555/450/555/545/473 for Balanced/Compact/Editorial/cart/story. It is neither normative1.4.10 failure nor a reason for a rescue iteration. Historical Batch A reporting is unchanged; this authority corrects its interpretation.

## Actual JS-off attempts
`tests/js-off.cjs` uses Playwright engine launch and real `newContext({javaScriptEnabled:false})`, with a planned Guided → native product link → native purchase POST/cart journey and screenshot. Configuration is not script omission, CSP or failFirst. Installed Chromium launch fails at macOS MachPort bootstrap permission; ordinary Chrome also aborts. Network permission was granted and Chromium was retried, including bundled node runtime, without success. Native Chrome cannot be controlled: Computer Use permissions are not granted. A further legitimate alternative was downloaded from Playwright's official distribution into workspace scratch: Firefox153.0/build1538. Its real headless process also aborts before a context can be created.

Final reproducible attempts (`node tests/js-off.cjs`) record both launch errors in `tests/evidence/js-disabled.json`: **zero journey steps executed**. No browser version is falsely reported as running, no screenshot invented, no JS-off PASS awarded. The ordinary in-app browser has no documented JS-disable/context control. Actual initialization-failure native links remain genuine separate Batch A evidence.

Smallest M1 correction: execute the prepared JS-off journey in one browser environment that permits engine launch or supplies a genuine JS-disable control, record engine/config/native navigation/purchase result. It needs no prototype change, visual iteration, new experiment or M2.

## Consolidated system-level resilience matrix
A = unchanged Batch A6dd6619; ST873cfbb; CM105ecdd; ER06c34717. Branch/document pins are in final verdict. The rows identify observed/model/structural scope rather than treating unrelated counts as certification.

|State|Existing exact evidence|Remaining uncovered scope|
|---|---|---|
|1/2/6/20+ combinations; unresolved/nonexistent/sold-out|A dataset/model; `tests/static.py`, `server_journeys.py`, `browser-views.json`; ST `tests/state.mjs`|Live Shopify object resolution/inventory|
|Compare/unit/sale/quantity|A truth/cart tests and native journeys; CM truth-stress; ST money/state tests|Markets/real allocations/price adjustments|
|Missing/short/long/title/options/source/content|A missing/short/long/manual/structured/disconnected8-width views; ER long/omission normalizers|Genuine merchant data/provenance|
|One/no/many/mixed media|A simple/missing/many/rich-media; ER ratios; CM mixed-media|Real video/3D players, zoom, variant-image changes and decode errors|
|No reviews/metafields/complementary|A manual/disconnected/short; ER zero/removed sources; CM ordinary native cards|Live deleted-binding lifecycle|
|Selling plan/properties/pickup/gift-shaped|A plan/properties/pickup and canonical care23 records; model/cart tests|Platform plan pricing, pickup execution, gift issuance/recipient/redemption|
|12/24/100+ collection density|A collection12/24/100; CM104 encounter stress and native sort/filter/page observations|Real facets/search/pagination,100-item merchant reading study|
|App expected/awkward/tall/wide/absent/remove/reorder/repeat|ER `tests/evidence/browser-matrix.json`, `interactions.json`, guests, `app-host.liquid`; A app/repeated|Live @app/embeds/editor/vendor execution; ER engineering remains NARROW|
|Delayed/failed/race/pending/stale|ST state suite/pending browser journey; A copied adapter57 checks and init failure|Actual browser JS-off **M1 missing**; real API/network atomicity/concurrency|
|Keyboard/focus/native action|A `tests/evidence/browser-journeys.json`, findings§7, keyboard frame and server journeys; ST/CM/ER interaction records|AT certification; full checkout keyboard/payment execution|
|320 reflow /200% text|B `reflow.json`, native quantity action; A264 width observations|Native zoom/AT certification, hardware keyboard/IME|
|RTL/translation/mobile order|A rtl8 widths/heading invariants; ER expansion/RTL; ST localized; CM localized|Complete locale parity/native-language RTL validation|
|Repeated instances/global roles|A repeated390/1440 and shared tokens; B two isolated operator states; ST scoped engine instances|Theme-editor unload/reload/live global schema|
|Motion/loading/safe area|A reserved sizes, loaded40JPEG manifest, zero sticky owners, footer env insets; ER reduced-motion supplement|OS preference switch and physical notch/touch/keyboard overlap|
|Low-end performance threat|A complexity/payload/HTML cost and findings§9; no layout JS; CM/ER cost records|Measured low-end CPU/network/CWV/Lighthouse and app-attributed cost|

Only actual browser-JS-disabled execution remains a newly required M1 resilience closure artifact. Certification, native Shopify execution and measured production behavior remain later gates; they are not labelled passed.
