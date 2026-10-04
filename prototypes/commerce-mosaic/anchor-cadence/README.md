# M1 Commerce Mosaic / Anchor Cadence

Engineering verdict: PASS for isolated prototype checks. Visual verdict: PENDING HUMAN REVIEW.

Controlling documents are `docs/m1-commerce-mosaic-prebuild-contract.md` (blob `9df10a77e00908b8dfdf52c0cae0bb4542602e39`) and `docs/m1-commerce-mosaic-implementation-brief.md` (blob `41493e5a3e671e865b92aa2a1a17220df46b13a9`) from `m0-live-market-evidence-2026-10-03`. No conflict was found. This is fixture-driven M1 evidence, not a production Shopify section.

Run from repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/commerce-mosaic/anchor-cadence/serve.py
```

Open `http://localhost:3002/`. Native GET controls expose fixture, sort and availability. Product and editorial destinations are read-only local navigation stubs. No checkout or add-to-cart is represented.

## Authored cadence

Six ordinary encounters establish scanning rhythm. On the first page with at least twelve products and automatic feature enabled, product seven receives a two-column, two-row feature on wide screens; products eight and nine occupy its adjacent lane. Optional editorial follows product nine only when at least three products remain. Product ten onward restores ordinary scanning. In two-column layouts the same feature and editorial span the full row at the same source positions. No source reordering, masonry, dense packing or viewport placement logic exists.

Small sets, disabled/missing feature, later pagination pages and Standard Grid use ordinary cards. Editorial absence removes the story without leaving an interior hole. A normal incomplete final catalog row is allowed. One planner takes only result count and bounded settings; one card renderer and one product truth function serve both treatments.

Five bounded merchant-like control groups: rhythm (Anchor Cadence/Standard Grid), automatic feature enabled/absent (missing source safely suppresses), optional editorial content, density (compact/balanced/spacious), preset tokens. Editorial content contains enabled/title/body/image/link label/link URL. Automatic feature position is authored and fixed; no arbitrary selected-position, row/column/span, device coordinates or raw CSS controls exist. Fixture/sort/filter/page selectors are test harness inputs, not placement controls. Media always uses contain.

## Fixtures and evidence

46 distinct product records and 43 collection/stress fixtures. Repeated density cases extend to 104 encounters; these are conceptual density cases, not 104 unique SKU records. Beauty/Wellness branded and ordinary non-beauty neutral controlling proofs share identical architecture. Neutral uses system sans, monochrome, ordinary media and generic copy. Localized description is exactly 50% longer than its baseline. No category-specific layout exists; Jewelry and Food fixtures change data/tokens only.

Review frames and provenance are in `tests/evidence/`. `frames.json` lists 36 full-page JPEGs; `focus-390.jpg` separately records native keyboard focus. `browser-matrix.json` records all 344 observed fixture/width views. `capture.json` fingerprints runtime sources, media and the read-only test probe. `media-loading.json` records complete loading before screenshots. `interactions.json` records native filter/sort, keyboard destination, pagination and skip-link checks. `asset-provenance.json` contains full prompts for three generated ordinary product photographs and the seven read-only media copies from Monument; no preserved composition or behavior was changed.

The browser probe under tests is never shipped or loaded by pages. It measures DOM geometry without placing or mutating elements. Browser evidence validation consumes actual observations; it does not regenerate browser measurements. For new implementation changes recapture the matrix before accepting its fingerprints.

See `findings.md` for the required completion report and `tests/evidence/changed-files.json` for the exact file manifest. Commit SHA is reported externally after commit to avoid self-referential commit content.
