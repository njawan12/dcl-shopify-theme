# M1 Living Canvas — Shopify editor, schema and interaction specification

**Date:** 2026-10-03
**Status:** M1 prototype specification only. No production implementation authorization.

## Purpose
Prove Living Canvas can deliver striking agency-grade compositions through a small Shopify-native editing model without becoming a page builder. Real Shopify resources and ordinary merchant media are mandatory; baked-in product UI or fake interactions fail.

## Merchant model
Add Living Canvas → choose Monument / Split Tension / Edge Crop / Quiet Frame → replace common content/media/product → add only relevant blocks → preview deterministic desktop/mobile adaptations. Changing composition must not destroy content.

### Core section settings
Content: eyebrow, heading, body, primary CTA, secondary CTA. Media: desktop image, optional mobile image, focal strategy, optional video only if later gates approve it. Composition: layout, bounded content position where applicable, density, color scheme, overlay/contrast. Commerce: optional featured product.

Target <=15 visible section-level controls on the normal path. No x/y positioning, arbitrary width percentages/transforms, custom CSS, breakpoint controls, per-device typography/spacing or animation-speed controls.

## Shared blocks
**Evidence stat:** value, label, optional source/footnote/link; max 3. **Hotspot:** information or product mode, label, text/product reference, authored safe anchor rather than x/y; max 4. **Routine step:** label, product reference, optional text; max 5. **Feature fact:** optional icon/image, heading, text/link; max 4. App blocks only where current Shopify architecture and the composition safely support them. No generic canvas/group abstraction.

## Live commerce object
A featured product renders title, current variant price, compare-at/unit price where applicable, independent product image, availability, product link and a safe CTA. View product is universal. Quick add is allowed only when required choices are correctly resolved; never silently choose an arbitrary variant. No fabricated ratings.

## Monument
High-impact campaign statement with live commerce/evidence. Desktop: editorial text, dominant media, optional live product card crossing/anchoring the boundary, evidence rail, at most one major overlap. Mobile: no text/focal collision; commerce becomes a discrete reachable object; evidence stacks or uses accessible overflow. Must work with ordinary packshot/lifestyle media, not only a model holding product.

## Split Tension
Editorial proposition plus Guided Set preview. Desktop: asymmetric copy/media; 2–5 real-product steps; explicit selected state; optional truthful sum of selected variants; Add selected may add ordinary variants individually. Mobile: large readable swipe/scroll cards, not tiny four-column steps. No bundle discount/inventory semantics or app-owned behavior is imitated.

## Edge Crop
Signature replaceable-media treatment using CSS/SVG/clip-path/mask or layout primitives, never a pre-cut merchant asset. Desktop guarantees readable text safe zone and supports 1–4 semantic-anchor hotspots. Hotspots open information or a real-product popover. Mobile geometry reduces/reorients; if overlay positions become unsafe, hotspots become a keyed list beneath media. Trigger is a button, keyboard accessible, visibly focused, exposes expanded state, supports Escape/focus management, and is never hover-only.

## Quiet Frame
Restrained product-led launch hero. Real selected-product title, price, availability and media; rating only via legitimate app data. Variant controls only if they correctly update variant/price/media/availability. Small gallery uses product media. View product is safe default; Add to cart requires correct variant resolution. Mobile keeps price/action obvious and prevents badge/gallery collisions.

## Badge contract
Factual merchant-authored badge via explicit content, metafield/dynamic source, or inherent product state such as sale. Do not make undocumented magic tags the primary system. No fabricated scarcity, popularity or proof.

## Theme-editor proof
M1 must show a truthful editor model: Composition, Content, Media, Featured product, Color scheme, Density, conditional Overlay/contrast; blocks for Evidence stat, Hotspot, Routine step, Feature fact and only proven app contexts. Basic setup should require no documentation. Avoid exposing irrelevant controls for the active composition where Shopify's schema/editor behavior permits.

## Accessibility contract
Internal target WCAG 2.2 AA. Test worst-case contrast, heading order, keyboard operation, visible focus, hotspot semantics, popover focus, reduced motion, 200%/400% zoom/reflow, logical DOM order, long translations and decorative-art exclusion. Internal primary touch target >=44 CSS px. Visual asymmetry must not corrupt screen-reader order.

## Performance contract
Likely LCP image is not lazy-loaded; responsive image output has explicit dimensions/aspect behavior; fetch priority only when justified; optional mobile media must not make both desktop and mobile assets download; below-fold/product thumbnails lazy-load appropriately. Edge Crop uses no extra raster solely for its shape. No autoplay hero video default, no JS for visual masking/overlap, no external animation/carousel dependency. Do not market performance until realistic tests pass.

## Editor lifecycle
Interactive JS must handle Shopify editor load/unload/select/reorder safely: idempotent initialization, listener/observer cleanup, no full-page reload dependency, storefront behavior independent of editor hooks.

## Missing-data resilience
Remain polished with no product, no blocks, 1 vs 3 stats, missing hotspot target, sold-out product, absent compare-at, absent mobile image, permitted text-only state, long copy, expanded translations, absent app block and delayed/failed JS. Broken references never create blank floating UI.

## Cross-preset proof
Before pass: Beauty/Wellness Edge Crop or Split Tension; Jewelry/Accessories using the exact same schema/architecture; neutral ordinary-packshot torture case. Jewelry may change tokens, presets and content—not schema.

## Acceptance gate
PASS only if Edge Crop and Split Tension survive the originality torture test; Monument gains character from live commerce/evidence rather than photography; Quiet Frame proves real commerce rather than mock UI; composition changes preserve content; merchant setup remains shallow; mobile is intentionally composed; apparent interactions are real/prototypable; accessibility/performance contracts are credible; and no prohibited app-like behavior enters the section. Otherwise narrow/redesign before full-theme propagation.