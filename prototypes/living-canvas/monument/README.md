# M1 Monument — One Line, One Object

Isolated server-rendered visual proof. Engineering checks pass within this prototype's scope. **Visual verdict: PENDING HUMAN REVIEW.**

Run from the repository root (Python standard library only):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/serve.py
```

Open `http://localhost:3001/` in the Codex in-app browser. The native fixture form submits a GET request; no browser JavaScript is present. Port 3001 keeps the accepted Split Tension preview separate. `PORT` can select a different local port. Product/editorial destinations are truthful read-only navigation stubs, not Shopify commerce.

`render.py` owns one semantic component and one surrounding test harness. `fixtures.json` supplies 41 data/copy/media states. `monument.css` owns an L-shaped desktop/tablet editorial field and a continuous vertical mobile rail beginning alongside the statement. One bounded media object crosses into the editorial field and interrupts the axis; commerce stays attached to its baseline. The default branded proof uses the existing Beauty/Wellness care bottle. Text remains in normal flow. Presets change tokens, never the component structure.

`index.html` is the literal default output of the same renderer; regenerate only when changing the renderer/default fixture:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/render.py
```

Verification, with the server running for the last command:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/tests/static.py
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/tests/browser_evidence.py
PYTHONDONTWRITEBYTECODE=1 python3 prototypes/living-canvas/monument/tests/server_responses.py
```

Browser evidence was captured using native browser navigation, read-only DOM measurement and full-page screenshots. `browser_evidence.py` checks saved observations and source fingerprints; it does not silently regenerate evidence. Any component/media change requires fresh affected browser captures before that test can pass again.

See `findings.md` for the Section 14 completion report, `tests/evidence/changed-files.json` for the exact manifest, and `tests/evidence/checks.json` for counts/complexity. The four controlling frames are `branded-1440.jpg`, `neutral-1440.jpg`, `branded-390.jpg`, and `neutral-390.jpg` in `tests/evidence/`.

This is one M1 prototype. Production Shopify, full accessibility/performance certification, M2 and visual acceptance are outside its completed scope.
