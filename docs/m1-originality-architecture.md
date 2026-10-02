# M1 originality architecture

## Decision statement

The hypothesis **passes conditionally as an architecture worth prototyping; it does not yet pass the M1 originality gate**. The differentiator is not a five-word narrative, a set of presets, or more sections. It is a constrained **decision-path system** that carries one commercial argument across campaign, collection, and product surfaces while preserving the native job of each surface and substantially reducing merchant assembly decisions.

That claim must be demonstrated against current competitor implementations and five merchant tests. If a stripped prototype is perceived as generic, or intent-led starts do not measurably reduce time and decisions, the architecture fails and M2 remains blocked.

## The distinctive system: decision paths, not pages

A **decision path** is a native composition contract connecting a merchandising subject (product, collection, or story), a shopper question sequence, and one honest next action. It has four properties:

1. **Continuity:** campaign claims resolve into collection context and product evidence instead of restarting at each page.
2. **Surface integrity:** campaign pages persuade, collections orient and browse, and PDPs explain and transact. Shared content does not erase those jobs.
3. **Priority-aware transformation:** mobile may promote, condense, or omit supporting content by shopper priority; it is not desktop stacked into one column.
4. **Progressive data:** standard Shopify objects make a complete path; structured data improves consistency and reuse but never unlocks basic quality.

This is narrower than a page builder. Merchants choose a job, a subject, and bounded emphasis; they do not design an arbitrary component tree or configure a funnel engine.

## Composition architecture

### Layers and ownership

| Layer | Owns | Must not own |
|---|---|---|
| Shopify data | Products, variants, collections, pages/articles, media, navigation, Markets context | Narrative sequencing or visual layout |
| Reusable primitives | Media rendering, product facts, price, option selection, CTA, disclosures, badges from legitimate data, responsive layout behaviors | Merchant-facing page intent |
| Blocks | One repeatable semantic unit inside a section: claim, benefit, evidence item, comparison dimension, FAQ, product reference, app placement | Cross-page sequencing or universal layout |
| Sections | One primary shopper question, one surface-aware information role, and a defined relationship to the next action | Every narrative stage, arbitrary nesting, or hidden commerce logic |
| Surface composition | Native ordered sections and defaults appropriate to campaign, collection, PDP, editorial, or home context | Proprietary runtime orchestration |
| Workflow start | Chooses the smallest useful surface composition, meaningful defaults, omissions, and suggested data connections for a merchant job | A locked funnel or duplicate rendering engine |
| Global system | Semantic type/spacing/color roles, cards, media rules, controls, localization, focus/motion behavior | One global layout imposed on all surfaces |

### Section contract

Every narrative-capable section must declare in its design specification:

- a single primary shopper question;
- its primary responsibility: orient, clarify, substantiate, distinguish, or enable the next action;
- supported surfaces and the distinct behavior on each;
- required standard data and zero-setup fallback;
- optional dynamic-source connections;
- allowed blocks, maximum useful count, and order rules;
- CTA relationship: none, contextual next step, product/collection destination, or purchase handoff;
- mobile priority and content-order behavior;
- missing/long-content, localization, accessibility, and media-loading behavior;
- compatible generic app-block positions, if any.

A section is rejected if its description needs “anything,” if it performs multiple unrelated shopper jobs, or if its useful default requires filling several blank blocks.

### Block contract

Blocks represent merchant-meaningful repeatable evidence, not columns or CSS fragments. They may supply a benefit, proof item, comparison row, question/answer, step, product reference, or app extension. Blocks do not control outer width, global typography, breakpoint behavior, or unrelated section chrome. Reordering a block must preserve semantic reading order; limits prevent galleries of empty options.

### Reusable primitives

Shared primitives include responsive media, editorial/product reference, fact rail, price and availability, option/value chooser, action group, claim/evidence pair, disclosure group, comparison semantics, pagination/filter status, and accessible media controls. These are implementation reuse, not a promise that every section exposes every primitive.

## Internal grammar and merchant language

**Reveal → Explain → Prove → Compare → Act** remains internal responsibility metadata. It governs information order and QA, but merchants see job and shopper-outcome language such as “Open the launch,” “Show why it matters,” “Add evidence,” “Help shoppers choose,” and “Lead to the product.” The five stages are neither mandatory nor always sequential:

- a paid page can Reveal → Prove → Act;
- a collection can Reveal → Explain within one editorial interruption → Act through product discovery;
- a PDP can begin with factual Act controls alongside Reveal, then Explain/Prove below;
- Compare is absent when the data would be invented, weak, or coercive;
- Editorial Story may end in a contextual destination rather than purchase.

The architecture is successful only if merchants can explain the shopper flow without learning the internal terms.

## Intent-led starting states

Each workflow start is a supported native template/section preset composition with:

- the minimum sections needed for the job;
- a selected merchandising subject or clearly explained connection point;
- example-safe headings and standard-object fallbacks rather than lorem ipsum dependency;
- intentional omissions and bounded choices;
- mobile priorities and app insertion points encoded in the design contract;
- a removal path: sections remain normal native sections that can be reordered, removed, or reused within their supported contexts.

Workflows alter initial composition, defaults, suggested connections, and guidance. They do **not** create a parallel editor, persist proprietary graph data, intercept Shopify rendering, lock section order, or make a store dependent on an app/API. The exact supported template/preset map is deferred to ADR-006 after prototype tests.

## Multi-workflow sections without catch-all drift

Reuse is approved by **same shopper question, different context**, not by visual similarity. An evidence section can serve Product Launch and Product Education because both answer “why should I believe this?”, while its campaign CTA may hand off to a PDP and its PDP version remains subordinate to purchase facts. It cannot also become a logo cloud, FAQ, comparison table, and gallery.

Each section gets a surface support matrix. A new workflow may reuse it only when its primary question, data contract, accessibility semantics, and bounded blocks remain intact. Otherwise create a surface-specific section or deliberately omit the need. Near-duplicate sections require a documented reason; universal sections are rejected.

## Global versus surface-specific

### Shared globally

- semantic color, typography, density, spacing, width, radius, and motion roles;
- accessibility and interaction primitives;
- media policy, product facts, buttons, links, cards, and app wrapper behavior;
- decision-path responsibility metadata and content-quality rules;
- data fallback rules and structured-content vocabulary;
- performance ownership, localization behavior, and provenance standards.

### Intentionally surface-specific

- **PDP:** factual purchase core, variants, price, availability, product media, pickup/selling-plan/app compatibility, and purchase continuity;
- **Collection:** canonical product set, filtering/sorting/pagination, clearly non-product editorial interruption, and collection orientation;
- **Campaign/landing:** concise argument and deliberate destination; no imitation of product form or collection grid unless the real object is rendered correctly;
- **Editorial:** reading rhythm, author/date/content semantics where applicable, and contextual commerce links;
- **Home:** wayfinding among current decisions, not a compressed version of every workflow.

## Cross-surface relationship

The campaign establishes the promise and sends the shopper to a collection edit or a product. The collection preserves the promise in its orientation and optional editorial interruption, then lets shoppers browse using canonical product semantics. The PDP resolves the promise into product-specific benefits, evidence, comparison only when honest, and a correct purchase core. Repeated content is condensed or referenced rather than copied wholesale. URL state, selected product/variant, and canonical Shopify behavior take precedence over narrative continuity.

This “argument handoff” is the strongest originality claim: not merely shared styling, but a governed relationship between what one surface promises and what the next surface must answer.

## Mobile composition

Mobile composition follows shopper priority rather than desktop geometry:

- reveal identity and the highest-value claim without forcing a full-screen media toll;
- expose essential product facts and the next action earlier on PDPs;
- retain collection count/filter/sort clarity before editorial interruption;
- reduce duplicate proof, secondary media, and decorative motion;
- allow one sticky owner at most, with app/browser safe-area and collision testing;
- preserve DOM/reading/focus order; visual reordering cannot create a contradictory accessible sequence;
- use disclosures only when collapsed content remains discoverable and suitable;
- avoid carousels when a short ordered list or scroll is clearer.

The prototype must specify what is promoted, condensed, deferred, or omitted for every screen—not simply show responsive widths.

## Data architecture

### Polished zero-setup

Standard product title, vendor, description, price, variants, media, availability, collection title/description/image, page/article content, and navigation produce complete layouts. Defaults derive hierarchy from available content, cap repeated modules to meaningful quantities, omit empty optional regions, preserve media ratios, and never fabricate proof, urgency, ratings, ingredients, or comparisons.

Where evidence is absent, the section disappears or uses factual product/collection content; it never displays empty cards or claims. A new section is immediately coherent using its preset content and obvious object selector where native data cannot be inferred.

### Progressive structured enhancement

Optional metafields/metaobjects can normalize benefits, usage steps, specifications, ingredients/materials, certifications, evidence citations, FAQs, and comparison dimensions. Dynamic sources should populate the same section/block contracts used by manual content. Deleting or disconnecting data restores omission/fallback behavior. Recipes must be documented, portable, localized where supported, and never required for purchasing or baseline polish. Namespace and ownership decisions remain ADR-003.

### Apps as guests

Required and useful `@app` positions sit at explicit seams: product purchase context, supporting product information, evidence/reviews region, or a bounded campaign/content insertion where currently supported. The theme owns spacing and hierarchy but does not restyle opaque app internals aggressively. An app can enrich evidence or commerce, but removing it cannot break the decision path. No workflow promises a vendor-specific app.

## Stripped-system test against the named field

If photography, fonts, copy, colors, and motion are removed, the proposed system is **potentially** recognizable by this combined behavior:

1. a merchant begins with a commercial job rather than a blank page or feature catalog;
2. that start encodes deliberate omissions and shopper-question order;
3. the same argument is handed off differently across campaign, collection, and PDP without erasing native surface semantics;
4. mobile changes information priority rather than only layout;
5. standard Shopify data creates a complete path, while structured data reuses evidence without becoming mandatory;
6. every section has a narrow question/CTA contract, preventing generic-section accumulation.

No repository evidence yet proves that this combination is absent or materially weaker in Prestige, Impulse, Impact, Enterprise, Broadcast, Symmetry, Motion, and Pipeline. Current competitor entries are explicitly marked for revalidation. Therefore the honest answer is **conditionally yes as a design hypothesis, not yet convincingly yes as evidence**.

Before M2, the prototype must change or stop if any of these occur:

- the stripped screens can be reproduced by merely renaming/reordering generic hero, rich-text, logo, and product-grid sections;
- cross-surface handoff is invisible to shoppers or cumbersome to merchants;
- mobile prioritization adds settings instead of making governed decisions;
- each workflow requires unique sections, proving there is no coherent system;
- adjacent-vertical probes require “industry mode” toggles or generic catch-all controls;
- merchants do not beat the blank/default baseline on completion, time, and decision count;
- current competitor teardowns show the same end-to-end system without at least three material workflow gaps.

If it fails, first narrow the supported workflows and strengthen argument handoff and surface-specific rules. Do not add sections, settings, motion, or novelty styling as a substitute. If those changes still cannot produce measurable difference, do not build the product.

## Originality evidence required

- dated task-level teardowns of all eight named themes, not feature-list comparison;
- grayscale stripped-system comparison using equivalent content and data;
- merchant task recordings, decisions, completion time, errors, and comprehension;
- section responsibility and cross-surface handoff maps;
- mobile priority diffs and zero/structured-data pairs;
- design history, rejected alternatives, provenance ledger, and foundation diff;
- a red-team review asking whether native presets and good defaults alone explain the result.
