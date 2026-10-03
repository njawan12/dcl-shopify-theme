# M1 Split Tension — Commerce State-Machine Contract

**Date:** 2026-10-03  
**Status:** Controlling pre-build contract for the Split Tension validation prototype.  
**Scope:** M1 prototype only. This document authorizes no production theme code and does not reopen the launch-market decision.

## 1. Prototype question

Split Tension is the highest-commerce-risk Living Canvas composition. The prototype exists to answer three questions before production architecture is allowed:

1. Can a 2–5 step Guided Set remain truthful when products have variant, availability, pricing, and selling-plan complexity?
2. Can the mobile experience remain understandable and operable with five products?
3. Can the no-JavaScript experience remain commercially useful rather than becoming a broken imitation of the enhanced flow?

If the answer requires bundle semantics, silent variant defaults, app-owned subscription logic, a page-builder control model, or a large client runtime, Split Tension fails or narrows.

## 2. Product boundary

Split Tension is **guided merchandising**, not a bundle builder.

A set contains 2–5 ordered steps. Each step may reference one ordinary Shopify product and merchant-authored explanatory content. The enhanced experience may let a shopper choose eligible native variants and add multiple resolved selections as **individual cart line items**.

It must never:
- create a synthetic bundle product;
- imply a bundle discount that Shopify does not actually provide;
- reserve inventory across the set;
- invent availability, scarcity, ratings, savings, or demand;
- recreate a subscription, bundle, loyalty, personalization, or back-in-stock app;
- silently choose an arbitrary required option for the shopper;
- describe a partially successful cart operation as fully successful.

A product link is the universal safe fallback.

## 3. State ownership

There are three independent state layers.

### 3.1 Merchant-authored step state
Server rendered and authoritative for:
- step order;
- step label;
- explanatory copy;
- referenced product;
- optional editorial media where the later prototype requires it.

Missing/deleted product references produce no fake commerce object. The remaining set rebalances coherently.

### 3.2 Shopify commerce state
Shopify product/variant data is authoritative for:
- product and variant identity;
- option values;
- price and compare-at price;
- unit price where applicable;
- availability;
- product URL;
- selling-plan applicability.

The prototype may model these states with fixtures, but production behavior may not replace Shopify truth with merchant-entered duplicates.

### 3.3 Shopper selection state
Client enhancement may own only:
- which step is currently active;
- which valid option values the shopper explicitly selected;
- which resolved eligible variant is selected;
- whether an eligible step is included in the pending multi-add operation;
- transient request/loading/error/success state.

Selection state must be derivable, reversible, and exposed semantically. It must not become a second inventory or pricing authority.

## 4. Per-step state machine

Each step resolves to exactly one of these shopper-facing states.

| State | Entry condition | Price contribution | Primary behavior |
|---|---|---:|---|
| unavailable-reference | Product missing/deleted/unpublished | none | Omit commerce controls; preserve editorial step only if meaningful |
| link-only | Product type/state is unsafe for inline purchase | none until product page resolves it | View product |
| unresolved | Product has required options and no explicit valid selection | none | Choose options / View product; cannot be included |
| resolved-available | Explicitly resolved variant is purchasable and inline add is eligible | resolved variant price | May be selected for Add selected |
| resolved-sold-out | Explicitly resolved variant is unavailable | none | Sold out; View product remains |
| single-available | One purchasable variant and no shopper choice is required | variant price | May be selected for Add selected |
| fully-sold-out | No purchasable variant | none | Sold out; View product remains |
| selling-plan-sensitive | Selling-plan choice affects truthful purchase semantics and is not explicitly resolved | none | View product; exclude from multi-add |
| app-owned | Bundle/subscription/special purchase behavior belongs to an app | none | Host/app seam or View product; exclude from theme multi-add |
| request-pending | Eligible selected item is in active cart request | frozen displayed resolved price | Disable duplicate submit; announce progress |
| request-error | Cart add failed for this item/request | none in success accounting | Preserve selection; expose actionable error and retry/product link |
| request-success | Shopify confirms line was added | confirmed selected price for pre-add summary only | Announce result; cart is authority thereafter |

A step may visually transition among unresolved, resolved-available, resolved-sold-out, and link-only as explicit shopper choices change.

## 5. Variant-resolution rules

1. **No silent choice.** If a product has multiple meaningful variants/options, the initial state is unresolved unless Shopify/product semantics establish that no shopper choice is required.
2. A variant is resolved only when the shopper has explicitly supplied every required option and the combination maps to a real variant.
3. Changing any option invalidates the previous resolved variant until the new combination is resolved.
4. Price, compare-at price, unit-price context, availability, and add eligibility update from the resolved variant together. They may never update independently.
5. An unavailable combination cannot remain selected as add-eligible.
6. Variant selection is conveyed by native controls/semantics and not color alone.
7. The prototype must include at least: one single-variant product, one multi-option product, one sold-out variant, and one fully sold-out product.
8. If inline option UI becomes materially more complex than a bounded guided-merchandising surface, the state narrows to **View product** rather than importing full PDP complexity.

## 6. Selling-plan and unusual-product rule

Split Tension does not implement a second subscription engine.

- If a product can be truthfully purchased as an ordinary one-time variant without requiring a plan decision, that ordinary purchase may remain eligible.
- If a selling plan is required, preselected by app logic, materially changes price/purchase terms, or cannot be represented correctly by the bounded prototype, the step becomes **selling-plan-sensitive** and is excluded from Add selected.
- App-owned bundles/subscriptions are **app-owned** and excluded.
- Gift cards, products requiring recipient/custom properties, quantity rules, personalization, or other unusual purchase requirements default to **link-only** unless a later explicit contract proves inline correctness.

This is deliberate graceful narrowing, not a missing feature.

## 7. Selection and summed-price contract

There are two distinct concepts: **resolved** and **included**.

A step contributes to the displayed set total only when:
- it has a resolved eligible variant;
- it is included by the shopper;
- the variant is currently available;
- its purchase semantics are safe for native individual add.

Therefore:

`displayed total = sum(current price of every included, resolved, eligible variant)`

Rules:
- unresolved, sold-out, link-only, selling-plan-sensitive, app-owned, and missing products contribute nothing;
- compare-at values are not summed into invented “set savings”;
- no discount language appears unless a real Shopify discount is independently applied by Shopify;
- currency formatting must use Shopify's applicable money presentation in production;
- unit-price context stays with the relevant item and is not collapsed into a misleading aggregate;
- a changed option immediately removes the stale contribution until the new variant resolves;
- the UI labels the number of eligible included items so a shopper cannot mistake a partial set for all steps.

## 8. Add-selected transaction contract

**Add selected** means: request Shopify to add the currently included, resolved, eligible variants as ordinary individual cart line items.

Preconditions:
- at least one eligible item is included;
- every included item is resolved and available;
- no included item requires unsupported selling-plan/app/custom-property semantics;
- no add request is already pending.

If any included step becomes invalid before submission, submission is blocked and focus/message points to the first affected step.

During request:
- prevent duplicate submission;
- retain the visible selections;
- expose an accessible pending status;
- do not optimistically claim cart success.

On response:
- Shopify's response is authoritative;
- announce confirmed success only after confirmation;
- update cart UI/count from confirmed cart state, not arithmetic assumptions.

### Partial/failure rule

The implementation must not tell the shopper “Set added” when only part succeeded.

The prototype must explicitly test the chosen Shopify request strategy. If the eventual endpoint can produce ambiguous/partial results, the UI must reconcile confirmed cart state and identify failures. If reliable atomic semantics cannot be established, narrow the enhanced behavior to per-step adds or another truthful native flow rather than masking uncertainty.

This uncertainty is a **PROTOTYPE REQUIRED** gate, not an assumption.

## 9. No-JavaScript contract

With JavaScript disabled, Split Tension must remain useful.

Server-rendered output provides:
- editorial proposition;
- ordered 2–5 step content;
- real product title/image/price context where safe;
- truthful availability;
- a View product link for every valid product.

No-JS does **not** pretend that a multi-product Add selected control works. If a single-variant native product form is included in the prototype, it must be a real independent form for that product; otherwise View product is sufficient and preferred for the first proof.

Core discovery and product navigation therefore survive JS failure. Enhanced multi-selection is optional enhancement, not the only commerce path.

## 10. Mobile interaction contract

At narrow widths, Split Tension becomes an ordered sequence of large step cards. It must not become a miniature desktop strip.

Required behavior:
- logical DOM order equals step order;
- each card exposes step number/label, product identity, current state, and safe action;
- selected/included state is conveyed by text/state semantics as well as styling;
- no hover dependency;
- primary touch targets meet the internal 44 CSS px target;
- five-step fixture remains readable without clipped product names/prices/actions;
- horizontal overflow is permitted only if the prototype proves visible offscreen affordance, keyboard order, focus visibility, and no hidden essential state; otherwise use vertical sequence;
- aggregate selection summary/Add selected must not obscure card controls or become a sticky collision;
- zoom/reflow must preserve the same order and functionality.

Default prototype direction: **vertical sequential cards on narrow mobile**. A swipe carousel is not the default and requires separate evidence.

## 11. Accessibility contract

Before implementation:
- use native radio/select/button/link semantics where they fit;
- each option group has a programmatic label tied to its product/step;
- included/selected state is programmatically determinable;
- price/availability changes are announced deliberately without turning every option movement into noisy live-region output;
- request pending, success, and error are announced;
- errors identify the affected product/step and provide a recovery action;
- focus is not moved on ordinary option changes;
- on blocked Add selected, focus moves only when necessary to the first invalid control/message using a documented pattern;
- successful add does not force focus into a cart drawer unless that later cart contract explicitly requires it;
- keyboard order follows DOM order;
- no focus trap;
- reduced motion does not hide state;
- 200%/400% zoom and reflow require manual evidence before PASS.

Static code inspection cannot establish experiential accessibility PASS.

## 12. Missing data and mutation rules

The prototype must cover:
- referenced product removed;
- product becomes sold out;
- previously selected variant becomes unavailable;
- selected variant changes price;
- compare-at disappears/appears;
- optional media absent;
- long product title;
- 30–50% text expansion;
- two steps and five steps.

Behavior:
- never leave an empty card shell solely because a reference broke;
- never retain stale total/add eligibility after a state mutation;
- never show merchant/editor diagnostics in storefront simulation;
- preserve a coherent ordered story when one commerce reference disappears.

## 13. Merchant configuration boundary

Normal merchant configuration remains shallow:
1. choose Split Tension;
2. author shared editorial content;
3. add 2–5 Guided Set steps;
4. select a product for each step;
5. optionally add short explanatory copy/media;
6. choose bounded color scheme/density.

Not allowed as rescue controls:
- x/y positions;
- arbitrary widths;
- custom breakpoints;
- per-card CSS;
- per-device duplicate content;
- merchant-authored variant logic;
- merchant-authored prices/availability;
- rules for bundle discounts;
- manual mobile ordering separate from semantic step order.

If the prototype needs those controls, redesign or fail the composition.

## 14. Performance and lifecycle threats

Prototype/production direction:
- server-render initial step content;
- no framework/runtime;
- no carousel dependency;
- no eager media for every step;
- no duplicate mobile/desktop DOM solely for layout;
- scope JS to the rendered Split Tension instance;
- later production implementation must support Shopify section load/unload/re-render without duplicate listeners or stale requests;
- stale async responses must not overwrite newer shopper selections;
- do not fetch product data repeatedly if the required variant state is already safely serialized/rendered.

Measured performance remains a later evidence gate.

## 15. Required prototype fixtures

The Split Tension executable prototype may not be called complete without all of these fixtures:

1. **2-step simple** — two single-variant available products.
2. **5-step maximum** — long realistic titles/copy; mobile stress.
3. **Multi-option unresolved** — at least one product requiring explicit option resolution.
4. **Variant sold out** — one option combination unavailable.
5. **Product sold out** — whole step unavailable.
6. **Missing product** — broken reference with coherent reflow.
7. **Mixed eligibility** — eligible + unresolved + link-only in one set.
8. **Selling-plan-sensitive** — excluded safely from aggregate add.
9. **Price mutation** — selection changes current price and total truthfully.
10. **Long/localized copy** — 30–50% expansion.
11. **Neutral originality torture** — neutral palette/system type/ordinary packshots/non-vertical language.
12. **No-JS** — useful ordered product discovery with no dead enhanced controls.
13. **Request failure** — cart operation error retains selections and exposes recovery.
14. **Partial/ambiguous response simulation** — must not falsely report complete success.

## 16. Acceptance tests

### Commerce correctness
- [ ] No unresolved product can enter the aggregate total or Add selected payload.
- [ ] No unavailable variant can enter the payload.
- [ ] Changing an option invalidates stale price/availability/eligibility synchronously.
- [ ] Total equals only current included resolved eligible variants.
- [ ] Compare-at pricing never creates invented set savings.
- [ ] Selling-plan/app-owned/link-only products are excluded without breaking the story.
- [ ] Missing product leaves no dead commerce control.
- [ ] Request failure/partial ambiguity never yields a false full-success message.

### Mobile/usability
- [ ] Two- and five-step states remain understandable at narrow mobile.
- [ ] Product title, price/state, options, inclusion, and safe action remain legible.
- [ ] No miniaturized desktop strip or clipped essential content.
- [ ] 44px internal touch target rule holds.
- [ ] Long copy and 30–50% expansion do not collide.

### Accessibility
- [ ] Keyboard-only operation covers every enhanced control.
- [ ] State is not conveyed by color alone.
- [ ] Names/roles/states are correct.
- [ ] Pending/success/error messaging is announced.
- [ ] Focus remains predictable through option changes and errors.
- [ ] Zoom/reflow, VoiceOver, NVDA, reduced motion and representative touch testing remain NARROW until manually evidenced.

### Progressive enhancement
- [ ] Useful product discovery exists with JS disabled.
- [ ] Enhanced controls are not exposed as dead controls before initialization.
- [ ] JS failure after initial render does not erase server-rendered product/story content.

### Originality/product quality
- [ ] Neutral fixture still reads as Split Tension rather than a generic product list.
- [ ] Ordinary packshots do not require merchant layout rescue.
- [ ] The composition remains guided merchandising rather than a bundle-builder imitation.
- [ ] The normal merchant path stays bounded and shallow.

## 17. Prototype implementation boundary

When this contract is approved, Codex may implement **only** an isolated Split Tension M1 validation harness under:

`prototypes/living-canvas/split-tension/`

It must not:
- add production `sections/`, `blocks/`, `templates/`, `config/`, `locales/`, `layout/`, or production assets;
- import Skeleton/Dawn/Horizon;
- implement other Living Canvas variants;
- start M2;
- claim Shopify/browser/AT/performance PASS without evidence.

Before coding, the implementation brief must convert this contract into exact files, fixtures, interaction rules, test commands, and PASS/NARROW/FAIL reporting.

## 18. Decision rule after prototype

**PASS:** truthful complex-variant behavior, useful no-JS path, comprehensible five-step mobile state, bounded merchant model, and no false cart semantics are evidenced.

**NARROW:** the composition remains valuable but aggregate add or complex inline variant selection must be reduced (for example, link-only for complex products or per-step native add).

**FAIL:** the signature depends on bundle/app semantics, silent defaults, excessive merchant configuration, inaccessible interaction, misleading totals/cart results, or a mobile experience too complex to remain premium and usable.

Do not rescue a FAIL with more settings or more JavaScript.
