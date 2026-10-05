# Split Tension — isolated M1 validation

One native browser implementation, one pure state engine, 24 deterministic fixtures. This is guided merchandising, not a bundle builder. All cart outcomes and commerce data are simulated. Nothing calls Shopify or changes a real cart.

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

## Run

From the repository root, with Node.js 22+ (verified with Node 26.10.0):

```sh
node prototypes/living-canvas/split-tension/tests/serve.mjs
```

Open **http://localhost:3000/**. The server binds only to `127.0.0.1`. There is no install, dependency, build or remote asset. Stop the server with Ctrl+C. `PORT` may select another port; use that port in the URL.

This small static server includes read-only `/products/...` fixture destinations so baseline product links navigate successfully locally. These destinations are navigation adapters, not PDP architecture, live Shopify pages or purchase support. A generic static server can serve the HTML/CSS/modules, but must map these fixture product URLs to test local product navigation. Real production links would come from Shopify product objects.

The header is test instrumentation, separate from the storefront. Choose a fixture there, or use `/?fixture=multi-option`, `/?fixture=maximum`, etc. Unknown values safely use `simple`. The query stores only the fixture identity. Every switch tears down timers/listeners and discards shopper choices. Back/forward restoration resets native form values and engine state after browser restoration; it never restores inclusion.

## Exercises

- All eligible items load unchecked. Include an item explicitly to add its price to the selected-items total. Quantity is 1. No compare-at aggregate, savings, discount or checkout-total promise is offered.
- `multi-option`: choose **30 ml + Light** (available), **30 ml + Rich** (sold out), **60 ml + Rich** (nonexistent), or **60 ml + Light** (available, changed price/no compare-at). A transition into invalidity clears inclusion; recovery does not re-include.
- `maximum`: five steps, with 1-, 2-, 6- and 24-variant product subcases and square/portrait/landscape media. Each complex product uses at most two native selects.
- `price-mutation`: include the resolved formula, then change size. Current price, compare-at, unit price and eligibility transition together.
- `duplicate`: both repeated product references narrow to product links; the authored steps remain. The remaining single eligible item gets inclusion but no aggregate action.
- `failure`: select and submit, then retry. The failure is deterministic and preserves valid choices.
- `ambiguous`: select and submit. Neither item-level success nor full success is inferred. Selection changes cannot remove the warning or bypass review gating. **Review simulated cart** reveals the simulation limitation; only then can **Retry simulation** repeat the response. This is not real reconciliation.
- `inventory-race`: the first submitted variant becomes unavailable after a simulated 422. Its inclusion clears; unaffected selections remain. When fewer than two eligible items remain the aggregate action is omitted, while the error and product recovery links remain.
- `two-instances`: add in one instance while changing the other. IDs, labels, totals, pending state and messages are independent.
- `init-failure`: instance one deliberately fails before exposing controls. Its baseline survives and instance two enhances normally.
- Start a request, then immediately switch fixtures. The outgoing instance is destroyed and cannot update the replacement.
- `money`: select both items. 101 + 202 integer minor units = KWD 0.303. Currency/context is fixture-owned; changing fixtures resets it and shopper state.

## Real no-JavaScript test

Disable JavaScript using the browser's own setting, then reload `/` or `/index.html`. The literal HTML supplies the default editorial proposition, two ordered products, CAD 24.00/CAD 38.00, availability and working product links via the local adapter. It contains no option, inclusion or aggregate controls. The fixture header's selector is also hidden until successful bootstrap.

`no-js` with JavaScript enabled deliberately withholds enhancement; it does **not** prove the browser-disabled-JS condition. With JS disabled, query fixtures cannot change the literal default baseline. The initialization-failure fixture separately tests an instance failing without deleting its fallback.

## Checks

From the repository root:

```sh
node --check prototypes/living-canvas/split-tension/fixtures.js
node --check prototypes/living-canvas/split-tension/split-tension.js
node --check prototypes/living-canvas/split-tension/tests/serve.mjs
node prototypes/living-canvas/split-tension/tests/state.mjs
node prototypes/living-canvas/split-tension/tests/static.mjs
git diff --check
```

The state tests exercise transitions, exact totals, consent clearing, 2/6/24 variant tuples, duplicate narrowing, unsafe exclusions, submission preconditions, pending freeze, failure/ambiguity/422, review gating, instance isolation and stale local timers. Static checks inspect the fixture matrix, literal fallback identity, safe text/URLs, dependencies and change scope.

Browser evidence is checked in under `tests/evidence/`. `browser-matrix.json` records 24 × 7 viewport checks. The other JSON records contain observed DOM results from the Codex in-app browser. They are captured evidence, not a new browser test framework; no automation dependency is shipped. Re-run the native browser journeys for independent review.

## Evidence limits

Read `findings.md` for the accepted human verdict and its scope. Engineering logic and observed browser checks do not authorize production, validate Shopify atomicity, establish WCAG conformance or decide visual quality. Visual/product-owner decision is **PASS TO PRESERVE**, recorded from human review. VoiceOver, NVDA, actual JS-disabled browsing, manual text enlargement/200%/400% zoom, physical touch and measured performance remain untested. The broader M1 product/app/editor/cross-preset proof package is outside this isolated prototype and remains open.

## Approved second visual pass

The shared composition now uses a dominant editorial image field, large boundary-crossing product media, open commerce zones and one numbered rail ending in the aggregate action. Tablet/mobile relax the overlap while preserving the same ordered DOM and engine. Neutral changes only tokens/type/content/media. The `maximum` fixture supplies landscape editorial media; `missing` omits editorial media; ordinary and transparent product art coexist.

Read [second-pass-report.md](second-pass-report.md) for the current verdict, exact audit and complexity delta. Original evidence remains historical; final second-pass frames and JSON are under `tests/evidence/second-pass/`. Run `node prototypes/living-canvas/split-tension/tests/second-pass.mjs` from repository root to verify the original commerce engine/adapter/fixture semantics/test files are unchanged. The script-free fallback evidence is served at `/tests/evidence/second-pass/server-fallback.html`; it removes the literal index's script and adds only a base URL to resolve nested assets. This is distinct from browser-wide JS disabling.
