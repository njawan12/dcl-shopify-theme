# Theme Store build

Date: 2026-10-15. Builds on the tested `m2-production-theme` commerce core. The M0/M1 research gates are retired; Theme Check, the structural validator, unit tests and the browser suite remain the quality bar.

## Added

**Signature sections**
- **Living Canvas** (`living-canvas`): one hero section, three compositions.
  - Monument: oversized type, image anchored by a rule, live product object, proof points rail.
  - Edge Crop: clip path cut on the merchant's own image, numbered image details. Native popovers on wide screens; a plain numbered list on phones and older browsers.
  - Quiet Frame: product led launch hero with real price and a direct add to cart only when no option choice is needed.
- **Guided set** (`guided-set`): the Split Tension routine builder. Shoppers tick steps and add them in one request; the total is the honest sum of prices. Without JavaScript every step keeps its own native product form. Products with options link to the product page instead of guessing a variant.
- **Commerce Mosaic** (`commerce-mosaic`): featured collection with three rhythms (even grid, lead product, story break). Product count adapts so rows stay full.

**Standard library:** collection list, image with text, rich text, feature facts, customer quotes, video (uploaded or YouTube/Vimeo, never autoplay), email signup, logo list, questions (FAQ), announcement bar.

**Theme wide:** Vela preset (Fraunces + Geist, sage palette), Vela homepage composition in `templates/index.json`, sticky header option, announcement bar in the header group, redesigned blog grid, article and collection headers. New CSS lives in `assets/canvas.css`; new JS is `assets/guided-set.js` only, loaded by that section.

Every new section has presets, translated schema labels, placeholder states for a fresh store, at most 12 settings and at most 8 settings per block.

## Verified

- Theme Check: no offenses.
- `tests/m2/validate.py`: all structural, locale, budget and preservation checks pass.
- Unit tests 46/46; browser suite 369 assertions / 128 observations pass.
- Local Liquid render of every new section at 1440 and 390 px: no horizontal overflow, no console errors, guided set total and image detail popovers work.

## Still needed before submission

1. Upload to `dcl-theme-dev` and review in the real Theme Editor, including adding each section from scratch.
2. Vela demo store: real products, photography and collections.
3. Real product photography in the hero (shipped defaults use Shopify placeholders).
4. Theme Store listing: screenshots, description, documentation page and support contact.
5. Accessibility pass with a screen reader, plus Safari and Firefox checks.
6. Optional: mobile slide out menu and a cart drawer.
