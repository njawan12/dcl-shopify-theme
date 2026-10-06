import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
const source = await readFile(new URL('../../theme/assets/cart-state.js', import.meta.url), 'utf8');
const { updatePayload, errorMessage } = await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);
const input = (lineKey, value) => ({ dataset: { lineKey }, value });
test('same variant with different properties/plans is updated by distinct line keys', () => {
  const result = updatePayload([input('501:property-a', '2'), input('501:plan-b', '3')], 'Gift');
  assert.equal(result.updates['501:property-a'], 2); assert.equal(result.updates['501:plan-b'], 3); assert.equal(result.note, 'Gift');
});
test('zero removal is valid at the API boundary; no line is merged', () => assert.equal(updatePayload([input('501:a', '0')], '').updates['501:a'], 0));
for (const [label, value] of [['empty',''],['whitespace',' '],['fraction','1.5'],['negative','-1'],['text','bad'],['unsafe','9007199254740992']]) {
  test(`reject ${label} quantity before sending`, () => assert.throws(() => updatePayload([input('501:a', value)], ''), /Invalid/));
}
test('duplicate line keys cannot silently overwrite quantities', () => assert.throws(() => updatePayload([input('a','1'),input('a','2')], ''), /Invalid/));
test('missing line identity cannot mutate cart', () => assert.throws(() => updatePayload([input('', '2')], ''), /Invalid/));
test('server error description/message are displayed; otherwise localized fallback', () => {
  assert.equal(errorMessage({description:'Inventory changed'},'fallback'),'Inventory changed');
  assert.equal(errorMessage({message:'Limit reached'},'fallback'),'Limit reached');
  assert.equal(errorMessage({errors:{}},'localized failure'),'localized failure');
});
