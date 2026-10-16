/* Option links work as plain links. With JavaScript, swap the product section in place
   so choosing a size or shade keeps the shopper's scroll position. */
const sectionOf = (el) => el.closest('[data-variant-section]');
let pending;

document.addEventListener('click', async (event) => {
  const link = event.target.closest('a.option-link');
  const section = link && sectionOf(link);
  if (!section || event.defaultPrevented || event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  event.preventDefault();
  if (link.getAttribute('aria-current') === 'true') return;

  const url = new URL(link.href);
  url.searchParams.set('section_id', section.dataset.variantSection);
  const index = [...section.querySelectorAll('a.option-link')].indexOf(link);
  pending?.abort();
  pending = new AbortController();
  section.setAttribute('aria-busy', 'true');

  try {
    const response = await fetch(url, { signal: pending.signal });
    if (!response.ok) throw new Error(response.status);
    const html = new DOMParser().parseFromString(await response.text(), 'text/html');
    const fresh = html.querySelector('[data-variant-section]');
    if (!fresh) throw new Error('missing section');
    section.replaceWith(document.importNode(fresh, true));
    history.replaceState(history.state, '', link.href);
    window.Shopify?.PaymentButton?.init?.();
    document.querySelectorAll('[data-variant-section] a.option-link')[index]?.focus({ preventScroll: true });
  } catch (error) {
    if (error.name !== 'AbortError') window.location.assign(link.href);
  }
});
