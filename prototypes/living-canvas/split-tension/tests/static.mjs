import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
import { fixtures } from '../fixtures.js';
import { money } from '../split-tension.js';
const base = fileURLToPath(new URL('../', import.meta.url));
const html = readFileSync(`${base}index.html`, 'utf8');
const js = readFileSync(`${base}split-tension.js`, 'utf8');
const css = readFileSync(`${base}split-tension.css`, 'utf8');
let count = 0;
const check = (condition, name) => { assert.ok(condition, name); count++; };
check(fixtures.length === 24 && new Set(fixtures.map(f => f.id)).size === 24, 'canonical 24 fixtures');
for (const f of fixtures) for (const s of f.steps) if (s.product) {
  check(/^\/products\/[a-z0-9-]+$/.test(s.product.url), 'root-relative product URL');
  for (const v of s.product.variants) check(Number.isSafeInteger(v.price), 'integer price');
}
for (const id of ['two-instances', 'init-failure', 'failure', 'ambiguous', 'inventory-race']) check(fixtures.some(f => f.id === id), `${id} represented`);
check(!/\binnerHTML\b|\beval\s*\(|new Function\b/.test(js), 'safe text APIs');
check(!/fetch\s*\(|XMLHttpRequest|https?:|import\s*\(['"](?!\.)|from ['"](?!\.)/.test(js + css + readFileSync(`${base}fixtures.js`, 'utf8')), 'no dependency/import/network');
check(!/<(?:input|button|fieldset)\b/.test(html), 'no baseline dead enhanced commerce controls');
check(!/on(?:click|change)=/.test(html), 'no inline event substitutes');
check((html.match(/class="step"/g) || []).length === 2, 'literal ordered baseline');
for (const step of fixtures[0].steps) {
  check(html.includes(step.product.title) && html.includes(step.product.url) && html.includes(step.label) && html.includes(step.copy), 'hydration identities match');
  check(html.includes(money(step.product.variants[0].price, fixtures[0].money).replace(/\s/g, ' ')), 'literal baseline price matches');
}
check(js.includes('initial.id === \'simple\' || initial.id === \'no-js\''), 'default enhancement preserves baseline');
check(js.includes('clearTimeout(timer)') && js.includes("removeEventListener('change', onChange)"), 'lifecycle cleanup');
check(css.includes('prefers-reduced-motion') && css.includes(':focus-visible'), 'focus and reduced motion');
const changed = execFileSync('git', ['status', '--porcelain', '--untracked-files=all'], { encoding: 'utf8' }).trim().split('\n').filter(Boolean).map(line => line.slice(3));
check(changed.every(path => path.startsWith('prototypes/living-canvas/split-tension/')), 'only allowed scope changed');
const sources = ['fixtures.js', 'split-tension.js'];
const lines = sources.reduce((n, file) => n + readFileSync(base + file, 'utf8').split('\n').filter(line => line.trim() && !line.trim().startsWith('//')).length, 0);
console.log(`PASS: ${count} static assertions. Nonblank, non-comment JS lines: ${lines}; CSS lines: ${css.trimEnd().split('\n').length}.`);
