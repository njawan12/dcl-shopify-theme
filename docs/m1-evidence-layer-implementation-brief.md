# M1 Evidence Rail — isolated implementation brief

Date: 2026-10-05. Controlling contract: [pre-build red-team contract](m1-evidence-layer-prebuild-red-team-contract.md). Status: pre-code self-red-team closed for user-authorized isolated M1 experiment; no claim of a new human visual approval. Conflict means stop before code.

## 1. Branch, paths and preservation

Dedicated local branch `m1-evidence-layer-evidence-rail`, from current preserved documentation lineage `39bd22bfa717951e746dc2be0035a687348d53e8`. Commit these two controlling docs before writing runtime code. Then implement only `prototypes/evidence-layer/evidence-rail/`. Do not modify prior attached-proof, Split Tension, Monument, Edge Crop, Quiet Frame, Commerce Mosaic, any production code or preserved refs. Do not cherry-pick/merge unrelated branch implementations.

Allowed: README/findings, fixture/data normalizer, three primitive renderers/host renderer, CSS, literal index, dependency-free Python local server, copied local packshot/schematic media with provenance, isolated non-deployed app-host.liquid specimen, tests/independent guest HTML and evidence. No framework/install/build/runtime browser dependency. Existing bundled browser automation may capture tests; its JS stays test-only.

## 2. Exact fixture inventory

38 fixtures, one implementation, eight widths = **304 fixture/width views**:

1 branded-pdp; 2 neutral-pdp; 3 branded-editorial; 4 neutral-editorial; 5 jewelry; 6 food; 7 zero; 8 one; 9 dense; 10 missing-optional; 11 no-media; 12 portrait; 13 landscape; 14 metric-no-source; 15 long-claim; 16 long-source; 17 long-quote; 18 translation; 19 rtl; 20 before-after; 21 before-after-incomplete; 22 comparison; 23 comparison-incomplete; 24 reorder; 25 repeated; 26 manual; 27 dynamic; 28 disconnected-fallback; 29 disconnected-omit; 30 app-absent; 31 app-expected; 32 app-awkward; 33 app-tall; 34 app-wide; 35 app-removed; 36 app-reordered; 37 one-process; 38 editorial-process.

Dense =3 notes+4 comparison rows+4 steps. Invalid required note/issuer/quote attribution, optional invalid media, malformed/unsupported URL and unresolved fragment subcases exercised by static normalization tests. Dynamic fixture uses same fields as manual; disconnection has explicit fallback or omission. Before-after uses explicitly schematic non-clinical storage arrangement, not invented customer results. Long claim/source/quote are readable authored test strings, translation includes50% expansion, CJK/unbroken strings. RTL sets real dir=rtl and Arabic context. Repeated has independent instance IDs/content, includes duplicate guest stress. Reorder changes valid source block order; app-awkward between evidence education attachments, app-reordered before notes, removed identical evidence to absent. JS delayed/failed is same static output with JS disabled; separately capture no-JS neutral proof and reduced-motion neutral proof.

## 3. Coverage and app seam

Evidence Note covers fact, metric, claim, certification, quote with distinct kind labelling, required fields and qualifications. Evidence Pair covers labelled alternatives/static before-after and comparison with semantic table. Process Sequence includes4-step and ordered one-step. PDP media note attachment, distinct PDP education pair/process, editorial notes and editorial process. One manual data path and source adapter; no invented commerce action/review system.

Isolated app-host.liquid uses @app schema and render-block dispatch in a section-block loop, ordinary-flow wrapper, no limit, no vendor internals. Parse schema and assert dispatch. Independent tests/guests files contain plain labelled test-only content and native links, never baked reviews. Local renderer takes trusted guest files from harness registry, not arbitrary merchant HTML. Browser evidence proves geometry/order/removal/duplication; live Shopify/editor/app execution stays NOT TESTED. If “real compatible seam” requires deployment to a store, report that limitation instead of imitating it.

## 4. Desktop/mobile evidence

Capture full-page JPEGs with loaded images: branded-pdp1440/390, neutral-pdp1440/390, branded-editorial1440/390, neutral-editorial1440/390. Additional frames: jewelry1440/390, food1440/390, zero390, one390, dense1440, no-media390, portrait768, landscape1024, metric-no-source390, long-claim320, long-source320, long-quote390, translation320, rtl390, before-after1440/390, incomplete-pair390, comparison1440, incomplete-comparison390, reorder1440, repeated1280, dynamic390, disconnected-fallback390, disconnected-omit390, app-expected1440, app-awkward1440, app-tall320, app-wide320, app-removed1440, app-reordered390, one-process390, editorial-process1440/390. **43 review frames** plus keyboard-focus390, no-JS390, reduced-motion390 and reflow320 supplemental frames. Evidence manifest explicitly lists captures rather than relying on prose totals.

Each304 view records actual browser width, overflow, IDs, runtime scripts, evidence kind/order/count, text/media/card geometry, link targets, media loading, app local overflow and semantic source order. Evidence JSON must carry hashes of runtime/fixtures/media/probe and actual screenshot dimensions. Do not synthesize browser observations from static source.

## 5. Tests before completion

Static Python suite: required schema/content normalizers, optional/missing/disconnected data, URL structural validity/context escaping, alt/labels/caption/blockquote/table/ordered steps, all38 fixtures, max caps/control budget, reorder/repeated instance IDs, no runtime JS/remote dependency/fixture-specific CSS/duplicate responsive DOM, Liquid schema/dispatch, preservation hashes for all existing tracked files and refs. No factual validity checker.

Server suite: all38 fixtures, unknown/malformed query fallback, local product and editorial/source destination, independent guest route, safe file traversal rejection, headers, script-free literal baseline parity.

Browser suite: actual304 views × invariants, full43-frame manifest/dimensions/source fingerprints, keyboard Tab/Enter/skip link/source focus, source/destination URLs, app absent/inserted/removed/tall/wide/reordered/duplicate geometry and no local state leakage. JS-disabled and reduced-motion same content; enlarged text/reflow feasibility at320 (not manual browser zoom certification). No claim of VoiceOver/NVDA, physical touch or production accessibility certification.

Commands: `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/evidence-rail/tests/static.py`; corresponding `server.py` and `browser.py`; browser capture with bundled Node/Playwright path documented in README; `git diff --check`. Record actual assertion totals, not invented expected counts. Browser unavailability is an explicit incomplete/NARROW gate, not static PASS.

## 6. Complexity and red-team acceptance

Report physical/nonblank lines and bytes/gzip CSS/runtime/data/renderer/server/tests, responsive breakpoints, merchant decisions/content caps/shared fields, primitive/normalizer count, JS0, no state/lifecycle listeners, DOM duplication0, dependency0 at runtime, test-only tooling separately, image provenance and no new token system. Existing density/emphasis/mode only; no new rescue setting. One primitive may serve several evidence kinds, never collapse all into an interchangeable mega-section.

Pre-code consistency audit: fixtures cover every user matrix item; dynamic/app specimens do not certify live integrations; metric source optional; synthetic claims disclosed; process one-step remains ordered; every missing type has deterministic omission; all sources/qualification remain visible; zero evidence is valid; refs/preserved files fingerprinted before edits; app width containment allows access, not destructive clipping. No unresolved contract conflict. Engineering completion may be PASS only within executed isolated checks; real-platform compatibility remains NARROW/NOT TESTED.

## 7. Completion report and stop

README/findings report branch, exact commit/parent externally, clean/dirty, manifest, commands/counts, fixture×width counts, screenshot paths, app evidence, metrics, requirement audit, exceptions and all untested categories. Mandatory known gates: human visual review; genuine merchant evidence/provenance and permission; live Shopify Liquid/schema/app/dynamic-source/editor/main-product integration; product/cart/Markets/selling-plan semantics outside read-only host; merchant task usability; accessibility certification/AT/real zoom/full translation+RTL; cross-browser/hardware touch; measured LCP/CLS/INP/Lighthouse/low-end network/production responsive media; Theme Store originality and overall M1 closure/M2 gate.

Commit locally only after complete isolated evidence/tests. **Engineering verdict only. Visual verdict: PENDING HUMAN REVIEW.** No push/PR/merge/M2/further visual verdict. Stop for human review.
