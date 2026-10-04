import assert from 'node:assert/strict';
import { fixtures, getFixture } from '../fixtures.js';
import { createState, resolve, summary, changeOption, includeStep, beginRequest, finishRequest, destroyState, reviewResult, money } from '../split-tension.js';
let assertions = 0;
const check = (condition, message) => { assert.ok(condition, message); assertions++; };
const equal = (actual, expected, message) => { assert.deepEqual(actual, expected, message); assertions++; };
const choose = (s, size, finish) => changeOption(changeOption(s, 0, 0, size), 0, 1, finish);
for (const f of fixtures) {
  const s = createState(f);
  check(s.steps.every(step => !step.included), `${f.id}: no assumed consent`);
  equal(summary(s).total, 0, `${f.id}: exact initial zero`);
  equal(summary(s).count, 0, `${f.id}: initial count zero`);
  equal(beginRequest(s).token, null, `${f.id}: cannot submit initial state`);
  let selected = s;
  f.steps.forEach((_, i) => { selected = includeStep(selected, i, true); });
  check(summary(selected).selected.every(item => resolve(selected, item.index).eligible), `${f.id}: only valid selections`);
  const started = beginRequest(selected);
  if (started.token) {
    check(started.state.request.payload.every(line => line.quantity === 1 && Object.keys(line).length === 2), `${f.id}: bounded payload`);
    equal(includeStep(started.state, 0, false), started.state, `${f.id}: frozen pending inclusion`);
    equal(changeOption(started.state, 0, 0, ''), started.state, `${f.id}: frozen pending options`);
    const result = finishRequest(started.state, started.token, f.response);
    check(result.request.status !== 'pending', `${f.id}: deterministic result`);
  }
}
// Resolve every tuple in the 2-, 6- and 24-variant maximum-density subcases.
const maximum = getFixture('maximum');
for (let index = 2; index < 5; index++) {
  for (const variant of maximum.steps[index].product.variants) {
    let candidate = createState(maximum);
    variant.options.forEach((value, option) => { candidate = changeOption(candidate, index, option, value); });
    equal(resolve(candidate, index).variant.id, variant.id, 'dense variant resolves exactly');
    candidate = includeStep(candidate, index, true);
    equal(summary(candidate).total, variant.price, 'dense tuple contributes its price only');
  }
}
let s = createState(getFixture('multi-option'));
equal(resolve(s, 0).kind, 'unresolved', 'required choices initially unresolved');
const corrupted = { ...s, steps: s.steps.map((step, index) => index === 0 ? { ...step, included: true } : step) };
equal(beginRequest(corrupted).invalid, 0, 'pre-submit invalid inclusion identifies first affected step');
equal(beginRequest(corrupted).token, null, 'pre-submit invalid inclusion never sends');
s = choose(s, '30 ml', 'Light');
equal(resolve(s, 0).kind, 'resolved-available', 'explicit tuple resolves');
s = includeStep(s, 0, true);
equal(summary(s).total, 2900, 'included resolved amount');
s = choose(s, '60 ml', 'Rich');
equal(resolve(s, 0).kind, 'unresolved', 'nonexistent tuple invalidates');
equal(resolve(s, 0).variant, null, 'no stale variant identity');
equal(summary(s).total, 0, 'nonexistent tuple removes stale money');
check(!s.steps[0].included, 'invalid state clears consent');
s = choose(s, '60 ml', 'Light');
check(!s.steps[0].included, 'recovery never re-includes');
s = includeStep(s, 0, true);
equal(summary(s).total, 4700, 'price mutation updates exact total');
equal(resolve(s, 0).variant.compareAt, undefined, 'compare-at disappears');
equal(resolve(s, 0).variant.unitPrice.price, 7833, 'unit-price changes together');
s = choose(s, '30 ml', 'Light');
check(s.steps[0].included, 'continuous valid mutation preserves explicit consent');
equal(resolve(s, 0).variant.compareAt, 3400, 'compare-at reappears');
equal(summary(s).total, 2900, 'price and compare-at never sum');
s = choose(s, '30 ml', 'Rich');
equal(resolve(s, 0).kind, 'resolved-sold-out', 'sold-out tuple truthful');
check(!s.steps[0].included, 'sold-out clears inclusion');
equal(summary(s).total, 0, 'sold-out cannot contribute');
s = changeOption(s, 0, 0, '');
equal(resolve(s, 0).variant, null, 'partial selection cannot retain variant');
const duplicate = createState(getFixture('duplicate'));
equal(resolve(duplicate, 0).kind, 'link-only', 'first duplicate narrowed');
equal(resolve(duplicate, 2).kind, 'link-only', 'second duplicate narrowed');
check(!summary(duplicate).showAggregate, 'one remaining eligible omits aggregate');
for (const id of ['ineligible', 'one-surviving', 'fully-sold-out']) check(!summary(createState(getFixture(id))).showAggregate, `${id}: aggregate omitted`);
for (const id of ['selling-plan', 'quantity-rule', 'properties', 'mixed']) {
  const state = createState(getFixture(id));
  const last = state.steps.length - 1;
  check(!resolve(state, last).eligible, `${id}: unsafe purchase excluded`);
  check(!includeStep(state, last, true).steps[last].included, `${id}: cannot acquire consent`);
}
for (let i = 0; i < 5; i++) {
  const ratio = getFixture('localized').steps[i].copy.length / getFixture('maximum').steps[i].copy.length;
  check(ratio >= 1.3 && ratio <= 1.5, 'localized body expansion in 30–50% range');
}
let exact = createState(getFixture('money'));
exact = includeStep(includeStep(exact, 0, true), 1, true);
equal(summary(exact).total, 303, 'three-decimal exact sum');
check(money(303, exact.fixture.money).includes('0.303'), 'context digits preserved');
check(money(101, { currency: 'JPY', digits: 0, locale: 'en-JP' }).includes('101'), 'zero-decimal formatter');
check(money(2400, getFixture('simple').money).includes('24.00'), 'two-decimal formatter');
for (const mode of ['failure', 'ambiguous', 'success', 'inventory']) {
  let state = createState(getFixture('simple'));
  state = includeStep(includeStep(state, 0, true), 1, true);
  const start = beginRequest(state);
  equal(beginRequest(start.state).token, null, 'duplicate submit blocked');
  const done = finishRequest(start.state, start.token, mode);
  if (mode === 'failure') {
    check(done.steps.every(step => step.included), 'failure retains valid consent');
    check(done.request.message.includes('failed'), 'failure message truthful');
  }
  if (mode === 'ambiguous') {
    check(!done.request.message.includes('confirmation:'), 'ambiguity never claims success');
    equal(beginRequest(done).token, null, 'ambiguous retry gated on review');
    equal(beginRequest(includeStep(done, 1, false)).token, null, 'selection mutation cannot bypass ambiguous review');
    check(Boolean(beginRequest(reviewResult(done)).token), 'review enables explicit simulated retry');
  }
  if (mode === 'inventory') {
    check(!done.steps[0].included && done.steps[1].included, '422 clears invalid item only');
    equal(resolve(done, 0).kind, 'fully-sold-out', '422 availability change');
    equal(summary(done).total, 3800, '422 removes stale amount');
    check(!summary(done).showAggregate, '422 reduces aggregate eligibility');
  }
  equal(finishRequest(start.state, start.token + 1, mode), start.state, 'wrong version rejected');
  equal(finishRequest(destroyState(start.state), start.token, mode).alive, false, 'destroyed instance rejects response');
}
// A real local timer arrives after a fixture switch. Only the captured instance receives it;
// its dead/version guard rejects the response and the replacement remains pristine.
let old = beginRequest(includeStep(createState(getFixture('simple')), 0, true));
let oldState = old.state;
const callback = new Promise(resolveTimer => setTimeout(() => {
  const result = finishRequest(oldState, old.token, 'success');
  equal(result, oldState, 'pending fixture switch rejects late timer response');
  resolveTimer();
}, 10));
oldState = destroyState(oldState);
const replacement = createState(getFixture('neutral'));
await callback;
equal(summary(replacement).total, 0, 'replacement currency and totals untouched');
equal(replacement.request, null, 'replacement gets no old result');
let first = includeStep(createState(getFixture('two-instances')), 1, true);
const second = createState(getFixture('two-instances'));
first = beginRequest(first).state;
equal(summary(second).total, 0, 'second instance independent');
equal(second.request, null, 'pending request scoped');
equal(getFixture('unknown').id, 'simple', 'unknown fixture fallback');
console.log(`PASS: ${assertions} state-transition assertions across 24 fixtures.`);
