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

## Representative section and block inventory

| Surface/role | Initially visible section controls | Conditional controls | Representative block controls | Default/reveal rule |
|---|---:|---:|---:|---|
| Reveal / campaign hero | 5 | 3 | 4 | media-specific controls appear only when media exists |
| Explain / text-media | 4 | 3 | 5 | alignment/detail controls reveal only after corresponding content is enabled |
| Prove / evidence | 4 | 2 | 5 | source/attribution controls reveal only when evidence is present |
| Compare | 4 | 3 | 5 | comparison-detail controls reveal only after a comparison source is connected |
| Act / CTA | 3 | 2 | 4 | secondary-action controls reveal only when a secondary action is enabled |
| Product purchase core | 5 | 4 | 5 | variant/media/app-specific controls appear only when applicable |
| Collection merchandising | 5 | 3 | 4 | editorial interruption controls reveal only when enabled |
| Editorial story | 4 | 2 | 4 | commerce-reference controls reveal only when a product/collection is attached |

No representative section may exceed 8 initially visible merchant decisions without an explicit M1 redesign decision. No representative block may exceed 6 initially visible controls. Conditional controls must be causally tied to an enabled feature or connected data source; “advanced” dumping grounds do not count as progressive disclosure.

## Applied workflow compositions

| Workflow | Starting composition | Expected merchant decisions before preview-ready |
|---|---|---:|
| Product Launch | Reveal → Explain → Prove → Act + product handoff | ≤10 |
| Paid Landing Page | Reveal → focused Explain/Prove → Act | ≤7 |
| Collection Launch | Reveal → collection merchandising → optional Explain → Act | ≤8 |
| Editorial Story | editorial lead → Explain/Prove → contextual commerce handoff | ≤8 |
| Product Education | Explain → Prove → Compare → Act/product handoff | ≤10 |

The inventory must be exercised in the clickable editor simulation. Record actual sections/blocks/settings touched and compare observed decision counts with these proposed ceilings; do not infer usability from schema counts alone.

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
