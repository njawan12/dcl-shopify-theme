# M1 Evidence Layer / Evidence Rail

**Engineering verdict: NARROW** — executed isolated content, semantic, server and browser checks pass; live Shopify/app compatibility and accessibility certification remain untested. **Human M1 visual verdict: PASS TO PRESERVE.**

Human review accepts:

- the Evidence Rail as a recognizable proof language;
- survival of the neutral/originality torture test;
- successful desktop-to-mobile structural adaptation;
- successful use across PDP and editorial contexts;
- comparison as acceptable differentiated evidence hierarchy;
- no further M1 visual iteration required.

Desktop opening-space balance, typography refinement and comparison presentation are deferred to production art direction and are **not M1 blockers**. This does not authorize further M1 visual iteration or M2.

The engineering verdict remains **NARROW**. All unresolved production/integration gates remain open, including live Shopify Theme Editor execution, real `@app` integration, merchant usability, accessibility/AT/zoom, localization/RTL, cross-browser/touch, production performance and full-theme integration. Human visual acceptance does not certify these gates.

This is a separately authorized isolated experiment, not an edit to the preserved attached-proof Evidence Layer. Controlling documents: `docs/m1-evidence-layer-prebuild-red-team-contract.md` and `docs/m1-evidence-layer-implementation-brief.md`, committed before implementation. Local branch `m1-evidence-layer-evidence-rail`. No production or M2 authorization.

One CSS-owned subject/evidence/qualification rhythm, three narrow semantic primitives: Evidence Note (fact/metric/claim/certification/merchant-authored quote), Evidence Pair (static labelled before-after or comparison), Process Sequence (ordered even when only one valid step survives). PDP attachments have truthful read-only product context, media notes and separate education attachments. Editorial uses notes OR process. There is no universal mega-section, runtime JS, review widget, before-after slider or merchant positioning UI.

## Run

From repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/evidence-rail/serve.py
```

Open http://127.0.0.1:3004/. Port override: EVIDENCE_RAIL_PORT. All assets are local. Native GET fixture selector is harness instrumentation. Product/editorial/guest links go to read-only local stubs, never a cart or review service. Literal index.html is generated from the exact default server output and has no scripts/dead enhanced controls. A basic static server may serve the index, but does not implement the fixture/query/navigation routes.

The approved manual content schema is sufficient. Dynamic-shaped connections only model value/fallback/omission, not live Shopify metafields. All evidence is explicitly synthetic, including quotations/certification and schematic before-after; none represents genuine merchant proof or independently verified claims. Source links express context, not credibility. URL completeness/rendering validity checks never judge factual truth.

## Controls and apps

Presentation budget: note2(density/system scheme), pair3(mode/density/system scheme), process2(density/system scheme); conditional0; app0 new settings. Presets reuse global semantic schemes, not new per-primitive font/color controls. Notes8 fields/max3; pair shared6 fields+two4-field sides OR two subjects/four4-field rows; process shared4 fields/four5-field steps. Geometry/order/media containment are authored. Fixture/preset/binding/guest switches are test data, not a merchant page builder.

`app-host.liquid` is a non-deployed real @app schema/dispatch architecture specimen, not production theme code. The section-defined block seam uses generic @app with no forbidden limit and render-block dispatch. Local tests insert independent plain/tall/wide documents at expected/awkward/reordered positions and remove/duplicate guests. Guests own their internal presentation; host owns ordinary-flow wrapper and accessible local overflow. No fabricated app UI, stars/counts or vendor integration. Static architecture plus local geometry does not prove live Shopify Liquid/editor/app execution.

## Checks and evidence

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/evidence-rail/tests/static.py
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/evidence-rail/tests/server.py
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/evidence-rail/tests/browser.py
git diff --check
```

Server suite requires port3004 running. Browser suite consumes captured observations, checks every38×8 pair and fingerprints; it never manufactures geometry. Recapture protocol is `tests/recapture.md`. Test-only capture probe and the in-app browser are not storefront dependencies. Browser evidence is304 views,43 full-page review JPEGs and4 supplements. Main controlling frames: branded-pdp/neutral-pdp/branded-editorial/neutral-editorial at1440 and390, all under tests/evidence. Full list frames.json. Known limits and exact counts/complexity are in findings.md.

Human review has accepted **PASS TO PRESERVE** for this Evidence Rail proof. No automated visual verdict is awarded. Preserve the implementation; no further M1 visual iteration, experiment, push, PR, merge or M2 is authorized.
