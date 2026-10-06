/* Shopify line keys keep identical variants with different properties/plans distinct. */
export function updatePayload(inputs, note) {
  const updates = Object.create(null);
  for (const input of inputs) {
    const key = input.dataset.lineKey;
    const quantity = Number(input.value);
    if (String(input.value).trim() === '' || !key || Object.hasOwn(updates, key) || !Number.isSafeInteger(quantity) || quantity < 0) {
      throw new Error('Invalid cart line or quantity');
    }
    updates[key] = quantity;
  }
  return { updates, note };
}
export function errorMessage(body, fallback) {
  if (typeof body?.description === 'string') return body.description;
  if (typeof body?.message === 'string') return body.message;
  return fallback;
}
