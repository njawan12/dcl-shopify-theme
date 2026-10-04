# M1 Monument — pre-build red-team and visual contract

**Date:** 2026-10-04  
**Status:** APPROVED PRE-CODE CONTRACT for the isolated M1 Monument experiment.  
**Parent system:** Living Canvas.  
**Chosen direction:** Concept 06 — **One Line, One Object**.  
**Fallback reference only:** Concept 05. It is not a second prototype.

## 1. Decision and purpose

Monument must prove one question before production work:

> Can a single-product editorial composition remain unmistakably Monument when premium photography, beauty/fashion styling, serif typography, color, motion and transparent packshots are removed?

The defining sentence is:

> **One product, one dominant statement, one dominant product moment, one continuous compositional axis.**

The experiment is not a homepage hero competition and not a production Shopify section. It is a structural/originality proof.

## 2. What makes Monument Monument

All controlling frames must preserve these relationships:

1. **Dominant statement** — one editorial headline has enough scale and compositional authority to define the surface.
2. **Dominant object** — exactly one product is the commercial object. Its media participates in the composition rather than sitting inside a conventional card.
3. **Continuous axis** — a strong line/rail/datum connects editorial statement, product moment and commerce information. It is structural, not decoration pasted on afterward.
4. **Boundary transgression** — the product moment must visibly interrupt, cross, mask, or reshape the editorial field/axis in a deterministic way.
5. **Negative space as structure** — the composition must not be rescued by filling empty space with badges, cards or secondary modules.
6. **Commerce remains legible** — title, price/state and safe action remain clear without turning the object into a boxed product card.

If neutral fixtures look like “large headline + product card”, Monument fails.

## 3. Merchant-control contract

Merchant supplies:
- featured product;
- headline;
- optional eyebrow/kicker;
- optional short supporting copy;
- optional primary editorial link when appropriate;
- semantic composition choice only if a second bounded Monument treatment is later proven.

Theme owns:
- geometry;
- axis behavior;
- overlap/boundary relationship;
- responsive transformation;
- type scale relationships;
- safe media containment;
- commerce placement.

Forbidden controls:
- x/y coordinates;
- arbitrary offsets/transforms;
- raw pixel widths/heights;
- per-device positioning;
- separate desktop/mobile content trees;
- per-breakpoint typography controls;
- freeform z-index;
- arbitrary overlap amount;
- custom CSS as a normal merchant requirement.

## 4. Data and commerce states

This prototype may remain static/server-rendered; it must not invent commerce JS merely to look interactive.

Required fixtures/behaviors:

| State | Required behavior |
|---|---|
| Product absent | Commerce object disappears and composition deliberately rebalances; no empty frame |
| Deleted/unpublished reference | Same shopper-safe behavior as absent product |
| Single variant available | Truthful title/price/action representation |
| Multi-option unresolved | Safe “View product” behavior; never imply an arbitrary variant is selected |
| Selected/representable variant | Correct price/availability in fixture model |
| Sold out | Truthful sold-out state; product link remains useful |
| Compare-at absent | No empty sale treatment |
| Compare-at valid | Truthful price hierarchy without becoming a badge-led promo card |
| Unit price | Context has room to render without collision |
| Selling-plan/app-owned product | Degrade to product link; do not simulate subscription/bundle behavior |
| Gift card/unusual product | Safe product-link fallback |
| Long product title | Wraps without collision or fixed-height clipping |
| Missing product media | Text/commerce remain deliberate; no broken overlap |
| Multiple product images | Monument still chooses one dominant object; it is not a gallery |
| Ordinary rectangular media | Must work without transparent PNG cutout |
| Transparent packshot | Supported but not required for identity |

No ratings, scarcity, popularity, countdown, stock-pressure, review stars or invented evidence.

## 5. Media torture contract

The design must be tested with:
- transparent object/packshot;
- white-background rectangular product image;
- dark rectangular product image;
- portrait 4:5;
- square 1:1;
- landscape 3:2 or wider;
- low-art-direction catalog photo;
- missing media;
- image with focal subject near each edge.

Rules:
- no manual merchant focal-point coordinates required by the concept;
- no product/media clipping that hides essential product identity;
- `object-fit`/container behavior must be deterministic;
- ordinary rectangular images may become bounded media surfaces, but must still participate in the axis/boundary composition;
- no desktop/mobile duplicate image download merely to achieve layout.

## 6. Copy/localization torture contract

Test:
- very short headline;
- 2-line intended headline;
- 4+ line long headline;
- 30–50% text expansion;
- long product title;
- long price/unit-price string;
- long CTA label;
- empty optional supporting copy.

Rules:
- no fixed text heights;
- no clipping;
- headline scale may fluidly reduce within bounded tokens;
- composition may relax overlap before text becomes unreadable;
- architecture cannot depend on a specific English line break;
- RTL feasibility must not be structurally impossible, though full RTL validation is deferred.

## 7. Responsive contract

### Desktop
- dominant statement and object share one composition;
- axis is immediately visible;
- exactly one major overlap/boundary event;
- commerce information is restrained and attached to the object/axis;
- no conventional boxed product card.

### Tablet
- overlap relaxes before collision;
- axis remains legible;
- object remains dominant;
- no squeezed desktop composition.

### Mobile
Mobile is an authored poster, not a scaled desktop screenshot:
1. statement establishes identity;
2. axis continues through the composition;
3. dominant object interrupts/anchors that axis;
4. commerce follows in logical reading order;
5. safe action remains obvious.

No horizontal page overflow, miniature commerce UI or duplicated semantic DOM.

### Zoom/reflow
At enlargement/reflow, Monument must collapse toward the mobile reading model before content clips or overlaps destructively.

## 8. Accessibility and semantic contract

- one semantic DOM order matching reading/task order;
- visual reordering only where it does not corrupt reading order;
- links are links and buttons are buttons;
- no interaction required to understand the core content;
- visible focus for all interactive controls;
- internal primary targets >=44 CSS px;
- text contrast cannot depend on merchant photography remaining dark/light in one region;
- decorative axis is hidden from accessibility APIs when it carries no information;
- meaningful product image has appropriate alternative text in production;
- no essential meaning conveyed by overlap/color alone;
- reduced-motion state is trivial because motion is nonessential.

Manual AT/zoom/browser validation remains a later evidence gate; static inspection cannot claim full accessibility PASS.

## 9. Performance and implementation constraints

- CSS/layout primitives own composition; no positional JavaScript;
- no canvas/WebGL;
- no external animation/carousel library;
- no JS measurement loop;
- no duplicate responsive DOM;
- no duplicate desktop/mobile LCP media;
- prototype JS should be zero unless a named state genuinely requires it;
- responsive images and LCP priority are production concerns that the architecture must permit;
- structure must tolerate editor re-render/lifecycle later without depending on page-load-only geometry.

## 10. Multi-instance and section-context behavior

Two Monument instances on one page must:
- have no duplicate IDs;
- have no global selectors/state collision;
- not assume first/last section position;
- retain coherent spacing when adjacent;
- not require viewport-global JS.

The section must also survive being placed below the fold.

## 11. Neutral originality torture state

Required neutral frame:
- system sans;
- black/white/gray only;
- no beauty/fashion terminology;
- ordinary non-beauty product;
- ordinary catalog image;
- no transparent cutout requirement;
- no motion;
- no decorative handwriting;
- generic truthful commerce copy.

Human acceptance question:

> If branding and photography are stripped away, can we still identify Monument from the statement/object/axis relationship alone?

If no, FAIL. Do not rescue with styling.

## 12. Cross-vertical proof

At minimum the same architecture must plausibly support:
- Beauty/Wellness;
- Jewelry/Accessories;
- Food/Drink or home/object-based neutral fixture.

No vertical-specific markup fork. Presets may change content/tokens/defaults, not architecture.

## 13. Merchant-misuse cases

Test:
- headline omitted;
- headline excessively long;
- optional copy omitted;
- product missing;
- product title very long;
- media missing;
- low-quality/awkward crop;
- sale price;
- sold out;
- long CTA;
- two sections adjacent.

The system must fail gracefully rather than expose broken geometry.

## 14. Kill conditions

Monument is FAIL if any of these remain true after one implementation pass:
- neutral frame becomes a normal hero or featured-product section;
- identity requires transparent PNGs or bespoke campaign photography;
- product is visually just a card floating over a hero;
- axis is merely decorative and can be removed without changing composition;
- merchant must tune coordinates/offsets to avoid collisions;
- mobile loses the statement/object/axis relationship;
- ordinary rectangular media makes the concept look accidental;
- long/localized copy requires bespoke per-fixture CSS;
- implementation introduces positional JS to maintain geometry.

NARROW is allowed if the system is strong but requires a tighter media/copy envelope that is commercially reasonable and supportable.

## 15. Evidence required before human verdict

Controlling frames:
1. branded desktop 1440;
2. neutral desktop 1440;
3. branded mobile 390;
4. neutral mobile 390.

Stress evidence:
- 320 mobile;
- 768 tablet;
- long/localized copy desktop + mobile;
- ordinary rectangular media desktop + mobile;
- missing media;
- missing product;
- sold out;
- 2 adjacent instances.

Automated/static evidence:
- no horizontal overflow at 320/375/390/430/768/1024/1280/1440;
- no duplicate IDs;
- no forbidden positioning controls;
- no positional JS;
- no duplicated responsive semantic content;
- target-size/static focus checks where applicable;
- all fixture states render without runtime errors.

## 16. Gate

This contract authorizes **one isolated M1 Monument prototype** only.

It does not authorize:
- production theme code;
- M2;
- a Shopify schema;
- PR/merge;
- another Monument concept;
- production-readiness claims.

Human visual verdict is one of **PASS TO PRESERVE / NARROW / FAIL**.
