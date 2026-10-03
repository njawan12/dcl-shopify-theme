# M0 historical customization-demand inventory — 2026-10-03

## Purpose

This inventory reconstructs recurring storefront customization work from DCL's historical client/operator evidence. It is used to decide what a premium theme should productize and what should remain custom agency work.

This is **not** a merchant survey and does not claim statistical frequency. Items are separated by evidence strength so recollection, prior project records and generic agency capability are not accidentally treated as equivalent.

## Decision rule

A pattern is a strong productization candidate only when it:

1. recurs across brands or clearly represents a repeatable storefront need;
2. is achievable within Theme Store rules and native Shopify architecture;
3. can reduce meaningful custom-development work;
4. can be exposed without creating an excessive settings surface;
5. does not depend on one vendor/app;
6. preserves correct commerce behavior, accessibility, performance and mobile resilience.

A recurring request can still be rejected if it creates disproportionate support or complexity.

## 15 reconstructed demand patterns

| # | Historical demand pattern | Concrete DCL evidence / example | Evidence strength | Theme implication | Initial disposition |
|---|---|---|---|---|---|
| 1 | Reworked PDP buy boxes | Buoy: PDP/buy-box redesign around product selection, subscription merchandising, value communication and purchase journey. Founder reports new buy boxes as a recurring request because brands want to change the look and experiment. | **HIGH** | Purchase area needs more than one cosmetic layout; define a small set of materially different, correct compositions with reorderable supporting content. | **PRODUCTIZE — P0 candidate** |
| 2 | Merchant-controlled product badges | Cowboy requested product-data controls such as badges on product imagery. Fresh Cut Paper work also included dynamic PDP badge metafields with text/color/background controls. | **HIGH** | Objective product-specific badges should be data-driven, optional, media-safe and merchant-operable. | **PRODUCTIZE — P0 candidate** |
| 3 | Subscription / selling-plan presentation | Buoy work included selling-plan configuration, subscription-module frontend rendering and later subscription-platform migration. Cowboy requested control around the subscription area. | **HIGH** | Theme owns native selling-plan presentation and generic app-block fit, not subscription business logic or vendor APIs. | **PRODUCTIZE NATIVE LAYER — P0** |
| 4 | New custom sections for campaign/content needs | Founder identifies creation of new sections as one of the most common developer responses when a theme cannot express a design. Buoy requested reusable podcast landing-page composition rather than one product template per podcast. | **HIGH** | Build a curated library of genuinely useful composition primitives; prioritize structural range over dozens of cosmetic section clones. | **PRODUCTIZE SELECTIVELY — P0** |
| 5 | Structural layout changes beyond existing settings | Founder reports structural changes as a common implementation requirement after design handoff; premium themes only sometimes accommodate the design cleanly. | **HIGH** | Core surfaces need bounded structural variants. Avoid pretending spacing/color controls equal structural flexibility. | **ARCHITECTURAL P0** |
| 6 | Design/CSS customization for brand refreshes | Founder reports complete design refreshes to keep brands feeling current and CSS work as a common implementation path when themes reach their limit. Refreshes require both designers and DCL. | **HIGH** | Strong semantic design tokens plus meaningful composition variants; do not promise designer replacement or arbitrary CSS controls. | **PRODUCTIZE FOUNDATION — P0** |
| 7 | Cart redesign / purchase-continuity changes | Founder names new cart designs among recurring client requests. Historical Fresh Cut Paper work included AJAX cart synchronization, line-item properties and PDP→cart→checkout QA for an add-on experience. | **HIGH** | Cart deserves a first-class visual/interaction system, but custom discount/app logic remains outside theme scope. | **PRODUCTIZE CORE CART — P0** |
| 8 | Metafield-backed merchant controls | Founder reports merchants often do not know how to create metafields and wire them to frontend components; once DCL creates the control they generally operate it themselves. Buoy used Accentuate/metafield-backed PDP implementations. | **HIGH** | Dynamic-source-compatible settings and documented native metafield recipes should be pervasive where useful, but metafields themselves are not differentiation. | **PRODUCTIZE AS CAPABILITY — P0** |
| 9 | Flexible product education | Historical work/proposals across DCL include PDP tabs, product information, education sections and structured PDP content. The revised target vertical has recurring needs for benefits, ingredients/materials, usage, specifications, FAQs and proof. | **MEDIUM-HIGH** | Create high-quality education components with standard-content fallbacks and optional structured data. | **PRODUCTIZE — P0 candidate** |
| 10 | Product media/gallery treatment | Buoy/Fresh Cut Paper history includes PDP image work; prior DCL scopes include galleries/video and founder evidence says brands request visual experimentation. | **MEDIUM-HIGH** | Multiple polished media compositions, mixed-media correctness, badge overlays and strong mobile behavior. | **PRODUCTIZE — P0 candidate** |
| 11 | Variant / option presentation fixes | Founder specifically cites variants not showing properly as a reason merchants come to DCL. Buoy work includes flavor selectors and product-selection behavior. | **HIGH** | Variant correctness is table stakes; provide polished option-value presentation and graceful fallback rather than exotic inference. | **P0 TABLE STAKES + POLISH** |
| 12 | Landing/campaign pages without template proliferation | Buoy requested reusable podcast landing pages with unique URLs and customizable image/copy/banner content; DCL has historically built campaign/landing-page experiences. | **HIGH** | Provide strong page compositions and flexible sections without one bespoke template per campaign or a proprietary builder. | **PRODUCTIZE — P0/P1** |
| 13 | Collection/product-card merchandising | Historical DCL work includes collection/PLP price logic, badges, product-card CTA changes and promotional merchandising; broader scopes include filters/search and collection UX. | **MEDIUM-HIGH** | Stable product cards, merchandising/story tiles, collection headers and native filter/sort behavior. | **PRODUCTIZE — P0** |
| 14 | Mobile-specific storefront behavior and recovery | DCL historical work includes mobile optimization, sticky mobile ATC proposals, mobile-only media, responsive fixes and cross-device QA. Founder evidence also identifies CSS/structure work when existing themes cannot match design. | **MEDIUM-HIGH** | Mobile is not positioning; it is a hard quality requirement. Components need explicit mobile composition/recovery behavior rather than desktop collapse. | **P0 QUALITY GATE** |
| 15 | Clean developer extensibility after native limits | Founder reports premium-theme structure and code issues as recurring developer pain. DCL still needs custom development for truly bespoke designs and functionality. | **HIGH** | Clean section/block contracts, predictable CSS, low coupling, modular JS, documented extension points and no universal catch-all architecture. | **ARCHITECTURAL P0** |

## What this inventory changes

### Productize aggressively

The strongest repeatable opportunity is around **high-value commerce surfaces and merchant-operable control**:

- PDP purchase area / buy box;
- product media and product-specific badges;
- native selling-plan presentation;
- structured product education;
- cart presentation;
- reusable content/storytelling sections;
- collection/product-card merchandising;
- dynamic-source-compatible controls;
- semantic design system;
- clean extension architecture.

### Productize carefully

These are valuable only if they remain bounded:

- structural variants;
- page/landing compositions;
- design controls;
- section libraries;
- experimentation-friendly settings.

The theme fails if these become hundreds of loosely related toggles.

### Keep custom

The following should remain agency/app work:

- genuinely bespoke art direction that requires new primitives;
- custom business logic;
- vendor-specific subscription/review/loyalty/bundle behavior;
- API-backed app functionality;
- custom discount engines;
- data-collection quizzes;
- arbitrary "build anything" systems;
- unusual integrations;
- one-off interactions whose support cost exceeds repeatable merchant value.

## Emerging component architecture

The evidence supports organizing the product around **surfaces and primitives**, not marketing-job workflows.

### Commerce surfaces
1. Product media
2. Product purchase area
3. Product education
4. Product card
5. Collection merchandising
6. Cart
7. Header/navigation/search

### Content primitives
1. Rich media + copy
2. Benefits/features
3. Comparison
4. Ingredients/materials/specifications
5. Usage/process/timeline
6. FAQ/disclosure
7. Proof/results/testimonial host
8. Promotional/story tile
9. CTA/action group
10. App-block host

### Control layers
1. Global semantic design tokens
2. Surface-level structural variants
3. Block composition/order
4. Dynamic product data
5. Limited local presentation controls
6. Developer extension contracts

This model is deliberately conventional in merchant-facing terminology.

## Incumbent challenge required

The inventory is **not yet a feature specification**.

For each P0 candidate, the next task is to challenge the requirement against current strong premium themes. The question is not "does competitor X have a sticky ATC?" It is:

> Does a strong incumbent already provide enough structural and merchant-operable flexibility that a competent designer/merchant can achieve the intended variation without custom Liquid/CSS/JS?

Each pattern must be classified:

- **TABLE STAKES** — incumbents solve it well; implement excellently but do not position as differentiation.
- **GAP / PRODUCTIZATION OPPORTUNITY** — incumbents offer the feature but recurring brand needs exceed the exposed control in a repeatable way.
- **CUSTOM BY NATURE** — trying to productize it would create excessive complexity/support.
- **UNTESTED** — access/evidence insufficient.

## Current conclusion

The 15-pattern inventory supports the revised thesis strongly enough to continue M0.

It does **not** prove Theme Store differentiation. Many individual features are already common. The candidate differentiation is the system-level combination of:

1. exceptional target-vertical visual design;
2. deliberately chosen structural flexibility on high-value surfaces;
3. merchant-operable controls based on recurring agency requests;
4. complete, polished defaults;
5. clean developer extensibility when the native boundary is reached.

The next evidence step is the incumbent capability challenge. Weak or already-solved patterns must be downgraded rather than defended.
