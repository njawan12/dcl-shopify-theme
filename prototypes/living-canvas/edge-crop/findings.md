# Edge Crop M1 findings

**Recommendation: NARROW.** Edge Crop is strong enough to continue as the sole Living Canvas variant proven by this experiment, but it is not a pass for Living Canvas as a whole or for production. Browser/assistive-technology manual coverage is incomplete, the product data is mock-shaped rather than Liquid-rendered, and this experiment does not satisfy the broader gate requiring all four variants.

## Evidence against the brief

| Check | Result | Evidence / limitation |
| --- | --- | --- |
| Keyboard-only | NARROW (code review only) | Native select, links, and hotspot buttons follow DOM order; open panels receive focus; close controls are keyboard reachable. A real-browser keyboard pass remains required. |
| Escape / focus restoration | NARROW (code review only) | Escape and explicit close are implemented to restore focus to the opening trigger. Outside pointer close intentionally does not move focus. A real-browser pass remains required. |
| Reduced motion | PASS (code review) | No component animation is required; smooth scrolling is removed and durations collapse under `prefers-reduced-motion`. |
| 320px | NARROW (CSS inspection) | The media is specified as 4:5 and all hotspots become a full-width keyed list below it. Text measure remains bounded. Real-browser inspection remains required. |
| Tablet / desktop | NARROW (CSS inspection) | At 768–1023px the zones interlock while hotspots use a keyed list; at 1024px and above semantic anchors overlay the media with deterministic panel direction/alignment. Real-browser inspection remains required. |
| 200% / 400% zoom | NARROW | CSS reflows to the list layout as viewport CSS pixels contract, but physical browser zoom and assistive-technology combinations still require human device testing. |
| Ordinary packshot | NARROW | The white-background fixture retains the structural crop in code, but intentional visual behavior has not been established by browser rendering evidence. |
| Long copy | NARROW | Content is not assigned a fixed height and is designed to grow without clipping, but visual behavior has not been established by browser rendering evidence. |
| Missing product | PASS | The missing target renders explanatory content with no dead product link, invented price, or empty marker. |
| JavaScript disabled | PASS | Default editorial/media composition renders, and hotspot panels—including the product destination—remain expanded in document order. Fixture switching is enhancement-only. |
| Screen readers | NARROW | Names, native controls, relationship state, and focus flow are implemented, but VoiceOver and NVDA were not available for hands-on verification. |
| Performance | NARROW | No framework, network dependency, crop JS, or animation library exists. Media reserves aspect ratio and the hero is eager/high priority. No lab LCP/low-end network run is claimed. |

## Required questions

### 1. Does Edge Crop remain distinctive after neutralizing photography/color/type?

**Not yet proven; the hypothesis remains credible.** The dedicated neutral fixture combines a plain white-background generic object, neutral grayscale tokens, system typography, non-beauty language, and disabled nonessential motion while retaining the same curved Edge Crop structure. Static inspection confirms that the neutralization is real, but without browser evidence this remains **NARROW**, not a visual pass or whole-theme originality proof.

### 2. Does the ordinary-packshot fixture still look intentional?

**NARROW.** The centered bottle is subjected to the same off-axis crop and bounded annotations rather than receiving a tailored asset, but the claim that it “looks intentional” requires browser review that has not occurred.

### 3. Which semantic hotspot anchors worked or failed?

`upper-left`, `upper-right`, `lower-left`, and `lower-right` are implemented as bounded desktop positions, but remain **NARROW** pending browser verification. Only one panel opens at once. At 1024px and above, upper panels open downward, lower panels flip upward, and right panels align inward. Below 1024px all anchors deterministically become an ordered key, removing tablet collision risk. The schema should not promise that anchor meaning survives visually on mobile or tablet.

### 4. What breaks first on mobile / long copy?

Overlay annotation placement is expected to break first, hence the deterministic list conversion below 1024px. Long copy is expected to increase scroll length rather than clip because no fixed content height is used; that remains unverified visually. At 320px, very long strings are configured to wrap and the editorial-to-media reveal may move below the first viewport. That priority tradeoff is preferable to truncation.

### 5. Did accessibility force visual changes?

**Yes.** Markers are 48px rather than tiny dots, strong blue focus rings are intentionally conspicuous, panels have explicit close buttons, numbering keys position without relying on it, and collision-prone widths use a spacious list. The chosen non-modal disclosure pattern moves focus to the first actionable panel control (the close button); Escape and explicit close restore focus to the originating trigger.

### 6. Is the merchant-control model still shallow?

**Yes.** The modeled choices are common content/media, hotspot type/content, and one of four named anchors. There are no x/y values, device offsets, arbitrary transforms, animation controls, or layout nesting. Mobile behavior is automatic.

### 7. What should change in the schema spec before production?

1. Define the four anchor enum values and disclose that mobile renders hotspot block order, not anchor order.
2. Require a concise accessible hotspot label separate from the visible title.
3. Treat a deleted product as a diagnostic/editor-visible missing-reference state that produces no storefront trigger unless merchant-authored fallback text exists. The prototype keeps its diagnostic in the harness controls, separate from the simulated storefront.
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

## Correction audit

1. **Initial progressive enhancement:** the default HTML hotspot articles remain authoritative and are hydrated in place; `replaceChildren` runs only for a different initial query fixture or a subsequent fixture switch. The `js` class is added only after successful initialization, so failed enhancement leaves panels visible.
2. **Missing product:** the missing fixture contains no product hotspot. Its harness-only diagnostic is outside the canvas and explicitly labelled; there are no shopper-facing editor instructions.
3. **Desktop geometry:** at 48rem and wider, a scalable CSS ellipse creates the structural curved crop; it is applied to the media container, never baked into merchant media.
4. **Collision safety:** hotspot panels become a non-overlay key below 64rem (1024px). At and above 64rem, upper/lower opening direction and inline alignment are deterministic, with one panel open at a time. Browser checks at 768–1024px remain outstanding and therefore NARROW.
5. **Focus model:** non-modal disclosure behavior is consistent; opening focuses the first actionable control, while Escape and explicit close restore the trigger. No focus trap or modal semantics are used.
6. **URLs:** every product fixture and the server-rendered fallback use root-relative `/products/...` destinations.
7. **Evidence language:** ordinary packshot and long-copy results are NARROW pending actual rendering evidence.
8. **Neutral torture fixture:** the ninth selectable fixture uses a generic white-background object, grayscale accessible palette, system type, generic language, no mobile-specific image, and forced removal of nonessential motion while preserving Edge Crop structure.

## Full implementation-brief self-audit

- **Scope and structure:** Edge Crop alone is implemented in the isolated prototype directory. It has editorial and dominant media zones, a container-owned curve, 1–4 authored semantic anchors, and no arbitrary coordinates.
- **Interaction:** information and product disclosures use real buttons, accessible names, accurate expanded/relationship state, explicit close, Escape, outside pointer close, visible focus, single-open state, and no hover-only content. Product records include id, handle, title, root-relative URL, image, price, optional compare-at price, and availability; no ratings, urgency, or app data are fabricated.
- **Responsive behavior:** source order is unchanged. Mobile protects readable width, reorients geometry, and uses an ordered key; tablet also uses the key to prevent panel collisions. Browser confirmation remains NARROW.
- **Fixtures:** all eight required states plus the stricter neutral originality state are switchable. The missing reference emits no product trigger. Coherence is not claimed as PASS without rendering evidence.
- **Accessibility:** semantic heading/content, native controls, focus visibility, disclosure state, Escape/restoration, reduced-motion behavior, text alternatives, non-color keys, and >=44px primary controls are implemented. Keyboard, screen-reader, touch, and 200%/400% real-browser evidence remains unmet.
- **Performance:** crop geometry is CSS-only; there is no framework or animation library. Hero media has intrinsic dimensions, eager/high priority behavior, and one `<picture>` candidate; optional mobile source removal avoids deliberately loading two alternatives. Product thumbnails are lazy. Lab LCP/network evidence remains unmet.
- **Progressive enhancement:** HTML renders the composition and expanded hotspot content without JavaScript. Initialization hydrates the default markup; failed JavaScript does not apply the hiding class. Direct product destinations remain available.
- **Documentation and recommendation:** run instructions, test protocol, interaction pattern, evidence limits, schema changes, and NARROW recommendation are recorded. No Theme Store compliance or production authorization is claimed.
