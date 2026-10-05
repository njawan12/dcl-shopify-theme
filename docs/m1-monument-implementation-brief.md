# M1 Monument — isolated prototype implementation brief

**Date:** 2026-10-04  
**Status:** APPROVED FOR ONE ISOLATED PROTOTYPE after reading the controlling red-team contract.  
**Direction:** Concept 06 — One Line, One Object.

## 1. Objective

Build the smallest serious prototype that can answer whether Monument's structural identity survives branded and neutral conditions, ordinary media, responsive transformation and predictable merchant/data abuse.

Do not build production Shopify code.

## 2. Controlling documents

Read before implementation:
1. `docs/m1-living-canvas-prebuild-red-team-matrix.md`
2. `docs/m1-signature-system.md`
3. `docs/m1-product-architecture-contract.md`
4. `docs/engineering-compliance-standard.md`
5. `docs/m1-monument-prebuild-red-team-contract.md`
6. existing Split Tension findings only as process precedent, not as visual architecture to copy.

If these conflict, stop and report the conflict before coding.

## 3. Scope

All prototype files must live under:

`prototypes/living-canvas/monument/`

No production theme directories. No M2. No PR. No merge. Do not modify another Living Canvas prototype.

## 4. Architecture

Use one shared semantic component/rendering path for branded, neutral and stress fixtures.

Required conceptual regions:
- editorial statement;
- dominant product/media object;
- continuous axis/datum;
- restrained commerce information/action.

Do not create a conventional product-card wrapper as the central visual primitive.

The product/media must cross, interrupt, mask or reshape the axis/editorial boundary through CSS-owned deterministic geometry.

No fixture-specific DOM architecture.

## 5. Controls/data model for prototype

Model only semantic inputs that could plausibly become merchant inputs:
- product reference/data fixture;
- headline;
- optional eyebrow;
- optional support copy;
- optional editorial link;
- bounded visual token/preset inputs only if genuinely necessary.

Do not model:
- x/y;
- offsets;
- raw widths/heights;
- z-index;
- per-device positions;
- arbitrary overlap;
- separate mobile content;
- raw CSS.

## 6. Commerce rule

This experiment is primarily visual/static. Prefer server-rendered truthful fixture states.

Do not implement quick add, variant selector, selling-plan selector, bundle behavior, cart mutation or other commerce JS merely to make the prototype feel complete.

For unresolved/complex/app-owned states, render a safe product-link action.

## 7. Required fixtures

At minimum:
- branded/default;
- neutral torture;
- short headline;
- long headline + 50% expansion;
- single available product;
- multi-option unresolved;
- sold out;
- valid compare-at;
- unit price;
- missing product;
- missing media;
- transparent packshot;
- white-background rectangular image;
- dark rectangular image;
- portrait image;
- square image;
- landscape image;
- awkward focal edge;
- long product title;
- long CTA;
- adjacent two-instance page.

Reuse one engine/component. Do not write mini-apps per fixture.

## 8. Required responsive evidence

Generate at least:
- branded 1440;
- neutral 1440;
- branded 390;
- neutral 390;
- ordinary rectangular media 1440 + 390;
- long/localized copy 1440 + 390;
- missing media;
- missing product;
- sold out;
- adjacent instances;
- representative 320 and 768 stress frames.

Audit widths:
320, 375, 390, 430, 768, 1024, 1280, 1440.

## 9. Visual floor

This cannot be a wireframe.

The branded frame must be polished enough to judge Theme Store screenshot potential:
- deliberate type hierarchy;
- premium spacing;
- dominant product moment;
- clear axis;
- controlled negative space;
- restrained commerce;
- intentional desktop and mobile compositions.

But do not use beautiful media to conceal weak structure. The neutral frame is equally controlling.

## 10. Neutral fixture

Use:
- system sans;
- monochrome;
- non-beauty generic product;
- ordinary rectangular catalog media;
- generic truthful copy;
- no motion;
- no decorative handwritten styling.

Same markup, same component, same geometry rules as branded.

## 11. Forbidden shortcuts

Do not:
- hardcode fixture names into CSS;
- use nth-child to fake authored object placement;
- use JS geometry/measurement;
- duplicate desktop/mobile DOM;
- require transparent PNG;
- hide failures with overflow clipping;
- use fixed heights for text regions;
- add arbitrary media queries solely for one screenshot;
- use absolute positioning without a bounded structural containing block and collision-safe responsive rule;
- add fake reviews/scarcity/badges;
- create custom product data inconsistent with fixture truth;
- silently alter the red-team contract.

## 12. Tests

Add static/regression tests proving:
- files remain in isolated scope;
- no forbidden controls;
- no positional JS;
- no duplicated desktop/mobile semantic tree;
- no duplicate IDs across two instances;
- no horizontal overflow across required widths;
- every required fixture renders;
- missing data states do not leave broken UI;
- long content is not clipped;
- target/focus baseline for interactive elements;
- neutral and branded use the same component path.

Tests must assert system behavior, not merely fixture filenames.

## 13. Complexity report

Report:
- CSS physical/nonblank lines;
- JS physical/nonblank lines;
- number of component/rendering paths;
- number of responsive breakpoints introduced;
- number of merchant-like controls modeled;
- any absolute positioning and why it is structurally bounded;
- any JS and why it is necessary.

Unexpected complexity is a reason to NARROW, not hide.

## 14. Required completion report

When finished, provide:
1. exact local commit SHA and parent SHA;
2. changed-file list and confirmation all are under Monument prototype path;
3. test commands and exact pass/fail counts;
4. fixture/width audit results;
5. complexity report;
6. four controlling frame paths;
7. stress-frame paths;
8. known untested items;
9. engineering verdict only: PASS / NARROW / FAIL;
10. visual verdict: **PENDING HUMAN REVIEW**.

## 15. Stop condition

Commit locally and stop.

Do not push unless explicitly instructed.
Do not create a PR.
Do not merge.
Do not start M2.
Do not modify Split Tension, Edge Crop or Quiet Frame.
Do not declare visual PASS.
