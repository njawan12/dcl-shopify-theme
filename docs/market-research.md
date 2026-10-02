# Market research

**Research date:** 2 October 2026
**Decision status:** directional, with a mandatory live-data refresh before investment approval

## Method and evidence standard

The repository contained no prototype or prior research at the start of M0. This study uses the official Theme Store taxonomy, product-page feature vocabulary, Shopify developer documentation, and publicly observable merchant-review patterns. A network proxy blocked live retrieval during this work; therefore volatile facts (price, preset count, review count/rating, current browser and Lighthouse thresholds) are explicitly marked **REVALIDATE**, never presented as current fact. Review count is treated as adoption evidence, not sales evidence.

Sources to re-open during the approval gate: [Theme Store](https://themes.shopify.com/), [Theme Store collections](https://themes.shopify.com/collections), [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements), [theme architecture](https://shopify.dev/docs/storefronts/themes/architecture), and each linked listing below.

## What the market signals

1. Theme Store discovery is organized around industries, catalog size, and capabilities. Merchants shop for a credible fit, not merely an aesthetic.
2. Mature premium listings converge on mega menus, filtering, quick buy, swatches, sticky purchasing, promotional tiles, and rich media. Those are table stakes, not a defensible proposition.
3. Review narratives (to be re-counted) recurrently reward fast, specific support and criticize regressions, app conflicts, unclear settings, mobile defects, and upgrade friction. Support operations are part of the product.
4. “High volume” and “visual storytelling” are both crowded claims. A new product needs a coherent workflow advantage rather than a longer checklist.
5. Shopify’s native platform keeps absorbing commodity theme features. Durable value lies in information architecture, art direction, merchant workflows, accessibility, and quality—not an imitation app.

## Competitor sample

The required four are joined by Broadcast, Symmetry, Motion, and Pipeline because they represent adjacent editorial, promotion-heavy, catalog, and motion-led positions. Details are in [the competitor matrix](./competitor-matrix.md).

| Theme | Observable positioning | Official evidence |
|---|---|---|
| Prestige | Premium/luxury imagery and editorial storytelling | [Listing](https://themes.shopify.com/themes/prestige) |
| Impulse | Promotion-led, high-conversion merchandising | [Listing](https://themes.shopify.com/themes/impulse) |
| Impact | Bold, modern visual presentation and conversion features | [Listing](https://themes.shopify.com/themes/impact) |
| Enterprise | Large-catalog/high-volume operations and fast purchase paths | [Listing](https://themes.shopify.com/themes/enterprise) |
| Broadcast | Editorial content plus product discovery | [Listing](https://themes.shopify.com/themes/broadcast) |
| Symmetry | Broad catalog and promotion flexibility | [Listing](https://themes.shopify.com/themes/symmetry) |
| Motion | Motion-forward brand storytelling | [Listing](https://themes.shopify.com/themes/motion) |
| Pipeline | Image-led editorial commerce | [Listing](https://themes.shopify.com/themes/pipeline) |

## Segment assessment

| Segment | Demand hypothesis | Competition | Product opportunity | Verdict |
|---|---|---|---|---|
| Fashion/apparel | Large, visually demanding, variant-heavy | Very high | Strong but costly support around swatches/sizing | Secondary preset |
| Beauty/skincare | Repeat purchase; structured education; launches | High | Benefits, routines, ingredients and proof can share one grammar | **Primary** |
| Wellness/supplements | Education and subscriptions matter | Medium-high | Regulatory claims and subscription expectations raise risk | Adjacent, carefully scoped |
| Food/beverage | Bundles, subscriptions, gifting | Medium | Strong campaigns, but freshness/shipping logic belongs to apps | Later preset |
| Home/lifestyle | Storytelling and specifications | High | Larger media/specification needs; fewer repeat launches | Adjacent |
| General high-volume | Broad audience | Very high | Becomes generic and checklist-led | Reject as positioning |

## Customer hypothesis to validate

The best initial customer is a design-conscious beauty, personal-care, or adjacent wellness DTC team with roughly 20–500 products, frequent launches, a marketing manager operating the theme editor, and enough revenue to value reduced agency dependence. Catalog range is a design target, not a promise that every enterprise workflow is native.

## Primary research still required

Before M1, DCL should conduct 8–12 structured merchant interviews, review at least 50 recent reviews across the sample, record Theme Store listing facts in a dated spreadsheet, and run task-based teardowns of live demos on phone and desktop. Questions must test campaign creation time, PDP maintenance, structured content adoption, app-block friction, and upgrade pain. This is a go/no-go gate, not optional validation.

## Facts versus hypotheses

- **Verified, stable documentation:** Shopify supports JSON templates, sections/section groups, theme blocks, app blocks, dynamic sources, metafields and metaobjects; see linked developer documentation.
- **Observable but volatile:** listing prices, presets, review totals, sentiment ratios, and advertised feature tags. All are **REVALIDATE**.
- **Hypothesis:** a guided “launch-to-library” workflow will create willingness to pay. It requires interviews and usability tests.
- **Unknown:** sales volume, conversion lift, and competitor support-ticket volume. Public reviews cannot establish these.
