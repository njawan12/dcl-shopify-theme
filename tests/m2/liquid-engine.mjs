/* Unit renderer for actual production snippets. Platform filters/form tag are explicit
 * test adapters, NOT a Shopify server and NOT live commerce integration evidence. */
import { Liquid } from 'liquidjs';
import { readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
const snippets = fileURLToPath(new URL('../../theme/snippets/', import.meta.url));
const strings = JSON.parse(await readFile(new URL('../../theme/locales/en.default.json', import.meta.url)));
export const engine = new Liquid({ root: snippets, extname: '.liquid', strictFilters: true });
engine.registerFilter('image_url', () => '/unit-image.svg');
engine.registerFilter('image_tag', (url) => `<img src="${url}" width="30" height="30" alt="">`);
engine.registerFilter('money_with_currency', (v) => `${(Number(v) / 100).toFixed(2)} CAD`);
engine.registerFilter('t', (key, ...pairs) => {
  let text = key.split('.').reduce((value, part) => value?.[part], strings);
  if (typeof text !== 'string') throw new Error(`Missing test translation: ${key}`);
  for (const [name, value] of pairs) text = text.replaceAll(`{{ ${name} }}`, String(value));
  return text;
});
engine.registerFilter('asset_url', (name) => '/assets/' + name);
engine.registerFilter('structured_data', (product) => JSON.stringify({ '@type': 'Product', name: product.title }));
engine.registerFilter('video_tag', () => '<video controls></video>');
engine.registerFilter('external_video_url', () => '/unit-video');
engine.registerFilter('external_video_tag', () => '<iframe title="Unit video adapter"></iframe>');
engine.registerFilter('model_viewer_tag', () => '<model-viewer></model-viewer>');
engine.registerFilter('default_errors', (errors) => errors ? '<p role="alert">Server error</p>' : '');
engine.registerFilter('payment_button', () => '<div data-platform-payment>Platform checkout adapter</div>');
engine.registerFilter('payment_terms', () => '<div data-platform-terms>Platform terms adapter</div>');
engine.registerTag('form', {
  parse(token, remainTokens) {
    this.templates = [];
    const stream = engine.parser.parseStream(remainTokens)
      .on('tag:endform', () => stream.stop())
      .on('template', (template) => this.templates.push(template));
    stream.start();
  },
  *render(context, emitter) {
    // Tests examine conditional input/button output, not Shopify's generated form internals.
    emitter.write(`<form method="post" action="/cart/add" id="${context.get(['form_id']) || 'ProductForm-test'}">`);
    yield engine.renderer.renderTemplates(this.templates, context, emitter);
    emitter.write('</form>');
  },
});
export const render = (name, data) => engine.renderFile(name, data);
export function fixture(overrides = {}) {
  const variant = {
    id: 501, title: 'Small / Red', available: true, price: 2400, compare_at_price: 3000,
    quantity_rule: { min: 3, max: 15, increment: 2 },
    unit_price: 1200, unit_price_measurement: { reference_value: 100, reference_unit: 'ml' },
    selling_plan_allocations: [],
  };
  return { variant, product: { id: 50, url: '/products/unit-test', requires_selling_plan: false },
    block: { settings: { dynamic_checkout: true, recipient: true } },
    section: { id: 'test' }, form_id: 'ProductForm-test', form: {}, allocation: null,
    has_quantity: true, ...overrides };
}
