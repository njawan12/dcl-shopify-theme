# M1 Living Canvas — Pre-build red-team matrix

**Date:** 2026-10-03  
**Status:** Controlling pre-build gate for the remaining Living Canvas experiments.  
**Purpose:** Resolve predictable system behavior before more prototype code is written. Edge Crop evidence informs this matrix; it does not authorize production implementation.

## 1. Decision rule

No remaining Living Canvas composition is coded until its row-level risks below have an explicit intended behavior and acceptance test.

Classify outcomes as:
- **SYSTEM RULE** — solve once and inherit across compositions.
- **COMPOSITION RULE** — bounded behavior unique to a composition.
- **PROTOTYPE REQUIRED** — uncertainty cannot responsibly be resolved from architecture/specification alone.
- **DEFER TO PRODUCTION VALIDATION** — implementation is understood but requires real Shopify/browser/device evidence.

A prototype exists to answer a named uncertainty. It must not become exploratory coding.

## 2. Cross-composition invariants

These are SYSTEM RULES for Monument, Split Tension, Edge Crop and Quiet Frame.

| Domain | Failure to prevent | Controlling behavior | Evidence needed |
|---|---|---|---|
| Content model | Changing composition destroys/requires re-entry of common content | Shared content/media/featured-product model; composition changes presentation, not ownership | Schema-model inspection + editor prototype later |
| Merchant controls | Page-builder/settings explosion | Bounded semantic choices; no x/y, raw widths, breakpoints, transforms, per-device typography/spacing | Control-count audit |
| Missing data | Blank floating UI / broken reference | Omit invalid optional object; preserve coherent layout; never expose editor diagnostics to shoppers | Fixture/state tests |
| Product truth | Baked/fake commerce | Product title, price, compare-at/unit price, availability and URL originate from product/variant data | Shopify prototype later |
| Variant state | Wrong price/availability/add | Never quick-add unresolved required options; product link is safe fallback | Commerce state matrix |
| Ratings/reviews | Fabricated proof | No stars/count unless legitimate app/data source is present | App insertion test later |
| Scarcity/proof | Fake urgency | No invented viewers, stock, countdown, popularity or claims | Content audit |
| App ownership | Theme recreates specialist app | Host legitimate app blocks/seams; do not implement review/subscription/bundle/back-in-stock services | App compatibility test |
| DOM order | Visual asymmetry corrupts reading order | One logical semantic order; CSS changes visual composition only | Keyboard + screen-reader test |
| Focus | Inconsistent custom interaction | Native elements first; non-modal disclosures use explicit open/close/focus-return contract | Browser/AT test |
| Touch | Tiny decorative controls | Internal primary target >=44 CSS px | Browser/device test |
| Mobile | Desktop merely stacks/shrinks | Each composition has deterministic authored mobile resolution | Visual fixture test |
| Long content | Clipping/collision | No fixed content heights; bounded measure; composition can relax before content clips | Long-copy fixtures |
| Localization | English geometry assumptions | Expansion-tolerant labels/text; avoid typography dependent on exact line count | 30–50% expansion fixture + RTL feasibility later |
| JS failure | Core story/commerce disappears | Server-render meaningful content; JS only enhances state/interaction | JS-disabled test |
| Editor lifecycle | Duplicate handlers/stale state | Idempotent init + cleanup when production Shopify section lifecycle exists | Production implementation test |
| LCP/media | Signature destroys performance | Above-fold likely LCP prioritized; responsive source; no double desktop/mobile download; below-fold lazy | Lighthouse/network later |
| Visual effects | Decorative JS/dependencies | CSS/SVG/layout primitives first; no external animation/carousel runtime | Code inspection |
| Motion | Accessibility/perf distraction | Nonessential, restrained, reduced-motion safe | Browser test |
| Ordinary media | Demo art hides weak architecture | White-background/mixed-ratio/low-art-direction fixtures required | Visual torture test |
| Originality | Palette/type/photo mistaken for IP | Neutral palette/type/media/motion torture state retains recognizable structural language | Visual review |
| Presets | Vertical code forks | Same schema/architecture across Beauty, Jewelry, Food; differentiation via tokens/defaults/content | Cross-preset proof |
| Empty/minimal | Section only works when full | Coherent with minimum valid content and zero optional blocks | Fixture |
| Maximum density | Collisions/support burden | Explicit block caps; deterministic overflow/reflow | Max-density fixture |
| Accessibility claims | Static code called “pass” | Browser/AT/zoom evidence required for experiential PASS | Manual evidence |
| Performance claims | Architecture called “fast” | Measured realistic-density evidence required | Lighthouse/network evidence |

## 3. Commerce-state matrix

Every composition that exposes commerce must define behavior for these states before implementation.

| State | Required behavior |
|---|---|
| Product absent | Commerce object omitted; composition rebalances |
| Product deleted/unpublished | No dead trigger/link; shopper sees no editor diagnostic |
| Single variant available | Direct add may be permitted if product form semantics are correct |
| Multiple variants, unresolved options | Never silently add default/arbitrary variant; route to product or proven accessible selector |
| Selected variant available | Correct price/media/availability/action |
| Selected variant sold out | Disabled/unavailable purchase state; product link remains useful |
| Product fully sold out | Truthful sold-out state; no urgency workaround |
| Compare-at absent | No empty sale treatment |
| Compare-at valid | Truthful sale presentation |
| Unit price applicable | Preserve required unit-price context |
| Selling plans exist | Theme must not erase/misrepresent plan state; direct-add only when correct plan/variant semantics are proven |
| Gift card / unusual product | Must degrade to safe product link if inline purchase model is inappropriate |
| App-owned bundle/subscription | Do not imitate; provide compatible host/seam |
| No reviews app | No empty stars or fake rating |
| Complementary/recommendation data absent | Omit cleanly |

## 4. Composition risk matrix

### Monument

**Job:** expressive editorial statement with one live commerce object and optional evidence.

Predictable risks:
- becomes generic image + headline once art direction is neutralized;
- floating product card collides with text/focal subject;
- evidence rail creates tiny mobile text;
- ordinary packshot makes overlap feel arbitrary;
- second CTA adds clutter;
- image overlay/contrast becomes merchant-tuning burden.

Pre-build rules:
- only one major overlap relationship;
- commerce object has authored bounded anchor choices, not x/y;
- mobile commerce object exits dangerous overlay and becomes discrete;
- evidence max 3 and may reflow/stack;
- product absent must still leave a deliberate composition;
- overlay strength exists only where media-under-text requires it.

**Named uncertainty:** Can Monument remain structurally recognizable with neutral type/color and ordinary packshot, or is it merely a conventional hero?

**Decision:** PROTOTYPE REQUIRED, but visual/static composition proof first; no commerce JS needed initially.

### Split Tension

**Job:** strongest guided-commerce expression; editorial proposition + 2–5 product steps.

Predictable risks:
- accidentally becomes bundle builder;
- summed price becomes false when variants/selling plans change;
- “Add selected” produces partial/failing cart state;
- 5 steps become unreadable on mobile;
- selection state inaccessible;
- merchant must configure too much;
- products with required options break the flow.

Pre-build rules:
- Guided Set is merchandising, not a bundle product;
- each step references ordinary product/resource data;
- unresolved options cannot be silently selected;
- price sum is shown only for resolved selected variants;
- Add selected means individual native line items, never discount/bundle semantics;
- no-JS path is ordinary product links/forms;
- mobile uses large sequential cards/overflow with clear state, never miniature strip;
- max 5 steps.

**Named uncertainties:** Can a useful guided set remain truthful with variant complexity? Can mobile interaction stay simple with 5 products? Can no-JS fallback remain commercially useful?

**Decision:** PROTOTYPE REQUIRED after state-machine contract is written. This is the highest commerce-risk Living Canvas variant.

### Edge Crop

**Job:** signature editorial edge geometry + information/product annotation.

Already demonstrated structurally:
- CSS-owned curved geometry;
- semantic hotspot anchors;
- tablet/mobile list transformation;
- information/product-shaped data;
- progressive enhancement and missing-reference behavior;
- neutral torture fixture exists.

Remaining evidence gaps:
- actual visual quality;
- browser collision/reflow;
- keyboard/AT/zoom;
- measured performance;
- cross-preset visual proof.

**Decision:** NARROW AND HOLD. No more code until visual/browser evidence stage. Do not patch speculatively.

### Quiet Frame

**Job:** restrained product-led commerce composition and commercial counterweight.

Predictable risks:
- becomes a normal PDP/featured-product section;
- inline variants duplicate PDP complexity;
- rating UI faked without app;
- gallery/video increases LCP/JS cost;
- badges collide with media;
- direct add wrong for multi-option products.

Pre-build rules:
- real product media/title/price/availability only;
- View product universal safe action;
- inline variant selection only if we can prove correct state synchronization;
- rating only through legitimate source/app seam;
- gallery is native product media, bounded count/behavior;
- no custom carousel dependency;
- badge is factual merchant data/product state, not magic-tag requirement.

**Named uncertainty:** Does Quiet Frame contribute enough identity to Living Canvas while remaining intentionally quieter, or is it redundant with a strong featured-product section?

**Decision:** VISUAL PROOF FIRST. Do not code until its structural distinction is visible in neutral form.

## 5. Responsive state matrix

Required widths are evidence points, not merchant-configurable breakpoints.

| State | Monument | Split Tension | Edge Crop | Quiet Frame |
|---|---|---|---|---|
| Narrow mobile | Separate commerce object; evidence stack | Sequential/swipe cards; persistent clear selected state | Reduced curve + keyed annotation list | Product-first or text-first bounded variant; obvious price/action |
| Wide mobile | No subject/text collision | 2–5 cards remain readable | Overlay only if proven safe; otherwise list | Gallery/variants cannot crowd CTA |
| Tablet | Relax overlap before collision | Two-zone only if cards remain usable | List/non-overlay mode already preferred | Product/media balance without desktop squeeze |
| Desktop | One deliberate overlap | Split editorial + guided strip/cards | Signature curved geometry + bounded overlays | Restrained product/media frame |
| Zoom/reflow | Must collapse like mobile before clipping | Must preserve step order/state | Must preserve semantic order | Must preserve commerce order |

No composition may rely on duplicated desktop/mobile semantic content.

## 6. Accessibility interaction model

System default: avoid custom widgets unless the signature requires them.

- Links remain links; actions remain buttons.
- Disclosure/popover is non-modal unless there is a genuine modal task.
- Open state has an explicit accessible relationship.
- Focus destination and restoration are defined before implementation.
- Escape closes dismissible overlays.
- Pointer-outside close must not unexpectedly steal focus.
- No hover-only content.
- Selected Guided Set step must be conveyed beyond color/position.
- Horizontal mobile overflow must retain logical keyboard order and visible offscreen affordance.
- Product option controls use native semantics where possible.
- Decorative crop/mask geometry is absent from accessibility tree.
- Motion is never required to understand state.

## 7. Merchant misuse / content stress

Every composition must survive:
- 1-word and very long headings;
- no eyebrow;
- no body;
- no CTA where allowed;
- long CTA;
- 30–50% translated-text expansion;
- portrait, square and landscape merchant imagery;
- low-quality/white-background packshot;
- no mobile-specific image;
- product title 2–3 lines;
- price with sale/unit-price complexity;
- sold-out product;
- all optional blocks at maximum;
- one optional block only;
- missing dynamic source;
- app block absent;
- merchant changes composition after content is populated.

If a composition requires a narrow photographic art direction to remain coherent, it fails the merchant-operability goal.

## 8. Performance threat model

Reject before coding:
- JS-driven crop/layout;
- autoplay hero video as default;
- duplicate desktop/mobile image downloads;
- carousel library for a handful of media items;
- animation runtime;
- eager below-fold thumbnails;
- DOM duplication solely for responsive layout;
- universal component that loads all four composition scripts/styles regardless of use.

Production implementation should load only behavior required by rendered blocks/composition where practical.

## 9. App boundary matrix

Living Canvas may **host**, not recreate:
- reviews/ratings;
- subscriptions/selling plans;
- bundles;
- loyalty;
- back-in-stock;
- personalization.

Before production, prove representative app insertion does not destroy spacing, DOM order, sticky behavior or mobile layout. App absence must leave no placeholder scar.

## 10. Editor model gate

Normal merchant path remains:
1. choose Composition;
2. enter shared Content;
3. choose Media;
4. optionally select Featured product;
5. choose Color scheme/Density;
6. add a small number of semantic blocks.

Composition-specific settings must be exceptional and bounded. If a prototype needs more controls to rescue its layout, redesign the composition rather than expose more settings.

Target remains <=15 visible normal-path section-level controls, excluding naturally grouped content fields.

## 11. What requires code vs visual proof

**Do not code yet:**
- Quiet Frame: first prove it is visually/structurally non-redundant.
- Monument: first prove neutral/packshot structural identity.

**Code later for named uncertainty:**
- Split Tension: variant/selection/cart truthfulness and mobile guided-set state.
- Edge Crop: no more prototype code until browser/visual evidence.

This prevents implementation from becoming the design process.

## 12. Living Canvas M1 exit criteria

Living Canvas can only move toward production architecture when:

1. Edge Crop has browser-rendered visual evidence and survives neutral/ordinary-media review.
2. Split Tension has a written state machine, then proves truthful Guided Set behavior with complex variants and no-JS fallback.
3. Monument survives a neutral static/interactive visual proof without relying on photography.
4. Quiet Frame proves it is materially more valuable/distinctive than a conventional featured-product section; otherwise remove it.
5. One non-Beauty preset reproduces the surviving system without schema/code forks.
6. Merchant control audit remains shallow.
7. Accessibility behavior is specified before code and manually evidenced where experiential.
8. Performance claims wait for measured evidence.
9. Any composition that fails is removed or narrowed rather than rescued through settings proliferation.

**Important:** Living Canvas does not need four surviving variants. A stronger system with 2–3 excellent, coherent compositions is preferable to four weak variants kept for symmetry.
