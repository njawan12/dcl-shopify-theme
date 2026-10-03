# M0 closure matrix — 2026-10-03

## Purpose

This is the controlling finite checklist for closing M0. It reconciles the roadmap, market research, product opportunity, requirements, support risks, and the dated live evidence added in PR #7. No new M0 research task should be added unless it is required to resolve one of these gates or a newly discovered Shopify requirement.

## Gate matrix

| Gate | Required evidence | Current status | Can AI/DCL desk research close it? | Blocking next action |
|---|---|---|---|---|
| G1 Current official Shopify requirements | dated official-source snapshot; mandatory unknowns resolved enough for M1 | **PASS FOR M0 WITH REVALIDATION OBLIGATION** — refreshed 2026-10-03 against current official Shopify docs | Mostly yes | revalidate at documented future milestones |
| G2 Current competitor commercial facts | dated price/review/preset/position snapshot | SUBSTANTIALLY COMPLETE in PR #7 | Yes | normalize final dated table/workbook |
| G3 Review evidence | ≥50 recent reviews across sample, systematically coded with positive/counter-evidence and friction | **PASS WITH LIMITATION** — 50 official reviews coded; two Pipeline observations older due sparse current accessible reviews | Yes | reopen only under documented triggers |
| G4 Incumbent capability challenge | current public evidence plus hands-on editor evidence where legitimately accessible; surviving system hypotheses must withstand strong-incumbent challenge | **PARTIAL — PUBLIC CHALLENGE COMPLETE**; feature-presence differentiation rejected; H1 structural flexibility, H2 agency-informed controls, H3 visual system + clean implementation survive as hypotheses | Partly | do not infer editor limitations from listings; hands-on editor evidence remains required for claims about configuration depth |
| G5 Operator / merchant problem evidence | Founder/operator evidence from repeated DCL client work plus independent merchant evidence where practical; distinguish evidence types; validate recurring customization demand without fabricating equivalence | **PARTIAL — FOUNDER/OPERATOR EVIDENCE + 15-PATTERN HISTORICAL INVENTORY CAPTURED**; routine launch-pain premise contradicted; recurring flexibility/customization demand strongly reported and categorized | Partly | historical inventory complete; challenge highest-value patterns against strong incumbents; collect independent merchant evidence opportunistically |
| G6 Product/positioning coherence | one target, positioning and vertical strategy; explicit non-targets/unknowns | PROVISIONAL/PASS | Yes + founder | final reconcile after G3–G5 |
| G7 Commercial/support commitment | founder accepts exclusivity, support/bug-fix duty, docs/contact plan, demo investment; named product/design/engineering/QA/support ownership; SLA/maintenance capacity | **PARTIAL — OPERATING MODEL ACCEPTED 2026-10-03**: founder explicitly committed DCL to a real Beauty/Wellness-first Theme Store product business, Theme Store exclusivity, ongoing maintenance/QA, proper demo content, documentation and merchant support meeting Shopify requirements. Product owner/final product decision owner: **Nouman Javaid (founder), confirmed 2026-10-03**. Visual design/art direction owners: **Nouman Javaid + ChatGPT**, confirmed 2026-10-03; ChatGPT serves as design/product-system partner and Nouman retains human final approval. Engineering/code-quality ownership: **ChatGPT as technical architect/reviewer + Codex as implementation engineer**, confirmed 2026-10-03; Nouman retains approval over major product decisions. QA and support ownership/capacity details remain to be named. | No — founder decision | record named ownership/capacity before release; this does not block M1 product/design validation if responsibilities are explicitly carried as a pre-M2/release gate |
| G8 M0 go/no-go | revised thesis survives historical customization inventory and incumbent challenge; requirements revalidated; product/support ownership committed; no unresolved blocking originality/compliance risk | OPEN | No — depends on G1–G7 | formal founder review after finite evidence tasks complete |

## Stop rule

M0 research stops when G1–G7 have enough evidence to make G8. We do **not** continue collecting competitor anecdotes for confidence theater.

## What AI should finish before asking founder for participant work

1. Complete the systematic 50-review evidence set with balanced positive/counter/friction sampling.
2. Normalize the current competitor listing snapshot.
3. Prepare the controlled competitor task protocol and evidence sheet.
4. Refresh the remaining M0-relevant official Shopify unknowns.
5. Prepare a fixed merchant interview script, recruitment criteria, coding sheet and pass/fail rubric.

After those are ready, the project reaches a genuine human-evidence dependency: real competitor task interaction where access permits, real operator/merchant evidence where practical, and founder commercial decisions.

## M0 operator / merchant evidence rule

Do not fabricate, infer, or have AI role-play merchant evidence. Founder/operator evidence from repeated DCL work may inform the product thesis, but must be labeled as such and must not be represented as ten independent merchant interviews. Independent merchant evidence remains valuable and should be captured when practical. Historical DCL work may be used for a customization-demand inventory when the request and outcome can be reconstructed honestly.

## M0 teardown evidence rule

A competitor gap is not accepted because its listing omits a claim. It must survive a controlled task attempt. For each theme/task record:

- exact theme/preset and date;
- device/viewport;
- starting state;
- task goal;
- available starting template/composition;
- consequential choices required;
- section/template switching;
- custom-code/support dependency if encountered;
- mobile recovery behavior;
- cross-surface reuse/handoff behavior;
- completion outcome and evidence;
- uncertainty/access limitation.

At least three gaps must remain defensible after strong-incumbent testing.

## M0 founder decision rule

Founder decisions are not delegated to AI. AI can provide the evidence and recommendation framework, but M0 closes only when the founder explicitly accepts/rejects:

- target customer and non-targets;
- Beauty & Wellness-first vs broader launch scope;
- Theme Store exclusivity;
- ongoing support/bug-fix obligation;
- public docs/contact operation;
- product/design/engineering/QA/support owners;
- support SLA and customization/app-conflict boundaries;
- annual maintenance/QA budget;
- demo content budget;
- build / narrow / stop decision.

## Explicit non-M0 work

Do not use M0 as an excuse to start:

- production Liquid/CSS/JS/JSON;
- Skeleton import/scaffold;
- production sections/blocks;
- final presets;
- M2 foundation.

M1 prototype/product-definition work begins only after G8 authorizes it. The controlling revised thesis is documented in `m0-product-thesis-reconciliation-2026-10-03.md`.
