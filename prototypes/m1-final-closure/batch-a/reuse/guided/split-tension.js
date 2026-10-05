import { fixtures, getFixture } from './fixtures.js';

// Pure engine. Variant identity and money are always derived together, never cached in UI.
export function createState(fixture) {
  validateFixture(fixture);
  return { fixture, steps: fixture.steps.map(s => ({ choices: (s.product?.options || []).map(() => ''), included: false })), version: 0, request: null, alive: true, unavailable: [] };
}
export function validateFixture(fixture) {
  if (fixture.steps.length < 2 || fixture.steps.length > 5) throw new Error('Expected 2–5 authored steps');
  if (!Number.isInteger(fixture.money.digits) || fixture.money.digits < 0 || fixture.money.digits > 3) throw new Error('Invalid money context');
  for (const { product: p } of fixture.steps) {
    if (!p) continue;
    if (!/^\/products\/[a-z0-9-]+$/.test(p.url)) throw new Error('Invalid product URL');
    if (p.image && !/^media\/[a-z0-9-]+\.svg$/.test(p.image.src)) throw new Error('Invalid local media');
    for (const v of p.variants) {
      for (const amount of [v.price, v.compareAt, v.unitPrice?.price].filter(x => x !== undefined)) {
        if (!Number.isSafeInteger(amount) || amount < 0) throw new Error('Money must be safe nonnegative integer minor units');
      }
      if (v.options.length !== p.options.length) throw new Error('Invalid option tuple');
    }
  }
}
export function resolve(state, index) {
  const p = state.fixture.steps[index].product;
  const selection = state.steps[index];
  if (!p) return { kind: 'unavailable-reference', variant: null, eligible: false };
  const duplicate = state.fixture.steps.filter(s => s.product?.id === p.id).length > 1;
  const unsafe = duplicate || p.linkOnly || p.quantityRule || p.requiredProperties;
  const kind = p.sellingPlanSensitive ? 'selling-plan-sensitive' : p.appOwned ? 'app-owned' : unsafe ? 'link-only' : null;
  if (kind) return { kind, variant: null, eligible: false };
  const available = v => v.available && !state.unavailable.includes(v.id);
  if (!p.variants.some(available)) return { kind: 'fully-sold-out', variant: null, eligible: false };
  const variant = p.options.length
    ? (selection.choices.every(Boolean) ? p.variants.find(v => v.options.every((o, i) => o === selection.choices[i])) : null)
    : (p.variants.length === 1 ? p.variants[0] : null);
  if (!variant) return { kind: 'unresolved', variant: null, eligible: false, nonexistent: selection.choices.length > 0 && selection.choices.every(Boolean) };
  if (!available(variant)) return { kind: 'resolved-sold-out', variant, eligible: false };
  return { kind: p.options.length ? 'resolved-available' : 'single-available', variant, eligible: true };
}
export function summary(state) {
  const resolved = state.steps.map((_, i) => resolve(state, i));
  const selected = resolved.flatMap((r, i) => r.eligible && state.steps[i].included ? [{ index: i, variant: r.variant }] : []);
  const total = selected.reduce((n, s) => n + s.variant.price, 0);
  if (!Number.isSafeInteger(total)) throw new Error('Unsafe total');
  return { eligibleCount: resolved.filter(r => r.eligible).length, count: selected.length, total, selected, showAggregate: resolved.filter(r => r.eligible).length >= 2 };
}
export function changeOption(state, index, optionIndex, value) {
  if (!state.alive || state.request?.status === 'pending') return state;
  const options = state.fixture.steps[index].product?.options || [];
  if (!options[optionIndex] || (value && !options[optionIndex].values.includes(value))) return state;
  const steps = state.steps.map(s => ({ ...s, choices: [...s.choices] }));
  steps[index].choices[optionIndex] = value;
  const next = { ...state, steps, version: state.version + 1, request: state.request?.status === 'ambiguous' ? state.request : null };
  if (!resolve(next, index).eligible) steps[index].included = false;
  return next;
}
export function includeStep(state, index, included) {
  if (!state.alive || state.request?.status === 'pending' || !resolve(state, index).eligible) return state;
  return { ...state, steps: state.steps.map((s, i) => i === index ? { ...s, included: Boolean(included) } : s), version: state.version + 1, request: state.request?.status === 'ambiguous' ? state.request : null };
}
export function beginRequest(state) {
  if (!state.alive || state.request?.status === 'pending') return { state, token: null };
  if (state.request?.status === 'ambiguous' && !state.request.reviewed) return { state, token: null };
  const invalid = state.steps.findIndex((s, i) => s.included && !resolve(state, i).eligible);
  const selected = summary(state);
  if (invalid >= 0 || !selected.showAggregate || !selected.count) {
    return { state, token: null, invalid, error: invalid >= 0 ? `Review ${state.fixture.steps[invalid].product?.title || 'this step'} before adding your selection.` : 'Include an available product before adding your selection.' };
  }
  const token = state.version + 1;
  const payload = Object.freeze(selected.selected.map(s => Object.freeze({ id: s.variant.id, quantity: 1 })));
  return { state: { ...state, version: token, request: { status: 'pending', token, payload, message: 'Adding selected items — simulation in progress.', reviewed: false } }, token };
}
export function resultMessage(mode, count, affectedTitle = 'The first requested product') {
  if (mode === 'success') return `Simulated confirmation: ${count} selected ${count === 1 ? 'item' : 'items'} added. No real cart was changed.`;
  if (mode === 'ambiguous') return 'The simulated cart result could not be fully confirmed. Review the result before retrying; some items may have been added.';
  if (mode === 'inventory') return `Simulated inventory failure (422). ${affectedTitle} is now sold out. Review available products and try again.`;
  return 'The simulated request failed. Your available selections are retained. Try again or view each product.';
}
export function finishRequest(state, token, mode) {
  if (!state.alive || state.version !== token || state.request?.token !== token || state.request.status !== 'pending') return state;
  let unavailable = state.unavailable;
  let steps = state.steps;
  if (mode === 'inventory') {
    unavailable = [...unavailable, state.request.payload[0].id];
    const updated = { ...state, unavailable };
    steps = state.steps.map((s, i) => resolve(updated, i).eligible ? s : { ...s, included: false });
  }
  const affectedTitle = state.fixture.steps.find(s => s.product?.variants.some(v => v.id === state.request.payload[0].id))?.product.title;
  return { ...state, steps, unavailable, request: { ...state.request, status: mode === 'inventory' ? 'failure' : mode, message: resultMessage(mode, state.request.payload.length, affectedTitle) } };
}
export function reviewResult(state) {
  if (!state.request || state.request.status === 'pending') return state;
  return { ...state, request: { ...state.request, reviewed: true } };
}
export function destroyState(state) { return { ...state, alive: false, version: state.version + 1 }; }
export function money(amount, context) {
  if (!Number.isSafeInteger(amount) || amount < 0) throw new Error('Invalid money');
  const divisor = 10n ** BigInt(context.digits);
  const whole = BigInt(amount) / divisor;
  const fraction = (BigInt(amount) % divisor).toString().padStart(context.digits, '0');
  return new Intl.NumberFormat(context.locale, { style: 'currency', currency: context.currency, currencyDisplay: 'code', minimumFractionDigits: context.digits, maximumFractionDigits: context.digits })
    .formatToParts(whole).map(part => part.type === 'fraction' ? fraction : part.value).join('');
}

const node = (tag, className, text) => {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
};
const priceText = (p, context) => {
  if (!p) return '';
  const prices = p.variants.map(v => v.price);
  const minimum = Math.min(...prices);
  return `${prices.some(n => n !== minimum) ? 'From ' : ''}${money(minimum, context)}`;
};
const statusText = r => ({
  'unavailable-reference': '', 'link-only': 'Explore purchase choices on the product page.',
  'selling-plan-sensitive': 'Choose purchase terms on the product page.', 'app-owned': 'Explore the collection on the product page.',
  unresolved: r.nonexistent ? 'This combination is unavailable. Choose different options.' : 'Choose every option to include this product.',
  'resolved-sold-out': 'This option is sold out.', 'fully-sold-out': 'Sold out.',
  'resolved-available': 'Available · quantity 1', 'single-available': 'Available · quantity 1'
})[r.kind];

export function renderBaseline(fixture, instanceId) {
  const root = node('section', `split-tension${fixture.neutral ? ' neutral' : ''}`);
  root.id = instanceId;
  root.setAttribute('aria-labelledby', `${instanceId}-heading`);
  const editorial = node('header', 'editorial');
  const media = fixture.editorial.media;
  if (media && /^media\/[a-z0-9-]+\.(jpg|svg)$/.test(media.src)) {
    const image = node('img', 'editorial-media');
    Object.assign(image, { src: media.src, width: media.width, height: media.height, alt: '', loading: 'eager' });
    editorial.append(image);
  }
  const copy = node('div', 'editorial-copy');
  copy.append(node('p', 'eyebrow', fixture.editorial.eyebrow));
  const heading = node('h1', '', fixture.editorial.heading);
  heading.id = `${instanceId}-heading`;
  copy.append(heading, node('p', 'proposition', fixture.editorial.body), node('p', 'editorial-note', fixture.editorial.note));
  editorial.append(copy);
  const list = node('ol', 'steps');
  fixture.steps.forEach((s, i) => {
    if (!s.product && !s.copy) return;
    const card = node('li', 'step');
    card.dataset.step = String(i);
    const lead = node('div', 'step-lead');
    lead.append(node('span', 'step-number', String(i + 1).padStart(2, '0')), node('h2', 'step-label', s.label));
    card.append(lead, node('p', 'step-copy', s.copy));
    if (s.product) {
      const product = node('div', 'product');
      if (s.product.image) {
        const media = node('div', 'product-media');
        const img = node('img');
        Object.assign(img, { src: s.product.image.src, width: s.product.image.width, height: s.product.image.height, alt: '', loading: i === 0 ? 'eager' : 'lazy' });
        media.append(img);
        product.append(media);
      }
      const info = node('div', 'product-info');
      info.append(node('h3', 'product-title', s.product.title), node('p', 'price', priceText(s.product, fixture.money)), node('p', 'availability', s.product.variants.some(v => v.available) ? 'Available on the product page.' : 'Sold out.'));
      const link = node('a', 'product-link', 'View product');
      link.href = s.product.url;
      link.setAttribute('aria-label', `View product: ${s.product.title}`);
      info.append(link);
      product.append(info);
      card.append(product);
    }
    list.append(card);
  });
  root.append(editorial, list);
  return root;
}

export function initInstance(root, fixture, options = {}) {
  // An idempotent instance seam without document-global mutable commerce state.
  if (root.dataset.enhanced === 'true') return root.splitTension;
  let state = createState(fixture);
  let timer = null;
  const refs = [];
  const enhancedNodes = [];
  let aggregate;
  const onChange = event => {
    const control = event.target;
    if (control.dataset.option !== undefined) state = changeOption(state, Number(control.dataset.index), Number(control.dataset.option), control.value);
    if (control.dataset.include !== undefined) state = includeStep(state, Number(control.dataset.index), control.checked);
    render();
  };
  const onClick = event => {
    if (event.target.dataset.action === 'review') {
      event.preventDefault();
      state = reviewResult(state);
      render();
      aggregate.cart.scrollIntoView({ block: 'nearest' });
    }
    if (event.target.dataset.action === 'add' || event.target.dataset.action === 'retry') submit();
  };
  const cleanup = () => {
    clearTimeout(timer);
    state = destroyState(state);
    root.removeEventListener('change', onChange);
    root.removeEventListener('click', onClick);
    enhancedNodes.forEach(n => n.remove());
    refs.forEach(r => {
      if (!r) return;
      r.price.textContent = r.originalPrice;
      r.availability.textContent = r.originalAvailability;
      r.card.removeAttribute('data-included');
      r.card.removeAttribute('data-state');
    });
    delete root.dataset.enhanced;
    delete root.splitTension;
  };
  function render() {
    const pending = state.request?.status === 'pending';
    state.steps.forEach((s, i) => {
      const r = resolve(state, i);
      const ui = refs[i];
      if (!ui) return;
      ui.card.dataset.state = s.included && pending ? 'request-pending' : s.included && state.request?.status === 'failure' ? 'request-error' : s.included && state.request?.status === 'success' ? 'request-success' : r.kind;
      ui.card.dataset.included = String(s.included);
      ui.price.textContent = r.variant ? money(r.variant.price, fixture.money) : r.kind === 'unresolved' ? 'Choose options for price' : priceText(fixture.steps[i].product, fixture.money);
      ui.compare.textContent = r.variant?.compareAt > r.variant?.price ? `Previously ${money(r.variant.compareAt, fixture.money)}` : '';
      ui.compare.hidden = !ui.compare.textContent;
      ui.unit.textContent = r.variant?.unitPrice ? `${money(r.variant.unitPrice.price, fixture.money)} / ${r.variant.unitPrice.reference}` : '';
      ui.unit.hidden = !ui.unit.textContent;
      ui.availability.textContent = statusText(r);
      ui.includeLabel.hidden = ['link-only', 'app-owned', 'selling-plan-sensitive', 'fully-sold-out'].includes(r.kind);
      ui.checkbox.checked = s.included;
      ui.checkbox.disabled = pending || !r.eligible;
      ui.includeText.textContent = s.included ? 'Included · quantity 1' : 'Include this product · quantity 1';
      ui.selects.forEach((select, o) => { select.value = s.choices[o]; select.disabled = pending; });
    });
    const total = summary(state);
    // Preserve request recovery even when a 422 leaves fewer than two eligible items.
    aggregate.summary.hidden = !total.showAggregate;
    aggregate.result.hidden = false;
    aggregate.total.textContent = money(total.total, fixture.money);
    aggregate.count.textContent = `${total.count} selected ${total.count === 1 ? 'item' : 'items'}`;
    aggregate.add.disabled = pending || !total.count || (state.request?.status === 'ambiguous' && !state.request.reviewed);
    aggregate.add.textContent = pending ? 'Adding…' : 'Add selected · simulation';
    if (state.request) {
      if (aggregate.status.textContent !== state.request.message) aggregate.status.textContent = state.request.message;
    } else aggregate.status.textContent = '';
    aggregate.review.hidden = !state.request || pending;
    aggregate.cart.hidden = !state.request?.reviewed;
    aggregate.retry.hidden = !['failure', 'ambiguous'].includes(state.request?.status) || !total.showAggregate;
    aggregate.retry.disabled = pending || !total.count || (state.request?.status === 'ambiguous' && !state.request.reviewed);
  }
  function submit() {
    const result = beginRequest(state);
    if (!result.token) {
      if (result.error && aggregate.error.textContent !== result.error) aggregate.error.textContent = result.error;
      if (result.invalid >= 0 && refs[result.invalid]) {
        refs[result.invalid].availability.setAttribute('tabindex', '-1');
        refs[result.invalid].availability.focus();
      }
      return;
    }
    const submitter = document.activeElement;
    aggregate.error.textContent = '';
    state = result.state;
    render();
    timer = setTimeout(() => {
      const completed = finishRequest(state, result.token, fixture.response);
      if (completed === state) return;
      state = completed;
      render();
      // Native disabled buttons can lose focus. Restore the initiating control
      // only if focus stayed on the document and that control remains visible.
      if (document.activeElement === document.body && submitter?.isConnected && root.contains(submitter) && !submitter.closest('[hidden]')) submitter.focus();
    }, 900);
  }
  try {
    // The deliberate failure precedes any visible enhancement or fallback mutation.
    if (options.fail) throw new Error('Deliberate initialization failure');
    fixture.steps.forEach((s, i) => {
      const card = root.querySelector(`[data-step="${i}"]`);
      if (!s.product || !card) { refs[i] = null; return; }
      const info = card.querySelector('.product-info');
      const controls = node('div', 'enhancement');
      controls.hidden = true;
      const selects = [];
      const r = resolve(state, i);
      if (!['link-only', 'selling-plan-sensitive', 'app-owned', 'fully-sold-out'].includes(r.kind) && s.product.options.length) {
        const group = node('fieldset', 'options');
        group.append(node('legend', '', `Choose options for ${s.product.title}`));
        s.product.options.forEach((option, o) => {
          const label = node('label', 'option-label', option.name);
          const select = node('select');
          select.id = `${root.id}-step-${i}-option-${o}`;
          select.name = select.id;
          select.dataset.index = String(i);
          select.dataset.option = String(o);
          select.setAttribute('aria-describedby', `${root.id}-step-${i}-state`);
          label.htmlFor = select.id;
          const placeholder = node('option', '', 'Choose…');
          placeholder.value = '';
          select.append(placeholder);
          option.values.forEach(value => { const choice = node('option', '', value); choice.value = value; select.append(choice); });
          group.append(label, select);
          selects.push(select);
        });
        controls.append(group);
      }
      const compare = node('p', 'compare-at');
      const unit = node('p', 'unit-price');
      const includeLabel = node('label', 'include');
      const checkbox = node('input');
      checkbox.type = 'checkbox';
      checkbox.id = `${root.id}-step-${i}-include`;
      checkbox.name = checkbox.id;
      checkbox.dataset.index = String(i);
      checkbox.dataset.include = '';
      checkbox.setAttribute('aria-label', `Include ${s.product.title} · quantity 1`);
      checkbox.setAttribute('aria-describedby', `${root.id}-step-${i}-state`);
      const includeText = node('span');
      includeLabel.append(checkbox, includeText);
      controls.append(compare, unit, includeLabel);
      const availability = info.querySelector('.availability');
      availability.id = `${root.id}-step-${i}-state`;
      refs[i] = { card, price: info.querySelector('.price'), availability, originalPrice: info.querySelector('.price').textContent, originalAvailability: availability.textContent, compare, unit, checkbox, includeLabel, includeText, selects };
      // Keep options/inclusion before the persistent safe product link in DOM order.
      info.insertBefore(controls, info.querySelector('.product-link'));
      enhancedNodes.push(controls);
    });
    const summaryNode = node('div', 'selection-summary');
    summaryNode.hidden = true;
    const count = node('p', 'selected-count');
    const total = node('strong', 'total');
    const add = node('button', 'primary', 'Add selected · simulation');
    add.type = 'button'; add.dataset.action = 'add';
    summaryNode.append(node('p', 'eyebrow', 'Your selection'), count, total, node('p', 'total-context', 'Selected-items total only. Taxes, shipping, duties and discounts are determined at checkout.'), add);
    const result = node('div', 'request-result');
    const status = node('p', 'request-status');
    status.setAttribute('role', 'status'); status.setAttribute('aria-atomic', 'true');
    const error = node('p', 'request-error');
    error.setAttribute('role', 'alert');
    const review = node('a', 'product-link', 'Review simulated cart');
    review.href = `#${root.id}-cart`; review.dataset.action = 'review';
    const cart = node('p', 'cart-review', 'Simulation only: no real cart or item-level reconciliation is available here. Review authoritative cart contents before any real retry. Retrying this harness repeats its fixture response.');
    cart.id = `${root.id}-cart`;
    const retry = node('button', 'secondary', 'Retry simulation');
    retry.type = 'button'; retry.dataset.action = 'retry';
    result.append(status, review, cart, retry);
    // Mount live regions empty, then update them only when request state changes.
    const transaction = node('div', 'transaction');
    transaction.append(summaryNode, error, result);
    root.append(transaction);
    enhancedNodes.push(transaction);
    aggregate = { summary: summaryNode, count, total, add, status, error, result, review, cart, retry };
    root.addEventListener('change', onChange);
    root.addEventListener('click', onClick);
    render();
    enhancedNodes.forEach(n => { if (n.classList.contains('enhancement')) n.hidden = false; });
    root.dataset.enhanced = 'true';
    root.splitTension = {
      destroy: cleanup,
      getState: () => state,
      reset() {
        clearTimeout(timer);
        state = { ...createState(fixture), version: state.version + 1 };
        aggregate.error.textContent = '';
        render();
      }
    };
    return root.splitTension;
  } catch (error) {
    cleanup();
    throw error;
  }
}

export function bootstrap(doc = document) {
  const selector = doc.querySelector('#fixture');
  const host = doc.querySelector('#instances');
  if (host.splitTensionHarness) return host.splitTensionHarness;
  const diagnostics = doc.querySelector('#diagnostics');
  const label = doc.querySelector('#fixture-label');
  let controllers = [];
  let historyResetTimer = null;
  function mount(fixture, preserveBaseline = false) {
    controllers.forEach(c => c.destroy());
    controllers = [];
    if (!preserveBaseline) {
      host.replaceChildren(...Array.from({ length: fixture.instances || 1 }, (_, i) => renderBaseline(fixture, `split-${i + 1}`)));
    }
    Array.from(host.children).forEach((root, i) => {
      if (fixture.enhance === false) return;
      try { controllers.push(initInstance(root, fixture, { fail: fixture.failFirst && i === 0 })); }
      catch { diagnostics.textContent = `${fixture.diagnostic} Initialization failure contained; product links remain available.`; }
    });
    selector.value = fixture.id;
    label.textContent = fixture.label;
  }
  selector.replaceChildren();
  fixtures.forEach(f => { const option = node('option', '', f.label); option.value = f.id; selector.append(option); });
  const initial = getFixture(new URL(location.href).searchParams.get('fixture'));
  diagnostics.textContent = initial.diagnostic;
  mount(initial, initial.id === 'simple' || initial.id === 'no-js');
  selector.disabled = false;
  doc.querySelector('#fixture-control').hidden = false;
  const switchFixture = () => {
    const fixture = getFixture(selector.value);
    diagnostics.textContent = fixture.diagnostic;
    mount(fixture);
    const url = new URL(location.href);
    url.searchParams.set('fixture', fixture.id);
    history.replaceState(null, '', url);
  };
  const restore = () => {
    const fixture = getFixture(new URL(location.href).searchParams.get('fixture'));
    diagnostics.textContent = fixture.diagnostic;
    mount(fixture);
  };
  selector.addEventListener('change', switchFixture);
  window.addEventListener('popstate', restore);
  // Browsers restore native form values after pageshow. Reset on the next task,
  // retaining the literal baseline nodes while discarding restored shopper state.
  const restorePage = () => {
    clearTimeout(historyResetTimer);
    historyResetTimer = setTimeout(() => {
      controllers.forEach(c => c.reset());
      selector.value = getFixture(new URL(location.href).searchParams.get('fixture')).id;
    }, 0);
  };
  window.addEventListener('pageshow', restorePage);
  host.splitTensionHarness = { destroy() {
    clearTimeout(historyResetTimer);
    controllers.forEach(c => c.destroy());
    selector.removeEventListener('change', switchFixture);
    window.removeEventListener('popstate', restore);
    window.removeEventListener('pageshow', restorePage);
    selector.disabled = true;
    doc.querySelector('#fixture-control').hidden = true;
    delete host.splitTensionHarness;
  } };
  return host.splitTensionHarness;
}
if (typeof document !== 'undefined') bootstrap();
