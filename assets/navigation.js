/* Native disclosures keep navigation usable without JavaScript. */
class SiteNavigation extends HTMLElement {
  connectedCallback() {
    this.controller?.abort();
    this.controller = new AbortController();
    const { signal } = this.controller;
    this.addEventListener('keydown', (event) => {
      if (event.key !== 'Escape') return;
      const disclosure = event.target.closest('details[open]');
      if (!disclosure || !this.contains(disclosure)) return;
      disclosure.open = false;
      disclosure.querySelector(':scope > summary')?.focus();
      event.preventDefault();
    }, { signal });
    document.addEventListener('shopify:block:select', (event) => {
      if (this.closest('.shopify-section')?.contains(event.target)) {
        const disclosure = this.querySelector('details');
        if (disclosure) disclosure.open = true;
      }
    }, { signal });
  }
  disconnectedCallback() { this.controller?.abort(); }
}
if (!customElements.get('site-navigation')) customElements.define('site-navigation', SiteNavigation);
