# Feature matrix

Priorities: **P0** initial commercial release; **P1** valuable follow-up; **P2** future consideration; **REJECT** deliberately excluded. Complexity/support assess delivery risk; differentiation assesses market distinctiveness.

| Feature | Priority | Merchant value | Complexity | Support risk | Differentiation | Scope note |
|---|---|---|---|---|---|---|
| Semantic global design tokens/color schemes | P0 | High | Medium | Low | Medium | Constrained brand system |
| Accessible header + mobile navigation | P0 | High | High | Medium | Medium | Two-level tested model; mega-menu promotions |
| Predictive search | P0 | High | Medium | Medium | Low | Native endpoint, resilient fallback |
| Stable product-card system | P0 | High | High | Medium | Medium | Price/status/alternate media |
| Native filtering/sorting + mobile drawer | P0 | High | High | Medium | Low | Server URL is source of truth |
| Product card quick add | P0 | High | High | High | Low | Simple products direct; complex opens choices |
| Legitimate badges | P0 | Medium | Low | Medium | Low | Sale/sold out/product data only |
| Collection promotional/story tiles | P0 | High | High | Medium | High | Clearly non-product and pagination-safe |
| PDP gallery: carousel + stacked desktop | P0 | High | High | High | Medium | Images/video/model compatible |
| Zoom/lightbox | P0 | Medium | Medium | Medium | Low | Accessible dialog |
| Product form/variants/quantity/unit price | P0 | High | High | High | Low | Shopify correctness first |
| Sticky purchase panel (desktop) | P0 | High | Medium | Medium | Low | Disable when unsuitable |
| Sticky mobile add-to-cart | P0 | High | High | High | Medium | No overlap with apps/OS chrome |
| Pickup availability | P0 | Medium | Medium | Medium | Low | Native availability data |
| Recommendations/complementary products | P0 | High | Medium | Medium | Low | Native APIs and empty state |
| Grouped accordions/highlights | P0 | High | Medium | Low | Medium | Dynamic sources optional |
| `@app` block surfaces | P0 | High | Medium | Medium | Low | Vendor-neutral |
| Launch Narrative System sections | P0 | High | High | Medium | High | Reveal/Explain/Prove/Compare/Act |
| Five intent-led native starting compositions | P0 | High | High | Medium | High | Product Launch, Paid Landing, Collection Launch, Editorial Story, Product Education; no proprietary builder |
| Optional metafield/metaobject recipes | P0 | High | High | High | High | Documentation + fallbacks |
| Cart page with errors/updates | P0 | High | High | Medium | Low | Server-correct baseline |
| Cart drawer | P1 | Medium | High | High | Low | Only after app/a11y validation |
| Localization/currency/long-text resilience | P0 | High | High | Medium | Medium | Logical layout, locale strings |
| Blog/article/pages/404/password/gift card | P0 | Medium | Medium | Low | Low | Required completeness |
| Product comparison section | P1 | Medium | High | High | High | Manual/native data only |
| Routine/collection builder editorial flow | P1 | High | High | Medium | High | Not an actual bundle engine |
| RTL production support | P1 | Medium | High | High | Medium | Commit only with native-language QA |
| Apparel/lifestyle/food-beverage presets | P2 | Medium | High | High | Medium | Only after architecture-fit evidence; narrow instead of adding generic controls |
| Advanced B2B/quantity rules UX | P2 | Medium | High | High | Medium | Re-evaluate audience |
| Reviews engine | REJECT | Low | High | High | Low | App responsibility |
| Subscription engine | REJECT | Low | High | High | Low | App/platform responsibility |
| Bundle engine | REJECT | Medium | High | High | Low | Use compatible app blocks |
| Loyalty/referrals | REJECT | Low | High | High | Low | App responsibility |
| Fake countdown/activity/scarcity | REJECT | Low | Low | High | Low | Misleading and approval risk |
| Arbitrary custom CSS per block | REJECT | Low | Medium | High | Low | Breaks consistency/supportability |
| Proprietary drag-and-drop page builder | REJECT | Low | High | High | Medium | Native editor is the platform |
| AI copy/image generation | REJECT | Low | High | High | Low | Rapidly commoditized/app-like |
| Client-side SPA storefront | REJECT | Low | High | High | Low | Performance and resilience cost |

P0 is still too large for a single implementation pass; the roadmap divides it into independently reviewable milestones. Any added feature requires a row before code begins.
