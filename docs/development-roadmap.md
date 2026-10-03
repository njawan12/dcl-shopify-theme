# Development roadmap

No production theme work begins until M0 gates are approved. Each milestone is an independently reviewable merge with updated requirements, risk register and evidence.

From M2 onward, every milestone must complete the pre-code review and every implementation PR must pass the mandatory checklist in [`engineering-compliance-standard.md`](engineering-compliance-standard.md). Known failures of applicable Shopify requirements or internal hard gates block implementation completion.

## M0 — Research and validation (current)
**Objective:** establish a defensible product direction. **Scope/files:** reconciled strategy, official requirements, coded review evidence, historical customization inventory, incumbent challenge and founder operating decision. **Acceptance:** one consistent Beauty/Wellness-first target/positioning; explicit non-targets and evidence limits; obsolete workflow thesis retired; current official requirements captured; recurring customization demand categorized; public incumbent challenge completed without inventing editor-depth claims; founder operating commitments answered. **Tests:** link check, terminology/priority audit, evidence audit. **Dependencies:** live official sources plus founder decisions; legitimate hands-on competitor/merchant evidence may continue opportunistically. **Risks:** operator evidence or public listings being overstated as independent merchant/editor proof.

## M1 — Surface-system prototype and foundation decision
**Objective:** prove that the revised product thesis can create visibly distinct, merchant-operable Beauty/Wellness storefronts through bounded structural flexibility on high-value surfaces, without configuration overload or brittle implementation.

**Provisional status:** ADR-001 and prior M1A work remain evidence inputs only. Product Launch, Paid Landing, Collection Launch, Editorial Story, Product Education and Reveal/Explain/Prove/Compare/Act are no longer controlling product architecture. Reveal/Explain/Prove/Compare/Act may be used only as an internal CRO/content-review lens.

**Exact scope:**

1. Prototype six highest-risk systems first: PDP purchase area/buy box; product media + badges; product education; cart; one general storytelling/content system; global design system + local structural controls.
2. For each system define a premium default, only evidence-justified structural variants, mobile behavior, missing/long-data behavior, dynamic-source strategy, app-block seams where applicable, setting-count budget, extension contract, accessibility constraints and performance ownership.
3. Produce at least three materially different Beauty/Wellness storefront compositions from the same underlying system. Difference must survive normalized copy/media and cannot rely only on photography, fonts, color or motion.
4. Demonstrate zero-setup polish from standard Shopify data and optional structured enhancement without making metafields/metaobjects mandatory.
5. Demonstrate designer range and merchant operability: a designer can create materially different supported outcomes without source edits; a merchant can safely operate the configured result afterward.
6. Demonstrate developer extensibility with a small extension exercise on at least the PDP purchase area and one content surface; no brittle global coupling or proprietary editor state.
7. Complete the control inventory: global token vs surface variant vs block composition vs dynamic product data vs bounded local setting. Reject arbitrary CSS/pixel controls as normal merchant workflow.
8. Refresh ADR-001 foundation eligibility and complete only ADRs still relevant to the revised architecture. Retire/replace obsolete workflow ADRs rather than carrying them forward by inertia.
9. Produce a current requirements traceability map and a stripped-system originality comparison against the strongest accessible incumbents. Do not infer competitor editor limitations without legitimate access.

**Blocking acceptance criteria:**

- The six prototype systems have complete contracts and setting-count budgets.
- At least three Beauty/Wellness compositions are visibly and structurally distinct while sharing the same coherent architecture.
- Structural variation is achieved without universal catch-all sections, vertical-mode switches, deep arbitrary nesting, proprietary workflow state, or settings-panel explosion.
- Standard Shopify data yields a complete premium storefront; optional structured data enhances rather than unlocks basic quality.
- Commerce surfaces preserve correct variants, prices, availability, selling plans where applicable, cart state, app seams and error behavior.
- Mobile behavior is explicitly designed, not desktop collapse; no conflicting sticky layers.
- Accessibility/performance constraints are designed into each system before production.
- The extension exercise demonstrates that a competent Shopify developer can add a justified variant/section without rewriting unrelated systems.
- Originality evidence is system-level: visual identity + high-value structural flexibility + agency-informed control selection + coherent implementation. Extra features/settings, metafields, Rollouts compatibility, preset names or CRO terminology do not satisfy the gate.
- Founder approves the reference direction, Theme Store-exclusive distribution, support/bug-fix obligation, public documentation/contact plan, demo investment and named product/design/engineering/QA/support ownership.

**Out of scope:** production Liquid/CSS/JavaScript/JSON, final preset, app-specific integrations, a proprietary page builder, and attempts to eliminate all custom development.

**Dependencies:** M0 closure under the revised closure matrix and current Shopify requirement revalidation.

**Failure rule:** if the six systems cannot produce materially different premium Beauty/Wellness outcomes without configuration overload, do not compensate by adding sections/settings. Narrow or stop before M2.

## M2 — Theme foundation/design system
**Objective:** valid, fast, accessible shell. **Scope:** layouts, tokens, settings, locales, base primitives, section groups, CI/package allowlist. **Files:** `layout/`, `config/`, `locales/`, base `assets/`, core `snippets/`. **Acceptance:** required skeleton routes render, branding task ≤10 minutes. **Tests:** Theme Check, JSON/locale parity, keyboard baseline, CSS/JS budgets. **Dependencies:** M1. **Risks:** starting-code policy changes.

## M3 — Navigation and discovery
**Objective:** reliable header, mobile navigation and predictive search. **Files:** header/announcement sections, navigation/search snippets and modules. **Acceptance:** keyboard/touch paths, long menus/translations, empty/error search. **Tests:** Playwright journeys, axe, required browsers. **Dependencies:** M2. **Risks:** mega-menu schema overload.

## M4 — Product-card and collection system
**Objective:** scalable browsing and merchandising. **Scope:** cards, grid, filters/sort, pagination, promo tiles, collection hero, quick add. **Files:** collection sections, card/filter snippets/modules, templates. **Acceptance:** all collection fixtures and URL-backed no-JS behavior. **Tests:** filter/sort/quick-add journeys, performance, visual/accessibility regression. **Dependencies:** M2–M3. **Risks:** variant and pagination complexity.

## M5 — Flagship product experience
**Objective:** correct, visually exceptional purchase flow with validated structural flexibility. **Scope:** media, form, variants, price/unit price, pickup, sticky behavior, grouped content, apps, recommendations. **Files:** main/featured product sections, blocks, product primitives/modules/templates. **Acceptance:** full product fixture matrix, zero-structured-data quality, app slots. **Tests:** commerce state suite, keyboard/screen reader, editor lifecycle, media performance. **Dependencies:** M2 and M4 card contracts. **Risks:** highest correctness/support surface.

## M6 — Cart and purchase continuity
**Objective:** calm, correct cart page; decide drawer separately. **Files:** cart sections/templates/modules. **Acceptance:** add/update/remove/errors and assistive announcements. **Tests:** concurrency/error/app-block cases, browsers. **Dependencies:** M5. **Risks:** accelerated checkout/app behavior.

## M7 — Narrative content system
**Objective:** implement the validated reusable product-education and storytelling primitives without a proprietary narrative grammar. **Files:** narrative sections/blocks/snippets and presets. **Acceptance:** missing-data safety and validated context-specific compositions. **Tests:** editor task study, omitted/reordered stages, long content, reduced motion, visual regression. **Dependencies:** M2/M5. **Risks:** generic-section drift or marketing-only terminology.

## M8 — Landing and content compositions
**Objective:** implement validated native page compositions and reusable sections without template proliferation or a proprietary workflow. **Files:** the minimum approved JSON templates and job-named section presets, plus documentation. **Acceptance:** marketing managers choose an appropriate start and complete each supported job at ≥80% unassisted success. **Tests:** editor lifecycle, duplicate/reorder/remove, mobile/performance. **Dependencies:** M7. **Risks:** too much choice or one-template-per-job sprawl.

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
**Objective:** honest, distinctive sales demonstration and support readiness. **Scope:** at least one industry/catalog-appropriate demo store for every preset, original licensed content, listing assets, public documentation and support contact form, support/bug-fix playbooks, and release notes. **Acceptance:** every preset has a corresponding demo; demos show standard and enhanced data; no misleading claims; support ownership and SLA are staffed. **Tests:** preset/demo mapping, content/license audit, public support-path check, merchant onboarding rehearsal. **Dependencies:** M11–M14. **Risks:** visual quality, multiplied preset cost, and support capacity.

## M16 — Theme Store submission
**Objective:** submit a traceable compliant package. **Scope:** final requirements refresh, package, listing and reviewer responses. **Acceptance:** all official checks and internal release gates pass; version tagged. **Tests:** clean-store install, package diff, full smoke and checklist. **Dependencies:** M15. **Risks:** requirement drift/reviewer findings.

## Exact next milestone

Finish M0 under the revised closure matrix: reconcile obsolete M1/workflow documents, complete the finite founder commercial/support decisions, and close or explicitly carry forward any honest evidence limitation. Do not resurrect the rejected Product Launch/workflow thesis. Production theme code and M2 remain blocked until M0 closes and revised M1 is approved.
