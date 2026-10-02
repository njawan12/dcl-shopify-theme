# Development roadmap

No production theme work begins until M0 gates are approved. Each milestone is an independently reviewable merge with updated requirements, risk register and evidence.

## M0 — Research and validation (current)
**Objective:** establish a defensible decision. **Scope/files:** 13 `docs/` deliverables; live listing/review workbook and interviews still gated. **Acceptance:** founder decisions answered, current requirements captured, ≥8 interviews and competitor task teardowns completed. **Tests:** link check, document consistency, evidence audit. **Dependencies:** network access and participants. **Risks:** directional desk research mistaken for validation.

## M1 — Experience prototype and foundation decision
**Objective:** prove Launch Narrative System before code. **Scope:** journeys, grayscale/mobile prototypes, token specimen, ADR-001–005. **Files:** design source, `docs/adr/`, architecture updates. **Acceptance:** five target merchants complete core prototype tasks; originality review passes; approved starting foundation documented. **Tests:** moderated tasks, accessibility annotation review. **Dependencies:** M0 gate. **Risks:** differentiation depends on imagery.

## M2 — Theme foundation/design system
**Objective:** valid, fast, accessible shell. **Scope:** layouts, tokens, settings, locales, base primitives, section groups, CI/package allowlist. **Files:** `layout/`, `config/`, `locales/`, base `assets/`, core `snippets/`. **Acceptance:** required skeleton routes render, branding task ≤10 minutes. **Tests:** Theme Check, JSON/locale parity, keyboard baseline, CSS/JS budgets. **Dependencies:** M1. **Risks:** starting-code policy changes.

## M3 — Navigation and discovery
**Objective:** reliable header, mobile navigation and predictive search. **Files:** header/announcement sections, navigation/search snippets and modules. **Acceptance:** keyboard/touch paths, long menus/translations, empty/error search. **Tests:** Playwright journeys, axe, required browsers. **Dependencies:** M2. **Risks:** mega-menu schema overload.

## M4 — Product-card and collection system
**Objective:** scalable browsing and merchandising. **Scope:** cards, grid, filters/sort, pagination, promo tiles, collection hero, quick add. **Files:** collection sections, card/filter snippets/modules, templates. **Acceptance:** all collection fixtures and URL-backed no-JS behavior. **Tests:** filter/sort/quick-add journeys, performance, visual/accessibility regression. **Dependencies:** M2–M3. **Risks:** variant and pagination complexity.

## M5 — Flagship product experience
**Objective:** correct purchase flow plus narrative chapters. **Scope:** media, form, variants, price/unit price, pickup, sticky behavior, grouped content, apps, recommendations. **Files:** main/featured product sections, blocks, product primitives/modules/templates. **Acceptance:** full product fixture matrix, zero-structured-data quality, app slots. **Tests:** commerce state suite, keyboard/screen reader, editor lifecycle, media performance. **Dependencies:** M2 and M4 card contracts. **Risks:** highest correctness/support surface.

## M6 — Cart and purchase continuity
**Objective:** calm, correct cart page; decide drawer separately. **Files:** cart sections/templates/modules. **Acceptance:** add/update/remove/errors and assistive announcements. **Tests:** concurrency/error/app-block cases, browsers. **Dependencies:** M5. **Risks:** accelerated checkout/app behavior.

## M7 — Narrative content system
**Objective:** implement Reveal/Explain/Prove/Compare/Act reusable grammar. **Files:** narrative sections/blocks/snippets and presets. **Acceptance:** missing-data safety and three art-direction demonstrations. **Tests:** editor task study, long content, reduced motion, visual regression. **Dependencies:** M2/M5. **Risks:** generic-section drift.

## M8 — Campaign workflow
**Objective:** build a launch page without developer/template copying. **Files:** `page.campaign.json`, six section presets, documentation. **Acceptance:** marketing managers complete launch task at ≥80% unassisted success. **Tests:** editor lifecycle, duplicate/reorder/remove, mobile/performance. **Dependencies:** M7. **Risks:** too much choice.

## M9 — Search and content completeness
**Objective:** complete required storefront resources. **Files:** search, blog/article, page, 404, password, gift-card, customer-related templates as currently required. **Acceptance:** requirements traceability complete. **Tests:** content/empty/localization/a11y cases. **Dependencies:** M2–M3. **Risks:** overlooked platform states.

## M10 — Structured-content recipes and app compatibility
**Objective:** optional native enhancements with safe integrations. **Files:** dynamic-source-compatible settings, recipe docs, compatibility fixtures. **Acceptance:** zero-setup and enhanced PDP both pass; representative app categories fit generic slots. **Tests:** connect/disconnect sources, deleted references, app blocks. **Dependencies:** M5/M7. **Risks:** setup/support burden and vendor variance.

## M11 — Merchant editing refinement
**Objective:** eliminate confusing settings and failure-prone combinations. **Scope:** schema language, defaults, presets, contextual help. **Acceptance:** all 12 merchant tasks meet targets. **Tests:** moderated usability and editor regression. **Dependencies:** M3–M10. **Risks:** late schema changes/migrations.

## M12 — Accessibility conformance
**Objective:** WCAG 2.2 AA target and Theme Store compliance. **Scope:** independent audit/remediation. **Acceptance:** no known A/AA blocker; Lighthouse target; documented exceptions. **Tests:** axe, keyboard, VoiceOver, NVDA, zoom/reflow, contrast, reduced motion. **Dependencies:** feature complete. **Risks:** app content outside control.

## M13 — Performance hardening
**Objective:** meet internal budgets with demo content. **Scope:** Liquid/render, assets, media, JS and CSS audit. **Acceptance:** all hard gates in performance budget. **Tests:** Lighthouse CI repeat sets, bundle budgets, traces. **Dependencies:** feature complete. **Risks:** demo/app payload attribution.

## M14 — Cross-browser, Markets and resilience QA
**Objective:** production confidence across current required matrix. **Acceptance:** no P0/P1 defects; localization and webviews verified. **Tests:** complete QA plan, failure injection and regression. **Dependencies:** M12–M13. **Risks:** device lab access.

## M15 — Demo preset and commercial readiness
**Objective:** honest, distinctive sales demonstration and support readiness. **Scope:** original licensed content, listing assets, docs, support playbooks, release notes. **Acceptance:** demo shows standard and enhanced data; no misleading claims; SLA staffed. **Tests:** content/license audit, merchant onboarding rehearsal. **Dependencies:** M11–M14. **Risks:** visual quality/content cost.

## M16 — Theme Store submission
**Objective:** submit a traceable compliant package. **Scope:** final requirements refresh, package, listing and reviewer responses. **Acceptance:** all official checks and internal release gates pass; version tagged. **Tests:** clean-store install, package diff, full smoke and checklist. **Dependencies:** M15. **Risks:** requirement drift/reviewer findings.

## Exact next milestone

Complete the unfinished empirical portion of **M0**—live requirement capture, dated competitor/review audit, and 8–12 merchant interviews—then hold a founder go/no-go review. Only after approval begin M1; do not scaffold theme code yet.
