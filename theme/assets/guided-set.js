/* Guided set: shoppers tick the steps they want and add them in one request.
   Without JavaScript each step keeps its own native product form. The total is the
   plain sum of the selected variant prices; no bundle discount is implied. */
class GuidedSet extends HTMLElement {
  connectedCallback() {
    this.controller?.abort();
    this.controller = new AbortController();
    const { signal } = this.controller;
    this.summary = this.querySelector('.guided-summary');
    this.checks = [...this.querySelectorAll('.guided-step__check input')];
    if (!this.summary || this.checks.length === 0) return;

    this.classList.add('is-enhanced');
    this.querySelectorAll('.guided-step__check').forEach((label) => { label.hidden = false; });
    this.querySelectorAll('.guided-step__info form').forEach((form) => { form.hidden = true; });
    this.summary.hidden = false;

    this.count = this.summary.querySelector('[data-count]');
    this.total = this.summary.querySelector('[data-total]');
    this.error = this.summary.querySelector('[data-error]');
    this.button = this.summary.querySelector('[data-add]');
    this.format = this.formatter();

    this.addEventListener('change', () => this.update(), { signal });
    this.button.addEventListener('click', () => this.add(), { signal });
    this.update();
  }

  disconnectedCallback() { this.controller?.abort(); }

  formatter() {
    try {
      return new Intl.NumberFormat(this.dataset.locale || undefined, {
        style: 'currency',
        currency: this.dataset.currency || 'USD',
      });
    } catch (error) {
      return null;
    }
  }

  selected() { return this.checks.filter((input) => input.checked); }

  update() {
    const chosen = this.selected();
    const cents = chosen.reduce((sum, input) => sum + Number(input.dataset.price || 0), 0);
    this.count.textContent = String(chosen.length);
    if (this.format) this.total.textContent = this.format.format(cents / 100);
    this.button.disabled = chosen.length === 0;
    this.error.hidden = true;
  }

  async add() {
    const items = this.selected().map((input) => ({ id: Number(input.value), quantity: 1 }));
    if (items.length === 0) return;
    this.button.disabled = true;
    this.setAttribute('aria-busy', 'true');
    try {
      const response = await fetch(`${this.dataset.addUrl}.js`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ items }),
      });
      if (!response.ok) throw new Error(String(response.status));
      window.location.assign(this.dataset.cartUrl);
    } catch (error) {
      this.error.hidden = false;
      this.button.disabled = false;
    } finally {
      this.removeAttribute('aria-busy');
    }
  }
}

if (!customElements.get('guided-set')) customElements.define('guided-set', GuidedSet);
