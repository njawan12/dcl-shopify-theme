# M0 closure matrix — 2026-10-03

## Purpose

This is the controlling finite checklist for closing M0. It reconciles the roadmap, market research, product opportunity, requirements, support risks, and the dated live evidence added in PR #7. No new M0 research task should be added unless it is required to resolve one of these gates or a newly discovered Shopify requirement.

## Gate matrix

| Gate | Required evidence | Current status | Can AI/DCL desk research close it? | Blocking next action |
|---|---|---|---|---|
| G1 Current official Shopify requirements | dated official-source snapshot; mandatory unknowns resolved enough for M1 | **PASS FOR M0 WITH REVALIDATION OBLIGATION** — refreshed 2026-10-03 against current official Shopify docs | Mostly yes | revalidate at documented future milestones |
| G2 Current competitor commercial facts | dated price/review/preset/position snapshot | **PASS FOR M0 — dated 2026-10-03 snapshot captured across the eight-theme comparison set; values are point-in-time evidence, not permanent facts** | Yes | refresh only when current commercial facts are needed |
| G3 Review evidence | ≥50 recent reviews across sample, systematically coded with positive/counter-evidence and friction | **PASS WITH LIMITATION** — 50 official reviews coded; two Pipeline observations older due sparse current accessible reviews | Yes | reopen only under documented triggers |
| G4 Incumbent capability challenge | current public evidence plus hands-on editor evidence where legitimately accessible; surviving system hypotheses must withstand strong-incumbent challenge | **PASS FOR M0 WITH EVIDENCE LIMITATION** — public incumbent challenge eliminated feature-presence claims; H1 structural flexibility, H2 agency-informed controls, H3 visual system + clean implementation survive only as M1 hypotheses. No claim is made about competitor editor-depth limitations without legitimate access. | Partly | carry hands-on incumbent comparison into M1 where legitimate access exists; absence of L2/L3 access cannot be converted into a gap claim |
| G5 Operator / merchant problem evidence | Founder/operator evidence from repeated DCL client work plus independent merchant evidence where practical; distinguish evidence types; validate recurring customization demand without fabricating equivalence | **PASS FOR M0 WITH EVIDENCE LIMITATION** — founder/operator evidence + 15-pattern historical inventory captured; routine launch-pain premise was contradicted and rejected; recurring customization demand is sufficiently categorized to justify M1 prototyping, but is not represented as independent merchant validation. | Partly | collect independent merchant evidence opportunistically; reopen before stronger demand claims if contrary evidence appears |
| G6 Product/positioning coherence | one target, positioning and vertical strategy; explicit non-targets/unknowns | **PASS — Beauty/Wellness-first target, explicit non-targets, revised value hierarchy and three surviving M1 hypotheses reconciled** | Yes + founder | reopen only if M1 evidence forces narrowing or repositioning |
| G7 Commercial/support commitment | founder accepts exclusivity, support/bug-fix duty, docs/contact plan, demo investment; named product/design/engineering/QA/support ownership; SLA/maintenance capacity | **PASS — OPERATING MODEL + OWNERSHIP ACCEPTED 2026-10-03**: founder explicitly committed DCL to a real Beauty/Wellness-first Theme Store product business, Theme Store exclusivity, ongoing maintenance/QA, proper demo content, documentation and merchant support meeting Shopify requirements. Product owner/final product decision owner: **Nouman Javaid (founder), confirmed 2026-10-03**. Visual design/art direction owners: **Nouman Javaid + ChatGPT**, confirmed 2026-10-03; ChatGPT serves as design/product-system partner and Nouman retains human final approval. Engineering/code-quality ownership: **ChatGPT as technical architect/reviewer + Codex as implementation engineer**, confirmed 2026-10-03; Nouman retains approval over major product decisions. QA ownership: **ChatGPT + Codex for systematic/automated QA, with Nouman Javaid responsible for final human acceptance testing**, confirmed 2026-10-03. Merchant support ownership: **DCL**, with **Nouman Javaid accountable for the support function and Nouman + ChatGPT jointly developing support processes, documentation, triage/playbooks and response quality**; DCL team members may handle tickets operationally, confirmed 2026-10-03. | No — founder decision | ownership model recorded; quantify staffing/capacity, escalation coverage and operating budget before release readiness |
| G8 M0 go/no-go | revised thesis survives historical customization inventory and incumbent challenge; requirements revalidated; product/support ownership committed; no unresolved blocking originality/compliance risk | **PASS — M0 CLOSED 2026-10-03; PROCEED TO M1 PRODUCT/DESIGN VALIDATION, NOT PRODUCTION IMPLEMENTATION** | No — depends on G1–G7 | begin revised M1 only; preserve evidence limitations and revalidation obligations |

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


## M0 closure decision — 2026-10-03

**Decision: CLOSE M0 and proceed to M1 surface-system/product-design validation.**

This is not authorization for production theme implementation, Skeleton import, or M2.

### Why closure is justified

- Current official Shopify requirements were refreshed for M0 and remain hard constraints.
- The original routine-launch/workflow thesis was contradicted by operator evidence and explicitly retired rather than defended.
- A 50-review workbook and dated eight-theme market snapshot provide current market context.
- The 15-pattern historical DCL inventory provides sufficient operator evidence to choose what M1 should prototype, while remaining explicitly distinct from independent merchant validation.
- The incumbent challenge rejected feature-presence differentiation and left only system-level hypotheses for M1 to prove.
- The product is narrowed to Beauty/Wellness first with explicit non-targets.
- The founder accepted the Theme Store operating model and ownership for product, design, engineering, QA and support has been recorded.

### Evidence limitations carried forward

- Public competitor evidence does not prove editor-depth limitations.
- Founder/operator evidence is not ten independent merchant interviews.
- Originality is not proven; it is an M1 gate.
- Skeleton eligibility/provenance and volatile Shopify requirements require live revalidation at the documented milestones.
- Commercial sales volume and support cost remain unforecast because no honest evidence supports a forecast.

### M1 authorization boundary

M1 may create prototypes, contracts, design directions, control budgets, comparison evidence and foundation decisions. It may not begin production Liquid/CSS/JS/JSON or import a production Skeleton foundation.

M2 remains blocked until M1 passes.
