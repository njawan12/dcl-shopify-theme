# M1 Signature System — Design IP Contract

**Date:** 2026-10-03  
**Status:** controlling originality/design hypothesis for M1; prototype only, no production authorization.

## Objective

The theme must be recognizable at Theme Store thumbnail scale and remain structurally distinctive after photography, color, typography and motion are neutralized.

The signature is not a beauty aesthetic. It is a reusable composition and interaction language for premium brand-led DTC.

## Signature 1 — Living Canvas

A bounded editorial composition system that lets media, commerce and typography occupy one intentional canvas instead of stacking as conventional Shopify rectangles.

### Behaviors
- 2–3 controlled composition zones, never freeform drag/drop.
- Deliberate overlap/crop relationships with safe text and focal zones.
- Product or collection can be embedded as a live commerce object, not baked into imagery.
- Optional annotation/fact layer sourced from real merchant content.
- Mobile resolves to a separately art-directed composition from the same content source.
- Variants: **Monument**, **Split Tension**, **Edge Crop**, **Quiet Frame**.

### Merchant controls
Content, media, focal point, featured resource, contrast scheme, composition variant, density, optional annotation.
No x/y positioning, arbitrary transforms or per-device pixel controls.

### Surfaces
Hero, editorial campaign, collection intro, brand story, product spotlight.

## Signature 2 — Commerce Mosaic

A merchandising grammar that mixes product cards, collection/story cards and promotional/editorial cards in a controlled grid while preserving product semantics and discovery.

### Behaviors
- Products can occupy standard or feature spans according to bounded patterns.
- Editorial tiles may interrupt the grid without disguising products.
- Merchant chooses from authored grid rhythms rather than placing arbitrary cells.
- Product count/filter/sort/pagination semantics remain conventional.
- Mobile has deterministic order and no masonry accessibility trap.
- Mixed ratios and ordinary packshots must still look intentional.

### Pattern families
**Cadence A:** 3 products → feature story → products.  
**Cadence B:** lead product + compact supporting products.  
**Cadence C:** collection story break between product groups.  
**Cadence D:** conventional grid fallback.

### Surfaces
Collection, search merchandising where appropriate, featured collection, homepage discovery.

## Signature 3 — Guided Set

A native guided-merchandising composition for discovering a set/routine/look/box without pretending to be a bundle app.

### Behaviors
- Merchant defines 2–5 semantic steps.
- Each step points to products/collections or merchant-authored recommendations.
- Shopper moves through steps and sees selected native products.
- Theme may use native Ajax cart to add selected variants individually.
- Price shown is truthful sum of selected native variants; no invented bundle discount.
- Selling-plan/app-owned bundle logic is not recreated.
- Works as **routine** (beauty), **stack/look** (jewelry/accessories), **box/menu** (food), while merchant-facing schema uses neutral terminology such as “Guided set”.
- Fully usable without JS through links/product forms or a server-rendered fallback.

### Merchant controls
Step label, explanatory copy, source/curated products, optional/required presentation, imagery, completion CTA copy.
No rule engine, inventory orchestration, API-backed personalization or discount engine.

## Signature 4 — Evidence Layer

A reusable proof language integrated into commerce/story surfaces rather than isolated generic icon rows.

### Content types
- sourced metric/stat;
- ingredient/material/specification fact;
- before/after;
- comparison;
- testimonial/review-app host;
- certification/claim;
- process/usage step.

### Behaviors
- Evidence can attach visually to Living Canvas, PDP media, product education and editorial surfaces.
- Claims are merchant-authored; metrics support optional source/footnote.
- Before/after requires explicit labels and accessible alternative content.
- No fake activity, inventory, urgency or unsupported default claims.
- App review content enters through app blocks; theme does not fabricate ratings.

## Cross-system visual grammar

The four signatures share:
- strong scale contrast rather than decorative clutter;
- intentional negative space;
- bounded asymmetry;
- live commerce objects inside editorial compositions;
- repeated edge/focal relationships;
- a restrained motion model used only to reveal hierarchy or state;
- semantic tokens and preset-specific art direction.

They must not depend on beige palettes, serif fonts, wet-face photography, botanical imagery or beauty-specific language.

## Preset differentiation test

The same four systems must support visibly distinct presets without code forks.

### Beauty + Wellness
Editorial/clinical tension; fluid macro media; routine-oriented Guided Set; evidence emphasizes ingredients/results/usage.

### Jewelry + Accessories
Sharper geometry, smaller type-to-object scale, metallic/material detail, stack/look Guided Set; evidence emphasizes materials/craft/size/provenance.

### Food + Drink
More energetic density and color, tactile packaging/ingredient media, box/menu Guided Set; evidence emphasizes flavor/ingredients/nutrition/serving/provenance.

Preset differentiation must use tokens, composition defaults, section presets and content—not vertical-specific Liquid forks.

## Originality torture test

Before M1 passes:

1. Replace all imagery with neutral white-background packshots and generic lifestyle placeholders.
2. Replace preset fonts with neutral Shopify-available fonts.
3. Convert colors to a simple monochrome accessible palette.
4. Disable nonessential motion.
5. Remove beauty terminology.

A reviewer should still be able to identify Living Canvas, Commerce Mosaic, Guided Set and Evidence Layer as one coherent system.

Then reproduce the same system with Jewelry and Food content. If either requires arbitrary layout controls or new vertical-specific architecture, M1 fails/narrows.

## Merchant usability gate

A first-time merchant must be able to:
- choose a signature composition from a preset;
- replace its media/copy/product;
- change one structural variant;
- reorder permitted content;
- preview a safe mobile result;
without documentation for the basic path and without touching code.

Advanced flexibility belongs in dynamic sources, app blocks and developer extension points—not a page-builder UI.

## Shopify review guardrails

- Uniqueness must exist across overall experience, core templates, navigation, product cards, media treatment and page structure.
- No signature may be reproducible solely through cosmetic settings.
- No app-dependent or API-backed theme functionality.
- No deceptive/fake urgency, scarcity, stock or social proof.
- Demo functionality must be genuinely built into the theme; no baked-in UI masquerading as functionality.
- All interactive signatures require keyboard/focus/semantic/manual accessibility design.
- Realistic image/content density must remain within performance budgets.
- Settings stay shallow, merchant-readable and opinionated.

## What we are explicitly NOT building

- freeform canvas/page builder;
- arbitrary x/y/rotation controls;
- masonry as the primary product grid;
- proprietary content database;
- native wishlist;
- review system;
- subscription engine;
- bundle/discount engine;
- back-in-stock service;
- fake stock/viewer/countdown features;
- dozens of cosmetic section clones.

## M1 visual proof required next

Do not generate another whole-theme moodboard first.

Prototype these signatures independently using ordinary merchant content:
1. Living Canvas: four structural variants, desktop + mobile.
2. Commerce Mosaic: three rhythms + conventional fallback, 12+ mixed products.
3. Guided Set: full 3-step interaction states + native-cart outcome + no-JS fallback.
4. Evidence Layer: PDP/editorial attachment examples with long/short/missing content.

Only after these survive the torture test should they be propagated into full homepage/PDP/collection/cart/search/editorial templates.
