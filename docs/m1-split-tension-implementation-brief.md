# M1 Split Tension — Prototype Implementation Brief

**Date:** 2026-10-03  
**Status:** Draft implementation contract; requires pre-code red-team approval before Codex implementation.  
**Authority:** Must comply with `m1-split-tension-commerce-state-machine.md`, `m1-living-canvas-prebuild-red-team-matrix.md`, `m1-signature-system.md`, and the M1 product architecture contract. If this brief conflicts with the state-machine contract, the state-machine contract wins.

## 1. Named experiment

Build one isolated browser-runnable M1 prototype answering only:

1. Can Split Tension provide truthful guided multi-product commerce across complex variant states without becoming a bundle engine?
2. Can five steps remain premium, understandable and operable on mobile?
3. Does the no-JavaScript path remain commercially useful?
4. Does the composition remain visually recognizable under neutral typography, palette and ordinary packshots?

This is validation code, not production theme development.

## 2. Hard scope boundary

All prototype files live only under:

`prototypes/living-canvas/split-tension/`

Allowed files:
- `index.html`
- `split-tension.css`
- `split-tension.js`
- `fixtures.js`
- `README.md`
- `findings.md`
- `media/` containing only local prototype SVG/image fixtures
- `tests/` containing small dependency-free/static test scripts if useful

Do not create or modify production `sections/`, `blocks/`, `templates/`, `config/`, `locales/`, `layout/`, snippets, or production assets. Do not import Skeleton, Dawn or Horizon. Do not implement Monument, Edge Crop, Quiet Frame, Commerce Mosaic, production cart infrastructure, or M2.

No framework, jQuery, external UI/carousel library, network dependency, package install, build step, remote font, analytics, or third-party request.

## 3. Visual composition contract

Desktop is not a generic equal two-column section.

Use one semantic DOM order:
1. editorial proposition;
2. ordered Guided Set steps;
3. aggregate selection summary/action.

At desktop widths, create **Split Tension** through authored CSS layout:
- editorial zone occupies a strong, intentionally constrained field;
- commerce zone visibly pushes/pulls against it through asymmetrical track proportions and one structural boundary/overlap relationship;
- product cards remain readable and never depend on freeform x/y placement;
- the visual tension is structural CSS, not baked into fixture imagery;
- ordinary white-background packshots must still look intentional.

At tablet, relax overlap before text/options collide.

At narrow mobile, resolve to a vertical ordered sequence of large step cards. Do not use a miniature horizontal desktop strip. No carousel in this prototype.

Neutral torture mode must replace brand color, decorative typography and vertical-specific language while retaining the same layout grammar.

The prototype may use simple local SVG packshots. Artwork must not carry the signature.

## 4. Server-rendered baseline

The literal `index.html` must contain a usable default fixture before JS runs. Do not generate the entire initial experience from JavaScript.

Baseline HTML must include:
- section heading/proposition;
- ordered step markup;
- valid product links;
- truthful fixture price/availability text;
- no aggregate enhanced controls that are dead without JS.

JS may hydrate/enhance that existing structure after successful instance initialization. Initial enhancement must not destroy and recreate authoritative fallback markup merely for convenience.

A deliberate initialization-failure fixture must prove fallback survival.

## 5. Instance architecture

Every Split Tension root uses an instance-scoped identifier. All queries/mutations are rooted to that instance except a justified shared bootstrap.

Requirements:
- support at least two instances in one document;
- no duplicate IDs;
- option group names are instance/step scoped;
- state, totals, messages and pending requests never leak between instances;
- failure in one instance cannot prevent another from initializing;
- no mutable global commerce state.

For prototype simplicity, fixture data may exist in a read-only namespaced object, but runtime shopper state belongs to each instance.

## 6. Fixture commerce data shape

Each product fixture must provide only fields needed to test the contract, using Shopify-shaped semantics:

- product id/handle/title/url;
- image;
- option names/values where applicable;
- variants with id, option tuple, price in integer minor units, optional compare-at minor units, availability;
- optional unit-price display data;
- flags for selling-plan-sensitive, quantity-rule, required-line-properties, app-owned, or link-only;
- fixture-only mutation/error behavior.

Merchant-facing text must be separate from commerce truth.

Never use floating-point money.

## 7. Per-step rendering rules

Render the states defined by the controlling state machine.

### Missing/deleted reference
No dead commerce controls or broken link. Preserve editorial step only when it has meaningful authored content. Never show editor instructions to the shopper.

### Link-only/app-owned/selling-plan-sensitive/quantity-rule/property-required
Show truthful product context and `View product`. Do not show inclusion control. Do not count toward aggregate total.

### Single available variant
Show price/state and an initially **unchecked** inclusion control. Quantity is fixed to 1.

### Multi-option unresolved
Show native labeled option controls and `View product`. Inclusion control remains unavailable until a real available variant is explicitly resolved.

Do not preselect meaningful required options. A placeholder such as “Choose size” is required where appropriate.

### Resolved available
Synchronously update current variant ID, price, compare-at/unit-price context, availability and inclusion eligibility as one state transition.

### Resolved sold out / fully sold out
Truthful sold-out state. Exclude from aggregate purchase. Product link remains.

## 8. Inclusion rules

Eligibility and inclusion are different.

- Initial inclusion is false for every step.
- Shopper explicitly includes an eligible step.
- Included state has visible text/semantic state, not color alone.
- If an included step becomes unresolved or ineligible, clear inclusion and remove its amount immediately.
- Returning to eligibility does not silently restore cleared inclusion.
- Variant changes may preserve inclusion only if the step remains continuously valid and the shopper had explicitly included it.
- Aggregate action is omitted when fewer than two aggregate-eligible steps remain. With two or more eligible steps but none included, show the summary state without implying items are selected.
- Duplicate product/variant references must not create accidental duplicate purchase. Apply the controlling duplicate rule and explain the fixture behavior in `findings.md`.

## 9. Money/summary rules

All fixture prices use integer minor units.

The displayed selected-items total is the exact sum of currently **included + resolved + available + inline-eligible** variants only.

The summary must state:
- number of selected items;
- selected-items total;
- that this is not a checkout total if wording could otherwise imply taxes/shipping/discounts are included.

Never:
- sum unresolved/link-only/sold-out items;
- calculate with binary floating point;
- invent bundle savings;
- aggregate compare-at prices into a “you save” claim.

Option mutation must invalidate stale derived money before rendering the new resolved state.

## 10. Aggregate Add selected simulation

This harness does **not** call Shopify. It simulates the request boundary so state/error handling can be tested without pretending platform semantics are proven.

The Add selected action exists only when at least two steps are aggregate eligible. It is enabled only when at least one eligible step is explicitly included.

Payload model:
- variant id;
- quantity exactly 1;
- no unsupported selling plan or unknown line-item properties.

On submit:
1. validate every included step against current state;
2. if invalid, do not send simulation; expose the first affected step and recovery message;
3. freeze the outgoing payload/version;
4. set that instance to pending;
5. disable payload-mutating controls for that instance;
6. announce a concise pending state.

Fixture-controlled response modes:
- `success`
- `failure`
- `ambiguous`

Success: announce only simulated confirmed success and expose a cart-link placeholder. Do not invent a global cart count.

Failure: retain shopper choices where still valid, announce error, expose retry and product links.

Ambiguous: never say all items were added and never infer item-level success from the outgoing payload. State that the cart result could not be fully confirmed and expose review/retry actions.

A 422/inventory-race fixture must transition from apparently eligible pre-submit state to recoverable request failure.

## 11. Async/race behavior

Every instance maintains a monotonically increasing state version.

- Any option/inclusion mutation increments it.
- Derived total/payload is rebuilt from current state.
- Pending submission captures the version.
- Payload-mutating controls are disabled while pending.
- A stale simulated response whose instance/version is no longer current is ignored.
- Prototype teardown/reinitialization must not allow old callbacks to mutate replacement UI.

Use a deterministic short local timer only to expose pending behavior. No network request.

## 12. Accessibility interaction contract

Use native elements.

- Product navigation: links.
- Inclusion: labeled checkbox.
- Mutually exclusive product options: native radio group or select, chosen according to the fixture; labels required.
- Aggregate action/retry: buttons.
- Status/error: scoped live/status messaging with restrained announcements.

Requirements:
- no clickable div/span;
- visible focus;
- logical DOM/tab order;
- 44 CSS px minimum internal primary target;
- state not color-only;
- option groups programmatically named with product/step context;
- no focus movement on ordinary option change;
- if aggregate submission is blocked, expose an inline error and move focus only to the first invalid control/message when needed;
- pending/success/failure/ambiguous result announced;
- no focus trap;
- no hover-only information;
- reduced motion safe;
- visual DOM rearrangement must not change semantic order.

VoiceOver/NVDA/zoom/touch remain NARROW until manually evidenced.

## 13. Responsive contract

Evidence widths to document/test:
- 320px
- 375px
- 430px
- 768px
- 1024px
- 1280px
- 1440px

At 320–430:
- vertical cards;
- no horizontal page overflow;
- options/actions remain readable;
- five-step fixture is usable;
- aggregate summary does not cover controls.

At 768–1024:
- layout may transition, but no desktop overlap may collide with product options/long text.

At >=1280:
- structural Split Tension must be visually apparent without relying on media art direction.

At 200%/400% zoom/reflow, manual evidence is required before PASS.

## 14. Required 24 fixtures

Implement switchable deterministic fixtures for all controlling cases:

1. 2-step simple.
2. 5-step maximum.
3. Multi-option unresolved.
4. Variant sold out.
5. Product fully sold out.
6. Missing product.
7. Mixed eligibility.
8. Selling-plan-sensitive.
9. Price mutation.
10. Long/localized copy.
11. Neutral originality torture.
12. No-JS baseline.
13. Request failure.
14. Partial/ambiguous response.
15. Explicit inclusion default.
16. Quantity-rule product.
17. Duplicate reference.
18. Two instances.
19. Initialization failure.
20. Inventory race / simulated 422.
21. All inline-ineligible.
22. One surviving valid step.
23. Money precision/context.
24. Required line-item properties.

Fixtures may reuse product records but each must isolate the named risk. Fixture diagnostics belong to the harness controls, not the storefront simulation.

## 15. Fixture selector / harness controls

Provide a compact prototype header outside the simulated storefront with:
- fixture selector;
- current fixture label;
- concise diagnostic text where needed;
- explicit “Simulate JavaScript failure” only if required to exercise fixture 19 without corrupting the baseline.

Harness controls are test instrumentation and must be visually/seman­tically separate from storefront UI.

URL query parameter may identify a fixture for reproducibility.

## 16. Progressive enhancement and no-JS test

`README.md` must document how to run via a simple local static server and how to test with JS disabled.

No-JS acceptance:
- editorial proposition visible;
- ordered steps visible;
- valid product links work;
- truthful baseline product context visible;
- no dead aggregate/inclusion/variant controls presented as functional;
- no content requires JS merely to become visible.

The no-JS fixture is not permission to duplicate semantic content.

## 17. Performance constraints

Prototype:
- local assets only;
- no framework/dependency/build step;
- no autoplay/video;
- no carousel;
- no JS layout measurement for the signature;
- CSS owns composition;
- images include intrinsic dimensions;
- below-first-view product media may be lazy where appropriate;
- no duplicate desktop/mobile semantic DOM.

Do not claim a Lighthouse/performance PASS without measurement.

## 18. Security/robustness constraints

- fixture strings enter DOM via safe text APIs when JS-rendered;
- do not inject fixture text through `innerHTML`;
- no `eval`, dynamic code generation, or scriptable merchant URL field;
- fixture product URLs are root-relative `/products/...`;
- initialization is idempotent;
- event listeners/timers are cleaned up on prototype teardown/reinit;
- one broken fixture/instance must not crash all instances.

## 19. Required self-audit

Before completion, inspect the whole implementation against:
1. this brief;
2. the complete state-machine contract, including red-team corrections;
3. Living Canvas cross-composition invariants.

Do not audit only changed lines.

`findings.md` must contain a requirement-by-requirement evidence table with **PASS / NARROW / FAIL / NOT TESTED**.

Rules:
- static/code evidence may support logic/structure PASS;
- browser visual behavior cannot be PASS without browser rendering evidence;
- VoiceOver/NVDA/physical touch/zoom cannot be PASS without manual evidence;
- Shopify Cart API atomicity cannot be PASS from this harness;
- real Shopify selling-plan/Markets/app behavior cannot be PASS from fixtures;
- performance cannot be PASS without measurement.

Any unmet hard requirement is explicit.

## 20. Required automated/static checks

At minimum run and record:
- `node --check prototypes/living-canvas/split-tension/fixtures.js`
- `node --check prototypes/living-canvas/split-tension/split-tension.js`
- `git diff --check`
- static assertions proving all 24 fixtures exist;
- no production directories/files changed by this task;
- no forbidden dependency/import/network URL;
- no `innerHTML`/eval;
- root-relative modeled product URLs;
- initial default inclusion false;
- integer money data;
- two-instance fixture exists;
- initialization-failure fixture exists;
- failure/ambiguous/422 fixtures exist.

If a browser runtime is available, also test the required widths and record screenshots/evidence. If unavailable, mark those visual items NARROW/NOT TESTED rather than inferring PASS.

## 21. Stop conditions

Stop and report rather than silently redesign if:
- truthful aggregate add requires bundle semantics;
- variant selection requires full PDP architecture;
- mobile five-step state cannot remain understandable without a complex custom widget;
- visual identity only survives with art-directed photography/type/color;
- duplicate/missing/ineligible states require merchant rescue settings;
- accessibility requires non-native interaction complexity;
- implementation starts needing a framework or large runtime;
- any requirement conflicts materially with the controlling state-machine contract.

Do not weaken acceptance criteria to make the experiment pass.

## 22. Completion output

A completed Codex task must report:
- exact files added/changed;
- commit SHA;
- tests run and outcomes;
- PASS/NARROW/FAIL experimental recommendation;
- every untested evidence category;
- every deviation from this brief;
- confirmation that no production theme code or other Living Canvas variant was touched.

Do not create or merge a PR unless explicitly instructed after review.
