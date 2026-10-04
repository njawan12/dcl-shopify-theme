// Optional dependency-free static server, with read-only destinations for modeled product links.
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve, extname } from 'node:path';
import { fixtures } from '../fixtures.js';
const port = Number(process.env.PORT || 3000);
const base = fileURLToPath(new URL('../', import.meta.url));
const escape = text => String(text).replace(/[&<>"']/g, char => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[char]);
const types = { '.html': 'text/html', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.css': 'text/css', '.mjs': 'text/javascript', '.jpg': 'image/jpeg', '.json': 'application/json', '.md': 'text/plain' };
createServer(async (req, res) => {
  const path = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  if (path.startsWith('/products/')) {
    const product = fixtures.flatMap(f => f.steps.map(s => s.product)).find(p => p?.url === path);
    if (!product) { res.writeHead(404); res.end('Unknown fixture product'); return; }
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(`<!doctype html><html lang="en"><meta name="viewport" content="width=device-width, initial-scale=1"><title>${escape(product.title)}</title><link rel="stylesheet" href="/split-tension.css"><body><header class="harness"><strong>Fixture product destination</strong><p>Read-only local navigation adapter. This is modeled product discovery, not a Shopify PDP or real purchase path.</p></header><main class="editorial"><h1>${escape(product.title)}</h1><p>${product.variants.some(v => v.available) ? 'This fixture product has available variants.' : 'This fixture product is sold out.'}</p><p>Purchase choices belong on the real product page in production.</p><a class="product-link" href="/">Return to the guided collection</a></main></body></html>`);
    return;
  }
  const file = resolve(base, `.${path === '/' ? '/index.html' : path}`);
  if (!file.startsWith(base)) { res.writeHead(403); res.end(); return; }
  try {
    const bytes = await readFile(file);
    res.writeHead(200, { 'Content-Type': `${types[extname(file)] || 'application/octet-stream'}; charset=utf-8`, 'Cache-Control': 'no-store' });
    res.end(bytes);
  } catch { res.writeHead(404); res.end('Not found'); }
}).listen(port, '127.0.0.1', () => console.log(`Split Tension: http://localhost:${port}/ (localhost only; no Shopify requests)`));
