# Edge Crop executable prototype

This directory is an isolated M1 validation harness. It is not Shopify Liquid, a production section, or authorization for M2.

## Run

From the repository root:

```sh
python3 -m http.server 4173 --directory prototypes/living-canvas/edge-crop
```

Open `http://localhost:4173/`. Use the labelled select to switch the eight required fixtures plus the neutral originality torture fixture. A fixture can also be linked directly with `?fixture=packshot` (or another select value).

## What is being validated

- A two-zone editorial/media composition whose clipped edge is CSS-owned, not part of merchant media.
- Four bounded semantic anchors: `upper-left`, `upper-right`, `lower-left`, and `lower-right`; no arbitrary coordinates.
- Information and mock-Shopify-shaped product hotspot records, including compare-at, sold-out, and deleted-reference states.
- One semantic order across widths. Below 1024px, overlay annotations become a numbered list so panels cannot collide at tablet/small-desktop widths.
- Server-rendered default content and visible non-JavaScript hotspot panels. Initial JavaScript enhancement hydrates those exact nodes rather than replacing them; only subsequent fixture changes render alternate records.

The lifestyle and packshot SVGs are local deterministic stand-ins, with intrinsic dimensions. The `<picture>` selects at most one art-directed source; when no mobile source exists, its `srcset` is removed. The above-fold hero is not lazy-loaded and is the only high-priority image. Product thumbnails are lazy-loaded.

## Hotspot focus pattern

Hotspots are non-modal disclosures: only one is expanded at a time, background content is not inert, and focus is not trapped. Opening moves focus to the panel's first actionable control (the explicitly labelled close button). Escape and that close button collapse the panel and restore focus to the originating numbered trigger. Pointer interaction outside closes without unexpectedly moving pointer users' focus. Without JavaScript, panels remain expanded in source order and their links remain usable.

## Manual test protocol

1. Test each select option at 320px, 768px, 1024px, and 1440px. At 768–1023px, confirm the four-hotspot fixture is a collision-free keyed list; at 1024px, confirm each lower panel flips above its trigger and right-side panels align inward.
2. Tab through the selector, CTA, and every hotspot; activate with Enter/Space.
3. Open a hotspot, press Escape, and confirm focus returns to its numbered trigger. Repeat with the close button and an outside click.
4. Enable reduced motion and confirm no meaningful transition/animation remains.
5. Test browser zoom at 200% and 400%, checking horizontal reflow and complete text.
6. Disable JavaScript and reload: the default composition and all default hotspot content/links must remain visible and usable.

See [`findings.md`](findings.md) for evaluated results and explicit limitations.
