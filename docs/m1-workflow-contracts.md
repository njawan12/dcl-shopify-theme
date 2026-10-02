# M1 intent-led workflow contracts

## Shared contract

These are prototype contracts, not final UI or production schemas. All workflows use native Shopify surfaces and the narrow section responsibilities defined in [`m1-originality-architecture.md`](m1-originality-architecture.md). Sections may be removed, reordered, duplicated where safe, or added from a bounded catalog; a workflow is a starting state, not a lock.

Shared rules:

- standard Shopify data must produce a complete, honest zero-setup experience;
- structured content and apps only enhance it;
- Reveal/Explain/Prove/Compare/Act is internal metadata, not merchant jargon or a mandatory sequence;
- missing stages collapse without empty containers; no invented claims, ratings, evidence, comparisons, or urgency;
- one sticky owner maximum on mobile;
- visual changes cannot contradict DOM, reading, focus, or action order;
- app positions are generic and subject to current Shopify support; no vendor controls the workflow;
- allowable controls use semantic, bounded choices and the repository setting budgets.

## Product Launch

| Contract field | Specification |
|---|---|
| Merchant intent | Introduce one new or hero product with a clear reason to care and a direct path to correct product selection/purchase. |
| Shopper intent | Understand what is new, whether it fits, why to trust it, and what to do next. |
| Default composition | Campaign reveal linked to the product → concise benefit explanation → factual evidence → product handoff; PDP continues with factual purchase core → prioritized explanation/proof → optional honest comparison. Do not repeat the full campaign on PDP. |
| Required Shopify data | Product title, URL, price, availability, variants, featured/product media, description; page title if a campaign page is used. |
| Optional structured data | Benefits, usage, ingredients/materials, evidence/citations, launch date only when factual, FAQs, comparison dimensions. |
| Section responsibilities | Launch reveal orients; benefit section clarifies; evidence section substantiates; product handoff summarizes real facts and links; PDP product core transacts; product chapters resolve remaining questions. |
| Allowed merchant changes | Select product; choose concise/standard depth; replace claims/media; omit evidence/compare; reorder explanation and proof when comprehension remains; choose campaign destination. Product core facts cannot be disguised. |
| Mobile priority | Product identity, highest-value claim, price/status or direct product path early; secondary media/proof condensed; no full-screen media toll or competing sticky CTA. |
| Zero-setup behavior | Use product title, featured media, description excerpt, price/status, and product link. Omit unsupported proof/compare. The PDP alone remains complete if no campaign is created. |
| Empty/missing-data behavior | No media uses a composed text reveal; absent description yields facts and action without filler; unavailable/sold-out state stays accurate; broken structured references disappear with no empty chapter. |
| App-block opportunities | PDP purchase context for selling plans/personalization; supporting evidence/reviews seam; bounded campaign seam only if supported. Removal restores a complete path. |
| Accessibility risks | Media alternatives; heading duplication across handoff; variant/error/status announcements; video controls; focus and sticky overlap. |
| Performance risks | Hero/LCP media, duplicate campaign/PDP assets, video, product recommendations, app payload. Only the actual LCP candidate gets priority. |
| Meaningful difference | The launch is one cross-surface argument with controlled repetition and a factual handoff, not a hero plus generic feature rows assembled independently. |

## Paid Landing Page

| Contract field | Specification |
|---|---|
| Merchant intent | Match an advertisement's promise with a focused, measurable route to one legitimate destination. |
| Shopper intent | Confirm message match quickly, resolve the highest-risk objection, and reach the offer/product without distraction. |
| Default composition | Message-matched reveal → one explanation or proof module → product/collection destination → action. Compare only when required and supported; default navigation treatment is a prototype decision, not hidden by assumption. |
| Required Shopify data | Page title/content, destination product or collection, destination URL and standard product/collection facts. |
| Optional structured data | Campaign claim/evidence, source citation, objections/FAQs, product set, honest comparison data. Analytics remains platform/app responsibility. |
| Section responsibilities | Reveal establishes continuity; clarification answers one objection; evidence substantiates; destination module renders real Shopify facts; action hands off. |
| Allowed merchant changes | Choose destination, claim, proof, depth, section omission, and bounded emphasis. Cannot fabricate urgency, hide material purchase facts, or turn the page into an arbitrary section dump. |
| Mobile priority | Message match and destination visible with minimal delay; short proof; compressed media; one clear action; no repeated sticky layers. |
| Zero-setup behavior | Page title/content plus selected product/collection summary and link creates a restrained landing page. If no destination is selected, use an honest page CTA only when configured; otherwise show editor guidance, not a dead storefront action. |
| Empty/missing-data behavior | Missing campaign media becomes text-first; unavailable destination reflects status or omits the action; no claim/proof placeholders; long legal copy remains readable. |
| App-block opportunities | Generic campaign content seam for compatible apps; product-context app only where platform context is valid. Consent, analytics, forms, reviews, and subscriptions remain app responsibilities. |
| Accessibility risks | Over-aggressive focus/action treatment, embedded forms, unclear destination, hidden navigation, contrast, autoplay media. |
| Performance risks | Third-party ad/analytics scripts outside theme ownership, hero media, embeds, app forms. Attribute costs separately without excusing theme regressions. |
| Meaningful difference | Default omission and a claim-to-destination contract reduce assembly and drift; it is intentionally shorter than an editorial story, not a blank page with conversion sections. |

## Collection Launch

| Contract field | Specification |
|---|---|
| Merchant intent | Introduce a curated range while preserving fast product discovery and canonical collection behavior. |
| Shopper intent | Understand the edit, narrow choices, compare products, and enter the right PDP. |
| Default composition | Collection orientation → filter/sort/count and product grid → at most one early explanatory/editorial interruption → continued canonical grid; optional evidence near the relevant group. |
| Required Shopify data | Collection title, description/image when present, products, prices, availability, URLs, filters/sort/pagination data. |
| Optional structured data | Collection premise, buying guide, product relationships, evidence, comparison dimensions, promotional destination. |
| Section responsibilities | Collection reveal orients; grid owns discovery; editorial module clarifies the range; product cards expose stable facts; optional guide helps selection without changing canonical product semantics. |
| Allowed merchant changes | Choose orientation depth, editorial insertion from bounded positions, related story, card density, and permitted filtering presentation. Cannot insert faux product cards or alter counts/pagination with promotional content. |
| Mobile priority | Title/context → count/filter/sort → products; editorial content is brief or later; filter controls remain usable and stateful; quick actions do not obscure browsing. |
| Zero-setup behavior | Title, optional description/image, canonical grid, product facts, sort/filter/pagination. No promo tile required for polish. |
| Empty/missing-data behavior | Empty collection explains no products without fake recommendations; no-results retains filter recovery; missing image uses text orientation; product/card data degrades factually. |
| App-block opportunities | Bounded pre/post-grid content seams if supported; filter/recommendation integrations must not own canonical collection behavior. |
| Accessibility risks | Filter focus/state, result announcements, pagination, quick-add status, non-product tile confusion, heading/card link repetition. |
| Performance risks | Many product images, quick-add code, filters, editorial media, app injections, layout shift from mixed ratios. |
| Meaningful difference | Editorial explanation has a governed relationship to the collection and never impersonates or corrupts the product set; the workflow balances launch narrative with browse integrity by default. |

## Editorial Story

| Contract field | Specification |
|---|---|
| Merchant intent | Publish a brand, founder, ingredient/material, or cultural story that can lead naturally to commerce without becoming an advertorial template. |
| Shopper intent | Read, understand, trust, and optionally explore a relevant product or collection. |
| Default composition | Editorial reveal → readable narrative chapters → factual evidence/context where available → contextual product/collection references → optional next story/action. |
| Required Shopify data | Article or page title/content, author/date where applicable, media and links when supplied. Referenced commerce objects use native data. |
| Optional structured data | Pull quotes, sources, contributors, chapters, related products/collections, evidence, captions. |
| Section responsibilities | Editorial header establishes context; chapter sections maintain reading rhythm; evidence identifies support; commerce reference stays visually distinct from editorial content; continuation routes onward. |
| Allowed merchant changes | Add/reorder bounded chapters, media, quotes, evidence, and references; choose reading density. Cannot turn every paragraph into a setting or insert an aggressive purchase layer that overrides reading. |
| Mobile priority | Text readability, meaningful media/captions, compact commerce references, no sticky purchase UI, and safe long-form navigation. |
| Zero-setup behavior | Native article/page title and rich text render as a polished reading surface; related commerce is optional. |
| Empty/missing-data behavior | No hero image becomes typography-led; missing author/date omitted when not applicable; deleted references disappear; long text, tables/embeds, and captions remain resilient or are explicitly constrained. |
| App-block opportunities | Bounded inline or end-of-story seam for compatible forms/media/apps; apps cannot fragment every chapter. |
| Accessibility risks | Heading hierarchy from rich text, link purpose, captions/transcripts, pull-quote semantics, embedded content, reading order. |
| Performance risks | Long-page media, embeds, video, excessive chapter scripts, below-fold eager loading. |
| Meaningful difference | Commerce references participate in a controlled reading-to-discovery handoff while the surface remains genuinely editorial; it is not alternating generic image/text sections. |

## Product Education

| Contract field | Specification |
|---|---|
| Merchant intent | Explain use, suitability, ingredients/materials, specifications, care, or routine for a product/category with high consideration. |
| Shopper intent | Learn how it works, whether it fits, how to use it, and which option to choose safely. |
| Default composition | Question-led orientation → steps/benefits → factual evidence/specifications → optional honest comparison → product handoff or PDP purchase core. FAQ handles residual questions, not primary content. |
| Required Shopify data | Product or collection reference with title, description, media, variants, price/status and URL; page content if standalone. |
| Optional structured data | Steps, ingredients/materials, specifications, suitability cautions, evidence sources, FAQs, comparison dimensions. No medical efficacy claim is inferred. |
| Section responsibilities | Orientation scopes the lesson; steps explain use; specification/evidence blocks substantiate; comparison aids selection; handoff renders real product facts; PDP core transacts. |
| Allowed merchant changes | Select subject and lesson emphasis; add/reorder bounded steps/evidence; omit compare/FAQ; choose standalone or PDP continuation. Cannot hide safety/care context or create unsupported claims. |
| Mobile priority | Answer the top suitability/use question early; short ordered steps; accessible disclosures for secondary detail; product handoff remains obvious without persistent collision. |
| Zero-setup behavior | Product description, media, standard facts and option labels create a concise guide; absent structured steps becomes a readable explanation plus handoff, not empty numbered cards. |
| Empty/missing-data behavior | Missing evidence/compare omitted; missing media becomes text/facts; deleted referenced product disables/omits action; long ingredient/specification terms wrap and remain navigable. |
| App-block opportunities | Product-support, reviews/evidence, consultation/form, or compatibility seam where supported; app content is supplemental. |
| Accessibility risks | Dense tables/comparisons, disclosure names/states, ordered-step semantics, technical terminology, video transcripts, error-prone option handoff. |
| Performance risks | Tutorial video, many step images, comparison DOM size, embeds/apps, duplicated PDP media. |
| Meaningful difference | Education is a question-and-handoff contract reusable on campaign and PDP surfaces, with honest omissions and standard-data fallback—not FAQs and icon rows assembled manually. |

## Workflow validation gate

For each workflow, prototype one standard-data state, one enhanced state, one missing/long state, and a mobile priority variant. A workflow needs at least four valid paired B0/B1 observations from four merchants; with that sample, all four B1 tasks must be completed unassisted to meet the ≥80% workflow threshold, and the paired median time and decision count must both improve over B0. Every merchant must also complete at least four of their five assigned B1 representative tasks unassisted. Separately, the stripped shopper flow containing the workflow must pass the representative-shopper comprehension method in [`m1-prototype-plan.md`](m1-prototype-plan.md); expert review cannot substitute. Otherwise narrow, redesign, and retest the contract rather than hiding failure in an aggregate or adding controls.
