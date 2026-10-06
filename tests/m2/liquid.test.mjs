import test from 'node:test';
import assert from 'node:assert/strict';
import { render, fixture } from './liquid-engine.mjs';
test('available selection submits exact native variant; accelerated default is present', async () => {
  const html = await render('product-form', fixture());
  assert.match(html, /name="id" value="501"/);
  assert.doesNotMatch(html, /name="id"[^>]*disabled/);
  assert.match(html, /name="add" >Add to cart/);
  assert.match(html, /data-platform-payment/);
  assert.doesNotMatch(html, /name="quantity"/); // external quantity block owns this field
});
test('sold-out preserves canonical identity while blocking purchase and checkout', async () => {
  const data = fixture(); data.variant.available = false;
  const html = await render('product-form', data);
  assert.match(html, /name="id" value="501" disabled/);
  assert.match(html, /name="add" disabled>Sold out/);
  assert.doesNotMatch(html, /data-platform-payment/);
});
test('nonexistent tuple does not invent an ID or purchasable combination', async () => {
  const html = await render('product-form', fixture({ variant: null }));
  assert.match(html, /name="id" value="" disabled/);
  assert.match(html, /name="add" disabled>Unavailable/);
  assert.doesNotMatch(html, /data-platform-payment/);
});
test('required plan without allocation cannot degrade to one-time', async () => {
  const data = fixture(); data.product.requires_selling_plan = true;
  const html = await render('product-form', data);
  assert.match(html, /name="add" disabled/);
});
test('invalid selected plan blocks purchase even on an available variant', async () => {
  const data = fixture(); data.product.selected_selling_plan = { id: 999 };
  assert.match(await render('product-form', data), /name="add" disabled/);
});
test('valid required allocation posts the exact plan alongside variant', async () => {
  const data = fixture({ allocation: { price: 2000, compare_at_price: 2400, selling_plan: { id: 91 } } });
  data.product.requires_selling_plan = true;
  const html = await render('product-form', data);
  assert.match(html, /name="selling_plan" value="91"/);
  assert.doesNotMatch(html, /name="add" disabled/);
});
test('removed quantity block falls back to the real rule minimum, not one', async () => {
  assert.match(await render('product-form', fixture({ has_quantity: false })), /name="quantity" value="3"/);
});
test('quantity block uses native rule min, max, increment, ID and form association', async () => {
  const html = await render('quantity', fixture());
  assert.match(html, /form="ProductForm-test" min="3" max="15" step="2" value="3"/);
  assert.match(html, /for="Quantity-test"/);
  assert.match(html, /Minimum 3; increments of 2/);
});
test('normal variant price, compare and unit are from one identity', async () => {
  const html = await render('price', fixture());
  assert.match(html, /30.00 CAD/); assert.match(html, /24.00 CAD/); assert.match(html, /12.00 CAD/);
});
test('equal or lower compare-at is never presented as a sale', async () => {
  const data = fixture(); data.variant.compare_at_price = 2000;
  assert.doesNotMatch(await render('price', data), /<s>/);
});
test('allocation changes price and unit with variant measurement, never a client discount', async () => {
  const html = await render('price', fixture({ allocation: { price: 2000, compare_at_price: 2400, unit_price: 1000 } }));
  assert.match(html, /20.00 CAD/); assert.match(html, /10.00 CAD/); assert.match(html, /100ml/);
  assert.doesNotMatch(html, /30.00 CAD/);
});
test('null variant produces no fictional money', async () => {
  assert.doesNotMatch(await render('price', fixture({ variant: null })), /CAD/);
});
test('gift recipient mode uses official properties and excludes accelerated checkout', async () => {
  const data = fixture(); data.product['gift_card?'] = true;
  const html = await render('product-form', data);
  assert.match(html, /properties\[__shopify_send_gift_card_to_recipient\]/);
  assert.match(html, /properties\[Recipient email\]/);
  assert.match(html, /maxlength="255"/); assert.match(html, /maxlength="200"/);
  assert.doesNotMatch(html, /data-platform-payment/);
});
test('gift without recipient mode may use platform checkout', async () => {
  const data = fixture(); data.product['gift_card?'] = true; data.block.settings.recipient = false;
  assert.match(await render('product-form', data), /data-platform-payment/);
});
test('native server errors remain visible', async () => {
  assert.match(await render('product-form', fixture({ form: { errors: ['inventory'] } })), /role="alert"/);
});
test('required purchase plans expose only allocations for this variant', async () => {
  const data = fixture(); data.product.requires_selling_plan = true;
  data.variant.selling_plan_allocations = [{ price: 2000, selling_plan: { id: 91, name: 'Monthly' } }];
  const html = await render('selling-plans', data);
  assert.match(html, /method="get"/); assert.match(html, /name="variant" value="501"/);
  assert.doesNotMatch(html, /One-time purchase/); assert.match(html, /value="91"/);
});
test('native option URLs preserve tuple IDs, selected state, escaped labels and swatches', async () => {
  const data = fixture(); data.product.has_only_default_variant = false;
  data.product.options_with_values = [
    { position: 1, name: 'Size', values: [{ id: 11, name: 'S', selected: true, available: true }, { id: 12, name: 'L <large>', available: false }] },
    { position: 2, name: 'Color', values: [{ id: 21, name: 'Red', selected: true, available: true, swatch: { color: '#ff0000' } }] },
  ];
  const html = await render('variant-options', data);
  assert.match(html, /option_values=12%2C21/); assert.match(html, /aria-current="true"/);
  assert.match(html, /L &lt;large&gt;/); assert.match(html, /background-color: #ff0000/);
  assert.doesNotMatch(html, /name="id"/);
});
test('default single variant needs no fabricated options', async () => {
  const data = fixture(); data.product.has_only_default_variant = true;
  assert.doesNotMatch(await render('variant-options', data), /fieldset/);
});
test('missing product is omitted on storefront and explained only in editor', async () => {
  assert.equal((await render('product-surface', { product: null, request: { design_mode: false } })).trim(), '');
  assert.match(await render('product-surface', { product: null, request: { design_mode: true } }), /Choose a product/);
});
test('Balanced initializes required allocation and no-media fallback from the same native truth', async () => {
  const data = fixture(); data.variant.selling_plan_allocations = [{price:2000,selling_plan:{id:91}}];
  data.product = {...data.product, title:'Canonical product', requires_selling_plan:true, selected_or_first_available_variant:data.variant,media:[],has_only_default_variant:true};
  data.section.blocks = [{type:'title'},{type:'price'},{type:'buy',settings:data.block.settings}];data.primary=true;
  const html=await render('product-surface',data);
  assert.match(html, /<h1>Canonical product<\/h1>/);assert.match(html,/No media available/);
  assert.match(html,/20.00 CAD/);assert.match(html,/name="selling_plan" value="91"/);
});
test('featured instances produce distinct native form IDs without a second commerce engine', async () => {
  const data=fixture();data.product={...data.product,title:'Canonical',selected_or_first_available_variant:data.variant,media:[]};
  data.section.blocks=[{type:'quantity'},{type:'buy',settings:data.block.settings}];
  data.section.id='first';const first=await render('product-surface',data);
  data.section.id='second';const second=await render('product-surface',data);
  assert.match(first,/id="ProductForm-first"/);assert.match(first,/form="ProductForm-first"/);
  assert.match(second,/id="ProductForm-second"/);assert.match(second,/form="ProductForm-second"/);
});
test('native filters preserve active unavailable values, range numbers and sort identity', async () => {
  const html=await render('filters',{section:{id:'filters'},collection:{url:'/collections/catalog',sort_by:'price-descending',sort_options:[{value:'price-descending',name:'Price descending'}],filters:[{type:'boolean',label:'Available',active_values:[1],values:[{param_name:'filter.v.availability',value:'1',label:'In stock',active:true,count:0}]},{type:'price_range',label:'Price',active_values:[],min_value:{param_name:'filter.v.price.gte',value:1200},max_value:{param_name:'filter.v.price.lte',value:2400}}]}});
  assert.match(html,/name="filter.v.availability" value="1" checked/);
  assert.match(html,/name="filter.v.price.gte" value="12"/);assert.match(html,/value="price-descending" selected/);
});
