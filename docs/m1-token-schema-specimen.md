# M1 token/schema specimen

## Status and purpose

This is a **blocking M1 design specimen**, not production theme schema. It makes the proposed control architecture concrete enough to test merchant decision load, progressive disclosure, cross-vertical reuse, and the no-routine-developer-dependence goal before M2.

## Proposed global token specimen

Global controls are semantic roles, not per-component styling escape hatches.

| Token group | Representative controls | Default | Ceiling |
|---|---|---|---|
| Brand | logo, primary/secondary type roles | neutral system-safe prototype roles | 4 |
| Color roles | background, surface, text, muted text, accent, critical/status | accessible neutral palette | 6 |
| Layout | content width, reading width, section rhythm | medium | 3 |
| Shape | radius role, border treatment | restrained | 2 |
| Motion | reduced/standard motion policy | standard with reduced-motion support | 1 |

Global-token changes must propagate across representative surfaces without section-by-section repair. The prototype records proposed count, observed merchant decisions, and any control requested but intentionally excluded.

### Global control inventory

The global token summary above is only a roll-up. The audit source of truth for global controls is the row-level inventory below.

| Token group | Control | Default | Visibility | Reveal predicate |
|---|---|---|---|---|
| Brand | logo source | merchant logo or text fallback | initial | always |
| Brand | primary type role | system-safe sans | initial | always |
| Brand | secondary type role | inherit primary | initial | always |
| Brand | brand scale | medium | initial | always |
| Color roles | background | neutral light | initial | always |
| Color roles | surface | neutral surface | initial | always |
| Color roles | text | high-contrast dark | initial | always |
| Color roles | muted text | accessible muted dark | initial | always |
| Color roles | accent | restrained brand accent | initial | always |
| Color roles | critical/status | accessible semantic status role | initial | always |
| Layout | content width | medium | initial | always |
| Layout | reading width | narrow/reading | initial | always |
| Layout | section rhythm | medium | initial | always |
| Shape | radius role | restrained | initial | always |
| Shape | border treatment | subtle | initial | always |
| Motion | motion policy | standard with reduced-motion support | initial | always |

Audit rule: the count of controls in this global inventory must exactly reconcile with the ceilings in the token summary table. Any additional global setting introduced during prototyping is a specimen defect until it is added here with a default, visibility classification, and reveal predicate. Prototype instrumentation must record the exact global control names changed so brand-level decisions are auditable alongside section/block decisions.

## Representative section and block inventory

| Surface/role | Initially visible section controls | Conditional controls | Representative block controls | Default/reveal rule |
|---|---:|---:|---:|---|
| Reveal / campaign hero | 6 | 2 | 4 | focal-point and crop controls reveal when the media source field is non-empty; media priority is always visible |
| Explain / text-media | 5 | 2 | 5 | media treatment reveals when media is non-empty; detail density reveals when a key-point or supporting-detail block is enabled |
| Prove / evidence | 4 | 2 | 5 | source label/reference reveal when at least one evidence/claim block has a non-empty claim field |
| Compare | 4 | 3 | 5 | conditional controls use the explicit item/detail/count predicates in the row-level inventory |
| Act / CTA | 3 | 2 | 4 | secondary-action label/destination reveal when the secondary-action toggle is on |
| Product purchase core | 5 | 4 | 5 | conditional controls use explicit variant, media, pickup-location, selling-plan, or app-block presence predicates |
| Collection merchandising | 5 | 3 | 4 | interruption position/source/span reveal when the editorial-interruption toggle is on |
| Editorial story | 4 | 2 | 4 | commerce-reference position/treatment reveal when the reference field contains a product or collection |

No representative section may exceed 8 initially visible merchant decisions without an explicit M1 redesign decision. No representative block may exceed 6 initially visible controls. Conditional controls must be causally tied to an enabled feature, connected data source, or an explicit measurable content-state threshold recorded in this specimen; “advanced” dumping grounds do not count as progressive disclosure.

### Row-level control inventory

The aggregate counts above are only summaries. The audit source of truth is the row-level inventory below; every proposed merchant-facing control is named, assigned a scope, given a default, classified as initially visible or conditional, and tied to an explicit reveal predicate where conditional.

| Surface/role | Scope | Control | Default | Visibility | Reveal predicate |
|---|---|---|---|---|---|
| Reveal / campaign hero | section | content emphasis | product-led | initial | always |
| Reveal / campaign hero | section | media source | product media | initial | always |
| Reveal / campaign hero | section | primary heading source | product title | initial | always |
| Reveal / campaign hero | section | supporting copy source | product description excerpt | initial | always |
| Reveal / campaign hero | section | primary action destination | product | initial | always |
| Reveal / campaign hero | section | media focal point | center | conditional | reveal when the media source field is non-empty |
| Reveal / campaign hero | section | media crop behavior | natural | conditional | reveal when the media source field is non-empty |
| Reveal / campaign hero | section | media priority | normal | initial | always |
| Reveal / campaign hero | block | eyebrow | empty | initial | always |
| Reveal / campaign hero | block | badge | empty | initial | always |
| Reveal / campaign hero | block | secondary copy | empty | initial | always |
| Reveal / campaign hero | block | secondary action | disabled | initial | always |
| Explain / text-media | section | content source | manual/connected | initial | always |
| Explain / text-media | section | media position | auto | initial | always |
| Explain / text-media | section | emphasis | balanced | initial | always |
| Explain / text-media | section | content width | reading | initial | always |
| Explain / text-media | section | alignment | start | initial | always |
| Explain / text-media | section | media treatment | contained | conditional | reveal when the media block/source is non-empty |
| Explain / text-media | section | detail density | standard | conditional | reveal when at least one key-point or supporting-detail block is enabled |
| Explain / text-media | block | heading | empty | initial | always |
| Explain / text-media | block | body | empty | initial | always |
| Explain / text-media | block | media | empty | initial | always |
| Explain / text-media | block | key point | empty | initial | always |
| Explain / text-media | block | action | disabled | initial | always |
| Prove / evidence | section | evidence source | connected/manual | initial | always |
| Prove / evidence | section | evidence type | factual | initial | always |
| Prove / evidence | section | display density | standard | initial | always |
| Prove / evidence | section | attribution position | inline | initial | always |
| Prove / evidence | section | source label | empty | conditional | reveal when at least one evidence/claim block has a non-empty claim field |
| Prove / evidence | section | source URL/reference | empty | conditional | reveal when at least one evidence/claim block has a non-empty claim field |
| Prove / evidence | block | claim | empty | initial | always |
| Prove / evidence | block | supporting detail | empty | initial | always |
| Prove / evidence | block | source | empty | initial | always |
| Prove / evidence | block | qualifier | empty | initial | always |
| Prove / evidence | block | icon/media | empty | initial | always |
| Compare | section | comparison source | connected/manual | initial | always |
| Compare | section | comparison axis | merchant-defined | initial | always |
| Compare | section | emphasis | neutral | initial | always |
| Compare | section | layout | table/list auto | initial | always |
| Compare | section | highlight item | none | conditional | reveal when the comparison contains at least 2 compared items |
| Compare | section | detail density | standard | conditional | reveal when at least one comparison item contains a non-empty qualifier or source/reference value |
| Compare | section | mobile condensation | auto | conditional | reveal when the comparison contains more than 4 comparison rows or more than 3 compared items; prototype mobile checks use the fixed 390 px viewport defined for M1 |
| Compare | block | item label | empty | initial | always |
| Compare | block | value | empty | initial | always |
| Compare | block | qualifier | empty | initial | always |
| Compare | block | source/reference | empty | initial | always |
| Compare | block | emphasis flag | off | initial | always |
| Act / CTA | section | primary action label | context-derived | initial | always |
| Act / CTA | section | primary destination | context-derived | initial | always |
| Act / CTA | section | alignment | context-derived | initial | always |
| Act / CTA | section | secondary action label | empty | conditional | reveal when the secondary-action toggle is on |
| Act / CTA | section | secondary destination | none | conditional | reveal when the secondary-action toggle is on |
| Act / CTA | block | supporting copy | empty | initial | always |
| Act / CTA | block | trust note | empty | initial | always |
| Act / CTA | block | secondary action toggle | off | initial | always |
| Act / CTA | block | app insertion seam | enabled | initial | always |
| Product purchase core | section | media priority | product-first | initial | always |
| Product purchase core | section | purchase information density | standard | initial | always |
| Product purchase core | section | sticky action policy | auto | initial | always |
| Product purchase core | section | supporting content position | after purchase core | initial | always |
| Product purchase core | section | app insertion seam | enabled | initial | always |
| Product purchase core | section | variant display mode | auto | conditional | reveal when the product has more than 1 variant |
| Product purchase core | section | media gallery treatment | auto | conditional | reveal when the product has more than 1 media item |
| Product purchase core | section | pickup display | auto | conditional | reveal when Shopify provides at least 1 pickup-availability location for the selected variant |
| Product purchase core | section | selling-plan/app accommodation | auto | conditional | reveal when the product exposes at least one selling plan or an app block is present in the purchase-core section |
| Product purchase core | block | title | product title | initial | always |
| Product purchase core | block | price/status | product data | initial | always |
| Product purchase core | block | variant selector | auto | initial | always |
| Product purchase core | block | quantity/action | enabled | initial | always |
| Product purchase core | block | supporting facts/app seam | enabled | initial | always |
| Collection merchandising | section | grid density | auto | initial | always |
| Collection merchandising | section | filter presentation | auto | initial | always |
| Collection merchandising | section | sort visibility | shown | initial | always |
| Collection merchandising | section | editorial interruption | off | initial | always |
| Collection merchandising | section | merchandising emphasis | balanced | initial | always |
| Collection merchandising | section | interruption position | after first product row | conditional | reveal when the editorial-interruption toggle is on |
| Collection merchandising | section | interruption source | none | conditional | reveal when the editorial-interruption toggle is on |
| Collection merchandising | section | interruption span | full row | conditional | reveal when the editorial-interruption toggle is on |
| Collection merchandising | block | product card | native product | initial | always |
| Collection merchandising | block | editorial tile | empty | initial | always |
| Collection merchandising | block | collection note | empty | initial | always |
| Collection merchandising | block | app insertion seam | enabled | initial | always |
| Editorial story | section | story source | manual/connected | initial | always |
| Editorial story | section | reading width | reading | initial | always |
| Editorial story | section | media rhythm | auto | initial | always |
| Editorial story | section | commerce reference | none | initial | always |
| Editorial story | section | commerce reference position | contextual | conditional | reveal when the commerce-reference field contains a product or collection |
| Editorial story | section | commerce reference treatment | subtle | conditional | reveal when the commerce-reference field contains a product or collection |
| Editorial story | block | heading | empty | initial | always |
| Editorial story | block | rich text | empty | initial | always |
| Editorial story | block | media | empty | initial | always |
| Editorial story | block | contextual product/collection reference | empty | initial | always |

Audit rule: the summary counts in the first table must equal the number of row-level controls above by surface/role, scope, and visibility classification. Prototype instrumentation must record the exact control names touched so observed behavior can be reconciled directly against this inventory. Any unlisted control used during testing is a specimen defect and blocks M1 until the inventory is corrected and the affected task is retested.

### Mechanical reconciliation procedure

Before requesting review or accepting any specimen change:

1. Count section rows by surface and visibility; each total must exactly equal the corresponding summary-table initial/conditional count.
2. Count block rows by surface; each total must exactly equal the corresponding summary-table block count.
3. Count global rows by token group; each total must exactly equal the token-summary ceiling.
4. Every conditional row must name an observable field, toggle, Shopify object/data presence, or numeric threshold. Subjective predicates fail the audit.
5. Every initial row must use `always` as its reveal predicate.
6. Any reclassification requires updating the row and its roll-up in the same change.

A mismatch fails the specimen audit before external review.

## Applied workflow compositions

| Workflow | Starting composition | Expected merchant decisions before preview-ready |
|---|---|---:|
| Product Launch | Reveal → Explain → Prove → Act + product handoff | ≤10 |
| Paid Landing Page | Reveal → focused Explain/Prove → Act | ≤7 |
| Collection Launch | Reveal → collection merchandising → optional Explain → Act | ≤8 |
| Editorial Story | editorial lead → Explain/Prove → contextual commerce handoff | ≤8 |
| Product Education | Explain → Prove → Compare → Act/product handoff | ≤10 |

The inventory must be exercised in the clickable editor simulation. Record actual sections/blocks/settings touched and compare observed decision counts with these proposed ceilings; do not infer usability from schema counts alone.

## Prototype observability constants

For M1 reproducibility, mobile-state predicates are evaluated at a fixed **390 px CSS viewport width** unless a workflow contract explicitly defines another fixture. Content-state predicates use the explicit field, toggle, object-presence, or count conditions named in the row-level inventory. Prototype authors must not infer control visibility from subjective notions such as “important,” “merchant-relevant,” “applicable,” or “above the fold.”

## Progressive-disclosure rules

1. Show the minimum controls required to produce a coherent default.
2. Reveal dependent controls only after the merchant enables the corresponding capability or connects the relevant data.
3. Prefer semantic choices over raw CSS/layout knobs.
4. Do not solve vertical differences with catch-all “mode” toggles or duplicated schemas.
5. Do not displace complexity into undocumented metafields, code edits, or proprietary tooling.
6. A hidden control still counts toward complexity evidence when merchants routinely need to reveal it.

## Cross-vertical reuse probes

Beauty & Wellness is the deep reference fixture. Apparel and food/beverage must use the same contracts and token roles. A probe fails if it requires a vertical-specific schema fork, vague catch-all controls, a setting-budget exception, or routine developer intervention. Failure triggers ADR-007 narrowing rather than generalized controls.

## No-routine-developer-dependence evidence

For each workflow, capture whether a target merchant can select the correct start, reach a coherent preview-ready state, change global brand roles, connect/disconnect optional structured content, recover from missing data, and resolve the defined mobile state without Liquid/CSS/JavaScript edits or a proprietary tool.

## Blocking M1 evidence

M1 cannot pass and M2 cannot begin unless:
- the specimen and complete setting-count/progressive-disclosure inventory are present and machine-countable;
- representative controls stay within the declared ceilings or are explicitly redesigned and retested;
- global-token changes propagate without local repair;
- all five workflows are exercised against the inventory;
- Beauty & Wellness, apparel, and food/beverage probes demonstrate contract reuse or ADR-007 narrows scope;
- routine supported work requires no developer intervention; and
- observed usability evidence does not reveal displaced complexity that the static inventory missed.

A ceiling breach, missing inventory, propagation failure, schema fork, or routine developer dependence is an independent M1 failure. Originality or usability success elsewhere cannot compensate for it.
