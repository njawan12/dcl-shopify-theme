# M1 Commerce Mosaic — pre-build red-team contract

**Status:** controlling M1 prototype contract; no production authorization.  
**Purpose:** prove that collection merchandising can be structurally distinctive without degrading shopping clarity, Shopify semantics, merchant usability, accessibility, performance or catalog resilience.

## 1. Product hypothesis

Commerce Mosaic is **not** a normal product grid with a promotional tile inserted into it.

It is an authored merchandising rhythm in which product cards, one bounded feature-product treatment and one optional editorial/story interruption share a coherent grid grammar. The rhythm must remain recognizable after neutralizing typography, color, photography and motion.

The shopper must still understand instantly: what is a product, what it costs, whether it is available, where it links, and how to continue scanning the collection.

## 2. M1 scope decision

Prototype **one primary rhythm plus one conventional safe fallback**. Do not build all historical pattern families merely because they were listed during exploration.

Primary rhythm: **Anchor Cadence**.

Desktop concept:
- ordinary products establish the shopping rhythm;
- one real product may become a bounded feature/anchor spanning more visual area;
- one optional editorial/story tile may interrupt the rhythm at a deterministic authored point;
- subsequent products restore the shopping rhythm rather than continuing arbitrary mosaic placement.

Mobile concept:
- one semantic source/order;
- deterministic linear reading order;
- feature product remains visually emphasized without moving ahead of products that precede it semantically;
- editorial content never traps or disguises products;
- no masonry.

Fallback: conventional product grid using the same product-card truth and data path.

## 3. Non-negotiable invariants

1. Product order and collection semantics remain truthful.
2. A product remains recognizably a product regardless of span/treatment.
3. Feature treatment cannot change price, availability, variant or destination truth.
4. Editorial tiles are visibly editorial and never imitate products.
5. Filters, sort, pagination/load-more boundaries and result counts cannot be corrupted by presentation.
6. DOM/source order remains logical and keyboard order follows it.
7. Mobile is deterministic, not a CSS masonry rearrangement.
8. The system works with ordinary rectangular packshots and mixed ratios.
9. No metafield is required for a usable collection.
10. No JS is required to calculate layout placement.
11. No arbitrary merchant x/y/span/row/column controls.
12. Multiple section instances cannot leak layout/state into each other.
13. Apps are guests; product-card/app seams cannot be visually clipped or structurally invalidated.
14. The conventional fallback remains first-class, not a broken degraded mode.

## 4. Merchant contract

Merchant-facing controls are intentionally shallow.

Allowed prototype-level controls:
- rhythm: Anchor Cadence / Standard Grid;
- feature product source: automatic bounded position or explicitly selected collection product where semantically valid;
- optional editorial tile enable/content/media/link;
- density: compact / balanced / spacious;
- product media treatment from bounded global/system choices;
- color scheme through semantic theme tokens.

Forbidden:
- arbitrary cell placement;
- row/column coordinates;
- arbitrary spans;
- per-device product ordering;
- freeform masonry;
- per-card custom CSS;
- duplicate desktop/mobile content trees;
- merchant-entered pixel dimensions;
- manual recreation of the entire collection as blocks.

For production, collection products must remain collection-driven. M1 fixtures may model selection states but must not normalize hand-authoring every product card.

## 5. Product-card truth matrix

Prototype evidence must cover at least:
- normal product;
- single-variant product;
- multi-variant product;
- sold out;
- unavailable/deleted fixture safety;
- compare-at/sale price;
- unit price;
- long title;
- long vendor/auxiliary text if shown;
- no image;
- one image;
- mixed portrait/square/landscape imagery;
- transparent packshot;
- ordinary white-background catalog image;
- factual badge absent/present;
- swatch/option preview absent/present if represented;
- rating/app seam absent/present without fabricated rating content;
- complex product where quick-add is inappropriate;
- selling-plan/app-owned commerce where card must degrade to product navigation rather than invent logic.

No fixture may fabricate urgency, scarcity, review counts, inventory claims or discounts.

## 6. Collection/system states

Challenge the rhythm with:
- 1 product;
- 2 products;
- 3–5 products;
- 12+ products;
- 30–100+ conceptual catalog density via repeated/varied fixtures;
- editorial tile absent;
- editorial tile present;
- feature product missing/unavailable;
- no eligible feature treatment;
- pagination boundary before/after editorial insertion;
- filtering that reduces results below the intended insertion point;
- sorting changes;
- empty collection;
- no-results filtered state;
- long collection title/description;
- localization expansion 30–50%;
- RTL feasibility;
- adjacent collection intro/filter/sort UI;
- app content inside/adjacent to product-card supported seam;
- JS delayed/failed.

The rhythm must collapse predictably when insufficient products exist. It must never leave unexplained holes.

## 7. Placement rules

M1 must implement placement from a small deterministic rule set, not fixture-specific CSS.

Anchor Cadence starting hypothesis:
- establish at least three ordinary product encounters before the strongest interruption on wide layouts;
- feature product consumes a bounded authored span only when enough products exist;
- editorial interruption occurs only when enough remaining products exist to restore the shopping rhythm afterward;
- if the catalog/result set is too small, omit interruptions rather than force them;
- filtered/sorted results recompute presentation from the current truthful result sequence without changing source semantics;
- pagination must not duplicate or orphan editorial interruptions.

Exact visual positions may be refined in the prototype, but any rule requiring product IDs, fixture names or per-index exceptions fails the architecture test.

## 8. Responsive contract

Evidence widths: **320, 375, 390, 430, 768, 1024, 1280, 1440**.

Desktop/wide:
- visual asymmetry may exist;
- scanning lanes remain obvious;
- feature product is visually dominant but not mistaken for advertising;
- editorial interruption is bounded and clearly non-product.

Tablet:
- cadence must recompose without collisions or accidental gaps;
- no assumption that desktop spans divide cleanly.

Mobile:
- preserve source order;
- default to a legible 2-column or intentionally bounded responsive grid where content permits;
- feature product may span full width at its semantic position;
- editorial tile may span full width at its semantic position;
- long titles/prices/badges cannot create overlap;
- touch targets and card destinations remain clear;
- no horizontal page overflow.

## 9. Accessibility contract

- semantic product lists/grids must remain understandable independent of CSS;
- headings follow page hierarchy;
- links/buttons have unambiguous accessible names;
- no whole-card nested interactive-control trap;
- keyboard order follows DOM order;
- focus indicators are visible and unclipped;
- badges/status are not color-only;
- editorial media has correct alt behavior;
- price/sale semantics remain understandable;
- zoom/reflow to 400% must not require two-dimensional page scrolling except legitimate media;
- reduced motion has no loss of meaning;
- no hover-only required information.

## 10. Performance contract

- layout is CSS-first; no runtime JS layout engine;
- responsive images use appropriate intrinsic dimensions/srcset behavior in production architecture;
- feature span must not cause duplicate media downloads;
- below-fold media can remain lazy-loadable;
- no carousel dependency;
- no third-party library;
- editorial tile cannot introduce mandatory video/heavy media;
- DOM growth must remain proportional to actual products/content, not duplicated layouts.

## 11. Originality torture test

Controlling neutral proof:
- system font;
- accessible monochrome palette;
- no decorative motion;
- ordinary non-beauty products;
- mixed white-background and plain rectangular catalog imagery;
- generic truthful product names/prices;
- editorial tile uses ordinary copy/media rather than campaign-grade art.

PASS only if a reviewer can still see a coherent authored merchandising rhythm rather than “Shopify grid + promo card.”

Cross-preset reasoning must also demonstrate that the same architecture can serve Beauty/Wellness, Jewelry/Accessories and Food/Drink through content/tokens/defaults only.

## 12. Merchant misuse / adversarial cases

Test:
- extremely long editorial heading;
- editorial tile with no image;
- editorial tile with no link;
- awkward landscape image;
- feature product with missing media;
- all products using white-background images;
- every product title two or three lines;
- mixed sale/sold-out badges;
- feature product sold out;
- only one product after filtering;
- repeated section instance;
- optional controls all disabled.

The system must remain deliberate and usable without fixture-specific patches.

## 13. Kill conditions

**FAIL / KILL Anchor Cadence** if any of these are true after one serious prototype pass:
- neutral proof reads as a conventional grid plus promo tile;
- distinction depends on premium photography, serif type, color or animation;
- product scanning becomes materially worse;
- feature product resembles an ad rather than a product;
- editorial content disguises product semantics;
- merchant needs arbitrary placement/span controls;
- mobile requires duplicated content or reordered DOM;
- mixed ratios/long titles cause fragile geometry;
- filter/sort/pagination correctness requires bespoke exceptions;
- layout needs runtime JS measurement/placement;
- product-card commerce truth forks between normal and feature treatments;
- ordinary 30–100+ catalog density becomes exhausting or chaotic.

**NARROW** if the system is useful only for homepage featured collections but not truthful collection pages.

**PASS TO PRESERVE** only if the neutral version is distinctive, shopping remains obvious, merchant controls stay bounded, and the same grammar can credibly extend to collection + featured-collection surfaces.

## 14. Evidence required before human verdict

At minimum:
- branded Beauty/Wellness desktop 1440;
- neutral desktop 1440;
- branded mobile 390;
- neutral mobile 390;
- mixed-ratio stress frame;
- long-title/sale/sold-out stress frame;
- editorial-absent frame;
- small-result frame;
- all eight target widths;
- automated assertions for source order, product truth, duplicate IDs, overflow, missing states and deterministic placement;
- complexity report: CSS, browser JS, breakpoints, merchant controls, DOM duplication, dependencies;
- explicit known-untested list.

Human verdict is one of: **PASS TO PRESERVE / NARROW AND HOLD / FAIL AND KILL**.

No M2 or production authorization follows automatically from a prototype pass.