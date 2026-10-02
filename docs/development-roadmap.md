# Development roadmap

No production theme work begins until M0 gates are approved. Each milestone is an independently reviewable merge with updated requirements, risk register and evidence.

From M2 onward, every milestone must complete the pre-code review and every implementation PR must pass the mandatory checklist in [`engineering-compliance-standard.md`](engineering-compliance-standard.md). Known failures of applicable Shopify requirements or internal hard gates block implementation completion.

## M0 — Research and validation (current)
**Objective:** establish a defensible product direction. **Scope/files:** 13 reconciled `docs/` deliverables; live listing/review workbook and interviews remain gates. **Acceptance:** one consistent target/positioning/vertical strategy; explicit unknowns; founder decisions answered; current official requirements captured; ≥8 interviews and competitor task teardowns completed. **Tests:** link check, terminology/priority audit, evidence audit. **Dependencies:** live official sources and participants. **Risks:** internally consistent hypotheses being mistaken for validation.

## M1 — Experience prototype and foundation decision
**Objective:** decide whether operability, intent-led starts, and the Launch Narrative create a distinctive, usable product before production theme code.

**Provisional status:** M1A foundation/originality architecture is documented in parallel, but it does not close or bypass M0's open empirical gates. Visual prototyping and the remaining M1 work cannot establish readiness for M2 until M0 is approved.

**Exact scope:**

1. Map current-state and proposed journeys for Product Launch, Paid Landing Page, Collection Launch, Editorial Story, and Product Education.
2. Produce grayscale, mobile-first clickable prototypes for home, PDP, collection, and campaign/landing contexts, including empty/long content and zero structured-data states.
3. Prototype the Beauty & Wellness preset deeply; apply the same section/block contracts to one apparel and one food/beverage content probe without polishing them into launch presets.
4. Define semantic global tokens and bounded section controls in a token/schema specimen; inventory setting counts and progressive disclosure.
5. Map Reveal/Explain/Prove/Compare/Act responsibilities to each surface, including omissions, mobile priority, merchandising, and optional data.
6. Compare intent-led starts against a blank/default baseline in moderated editor simulations with five target merchants.
7. Complete ADR-001–007: choose Skeleton Theme or fully original code (Dawn/Horizon excluded), then decide theme blocks, structured data, cart, RTL, native intent-composition map, and multi-vertical fitness/narrowing.
8. Refresh remaining Theme Store unknowns and dated competitor evidence. Produce an architectural originality comparison and requirements traceability map; do not claim approval.

**Acceptance criteria:**

- Five target merchants complete at least 80% of representative tasks unassisted, without code; median time and decision count improve over the baseline, and no critical accessibility issue is designed in.
- Participants can choose the correct starting composition and explain the shopper flow without being taught the internal narrative terms.
- Zero-setup states are visually complete; structured content demonstrably enhances rather than unlocks basic quality.
- Beauty & Wellness has a distinctive, agency-quality reference direction in grayscale and token specimens—not solely through photography, copy, fonts, or motion.
- Apparel and food/beverage probes reuse contracts within documented setting budgets and without vertical toggles or vague catch-all controls; otherwise ADR-007 explicitly narrows the product.
- Mobile prototypes keep purchase/navigation priorities clear, use no conflicting sticky layers, and specify keyboard, focus, reduced-motion, zoom, and content-order behavior.
- **Blocking originality gate:** a competitor comparison identifies at least three defensible workflow gaps, and prototype/system evidence demonstrates a fundamentally different architecture and overall experience with meaningful design and functional innovation. Intent-led templates, Launch Narrative terminology, semantic settings, presets, extra sections/settings, styling, or different JSON ordering alone fail this gate and block M2.
- ADR-001 chooses Skeleton Theme or fully original code, documenting provenance and trade-offs; Dawn and Horizon are excluded. All applicable Theme Store requirements have an owner, architecture mapping, validation status, and test plan; unknown mandatory rules block M2.
- Founder approves the target, Theme Store-exclusive distribution, support/bug-fix obligation, public documentation/contact plan, per-preset demo investment, named product/design/engineering/QA/support owners, and the resulting build/narrow/no-build decision.

**Out of scope:** production Liquid, final CSS/JavaScript, a complete scaffold, integrations, and production presets. **Dependencies:** completed M0 empirical gates. **Risks:** imagery carries perceived quality; workflow advantage is not measurable; cross-vertical abstraction weakens Beauty & Wellness; official requirements invalidate a foundation choice.

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
**Objective:** implement the validated Reveal/Explain/Prove/Compare/Act responsibility grammar without forcing a five-step funnel. **Files:** narrative sections/blocks/snippets and presets. **Acceptance:** missing-data safety and validated context-specific compositions. **Tests:** editor task study, omitted/reordered stages, long content, reduced motion, visual regression. **Dependencies:** M2/M5. **Risks:** generic-section drift or marketing-only terminology.

## M8 — Campaign workflow
**Objective:** implement validated native starting compositions without developer/template copying. **Files:** the minimum approved JSON templates and job-named section presets, plus documentation. **Acceptance:** marketing managers choose an appropriate start and complete each supported job at ≥80% unassisted success. **Tests:** editor lifecycle, duplicate/reorder/remove, mobile/performance. **Dependencies:** M7. **Risks:** too much choice or one-template-per-job sprawl.

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

Complete the unfinished empirical portion of **M0**—refresh remaining unverified official requirements, complete the dated competitor/review audit, conduct 8–12 merchant interviews (including adjacent-vertical evidence), complete the required competitor workflow/task teardowns, and hold the founder go/no-go review. The nine dated requirement facts in `shopify-requirements.md` are now verified; implementation compliance is not. M0 is **not ready to close** until the remaining gates pass. The provisional M1A documents and ADR-001 do not alter that gate; do not begin visual prototyping, scaffold theme code, or proceed to M2.
