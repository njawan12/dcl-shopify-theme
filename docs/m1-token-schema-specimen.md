# M1 control-budget specimen

## Status and purpose

This supersedes the old workflow/token specimen. It is a blocking design-control budget, not production Shopify schema.

The goal is to prove that high-value structural flexibility can be exposed without replacing developer complexity with merchant settings complexity.

## Control taxonomy

Every merchant-facing control belongs to exactly one layer:

1. Global semantic token — brand/system decision that should propagate.
2. Surface structural variant — materially different composition owned by one high-value surface.
3. Block composition/order — merchant-meaningful content/function units.
4. Dynamic content/product data — Shopify object data or optional connected source.
5. Bounded local presentation — a small local choice whose consequence is clear.
6. Developer extension point — deliberately not merchant-configurable.

A control is rejected if its primary justification is "more flexibility."

## Global token budget

| Group | Proposed controls | Initial ceiling |
|---|---|---:|
| Typography | display role; heading role; body role; scale | 4 |
| Color | background; surface; text; muted text; accent; status | 6 |
| Layout | content width; reading width; section rhythm | 3 |
| Shape | radius role; border treatment | 2 |
| Controls | button shape/emphasis policy | 2 |
| Media | default media treatment | 1 |
| Motion | motion policy with reduced-motion support | 1 |

Initial global ceiling: 19 controls. This is a prototype ceiling, not a requirement to expose all 19.

## Surface budgets

These count structural/presentation decisions, not ordinary content fields.

| Surface | Initial decisions | Conditional | Structural variants |
|---|---:|---:|---:|
| PDP purchase area | ≤6 | ≤4 | 3 |
| Product media | ≤5 | ≤3 | 3 |
| Product education | ≤5 | ≤3 | ≤3 per narrow family |
| Cart | ≤5 | ≤3 | 2–3 |
| Storytelling/content | ≤6 | ≤3 | ≤3 per primitive family |
| Product card / collection support | ≤5 | ≤3 | 2–3 |

Exceeding a ceiling is a redesign event, not permission to create an "advanced" drawer.

## S1 — PDP purchase area

Initial decisions: purchase composition; supporting-information density; option presentation; action emphasis; sticky mobile purchase action; supporting-content placement.

Conditional: selling-plan treatment only when plans exist; pickup treatment only when pickup data exists; secondary support action only when enabled; app-area treatment only when an app block exists.

Prototype structural variants:
- Balanced — conventional facts/options/action hierarchy.
- Compact — denser facts/action composition for simple focused catalogs.
- Editorial — correct purchase core with supporting product story/facts composed around it.

Variants must differ structurally, not merely by alignment.

Commerce invariant: product identity, price/status, option selection, quantity where supported, selling-plan truth, availability/errors and add-to-cart semantics cannot change meaning between variants.

## S2 — Product media

Initial decisions: media composition; first-media emphasis; thumbnail/navigation treatment; media-fit policy; product-badge treatment.

Conditional: video behavior when video exists; zoom/lightbox when eligible media exists; badge placement alternative when a badge exists.

Prototype variants: gallery; editorial stack; focused lead + supporting media.

No separate merchant breakpoint layout builder.

## S3 — Product education

This is a family of narrow sections, not one mega-section: benefits/features; ingredients/materials/specifications; usage/process; FAQ/disclosure; comparison; proof/results/app host.

Common initial decisions stay within five: presentation variant; density; alignment where meaningful; media relationship where meaningful; section emphasis.

Conditional controls reveal only when corresponding media/data/block types exist. Raw width, grid-column, breakpoint, animation and arbitrary CSS fields are prohibited in normal merchant UX.

## S4 — Cart

Initial decisions: cart presentation; item density; complementary-merchandising placement; factual progress-message visibility; checkout-action emphasis.

Conditional: configured progress threshold/content only when factual progress is enabled; note treatment only when notes are enabled; app/extension spacing only when an extension exists.

Structural variants must not fork cart business logic.

## S5 — Storytelling/content

Each section family gets one content responsibility. Candidate local decisions: composition; density; media relationship; alignment; emphasis; action treatment. Maximum six initial structural/presentation decisions.

Content blocks repeat only when the semantic unit is genuinely repeatable. Maximums are set per family during prototype design.

## Product card / collection support

Initial candidates: card composition; media treatment; secondary-media behavior; quick-action policy; information density.

Collection filtering/sorting/pagination are platform behavior, not design-system experimentation.

## Progressive disclosure rules

1. Conditional controls depend on an observable capability, connected source, object state or block presence.
2. No "advanced" bucket.
3. Hidden controls still count in complexity.
4. Mobile-only controls require exceptional justification; prefer governed responsive behavior.
5. A structural variant should absorb a coherent group of decisions when separate controls create invalid combinations.
6. Global tokens own global styling.
7. Dynamic sources change content, not architecture.

## Setting rejection test

Reject or move developer-only when a control is a raw CSS value; breakpoint implementation detail; creates many invalid combinations; lacks repeated need; duplicates a global token; should be owned by a structural variant; exists to imitate competitor feature count; or costs more to support/test than its plausible merchant value.

## Three-composition audit

For each Beauty/Wellness direction record structural variants selected, blocks changed, global tokens changed, dynamic sources connected, local settings touched and unsupported requests requiring developer extension.

The goal is not zero developer extension. It is materially larger supported design range than a single demo skin without settings explosion.

## Merchant-operability audit

A configured composition passes only if an operator can update content/product data, connect/disconnect supported sources, choose supported variants, reorder permitted blocks, change global brand roles, recover from missing optional data, and understand governed mobile behavior without source edits.

## Developer-extension audit

At least two extension exercises document files/contracts touched and regression surface. If a justified variant requires changes across unrelated sections, global CSS hacks or shared JS state, the architecture fails.

## Blocking rule

M2 remains blocked if budgets cannot be reconciled; variants are cosmetic; merchant range requires arbitrary CSS/breakpoint controls; a universal catch-all emerges; zero-setup is not premium; supported merchant operations routinely require code; or developer extension is brittle.
