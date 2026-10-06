# M2A production provenance

2026-10-05. ADR-001 selects fully original code. Every `theme/` Liquid/JSON/CSS/JS/locale file in this batch is authored for this repository. No theme source, tokens, CSS, component implementation, preset or production assets were imported from Dawn, Horizon, Skeleton or an incumbent. Source inspection during ADR was reference-only, outside the production root. Platform API/form/filter names are public Shopify contracts.

No first-party raster/media/icon/font binaries are shipped. Merchant media uses Shopify CDN; fonts use Shopify font_picker/font_face. QR vendor script/Apple Wallet badge and model-viewer UI are Shopify-provided platform dependencies loaded only on applicable surfaces; those are not theme-source inheritance. Their generated internals/third-party licensing remain platform-owned and require live compatibility checks. Branded account/checkout/Shop-follow controls are rendered by Shopify, without recoloring or imitation.

Development tools only, excluded from ZIP: Shopify CLI4.8.4; LiquidJS10.30.0 (MIT), Playwright1.62.1 (Apache-2.0), axe-core Playwright4.13.0 (MPL-2.0). Exact npm integrity hashes are in `tests/m2/package-lock.json`. LiquidJS's platform adapters are explicitly test-only; they do not implement a storefront or establish Shopify server compatibility.

Current official references: the foundation dated register plus M2A pre-code contract. No license notice has been removed from inherited code because no theme code is inherited. Generated code needs ongoing authorship/dependency review; a keyword check alone cannot prove provenance.

Package boundary: only supported directories under `theme/`. Docs/tests/tooling/evidence/node_modules are excluded. Preserve all baseline files and M1 JS-OFF-01 workflow unchanged. Every production change must extend this ledger when adding third-party assets/code; real merchant demo/evidence media licensing remains a later gate.
