# M0 closure matrix — 2026-10-03

## Purpose

This is the controlling finite checklist for closing M0. It reconciles the roadmap, market research, product opportunity, requirements, support risks, and the dated live evidence added in PR #7. No new M0 research task should be added unless it is required to resolve one of these gates or a newly discovered Shopify requirement.

## Gate matrix

| Gate | Required evidence | Current status | Can AI/DCL desk research close it? | Blocking next action |
|---|---|---|---|---|
| G1 Current official Shopify requirements | dated official-source snapshot; mandatory unknowns resolved enough for M1 | **PASS FOR M0 WITH REVALIDATION OBLIGATION** — refreshed 2026-10-03 against current official Shopify docs | Mostly yes | revalidate at documented future milestones |
| G2 Current competitor commercial facts | dated price/review/preset/position snapshot | SUBSTANTIALLY COMPLETE in PR #7 | Yes | normalize final dated table/workbook |
| G3 Review evidence | ≥50 recent reviews across sample, systematically coded with positive/counter-evidence and friction | **PASS WITH LIMITATION** — 50 official reviews coded; two Pipeline observations older due sparse current accessible reviews | Yes | reopen only under documented triggers |
| G4 Competitor task teardown | live phone + desktop task-based teardown; ≥3 defensible workflow gaps | OPEN; public listing teardown only | Partly | hands-on live demo task execution and evidence capture |
| G5 Merchant interviews | 8–12 structured interviews; ≥8 target merchants; majority Beauty & Wellness; ≥3 adjacent-vertical participants; repeated launch/PDP pain; concept understandable enough to prototype | OPEN | **No** — requires real merchants | recruit/interview participants using fixed script |
| G6 Product/positioning coherence | one target, positioning and vertical strategy; explicit non-targets/unknowns | PROVISIONAL/PASS | Yes + founder | final reconcile after G3–G5 |
| G7 Commercial/support commitment | founder accepts exclusivity, support/bug-fix duty, docs/contact plan, demo investment; named product/design/engineering/QA/support ownership; SLA/maintenance budget | OPEN | No — founder decision | structured founder decision gate |
| G8 M0 go/no-go | ≥8 interviews support pain; concept understandable; ≥3 competitor workflow gaps; requirements revalidated; ownership committed | OPEN | No — depends on G1–G7 | formal founder review after evidence complete |

## Stop rule

M0 research stops when G1–G7 have enough evidence to make G8. We do **not** continue collecting competitor anecdotes for confidence theater.

## What AI should finish before asking founder for participant work

1. Complete the systematic 50-review evidence set with balanced positive/counter/friction sampling.
2. Normalize the current competitor listing snapshot.
3. Prepare the controlled competitor task protocol and evidence sheet.
4. Refresh the remaining M0-relevant official Shopify unknowns.
5. Prepare a fixed merchant interview script, recruitment criteria, coding sheet and pass/fail rubric.

After those are ready, the project reaches a genuine human-evidence dependency: real competitor task interaction where access permits, real merchant interviews, and founder commercial decisions.

## M0 interview evidence rule

Do not count casual DCL client conversations retroactively unless the same required questions and evidence are captured. Do not fabricate, infer, or have AI role-play merchant evidence. Interview notes must record participant fit, vertical, role, relevant workflow frequency, current process, pain/cost/delay, support/developer dependence, concept comprehension, objections, and whether the observed evidence supports or contradicts the hypothesis.

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

M1 prototype work begins only after G8 authorizes it.
