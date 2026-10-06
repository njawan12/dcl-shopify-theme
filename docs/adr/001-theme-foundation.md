# ADR-001: Production theme foundation

- **Status:** Accepted; final post-M1 architecture decision.
- **Decision/check date:** 2026-10-05.
- **Decision owners:** Product and engineering; engineering owns implementation.
- **Decision:** **B — fully original Shopify theme foundation.** No upstream theme source is imported or pinned for production.
- **Accepted baseline:** M1 `da7da33153648575f53bcf088d32dd7bedc1ceea`, twelve requirements PASS; JS-OFF-01 Actions run `37381586532`.
- **Companion controls:** [Official-source refresh](../post-m1-foundation-revalidation-2026-10-05.md), [M2 entry checklist](../m2-production-entry-checklist.md), [engineering standard](../engineering-compliance-standard.md), [performance budget](../performance-budget.md).

This replaces the 2 October conditional Skeleton recommendation. The decision is final for M2 entry, subject to the explicit revalidation triggers below. It authorizes a subsequent production implementation task; this change contains no production theme files. M1 remains closed and does not certify production Shopify compliance.

## Current official evidence

Shopify permits Skeleton or fully original starting foundations; new Dawn/Horizon-derived submissions are excluded. Originality is evaluated structurally across the experience, not established by authorship alone. Checked **2026-10-05**, [Theme Store uniqueness requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#2-uniqueness-from-other-themes).

The [official Skeleton repository](https://github.com/Shopify/skeleton-theme) is active, not archived. Both current main and the latest published stable release were considered. These identities are audit references, **not production pins**:

| Candidate | Exact inspected identity | Finding and disposition |
|---|---|---|
| Current `main` | `a7a655e79b21e68316c228dc7e437b0b32550888`, committed 2026-10-01 | [Pinned README](https://github.com/Shopify/skeleton-theme/blob/a7a655e79b21e68316c228dc7e437b0b32550888/README.md) describes direct block composition without JSON templates/sections and feature-gated partial rendering. Unsuitable for our generally available section/editor build. Excluded without declaring all Skeleton ineligible. |
| Latest published stable `v1.0.0` | `8b8a1f4d2ef437d4d60df7a9cc4770f85a2f1b76`, published 2025-05-20; latest stable on check date | [Release](https://github.com/Shopify/skeleton-theme/releases/tag/v1.0.0), [pinned tree](https://github.com/Shopify/skeleton-theme/tree/8b8a1f4d2ef437d4d60df7a9cc4770f85a2f1b76). Conventional JSON/section-group scaffold makes this a credible eligible alternative. Its small reusable shell does not justify adopting and replacing its product-system scaffolding here. |

Official source status is not assurance that a snapshot satisfies every submission rule as shipped. Approval of a foundation does not waive the [public theme architecture](https://shopify.dev/docs/storefronts/themes/architecture). Current main's changed dialect and stable's conventional scaffold are treated separately.

Stable inspection covered its **53-file path manifest** and decision-bearing layout, image, metadata, font-variable, CSS, group/text block, header, product, cart, schema, locale, template/group, license and CI files. This was targeted source review, not executed storefront certification:

- `sections/product.liquid` provides a basic native form/variant select, not a product block/app architecture, selling-plan system or complete accessible labeled purchase/state treatment.
- `sections/cart.liquid` supplies basic update/checkout plumbing, not the accepted line-identity, allocation/plan/discount contract.
- `sections/header.liquid` is starter navigation/account-link markup, not the current account-component/responsive/editor implementation.
- `blocks/group.liquid` exposes layout direction/alignment/padding and general theme blocks: a broader composition model than our shallow semantic controls.
- Layout, image/font/metadata snippets and critical CSS are useful references but need our landmarks, tokens, media policy, translations, truth and lifecycle checks. No complete reusable focus/interaction system was established.

The previous ADR overstated Skeleton's provision of solved dialogs, focus traps and commerce correctness. That premise is not used for this decision.

## Actual alternative comparison

These are product-specific judgments, not measured implementation-speed or production-performance comparisons.

| Driver | Pinned stable Skeleton | Fully original — selected |
|---|---|---|
| Theme Store eligibility | Approved foundation route; submission still needs validation | Approved route; maintain authorship/provenance evidence |
| Originality risk | Manageable ceiling, but starter groups/tokens/compositions need removal | No starter composition inheritance; convergence remains a review risk |
| Speed | Small shell advantage; no demonstrated turnkey commerce/accessibility system | Author shell once; avoid import/remove/rewrite reconciliation. Full commerce work required either way |
| Maintainability | Pin/diff/retained-file ownership and selective upstream review | One owned implementation and explicit public-platform updates |
| Merchant editor | Useful stable groups, but generic grouping/product schema must change | Bounded section-local semantic blocks and reusable snippets |
| Accessibility | Native starter markup is not certification; inspected forms need work | Semantic baseline authored/tested from first commit; AT/zoom still mandatory |
| Performance | Minimal starter, no demonstrated production advantage | Route-scoped assets and internal budgets; real measurements still required |
| App compatibility | Add/test real hosts and lifecycle | Same work with deliberate generic guest boundary |
| Future Shopify compatibility | Official source useful; main shows automatic upgrades are inappropriate | Supported public APIs/changelog review; engineering owns compatibility patches |
| Inherited support burden | Every retained file needs support, license and source lineage | Own theme directly; separately track dependencies/platform components |

**Rejected alternative:** stable Skeleton is a viable route, but we would discard its grouping/settings/token model, header, purchase/cart sections, compositions and demo content, then materially edit the remaining helpers. The limited shell benefit does not offset inheritance reconciliation. This does not claim Skeleton is universally unsuitable, licensing prohibits our Shopify use, or freshly authored files alone prove IP.

## License and provenance

The actual [stable license](https://github.com/Shopify/skeleton-theme/blob/8b8a1f4d2ef437d4d60df7a9cc4770f85a2f1b76/LICENSE.md) and [main license](https://github.com/Shopify/skeleton-theme/blob/a7a655e79b21e68316c228dc7e437b0b32550888/LICENSE.md) is **Shopify-restricted MIT-style, not unmodified SPDX MIT**. Its grant restricts use to Shopify-interoperating themes and applicable Theme Store distribution, and requires retaining notices for copies/substantial portions. Both inspected license blobs have SHA-256 `7d691a206443039bb3737836c6843bca19b82d8d942db285357e4d7d97b9fe89`. GitHub identifies `Other` / `NOASSERTION`; the README badge is not the complete license.

The intended Shopify-only use fits the stated purpose, so license eligibility is not our rejection reason. No Skeleton source/assets are adopted; **no inherited Skeleton license or production source pin applies**. Later dependencies/media/examples still require provenance review.

Production ledger: author, path, source, exact version if applicable, license/notices and modifications. No Dawn/Horizon/competitor theme implementation may be copied or ported. Official API names/protocols and platform-rendered controls are public interfaces, not inherited theme systems. M1 schematic fixtures/media are proof content, not automatically cleared production demo assets. Clear rights/truth before reuse. Required notices must remain correct in supported packaging; notices are distinct from developer promotional credits.

## Inherited versus original boundary

| Layer | Production boundary |
|---|---|
| Skeleton/Dawn/Horizon theme files, assets, styles, scripts, presets, locales, grouping | **None inherited.** Skeleton SHAs are reference-only; no import or upstream merge. |
| Shopify-hosted services/branded controls | Consume supported Liquid objects/forms/routes, media/CDN, account/checkout/Shop controls, editor dispatch and APIs. Shopify owns generated internals. |
| Production shell/tokens/snippets/sections/block schemas/templates/locales/enhancement | Original repository implementation with authorship/tests. No framework or runtime layout dependency. |
| Accepted M1 systems | Preserve semantics, composition contracts, caps and relationships; adapt to real Liquid/resource/editor lifecycles. Do not ship Python proof servers/mock transports/schematic catalog/test app UI. |
| Tools/future dependencies | Separate versions/licenses/notice ledger; tools are not a theme foundation. No indirect theme-source inheritance through libraries. |

## Architectural consequences

When M2 is separately executed, use a distinct `theme/` root in this repository and package only supported theme directories. Keep docs, tests, CI, provenance tooling and preserved prototypes outside the ZIP. JSON resource templates and header/footer groups are the composition spine. Use generally supported storefront Liquid, not main-Skeleton experimental block-call syntax, gated partials or agentic-editor dependencies.

Platform product/variant/line data → shared semantic snippets → bounded editor blocks/sections → JSON compositions → shared tokens. Main/featured product hosts use **section-local semantic blocks plus `@app`**, with snippets for reusable purchase/evidence markup. Do not mix section-local and theme blocks within a host. No generic recursive grouping builder. Theme blocks can be added only through a later justified reuse decision that preserves control budgets; platform availability does not mandate a universal builder. Most main product elements must be separately operable blocks. Custom Liquid is a platform insertion capability, not a new branded positioning control.

Native product/cart pages and forms are baseline. Enhancements share canonical truth and instance-owned state; CSS composes one semantic source. JS requires an interaction reason, native fallback and editor cleanup. Optional app content uses genuine app dispatch and normal-flow containment, not imitation reviews or vendor dependencies.

### Accepted-system preservation

| System | Production invariant |
|---|---|
| Balanced PDP | Commercial default; familiar gallery/purchase hierarchy, same product/variant contract as alternatives. |
| Compact PDP | Bounded media matrix/purchase band; no second commerce engine or new setting vocabulary. |
| Editorial PDP | Signature media/narrative/attached-proof relationship; clear shared purchase path and semantic mobile order. |
| Commerce Mosaic / Anchor Cadence | Encounter/feature/lane/reset rhythm; ordinary media, truthful cards, predictable mobile scanning. No extra variants. |
| Standard Grid | Conventional collection fallback with same cards/data/filters; table stakes. |
| Evidence Rail | Note, Pair, ordered Process; subject → attached proof → qualification/source across PDP/editorial. One remaining process step stays ordered. No credibility assessment or invented evidence. |
| Split Tension / Guided Set | Two–five steps, explicit inclusion, truthful variants, independent product lines; aggregate invents no bundle/discount. Preserve unresolved/error/race/native fallback/isolation contracts. |
| Commerce truth | One native identity across cards/PDPs/Guided/cart; server-authoritative plans/prices/availability/allocations. No fabricated activity, reviews or proof. |
| Merchant controls | Accepted local ceilings/item caps; separate presentation/content/binding/shopper inputs. No coordinates/raw-CSS controls/per-device builder/vertical forks. |

Proof identities/control budgets: [M1 final closure](../m1-final-closure-verdict.md), Batch B `direction.md` / `controls.json`, accepted prototype contracts/findings. Split Tension and Commerce Mosaic remain **PASS TO PRESERVE**. Evidence Rail remains **visual PASS TO PRESERVE / engineering NARROW**; integration requires its own evidence. Monument and Edge Crop remain **NARROW AND HOLD**, reference-only, excluded from implementation authorization.

## Revalidation and remaining gates

Reopen ADR-001 for a changed foundation policy, adoption of theme-source code, supported-platform incompatibility requiring a different foundation, or inability to implement accepted contracts within control/performance architecture. A new Skeleton release does not silently change this decision. Review relevant official requirements at feature milestones and all rules before submission; record date, impact, owner/action.

Live Theme Editor/apps/embeds/dynamic sources/plans/cart/Markets, genuine merchant content/provenance/usability, AT/zoom/RTL, cross-browser/touch, measured performance and full-theme/submission integration remain unexecuted production gates. They are not reopened M1 blockers. Infrastructure unavailable means BLOCKED, never PASS. Apply engineering §15 preflight before production code.

**Unresolved foundation blocker: none.** The [M2 checklist](../m2-production-entry-checklist.md) defines first-commit, incremental and submission obligations.

**M2 AUTHORIZED — BEGIN PRODUCTION THEME IMPLEMENTATION**
