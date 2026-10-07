# M2B production completion report

Date checked: 2026-10-07. Store: `dcl-theme-dev.myshopify.com`; existing unpublished development theme **185844367583**. Branch: `m2-production-theme`. Accepted M2A base: `7b75cf1f6c45f302f8c72893123dec23446d57cd`. No theme publication, new theme, merge, PR, preserved prototype edit, Commerce Mosaic or Guided Set production work.

**Human visual verdict: PENDING HUMAN REVIEW.** The engineering results below do not award premium visual acceptance.

## Implementation and dispositions

| Area | Engineering disposition | Delivered behavior and boundary |
| --- | --- | --- |
| Balanced | PASS | Default gallery/purchase relationship, bounded first four media with native all-media disclosure, clear native purchase hierarchy, education after purchase. |
| Compact | PASS | Wide compact media matrix, distinct full-width decision band with purchase action lane, education below. Same product resolver and purchase form. |
| Editorial | PASS | Dominant media lead, narrative/attached Note beside purchase, Pair/Process education below. Deterministic mobile groups; purchase remains explicit. |
| Evidence Rail | NARROW | Shared manual-first Note, Pair and ordered Process; omission/qualification/source semantics, PDP and real storefront story proof. Generic native app guests. Genuine merchant provenance, metaobject/metafield lifecycle and full story editor/app rendering are not certified. |
| Header/footer/global | PASS for implemented structure and scoped checks | Original typography, semantic palette, restrained borders, primary/secondary/native form hierarchy; single navigation source, subordinate native localization, platform account, finished footer/card/page grammar. Human visual quality remains pending. |
| Commerce regression | PASS for executed journeys | Shared canonical identities/prices/allocations; real browser variant links and native add/update/remove/cart paths, JS on/off. No API cart mutation substitutes for browser action. |
| Real editor | NARROW | Saved Balanced→Compact→Editorial→Balanced switch with portable blocks; authored Note/Pair/Process; native Shop app inserted and preview removal/restoration; compatible `product.title` dynamic-source connection/restoration. Home/story editor iframe unavailable in this IAB session; storefront story proof separate. |
| Accessibility | NARROW | Scoped component/real Chromium checks, 320px and controlled 200% text, keyboard/focus observations, reduced motion and generic app containment. External preview iframe defect retained; no WCAG/AT/zoom certification. |
| Performance | NARROW — bounded lab evidence complete | Final lab medians remain strong; raw Shopify samples and elevated-TBT outlier retained, platform/unattributable runtime cost and variability investigated. Lab scores are not field performance certification. |

The default theme uses normal Shopify product records and default font/palette/layout roles. Shipped templates contain no invented evidence, rating, review or certification. Development evidence is expressly qualified demonstration content stored separately from shipped defaults. No new custom media or imported theme system. Compact/Editorial optional native templates differ only by semantic composition and retain their view context in native option/plan navigation.

Merchant ordering is preserved **within authored semantic groups**. Compact quantity/buy/pickup become the action lane; all other purchase context, including app/Custom Liquid, stays in the decision lane. Editorial description/Note form the narrative group; CSS places it beside purchase on desktop, while commerce precedes narrative in mobile source order. Pair/Process follow as education. Balanced/Compact description/attachments follow commerce. Switching is not unrestricted cross-group placement.

## Test and source provenance

Final theme implementation source: `394152fe95919d36b8aa88ac2311d7bf77153ae9`. It includes the evidence completeness correction and purchase-first mobile order. Capture navigation fix: `d0779888134041739c7cd9d22498d4aebfd646aa`. Exact final evidence commit/parent and remote verification are reported with publication; this document does not self-reference its containing commit.

Commands reused: `shopify theme check --path theme --fail-level warning --output json`; `M2_EVIDENCE_DIR=... python3 tests/m2/validate.py`; `npm --prefix tests/m2 test`; `npm --prefix tests/m2 run test:browser`; `node tests/m2/live-shopify.mjs` with authorized temporary preview secret and explicit phases; `shopify theme package --path theme` plus `tests/m2/package-check.py`.

Live regression run [37640188275](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37640188275): PASS, two JS-on/off browser journeys, 30 surface observations, native cart update/note/remove and checkout boundary. Catalog run [37640193193](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37640193193): PASS, real no-media/two-option/unit-price nonexistent-tuple recovery, weekly plan native cart and password observations. Both use source `77c9f4733a77aa18e2be997fabfdb6ad8e63bfb4`; subsequent theme changes tighten evidence completeness/editor ownership and Editorial mobile source order, preserving native commerce and JS. Final signature run rechecks all three native journeys against those final snippets.

Original signature [37640525182](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37640525182): functional PASS, six JS-on/off composition purchase journeys plus six JS-off advanced journeys, 36 fixture/composition/width observations, 24 stress observations and 72 keyboard observations. Its screenshots were superseded because one image had not finished decoding and preview chrome obscured content. Its raw performance history is retained, not selected away.

Attempts retained: `37640184372` failed on an ambiguous generic header selector matching platform account UI; corrected to `.site-header`. `37646516220` deliberately cancelled for a screenshot readiness correction. `37646973612` failed at capture on native preview-bar navigation destroying the page context; corrected by waiting for that actual navigation. These are harness failures, not converted functional passes. Expanded repeated-instance CI runs `37648053309` / `37648543862` failed because `HTMLFormElement.id` was masked by its native input named `id`, serializing an input Node twice. The literal `getAttribute("id")` assertion correctly checks unique IDs; no source IDs were changed. Run `37648857446` passed the expanded matrix.

## Real platform fixture and journey matrix

Six real products × three compositions × 1440/390 = **36** observations: Complete Snowboard; native two-option/no-media test product; Selling Plans Ski Wax; sold-out Snowboard; compare-at Snowboard; Videographer Snowboard. Ordinary product additionally covers 320,375,430,768,1024,1280 for all three structures; 1440/390 complete the eight-width matrix. Independent controlled 200% text at 320 and reduced-motion observations for each composition.

Native regular journeys: product `15414509732063`, Dawn variant `67931960606943`, quantity **2**, **69995 USD minor units per item**, browser-submitted cart. Six journeys = three structures × JS on/off contexts. Advanced JS-off journeys each composition: absent Large/Gloss tuple has no invented price/purchase, native Small recovery yields variant `67933304029407`, **1200 USD minor**, unit **600 USD minor**; weekly plan `8657469663` on variant `67931960738015` yields **2121 USD minor**. Read-only `/cart.js` independently verifies those browser submissions; it does not mutate the cart. Native removal restores empty cart after each exercise. Tests use US Markets context; CA stock/price differences are genuine platform data.

App proof: actual installed **Shop / Sign in with Shop Button** in native `@app` render dispatch, observed across 36 PDP states, outside evidence lists, normal flow. Native editor insertion saved; removal/restoration preview executed. Artificial tall/wide guest containment is separately labeled a component harness stress, not a real vendor app. No vendor-specific integration, app embed execution, app authentication, wallet transaction or universal app compatibility claim.

## Complexity and control budget

Machine report: `complexity.json`; exact changed production manifest included there.

- Global settings **19 → 19** (17 presentation, two platform brand inputs).
- Main/featured product: **one** composition select, three semantic values. Max section blocks **15 → 18**; each evidence type limit one.
- Note **27 IDs** = two presentation +25 content, max three records. Includes subject heading and 3×8 content fields.
- Pair **34 IDs** = three presentation +31 content; before/after OR comparison, max four complete comparison rows. Conditional visibility exposes the active mode; inactive values preserved.
- Process **26 IDs** = two presentation +24 content; max four valid ordered steps. One remaining step stays an ordered process.
- Story host **five IDs** = attachment select +four subject fields, Note OR Process plus generic app guests, max eight blocks. Footer adds one brand-context content field; four total existing/new fields.
- CSS **8344 → 20653 raw bytes** (+12309); gzip **2391 → 4610** (+2219). JS assets byte-identical; zero new runtime JS/state. Breakpoint union **600/750/990 unchanged**. No raw CSS setting was introduced, arbitrary coordinates, device builder, nested evidence builder or second commerce form/state implementation.

Evidence completeness: invalid required fields omit records; metric may remain as supplied with honest absent source, no fabricated source. Quotes require attribution and explicit merchant-authored role; certifications require issuer. Before/after requires heading, both actual media, explicit labels and nonblank supplied/native alternatives; incomplete pair omitted. Comparison requires heading, named subjects and complete rows. Process requires heading and valid instruction steps. Source links are structurally rendered only; theme assesses no credibility or claim truth.

## Official architecture checks

Rechecked 2026-10-06/07 using official Shopify documentation: [app blocks](https://shopify.dev/docs/storefronts/themes/architecture/blocks/app-blocks), [dynamic sources](https://shopify.dev/docs/storefronts/themes/architecture/settings/dynamic-sources), [input settings](https://shopify.dev/docs/storefronts/themes/architecture/settings/input-settings), [Theme Store requirements](https://shopify.dev/docs/storefronts/themes/store/requirements). Section-local native `@app` dispatch and compatible manual/source inputs retained. Text-bearing merchant content uses native translatable settings. Submission certification is distinct from this bounded development gate; originality/foundation decision remains the accepted original ADR.

## Remaining production/integration/certification gates

Retain M2A gates: genuine issued gift cards/redemption and recipient cart submission; enabled pickup, nondefault quantity rules, advanced B2B, annual/renewal/plan changes; real >24-item pagination, broad filtering/search/third-party filtering; additional languages/currencies and real RTL/full Markets/tax/duties; app embeds and broader app vendor/auth/wallet execution; real zoom, screen readers/AT, full keyboard/error audit and every merchant palette; Safari/Firefox/physical touch and lifecycle endurance; production/field INP/CWV and realistic full catalog/app budgets; merchant usability study; paid checkout/payment/fulfillment/accounts.

M2B additions: genuine merchant evidence/provenance and authoring study; real custom metafield/metaobject connection/disconnection lifecycle beyond the executed native product-title binding; real before/after sourced media (unit semantics proven, no fabricated clinical/material result); home/story Theme Editor preview execution in a working environment; full editorial/story app lifecycle and more vendors; final full-theme integration and premium art direction/human review. Expanded text is feasibility, not real localization or native zoom certification. Contrast automated incompletes and external `PBarNextFrame` naming findings remain recorded. No human visual PASS or production Theme Store compliance is claimed.

Temporary signed preview credentials, cookies and checkout session identifiers are excluded from durable evidence. The Actions secret is removed after the final run; no store password/authentication changes. Final working tree and remote SHA are verified after committing evidence.

## Final production CI

[37649193990](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37649193990), source `394152fe95919d36b8aa88ac2311d7bf77153ae9`: **PASS**. Theme Check has zero errors/warnings; **1172/1172** structural/schema/locale/budget/preservation checks; **46/46** unit tests; **369 browser assertions /128 observations**. Eight widths × JS on/off × eight routes. Each of three maximum/long-content routes renders two production instances with three Note records, four complete comparison rows and four Process steps; native form association and unique literal DOM IDs checked. This is a component harness with disclosed platform adapters, not a real Shopify evidence source. Packaging/source identity is in `ci/package-results.json`.

Read-only remote pull verifies exact source hashes for `base.css`, product surface, Note, Pair and Process. `editor/remote-source-verification.json` records the three actual development template compositions and qualified test configuration. The public signature evidence uses those configurations, not fabricated theme defaults. Product editor final state remains saved Balanced; no theme publication or other-theme mutation.

Final-source regression attempt `37649362908` stopped before cart submission: the preview-bar pointer target lay outside its mobile iframe viewport. The capture helper now activates the native button by keyboard once during context setup, before any variant/quantity state; screenshot observation is read-only. This avoids both the viewport obstruction and a toolbar-triggered reload resetting shopper fields. No commerce or theme implementation was changed for this harness correction.

## Final real Shopify runs and visual evidence

[Signature run 37649193805](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37649193805), theme source `394152fe95919d36b8aa88ac2311d7bf77153ae9`: **PASS executed functional checks**, Chromium **151.0.7922.34**, Playwright1.62.1, Ubuntu24.04. Six JS-on/off native product/variant/quantity/cart journeys +six JS-off advanced tuple/unit/plan journeys; **63** captured surface observations, **36** app-host observations, **24** stress records and **72** keyboard records. Final composition axe reports have no violations in the measured contexts after native preview-bar dismissal. Earlier platform iframe findings remain in performance-history/regression artifacts rather than being silently removed from the audit record.

[Final native regression 37649974374](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37649974374), harness source `3609df16ef3c7670b95b9409d833b5077429fa1e` with identical theme source: **PASS**, both JS-on/off purchase/cart/update/quantity/note/removal journeys, JS-on checkout boundary, 30 surface observations. Final harness production CI [37649973886](https://github.com/njawan12/dcl-shopify-theme/actions/runs/37649973886) also **PASS**. No mocked mutation or script-removal fallback substitutes for real native commerce. `javaScriptEnabled: false` is the browser-context policy for every JS-off journey.

Controlling images in `live/signature/`:

- `balanced-ordinary-1440.jpg`, `balanced-ordinary-390.jpg`
- `compact-ordinary-1440.jpg`, `compact-ordinary-390.jpg`
- `editorial-ordinary-1440.jpg`, `editorial-ordinary-390.jpg`
- `balanced-complex-1440.jpg`, `balanced-complex-390.jpg`
- `home-1440.jpg`, `home-390.jpg` (header, default home and footer)
- `story-1440.jpg`, `story-390.jpg` (real editorial attachment)
- `editorial-neutral-1440.jpg`, `editorial-neutral-390.jpg`

Each PDP frame also captures its actual authored attachments; all six fixture types across all compositions are available beside these. Neutral frames use disclosed diagnostic CSS on the **real Shopify DOM** for system fonts/monochrome semantic roles/no motion; native ordinary non-beauty product photography/data remains. No harness screenshot is mislabeled real Shopify evidence. `editor/final-product-editor.png` records native saved editor context; detailed editor operations and limitations are in `editor/operations.json`.

## Final Lighthouse assessment

Lighthouse13.5.0, same real Chromium151; **24 reports** = four actual surfaces ×mobile/desktop ×three repetitions. Table reports medians, not best runs. Accessibility scores are automated lab scores.

| Surface | Mode | Performance | Accessibility | LCP ms | CLS | TBT ms |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Home | Mobile | 99 | 96 | 1716.7 | 0.0008 | 2.5 |
| Balanced | Mobile | 95 | 97 | 1691.6 | 0.0157 | 2.5 |
| Editorial | Mobile | 98 | 97 | 1674.2 | 0.0009 | 0 |
| Collection | Mobile | 98 | 95 | 2122.4 | 0.0074 | 49.5 |
| Home | Desktop | 100 | 96 | 455.7 | 0.0006 | 0 |
| Balanced | Desktop | 100 | 97 | 520.8 | 0.0153 | 0 |
| Editorial | Desktop | 100 | 97 | 504.0 | 0.0034 | 0 |
| Collection | Desktop | 100 | 95 | 543.9 | 0.0053 | 0 |

M2A's single mobile baseline scores were 96/96/96 home/product/collection, with LCP2632/2551/2204ms. Final M2B medians are99/95/98 and1717/1692/2122ms; desktop remains100. Earlier M2B mobile samples were slower and retained in `live/performance-history/`; no claim every run clears an internal90 performance target. Final Balanced sample2 scored **89**, TBT**441ms** with LCP1370ms. Its long-task audit attributes232ms to Shopify WPM and several substantial tasks as unattributable; no new theme JS was introduced. This supports investigating platform/runtime variance, **not assigning all overhead conclusively to a third party**. Keep performance NARROW for variability/full-store certification, rather than hiding the sample or removing required Shopify scripts. INP is unavailable as a real-user field metric in lab. No sustained material median regression is demonstrated in this bounded matrix.

Raw final reports: `live/signature/lighthouse-*.json`; machine medians/ranges in `live/performance-summary.json`. Full changed-file manifest: `changed-file-manifest.json`; production-only paths and exact bytes/control counts: `complexity.json`. CI results: `ci/`; real native regression: `live/regression/`; native catalog history: `live/catalog/`. Each result pins its actual source/run; snapshots do not imply later certification.

The temporary Actions preview secret was deleted after both final live runs, and `gh secret list --json name` returned an empty list. The local signed URL file was removed; evidence scanning finds no signed preview credential. The existing draft theme is available for human visual review; publication remains prohibited. Source integrity/preservation/package checks pass, limitations remain explicit and human visual verdict remains pending.

**M2B READY FOR HUMAN VISUAL REVIEW**

**Human visual verdict: PENDING HUMAN REVIEW.** Stop; no next signature production work authorized by this result.
