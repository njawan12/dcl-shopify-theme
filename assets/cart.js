import { updatePayload, errorMessage } from './cart-state.js';
class NativeCart extends HTMLElement {
  connectedCallback() {
    this.listeners?.abort();
    this.listeners = new AbortController();
    this.querySelector('form')?.addEventListener('submit', (event) => this.update(event), { signal: this.listeners.signal });
  }
  disconnectedCallback() {
    this.listeners?.abort();
    this.request?.abort();
  }
  async update(event) {
    if (event.submitter?.name !== 'update') return; // Checkout always remains native.
    event.preventDefault();
    if (this.busy) return;
    const form = event.target;
    if (!form.reportValidity()) return;
    const status = this.querySelector('[data-cart-error]');
    let payload;
    try { payload = updatePayload(form.querySelectorAll('input[data-line-key]'), form.elements.note?.value || ''); }
    catch { status.textContent = this.dataset.error; status.hidden = false; status.focus(); return; }
    this.busy = true;
    this.setAttribute('aria-busy', 'true');
    status.hidden = true;
    this.request = new AbortController();
    const controls = [...form.querySelectorAll('button, fieldset')].map((element) => [element, element.disabled]);
    for (const [element] of controls) element.disabled = true;
    const accelerated = this.querySelector('.accelerated-cart');
    const previousInert = accelerated?.inert;
    if (accelerated) accelerated.inert = true;
    const timeout = setTimeout(() => this.request.abort(), 10000);
    try {
      const response = await fetch(this.dataset.updateUrl, {
        method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify(payload), signal: this.request.signal,
      });
      const body = await response.json();
      if (!response.ok) throw Object.assign(new Error(errorMessage(body, this.dataset.error)), { server: true });
      if (this.isConnected) window.location.assign(this.dataset.cartUrl);
    } catch (error) {
      if (this.isConnected) {
        status.textContent = error.server ? error.message : this.dataset.error;
        status.hidden = false;
        status.focus();
      }
    } finally {
      clearTimeout(timeout);
      for (const [element, disabled] of controls) element.disabled = disabled;
      if (accelerated) accelerated.inert = previousInert;
      this.busy = false;
      this.removeAttribute('aria-busy');
    }
  }
}
if (!customElements.get('native-cart')) customElements.define('native-cart', NativeCart);
