# M1 Evidence Layer implementation brief

Authority: exact parent `c92fc598a9016d75479b811b59c8fcd9275a1ea3`, `docs/m1-evidence-layer-prebuild-contract.md` and its four inherited M1 contracts. This brief closes implementation detail only. The user's current instruction authorizes the isolated prototype; no production authorization follows from it.

## Scope and preservation

Local branch `m1-evidence-layer-prototype`, based exactly on the approved commit. All additions, including this brief, implementation, tests, README/findings and evidence, live under `prototypes/evidence-layer/attached-proof/`. No controlling documentation, production files, preserved prototype paths or branches change. No push, PR, merge or M2. Existing media may be copied read-only from pinned preserved commits with provenance recorded. No new design system, variants, controls, primitive or Shopify integration.

## Primitive and host coverage

Three narrow renderers, one presentation each: Evidence note (metric/fact/claim/certification/quote), Evidence pair (before/after or comparison semantic modes), Process sequence. One normalized content path per primitive shared between hosts. Minimal read-only PDP context supplies subject media and separately legible title/price/status/product link, followed by separate pair and process education sections. This is not a purchase-area prototype or simulated add-to-cart. Editorial context supplies statement/media, either one note group OR one process sequence, then editorial action. PDP media has one note group (max3). No compound mega-section or selectable host layouts; hosts are fixture contexts, not new merchant controls.

Notes: kind/value/label/body/attribution/source_title/source_url/qualification (8 fields). Pair common heading/introduction/qualification/source_title/source_url; two before/after items label/media/alt/caption; or two named comparison subjects and up to4 criterion/left/right/qualification rows. Process common heading/introduction/source_title/source_url with up to4 heading/instruction/media/alt/qualification steps. One valid process step remains an ordered one-step process. Application/source bindings are test adapters around these contracts, not extra merchant fields.

## Exact fixtures (32)

All content is clearly marked synthetic test content, never observed clinical/customer/certification results. Ordinary product photographs are independently rendered media, not baked proof UI. Before/after uses explicitly identified schematic storage states of the same object, not product efficacy or photographic result evidence. No real certification, customer identity, ratings or review counts are invented.

1 branded-pdp: Beauty media notes metric/fact/claim; comparison and four-step usage.
2 neutral-pdp: system sans monochrome ordinary utility product; same primitive structure.
3 branded-editorial: editorial statement/media + notes + action.
4 neutral-editorial: ordinary non-beauty same note attachment.
5 jewelry-pdp: material/dimension/provenance and care; exact shared architecture.
6 food-pdp: ingredients/serving and process; exact shared architecture.
7 editorial-process: statement/media + process + action, no notes.
8 before-after: labelled storage diagrams, explanatory alt/captions, qualification/source.
9 short: compact density, minimal note, short pair labels, exactly one ordered process step.
10 long: long heading/body/value/qualification/attribution/source/link labels and step/comparison copy.
11 maximum: spacious density/strong semantic emphasis, three notes, four comparison rows, four steps.
12 zero-evidence: zero notes/no pair/no process; host remains complete.
13 invalid-notes: incomplete metric/fact/claim/certification/quote omitted; one valid note remains.
14 optional-empty: empty optional note fields/source/media omitted, valid text remains.
15 missing-media: invalid subject/step media omitted or honest subject text fallback; proof text remains.
16 incomplete-before-after: one missing labelled media item; entire pair omitted.
17 invalid-comparison: unnamed subject; pair omitted.
18 partial-comparison: incomplete rows removed; complete rows remain.
19 no-comparison-rows: all rows incomplete; pair omitted.
20 partial-process: invalid steps removed; remaining sequence numbered consecutively.
21 one-valid-step: several invalid steps plus one valid; one-item ol retained.
22 invalid-process: all steps invalid; process omitted.
23 disconnected-fallback: connected notes disconnected; explicit valid manual fallback rendered.
24 disconnected-omit: disconnected notes without fallback; stale connected data not rendered.
25 connected-source: compatible fixture source supplies same note fields, same presentation.
26 url-valid: HTTP(S), supported root-relative and scoped same-document source links.
27 url-invalid: malformed/empty/unsupported-scheme/unresolved-fragment links suppressed; source text remains.
28 app-present: one plain synthetic guest block near PDP education; no ratings.
29 app-tall: same guest with long content; no vendor-internal styling.
30 app-removed: exact app-present data without guest; no placeholder scar.
31 two-instances: two independently scoped PDP contexts including guest, fragments and all primitive IDs.
32 localization: exact50% introduction expansion, CJK/bidirectional text and long unbroken labels; no architecture change.

Renderer-level adversarial tests supplement the32 captured fixtures: every note kind's valid/invalid minimum, unknown kind, all URL structural categories/escaping, caps on excess input, deleted/malformed sources, disconnected pair/process with/without manual fallback, each media/row/step invalidity, and content escaping. No factual validity/credibility assessment is implemented or implied.

## Source and URL handling

Manual content complete without source/app. Test binding adapter chooses current connected content, explicit manual fallback after disconnection, otherwise omission; never cached stale values. Same validator/renderer follows resolution. Structural URL validation permits well-formed HTTP(S), confined supported root-relative local destinations and fragment targets actually rendered in that instance. Invalid scheme/host/port/encoding/control characters or missing fragment target suppress only links, retaining valid source title. Never fetch/grade source URLs, guarantee destination availability or judge claim truth. Scoped fragment resolution prevents cross-instance target collision. Optional media accepts existing confined fixture assets and intrinsic dimensions; before/after missing media invalidates its pair.

## Order, apps and accessibility

One semantic DOM. PDP subject media → notes/source, with commerce adjacent in separate native context; education pair then process follow. Editorial statement/media → notes OR process → action. Pair heading/context → before → after OR named subjects/each criterion and both values → qualification/source. Process heading/context → ol steps → source. Media precedes related text within items. Qualifications are normal readable text, not concealed. No slider, disclosure, required hover/motion, sticky region, duplicate responsive DOM or runtime JS. Comparison uses named definition-list values so mobile retains both values per criterion. Quote uses blockquote + attributed citation; labels are explicit; native links have focus and44px targets. CSS logical properties and wrapping; no content fixed heights/clip. Manual AT/zoom/browser/performance certification remains untested.

Guest block is a single ordinary-flow aside outside evidence labels/media/form; no vendor internals inspected or styled. Capture present/tall/removed; compare removal render to no-app baseline. Two instances model duplication independently. Real @app support/editor lifecycle deferred, not simulated as completed.

## Evidence matrix and checks

All32 fixtures × widths320/375/390/430/768/1024/1280/1440 =256 observed browser views, height1000. Read-only native browser geometry probe records overflow, duplicateIDs, runtime scripts, host/primitive order, note/row/step/pair/app counts, ol semantics, target sizes and card/text/media collisions. Full-page screenshots load lazy images before capture. Controlling frames: branded-pdp/neutral-pdp/branded-editorial/neutral-editorial at1440 and390 (8). Additional frames: jewelry-pdp/food-pdp at1440/390; editorial-process1440/390; before-after1440/390; short390; long1440/320; maximum1440; zero-evidence390; missing-media390; incomplete-before-after390; disconnected-fallback/omit390; app-present1440; app-tall320; app-removed1440; two-instances1024; localization320; one-valid-step390; neutral-pdp375/430/768/1280. Total35 review screenshots plus one native focus screenshot. JSON manifests/fingerprints bind actual measurements to current implementation/media/probe. Native GET fixture form, source-fragment focus and product/editorial stub navigation checked; no real commerce/network source validation.

Static assertions: schema/minima/omissions/source normalization/caps/order/IDs, image alt, one-step ol, quote/comparison semantics, escaped text/URLs, no fake stars/counts, no scripts/vendor-specific CSS/fixture selectors, app removal and multi-instance isolation, literal default HTML parity and allowed Git scope. Live server tests: all fixtures/assets, navigation stubs, structural URL handling, denied source/path traversal routes. Browser evidence assertions: exact fixture/width coverage, geometry/order/counts and realJPEG dimensions/loading. Any named failure fixed within approved structure or stop/report; no rescue variants/settings.

## Complexity and control report

Record physical/nonblank/bytes CSS, browser runtimeJS, renderers/source adapter, fixture authoring, server, tests and read-only probe. Count breakpoints/dependencies/DOM duplication/primitive paths. Notes2 decisions(density/emphasis), pair3(mode/density/emphasis), process2(density/emphasis),0 conditional each, guest0; notes8 content fields, pair/step child<=8. Existing semantic density/scheme tokens own styling; no additional global merchant controls. Normal cap3notes,1pair/4rows,4steps,1guest/seam. Report app/source fixture instrumentation separately, never hide it as merchant settings. Full changed-file manifest and preservation parent/ref audit.

## Stop and completion

Local commit only on isolated branch. Report exact SHA/parent, changed files, commands/pass-fail totals, fixture/viewport/evidence totals, complexity/control counts, known production gates and clean/dirty status. Human-owned verdict is **PENDING HUMAN REVIEW**. Do not award PASS/NARROW/FAIL. Do not push, PR, merge or beginM2. Production gates remain Shopify integration/real source and app/editor lifecycle, visual polish, accessibility certification, cross-browser/touch and measured performance. This brief has no unresolved mismatch with the approved contract; implementation may proceed under the user's current authorization.
