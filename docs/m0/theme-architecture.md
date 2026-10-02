# M0 Theme Architecture Direction

## Scope boundary

This is an architecture proposal for M1 validation, not production theme code. It uses native Shopify Online Store 2.0 concepts and must be checked against the platform version and Theme Store requirements current at implementation time.

## Architecture model

### Layer 1: design system

Global tokens govern typography roles, colour schemes, spacing rhythm, shape, motion and content width. Presets select coherent token values. Sections request semantic roles rather than exposing arbitrary CSS controls.

### Layer 2: commerce primitives

Stable primitives cover product identity, price, variants, purchase actions, media, cards, availability and complementary merchandising. Their information hierarchy stays consistent across templates.

### Layer 3: narrative sections

A restrained family of sections fulfils decision roles:

- proposition/reveal;
- benefit or feature explanation;
- evidence and trust;
- comparison or choice guidance;
- product/collection discovery; and
- action or next step.

These are internal roles, not necessarily merchant-facing names. A section should fulfil one dominant job, support a few compatible presentations and declare graceful empty states.

### Layer 4: native intent templates

JSON templates and section groups compose the primitives into Product Launch, Paid Landing Page, Collection Launch, Editorial Story and Product Education starting points. Merchants duplicate and assign templates through Shopify's native model. Section presets support deliberate additions, but the default workflow is not blank-page assembly.

### Layer 5: optional structured content

Standard metafields and metaobjects may provide attributes, evidence, usage steps, FAQs, comparison dimensions and editorial references. Templates must also accept local block content and degrade cleanly. Data contracts remain vertical-neutral while preset copy supplies vertical language.

## Launch Narrative as a composition grammar

Reveal → Explain → Prove → Compare → Act is an internal reasoning tool, not a mandatory five-section funnel and not proposed merchant terminology.

| Role | Architecture effect | PDP | Collection | Campaign/editorial |
|---|---|---|---|---|
| Reveal | Requires a clear proposition and primary subject | product identity + outcome | collection idea + entry products | campaign thesis |
| Explain | Allocates space for benefits, use or craft | benefits, usage, attributes | selection logic, category education | chapters or feature story |
| Prove | Defines reusable evidence patterns | reviews, testing, provenance | category trust, press or social proof | evidence near claims |
| Compare | Adds choice support only when useful | variants, alternatives, routine role | filters, product distinctions | featured options or bundles |
| Act | Maintains a legible next action | add to cart / subscription | shop a product or subset | shop, explore or read next |

The grammar influences default order, allowable transitions, mobile priority and content requirements. Roles may repeat, combine or be omitted. “Compare” is inappropriate for some editorial stories; “Act” can be a low-pressure next chapter rather than purchase. Templates should be evaluated by whether each module advances a decision, not whether all five labels are present.

## Intent compositions

| Intent | Default emphasis | Native realization |
|---|---|---|
| Product Launch | dramatic reveal, education, proof, purchase | alternate product JSON template with product-bound sections |
| Paid Landing Page | message match, focused evidence, minimal exits, decisive CTA | alternate page template and compatible header/footer section-group state where native constraints allow |
| Collection Launch | campaign story integrated with discovery | alternate collection template with editorial modules and product grid |
| Editorial Story | paced narrative with contextual commerce | alternate page/article template using editorial and product-reference sections |
| Product Education | explanation, usage, evidence, FAQ and action | alternate product/page template with optional structured sources |

## Cross-vertical strategy

Architecture names describe durable content roles: `attributes`, `evidence`, `usage`, `comparison`, `related products`. Presets translate labels and choose default presentations. Vertical-specific needs earn extensions only when a neutral primitive would become vague or unsafe. Regulatory claims, sizing and nutrition should not be forced into one shapeless “details” object.

## Constraints and risks

- Native template discovery may not feel like a true intent picker; M1 must prototype onboarding within allowed Theme Store mechanisms.
- Template proliferation can become another complexity tax. Ship few, clearly differentiated compositions.
- Dynamic source compatibility and fallback behaviour need technical spikes.
- Paid landing pages may be constrained by global section groups and navigation behaviour; do not promise isolation before validation.
- Accessibility and performance budgets can conflict with dramatic art direction; they are release constraints, not polish work.
