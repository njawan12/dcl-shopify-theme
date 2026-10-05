# Split Tension — second-pass completion report

Date: 2026-10-04. Local branch: `m1-split-tension-prototype`.
Starting commit: `e4b7c4aec751a3198277116f0b527a92e62323dd` exactly. Preserved second-pass implementation commit: `873cfbb4a73c366bca0f9c259349a187c81da968`. The tests, metrics and implementation manifest below record that original completion; this later reconciliation changes verdict documentation only.

**Engineering verdict: NARROW.** Every executed state, static, preservation and browser reflow check passes. Manual accessibility, zoom, actual browser-disabled JavaScript, real Shopify and measured performance remain open; no overall production or M1 PASS is inferred.

## Final human M1 verdict

**PASS TO PRESERVE.** Human review accepts the second-pass implementation at `873cfbb4a73c366bca0f9c259349a187c81da968`. This reconciliation changes documentation only; the implementation and existing evidence are preserved.

The accepted proof covers:

- Guided Set's 2–5 step merchandising model;
- explicit shopper inclusion;
- truthful native-product/variant pricing semantics;
- unresolved, sold-out, missing, duplicate, failure and race states;
- aggregate selected-item action without bundle or discount invention;
- no-JS/server-rendered fallback;
- multi-instance isolation;
- responsive visual identity;
- neutral originality torture survival.

Commerce proof remains within the simulated fixture scope. The fallback proof is literal/script-free server-rendered HTML and enhancement-withheld/failure evidence; actual browser-wide JavaScript disabling remains untested. Real Shopify cart atomicity/integration, selling plans, app interoperability, accessibility certification, cross-browser/touch testing and measured production performance remain later gates. Human M1 acceptance does not certify these gates or authorize production work, redesign or M2.

## Authority read before implementation

Read from `m0-live-market-evidence-2026-10-03`, fetched commit `3b8ed84a0bf0ea816a16047218a1293e8a852251`:

- `docs/m1-split-tension-second-pass-implementation-delta.md`
- `docs/m1-split-tension-visual-direction.md`, also read at its pinned commit `545a1c0f3e5f9ab1ceb0e91f6d9198e0d244d1ff`
- `docs/m1-split-tension-implementation-brief.md`
- `docs/m1-split-tension-commerce-state-machine.md`
- `docs/m1-living-canvas-prebuild-red-team-matrix.md`
- `docs/m1-signature-system.md`
- `docs/m1-product-architecture-contract.md`
- `docs/engineering-compliance-standard.md`

The original six documents are unchanged from the original implementation's controlling baseline. Commerce/state requirements take precedence. The later visual proof approval and implementation delta supersede the visual document's earlier pre-proof instruction to wait before coding.

## Result and contract audit

The shared component now uses a dominant editorial/media field, a continuous numbered rail, large product images that cross its desktop boundary, open commerce information and an aggregate action connected to the same rail. Native controls and fixed quantity 1 remain explicit. No quantity stepper, discount, bundle claim, sticky action, custom carousel, alternate component, rescue settings or extra storefront navigation was introduced.

| Delta requirement | Evidence |
|---|---|
| 1–3 isolated visual pass / exact starting point | Parent commit is exact e4b7c4; only the allowed prototype path changed; no dependencies or engine rewrite |
| 4 desktop >=1280 | Shared twelve-track grid; media spans seven tracks; numbered sequence starts inside the field; product media straddles its edge; open information lies beyond it; action closes the rail |
| 4 tablet 768–1024 | Editorial opening precedes the three-column step sequence; overlap relaxes without forced collisions |
| 4 mobile 320–430 | One semantic DOM: strong media opening, numbered vertical sequence, large product moments, full-width controls and connected action |
| 5 neutral | Same markup/engine/geometry; system sans, monochrome tokens, generic copy, ordinary white-background packshots and generic landscape media |
| 6 commerce | Pure engine and complete init/bootstrap adapter byte-for-byte identical; all 24 fixture commerce semantics unchanged; no native control or state changes |
| 7 media | Local portrait campaign JPG, generic landscape SVG, ordinary square/portrait/landscape packshots, transparent cutouts, missing product image and optional editorial media all exercised |
| 8 density/content | Two/five steps, long/localized heading/title/labels and 30–50% expansion; missing/sold-out/unresolved/mixed/zero/one eligible fixtures included in 168-case audit |
| 9 accessibility/progressive baseline | Logical DOM, native names/controls/status/focus, >=44px primary targets; instance isolation and script-free literal baseline evidenced; AT/manual gates remain open |
| 10 CSS-owned structure | Grid/Flex/pseudo rail/object-fit/tokens; one editorial-copy wrapper; no positional JS, nth-child coordinates, fixture-specific layout CSS or duplicated responsive commerce DOM |
| 11 evidence | Controlling/stress frames, unchanged original assertions, preservation regression, all seven widths and pending switch evidence below |
| 12 visual acceptance | PASS TO PRESERVE, awarded by human review of the preserved second-pass proof; no Codex-awarded visual verdict |
| 13 stop conditions | No observed requirement for bespoke-only art, coordinates, another component, carousel, a11y compromise or commerce rewrite; premium/originality assessment is human-owned |
| 14 completion/scope | Exact manifest below; local commit only; no PR, push, merge, production, M2 or other Living Canvas variant |

During stress inspection, media-less step copy initially moved over the dark desktop field. A general media-presence layout rule now keeps that copy aligned with the commerce column. All final screenshots and the 168-case audit use the corrected layout. This is not fixture-specific positioning.

## Tests and exact results

From repository root, Node.js 26.10.0:

```sh
node --check prototypes/living-canvas/split-tension/fixtures.js
node --check prototypes/living-canvas/split-tension/split-tension.js
node --check prototypes/living-canvas/split-tension/tests/serve.mjs
node --check prototypes/living-canvas/split-tension/tests/second-pass.mjs
node prototypes/living-canvas/split-tension/tests/state.mjs
node prototypes/living-canvas/split-tension/tests/static.mjs
node prototypes/living-canvas/split-tension/tests/second-pass.mjs
git diff --check HEAD
```

- Four syntax checks: PASS, exit 0.
- Original state suite: **335 assertions PASS**, across the canonical 24 fixtures.
- Original static suite: **215 assertions PASS**; combined nonblank/non-comment runtime JS 499, CSS 130 physical lines.
- New preservation suite: **8 assertions PASS**. Compares original engine and entire adapter byte-for-byte, all fixtures with only editorial/product media excluded, original state/static/server files, and exact script-free fallback derivation.
- Original `state.mjs`, `static.mjs` and `serve.mjs` are unchanged. The new test specifically guards the authorized visual-only boundary; it does not weaken old assertions.
- Initial static run on unstaged files failed its scope parser: its existing `.trim().slice(3)` handling drops the first pathname character for a leading unstaged status. After staging only the allowed prototype path, the unchanged suite passed. Independent Git scope verification also passes. No test was edited to hide this limitation.
- Browser reflow: **168/168 PASS**, 24 fixtures × widths **320, 375, 430, 768, 1024, 1280, 1440**. No horizontal overflow, checked default inclusions, duplicate IDs, primary target heights below 44px, or desktop commerce text positioned on the editorial field. The four controlling frames additionally use 390px.
- Pending fixture switch: outgoing request observed pending with controls locked; replaced with neutral; its own request independently confirmed **1 item, CAD 24.00**, with neutral heading/product and no outgoing product state. Existing state tests also prove stale/dead/version rejection and pending teardown.
- Browser option journey: 30ml Light explicitly included → CAD29.00, compare-at CAD34.00, unit CAD96.67/100ml; switching to Rich yields sold out, inclusion cleared/disabled, CAD0.00.
- Two-instance journey: first instance CAD24.00 / one checked; second CAD0.00 / zero checked.
- Keyboard Tab: focused View product link retains visible 3px solid outline. This is a browser focus observation, not a full manual accessibility audit.
- Request failure screenshot: truthful simulated error, selections retained, retry/review available.
- Literal server fallback: exact index HTML with script removed and a base URL for nested evidence assets. No executable script, inclusion/options/action controls; both product links remain. Browser-wide JavaScript disabling itself was not exercised.
- `git diff --check HEAD`: PASS. Manifest/scope and exact parent: PASS. Final working tree clean after local commit.

The JSON evidence contains recorded DOM observations, not a shipped automation framework. Original first-pass evidence remains unchanged in its parent directory.

## Controlling screenshots

All final screenshots are full-page captures from the Codex in-app browser. Paths below are relative to this prototype:

| Frame | File |
|---|---|
| 1440 branded | `tests/evidence/second-pass/branded-1440.jpg` |
| 1440 neutral | `tests/evidence/second-pass/neutral-1440.jpg` |
| 390 branded | `tests/evidence/second-pass/branded-390.jpg` |
| 390 neutral | `tests/evidence/second-pass/neutral-390.jpg` |

## Stress screenshots

- `five-step-1440.jpg`, `five-step-390.jpg`, `five-step-375.jpg`
- `localized-320.jpg` — long heading, localized content, missing product image
- `mixed-1024.jpg` — unresolved options, available singles and app-owned discovery
- `missing-product-1440.jpg` — authored missing-product step and absent optional editorial media
- `unresolved-1440.jpg`, `resolved-1440.jpg`, `sold-out-1440.jpg`
- `two-instances-1280.jpg`, `keyboard-focus-1280.jpg`
- `server-fallback-1440.jpg`, `enhancement-withheld-390.jpg`
- `pending-switch-neutral-1280.jpg`, `request-error-1440.jpg`

All are under `tests/evidence/second-pass/`; the evidence archive contains every frame plus `browser-matrix.json`, `browser-transitions.json`, `browser-lifecycle.json`, `complexity.json` and `checks.txt`.

## Complexity delta

| Metric | First pass | Second pass | Delta |
|---|---:|---:|---:|
| CSS physical lines | 125 | 130 | +5 |
| CSS bytes / gzip | 8986 / 2497 | 10591 / 2764 | +1605 / +267 |
| Component JS physical lines | 431 | 439 | +8 |
| Fixtures JS physical lines | 77 | 77 | 0 |
| Combined nonblank/non-comment JS | 491 | 499 | +8 |
| Combined runtime JS bytes / gzip sum | 34516 / 11007 | 35171 / 11185 | +655 / +178 |

Commerce complexity delta is **zero**: six top-level state fields, two fields per step, five per active request; four handled event types (change, click, popstate, pageshow); four interactive control types (native select, checkbox, button, link). The eight additional component JS lines create optional safe local editorial media and a copy wrapper. No geometry measurements, state fields, event types, native control types or merchant positioning controls were added. The new regression test is not runtime JS.

## Media provenance and resilience

`campaign-portrait-v2.jpg` is a locally generated photographic editorial asset using the imagegen skill; original output was 1024×1536 PNG, converted to JPEG quality 82 with the system image utility. It contains no UI, labels, product truth or layout signature. Prompt: portrait editorial photo of an adult woman in quiet morning profile with natural skin and a hand along her cheek, warm window light, deep olive/stone atmosphere, dark space for separate HTML type; no products/logos/text/badges/UI/graphic lines/collage/watermark. No external asset loads exist.

`objects-landscape.svg` is an original monochrome vector still life, 1200×800, with generic vessel and box geometry. It supplies a normal landscape source in both neutral and five-step branded content. Cutout SVGs remove only the white background from the existing bottle/jar art; ordinary original white packshots remain in neutral and dense fixtures. Asset composition does not bake in numbered steps or required coordinates. Centered object-fit handles all sources; essential text has a component-owned dark scrim and independent commerce surface.

## Deviations, conflicts and untested evidence

No unresolved contract conflict or implementation scope deviation. Only visual media fixture data changed; prices, options, eligibility, quantities, request modes, labels and authored commerce semantics remain intact. No controlling docs were modified.

The script-free HTML evidence document is a test artifact derived from the literal index. It proves the server-rendered fallback without executing the prototype, but is not a claim that the browser's JavaScript-disable setting was tested.

Untested: VoiceOver/NVDA and live announcement quality; physical touch; manual text enlargement, 200%/400% zoom and OS/high-contrast variants; cross-browser Safari/Firefox/device coverage; actual browser-disabled-JS settings; real Shopify Ajax/422/atomicity, Liquid objects, Markets, cart reconciliation, app blocks and selling plans; Theme Editor section load/unload/block lifecycle; real merchant images/content beyond the fixture envelope; measured LCP/INP/CLS, Lighthouse, throttled-network/runtime memory budgets; broader M1 proof packages. These remain review/integration gates, not implicit PASS or reasons to implement M2 here.

## Original second-pass implementation files changed

Every path below is relative to `prototypes/living-canvas/split-tension/`. No production directories, other Living Canvas variants, M0/M1 branch content or controlling docs were changed. At original implementation completion, no PR, merge, remote push, M2 or real cart action occurred and the prototype stopped for review. Human review has since accepted PASS TO PRESERVE; the documentation reconciliation is committed and published separately without altering this implementation manifest.

- `README.md`
- `findings.md`
- `fixtures.js`
- `index.html`
- `media/bottle-cutout.svg`
- `media/campaign-portrait-v2.jpg`
- `media/jar-cutout.svg`
- `media/objects-landscape.svg`
- `second-pass-report.md`
- `split-tension.css`
- `split-tension.js`
- `tests/evidence/second-pass/branded-1440.jpg`
- `tests/evidence/second-pass/branded-390.jpg`
- `tests/evidence/second-pass/browser-lifecycle.json`
- `tests/evidence/second-pass/browser-matrix.json`
- `tests/evidence/second-pass/browser-transitions.json`
- `tests/evidence/second-pass/checks.txt`
- `tests/evidence/second-pass/complexity.json`
- `tests/evidence/second-pass/enhancement-withheld-390.jpg`
- `tests/evidence/second-pass/five-step-1440.jpg`
- `tests/evidence/second-pass/five-step-375.jpg`
- `tests/evidence/second-pass/five-step-390.jpg`
- `tests/evidence/second-pass/keyboard-focus-1280.jpg`
- `tests/evidence/second-pass/localized-320.jpg`
- `tests/evidence/second-pass/missing-product-1440.jpg`
- `tests/evidence/second-pass/mixed-1024.jpg`
- `tests/evidence/second-pass/neutral-1440.jpg`
- `tests/evidence/second-pass/neutral-390.jpg`
- `tests/evidence/second-pass/pending-switch-neutral-1280.jpg`
- `tests/evidence/second-pass/request-error-1440.jpg`
- `tests/evidence/second-pass/resolved-1440.jpg`
- `tests/evidence/second-pass/server-fallback-1440.jpg`
- `tests/evidence/second-pass/server-fallback.html`
- `tests/evidence/second-pass/sold-out-1440.jpg`
- `tests/evidence/second-pass/two-instances-1280.jpg`
- `tests/evidence/second-pass/unresolved-1440.jpg`
- `tests/second-pass.mjs`
