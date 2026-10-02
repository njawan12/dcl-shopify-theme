# Support risk register

Scales: likelihood (L) and impact (I), 1–5. Score = L×I. Review each milestone and after support telemetry.

| ID | Risk | L | I | Score | Mitigation / trigger | Owner |
|---|---|---:|---:|---:|---|---|
| S01 | Too many settings confuse merchants | 4 | 4 | 16 | Setting budgets, presets, usability tests; reject redundant controls | Product |
| S02 | Structured content setup feels mandatory | 4 | 4 | 16 | Beautiful zero-setup state, optional recipes, onboarding examples | UX/docs |
| S03 | App block styling/conflicts | 4 | 4 | 16 | Neutral wrappers, generic slots, compatibility matrix, vendor escalation boundary | Engineering |
| S04 | Variant/swatches edge cases | 4 | 5 | 20 | Native option data, text fallback, exhaustive fixtures; never infer colors blindly | Engineering/QA |
| S05 | Sticky mobile UI overlaps apps/browser | 4 | 4 | 16 | Collision testing, disable control, safe-area support, one sticky owner | UX/QA |
| S06 | Theme upgrades collide with modifications | 4 | 4 | 16 | Stable contracts, release notes, discourage source edits, migration notes | Release |
| S07 | Merchant-created schemes fail contrast | 3 | 5 | 15 | Contrast-aware defaults/help, limited pairings, audit presets | Design/a11y |
| S08 | Missing/long content breaks compositions | 3 | 4 | 12 | Empty/overflow fixtures, graceful omission, bounded line handling only when safe | QA |
| S09 | Campaign flexibility becomes a page builder | 3 | 5 | 15 | Six job presets, shallow blocks, feature-matrix gate | Product |
| S10 | Collection promo tiles disrupt counts/filtering | 3 | 4 | 12 | Render as presentation around canonical pagination; regression tests | Engineering |
| S11 | Performance harmed by merchant apps/media | 5 | 4 | 20 | Separate theme/app attribution, budgets, documentation, no false score promise | Performance |
| S12 | Localization/RTL failures | 3 | 4 | 12 | Logical CSS, pseudo-localization; no RTL claim without native review | Localization |
| S13 | Browser/platform updates regress behavior | 4 | 4 | 16 | Scheduled matrix, dependency-free code, release cadence | QA/release |
| S14 | Merchants expect theme-owned reviews/subscriptions/bundles | 4 | 3 | 12 | Listing/docs scope, app-block guidance, no vendor promise | Product/support |
| S15 | Support response quality damages reviews | 3 | 5 | 15 | Named owner, SLA, triage templates, reproducible demo, telemetry | Support lead |
| S16 | Demo imagery sets unrealistic expectation | 3 | 3 | 9 | Multiple content qualities/aspect ratios; accurate listing disclosure | Marketing |
| S17 | Originality rejected | 2 | 5 | 10 | Original design history, code audit, pre-submission comparison | Product/legal |
| S18 | Requirements change after architecture | 3 | 5 | 15 | Revalidate at each release; traceability matrix | Technical owner |
| S19 | Multi-vertical ambition creates generic controls | 4 | 5 | 20 | Cross-vertical prototype tasks; setting budgets; narrow on trigger | Product/design |
| S20 | “No developer dependence” is read as unlimited customization | 4 | 4 | 16 | Define routine jobs and exclusions in listing/docs/support policy | Product/support |
| S21 | Intent presets are renamed templates, not differentiated workflow | 3 | 5 | 15 | Measure decision count, completion time and comprehension against blank/default baseline | Research |
| S22 | Each preset multiplies demo, documentation, QA and support obligations | 4 | 4 | 16 | Require funded demo/support owner before approving a preset; cap launch presets | Product/support |
| S23 | Theme Store exclusivity conflicts with distribution plan | 2 | 5 | 10 | Founder accepts exclusive channel before M1 investment; legal/commercial review | Founder/legal |

## Support design rules

Every feature requires: merchant-facing documentation, default/empty/error states, screenshots, diagnostic steps, ownership, compatibility boundary and removal plan. No launch until DCL can reproduce customer configuration safely without requesting store access by default.

## Operational targets requiring founder approval

Define coverage hours, first-response SLA, severity escalation, supported customizations, app-conflict policy, version-support window, privacy process, refund/escalation ownership, and documentation analytics. Theme engineering cannot compensate for an unfunded support function.
