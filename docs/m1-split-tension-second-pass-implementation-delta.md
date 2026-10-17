# M1 Split Tension — Second-Pass Implementation Delta

**Date:** 2026-10-04  
**Status:** APPROVED TO IMPLEMENT as an isolated M1 visual recomposition only.  
**Authority:** This delta supplements, and does not replace, `m1-split-tension-implementation-brief.md`, `m1-split-tension-commerce-state-machine.md`, `m1-split-tension-visual-direction.md`, the Living Canvas red-team matrix, product architecture contract, and engineering compliance standard. Commerce/state contracts win over visual mockup details.

## 1. Purpose

Recompose the already-proven Split Tension prototype to match the approved four-frame visual direction **without rewriting the proven commerce state engine**.

This pass answers:
1. Can the approved Editorial Breakthrough / Bold Image Integration direction be expressed by robust CSS/semantic markup?
2. Does the same implementation remain recognizable in branded and neutral states?
3. Can mobile preserve the trajectory without copying desktop overlap?
4. Can the visual improvement be achieved without adding merchant rescue controls or weakening the state-machine contract?

This remains prototype code. No production theme implementation and no M2.

## 2. Starting point

Implementation branch must start from the exact validated prototype commit:

`e4b7c4aec751a3198277116f0b527a92e62323dd`

Remote branch containing that commit:

`m1-split-tension-prototype`

The visual contract is on the M0/M1 evidence branch at commit:

`545a1c0f3e5f9ab1ceb0e91f6d9198e0d244d1ff`

Codex must read that visual contract before editing.

## 3. Hard scope

Modify files only under:

`prototypes/living-canvas/split-tension/`

Do not touch production theme directories, M2, other Living Canvas variants, or controlling docs during implementation.

Do not create a new commerce engine. Preserve the existing state model, fixture semantics, money rules, request simulation, lifecycle/race protections, progressive enhancement, and 24-fixture coverage unless a visual requirement exposes a documented conflict.

No framework, package, build system, remote font, third-party UI library, network dependency, carousel, or JS layout measurement.

## 4. Visual target

Implement the relationships proven by the four-frame visual proof, not a pixel copy.

The desktop signature is:

> **A dominant editorial/media field whose boundary is crossed and reshaped by a numbered Guided Set trajectory, product media and commerce controls, ending in an aggregate action that belongs to the same composition.**

It must not regress to:

> **editorial rectangle | bordered product-card stack**

### Desktop >=1280

Required:
- editorial/media field carries primary emotional impact;
- headline composes with media;
- 2–5 numbered steps form a visible trajectory along/across the boundary;
- product media is materially larger and may bridge the boundary where robust;
- commerce information uses open/lightly surfaced zones rather than large dead white cards;
- at least one structural relationship crosses the editorial/commerce boundary;
- summary/action visually closes the trajectory and feels attached to the composition;
- ordinary packshots remain intentional;
- no absolute merchant-authored coordinates.

The exact branded mockup is inspiration; do not encode its beauty photography into layout assumptions.

### Tablet 768–1024

Relax boundary crossing before content collisions. Preserve hierarchy and trajectory. Do not force desktop overlap.

### Mobile 320–430

Transform intentionally:
1. editorial/media opening;
2. ordered numbered Guided Set sequence;
3. integrated aggregate action.

Do not shrink desktop. Do not require a carousel. Preserve semantic DOM order and all commerce truth.

## 5. Branded and neutral modes

The **same markup/state engine/layout system** must produce both.

Branded proof:
- premium Beauty + Wellness content/media;
- expressive but locally available/system-safe typography treatment;
- rich but accessible art direction.

Neutral proof:
- black/white/gray accessible palette;
- system sans;
- generic non-beauty language;
- ordinary packshots/still life;
- no decorative motion.

No separate neutral component, alternate DOM architecture, fixture-specific layout fork, or special coordinates.

Neutral passes only if Split Tension remains recognizable through boundary, trajectory, media/step relationship and aggregate action.

## 6. Commerce UI constraints

Preserve:
- explicit shopper inclusion;
- no default consent;
- quantity exactly 1;
- truthful variants/availability/pricing;
- link-only degradation for unsafe products;
- safe product links;
- aggregate selected-items total only;
- simulated request boundary.

The concept artwork showed quantity steppers. **Do not implement them.** They conflict with the controlling M1 quantity contract.

Controls may be visually refined but must remain native/semantic. Do not invent non-native checkboxes/selects merely to imitate the mockup.

## 7. Media robustness

Test the visual system with:
- cinematic lifestyle editorial media;
- ordinary white-background packshots;
- transparent product media;
- portrait/landscape editorial crops;
- missing optional media;
- inconsistent product aspect ratios.

Use local prototype assets only.

Do not bake typography, step labels, badges or product truth into images.

No design requirement may assume every merchant has bespoke campaign photography.

## 8. Content robustness

Must survive:
- 2 steps;
- 5 steps;
- long heading;
- 30–50% text expansion;
- long product title;
- missing/deleted product;
- sold out;
- unresolved options;
- mixed link-only/inline eligibility;
- zero aggregate-eligible;
- one surviving valid step.

No clipped essential content, collision, unreadable overlays, or empty card scars.

## 9. Interaction/accessibility preservation

The visual pass must not regress:
- native control semantics;
- logical DOM/tab order;
- visible focus;
- 44 CSS px primary target;
- labels/names;
- scoped status/error messaging;
- predictable focus;
- no hover-only information;
- no focus trap;
- reduced-motion safety;
- useful server-rendered/no-JS fallback;
- instance isolation;
- stale-response protection.

If the visual target requires breaking any of these, STOP and report rather than workaround.

## 10. CSS/complexity budget

The signature should be CSS-owned.

Allowed:
- Grid/Flex;
- pseudo-elements for decorative trajectory/boundary;
- bounded transforms/overlap;
- object-fit/object-position using semantic preset behavior;
- CSS custom properties/tokens.

Avoid:
- JS geometry measurement;
- per-fixture positional rules;
- nth-child coordinates that only work for three steps;
- hardcoded pixel placement tied to current fixture artwork;
- duplicate desktop/mobile semantic DOM;
- deep wrapper proliferation solely for decoration.

Report new CSS/JS line deltas and any new runtime state/event/control complexity.

A visual recomposition should not materially increase commerce JS complexity.

## 11. Required evidence after implementation

Capture and report at minimum:

### Four controlling frames
- 1440 branded;
- 1440 neutral;
- 390 branded;
- 390 neutral.

### Stress evidence
- 1440 five-step;
- 390 five-step;
- 320 long/localized;
- 1024 mixed eligibility;
- missing product;
- sold-out/unresolved state;
- two instances;
- no-JS/server-rendered fallback.

Run all existing state/static tests unchanged where possible. Any test modification requires explanation.

Repeat:
- JS syntax checks;
- full state assertions;
- full static assertions;
- all seven required widths;
- pending fixture switch/race test;
- diff/scope checks.

Do not claim VoiceOver/NVDA/physical touch/real Shopify/performance PASS unless actually evidenced.

## 12. Visual acceptance test

Codex may report engineering evidence but **may not grant visual PASS**.

Human product-owner review must decide:

1. Does the first 1440 branded frame stop attention?
2. Does commerce feel part of the editorial composition?
3. Is the signature still obvious in 1440 neutral?
4. Does 390 mobile feel intentionally designed rather than stacked desktop?
5. Do ordinary packshots still look premium enough?
6. Does five-step density remain composed?
7. Is the aggregate action integrated without becoming sticky clutter?
8. Does the result avoid looking like a bundle-builder app?
9. Could a merchant plausibly achieve the effect with semantic settings only?
10. Is this meaningfully stronger than the first prototype?

## 13. Stop conditions

STOP and document instead of forcing the design if:
- the breakthrough requires fixture-specific coordinates;
- neutral mode collapses into generic cards;
- five steps require a different component;
- mobile needs duplicated content or a custom carousel;
- ordinary packshots make the layout incoherent;
- accessibility/DOM order must be compromised;
- commerce JS must be substantially rewritten for styling;
- merchant x/y/width/breakpoint rescue settings become necessary;
- the result only works with bespoke Beauty campaign art.

## 14. Completion report

Return:
- exact files changed;
- commit SHA;
- tests/checks and exact results;
- four controlling screenshots plus stress screenshots;
- engineering verdict PASS/NARROW/FAIL;
- visual verdict **PENDING HUMAN REVIEW**;
- deviations/conflicts;
- untested evidence;
- CSS/JS complexity delta;
- confirmation no production/M2/other Living Canvas work was touched.

Do not create a PR. Do not merge. Stop for review.
