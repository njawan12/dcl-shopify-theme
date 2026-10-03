# M0 commercial gate — 2026-10-03

## Purpose

A Theme Store product can be technically excellent and still be commercially unattractive. This gate separates product quality from business viability and prevents DCL from treating theme revenue as passive software revenue.

## Verified/current operating model to carry into the decision

The competitive snapshot places the audited premium set at roughly USD $360–$500 per license. The product therefore has meaningful price headroom, but a one-time license must fund continuing platform/browser maintenance, merchant support, documentation, demo operations, QA and Theme Store compliance.

Current Shopify Theme Store rules/operating assumptions already recorded in the repository include:

- Theme Store exclusivity for Theme Store-distributed themes.
- Theme Partners are responsible for merchant support and bug fixes.
- Public documentation and a support contact path are required.
- Every preset requires a corresponding demo store.
- Theme approval and continued operation require compliance; approval cannot be treated as a permanent one-time event.
- DCL's current architecture intentionally rejects app-like/API-dependent features, fake scarcity, and proprietary builder behavior.

These constraints make supportability and maintenance part of gross-margin design.

## Unit-economics model

Let:

- P = merchant license price
- r = Theme Store revenue-share rate applicable to gross theme sales
- S = average lifetime support/merchant-success cost per license
- M = allocated maintenance/QA/platform-change cost per license
- D = allocated demo/content/documentation cost per license
- C = payment/tax/other applicable costs not already included by platform treatment

Contribution per license before company overhead is:

**Contribution = P × (1 − r) − S − M − D − C**

The model deliberately does not insert a speculative sales forecast. M0 does not have evidence for conversion rate, annual license volume, refund rate, or support tickets per license.

## Commercial scenarios to validate after launch planning

At a hypothetical $450 list price and the currently documented 15% Shopify share, DCL receives $382.50 before its own support/maintenance/demo/other allocated costs.

Illustrative gross receipts before DCL operating costs:

| Licenses | Gross merchant sales | After 15% Shopify share |
|---:|---:|---:|
| 25 | $11,250 | $9,562.50 |
| 50 | $22,500 | $19,125 |
| 100 | $45,000 | $38,250 |
| 250 | $112,500 | $95,625 |
| 500 | $225,000 | $191,250 |
| 1,000 | $450,000 | $382,500 |

These are **not forecasts**. They exist to expose the economics: a premium price still requires meaningful license volume before this becomes a large standalone business, and support cost can materially reduce contribution.

## Business-leader interpretation

### 1. Do not optimize for maximum install count

A theme that attracts broad low-fit demand can create disproportionate support. The commercial target should be **high-fit merchants who understand the opinionated product**, not every Shopify merchant.

### 2. Support burden is a product metric

For routine supported workflows, documentation and editor design should let merchants succeed without contacting DCL. Support contacts should be categorized and fed back into product decisions. Repeated “how do I build X?” tickets are product defects or positioning failures, not merely support work.

### 3. One excellent preset is economically safer than premature preset proliferation

Each preset creates demo/content/QA/maintenance burden. Adjacent presets should launch only when they reuse the validated architecture without vertical-specific schema forks and when the additional addressable demand justifies their ongoing cost.

### 4. The theme should create agency upside without requiring the agency

The product must stand alone. Optional DCL implementation/customization work can be an economic upside, but intentionally making the theme difficult in order to generate service work would undermine reviews, support economics and the core positioning.

### 5. Price should follow demonstrated value

Do not pick a final price merely by averaging competitors. If the validated workflow advantage is substantial and the visual product is genuinely premium, pricing can sit in the premium band. If the workflow advantage is weak, lowering the price does not fix the product.

## Commercial kill criteria before production investment

Do not authorize M2 merely because M1 prototypes look attractive. Reconsider or narrow the product if any of these remain true:

1. The recurring DCL customization inventory cannot be translated into a compact set of useful, repeatable controls/surface variants.
2. Strong incumbents already provide comparable structural flexibility on the targeted high-value surfaces, leaving no defensible system-level distinction.
3. The architecture needs frequent custom code or support for ordinary variation that the product explicitly claims to support.
4. The Beauty/Wellness reference system cannot produce materially different premium outcomes without schema/settings explosion.
5. DCL cannot name ongoing product, engineering/maintenance, QA and merchant-support ownership.
6. Demo/content quality required to sell the theme cannot be funded/maintained.
7. Shopify eligibility/originality requirements cannot be satisfied with a defensible architecture/provenance trail.

## Metrics to instrument if the product reaches release

Commercial:
- listing → trial conversion where measurable
- trial → purchase conversion where measurable
- refund rate/reasons
- preset selection
- support contacts per 100 licenses
- support minutes per active license
- custom-code requests per 100 licenses
- update-related tickets
- app-conflict tickets

Product:
- workflow-start selection
- time to first publish for supported jobs where measurable/consented
- abandonment points
- setting/search/help usage where technically and policy-permitted
- zero-data vs structured-enhancement adoption
- mobile recovery/support incidents

Quality:
- escaped P0/P1 defects
- regression rate per release
- accessibility defects
- performance regressions
- browser/platform-change response time

## M0 commercial decision still required

Before M0 closes, founder approval must explicitly answer:

- target customer and deliberate non-targets;
- willingness to accept Theme Store-exclusive distribution;
- product/design/engineering/QA/support ownership (one person may own multiple roles before launch, but every responsibility must be named);
- support SLA and escalation model meeting Shopify's current two-business-day response requirement and immediate critical-bug obligation;
- maintenance/QA capacity and budget appropriate to release cadence;
- demo photography/copy/content budget/capacity;
- willingness to narrow to Beauty & Wellness first if adjacent-vertical evidence is weak;
- commercial threshold for continuing after launch.

Until those are answered alongside the empirical product gates, commercial readiness is not established.
