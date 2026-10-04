// Fixture commerce is immutable simulated data; editorial text has separate ownership.
const image = (name, width = 300, height = 300) => ({ src: `media/${name}.svg`, width, height });
const single = (id, title, price, media = image('bottle')) => ({
  id, handle: id, title, url: `/products/${id}`, image: media, options: [],
  variants: [{ id: `${id}-1`, options: [], price, available: true }]
});
const cleanse = single('daily-cleanser', 'Daily cleansing milk', 2400, image('bottle-cutout'));
const hydrate = single('barrier-cream', 'Everyday barrier cream', 3800, image('jar-cutout'));
const serum = single('concentrate', 'Lightweight daily concentrate for a considered morning ritual', 4200, image('bottle-portrait', 200, 360));
const finish = single('finishing-oil', 'Soft finish botanical oil', 3100, image('bottle'));
const cloth = single('woven-cloth', 'Reusable woven cleansing cloth', 1200, image('box', 420, 220));
const optionProduct = {
  ...single('balancing-formula', 'Balancing formula', 2900),
  options: [{ name: 'Size', values: ['30 ml', '60 ml'] }, { name: 'Finish', values: ['Light', 'Rich'] }],
  variants: [
    { id: 'formula-30-light', options: ['30 ml', 'Light'], price: 2900, compareAt: 3400, available: true, unitPrice: { price: 9667, reference: '100 ml' } },
    { id: 'formula-30-rich', options: ['30 ml', 'Rich'], price: 3100, available: false },
    { id: 'formula-60-light', options: ['60 ml', 'Light'], price: 4700, available: true, unitPrice: { price: 7833, reference: '100 ml' } }
  ]
};
const step = (product, label, copy) => ({ product, label, copy });
const baseSteps = [step(cleanse, 'Begin gently', 'A simple first step. Choose what belongs in your day.'), step(hydrate, 'Build comfort', 'Finish with a texture that feels right for you.')];
const optionSteps = [step(optionProduct, 'Find your texture', 'Choose each option before including this product.'), ...baseSteps];
const flagged = (flag, id = flag.replace(/[A-Z]/g, letter => `-${letter.toLowerCase()}`)) => ({ ...single(id, 'Considered care collection', 4500, image('box')), [flag]: true });
// Variant-count subcases stay inside the canonical maximum-density fixture.
const withOptions = (product, options) => {
  const tuples = options.reduce((rows, option) => rows.flatMap(row => option.values.map(value => [...row, value])), [[]]);
  return { ...product, options, variants: tuples.map((tuple, i) => ({ id: `${product.id}-${i + 1}`, options: tuple, price: product.variants[0].price + i * 100, available: true })) };
};
const denseSerum = withOptions(serum, [{ name: 'Volume', values: ['10 ml', '20 ml', '30 ml', '40 ml', '50 ml', '60 ml'] }, { name: 'Texture', values: ['Light', 'Smooth', 'Rich', 'Fluid'] }]);
const denseFinish = withOptions(finish, [{ name: 'Your preferred finishing texture for everyday use', values: ['Light', 'Silky', 'Soft', 'Rich', 'Fluid', 'Smooth'] }]);
const denseCloth = withOptions(cloth, [{ name: 'Weave', values: ['Fine', 'Textured'] }]);
const editorial = { media: { src: 'media/campaign-portrait-v2.jpg', width: 1024, height: 1536 }, eyebrow: 'A considered daily ritual', heading: 'Less, with\nintention.', body: 'Start with the essentials. Discover each step, then choose only the products you want to make your own.', note: 'Individual products. Your own rhythm.' };
const neutralEditorial = { media: { src: 'media/objects-landscape.svg', width: 1200, height: 800 }, eyebrow: 'Objects for everyday use', heading: 'A place for\nthe essentials.', body: 'Explore a small collection of useful objects. Follow the sequence and choose the pieces that belong in your space.', note: 'A guided collection. Each object stands alone.' };
const fixture = (id, label, steps = baseSteps, extra = {}) => ({ id, label, steps, editorial, money: { currency: 'CAD', digits: 2, locale: 'en-CA' }, response: 'success', diagnostic: 'Simulated fixture data. No Shopify requests. Quantity is always 1.', ...extra });
const longSteps = [
  ...baseSteps,
  step(denseSerum, 'Add a considered layer', 'A lightweight addition when your morning calls for a little more care.'),
  step(denseFinish, 'Find your finishing texture', 'An optional finishing step. Select it only if it belongs in your routine.'),
  step(denseCloth, 'Keep the useful things close', 'A reusable companion for the beginning and end of an ordinary day.')
];
const localizedSteps = longSteps.map((s, i) => ({ ...s, label: `${s.label} — in Ihrem eigenen Rhythmus`, copy: `${s.copy}${i === 1 ? ' In Ihrem eigenen Takt.' : ' In Ihrem eigenen Tempo.'}`, product: { ...s.product, title: `${s.product.title} für Ihre tägliche Pflege`, image: i === 2 ? null : s.product.image } }));
const neutralSteps = [step(single('storage-vessel', 'Everyday storage vessel', 2400, image('jar')), 'Make room', 'A useful object for the things you keep close.'), step(single('woven-case', 'Woven utility case', 3800, image('box')), 'Keep together', 'Choose a companion for the objects you carry.')];
export const fixtures = deepFreeze([
  fixture('simple', '01 · 2-step simple'),
  fixture('maximum', '02 · 5-step maximum', longSteps, { editorial: { ...editorial, media: neutralEditorial.media }, diagnostic: 'Five steps; 1, 2, 6 and 24 variants, bounded to two native option controls per item. Portrait, square and landscape media.' }),
  fixture('multi-option', '03 · Multi-option unresolved', optionSteps, { diagnostic: 'Choose 30 ml + Light (available), 30 ml + Rich (sold out), or 60 ml + Rich (nonexistent). Unit prices stay on the item.' }),
  fixture('variant-sold-out', '04 · Variant sold out', optionSteps, { diagnostic: 'Explicitly choose 30 ml + Rich to exercise the sold-out variant; no defaults are chosen.' }),
  fixture('fully-sold-out', '05 · Product fully sold out', [step({ ...hydrate, variants: hydrate.variants.map(v => ({ ...v, available: false })) }, 'Build comfort', 'Explore this step on its product page.'), baseSteps[0]]),
  fixture('missing', '06 · Missing product', [baseSteps[0], step(null, 'Leave a little space', 'Some days need fewer things. The sequence is yours.'), baseSteps[1]], { editorial: { ...editorial, media: null } }),
  fixture('mixed', '07 · Mixed eligibility', [...optionSteps, step(flagged('appOwned'), 'Explore the collection', 'Discover the full purchase choices on the product page.')]),
  fixture('selling-plan', '08 · Selling-plan-sensitive', [...baseSteps, step(flagged('sellingPlanSensitive'), 'Choose your cadence', 'Explore purchase terms on the product page.')]),
  fixture('price-mutation', '09 · Price / compare-at / unit-price mutation', optionSteps, { diagnostic: '30 ml + Light has compare-at and unit price; 60 ml + Light changes price and removes compare-at. Include first to observe an exact total update.' }),
  fixture('localized', '10 · Long / localized copy', localizedSteps, { editorial: { ...editorial, heading: 'Weniger Dinge, mit einer bewussten Absicht für jeden Tag.', body: `${editorial.body} In Ihrem eigenen Tempo und nach Ihren Wünschen.` }, diagnostic: 'Paired copy expands by 30–50%; a missing image and three media ratios exercise content resilience.' }),
  fixture('neutral', '11 · Neutral originality torture', neutralSteps, { neutral: true, editorial: neutralEditorial }),
  fixture('no-js', '12 · No-JS baseline', baseSteps, { enhance: false, diagnostic: 'Enhancement deliberately withheld. Also disable JavaScript in your browser and reload index.html to test the literal baseline.' }),
  fixture('failure', '13 · Request failure', baseSteps, { response: 'failure', diagnostic: 'Include either item and Add selected. Failure preserves choices; retry repeats this deterministic failure.' }),
  fixture('ambiguous', '14 · Partial / ambiguous response', baseSteps, { response: 'ambiguous', diagnostic: 'No item-level confirmation is inferred. Review the simulated result before explicitly retrying.' }),
  fixture('inclusion', '15 · Explicit inclusion default'),
  fixture('quantity-rule', '16 · Quantity-rule product', [...baseSteps, step(flagged('quantityRule'), 'Explore quantities', 'Purchase requirements are available on the product page.')]),
  fixture('duplicate', '17 · Duplicate reference', [...baseSteps, step(cleanse, 'Return to the beginning', 'Revisit this product without ordering a duplicate.')], { diagnostic: 'Both repeated product references narrow to View product. Authored steps stay intact; no duplicate payload or coalescing.' }),
  fixture('two-instances', '18 · Two instances', optionSteps, { instances: 2 }),
  fixture('init-failure', '19 · Initialization failure', baseSteps, { instances: 2, failFirst: true, diagnostic: 'First instance deliberately throws before controls are attached. Its fallback survives; the second instance enhances independently.' }),
  fixture('inventory-race', '20 · Inventory race / simulated 422', baseSteps, { response: 'inventory', diagnostic: 'A simulated 422 makes the first submitted variant unavailable, clears its inclusion and retains unaffected choices.' }),
  fixture('ineligible', '21 · All inline-ineligible', [step(flagged('sellingPlanSensitive'), 'Explore the cadence', 'Choose terms on the product page.'), step(flagged('appOwned'), 'Discover the collection', 'Explore the full collection on its product page.'), step(flagged('linkOnly', 'gift-card'), 'Give a thoughtful gift', 'Choose recipient details on the product page.')]),
  fixture('one-surviving', '22 · One surviving valid step', [baseSteps[0], step(null, 'Keep it simple', 'One carefully chosen thing can be enough.')]),
  fixture('money', '23 · Money precision / context', [step(single('small-object', 'Small useful object', 101, image('jar')), 'Choose one', 'Each amount is modeled in integer minor units.'), step(single('second-object', 'Second useful object', 202, image('box')), 'Choose another', 'The selection is separate from checkout totals.')], { money: { currency: 'KWD', digits: 3, locale: 'en-KW' }, neutral: true, editorial: neutralEditorial, diagnostic: 'KWD three-decimal context: 101 + 202 minor units = KWD 0.303 exactly. Fixture switching discards currency and selections.' }),
  fixture('properties', '24 · Required line-item properties', [...baseSteps, step(flagged('requiredProperties'), 'Make it personal', 'Choose personalization on the product page.')])
]);
export function deepFreeze(value) {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    Object.values(value).forEach(deepFreeze);
    Object.freeze(value);
  }
  return value;
}
export function getFixture(id) { return fixtures.find(f => f.id === id) || fixtures[0]; }
