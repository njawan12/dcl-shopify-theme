# M1 Final Closure — Batch A integrated proof

**Visual verdict: PENDING HUMAN REVIEW.** Engineering recommendations: B1 structural proof complete, B3 canonical synthetic catalog complete, **B6 NARROW / not closed**. Actual browser-JavaScript-disabled proof is unexecuted; 400% text-enlargement supplements overflow. This is not M1 overall acceptance or production Shopify validation.

Branch: `m1-final-closure-batch-a`. Parent: `8a7693e868eeb6fce5b0150f9044defd8593b3a7`. The exact local commit is reported externally to avoid a self-referential commit hash.

Read [contract.md](contract.md), then [findings.md](findings.md). Exact changed-file inventory is [changed-files.txt](changed-files.txt). All implementation and evidence are confined to this root. No production code, starter, preserved-path changes, push, PR, merge, M2 or Batch B.

## Run the isolated proof

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/m1-final-closure/batch-a/serve.py
```

Open `http://127.0.0.1:3005/?fixture=balanced`. Select proof fixtures using the separate harness. Browser-JavaScript-disabled testing requires a real browser setting; removing scripts or blocking a module is not equivalent.

Native collection/card → product → simulated cart navigation uses one catalog. The story is at `/pages/story`; canonical Guided Set Beauty/Jewelry/neutral reproductions are at `/guided?fixture=beauty`, `/guided?fixture=jewelry`, `/guided?fixture=neutral`. The original Guided Set `failFirst` hook is reproduced as `/guided?fixture=initialization-failure`, a stress state, not another visual variant. `/repeated` is the repeated-host isolation supplement. All cart/payment text identifies local simulation.

## Reproduce checks

With the local server running:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/m1-final-closure/batch-a/tests/static.py
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/m1-final-closure/batch-a/tests/server_journeys.py
node prototypes/m1-final-closure/batch-a/tests/adapter-engine.mjs
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/m1-final-closure/batch-a/tests/validate_observations.py
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/m1-final-closure/batch-a/tests/summarize.py
```

The observation validator audits **recorded real browser measurements**. It does not rerun a browser or synthesize new measurements. [tests/browser-capture.js](tests/browser-capture.js) records the documented CUA read-only probe/capture workflow; the complete fixture inventory and widths are in the contract and dataset manifest. `build_dataset.py` is an authoring/rebuild script, not storefront runtime; it copies pinned local accepted sources and authors explicitly synthetic data/assets.

## Preserve exactly

- Split Tension — **PASS TO PRESERVE**; exact renderer engine/CSS copied, canonical content adapter only.
- Commerce Mosaic — **PASS TO PRESERVE**; exact renderer/planner/CSS copied, canonical data/resource and global-role bindings only.
- Evidence Rail — **visual PASS TO PRESERVE / engineering NARROW**; exact renderers/normalizers/CSS copied. Live editor, real `@app`, merchant usability, accessibility/AT/zoom, localization/RTL, cross-browser/touch, measured production performance and full-theme integration remain unresolved.
- Monument and Edge Crop — **NARROW AND HOLD**, excluded from this assembly. No Quiet Frame invented.

Human acceptance of those components does not award visual acceptance to the new integrated package. Stop for review.
