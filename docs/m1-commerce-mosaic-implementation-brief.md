# M1 Commerce Mosaic — isolated prototype implementation brief

**Status:** implementation brief for M1 evidence only.  
**Controlling contract:** `docs/m1-commerce-mosaic-prebuild-contract.md`.  
**Production authorization:** none.

## Objective

Build one isolated prototype that answers one question:

> Can Anchor Cadence create a structurally recognizable premium collection merchandising rhythm while preserving fast product scanning, truthful Shopify-like product semantics, bounded merchant controls, deterministic responsive behavior and ordinary catalog resilience?

Do not build a production Shopify section. Do not start M2. Do not generalize into a page builder.

## 1. Scope boundary

All new prototype implementation/evidence files must live under:

`prototypes/commerce-mosaic/anchor-cadence/`

Do not alter Split Tension, Monument, Edge Crop, M2 foundation work or unrelated prototypes.

Use the pre-build contract as the source of truth. If this brief conflicts with it, stop and report the conflict rather than silently choosing.

## 2. Required architecture

Use one shared semantic product data path and one shared product-card renderer for ordinary and feature products. Feature treatment may change composition/classes, but it must not fork commerce truth.

Required conceptual pieces:
- collection/result sequence;
- deterministic cadence planner;
- shared product-card renderer;
- optional editorial tile renderer;
- Anchor Cadence layout;
- Standard Grid fallback;
- fixture/data layer;
- static/browser test harness;
- evidence capture.

The cadence planner must be deterministic from result count + bounded configuration. It must not inspect fixture names, product IDs or image aesthetics.

No runtime browser JS may be used for layout placement or measurement. Prefer zero browser JS unless a test/evidence need is clearly separated from runtime output.

## 3. Anchor Cadence implementation hypothesis

Implement one serious authored rhythm, not multiple decorative variants.

Wide-layout starting structure:
1. ordinary products establish baseline scan rhythm;
2. after sufficient product density, one product receives the bounded feature treatment;
3. one optional editorial tile interrupts at a later deterministic point only when enough products remain;
4. ordinary product rhythm resumes clearly after interruption.

The exact grid math is yours to implement, but it must satisfy the controlling contract and must not need arbitrary per-index exceptions.

When result count is too small, progressively remove editorial interruption and/or feature treatment. Never leave holes.

Standard Grid uses the same products and same card truth without Anchor Cadence spans/interruption.

## 4. Fixtures

Create a realistic fixture set large enough to expose collection behavior. Minimum 24 distinct product fixtures plus generated/repeated catalog-density cases where useful.

Must include:
- Beauty/Wellness branded set for controlling branded evidence;
- neutral ordinary non-beauty set for originality torture;
- portrait/square/landscape/transparent/white-background/missing media;
- short and very long titles;
- regular, sale/compare-at, unit-price and sold-out states;
- single/multi-variant representation;
- complex/selling-plan/app-owned marker states that do not receive invented quick-add logic;
- badge absent/present with factual fixture data only.

Also fixture collection/result counts: 0, 1, 2, 3, 5, 12, 24 and conceptual 30–100+ density.

Include editorial tile states: complete, no image, no link, long heading, absent.

Do not fabricate reviews, viewer counts, low-stock messages, urgency or discount logic.

## 5. Responsive evidence

Render and test at:
`320, 375, 390, 430, 768, 1024, 1280, 1440`.

The same semantic content/source order must serve every width.

At 390, capture branded and neutral controlling frames. At 1440, capture branded and neutral controlling frames.

Also capture representative stress evidence for mixed media, long copy/status density, editorial absent and small result sets.

## 6. Required assertions

Automate as much as reasonably possible. Tests must at least assert:
- rendered product count equals truthful fixture/result count;
- source/DOM product order equals input collection order;
- feature treatment does not duplicate or omit its product;
- editorial tile is not counted/marked as a product;
- no duplicate IDs;
- no horizontal page overflow at target widths;
- no unexplained empty grid cells caused by planner logic where measurable;
- missing media/state renders safely;
- sale/compare-at/unit/sold-out truth is preserved between Standard Grid and Anchor Cadence;
- feature product destination/price/state matches its ordinary-card truth;
- small result sets degrade deterministically;
- editorial absence degrades deterministically;
- repeated component instances do not collide in IDs/state/classes;
- planner output is deterministic for identical inputs;
- no fixture-specific product-ID/name placement logic exists;
- runtime output has no JS layout engine/dependency.

If browser geometry tooling is available, assert no card/media/text collisions for the fixture/width matrix. If unavailable, report that limitation explicitly; do not fake evidence.

## 7. Visual floor

Branded Beauty/Wellness proof should feel premium and commerce-first, but the architecture cannot rely on campaign-grade photography.

Neutral proof must intentionally remove the crutches:
- system sans;
- accessible monochrome;
- no nonessential animation;
- ordinary non-beauty products;
- mixed catalog imagery;
- generic truthful copy.

The primary human question is whether the neutral frame still looks like an authored merchandising system rather than a conventional grid with a promo card.

Do not spend implementation complexity on ornamental effects before the structural rhythm is visible.

## 8. Accessibility/static semantics

Prototype markup should model production intent:
- logical heading structure;
- semantic product-list/list-item relationship where appropriate;
- clear product links;
- no nested interactive controls;
- visible focus treatment;
- status/badge meaning not dependent on color;
- editorial tile semantically distinct from product items while remaining in logical reading flow;
- meaningful/empty alt behavior based on fixture intent.

Record manual gaps such as VoiceOver/NVDA, zoom, RTL and real Shopify semantics as untested unless actually tested.

## 9. Complexity ceiling

This is a proof of architecture, not a framework.

Report:
- CSS physical/nonblank lines and bytes;
- browser runtime JS lines/bytes;
- renderer/planner/test harness lines;
- breakpoint count;
- merchant-like control count;
- dependencies;
- DOM duplication;
- number of separate product-card truth paths.

Red flags to stop and report:
- layout JS;
- more than one product truth renderer;
- fixture-specific CSS selectors;
- product-ID/index exception pileups;
- duplicated desktop/mobile markup;
- arbitrary placement controls;
- dependency added only to make mosaic geometry work.

## 10. Completion report

On completion provide:
1. exact local branch;
2. exact commit SHA + parent;
3. clean/dirty status;
4. changed-file manifest;
5. test commands and exact pass/fail counts;
6. fixture × width evidence count;
7. controlling screenshot/evidence paths;
8. complexity report;
9. contract exceptions, if any;
10. known untested areas;
11. engineering verdict only: PASS / NARROW / FAIL;
12. **Visual verdict must remain PENDING HUMAN REVIEW.**

## 11. Git/process instruction

Create a dedicated local branch named:
`m1-commerce-mosaic-anchor-cadence`

Base it on the current preserved M1 lineage available in the working repository without modifying preserved prototype branches. If ancestry is ambiguous, stop and report before coding.

Commit the isolated prototype locally when tests/evidence are complete.

**Do not push. Do not create a PR. Do not merge. Do not start M2. Stop for human review.**