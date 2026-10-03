# Living Canvas M1 coded prototype

This directory is an isolated **M1 validation harness**, not production theme code and not an M2 scaffold.

## Goal

Mechanically validate the Living Canvas contract before production implementation:
- four compositions share one content model;
- live Shopify product data can replace baked mock commerce;
- Edge Crop geometry is structural, not baked into assets;
- Split Tension can express Guided Set merchandising without pretending to be a bundle engine;
- desktop/mobile composition remains intentional;
- ordinary merchant media does not collapse the design;
- keyboard/focus/missing-data behavior is designed before production.

## Required prototype slices

1. **Edge Crop first** — highest originality value and highest geometry/interaction risk.
2. **Split Tension second** — highest commerce/state risk.
3. **Monument third** — prove live commerce/evidence makes a familiar archetype distinctive.
4. **Quiet Frame fourth** — prove real product/variant behavior and a restrained counterpoint.

## Edge Crop acceptance

The first executable prototype must demonstrate:
- replaceable merchant image;
- CSS/SVG/clip-path/mask structural edge, no pre-cut asset;
- 1–4 semantic-anchor hotspots;
- info hotspot open state;
- product hotspot using real/mock-shaped Shopify product data rather than baked text;
- keyboard operation, visible focus, Escape close and logical DOM order;
- deterministic mobile adaptation with safe text width;
- no JS required for the visual crop itself;
- long heading/body, missing hotspot, no mobile image and ordinary packshot torture cases.

## Boundary

Do not import Skeleton, Dawn, Horizon or create production `sections/`, `templates/`, `config/`, `locales/` or production assets here.

The production foundation decision remains gated by M1 and refreshed ADR-001.

## Next implementation task

Build only the Edge Crop validation harness first. Do not implement all four compositions in one task. Its output must include the prototype, a short test fixture set, and a findings document recording what survived, what failed, and any schema changes required.
