# Merchant pain points

## Evidence levels

- **Documented platform constraint:** supported by official Shopify documentation linked below.
- **Review pattern:** a recurring theme-review topic that must be quantified in the pre-M1 live review study.
- **Product hypothesis:** requires merchant testing; it is not represented as fact.

| Pain | Evidence level | Consequence | Product response | Guardrail |
|---|---|---|---|---|
| Campaign pages require template duplication or agency work | Product hypothesis | Slow launches and inconsistent pages | One campaign JSON template plus purposeful section presets | Not a proprietary page builder |
| Product education is copied into descriptions | Product hypothesis | Inconsistent hierarchy and hard updates | Optional metafield/metaobject recipes with plain-data fallbacks | No mandatory setup wizard |
| Huge settings panels hide common controls | Review pattern | Errors and support tickets | Basic controls, conditional advanced controls, semantic choices | Setting-count budget per section |
| App blocks look bolted on | Review pattern / platform capability | Broken spacing and conversion paths | Deliberate app-block slots and neutral wrappers | No vendor-specific CSS contracts |
| Upgrades overwrite custom code | Review pattern | Upgrade avoidance and security debt | Broad native capability, release notes, stable contracts | Never promise preservation of edits |
| Mobile galleries, variants, filters, and drawers conflict | Review pattern | Purchase friction | Mobile-first state diagrams and device QA | Avoid stacked sticky UI |
| Variant swatches are inconsistent | Product hypothesis | Selection errors | Shopify-native option values and graceful text fallback | Do not infer color from names only |
| Promotional badges imply false scarcity | Policy/ethics risk | Trust and approval risk | Only objective product/price/inventory data | Reject fake countdowns and visitor counters |
| Large catalogs become slow and hard to scan | Product hypothesis | Discovery failure | Server-rendered filters, stable cards, pagination, restrained quick add | No client-side catalog framework |
| Long translations break polished compositions | Known localization risk | Truncation/overflow | Flexible layouts and pseudo-localization | Never encode text in imagery |
| Merchants cannot tell what will happen when data is absent | Review pattern | Empty gaps and support demand | Explicit editor help and graceful omission | Preview all empty states |
| “Flexible” themes produce inconsistent brands | Product hypothesis | Store looks templated or broken | Constrained tokens and opinionated presets | No arbitrary per-block pixel controls |
| Merchants begin from a blank canvas or irrelevant section list | Product hypothesis | Slow assembly and incoherent campaigns | Native job-led starting compositions | Presets remain editable; no proprietary builder |
| Routine edits require developer interpretation | Product hypothesis | Cost, delay and fragile source edits | Semantic controls, strong defaults and documented boundaries | Do not imply support for custom business logic |

## Jobs to be done

1. “When a product launches, help me publish a credible PDP, collection moment, and landing page in hours without a developer.”
2. “When content changes by product, let my team update structured information once and reuse it safely.”
3. “When I run a promotion, let me emphasize legitimate offers without damaging trust or mobile usability.”
4. “When our catalog grows, keep navigation and product comparison understandable.”
5. “When apps are installed, provide stable insertion points without making the theme depend on them.”
6. “When I start a commercial job, give me a coherent native composition whose next decisions I understand.”

## Custom-code requests to quantify

The review study should specifically count requests for PDP block rearrangement, sticky add-to-cart, swatch/card behavior, promotional tiles inside collections, mega-menu imagery, variant-specific media, metafield-driven accordions, badges, mobile spacing, app placement, and new landing templates. These are hypotheses until coded from evidence.

## Platform references

[Dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources), [metafields](https://shopify.dev/docs/apps/build/custom-data/metafields), [metaobjects](https://shopify.dev/docs/apps/build/custom-data/metaobjects), [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), and [product recommendations](https://shopify.dev/docs/storefronts/themes/product-merchandising/recommendations).
