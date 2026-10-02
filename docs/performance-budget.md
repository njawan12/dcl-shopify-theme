# Performance budget

Shopify’s current minimum must be re-read at [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements#performance). Our internal target is deliberately higher and measured on realistic demo content, both mobile and desktop.

## User-experience budgets (75th percentile lab repeat set)

| Metric | Target | Hard regression gate |
|---|---:|---:|
| Lighthouse Performance, representative pages | ≥90 median | no run <85 without waiver |
| Lighthouse Accessibility | ≥95; goal 100 | no critical/serious automated issue |
| LCP | ≤2.5 s | ≤3.0 s |
| INP (field target; lab proxy documented) | ≤200 ms | ≤300 ms |
| CLS | ≤0.05 | ≤0.10 |
| Total blocking time (lab proxy) | ≤150 ms | ≤250 ms |

Lab scores are diagnostic, not promises about merchant apps/content or field Core Web Vitals.

## Payload/execution budgets (theme-owned, initial route)

| Resource | Budget |
|---|---:|
| Global CSS compressed | 45 KB |
| Global JS compressed | 25 KB |
| Any page-specific JS compressed | 20 KB |
| Total theme-owned JS compressed on a route | 45 KB |
| Initial theme-owned font transfer | 100 KB; prefer system/Shopify-hosted strategy |
| Third-party requests from theme | 0 |
| Long tasks >50 ms during load | 0 theme-caused on reference hardware |

Images are content-dependent; enforce responsive widths, accurate `sizes`, dimensions/aspect ratio, modern Shopify CDN formats, priority for the single LCP candidate, and lazy loading below fold. Never lazy-load the LCP image by default.

## Reference pages and fixtures

Test home editorial, 24-product collection with filters, media-heavy product (10 images + video), simple product, campaign page, search results, and populated cart. Use production builds, cold cache, consistent mobile throttling, three or more runs, median plus worst run, and saved reports.

## Engineering rules

- Useful server-rendered HTML before JS; progressive enhancement only.
- Import a component module only when its markup exists.
- Reserve image/media and dynamic UI space to prevent shifts.
- Prefer CSS for presentation; avoid animation/layout libraries.
- Abort stale fetches and limit observers/listeners.
- Theme-editor scripts do not leak across section reloads.
- Performance waiver requires measured evidence, owner and expiry.

## CI and release gate

Theme Check and static budgets run on every change. Lighthouse CI runs against a representative preview when credentials exist. Production-like store measurements require Shopify credentials and content; until supplied, this remains an explicit blocked check, never a pass.
