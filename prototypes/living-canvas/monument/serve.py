"""Local read-only fixture server. Python standard library; binds loopback only."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
from html import escape
from pathlib import Path
import mimetypes
import os
from render import BASE, DATA, product_for, render_page


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        request = urlparse(self.path)
        if request.path in ('/', '/index.html'):
            fixture = parse_qs(request.query).get('fixture', ['default'])[0]
            self.send(render_page(fixture).encode(), 'text/html; charset=utf-8')
            return
        if request.path.startswith('/products/'):
            product = next((p for p in DATA['products'].values() if p['url'] == request.path and p.get('published', True)), None)
            if not product:
                self.send_error(404)
                return
            # Navigation proof only, not a PDP implementation or checkout.
            body = f'<!doctype html><html lang="en"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(product["title"])}</title><link rel="stylesheet" href="/monument.css"><body><main class="destination"><h1>{escape(product["title"])}</h1><p>Read-only fixture destination. This is not a real Shopify product page or purchase path.</p><a class="product-link" href="/">Return to Monument</a></main></body></html>'
            self.send(body.encode(), 'text/html; charset=utf-8')
            return
        if request.path == '/pages/materials':
            self.send(b'<!doctype html><html lang="en"><title>Fixture editorial destination</title><p>Read-only local editorial link proof.</p><a href="/">Return to Monument</a></html>', 'text/html; charset=utf-8')
            return
        path = (BASE / request.path.lstrip('/')).resolve()
        if not path.is_relative_to(BASE) or not path.is_file() or path.suffix not in ('.html', '.css', '.svg', '.jpg', '.json'):
            self.send_error(404)
            return
        self.send(path.read_bytes(), mimetypes.guess_type(path)[0] or 'application/octet-stream')

    def send(self, body, kind):
        self.send_response(200)
        self.send_header('Content-Type', kind)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    port = int(os.environ.get('PORT', '3001'))
    print(f'Monument: http://localhost:{port}/ (loopback only)', flush=True)
    ThreadingHTTPServer(('127.0.0.1', port), Handler).serve_forever()
