# M1 Split Tension — Visual Direction Synthesis

**Date:** 2026-10-04  
**Status:** Product-owner visual direction after review of the first implemented prototype and six visual explorations.  
**Purpose:** Define what Split Tension must become before any second implementation pass. This is a visual/product contract, not production authorization.

## 1. Decision on first prototype

**Verdict: NARROW.**

The first implementation validates the commerce/state architecture but does not meet the visual bar. Its neutral torture state remains structurally recognizable, which supports keeping the underlying concept, but the signature is too dependent on a large editorial rectangle plus conventional bordered product cards.

Keep:
- guided multi-product sequence;
- asymmetrical editorial/commerce relationship;
- explicit shopper inclusion;
- sequential storytelling;
- proven commerce state machine;
- progressive-enhancement/responsive architecture.

Reject as signature:
- boxed white product cards floating beside/on top of an editorial panel;
- small passive packshots;
- generic checkbox treatment as the dominant commerce gesture;
- detached summary/total footer;
- rectangular overlap alone as the primary design idea;
- a composition that reads as “editorial panel | product cards.”

## 2. Visual exploration synthesis

Six desktop directions were reviewed. The strongest source directions are:

### A. Editorial Breakthrough — PRIMARY
Strongest idea: editorial imagery, headline and commerce physically interlock. Product steps cross the editorial boundary instead of merely occupying a separate commerce column.

Preserve:
- dramatic image crop;
- oversized editorial type;
- numbered sequence;
- product controls embedded into the composition;
- anchored aggregate action.

Avoid copying the exact card treatment. The breakthrough relationship is the IP, not the white rectangles.

### B. Bold Image Integration — PRIMARY
Strongest idea: a single high-impact image field carries the emotional story while commerce occupies a disciplined edge and visibly intersects the image.

Preserve:
- image as structural field, not decoration;
- strong vertical sequence;
- numbered anchors;
- restrained but obvious commerce;
- bottom action integrated with the whole surface.

Risk: can collapse into a conventional split hero if the commerce edge is too independent.

### C. Immersive Split — SECONDARY
Strongest idea: steps become spatial anchors connecting editorial imagery to purchase controls.

Borrow:
- connective sequence;
- visible numbered journey;
- evidence/proof living inside the editorial field.

Do not make absolute-position hotspots the merchant editing model.

### Directions not selected as the core
- Layered Canvas: attractive, but too dependent on luxury art direction and conventional cards.
- Horizontal Flow: useful responsive/alternative grammar, but too close to a polished routine/product grid.
- Editorial Cards: visually strong but risks becoming card composition rather than a unique commerce system.

## 3. Target signature

Split Tension should feel like:

> **An editorial campaign surface that commerce breaks into and becomes part of.**

Not:

> **An editorial panel next to a product selector.**

The defining visual behavior is **boundary transgression**: imagery, typography, step sequence and purchase controls share one composition, with the Guided Set visibly crossing or reshaping the editorial/commerce boundary.

This must be recognizable even when:
- color becomes neutral;
- typography becomes a system sans;
- photography becomes ordinary packshots/product still life;
- beauty language is removed;
- motion is disabled.

## 4. Required desktop grammar

One coherent system, not six layouts.

At large desktop:
1. editorial/media field is dominant enough to establish campaign impact;
2. headline is intentionally composed with the media, not placed in a generic text column;
3. 2–5 commerce steps form a clear ordered trajectory;
4. at least one step or sequence rail crosses the editorial/commerce boundary;
5. product imagery may break its local container but must remain bounded and robust;
6. controls remain legible and conventional enough to use immediately;
7. the selected-items action belongs to the composition rather than looking like a separate utility panel;
8. negative space is deliberate; cards do not create large dead white rectangles;
9. the signature comes from CSS/layout/typographic relationships, not from fixture artwork.

The design should still work when product images have white backgrounds, inconsistent aspect ratios and ordinary merchant photography.

## 5. Commerce-surface treatment

Do not hide commerce in the pursuit of art direction.

Each step must make these immediately scannable when relevant:
- step number/purpose;
- product identity;
- current price;
- variant/option choice;
- availability;
- explicit inclusion;
- safe product-page path.

But the controls should be **composed**, not simply dropped into a bordered card.

Preferred directions:
- open or lightly surfaced step zones rather than full rectangular cards;
- sequence rail/anchors as structural connective tissue;
- product media allowed to bridge editorial and commerce zones;
- inclusion control visually tied to the step action;
- summary/action anchored to the Guided Set trajectory.

Do not invent custom checkbox semantics merely for styling. Native semantics remain mandatory.

## 6. Image and typography contract

Photography may amplify the experience but may not rescue weak structure.

The system must support:
- cinematic lifestyle crop;
- product still life;
- plain packshot;
- transparent-background product media;
- portrait and landscape source images.

Headline treatment may be expressive, but the neutral torture state must remain recognizable with ordinary system typography.

No baked text in images.

No design assumption that every merchant owns campaign photography.

## 7. Mobile translation

Mobile is not a shrunken desktop collage.

The signature should translate into:
- one strong editorial/media opening;
- an obvious numbered Guided Set trajectory;
- large product/media moments between or within steps;
- vertically sequenced controls;
- an aggregate action that feels connected to the journey without obscuring controls.

Do not preserve desktop overlap if it harms reading/order. Preserve **trajectory and boundary relationship**, not pixel geometry.

No carousel required for the core mobile experience.

## 8. Neutral originality torture test

The next visual proof must be shown in two states before code:

### Branded state
Premium Beauty + Wellness art direction with credible campaign imagery and products.

### Neutral state
- black/white/gray accessible palette;
- system sans typography;
- ordinary packshots;
- generic non-beauty copy;
- no decorative motion.

Pass only if a reviewer can still recognize the same Split Tension system from:
- editorial/commerce boundary;
- sequence trajectory;
- step/media relationships;
- integrated aggregate action.

If it reduces to a split hero plus cards, fail the direction.

## 9. Merchant-operability guardrails

The merchant must not need to art-direct coordinates.

Normal controls remain semantic:
- composition/preset;
- editorial media;
- heading/body;
- 2–5 ordered Guided Set steps;
- product references;
- optional short step copy/media;
- bounded scheme/density choices.

No x/y positions, arbitrary overlap sliders, custom breakpoints, per-card CSS, duplicate mobile content, or per-device artboards.

The visual system must create the breakthrough automatically from semantic content.

## 10. Second-pass proof gate

**Do not modify the prototype yet.**

Before a second code pass, create a single high-fidelity visual design for the synthesized direction at:
- 1440 desktop branded;
- 1440 desktop neutral;
- 390 mobile branded;
- 390 mobile neutral.

The four frames must depict the **same component/content architecture**, not four independently art-directed mockups.

Evaluate:
1. immediate visual strike;
2. structural originality;
3. commerce clarity;
4. ordinary-media resilience;
5. neutral-state recognizability;
6. mobile translation;
7. merchant-operability plausibility.

Only after those four frames pass should the existing proven state engine be reskinned/recomposed.

## 11. Product-owner bar

The next version must be strong enough that a Theme Store browsing merchant could plausibly stop on the screenshot before reading the feature list.

“Clean,” “premium,” and “well designed” are insufficient.

The desired reaction is:

> **I have not seen product education and product selection composed quite like this in a Shopify theme, and I can imagine my own brand using it.**

If the visual proof cannot reach that bar without bespoke agency art direction, Split Tension remains NARROW or is removed from the signature set.


## 12. Four-frame visual proof result — 2026-10-04

The required four-frame proof was completed as one coherent responsive system:
- desktop branded;
- desktop neutral/non-beauty;
- mobile branded;
- mobile neutral/non-beauty.

**Visual proof verdict: PASS TO SECOND IMPLEMENTATION PASS.**

Why it passes:
- the branded desktop reaches the required Theme Store screenshot impact;
- the neutral desktop remains recognizably the same system outside Beauty + Wellness;
- the numbered trajectory, editorial/commerce boundary and integrated action survive the vertical change;
- mobile preserves the same journey without attempting to reproduce desktop overlap literally;
- commerce remains immediately legible;
- the composition can plausibly be generated from semantic merchant inputs rather than coordinates.

Important caveat: the mockups prove visual direction, not production feasibility. They do not override the state-machine, accessibility, performance, responsive, app, or merchant-operability contracts.

### Controlling visual architecture for implementation

The second implementation pass should reproduce the **relationships**, not pixel-copy the mockup:

1. dominant editorial/media field;
2. numbered 2–5 step trajectory adjacent to and visually crossing the editorial boundary;
3. product media bridging the trajectory and commerce surface where space permits;
4. commerce details aligned as open/lightly surfaced zones rather than generic standalone cards;
5. aggregate selection/action visually attached to the full composition;
6. mobile transformation into editorial opening + ordered commerce sequence + connected aggregate action;
7. neutral state achieved by tokens/content/media changes only—no separate component architecture.

The implementation must continue to support ordinary merchant media. Campaign photography is an enhancement, not a prerequisite.

### Explicit non-goals from the visual proof

The mockups contain presentational details that are **not automatically product requirements**:
- quantity steppers shown in the concept do not override the M1 quantity=1 state-machine contract;
- decorative handwritten text is optional art direction, not required theme functionality;
- navigation/header shown in the mockup is context only and not part of Split Tension;
- badge/evidence language must remain truthful and data/merchant authored;
- imagery shown is directional and not a requirement for bespoke photography.

The existing proven commerce state engine should be preserved unless a visual requirement exposes a genuine contract conflict. Do not rewrite working commerce logic merely to restyle the surface.
