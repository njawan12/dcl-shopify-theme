# ADR-001: Theme foundation

- **Status:** Proposed, conditional M1A recommendation; not accepted for implementation until M0 closes, the live foundation facts are revalidated, and the remaining M1 gates pass
- **Decision date:** 2 October 2026
- **Decision owners:** Product and engineering
- **Scope:** Select the eligible starting-code strategy for this product; this ADR does not authorize production theme work
- **Repository evidence:** [`shopify-requirements.md`](../shopify-requirements.md), [`theme-architecture.md`](../theme-architecture.md), and [`engineering-compliance-standard.md`](../engineering-compliance-standard.md)

## Context and decision drivers

The repository's verified requirements baseline records only two eligible routes for a new Theme Store submission: Shopify Skeleton Theme or fully original code. Dawn and Horizon are excluded. Shopify approval is neither claimed nor predictable; the final artifact must still satisfy the current requirements and demonstrate meaningful architectural and overall-experience originality.

This product is not trying to invent a novel product form, dialog, image pipeline, or focus trap. It is trying to make five recurring commercial jobs operable through a coherent composition system: intent-led starts, surface-specific narrative behavior, strong zero-setup defaults, optional structured enhancement, and bounded merchant decisions. The foundation should preserve engineering effort for that product-level innovation while keeping provenance legible.

## Considered options

### A. Shopify Skeleton Theme

Use the current official Skeleton Theme as a minimal starting repository, pin the exact upstream commit and license, retain attribution, inventory every inherited file, and replace or extend it only through recorded decisions. “Skeleton” is a code foundation, not the product architecture, visual reference, section catalog, or permission to inherit future changes blindly.

### B. Fully original theme code

Create every distributable theme file from an empty repository using official platform contracts and documentation. Conventional behaviors may follow published standards, but no third-party theme implementation is copied. A clean-room provenance log still records authorship, references, and licenses.

## Comparative assessment

Ratings are relative for this product: **advantage**, **neutral**, or **disadvantage**. Eligibility is binary only after current rules are revalidated.

| Driver | Skeleton Theme | Fully original code | Product-specific conclusion |
|---|---|---|---|
| Theme Store eligibility | Eligible in the verified 2026-10-02 baseline; revalidate before M2 and submission | Eligible in the same baseline; revalidate before M2 and submission | Neutral. Neither route earns approval. |
| Architectural originality | Neutral if kept as a thin primitive layer; disadvantage if its composition is treated as a template | Superficial advantage only; novel file authorship does not prove a different experience | Originality must reside above the foundation in the composition contracts and workflows. |
| Provenance risk | **Advantage** when exact upstream commit, license, inherited-file inventory, and diff are retained; risk rises if upstream code is mixed without records | **Advantage** for ownership, but clean-room drift and accidental copying remain possible | Both need provenance controls; Skeleton has a more auditable starting boundary. |
| Implementation speed | **Advantage** for initial platform wiring and solved primitives | **Disadvantage** because baseline contracts and test fixtures must be created before differentiated work | Skeleton protects M1/M2 effort for the novel system. |
| Accessibility baseline | Modest **advantage**, subject to audit; no inherited behavior is presumed conformant | **Disadvantage** initially; all interaction semantics start unproven | Reusing a minimal official baseline is rational, but WCAG 2.2 AA remains DCL's gate. |
| Performance baseline | Modest **advantage** from minimal scope, subject to measurement | Potential advantage only if discipline survives; also higher regression risk | Neither route is accepted without the internal budgets and realistic fixtures. |
| Shopify-native correctness | **Advantage** as a current official reference, subject to version and requirement drift | **Disadvantage** during startup; every contract must be reconstructed and verified | This is the strongest reason to use Skeleton. |
| Long-term maintainability | **Advantage** if inherited scope stays small and DCL owns a documented boundary | Mixed: full ownership, but a larger bespoke primitive/test surface | Skeleton reduces undifferentiated maintenance without outsourcing ownership. |
| Upgrade burden | Periodic upstream review, never blind merges; **neutral** | No upstream merge, but all platform changes are DCL's burden; **neutral/disadvantage** | Pinning avoids an implicit update channel; both require active platform maintenance. |
| Merchant-operability architecture | No inherent advantage; must be built and tested by DCL | No inherent advantage | The layer above either foundation determines this. |
| Intent-led workflows | No inherent advantage; Skeleton must not dictate composition | No inherent advantage | Native templates, presets, sections, and blocks remain the mechanism. |
| Distinctive overall experience | Possible only if the M1 architecture and prototype pass the stripping test | Possible, but original source alone offers no shopper-visible difference | Fully original code would be originality theatre unless the system also differs. |
| Support burden | Lower initial primitive burden; inherited code must be understood and owned | Higher baseline support and regression surface | Skeleton is preferable for a support-constrained product. |
| Testing burden | Still substantial, but starts from a smaller known reference | Highest: both primitives and product systems need first-principles coverage | Skeleton does not waive any test; it reduces the number of novel claims. |
| Accidental convergence with existing Theme Store themes | Risk if Skeleton defaults survive into shipped composition | Risk through familiar patterns and competitor observation despite original authorship | Anti-convergence controls and comparison evidence matter more than authorship route. |

## Conditional recommendation

**Conditionally prefer Shopify Skeleton Theme as a pinned, audited primitive foundation, subject to M0 closure, the remaining M1 evidence, and live eligibility and license revalidation immediately before M2.**

This is a recommendation for this product, not a general preference. Its value is the opportunity cost it avoids: rebuilding solved Shopify plumbing would consume accessibility, commerce-correctness, and testing capacity without strengthening the merchant promise. Fully original code would be justified if Skeleton proves legally or technically ineligible, materially violates the performance/accessibility architecture, or imposes composition assumptions that cannot be removed cleanly. None of those contradictions is established in the repository baseline.

The recommendation is deliberately conditional on an **inheritance ceiling**:

1. Before production work, record the official repository URL, exact commit, retrieval date, license text, and cryptographic archive/commit identifier.
2. Produce an inherited-file inventory classifying each file as retain, rewrite, or remove, with rationale. No file survives merely because it came from Shopify.
3. Keep inherited code below the product-system boundary: platform shell and conventional primitives only. Do not inherit page composition, preset storytelling, merchant terminology, design tokens, visual direction, or section catalog as product decisions.
4. Never merge upstream wholesale. Review platform changes as explicit, tested patches.
5. Maintain authorship and third-party notices plus a provenance ledger for every later dependency, reference, and generated asset.
6. Run the same accessibility, performance, commerce, editor-lifecycle, app, localization, and originality gates as fully original code.
7. If the M1 prototype cannot demonstrate a distinctive stripped system, stop or redesign; switching to fully original code does not cure that failure.

## Rejected rationale

- **“Fully original sounds more original.”** Rejected. Source authorship is not evidence of functional or experiential innovation.
- **“Skeleton is faster.”** Insufficient by itself. It wins because speed is concentrated in conventional platform foundations and frees capacity for the differentiating system, with a controllable inheritance boundary.
- **“Official starter means compliant.”** Rejected. Every inherited behavior and all current Shopify rules require validation.
- **“Different section ordering proves originality.”** Rejected by the M1 blocking gate and the verified requirements baseline.

## Consequences

### Positive

- DCL can invest prototype and implementation effort in narrative composition, merchant decision reduction, cross-surface continuity, and robust defaults.
- Platform primitives begin from a minimal official reference rather than competitor code.
- The pinned boundary makes provenance and later upstream review auditable.

### Negative and mitigations

- **Convergence:** residual starter decisions could make the result generic. Mitigate by removing starter composition/presentation decisions and running the stripped-system comparison before M2 and at every implementation review.
- **False confidence:** official origin may be mistaken for compliance. Mitigate with requirement traceability and independent audits.
- **Upstream burden:** Shopify changes will not flow automatically. Mitigate with scheduled review and selective patches.
- **Knowledge gap:** inherited code still becomes DCL's support responsibility. Mitigate with file-level ownership and tests before retention.

## External revalidation required

Live documentation was not used for this ADR; it relies on the repository's verified 2 October 2026 baseline. Before M2, verify from official Shopify sources:

1. Skeleton Theme and fully original code remain the only eligible foundation routes, and Dawn/Horizon remain excluded for the intended submission class.
2. The current Skeleton repository, license, supported status, intended usage, and exact branch/tag/commit.
3. Current Theme Store submission eligibility, exclusivity, review process, fees, packaging, supported directories, required templates, and schema limits.
4. Current theme-block nesting/support and `@app` block requirements by surface.
5. Current browser, localization/translation, accessibility, and performance measurement requirements.

Any contradiction blocks implementation and reopens ADR-001. Approval remains a Shopify decision.
