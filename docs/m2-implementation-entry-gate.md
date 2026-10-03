# M2 implementation entry gate

Status: pre-M2 readiness only. M2 remains closed until the repository's blocking M0 and M1 validation gates are completed and approved. This file records compliance facts and the intended entry criteria; it does not authorize production scaffolding.

## Live Shopify revalidation — 2026-10-03

Official Shopify documentation was rechecked before M2 implementation. The implementation must preserve these constraints:

- Theme Store submissions must be fundamentally differentiated at the overall experience and architectural level; cosmetic changes or a few added sections/settings are insufficient.
- Shopify Skeleton Theme is the only approved existing codebase for Theme Store development; otherwise the theme must use fully original code. Dawn- or Horizon-derived submissions are not eligible.
- Theme Store minimum Lighthouse averages remain 60 performance and 90 accessibility across home, product, and collection on desktop and mobile. DCL's stricter internal budgets remain the engineering target.
- Themes must not depend on an app or API-backed app-like functionality for full theme functionality.
- Fake urgency/scarcity is prohibited.
- JSON-template sections should support app blocks where appropriate; app blocks are not supported in statically rendered sections. App-block support must be intentional rather than mechanically added everywhere.
- Theme blocks are reusable merchant-editable primitives; snippets remain the preferred primitive for reusable implementation markup that does not need merchant customization.
- Current platform architecture supports JSON templates, section groups, sections, theme blocks, section blocks, app blocks, snippets, assets, config, locales, and layout files.

## Foundation decision for M2

ADR-001 remains the controlling decision. When M2 is authorized after M0/M1 closure, production scaffolding may use only a pinned/audited Shopify Skeleton foundation or fully original code. No Dawn or Horizon code may enter the repository.

After M0/M1 closure and before importing any Skeleton files, record the exact upstream commit/tag and audit the inherited files. If provenance cannot be established cleanly, use fully original scaffolding instead.

## First implementation slice

When the blocking M0/M1 gates are closed, M2 must begin with the smallest runnable production foundation, not a broad feature dump:

1. valid Shopify directory/layout/config/locales/template skeleton;
2. global design-token plumbing;
3. semantic document shell and accessibility baseline;
4. header/footer section-group architecture;
5. one representative Reveal section sufficient to exercise schema, responsive media, merchant controls, and editor lifecycle;
6. Theme Check and smoke-test instructions.

No PDP, collection merchandising, cart, search, campaign system, or large section library belongs in the first slice. Those follow only after the foundation is runnable and reviewed.

## Hard acceptance conditions

The first M2 implementation PR cannot merge unless:

- provenance is recorded;
- no Dawn/Horizon-derived code is present;
- theme structure is runnable in Shopify;
- schema is valid;
- JavaScript is optional/progressive-enhancement only;
- responsive images use Shopify image primitives;
- keyboard/focus behavior has no known blocker;
- app-block decisions follow the actual rendering context;
- Theme Check is clean or every exception is documented and justified;
- no production feature contradicts the M1 bounded-complexity/control contracts;
- no app dependency, fake scarcity, or API-backed app-like functionality is introduced.

## Blocking dependency

This document does **not** authorize production scaffolding or M2 implementation yet. The controlling roadmap and M1 prototype plan remain authoritative: M0 approval and every blocking M1 validation gate must be completed and recorded before production implementation begins.

Until those approvals are recorded, this document is only a pre-M2 compliance/readiness checklist. No production Liquid, JSON templates, sections, blocks, assets, config, locales, or inherited Skeleton files may be added under this milestone.

Once M0 and M1 are formally closed, revalidate any volatile Shopify requirements and then use the implementation slice and acceptance conditions above as the M2 entry gate.
