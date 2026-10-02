# M1 conventional versus distinctive boundaries

## Purpose

Originality is an overall system property, not a requirement to make every control unfamiliar. This boundary prevents bespoke engineering from weakening accessibility, commerce correctness, performance, and maintainability while forcing product-level differentiation where the merchant and shopper can actually experience it.

## Conventional primitives we should not reinvent

Use current Shopify-native contracts, semantic HTML, platform data, and well-understood accessible patterns. “Conventional” does not mean untested or copied from a competitor.

| Primitive | Preserve | Product freedom |
|---|---|---|
| Navigation | Links navigate; buttons disclose; keyboard, focus, Escape, current state, and mobile depth are predictable | Calm information architecture, brand plane, and bounded promotional content |
| Search | Native predictive-search semantics/fallbacks, query URLs, empty/error/loading states | Result hierarchy and visual integration |
| Product form | Shopify variant IDs, availability, quantity, selling-plan/app and error semantics; server-valid submission | Placement within a factual purchase core and narrative handoff |
| Option/quantity controls | Labels, selected/disabled state, native values, keyboard/touch operability, text fallback | Constrained presentation tokens; never infer inaccessible color meaning |
| Price and status | Accurate price, compare-at, unit price, tax/availability context and legitimate inventory data | Fact-rail hierarchy |
| Media gallery | Correct images/video/3D, alternatives, controls, focus, responsive sizes, intrinsic space | Chapter pacing and mobile media reduction |
| Cart | Accurate add/update/remove, errors, totals, properties, discounts and accessible announcements | Quiet hierarchy; subordinate extensions |
| Collection browsing | Canonical product set, filters, sort, pagination/URLs, result counts and no-JS behavior | Clearly non-product editorial rhythm that cannot corrupt counts |
| Dialogs/drawers/popovers/disclosures | Native semantics where suitable; focus management, Escape, restoration, names/roles/states | Whether a disclosure is appropriate; bounded visual treatment |
| Localization and Markets | Locale strings, currency/market context, long-text resilience, logical layout | Voice and content defaults within translatable contracts |
| Images/performance | Shopify CDN transforms, responsive images, dimensions, justified loading priority | Art-direction slots and section priority rules |
| Accessibility | Semantic order, labels, headings, contrast, reflow, reduced motion, touch targets, announcements | Inclusive composition choices that exceed a numeric score |
| App blocks | Current `@app` contract and generic, non-destructive wrappers | Deliberate insertion seams and hierarchy |
| Theme editor lifecycle | Native add/remove/reorder/select/re-render behavior with cleanup | Merchant-facing workflow defaults and semantic controls |
| Standard resources | Required templates and platform-native objects | The smallest intentional composition for each resource |

These primitives may be authored by DCL or retained from the audited Skeleton boundary under ADR-001. They must never be copied from a competitor theme.

## Product-level systems where we must be distinctive

### 1. Job-first starting state

The merchant chooses a recurring commercial job and receives a smallest-useful native composition with deliberate omissions, content prompts, mobile priorities, and a clear destination. Difference must be measured against blank/default assembly, not asserted from preset names.

### 2. Cross-surface argument handoff

A campaign promise, collection orientation, and product explanation form one governed decision path. Each surface answers the next shopper question in its native role rather than repeating identical modules. This continuity is the primary architectural claim.

### 3. Narrow section responsibility system

Every section owns one shopper question and CTA relationship. Supported-surface matrices and block limits prevent the usual drift toward “image/text/everything” sections. Reuse is semantic, not merely visual.

### 4. Priority-transforming mobile behavior

Mobile contracts specify promotion, condensation, deferral, and omission of content. Purchase and navigation clarity can override desktop storytelling. Merchants do not manage a second mobile page or dozens of breakpoint settings.

### 5. Standard-data polish and structured enhancement

The same contracts produce a complete experience from ordinary Shopify objects, then accept optional structured evidence without changing architecture. The distinction is in graceful composition and reuse, not in owning a proprietary CMS.

### 6. Merchant decision economy

Semantic choices—shopper emphasis, density, evidence type, destination—replace implementation controls. Each workflow has a measured decision budget. More flexibility is a cost; controls exist only when target merchants understand the consequence and the output remains supportable.

### 7. Merchandising relationships

Editorial interruptions, claims, proof, comparisons, and product destinations have explicit relationships. Non-products never impersonate product cards, evidence is not fabricated, and comparisons appear only with honest data.

### 8. Constrained defaults as product behavior

Defaults determine order, omission, media priority, empty-state behavior, and action clarity. They are tested artifacts, not demo decoration. Adding a section should create a coherent state before configuration.

## Decision test for every proposed feature

1. Is this required for platform, commerce, accessibility, or content correctness? If yes, use the conventional contract.
2. Is it a merchant-visible decision central to one of the five jobs? If no, do not expose it merely for flexibility.
3. Does an existing narrow section answer the same shopper question? Reuse it only if its data and surface contract remain intact.
4. Does the feature strengthen job-first setup, argument handoff, mobile priority, standard-data polish, or decision economy? If none, it is not an originality investment.
5. Can Shopify-native templates, sections, blocks, presets, settings, and dynamic sources express it? If not, reject it unless a later ADR proves a supported need; do not create a proprietary builder.
6. Does the proposal add an app dependency, fabricated claim, inaccessible novelty, avoidable payload, or support-heavy combination? Reject it.

## Anti-patterns

- custom carousels, selectors, dialogs, or product forms whose only novelty is interaction;
- one section with every layout, content type, and breakpoint setting;
- one template for every campaign permutation;
- vertical-mode switches that silently change behavior;
- mandatory metafield setup to make defaults look finished;
- copying a competitor's section taxonomy and applying new styling;
- exposing pixel values, arbitrary CSS, animation menus, or mobile duplicate content as “creative control”;
- app-specific workflow ownership;
- claiming originality from terminology, section count, theme blocks, presets, or JSON order.

## Gate

Conventional primitives may look familiar in isolation. The assembled stripped system must still demonstrate at least three verified workflow gaps against the named competitors and materially improve merchant completion, time, decisions, and comprehension. If it does not, the answer is not more custom primitives; the product architecture must be narrowed or rejected.
