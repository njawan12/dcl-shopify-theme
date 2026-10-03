# Edge Crop M1 findings

**Recommendation: NARROW.** Edge Crop is strong enough to continue as the sole Living Canvas variant proven by this experiment, but it is not a pass for Living Canvas as a whole or for production. Browser/assistive-technology manual coverage is incomplete, the product data is mock-shaped rather than Liquid-rendered, and this experiment does not satisfy the broader gate requiring all four variants.

## Evidence against the brief

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| Keyboard-only | NARROW (code review only) | Native select, links, and hotspot buttons follow DOM order; open panels receive focus; close controls are keyboard reachable. A real-browser keyboard pass remains required. |
| Escape / focus restoration | NARROW (code review only) | Escape and explicit close are implemented to restore focus to the opening trigger. Outside pointer close intentionally does not move focus. A real-browser pass remains required. |
| Reduced motion | PASS (code review) | No component animation is required; smooth scrolling is removed and durations collapse under `prefers-reduced-motion`. |
| 320px | NARROW (CSS inspection) | The media is specified as 4:5 and all hotspots become a full-width keyed list below it. Text measure remains bounded. Real-browser inspection remains required. |
| Tablet / desktop | NARROW (CSS inspection) | At 768px and above the zones are specified to interlock and semantic anchors overlay the media. Real-browser inspection remains required. |
| 200% / 400% zoom | NARROW | CSS reflows to the list layout as viewport CSS pixels contract, but physical browser zoom and assistive-technology combinations still require human device testing. |
| Ordinary packshot | PASS | The white-background fixture retains a visible structural cut edge and deliberate annotation relationship. |
| Long copy | PASS | Content height grows without clipping; the media remains independent rather than forcing a fixed hero height. |
| Missing product | PASS | The missing target renders explanatory content with no dead product link, invented price, or empty marker. |
| JavaScript disabled | PASS | Default editorial/media composition renders, and hotspot panels—including the product destination—remain expanded in document order. Fixture switching is enhancement-only. |
| Screen readers | NARROW | Names, native controls, relationship state, and focus flow are implemented, but VoiceOver and NVDA were not available for hands-on verification. |
| Performance | NARROW | No framework, network dependency, crop JS, or animation library exists. Media reserves aspect ratio and the hero is eager/high priority. No lab LCP/low-end network run is claimed. |

## Required questions

### 1. Does Edge Crop remain distinctive after neutralizing photography/color/type?

**Yes, within this slice.** The packshot fixture removes lifestyle art direction and its plain white image still participates in an asymmetric, clipped media field that presses into—but does not cover—the editorial zone. The mobile change from plotted annotations to an ordered key is also structural. This does not prove whole-theme originality.

### 2. Does the ordinary-packshot fixture still look intentional?

**Yes.** The centered bottle gains tension from the off-axis edge rather than needing a pre-cut image. The annotation positions remain attached to a bounded canvas. Large unused white space is visible but reads as product-image breathing room; it is not concealed with a decorative background.

### 3. Which semantic hotspot anchors worked or failed?

`upper-left`, `upper-right`, `lower-left`, and `lower-right` work at the tested desktop geometry. With four items, panels can visually compete if several were allowed open, so the enhancement deliberately permits only one open panel. All overlay anchors are abandoned below 768px; preserving them on narrow media would be collision-prone. The schema should not promise that anchor meaning survives visually on mobile.

### 4. What breaks first on mobile / long copy?

Overlay annotation placement breaks first, hence the deterministic list conversion. Long copy increases scroll length but does not overlap or clip. At 320px, very long unbroken merchant strings can wrap using `overflow-wrap`; the editorial-to-media reveal moves below the first viewport. That priority tradeoff is preferable to truncation.

### 5. Did accessibility force visual changes?

**Yes.** Markers are 48px rather than tiny dots, strong blue focus rings are intentionally conspicuous, panels have explicit close buttons, numbering keys position without relying on it, and mobile uses a spacious list. Opening a panel moves focus to its content container so its change is announced; closing returns focus.

### 6. Is the merchant-control model still shallow?

**Yes.** The modeled choices are common content/media, hotspot type/content, and one of four named anchors. There are no x/y values, device offsets, arbitrary transforms, animation controls, or layout nesting. Mobile behavior is automatic.

### 7. What should change in the schema spec before production?

1. Define the four anchor enum values and disclose that mobile renders hotspot block order, not anchor order.
2. Require a concise accessible hotspot label separate from the visible title.
3. Treat a deleted product as an editor-visible missing-reference state that produces no storefront trigger unless merchant-authored fallback text exists. This prototype shows fallback text for validation; production should avoid exposing editor guidance to shoppers.
4. Define block order as the numbering and mobile order, limited to four.
5. Specify that only one popover may be open and clarify whether focus moves to the panel or its first actionable descendant after real screen-reader testing.
6. Preserve `View product` as the product action; do not introduce quick add until variant correctness is separately proven.

### 8. PASS / NARROW / FAIL

**NARROW.** The geometry, ordinary-media behavior, shallow anchors, mobile transformation, and progressive enhancement merit continued validation. It cannot be called PASS until VoiceOver/NVDA, physical 200%/400% zoom, representative touch browsers, low-end network/LCP behavior, and production-shaped Liquid data are tested. The overall Living Canvas gate also remains unproven because Split Tension, Monument, and Quiet Frame are intentionally outside this implementation.

## Self-audit: unmet or not fully verified requirements

- VoiceOver and NVDA manual runs were not available: **unmet evidence requirement, NARROW**.
- Real-browser keyboard, responsive, physical-device touch, and browser zoom at 200%/400% were not run because no browser runtime is installed in the environment: **unmet evidence requirement, NARROW**.
- No measured Lighthouse/LCP or throttled low-end network profile is claimed: **unmet performance evidence, NARROW**.
- Fixture products mirror Shopify fields but do not come from a Shopify runtime: expected for this isolated harness, but **not production proof**.
- Editor lifecycle hooks are not implemented because this is not a Shopify section; production must prove load/unload/select/reorder behavior later.
- The broader M1 acceptance gate covering four Living Canvas variants is **not met** and is not weakened here.
