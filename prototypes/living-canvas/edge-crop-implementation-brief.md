# Edge Crop — implementation brief

**Branch:** `m1-living-canvas-prototype`  
**Phase:** M1 isolated validation only.  
**Do not create production theme architecture or open M2.**

## Objective

Implement one executable Edge Crop prototype that proves the signature composition is structurally distinctive, merchant-operable, accessible, performant by construction, and resilient with ordinary content.

This is a validation harness, not a Theme Store-ready section.

## Inputs to obey

Read before coding:
- `docs/m1-signature-system.md`
- `docs/m1-living-canvas-schema-interaction-spec.md`
- `docs/m1-product-architecture-contract.md`
- `docs/engineering-compliance-standard.md`
- `prototypes/living-canvas/README.md`

## Current Shopify constraints revalidated 2026-10-03

Treat as implementation constraints:
- originality must be architectural/experiential, not cosmetic;
- do not derive production submission code from Dawn/Horizon; production foundation decision remains gated;
- avoid complicated/deep merchant configuration;
- app-dependent/API-backed app-like functionality is prohibited;
- fake urgency/scarcity/proof is prohibited;
- accessibility/performance must be tested with real content;
- JS-disabled critical commerce/navigation behavior must remain usable at production stage.

Do not infer that this prototype authorizes production code.

## Build scope — Edge Crop only

Create an isolated browser-runnable harness inside `prototypes/living-canvas/edge-crop/`.

Expected files may include:
- `index.html`
- `edge-crop.css`
- `edge-crop.js`
- `fixtures.js` or equivalent local fixture data
- `README.md`
- `findings.md`

No framework and no external runtime dependency.

### Required visual structure

- Two major zones: readable editorial content + dominant merchant media.
- The signature edge/curve is generated with CSS/SVG/clip-path/mask/layout primitives. It must not be baked into the image.
- The shape must materially affect composition, not merely add a decorative blob.
- Text and media should feel intentionally interlocked while maintaining a safe readable zone.
- Include 1–4 hotspot anchors whose positions are selected from a small authored semantic set.
- Do not expose arbitrary x/y coordinates.

### Required interaction

Implement:
1. information hotspot;
2. product hotspot;
3. open/close state;
4. Escape close;
5. outside-click close if appropriate;
6. focus return to trigger;
7. visible focus;
8. sensible tab order;
9. no hover-only information.

Product hotspot fixture should mimic the fields we will later receive from Shopify:
- id/handle;
- title;
- URL;
- image;
- price;
- compare-at price optional;
- availability.

Do not fabricate ratings, inventory urgency or app data.

### Required responsive behavior

Desktop and mobile must be intentionally different compositions from the same content.

At narrow widths:
- protect readable text width;
- reduce/reorient the edge geometry;
- if overlay hotspots become collision-prone, convert them into a keyed list beneath/adjacent to media;
- preserve one semantic DOM order;
- do not duplicate content solely for desktop/mobile presentation.

### Required torture fixtures

Provide switchable fixture states:
1. art-directed beauty/lifestyle;
2. ordinary white-background packshot;
3. long heading + long body;
4. one information hotspot;
5. four mixed hotspots;
6. missing product target;
7. no mobile-specific image;
8. minimal content.

The prototype passes only if the composition remains coherent in all states.

### Accessibility

- semantic heading/content structure;
- hotspot triggers are real buttons;
- accessible names;
- `aria-expanded` / relationship semantics where appropriate;
- popover content reachable and announced sensibly;
- Escape and focus restoration;
- logical DOM order independent of visual placement;
- visible focus;
- reduced-motion handling;
- no essential information encoded only by position/color;
- primary interactive targets target >=44 CSS px internally;
- test at 200% and 400% zoom/reflow.

Do not overuse ARIA where native semantics suffice.

### Performance

- no JS for the crop/mask itself;
- no animation library;
- no framework;
- explicit image dimensions/aspect strategy;
- prototype should model eager/high-priority behavior for the actual above-fold/LCP media and avoid lazy-loading it;
- do not cause desktop and mobile alternatives to both download;
- keep JS enhancement scoped to hotspot interaction.

### Progressive enhancement

The visual composition must render without JS.
Information/product hotspot content must have a usable non-JS fallback or direct destination/content path; document the chosen fallback in findings.

## Tests/checks

At minimum document/manual-check:
- keyboard-only;
- Escape/focus restoration;
- reduced motion;
- 320px narrow viewport;
- representative tablet and desktop widths;
- 200%/400% zoom;
- ordinary packshot;
- long copy;
- missing product;
- JS disabled.

If the repo already has suitable lightweight test tooling, use it. Do not add a large dependency stack just for this harness.

## Findings document

`findings.md` must answer:
1. Does Edge Crop remain distinctive after neutralizing photography/color/type?
2. Does the ordinary-packshot fixture still look intentional?
3. Which semantic hotspot anchors worked/failed?
4. What breaks first on mobile/long copy?
5. Did accessibility force any visual changes?
6. Is the merchant-control model still shallow?
7. What should change in the schema spec before production?
8. PASS / NARROW / FAIL recommendation.

Do not mark PASS merely because the prototype renders.

## Hard boundaries

Do not:
- create production `sections/`, `blocks/`, `templates/`, `config/`, `locales/` or `layout/`;
- import Skeleton/Dawn/Horizon;
- implement Monument, Split Tension or Quiet Frame;
- open/merge a PR;
- touch PR #6;
- claim Theme Store compliance from this prototype;
- expand scope to a full theme.

The deliverable is one rigorous Edge Crop experiment and its evidence.
