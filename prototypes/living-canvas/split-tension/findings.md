# Split Tension M1 — implementation findings

## Decision and authority

**Engineering/state-machine result: PASS within the simulated fixture scope and the explicitly observed browser journeys.**

**Experimental engineering recommendation: NARROW AND HOLD.** Do not advance to M2 or infer an overall M1 PASS. Visual/product-owner decision: **PENDING HUMAN REVIEW**. Manual accessibility, real commerce and measured performance are separate open gates.

Controlling baseline: branch `m0-live-market-evidence-2026-10-03`, starting commit `24e95425dce956127a1ea6d4fa1bc2711578df5c`. All six controlling documents were read before implementation. The commerce state machine wins over the brief; brief sections 1–24 are binding. The implementation uses one data-driven component and one pure engine. No stopped experiment was redesigned or acceptance criterion waived.

## 1. Engineering and state-machine evidence

`tests/state.mjs`: **335 passing assertions**. `tests/static.mjs`: **215 passing assertions**. Syntax checks for both required JS files and the optional server: **PASS**. `git diff --check`: **PASS**. Scope checks: **PASS**; only `prototypes/living-canvas/split-tension/` is added by the implementation commit.

The whole implementation was audited against the full state-machine contract, implementation brief, Living Canvas invariants, signature contract, product architecture and engineering standard. PASS below is restricted to the evidence column; a static PASS never means an experiential, visual or Shopify PASS.

### Binding implementation brief, sections 1–24

| Requirement | Result | Evidence / limitation |
|---|---|---|
| 1 Named experiment only | PASS | Isolated guided-merchandising question; no bundle, theme or milestone infrastructure |
| 2 Allowed files/scope/no dependencies | PASS | Manifest below; original native HTML/CSS/modules/local SVG; no package/install/build |
| 3 Structural visual composition | NARROW | CSS 5:8 desktop tracks, one boundary/overlap, staggered commerce edge; tablet relaxes; mobile sequential cards. Screenshots captured; premium/distinctive judgment pending |
| 4 Literal usable baseline | PASS / NARROW | Two authored steps/products/prices/links in literal index; default init attaches controls without replacing baseline. Real browser JS-disabled journey NOT TESTED |
| 5 Instance architecture | PASS | Root-scoped mutations/handlers; two-instance DOM and pending isolation recorded; idempotent init/bootstrap seam |
| 6 Shopify-shaped fixture data | PASS (simulated) | Product/variant/options/availability/int money isolated from authored label/copy; immutable fixtures |
| 7 Per-step rendering rules | PASS (simulated) | Missing editorial survives; unsafe products View product; no silent required choices; explicit sold-out/nonexistent states |
| 8 Inclusion rules | PASS | Initial false; valid-to-valid may retain consent; invalid clears; recovery does not re-include; duplicates link-only; aggregate omitted below two eligible |
| 9 Money/summary | PASS (simulated) | Integer sums; exact BigInt formatting; selected count/context; no summed compare-at or savings; unit context per item |
| 10 Aggregate simulation | PASS (simulated) | Frozen quantity-1 payload; success/failure/ambiguous/422 truthful; no global count or Shopify call |
| 11 Async/races | PASS | Monotonic version, timer cleanup, dead/version rejection, controls frozen; real pending fixture switch observed |
| 12 Accessibility interactions | NARROW | Native controls, labels, scoped status/alert, focus style; observed keyboard Space/Tab/Enter and request focus return. AT/manual coverage open |
| 13 Required widths | PASS for DOM reflow / NARROW for experience | 168 browser checks across all seven widths; no page overflow, primary target boxes >=44. Human legibility/zoom/touch approval open |
| 14 Canonical 24 fixtures | PASS | Fixture table below; risk subcases reuse same engine |
| 15 Separate harness controls | PASS | Labeled header selector/diagnostics outside storefront; unknown query fallback; no commerce persistence in URL |
| 16 Progressive enhancement/no-JS | NARROW | Literal source, enhancement-withheld screenshot and initialization-failure browser evidence. Actual disabled-JS browser test remains manual |
| 17 Performance architecture | PASS for structure / NOT TESTED measured | Local assets only, no gallery/carousel/video/runtime/layout measurement; dimensions reserved; later images lazy. No performance claim |
| 18 Safe output/lifecycle | PASS | Text APIs, validated local media/root-relative URLs, immutable data, idempotent seam, cleanup/reset; no executable fixture HTML |
| 19 Full self-audit | PASS | This full requirement audit, explicit open gates, no overall M1 PASS |
| 20 Minimum checks | PASS | Syntax, transition/static checks, diff/scope checks; actual browser capture available |
| 21 Stop conditions | PASS within tested scope | No evidence requiring bundle/full PDP/freeform widget/framework/rescue settings; visual viability undecided, not asserted |
| 22.1 One engine | PASS | No fixture-specific component implementations |
| 22.2 Hydration identity | PASS | Literal default matches fixture IDs/order/title/price/availability; only enhancement inserted; pageshow reset retains nodes |
| 22.3 Nonexistent combination | PASS | 60 ml + Rich has no variant; stale identity/price/consent cleared; recovery without reload |
| 22.4 Compare-at/unit-price mutations | PASS | 30 ml Light ↔ 60 ml Light updates 2900 ↔ 4700, compare-at 3400 ↔ absent, unit 9667 ↔ 7833 per 100 ml |
| 22.5 Fixture teardown while pending | PASS | Engine timer assertion and observed browser switch during pending; replacement stays zero/unselected with no old status |
| 22.6 Query/history | PASS for observed journey | Unknown value falls back; actual back navigation restores zero choices/total, including native browser form restoration |
| 22.7 Announcement discipline | PASS for code / NARROW for AT | Routine price/options not live; request status scoped/atomic, error alert only changes for validation; identical text not repeated |
| 22.8 Failure resistance | NARROW | Long heading/title, missing image, square/portrait/landscape, five steps rendered; no fixed text height. Browser text enlargement still NOT TESTED |
| 22.9 Visual ownership | NARROW | PENDING HUMAN REVIEW; no inferred visual acceptance |
| 22.10 Visual floor | NARROW | Authored spacing/type hierarchy, edges and card states captured. Human premium/distinctive decision pending |
| 22.11 Browser evidence | PASS for capture | Every mandatory capture listed in section 2 |
| 22.12 Transition assertions | PASS | 335 assertions; every listed minimum plus dense variants, pending freeze and review gating |
| 22.13 Complexity | PASS for reporting / NARROW for assessment | Metrics below; no invented numeric PASS threshold |
| 22.14 No fake Shopify verification | PASS | All fixtures/outcomes expressly simulated; no integration/atomicity claims |
| 23 Pre-code approval boundary | PASS | Isolated M1 implementation only |
| 24 Completion output | PASS for artifact preparation | Exact manifest, tests, metrics, limits and recommendation reported; commit SHA supplied in final task response |

### Commerce state machine, including red-team corrections

| Contract rule | Result | Evidence / boundary |
|---|---|---|
| State/data/selection ownership (1–3) | PASS (simulated) | Editorial separate; commerce immutable; instance shopper state only |
| Missing/link-only/unresolved/available/sold-out states (4) | PASS | `resolve`, fixture/browser matrix; missing controls omitted |
| Pending/error/success states (4) | PASS (simulated) | Scoped request result, selected card state attributes; no success accounting inferred on failure |
| Explicit complete option tuple (5) | PASS | No option default; nonexistent and sold-out tested; ID and all money derived together |
| Selling-plan/app/unusual purchase narrowing (6) | PASS (simulated) | Selling plans, app-owned, quantity, properties, gift-card flag excluded; ordinary variants alone allowed |
| Resolved + included + available + eligible totals (7) | PASS | Exact transitions; no implicit consent, aggregate compare-at or fake savings |
| Preconditions/frozen request/result authority (8) | PASS (simulated) | Invalid selected step blocks; captured payload immutable; zero optimistic success |
| Ambiguous partial result (8,18.4) | PASS (simulated) | Never infer item-level confirmation; review warning required before explicit simulated retry |
| Useful no-JS discovery (9) | NARROW | Literal baseline + local product-navigation adapter; disabled-JS manual test still open |
| Sequential mobile order (10) | PASS structure / NARROW experience | One DOM; 320–430 vertical cards; no sticky collision; no carousel |
| Accessibility/focus (11) | NARROW | Labels/native controls, error identifies affected product; scoped messages; submit focus restoration; AT/zoom/touch open |
| Missing/mutated data (12) | PASS (simulated) | Missing product/media, price/compare/unit, 422 availability, 30–50% body expansion; no dead commerce shell |
| Shallow merchant boundary (13) | PASS for absence of rescue settings | Authored content plus data only; no editor constructed or merchant-operability claim |
| Lifecycle/performance direction (14) | PASS structure / NOT TESTED production | Version/timer/listener cleanup, no eager-all media/dependencies; real editor/performance later |
| Fixtures/acceptance/prototype scope (15–17,19–21) | NARROW overall | Canonical fixture matrix complete; engineering logic passes; manual/product gates not closed |
| Explicit consent and deterministic restoration (18.1) | PASS | No auto include; invalid clears; browser restoration reset verified |
| Quantity/duplicate rule (18.2,18.12) | PASS | Quantity 1; all repeated product references link-only; no coalescing or duplicate purchase; below-two/zero eligible omit action |
| Inventory race/version isolation (18.3) | PASS (simulated) | 422 updates advisory availability, clears invalid inclusion, keeps recovery links and unaffected choices |
| Money/context (18.5) | PASS (simulated) | CAD two digits, KWD three digits; zero-digit formatter assertion; context switches discard selection. Real Markets NOT TESTED |
| Required properties (18.6) | PASS (simulated) | No hidden properties copied; link-only |
| Accelerated checkout/global cart (18.7–18.8) | PASS scope | Neither implemented; success has local cart-review placeholder, no invented cart count/drawer/event bus |
| Multiple instances (18.9) | PASS | IDs/names unique, request isolation observed; one failure cannot stop another |
| Native forms/Enter (18.10) | PASS structure / NARROW full manual | No forms/nesting; native button/checkbox/select; Enter/Space representative journey observed |
| Initialization/output (18.11,18.13) | PASS | Failure before controls attach, baseline survives, no executable fixture text |
| Separate visual gate (18.14) | NARROW | Evidence captured; human ownership remains explicit |

### Living Canvas invariants and broader contracts

| Invariant / governing concern | Result | Evidence / remaining gate |
|---|---|---|
| Content model + bounded controls | PASS prototype structure | Shared editorial/step/product model; same grammar across fixtures, zero rescue/editor controls. Editor model later |
| Missing/empty/minimal data | PASS (simulated) | Meaningful editorial fallback, missing media, one valid product, all ineligible, coherent lists |
| Product/variant/pricing truth | PASS (simulated) | Fixture authority only; real Shopify product/media/money truth not verified |
| Ratings/scarcity/proof | PASS for omission | No ratings, fake urgency, inventory counts, evidence statistics or fabricated discounts |
| App ownership | PASS boundary / NOT TESTED integration | App-owned, selling-plan and property products go to View product; no app engine |
| DOM/keyboard/focus | PASS observed structure / NARROW overall | Logical editorial → ordered steps → summary, native controls, visible focus; no overlays/traps; full AT/manual keyboard journey open |
| Touch/mobile/maximum density | PASS measured boxes/reflow / NARROW experience | All fixture widths; large labeled targets, five vertical steps, two selects maximum; physical touch and premium usability undecided |
| Long content/localization | NARROW | 30–50% paired body expansion, longer headings/titles/option label, no fixed text height. Real translation/RTL/text enlargement later |
| JS failure | NARROW | Literal baseline and contained init failure; withheld enhancement observed; actual disabled-JS manual test open |
| Lifecycle | PASS harness / NOT TESTED Shopify editor | Idempotent roots/bootstrap, cleanup, stale rejection, reset; section load/unload/reorder not implemented in M1 |
| LCP/media/performance | PASS structure / NOT TESTED measurement | Four local SVGs with real intrinsic ratios, reserved image size, below-first media lazy, one DOM; no Lighthouse/network budget certification |
| Decorative JS/motion | PASS code / NOT TESTED preference test | CSS owns geometry; no animation dependency or essential motion; reduced-motion rule. OS/browser preference not manually tested |
| Ordinary media/originality | NARROW | Neutral system font/monochrome/ordinary object packshots preserve same CSS grammar; distinctiveness needs human decision |
| Preset/merchant usability | NOT TESTED wider gate | Neutral non-beauty content reuses engine; Jewelry/Food presets, first-time merchant tasks and control editor not built |
| Accessibility/performance claim discipline | PASS | No WCAG, AT, Lighthouse or device PASS inferred from static/DOM checks |
| Product architecture (general resilience) | NARROW | 1/2/6/24 variants tested, sold-out, long option label, price/unit, image ratios, absent image, gift-card/link-only, plans/app semantics modeled. Broader PDP/cart/gallery/video/3D/pickup/app/collection tests remain later scope |
| Engineering standard sections 1–16 | NARROW applicability | Native semantic baseline, safe output, local/no-dependency CSS/modules, scoped lifecycle, commerce truth, provenance and evidence discipline applied. M2+ Liquid/schema/app blocks/locales/revalidation/PR gates not implemented or claimed |
| Full M1 proof package/signature system | NOT TESTED wider gate | No other Living Canvas composition, Commerce Mosaic, PDP family, Evidence Layer or production surfaces built; global M1 exit criteria remain open |

### Canonical fixture coverage

| # / ID | Executable risk exercised | Evidence |
|---|---|---|
| 1 simple | Two singles, literal baseline/default | Static identity, state + browser, desktop capture |
| 2 maximum | Five steps; 1/2/6/24 variants and mixed media ratios | Every dense tuple asserted; 375 capture; all widths |
| 3 multi-option | Empty/partial choices, real tuple, nonexistent tuple, unit context | State and browser transitions, unresolved/resolved/nonexistent captures |
| 4 variant-sold-out | Explicit 30 ml + Rich | State transition; fixture browser initial state; human sold-out journey can repeat |
| 5 fully-sold-out | Entire product unavailable, no purchase | State + browser omission |
| 6 missing | Missing product, meaningful editorial step survives | State + browser |
| 7 mixed | Available + unresolved + app-owned | State + browser |
| 8 selling-plan | Terms unsafe inline | State + browser (simulated) |
| 9 price-mutation | Price/compare-at/unit update together | State + observed browser transition |
| 10 localized | 30–50% paired body copy, very long heading/title, absent media | State expansion assertions, 320 capture, all widths |
| 11 neutral | Monochrome, system type, generic objects | 1440 capture, same engine/layout; human originality open |
| 12 no-js | Enhancement withheld; literal default also available | Source + withheld capture; actual browser-disabled JS NOT TESTED |
| 13 failure | Failed request, choice preservation, retry | State + browser error capture and focus check |
| 14 ambiguous | No full success; review gating survives mutation | State + browser, ambiguous capture |
| 15 inclusion | Zero items/total, unchecked eligible products | State + browser every fixture |
| 16 quantity-rule | View product only | State + browser (simulated) |
| 17 duplicate | Repeated product references link-only; authored sequence survives | State + browser; only one eligible → no aggregate |
| 18 two-instances | Unique labels/IDs/names, independent selections/pending | State + browser isolation, 1280 capture |
| 19 init-failure | Failed first instance retains fallback; second enhances | Browser controls/links asserted; capture |
| 20 inventory-race | 422/availability mutation clears only invalid selection | State + browser inventory capture; safe product links remain |
| 21 ineligible | No eligible aggregate; no permanent disabled scar | State + browser |
| 22 one-surviving | One valid product, useful discovery, aggregate omitted | State + browser |
| 23 money | 101 + 202 = KWD 0.303; context never mixed | State + browser initial reflow; real Markets untested |
| 24 properties | Required line properties narrow to link | State + browser (simulated) |

Duplicate policy intentionally makes **all** repeated product references link-only, rather than choosing an arbitrary privileged step or silently coalescing. This is the permitted safe narrowing in the controlling duplicate rules.

## 2. Browser/visual evidence actually captured

Codex in-app browser, native viewport overrides. All fixture/width reflow checks cover **320, 375, 430, 768, 1024, 1280, 1440** CSS pixels, 900px viewport height. `browser-matrix.json` contains **168** observed cases: zero page horizontal overflow, zero duplicate IDs, zero initial checked items and all visible primary component target boxes >=44 CSS px. This is DOM geometry evidence, not proof that every experiential quality passes.

Mandatory captures:

- `default-1440.jpg`
- `neutral-1440.jpg`
- `maximum-375.jpg`
- `multi-unresolved-1440.jpg` and `multi-resolved-1440.jpg`
- `localized-320.jpg`
- `two-instances-1280.jpg`
- `request-error-1440.jpg`

Additional captures: nonexistent combination, ambiguous review, inventory 422, initialization failure, enhancement withheld, keyboard focus and pending fixture switch. JSON transition/lifecycle records show actual observed DOM values, not assumed platform results. Runtime assertions in the browser checked those records before saving.

Observed defects corrected during verification:

1. A desktop heading wrapped its punctuation onto a separate line; bounded type scale corrected, screenshots refreshed.
2. Review-link hash navigation reset the fixture via history handling. The enhanced placeholder now reveals/scrolls to its local review explanation without writing browser history.
3. Browser back navigation restored a native checkbox while the engine total was zero. A next-task pageshow reset synchronizes native controls and engine while retaining baseline nodes. Actual browser back journey passed afterward.
4. Disabled native submit buttons lost focus during requests. Focus returns to the initiating visible control only when no other element received focus; success/failure Enter journeys passed afterward.
5. Ambiguous results could previously be cleared by changing inclusion. The warning/review gate now survives mutations; engine and browser checks pass.

6. Initial state/static checks rejected camelCase fixture flag handles as invalid product URLs; those handles were converted to deterministic kebab-case and all checks passed.

No captured screenshot itself decides premium quality, structural originality, mobile comprehension or Theme Store acceptability.

## 3. Visual/product-owner decision

**PENDING HUMAN REVIEW.** Review the desktop asymmetry, neutral structural identity, two-/five-step intentionality and mobile guided sequence, including how much vertical space the long/complex fixtures consume. Ordinary SVG packshots intentionally contribute no signature artwork. No merchant layout rescue control exists.

Do not approve the composition solely from the logic verdict or DOM geometry checks. Kill/narrow the composition if these captures do not meet the intended visual identity or mobile quality.

## 4. Simulated behavior versus real Shopify behavior

Only a local timer models request success/failure/ambiguous/inventory outcomes. No real API, native product form, cart count, cart drawer, selling plan, application purchase flow or market integration exists. Success says **simulated confirmation** and explicitly says no real cart changed. Ambiguous results infer no line identity. The local review placeholder explains that authoritative reconciliation is unavailable; explicit retry only repeats the simulation.

The optional static server supplies read-only modeled product destinations to exercise useful local link navigation. It proves neither a Shopify PDP nor a real purchase path. Root-relative production-shaped URLs would be sourced from real product objects in production.

Real Shopify multi-line atomicity, partial-result reconciliation, cart state, inventory races, quantity rules, line properties, active Markets/money and app/selling-plan semantics are **NOT TESTED**. They require dated official evidence and a real-store gate at the appropriate milestone.

## 5. Every untested/manual category

- **Visual/product-owner acceptance:** premium quality, structural originality under neutral mode, thumbnail identity, two-/five-step intent, comprehensibility of long/complex mobile sequence.
- **Actual browser JavaScript disabled/delayed:** literal HTML inspected and enhancement withheld/failed tested; disabling browser JS and delaying module delivery were not performed.
- **Accessibility:** VoiceOver, NVDA, complete independent keyboard journey, real announcement/focus/error perception, contrast/conformance audit, axe, Lighthouse Accessibility, browser text enlargement, manual 200%/400% zoom/reflow, OS/browser reduced-motion preference, representative physical touch/mobile devices.
- **Performance:** Lighthouse Performance, LCP/CLS/INP/CWV, real responsive CDN/srcset strategy, network attribution and budgets, low-end/mobile/network profiling, image-loading priority measurements. No fast/performance PASS claim.
- **Browser compatibility:** current in-app browser evidence only; Safari/Firefox/other supported versions/device engines not independently tested.
- **Real commerce/platform:** actual Shopify Cart API/atomicity/reconciliation, live stock/422, product/variant/Liquid serialization, Shopify money/Markets/tax/shipping/duty/discount/unit-price rules, plans, apps, personalization/recipient/quantity rules, product links/PDP/native forms/cart/accelerated checkout/pickup.
- **Production/editor lifecycle:** real Shopify section load/unload/reorder/duplicate/add/remove/re-render, app-block insertion in expected/awkward positions, route loading/global cart integration, schema/locales/packaging/volatile-requirement revalidation. Harness equivalents do not prove these.
- **Broader M1 product/design:** Jewelry/Accessories and Food/Drink preset proof, actual merchant settings/tasks/editor/control-budget usability, developer-extension exercise, video/3D and gallery media, realistic collections/search/filter/pagination, full PDP/cart/core-template proofs, other Living Canvas variants and full signature-system exit criteria.
- **Localization:** production translations/locale parity, actual Markets context mutation and RTL feasibility in-browser remain untested. The mixed-language expansion fixture is stress data, not a finished translation.

## 6. Deviations and bounded implementation choices

**No known deviation from the binding Split Tension implementation brief.** No acceptance requirement was weakened to obtain PASS. Open manual evidence is classified above rather than silently waived.

Bounded choices permitted by the contracts: all duplicate references become link-only; aggregate eligibility counts current resolved/available/inline-eligible steps; native selects use an unselected “Choose…” placeholder with full visible/programmatic group labels; failure retries repeat deterministic fixture behavior; the ambiguous review route is an explicit local simulation limitation, not fake reconciliation. The optional local server is a small dependency-free test script with read-only navigation stubs, not new preview/build infrastructure or a PDP implementation.

The general product architecture's larger M1 proof package is not completed by this isolated request. Those categories are open, not presented as implicit N/A/PASS or implemented as unauthorized scope expansion.

## 7. Complexity metrics

Metrics count shipped runtime `fixtures.js` + `split-tension.js`, excluding tests/evidence. No arbitrary numeric PASS threshold is claimed.

- **Nonblank, non-comment JS lines: 491.** **496 physical non-comment lines including blanks** (75 fixtures + 421 component); see final check record.
- **CSS lines: 125.** Source intentionally uses compact rules; byte metrics are reported in the final check record to avoid implying that line count alone measures size.
- **Runtime state fields:** 6 top-level engine fields (`fixture`, `steps`, `version`, `request`, `alive`, `unavailable`); each step has 2 (`choices`, `included`); an active request has 5 (`status`, `token`, `payload`, `message`, `reviewed`). Maximum five-step instance: 21 named slots when those nested field definitions are counted with the top-level fields. Variant/price/eligibility/total are derived, not separately cached.
- **Lifecycle adapter storage:** per-instance state reference, one timer handle, scoped DOM refs/enhancement-node list and aggregate refs; bootstrap owns controller handles and one next-task history-reset timer. These are lifetime handles rather than additional commerce truth. No mutable global commerce store.
- **Event types handled: 4** (`change`, `click`, `popstate`, `pageshow`). Instance handles only change/click; documented shared bootstrap handles query/history/native restoration.
- **Distinct interactive native control types: 4** (select, checkbox, button, link). No custom widgets, form, carousel, modal or gesture system.

The DOM adapter is the largest portion; most of its cost is native labeled control construction, lifecycle/failure rollback and transaction messaging. Native restoration and disabled-button focus required explicit lifecycle handling, so “zero lifecycle complexity” would be an inaccurate claim. The bounded runtime merits **NARROW** until experiential/product review confirms its value; production must not copy this harness or add settings to rescue a weak signature.

## 8. Scope and provenance

Every added repository file is under the authorized prototype path. No existing repository file is modified. No production `sections`, `blocks`, `templates`, `snippets`, `config`, `locales`, `layout` or `assets` is touched. No Skeleton/Dawn/Horizon foundation, package, framework, remote font, analytics, external UI/carousel library or third-party request is introduced. No M2, other Living Canvas variant, PR or merge work is performed.

Implementation is original native code and simple original SVG fixture objects. No theme/competitor code or external asset is imported. The repository commit is local on the requested branch; no push or PR is part of this task.

### Exact added-file manifest

All paths below are relative to `prototypes/living-canvas/split-tension/`. The task adds these files only:

- `README.md`
- `findings.md`
- `fixtures.js`
- `index.html`
- `media/bottle-portrait.svg`
- `media/bottle.svg`
- `media/box.svg`
- `media/jar.svg`
- `split-tension.css`
- `split-tension.js`
- `tests/evidence/ambiguous-1440.jpg`
- `tests/evidence/browser-lifecycle.json`
- `tests/evidence/browser-matrix.json`
- `tests/evidence/browser-transitions.json`
- `tests/evidence/checks.txt`
- `tests/evidence/default-1440.jpg`
- `tests/evidence/enhancement-withheld-1440.jpg`
- `tests/evidence/initialization-failure-1440.jpg`
- `tests/evidence/inventory-422-1440.jpg`
- `tests/evidence/keyboard-focus-375.jpg`
- `tests/evidence/localized-320.jpg`
- `tests/evidence/maximum-375.jpg`
- `tests/evidence/multi-resolved-1440.jpg`
- `tests/evidence/multi-unresolved-1440.jpg`
- `tests/evidence/neutral-1440.jpg`
- `tests/evidence/nonexistent-1440.jpg`
- `tests/evidence/pending-switch-neutral-1280.jpg`
- `tests/evidence/request-error-1440.jpg`
- `tests/evidence/two-instances-1280.jpg`
- `tests/serve.mjs`
- `tests/state.mjs`
- `tests/static.mjs`
