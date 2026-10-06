# M2A live integration gate — access checkpoint

2026-10-06. **M2A LIVE GATE NARROW — browser authentication required.**

Authorized store: dcl-theme-dev.myshopify.com. Shopify CLI4.8.4 uploaded the exact theme/ at b8d10863e668d8660b8b509ff2416f52620a894a as new development theme185844367583 (m2a-live-gate-b8d1086). Upload exit0, Theme Check[], no reported Liquid/schema/template upload errors. Existing live/unpublished themes were not targeted. This proves upload acceptance, not runtime integration correctness.

[Preview](https://dcl-theme-dev.myshopify.com/?preview_theme_id=185844367583) redirects to the password gate. [Theme Editor](https://dcl-theme-dev.myshopify.com/admin/themes/185844367583/editor) redirects to Shopify account login in the in-app browser. Native Chrome capture is unavailable because macOS screen-capture permission was denied. No credentials/passwords were read, changed or committed. No protection bypass or theme publication.

Required next human action: sign in to Shopify in the Codex in-app browser and open the above Theme Editor for this development theme. Resume after successful editor access; storefront password/access may then be resolved within the authorized store. No account identifier or password was invented.

All remaining live-gate steps are unexecuted: catalog/state manifest; desktop/mobile smoke; real product/cart/checkout-boundary JS-on/off journeys; editor operations; app insertion/embeds; Markets; search/filter; accessibility/reflow; populated-page Lighthouse. No functional failure or PASS is inferred. No theme source changed, so no source-change CI rerun is required. Preserved prototypes and later signature systems remain untouched.

Machine record: upload-and-access.json. Stop for browser-login handoff.
