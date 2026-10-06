class PredictiveSearch extends HTMLElement {
  connectedCallback() {
    this.listeners?.abort();
    this.listeners = new AbortController();
    const { signal } = this.listeners;
    this.input = this.querySelector('input[type="search"]');
    this.results = this.querySelector('[data-predictions]');
    this.status = this.querySelector('[data-search-status]');
    this.input?.addEventListener('input', () => {
      clearTimeout(this.timer);
      this.request?.abort();
      this.results.hidden = true;
      this.timer = setTimeout(() => this.suggest(), 250);
    }, { signal });
    this.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        clearTimeout(this.timer);
        this.request?.abort();
        this.results.hidden = true;
        this.input.focus();
      }
    }, { signal });
  }
  disconnectedCallback() {
    clearTimeout(this.timer);
    this.listeners?.abort();
    this.request?.abort();
  }
  async suggest() {
    const query = this.input.value.trim();
    if (query.length < 2) { this.status.textContent = ''; return; }
    const request = new AbortController();
    this.request = request;
    const url = new URL(this.dataset.url, window.location.origin);
    url.searchParams.set('q', query);
    url.searchParams.set('section_id', 'predictive-search');
    url.searchParams.set('resources[type]', 'product,query');
    this.setAttribute('aria-busy', 'true');
    let timedOut = false;
    const timeout = setTimeout(() => { timedOut = true; request.abort(); }, 6000);
    try {
      const response = await fetch(url, { signal: request.signal });
      if (!response.ok) throw new Error('Predictive search failed');
      const page = new DOMParser().parseFromString(await response.text(), 'text/html');
      const content = page.querySelector('#shopify-section-predictive-search');
      if (!content) throw new Error('Missing search section');
      if (!this.isConnected || this.request !== request || request.signal.aborted) return;
      this.results.replaceChildren(...content.childNodes);
      this.results.hidden = false;
      this.status.textContent = '';
    } catch {
      if (this.isConnected && this.request === request && (!request.signal.aborted || timedOut)) this.status.textContent = this.dataset.error;
    } finally {
      clearTimeout(timeout);
      if (this.request === request) this.removeAttribute('aria-busy');
    }
  }
}
if (!customElements.get('predictive-search')) customElements.define('predictive-search', PredictiveSearch);
