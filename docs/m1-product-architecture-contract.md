# M1 product architecture contract — brand-led DTC

**Status:** controlling M1 product contract.  
**Date:** 2026-10-03.  
**Authorization:** prototype/design validation only; no production theme code.

## 1. Product promise

A premium Shopify theme for brand-led DTC merchants with focused-to-medium catalogs who need an exceptional storefront, conversion-clear product pages and unusually strong native merchandising control without turning the theme editor into a page builder.

Primary first-preset catalog classification: **Some (11–100+)**.
First preset: **Beauty + Wellness**.
Architecture must remain capable of later Jewelry/Accessories and Food/Drink presets without vertical forks.

## 2. Architecture rule

Every merchant-facing control must belong to one of six layers, in this order:

1. semantic global token;
2. bounded surface variant;
3. merchant-controlled block composition/order;
4. Shopify/dynamic-source content;
5. small local presentation choice;
6. developer extension point.

If a requirement can only be solved with arbitrary CSS, raw dimensions, per-device layout builders, deep block trees or a vertical-specific code fork, the design must be reconsidered before adding a setting.

## 3. Core surface contracts

### A. Header / navigation
Must support:
- announcement/promotional context without fake urgency;
- multi-level navigation and mega-menu capability;
- search entry and predictive-search-ready interaction;
- account/cart/localization entry points where applicable;
- sticky behavior as an option;
- mobile navigation designed independently for touch and hierarchy;
- promotional content that degrades cleanly when absent.

Differentiation target: calm brand-first navigation that can become commercially dense without becoming visually noisy.

### B. Product card
Commerce truth is invariant: media, title, price/compare-at, availability state and destination.
Bounded capabilities may include:
- secondary/hover media where appropriate;
- native swatch/option preview;
- factual badge;
- rating/app seam;
- quick add/quick view only when product complexity permits;
- compact/editorial merchandising treatments.

No card may depend on metafields to remain usable.

### C. Collection / merchandising
Must support Shopify faceted filtering/search requirements and robust pagination/lazy behavior.
Product-grid system must handle:
- mixed image ratios without breakage;
- promotional/story tiles without corrupting product semantics;
- collection intro/editorial context;
- sorting/filtering;
- swatch-aware cards;
- realistic 30–100+ product density;
- mobile filtering and merchandising.

Differentiation target: collection pages should be capable of brand storytelling without becoming landing-page templates.

### D. PDP media
Three bounded structural families to prototype:
1. Gallery — efficient conventional browsing;
2. Editorial stack — larger narrative media rhythm;
3. Focused lead — dominant hero media with supporting assets.

All must support all Shopify rich product media types, variant-media truth, mixed ratios, zoom/lightbox where useful, keyboard/touch access, reduced motion and resilient loading.

### E. PDP purchase area
Three bounded structural families to prototype:
1. Balanced;
2. Compact;
3. Editorial.

Commerce truth cannot change across variants.

Required product information/functionality includes title, variant price/unit price/compare-at, description access, options, quantity, add to cart, availability/sold-out handling, variant price/state updates, accelerated checkout, Shop Pay Installments, pickup availability, product recommendations, rich media, swatches and gift-card recipient handling where relevant.

Block model should make most purchase-decision elements reorderable while preserving guardrails. Main product and featured product must accept app blocks.

Modern capability seams:
- ratings/reviews app;
- selling-plan/subscription apps and native selling-plan truth where applicable;
- complementary product/routine merchandising;
- shipping/returns/delivery reassurance;
- factual benefit/trust microcontent;
- line-item-property/personalization seam where appropriate.

No vendor-specific subscription/review/bundle implementation in core theme.

### F. Product education / proof
A narrow family of reusable content primitives, not one universal mega-section:
- feature/benefit;
- specifications/materials/ingredients/nutrition;
- usage/process/care;
- comparison;
- results/proof;
- FAQ/disclosure;
- testimonial/editorial quote host;
- media + text/story;
- icon/fact list.

Standard Shopify data/manual content must produce a complete experience. Dynamic sources/metafields/metaobjects enhance repeated structured content but are never mandatory for a polished default.

### G. Cart
Cart page is mandatory and cart drawer may be offered as an enhanced surface.
Must correctly support:
- line items, quantities and full refresh/update truth;
- discounts/automatic discounts;
- selling plans;
- cart notes;
- taxes-included messaging;
- checkout and accelerated checkout;
- empty state;
- app-extension seams;
- errors/loading/focus restoration;
- mobile collision safety.

Cross-sell/progress/reassurance features must be truthful and optional. No fictitious scarcity or fake progress.

### H. Storytelling / campaign content
Prefer a small system of composable primitives over dozens of near-duplicate sections.
Required families to prototype:
- editorial hero;
- split media/text;
- rich media;
- feature grid;
- comparison;
- proof/results;
- editorial collection/product spotlight;
- timeline/process;
- quote/testimonial host;
- CTA/action group.

Each family needs strong presets/defaults and only meaningful structural choices.

### I. Search / discovery
Must support:
- Shopify search and faceted filtering requirements;
- predictive-search-ready UX;
- product/article/page/result clarity;
- empty/no-result recovery;
- mobile usability;
- localization and long-content resilience.

This is a quality/table-stakes surface, not a differentiation claim.

## 4. Global design system

Initial global control budget remains deliberately small.

Semantic token groups:
- typography roles;
- color roles;
- content/container widths;
- spacing density;
- shape/radius;
- control/button treatment;
- media treatment;
- motion level.

A merchant should be able to create a recognizably different brand without manipulating dozens of per-section padding/font/color controls.

## 5. Theme blocks / sections strategy

Use Shopify-native JSON templates, section groups, sections, theme blocks, app blocks and dynamic sources.

Rules:
- theme blocks only when reuse/merchant composition materially improves usability;
- section-local blocks when scope is intentionally local;
- static blocks when structure must remain stable but merchant settings should remain editable;
- app blocks only in contexts with legitimate app-extension use cases;
- shallow purposeful trees even though Shopify technically permits deeper nesting;
- no universal canvas/group abstraction whose purpose is to recreate arbitrary page-builder layouts;
- no section-count arms race.

Current Shopify limits must be respected but are ceilings, not design targets.

## 6. Conversion doctrine

The theme does not claim a universally highest-converting layout.

Every conversion-oriented capability must:
1. answer a real purchase question or remove friction;
2. preserve Shopify commerce truth;
3. remain accessible and mobile-safe;
4. avoid meaningful performance regression;
5. be testable/disableable without code where reasonable.

Priority hierarchy:
- purchase clarity;
- product understanding;
- trust/reassurance;
- option/variant confidence;
- delivery/returns clarity;
- proof;
- complementary discovery;
- campaign persuasion.

No fake urgency, viewer counters, invented inventory, deceptive timers or manipulative defaults.

## 7. Mobile contract

Mobile is not “desktop stacked vertically.”

For each core surface define:
- first viewport priority;
- media height/rhythm;
- sticky-header/sticky-purchase collision rules;
- touch target and option-selection behavior;
- content compression/disclosure;
- filter/search behavior;
- drawer/modal focus behavior;
- app-block overflow/resilience;
- long title/price/localization behavior.

A desktop composition may adapt materially on mobile while retaining one semantic content source.

## 8. App compatibility contract

Apps are guests, not architectural dependencies.

Core product must work with no apps installed.
Provide intentional insertion seams for common app classes:
- ratings/reviews;
- subscriptions/selling plans;
- bundles/complementary commerce;
- loyalty/rewards;
- personalization;
- back-in-stock;
- size/fit or product-information extensions.

Unexpected app blocks must not collapse the layout. Do not write CSS targeted to a vendor unless an explicit compatibility fix is later justified and documented.

## 9. Resilience matrix required in M1

Every prototype must be challenged with:
- 1, 2, 6 and 20+ variants/options combinations where Shopify permits;
- unavailable/sold-out states;
- long titles and long option labels;
- sale/compare-at and unit pricing;
- one image vs many mixed-ratio images;
- video/3D media;
- no reviews/no metafields/no complementary products;
- long structured content;
- translations/long strings and RTL feasibility;
- gift cards;
- pickup enabled/disabled;
- selling plan present/absent;
- app block inserted in expected and awkward positions;
- 30–100+ product collection;
- JS delayed/failed for progressive-enhancement-critical flows;
- keyboard, screen reader, zoom/reflow and reduced motion;
- low-end/mobile network performance.

## 10. M1 proof package

M1 cannot pass on a moodboard.

Required:
1. three materially different PDP compositions from the same system/data;
2. one coherent selected/synthesized visual direction;
3. desktop + mobile for PDP, collection, product card, cart and one storytelling page;
4. realistic Beauty/Wellness demo dataset large enough to expose catalog behavior;
5. stripped originality comparison where fonts/colors/photography/motion are neutralized;
6. control-budget audit;
7. merchant-operability tasks;
8. app-block insertion test;
9. developer-extension exercise;
10. resilience-matrix review;
11. current Shopify requirement traceability;
12. explicit list of table-stakes vs differentiators.

## 11. M1 pass/fail

**PASS only if** the same bounded system produces materially different premium outcomes, remains understandable to a merchant, survives realistic commerce states, and still has visible structural character after decorative styling is stripped.

**FAIL / NARROW if**:
- quality depends on exceptional demo photography;
- differences are mostly fonts/color/motion;
- merchant freedom requires arbitrary layout controls;
- app insertion makes surfaces brittle;
- normal Shopify data produces a weak store;
- mobile requires separate duplicated content;
- PDP flexibility breaks commerce correctness;
- the system becomes a generic page builder;
- later preset feasibility requires vertical-specific forks.

## 12. Production boundary

This document does not authorize production code.

After M1 passes, ADR-001 must be refreshed against the final system and current Shopify foundation/originality requirements. Only then can the M2 entry gate be reconsidered.
