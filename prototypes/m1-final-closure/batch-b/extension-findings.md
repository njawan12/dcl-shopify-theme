# B5 measured extension exercises

2026-10-05. **B5 PASS**, exactly two isolated evidence exercises, not production scope. Both import Batch A interfaces read-only. No existing surface, renderer, fixture, token, CSS or preserved signature implementation was changed.

|Exercise|Exact changed file|Diff from empty / raw size|Interface / content input|Controls / CSS / JS / state|
|---|---|---|---|---|
|A Purchase|`extensions/purchase.py`|+13/-0 physical lines;12 nonblank;599 bytes|`with_support(product,choices,name,support=None)` wraps shared `purchase` and resolves shared `truth`. Optional escaped label/body in native details/summary is a bounded supporting-information behavior.|0 settings;2 content bindings;0 token/CSS/JS/commerce-state additions.|
|B Story|`extensions/story.py`|+11/-0 physical lines;10 nonblank;531 bytes|`product_note(product_id,body)` resolves canonical PRODUCTS identity/title/destination and escaped merchant body; missing ID/body omits section. Existing semantic type/spacing inherit.|0 settings;2 content bindings;0 token/CSS/JS/state additions.|

`tests/evidence/extension-metrics.json` includes source hashes, exact touched-file manifest, interfaces, counts and coupling. Two local modules are intentional read-only coupling to the proposed shared contracts; no duplicated commerce resolver, global CSS rescue, vertical fork, arbitrary controls or shared mutable browser state. Native disclosure requires no JS. Its AT/device behavior is not certified by unit tests. The narrow story section is an extension experiment, not a new signature or composition.

Executed regression command from repository root:

```
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/m1-final-closure/batch-b/tests/extensions.py
```

27/27 assertions PASS: five single/unresolved/nonexistent/sold-out/valid purchase cases retain the exact original purchase prefix/truth and immutable inputs while adding escaped native disclosure; omission returns the original purchase. Story checks canonical identity/destination, escaping, absent reference/body omission and cross-vertical reuse. Full old width matrix is not rerun: neither exercise is inserted into accepted surfaces. `validate_closure.py` additionally checks exact measured bytes/lines/hashes and all455 parent-file hashes plus eight branch refs. Preservation PASS. The absence of a renderer rewrite is measured directly, not inferred from test quantity.

Extensions remain evidence-only. Production promotion, actual Shopify objects/snippets, live disclosure AT/editor testing and performance remain later decisions. No additional extension exercise was performed.
