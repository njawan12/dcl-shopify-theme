/* Product recommendations load after the page, using Shopify's section rendering.
   If nothing is returned the section stays empty and takes no space. */
class ProductRecommendations extends HTMLElement {
  connectedCallback() {
    if (this.querySelector('.product-recs__grid') || !this.dataset.url) return;
    this.observer?.disconnect();
    this.observer = new IntersectionObserver((entries) => {
      if (!entries.some((entry) => entry.isIntersecting)) return;
      this.observer.disconnect();
      this.load();
    }, { rootMargin: '0px 0px 400px 0px' });
    this.observer.observe(this);
  }

  disconnectedCallback() { this.observer?.disconnect(); }

  async load() {
    try {
      const response = await fetch(this.dataset.url);
      if (!response.ok) return;
      const html = new DOMParser().parseFromString(await response.text(), 'text/html');
      const fresh = html.querySelector('product-recommendations');
      if (fresh && fresh.innerHTML.trim()) this.innerHTML = fresh.innerHTML;
    } catch (error) {
      /* Recommendations are optional; the page is complete without them. */
    }
  }
}

if (!customElements.get('product-recommendations')) {
  customElements.define('product-recommendations', ProductRecommendations);
}
