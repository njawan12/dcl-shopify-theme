# M1 Evidence Layer completion report

**Final M1 human visual verdict: PASS TO PRESERVE.**

Human review accepts:

- the subject → attached evidence → qualification/source relationship as recognizable signature language;
- survival of the neutral originality torture test;
- coherent desktop-to-mobile transformation;
- distinct semantic roles for Evidence Note, Evidence Pair and Process Sequence;
- preservation of commerce/content hierarchy;
- the bounded merchant-control model.

Wide-screen attachment spacing may receive production visual polish, but this does not authorize further M1 visual iteration.

Untested production gates remain unchanged: real Shopify/dynamic-source/app/editor integration, genuine merchant evidence/provenance, accessibility certification including zoom/RTL, cross-browser/touch validation and measured performance.

Automated checks below remain engineering observations; the final verdict above was supplied by human review. The implementation record describes commit `d2e7ac6375840034fff40119002b2a43ee581b76`. The subsequent documentation-only verdict commit has that exact parent, changes README/findings only and is published to `m1-evidence-layer-prototype`; its exact SHA is reported in delivery.

## Branch, ancestry and preservation

Branch `m1-evidence-layer-prototype`, based exactly on approved contract commit `c92fc598a9016d75479b811b59c8fcd9275a1ea3`. Local implementation commit SHA is reported externally after commit; its parent is the exact approved commit. Final clean working-tree status is verified in delivery. Every addition is under `prototypes/evidence-layer/attached-proof/`; exact manifest is `tests/evidence/changed-files.json`. No controlling docs/production/preserved prototype paths changed. Preserved branch hashes are recorded and checked in `tests/evidence/preservation.json`. No push, PR, merge, M2 or production integration.

`implementation-brief.md` preceded coding. It defines the32 fixtures, three primitive boundaries, host attachments, omissions/source/app states, matrix, semantics/budgets and stop conditions. No contract mismatch, added variant/control/primitive or rescue setting was required. The35th screenshot explicitly records one-valid-step390, closing the brief's35-frame total without introducing another fixture or design treatment.

## Architecture and primitive coverage

Evidence note: one normalizer/renderer for metrics, facts/specifications, claims, certification and quote. Same fields and presentation attach to PDP media and editorial context. Evidence pair: one normalizer/renderer with two approved semantic modes, comparison and before/after, in PDP education. Process sequence: one normalizer/renderer in PDP education and editorial; one step remains an ordered one-item ol. Three narrow pieces, not a universal switchable section. One source-binding adapter resolves manual/connected/disconnected content for all primitives; one structural URL checker. No credibility/factual claim checker.

PDP source order: subject → notes → separate read-only commerce context → pair → process → optional app guest. Editorial source order: statement/media → notes OR process → editorial action. Desktop uses adjacent edges and rails; mobile resolves in normal flow with the same source. All qualification/source text remains readable. App guest is an ordinary-flow stand-in, never a real review service. Its insertion/tall/removal/duplication tests do not prove Shopify @app or editor lifecycle.

## Tests and evidence

Commands from repository root:

- `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/attached-proof/tests/static.py`: 1816 PASS /0 FAIL.
- `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/attached-proof/tests/server_responses.py`: 112 PASS /0 FAIL.
- `PYTHONDONTWRITEBYTECODE=1 python3 prototypes/evidence-layer/attached-proof/tests/browser_evidence.py`: 9676 PASS /0 FAIL.
- `git diff --cached --check`: completed at staging in delivery.

Complete matrix:32 fixtures ×320/375/390/430/768/1024/1280/1440 =256 native-browser views, height1000. All observed views have zero horizontal overflow, duplicateIDs, runtime scripts, detected sibling card/text/media collisions, overflowing measured text, undersized tested targets or eagerly unloaded subject media. Browser assertions validate primitive kind/content/order, row/pair/step/app counts, ol numbering and actual host order against fixture contracts. They verify fingerprints rather than synthesizing measurements.

35 full-page review JPEGs +1 keyboard-focus JPEG. All screenshot images were loaded through native browsing/scroll before capture. JSON observations and source hashes are included. Native keyboard source focus had a3px outline; Enter moved focus to the scoped subject target; product link navigated to the truthful local stub; native form visited present/tall/removed app states and one-step process; skip link focused main. No actual source network/credibility test was performed or implied.

Controlling frames, relative to this prototype:

- `tests/evidence/branded-pdp-1440.jpg`
- `tests/evidence/neutral-pdp-1440.jpg`
- `tests/evidence/branded-pdp-390.jpg`
- `tests/evidence/neutral-pdp-390.jpg`
- `tests/evidence/branded-editorial-1440.jpg`
- `tests/evidence/neutral-editorial-1440.jpg`
- `tests/evidence/branded-editorial-390.jpg`
- `tests/evidence/neutral-editorial-390.jpg`

Full list: `frames.json`. Stress frames include Jewelry/Food1440/390, editorial-process1440/390, before-after1440/390, short390, long1440/320, maximum1440, zero-evidence390, missing-media390, incomplete-before-after390, disconnected-fallback/omit390, app-present/removed1440, app-tall320, two-instances1024, localization320, one-valid-step390 and neutral375/430/768/1280.

A final content audit corrected non-beauty comparison/instruction labels so case/ring/jar fixtures describe their own subject rather than carrying Beauty labels. Before/after's subject is the same explicitly schematic container depicted by its pair. All40 affected fixture-width observations and14 frames were recaptured. No renderers, geometry, controls or primitives were changed to solve those content issues. Short/maximum fixtures additionally exercise the existing compact/spacious/strong choices; their16 views and2 frames were refreshed. Semantic emphasis strengthens the existing rule weight across presets without adding a setting or composition.

## Complexity/control audit

| Piece | Physical / nonblank lines | Bytes |
|---|---:|---:|
| evidence.css | 11 / 11 | 6,425 |
| render.py | 91 / 80 | 8,148 |
| content.py | 90 / 77 | 4,594 |
| fixture_catalog.py | 72 / 67 | 12,446 |
| serve.py | 22 / 22 | 1,800 |
| tests/browser_evidence.py | 67 / 62 | 4,921 |
| tests/server_responses.py | 24 / 23 | 1,503 |
| tests/static.py | 117 / 113 | 9,649 |
| tests/capture-probe.js | 13 / 13 | 2,628 |

Exact physical/nonblank lines and byte counts are recorded in `tests/evidence/complexity.json`. CSS uses compact rule formatting; physical line counts are reported alongside full byte size rather than treated as the complexity claim. Runtime browser JS:0 lines/0 bytes. Two responsive breakpoints768/1024. Three primitive renderers and three normalizers, one source-binding adapter and one URL structural checker, zero factual/credibility checkers. Two fixed fixture host contexts; no host choice is exposed as a new merchant variant. Python standard library and native browser tooling; zero added dependencies, duplicate responsive DOM or vendor-specific selectors. Test probe JS is separately reported and never shipped as runtime.

Contract decisions: notes2(density/emphasis); pair3(mode/density/emphasis); process2(density/emphasis); guest0. Conditional decisions0 each. Notes8 content fields, pair child4 and process child5. Caps3notes,1pair/4rows,4steps,1guest/seam. Fixture selector/source binding/app stand-in are test instrumentation, not additional placement settings. Global typography/color/media roles reuse the accepted M1 vocabulary. No separate global token system or business logic is introduced.

## Exceptions and production gates

No approved contract scope exception. Root-relative URL support is confined to the two local fixture destinations; production URL contexts remain an integration task. Before/after proof is synthetic schematic content clearly identified as such, not a genuine customer/product outcome; real merchant media/provenance remains untested. The fixture adapter demonstrates content contract resolution, not live Shopify dynamic-source connections. Static editorial quotes/certification records are explicitly synthetic examples, never real reviews or endorsed claims.

Untested production gates: production visual polish; real Shopify sections/blocks/schema, PDP commerce/Markets, dynamic-source compatibility and editor lifecycle; real app insertion/removal/vendor interoperability and source media/provenance; VoiceOver/NVDA, manual200%/400% zoom/text enlargement/high contrast, complete localization/RTL, physical touch and cross-browser/device coverage; measured LCP/CLS/INP/Lighthouse/network budgets and production responsive image pipeline. The M1 before/after proof does not verify real result evidence or truth. Source links do not establish or certify credibility. No accessibility/performance certification is claimed.

Final M1 human verdict: **PASS TO PRESERVE**. Preserve the accepted prototype and original M1 systems. The documentation-only verdict commit is authorized for publication to `m1-evidence-layer-prototype`. No further M1 visual iteration, PR, merge or M2. Stop after remote SHA verification.
