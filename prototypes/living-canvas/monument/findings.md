# M1 Monument — isolated implementation findings / Section 14 completion report

**Engineering verdict: PASS for the authorized isolated static prototype only.**
**Visual verdict: PENDING HUMAN REVIEW.**

## Authority and pre-code conflict review

Read from `m0-live-market-evidence-2026-10-03` before implementation:

| Controlling source | GitHub blob SHA |
|---|---|
| m1-monument-implementation-brief.md | 4f417ede18770d0d97b4caa063c6cea62165227d |
| m1-monument-prebuild-red-team-contract.md | ef56a91f297f7d771f030c857a2260421edbd4c7 |
| m1-living-canvas-prebuild-red-team-matrix.md | 10e16e2d11f6d8a7059805b14073eeb6e46d510f |
| m1-signature-system.md | 40326f8342449f2e276b0d87ab761223b0a9eb24 |
| m1-product-architecture-contract.md | 174bf59e51fc3b6c55e9814629dffde0654365d0 |
| engineering-compliance-standard.md | 089d4cfc95b29d8ba69ece9d85616ddbc83189a2 |

Existing Split Tension findings were read as process precedent only. Its accepted composition/state engine was not reused or modified. No controlling conflict was found: the specific approved Monument contract/brief authorizes this one experiment after the earlier general matrix's visual-proof hold. Concept 05 remains a fallback reference only. The optional evidence allowance is unused (zero evidence modules). The broader production/M1 system obligations remain later gates, not a claim that this isolated static experiment completes the whole M1 system.

## 1. Commit and parent

Local branch: `m1-monument-prototype`.
Parent: `873cfbb4a73c366bca0f9c259349a187c81da968`.
The exact resulting local commit SHA is returned in the completion message and resolves with `git rev-parse HEAD`; an immutable commit cannot contain its own hash. No push is authorized or performed.

## 2. Changed files and scope

All files below are newly added under `prototypes/living-canvas/monument/`. No controlling document, Split Tension, Edge Crop, Quiet Frame or production theme file changed. No dependency manifest, lockfile or repository-global configuration changed. No PR, merge or M2 work.

```text
prototypes/living-canvas/monument/README.md
prototypes/living-canvas/monument/findings.md
prototypes/living-canvas/monument/fixtures.json
prototypes/living-canvas/monument/index.html
prototypes/living-canvas/monument/media/bag-transparent.svg
prototypes/living-canvas/monument/media/canvas-bag.jpg
prototypes/living-canvas/monument/media/care-bottle.svg
prototypes/living-canvas/monument/media/case-dark.svg
prototypes/living-canvas/monument/media/case-edge-bottom.svg
prototypes/living-canvas/monument/media/case-edge-left.svg
prototypes/living-canvas/monument/media/case-edge-right.svg
prototypes/living-canvas/monument/media/case-edge-top.svg
prototypes/living-canvas/monument/media/case-landscape.svg
prototypes/living-canvas/monument/media/case-portrait.svg
prototypes/living-canvas/monument/media/case-white.svg
prototypes/living-canvas/monument/media/case-wide.svg
prototypes/living-canvas/monument/media/metal-ring.svg
prototypes/living-canvas/monument/media/pantry-jar.svg
prototypes/living-canvas/monument/media/utility-case.jpg
prototypes/living-canvas/monument/monument.css
prototypes/living-canvas/monument/render.py
prototypes/living-canvas/monument/serve.py
prototypes/living-canvas/monument/tests/browser_evidence.py
prototypes/living-canvas/monument/tests/evidence/adjacent-1440.jpg
prototypes/living-canvas/monument/tests/evidence/adjacent-390.jpg
prototypes/living-canvas/monument/tests/evidence/beauty-1440.jpg
prototypes/living-canvas/monument/tests/evidence/below-fold-390.jpg
prototypes/living-canvas/monument/tests/evidence/branded-1440.jpg
prototypes/living-canvas/monument/tests/evidence/branded-390.jpg
prototypes/living-canvas/monument/tests/evidence/browser-matrix.json
prototypes/living-canvas/monument/tests/evidence/capture.json
prototypes/living-canvas/monument/tests/evidence/changed-files.json
prototypes/living-canvas/monument/tests/evidence/checks.json
prototypes/living-canvas/monument/tests/evidence/dark-rect-390.jpg
prototypes/living-canvas/monument/tests/evidence/focal-bottom-390.jpg
prototypes/living-canvas/monument/tests/evidence/focal-left-390.jpg
prototypes/living-canvas/monument/tests/evidence/focal-right-390.jpg
prototypes/living-canvas/monument/tests/evidence/focal-top-390.jpg
prototypes/living-canvas/monument/tests/evidence/focus-390.jpg
prototypes/living-canvas/monument/tests/evidence/food-1440.jpg
prototypes/living-canvas/monument/tests/evidence/frames.json
prototypes/living-canvas/monument/tests/evidence/interaction.json
prototypes/living-canvas/monument/tests/evidence/jewelry-1440.jpg
prototypes/living-canvas/monument/tests/evidence/landscape-768.jpg
prototypes/living-canvas/monument/tests/evidence/localized-1440.jpg
prototypes/living-canvas/monument/tests/evidence/localized-320.jpg
prototypes/living-canvas/monument/tests/evidence/localized-390.jpg
prototypes/living-canvas/monument/tests/evidence/long-cta-320.jpg
prototypes/living-canvas/monument/tests/evidence/long-money-320.jpg
prototypes/living-canvas/monument/tests/evidence/long-title-375.jpg
prototypes/living-canvas/monument/tests/evidence/missing-media-1440.jpg
prototypes/living-canvas/monument/tests/evidence/missing-product-1440.jpg
prototypes/living-canvas/monument/tests/evidence/neutral-1440.jpg
prototypes/living-canvas/monument/tests/evidence/neutral-390.jpg
prototypes/living-canvas/monument/tests/evidence/portrait-768.jpg
prototypes/living-canvas/monument/tests/evidence/rectangular-1440.jpg
prototypes/living-canvas/monument/tests/evidence/rectangular-390.jpg
prototypes/living-canvas/monument/tests/evidence/sold-out-1440.jpg
prototypes/living-canvas/monument/tests/evidence/transparent-1440.jpg
prototypes/living-canvas/monument/tests/evidence/two-line-1440.jpg
prototypes/living-canvas/monument/tests/evidence/wide-1024.jpg
prototypes/living-canvas/monument/tests/server_responses.py
prototypes/living-canvas/monument/tests/static.py
```

## 3. Tests and exact final counts

Run from the repository root:

| Command | Pass | Fail |
|---|---:|---:|
| `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/tests/static.py` | 817 | 0 |
| `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/tests/browser_evidence.py` | 12,036 | 0 |
| `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/tests/server_responses.py` | 145 | 0 |
| **Total assertions** | **12,998** | **0** |

`git diff --cached --check`: no whitespace errors. Scope assertions use porcelain-NUL paths and the final commit's changed-file manifest. No JS syntax tests apply because no JS exists. Renderer/server Python syntax is checked by AST parsing; test scripts execute successfully.

Static tests assert rendered behavior, safe omission, truthful price/state representation, semantic order, one image per instance, unique IDs, escaping, safe URLs, token-only neutral reuse, native links, first-image selection, lazy below-fold/second-instance behavior, literal default parity, forbidden-control absence, and no browser scripts/geometry rescue CSS.

Browser evidence tests assert the observed fixture/width Cartesian matrix, no horizontal overflow, no duplicate IDs, no scripts, valid/missing object counts, media containment, deterministic axis crossing, no statement/object/commerce collision, primary targets >=44px in both dimensions, wrapped unclipped text, separated adjacent instances, keyboard focus/navigation and actual JPEG dimensions. Source/media fingerprints prevent stale captures from passing silently. Display glyph ink can extend beyond its typographic line box; it remains visible, with no overflow clipping or collisions. This is not treated as a fixed-height text failure.

HTTP tests verify all 41 current rendered responses, no-store headers, byte-identical local assets, unknown fixture recovery, inaccessible source/escape routes, safe missing product routes, and the optional editorial destination.

During diagnosis, a shared mobile alignment defect was found: centering canceled part of the intended axis crossing. The mobile shared rule was corrected and all mobile cases re-audited. Final neutral system-font and non-square white-media refinements were re-audited across all affected fixtures and widths. An initial test filename shadowed Python's standard `http` package; it was renamed to `server_responses.py` before the successful final run. There is no unresolved test failure.

## 4. Fixture / width audit

41 fixtures × 8 widths = **328 observed views** in the Codex in-app browser, height 1000 CSS px. Widths: **320, 375, 390, 430, 768, 1024, 1280, 1440**. Zero horizontal overflow beyond the 1px measurement tolerance; zero duplicate IDs; zero component media/text collisions; every present object crosses the shared axis and remains contained. Missing product/deleted/unpublished states omit the object and commerce entirely; missing media omits the figure without a broken placeholder. Long content expands the component naturally.

| Fixture | Risk covered | Eight widths |
|---|---|---|
| `default` | Branded / default | PASS |
| `neutral` | Neutral originality torture | PASS |
| `short` | Very short headline | PASS |
| `long` | Long / localized +50% copy | PASS |
| `single` | Single available product | PASS |
| `multi-option` | Unresolved multi-option product | PASS |
| `sold-out` | Sold out | PASS |
| `sale` | Valid compare-at | PASS |
| `unit-price` | Unit-price context | PASS |
| `missing-product` | Missing product | PASS |
| `missing-media` | Missing product media | PASS |
| `transparent` | Transparent packshot | PASS |
| `white-rect` | Ordinary white rectangular media | PASS |
| `dark-rect` | Dark rectangular media | PASS |
| `portrait` | Portrait 4:5 media | PASS |
| `square` | Square 1:1 media | PASS |
| `landscape` | Landscape 3:2 media | PASS |
| `focal-left` | Focal subject near left edge | PASS |
| `focal-right` | Focal subject near right edge | PASS |
| `focal-top` | Focal subject near top edge | PASS |
| `focal-bottom` | Focal subject near bottom edge | PASS |
| `long-title` | Long product title | PASS |
| `long-cta` | Long editorial and product CTA | PASS |
| `adjacent` | Two adjacent instances | PASS |
| `deleted` | Deleted reference | PASS |
| `unpublished` | Unpublished reference | PASS |
| `represented` | Explicit represented sold-out variant | PASS |
| `selling-plan` | Selling-plan product-link fallback | PASS |
| `app-owned` | App-owned product-link fallback | PASS |
| `gift-card` | Unusual product-link fallback | PASS |
| `multiple-images` | Multiple images / one dominant object | PASS |
| `no-headline` | Headline omitted / semantic fallback | PASS |
| `no-optionals` | All optional content omitted | PASS |
| `catalog` | Ordinary low-art-direction catalog photo | PASS |
| `long-money` | Long money and localized unit price | PASS |
| `below-fold` | Below-fold section context | PASS |
| `beauty` | Beauty / Wellness content | PASS |
| `jewelry` | Jewelry / Accessories content | PASS |
| `food` | Food / Drink content | PASS |
| `wide` | Wide landscape catalog media | PASS |
| `two-line` | Intended two-line headline | PASS |

Single variants display their own price/state; unresolved options show a truthful price range and “choose options,” followed by a product link. The explicit represented unavailable variant shows CAD 62.00 and sold out. Compare-at/unit data only renders when valid. Selling-plan, app-owned and gift-card cases remain product-link fallbacks. Multiple images choose one first image, with no gallery or responsive duplicate. Mock fixture truth is not live Shopify/catalog verification.

The long-copy fixture has exactly 50% supporting-copy character expansion (30→45), with a long German headline and unrestricted natural wrapping. It intentionally mixes test languages; full locale parity is deferred. Intended two-line and 4+ line headings, empty optional content, omitted headline, long CTA/title/money/unit strings, all four focal edges, 4:5 / 1:1 / 3:2 / 2.5:1 media, and below-fold context are included. Geometry and content are shared across Beauty/Wellness, Jewelry/Accessories, and Food/Drink; human plausibility remains pending.

The neutral torture uses system-ui sans, gray/black/white tokens, an ordinary non-beauty utility-case catalog photograph, generic truthful copy and no motion. Its ordinary photo is a square bounded rectangular image surface; the separate white rectangular fixture is 3:2 and the wider-media fixtures test non-square envelopes. It uses the same DOM and geometry as branded.

## 5. Complexity report

- CSS: **69 physical / 69 nonblank lines**, **5,595 bytes** unminified.
- Browser JavaScript: **0 physical / 0 nonblank lines**, **0 bytes**. No JavaScript is needed; fixture selection is a native GET form and commerce is native links. Read-only browser audit instrumentation is not shipped.
- Shared component/rendering paths: **1** (`render_component`); one page harness and read-only navigation stubs surround it. No fixture/vertical mini-app or responsive DOM fork.
- Responsive breakpoints: **2**, at **768px / 1280px**; reduced-motion preference is not a layout breakpoint.
- Merchant-like semantic input groups: **6**: featured product, headline, optional eyebrow, optional support, optional editorial link, bounded token preset. Editorial link comprises label and destination. Preset has five finite token values (branded, neutral, beauty, jewelry, food), with one composition. No alternate composition has been introduced. Fixture ID/label/instance count/below-fold flags are test harness metadata, not merchant geometry controls. No x/y, dimensions, positioning, per-device settings, overlap amount, z-index, typography tuning, or raw CSS input.
- Component absolute positioning: **0**. Only the conventional skip link is absolute, anchored to the page origin with bounded insets; focus restores it at 12px. It is independent of the composition and does not solve a collision.
- Bounded geometry: mobile uses one grid-owned vertical rail and a -32px media registration; tablet/desktop use a horizontal grid datum and a fixed CSS-owned 48/64px media translation. Desktop's -36px media margin plus 64px translation leaves 28px of statement separation. Padding contains the media overhang. These are theme-owned structural rules, never fixture or merchant settings.
- Python renderer: **118 / 103** physical/nonblank lines, 6,588 bytes. Loopback server: **51 / 45**, 2,700 bytes. Tests: static **134 / 120**, browser evidence **103 / 92**, HTTP **42 / 35**. Python standard library only; no framework, build process or external runtime dependency.
- Media: **738,210 bytes** across 15 local product assets. One image per component. Primary object eager; below-fold and second-instance object lazy. No measured LCP/performance score is claimed; responsive Shopify CDN image transformation/priority remains a production gate.

## 6. Four controlling frames

All paths are repository-relative and under the authorized scope:

- `prototypes/living-canvas/monument/tests/evidence/branded-1440.jpg`
- `prototypes/living-canvas/monument/tests/evidence/neutral-1440.jpg`
- `prototypes/living-canvas/monument/tests/evidence/branded-390.jpg`
- `prototypes/living-canvas/monument/tests/evidence/neutral-390.jpg`

## 7. Stress frames

- `prototypes/living-canvas/monument/tests/evidence/rectangular-1440.jpg` — `white-rect`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/rectangular-390.jpg` — `white-rect`, 390px
- `prototypes/living-canvas/monument/tests/evidence/localized-1440.jpg` — `long`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/localized-390.jpg` — `long`, 390px
- `prototypes/living-canvas/monument/tests/evidence/missing-media-1440.jpg` — `missing-media`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/missing-product-1440.jpg` — `missing-product`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/sold-out-1440.jpg` — `sold-out`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/adjacent-1440.jpg` — `adjacent`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/adjacent-390.jpg` — `adjacent`, 390px
- `prototypes/living-canvas/monument/tests/evidence/localized-320.jpg` — `long`, 320px
- `prototypes/living-canvas/monument/tests/evidence/landscape-768.jpg` — `landscape`, 768px
- `prototypes/living-canvas/monument/tests/evidence/transparent-1440.jpg` — `transparent`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/dark-rect-390.jpg` — `dark-rect`, 390px
- `prototypes/living-canvas/monument/tests/evidence/portrait-768.jpg` — `portrait`, 768px
- `prototypes/living-canvas/monument/tests/evidence/focal-left-390.jpg` — `focal-left`, 390px
- `prototypes/living-canvas/monument/tests/evidence/focal-right-390.jpg` — `focal-right`, 390px
- `prototypes/living-canvas/monument/tests/evidence/focal-top-390.jpg` — `focal-top`, 390px
- `prototypes/living-canvas/monument/tests/evidence/focal-bottom-390.jpg` — `focal-bottom`, 390px
- `prototypes/living-canvas/monument/tests/evidence/wide-1024.jpg` — `wide`, 1024px
- `prototypes/living-canvas/monument/tests/evidence/long-money-320.jpg` — `long-money`, 320px
- `prototypes/living-canvas/monument/tests/evidence/long-title-375.jpg` — `long-title`, 375px
- `prototypes/living-canvas/monument/tests/evidence/long-cta-320.jpg` — `long-cta`, 320px
- `prototypes/living-canvas/monument/tests/evidence/below-fold-390.jpg` — `below-fold`, 390px
- `prototypes/living-canvas/monument/tests/evidence/beauty-1440.jpg` — `beauty`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/jewelry-1440.jpg` — `jewelry`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/food-1440.jpg` — `food`, 1440px
- `prototypes/living-canvas/monument/tests/evidence/two-line-1440.jpg` — `two-line`, 1440px

Keyboard focus: `prototypes/living-canvas/monument/tests/evidence/focus-390.jpg`.

Machine-readable observations: `browser-matrix.json`, `frames.json`, `interaction.json`, `capture.json`, `checks.json`, `changed-files.json`, all in `tests/evidence/`.

## 8. Known untested / deferred

- Human originality, polish, Theme Store screenshot potential, and the neutral kill conditions. No visual PASS is declared.
- VoiceOver/NVDA, axe/Lighthouse, actual browser zoom at 200%/400%, hardware touch/low-end devices, Safari/Firefox and broader browser coverage. Viewport reflow, native keyboard/focus and static motion absence do not substitute for these manual gates or full WCAG certification.
- Full translation/locale parity and RTL validation. Logical CSS properties preserve a plausible path; no RTL support claim.
- Real Shopify Liquid/schema/editor lifecycle, live product/Markets/localization APIs, native cart/variant/selling-plan/bundle/app behavior, pickup, accelerated checkout, rich video/3D media and complete theme journeys. This static experiment intentionally supplies safe product links, not those production features.
- Real network/mobile performance, LCP/CLS/INP, CDN srcset/sizes and measured fetch priority. Image dimensions and loading intent are present; no production performance PASS.
- Merchant usability tasks, live app blocks and the wider M1 product-system gate. No commercially narrowed media/copy envelope was needed by the observed fixture matrix.

## 9. Engineering verdict

**PASS — authorized isolated prototype scope only.** All final automated/static, observed geometry and native navigation checks above pass. This is neither overall M1 acceptance nor production/Shopify/accessibility certification. Future scope remains gated by its applicable controlling documents.

## 10. Visual verdict and stop

**PENDING HUMAN REVIEW.** Human review must decide **PASS TO PRESERVE / NARROW / FAIL** using both branded and neutral desktop/mobile frames and the stress evidence. Kill conditions remain unchanged. No styling rescue or second concept is proposed.

Commit locally and stop. No push, PR, merge, M2 or production work.

## Asset / code provenance

All component/fixture/server/test/CSS code and product-only SVG stress illustrations were authored for this isolated experiment. No competitor or other Living Canvas composition code was copied. Two product-only source images were generated with the imagegen skill: an unbranded everyday canvas bag and a mundane gray utility case on plain white catalog backgrounds, without copy, logo, props or UI. Native output dimensions were 1254×1254; local JPEG derivatives use 82/78 quality. These are fixture media, not baked layout screenshots or claims about real merchandise. SVGs contain only product-media stress illustrations; storefront headline, title, money, status and links remain semantic HTML.
