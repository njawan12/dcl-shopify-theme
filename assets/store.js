/* Vela store layer: cart drawer, steppers, gallery, sliders, tabs and dialogs.
   Every component enhances working HTML; forms and links still work without it. */

const define = (name, element) => {
  if (!customElements.get(name)) customElements.define(name, element);
};
const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
  || document.documentElement.dataset.motion === 'none';

/* ---------- dialogs ---------- */
function openDialog(dialog, opener) {
  if (!dialog || dialog.open) return;
  dialog.returnFocus = opener || document.activeElement;
  dialog.showModal();
  document.documentElement.classList.add('is-locked');
}
function closeDialog(dialog) {
  if (!dialog?.open) return;
  dialog.classList.add('is-closing');
  const finish = () => {
    dialog.classList.remove('is-closing');
    dialog.close();
  };
  if (reducedMotion()) finish();
  else setTimeout(finish, 200);
}
document.addEventListener('close', (event) => {
  if (!(event.target instanceof HTMLDialogElement)) return;
  if (!document.querySelector('dialog[open]')) document.documentElement.classList.remove('is-locked');
  event.target.returnFocus?.focus?.({ preventScroll: true });
}, true);
document.addEventListener('cancel', (event) => {
  if (!(event.target instanceof HTMLDialogElement)) return;
  event.preventDefault();
  closeDialog(event.target);
}, true);
document.addEventListener('click', (event) => {
  const target = event.target;
  if (target instanceof HTMLDialogElement && target.open) {
    const box = target.getBoundingClientRect();
    const inside = event.clientX >= box.left && event.clientX <= box.right
      && event.clientY >= box.top && event.clientY <= box.bottom;
    if (!inside) closeDialog(target);
    return;
  }
  const closer = target.closest('[data-dialog-close], [data-drawer-close]');
  if (closer) closeDialog(closer.closest('dialog'));
  const search = target.closest('[data-search-open]');
  if (search && document.getElementById('SearchModal')) {
    event.preventDefault();
    const modal = document.getElementById('SearchModal');
    openDialog(modal, search);
    modal.querySelector('input[type="search"]')?.focus();
  }
});

/* ---------- quantity stepper ---------- */
class QuantityStepper extends HTMLElement {
  connectedCallback() {
    this.input = this.querySelector('input');
    this.addEventListener('click', this);
    this.sync();
    this.input?.addEventListener('change', () => this.sync());
  }
  handleEvent(event) {
    const button = event.target.closest('[data-step]');
    if (!button || !this.input) return;
    event.preventDefault();
    const step = Number(this.input.step) || 1;
    const min = this.input.min === '' ? 0 : Number(this.input.min);
    const max = this.input.max === '' ? Infinity : Number(this.input.max);
    const next = Math.min(max, Math.max(min, (Number(this.input.value) || 0) + step * Number(button.dataset.step)));
    if (next === Number(this.input.value)) return;
    this.input.value = next;
    this.sync();
    this.input.dispatchEvent(new Event('change', { bubbles: true }));
  }
  sync() {
    const value = Number(this.input?.value);
    const min = this.input?.min === '' ? 0 : Number(this.input?.min);
    const max = this.input?.max === '' ? Infinity : Number(this.input?.max);
    const [down, up] = this.querySelectorAll('[data-step]');
    if (down) down.disabled = value <= min;
    if (up) up.disabled = value >= max;
  }
}
define('quantity-stepper', QuantityStepper);

/* ---------- cart drawer ---------- */
class CartDrawer extends HTMLElement {
  connectedCallback() {
    this.dialog = this.querySelector('dialog');
    this.addEventListener('change', (event) => {
      if (event.target.matches('input[data-line]')) this.queueChange(event.target);
      if (event.target.matches('[data-cart-note]')) this.saveNote(event.target.value);
    });
    this.addEventListener('click', (event) => {
      const remove = event.target.closest('[data-remove]');
      if (!remove) return;
      event.preventDefault();
      this.change(remove.dataset.remove, 0, remove);
    });
  }
  open(opener) {
    openDialog(this.dialog, opener);
    this.dialog.querySelector('[data-drawer-close]')?.focus();
  }
  queueChange(input) {
    clearTimeout(this.timer);
    this.timer = setTimeout(() => this.change(input.dataset.line, Number(input.value), input), 350);
  }
  async change(line, quantity, control) {
    const focusKey = control?.id || (control?.dataset.remove ? 'remove' : '');
    this.setBusy(true);
    try {
      const response = await fetch(`${this.dataset.changeUrl}.js`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ line: Number(line), quantity, sections: ['cart-drawer'], sections_url: window.location.pathname }),
      });
      const body = await response.json();
      if (!response.ok) throw new Error(body.description || body.message || this.dataset.error);
      this.render(body.sections?.['cart-drawer']);
      const again = focusKey && focusKey !== 'remove' ? this.querySelector(`#${CSS.escape(focusKey)}`) : null;
      (again || this.querySelector('[data-drawer-close]'))?.focus({ preventScroll: true });
    } catch (error) {
      this.message(error.message || this.dataset.error);
      await this.refresh();
    } finally {
      this.setBusy(false);
    }
  }
  async saveNote(note) {
    try {
      await fetch(`${this.dataset.updateUrl}.js`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ note }),
      });
    } catch { /* The note is also editable on the cart page. */ }
  }
  async refresh() {
    try {
      const response = await fetch(`${window.location.pathname}?sections=cart-drawer`);
      const body = await response.json();
      this.render(body['cart-drawer']);
    } catch { /* Keep the current markup. */ }
  }
  render(html) {
    if (!html) return;
    const fresh = new DOMParser().parseFromString(html, 'text/html').querySelector('[data-cart-content]');
    const current = this.querySelector('[data-cart-content]');
    if (!fresh || !current) return;
    current.replaceWith(fresh);
    updateCount(Number(fresh.dataset.count) || 0);
  }
  message(text) {
    const box = this.querySelector('[data-cart-message]');
    if (!box) return;
    box.textContent = text;
    box.hidden = false;
  }
  setBusy(busy) {
    this.dialog?.toggleAttribute('aria-busy', busy);
    this.dialog?.classList.toggle('is-busy', busy);
  }
}
define('cart-drawer', CartDrawer);

function updateCount(count) {
  document.querySelectorAll('[data-cart-count]').forEach((bubble) => {
    bubble.textContent = count;
    bubble.hidden = count === 0;
  });
  document.querySelectorAll('[data-cart-count-label]').forEach((label) => {
    label.textContent = label.textContent.replace(/\d+/, count);
  });
}
const drawer = () => document.querySelector('cart-drawer');

document.addEventListener('click', (event) => {
  const link = event.target.closest('[data-cart-open]');
  if (!link || !drawer() || event.metaKey || event.ctrlKey) return;
  event.preventDefault();
  drawer().open(link);
});

/* Product forms add in place and open the drawer when it is enabled. */
document.addEventListener('submit', async (event) => {
  const form = event.target;
  const cart = drawer();
  if (!cart || !(form instanceof HTMLFormElement) || !form.action.includes('/cart/add')) return;
  if (form.closest('[data-native-form]')) return;
  event.preventDefault();
  const submitter = event.submitter;
  const data = new FormData(form, submitter);
  data.delete('sections');
  data.append('sections', 'cart-drawer');
  data.append('sections_url', window.location.pathname);
  const buttons = form.querySelectorAll('button[type="submit"], button:not([type])');
  buttons.forEach((button) => button.setAttribute('aria-busy', 'true'));
  submitter?.classList.add('is-loading');
  let errorBox = form.querySelector('[data-form-error]');
  try {
    const response = await fetch(`${cart.dataset.addUrl}.js`, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
    const body = await response.json();
    if (!response.ok) throw new Error(body.description || body.message || cart.dataset.error);
    if (errorBox) errorBox.hidden = true;
    cart.render(body.sections?.['cart-drawer']);
    cart.open(submitter);
    form.closest('dialog')?.close();
  } catch (error) {
    if (!errorBox) {
      errorBox = document.createElement('p');
      errorBox.className = 'form-error';
      errorBox.setAttribute('role', 'alert');
      errorBox.dataset.formError = '';
      form.append(errorBox);
    }
    errorBox.textContent = error.message;
    errorBox.hidden = false;
  } finally {
    buttons.forEach((button) => button.removeAttribute('aria-busy'));
    submitter?.classList.remove('is-loading');
  }
});
document.addEventListener('vela:cart-updated', (event) => {
  const cart = drawer();
  if (!cart) return;
  cart.render(event.detail?.sections?.['cart-drawer']);
  cart.open(event.detail?.opener);
});

/* ---------- desktop menu: one panel open at a time, opens on hover ---------- */
const hoverable = window.matchMedia('(hover: hover) and (min-width: 990px)');
document.querySelectorAll('.header-menu').forEach((menu) => {
  const items = [...menu.querySelectorAll('.nav-disclosure')];
  items.forEach((item) => {
    let timer;
    item.addEventListener('toggle', () => {
      if (item.open) items.forEach((other) => { if (other !== item) other.open = false; });
    });
    item.addEventListener('mouseenter', () => {
      if (!hoverable.matches) return;
      clearTimeout(timer);
      item.open = true;
    });
    item.addEventListener('mouseleave', () => {
      if (!hoverable.matches) return;
      timer = setTimeout(() => { item.open = false; }, 150);
    });
    item.addEventListener('keydown', (event) => {
      if (event.key !== 'Escape' || !item.open) return;
      item.open = false;
      item.querySelector('summary')?.focus();
    });
  });
  document.addEventListener('click', (event) => {
    if (!menu.contains(event.target)) items.forEach((item) => { item.open = false; });
  });
});

/* ---------- media gallery ---------- */
class MediaGallery extends HTMLElement {
  connectedCallback() {
    this.viewport = this.querySelector('[data-gallery-viewport]');
    this.slides = [...this.querySelectorAll('[data-gallery-slide]')];
    this.thumbs = [...this.querySelectorAll('[data-gallery-thumb]')];
    this.counter = this.querySelector('[data-gallery-current]');
    if (!this.viewport || this.slides.length === 0) return;
    this.thumbs.forEach((thumb, index) => thumb.addEventListener('click', (event) => { event.preventDefault(); this.go(index); }));
    this.querySelector('[data-gallery-prev]')?.addEventListener('click', () => this.go(this.index - 1));
    this.querySelector('[data-gallery-next]')?.addEventListener('click', () => this.go(this.index + 1));
    this.observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && entry.intersectionRatio > 0.6) this.mark(this.slides.indexOf(entry.target));
      });
    }, { root: this.viewport, threshold: [0.6] });
    this.slides.forEach((slide) => this.observer.observe(slide));
    const start = Math.max(0, this.slides.findIndex((slide) => slide.hasAttribute('data-selected')));
    this.index = 0;
    if (start > 0) this.go(start, true);
    else this.mark(0);
    this.querySelectorAll('[data-zoom]').forEach((button) => button.addEventListener('click', () => this.zoom(button)));
  }
  disconnectedCallback() { this.observer?.disconnect(); }
  go(index, instant = false) {
    const target = this.slides[(index + this.slides.length) % this.slides.length];
    if (!target) return;
    this.viewport.scrollTo({ left: target.offsetLeft - this.viewport.offsetLeft, behavior: instant || reducedMotion() ? 'auto' : 'smooth' });
    this.mark(this.slides.indexOf(target));
  }
  mark(index) {
    if (index < 0) return;
    this.index = index;
    this.thumbs.forEach((thumb, i) => thumb.setAttribute('aria-current', i === index ? 'true' : 'false'));
    this.slides.forEach((slide, i) => slide.toggleAttribute('data-active', i === index));
    if (this.counter) this.counter.textContent = index + 1;
    this.slides.forEach((slide, i) => {
      if (i !== index) slide.querySelectorAll('video').forEach((video) => video.pause());
    });
  }
  zoom(button) {
    const dialog = this.querySelector('[data-zoom-dialog]');
    if (!dialog) return;
    openDialog(dialog, button);
    const target = dialog.querySelector(`[data-zoom-index="${button.dataset.zoom}"]`);
    target?.scrollIntoView({ block: 'start', behavior: 'auto' });
    dialog.querySelector('[data-dialog-close]')?.focus({ preventScroll: true });
  }
}
define('media-gallery', MediaGallery);

/* ---------- sticky add to cart ---------- */
class StickyBuy extends HTMLElement {
  connectedCallback() {
    const target = document.getElementById(this.dataset.watch);
    if (!target) return;
    this.observer = new IntersectionObserver(([entry]) => {
      const below = entry.boundingClientRect.top < 0;
      this.toggleAttribute('data-visible', !entry.isIntersecting && below);
    });
    this.observer.observe(target);
  }
  disconnectedCallback() { this.observer?.disconnect(); }
}
define('sticky-buy', StickyBuy);

/* ---------- horizontal sliders (carousels, slideshow) ---------- */
class SlideTrack extends HTMLElement {
  connectedCallback() {
    this.viewport = this.querySelector('[data-track]');
    if (!this.viewport) return;
    this.items = [...this.viewport.children];
    this.prev = this.querySelector('[data-track-prev]');
    this.next = this.querySelector('[data-track-next]');
    this.dots = [...this.querySelectorAll('[data-track-dot]')];
    this.prev?.addEventListener('click', () => this.step(-1));
    this.next?.addEventListener('click', () => this.step(1));
    this.dots.forEach((dot, index) => dot.addEventListener('click', () => this.go(index)));
    this.viewport.addEventListener('scroll', () => {
      cancelAnimationFrame(this.frame);
      this.frame = requestAnimationFrame(() => this.update());
    }, { passive: true });
    this.update();
    this.autoplay = Number(this.dataset.autoplay) || 0;
    this.pause = this.querySelector('[data-track-pause]');
    if (this.autoplay && !reducedMotion() && !window.Shopify?.designMode) this.play();
    this.pause?.addEventListener('click', () => (this.playing ? this.stop(true) : this.play()));
    this.addEventListener('focusin', () => this.stop());
    this.addEventListener('mouseenter', () => this.stop());
    this.addEventListener('mouseleave', () => { if (this.autoplay && !this.userPaused && !reducedMotion()) this.play(); });
    document.addEventListener('shopify:block:select', (event) => {
      const index = this.items.findIndex((item) => item.contains(event.target));
      if (index >= 0) { this.stop(true); this.go(index); }
    });
  }
  disconnectedCallback() { clearInterval(this.timer); }
  pageSize() {
    const first = this.items[0];
    if (!first) return 1;
    return Math.max(1, Math.round(this.viewport.clientWidth / first.getBoundingClientRect().width));
  }
  current() {
    const left = this.viewport.scrollLeft * (document.dir === 'rtl' ? -1 : 1);
    const width = this.items[0]?.getBoundingClientRect().width || 1;
    return Math.round(left / width);
  }
  go(index) {
    const item = this.items[Math.max(0, Math.min(index, this.items.length - 1))];
    if (!item) return;
    const offset = item.offsetLeft - this.items[0].offsetLeft;
    this.viewport.scrollTo({ left: offset, behavior: reducedMotion() ? 'auto' : 'smooth' });
  }
  step(direction) {
    const size = this.pageSize();
    let index = this.current() + direction * size;
    if (this.autoplay && index >= this.items.length) index = 0;
    this.go(index);
  }
  update() {
    const max = this.viewport.scrollWidth - this.viewport.clientWidth;
    const left = Math.abs(this.viewport.scrollLeft);
    if (this.prev) this.prev.disabled = left < 4;
    if (this.next) this.next.disabled = !this.autoplay && left > max - 4;
    const index = this.current();
    this.dots.forEach((dot, i) => dot.setAttribute('aria-current', i === index ? 'true' : 'false'));
    this.items.forEach((item, i) => item.toggleAttribute('data-active', i === index));
    this.toggleAttribute('data-scrollable', max > 4);
  }
  play() {
    clearInterval(this.timer);
    this.playing = true;
    this.userPaused = false;
    this.pause?.setAttribute('aria-pressed', 'false');
    this.timer = setInterval(() => this.step(1), this.autoplay * 1000);
  }
  stop(byUser = false) {
    clearInterval(this.timer);
    this.playing = false;
    if (byUser) {
      this.userPaused = true;
      this.pause?.setAttribute('aria-pressed', 'true');
    }
  }
}
define('slide-track', SlideTrack);

/* ---------- tabs ---------- */
class TabSet extends HTMLElement {
  connectedCallback() {
    this.tabs = [...this.querySelectorAll('[role="tab"]')];
    this.panels = [...this.querySelectorAll('[role="tabpanel"]')];
    this.tabs.forEach((tab, index) => {
      tab.addEventListener('click', (event) => { event.preventDefault(); this.select(index); });
      tab.addEventListener('keydown', (event) => {
        const keys = { ArrowRight: 1, ArrowLeft: -1 };
        if (!(event.key in keys)) return;
        const direction = document.dir === 'rtl' ? -keys[event.key] : keys[event.key];
        const next = (index + direction + this.tabs.length) % this.tabs.length;
        this.select(next);
        this.tabs[next].focus();
      });
    });
    this.select(0);
  }
  select(index) {
    this.tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', i === index ? 'true' : 'false');
      tab.tabIndex = i === index ? 0 : -1;
    });
    this.panels.forEach((panel, i) => { panel.hidden = i !== index; });
    this.panels[index]?.querySelectorAll('slide-track').forEach((track) => track.update?.());
  }
}
define('tab-set', TabSet);

/* ---------- before and after ---------- */
class BeforeAfter extends HTMLElement {
  connectedCallback() {
    const input = this.querySelector('input[type="range"]');
    const set = () => this.style.setProperty('--position', `${input.value}%`);
    input?.addEventListener('input', set);
    if (input) set();
  }
}
define('before-after', BeforeAfter);

/* ---------- share ---------- */
class ShareButton extends HTMLElement {
  connectedCallback() {
    this.querySelector('button')?.addEventListener('click', async () => {
      const url = this.dataset.url;
      const status = this.querySelector('[role="status"]');
      try {
        if (navigator.share) await navigator.share({ title: document.title, url });
        else {
          await navigator.clipboard.writeText(url);
          if (status) status.textContent = this.dataset.copied;
        }
      } catch { /* Sharing was cancelled. */ }
    });
  }
}
define('share-button', ShareButton);

/* ---------- newsletter popup ---------- */
class SignupPopup extends HTMLElement {
  connectedCallback() {
    this.dialog = this.querySelector('dialog');
    if (!this.dialog) return;
    const key = 'vela-popup-seen';
    const days = Number(this.dataset.days) || 7;
    if (window.Shopify?.designMode) {
      document.addEventListener('shopify:section:select', (event) => {
        if (this.closest('.shopify-section')?.id === event.target.id) openDialog(this.dialog);
      });
      document.addEventListener('shopify:section:deselect', () => closeDialog(this.dialog));
      return;
    }
    if (this.querySelector('[data-popup-submitted]')) { openDialog(this.dialog); return; }
    let seen = 0;
    try { seen = Number(localStorage.getItem(key)) || 0; } catch { seen = 0; }
    if (Date.now() - seen < days * 86400000) return;
    setTimeout(() => {
      if (document.querySelector('dialog[open]')) return;
      openDialog(this.dialog);
      try { localStorage.setItem(key, String(Date.now())); } catch { /* Private browsing. */ }
    }, (Number(this.dataset.delay) || 5) * 1000);
  }
}
define('signup-popup', SignupPopup);

/* ---------- reveal on scroll (optional, motion aware) ---------- */
if (!reducedMotion() && 'IntersectionObserver' in window) {
  const reveal = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-revealed');
      reveal.unobserve(entry.target);
    });
  }, { rootMargin: '0px 0px -10% 0px' });
  const watch = (root) => root.querySelectorAll('[data-reveal]').forEach((node) => reveal.observe(node));
  document.documentElement.classList.add('has-reveal');
  watch(document);
  document.addEventListener('shopify:section:load', (event) => watch(event.target));
}

/* ---------- collection and search filters ---------- */
class FacetForm extends HTMLElement {
  connectedCallback() {
    this.form = this.querySelector('form');
    this.drawer = this.querySelector('.facets__drawer');
    if (!this.form) return;
    this.form.addEventListener('change', (event) => {
      const delay = event.target.type === 'number' ? 600 : 0;
      clearTimeout(this.timer);
      this.timer = setTimeout(() => this.apply(event.target), delay);
    });
    this.form.addEventListener('submit', (event) => {
      event.preventDefault();
      if (this.drawer) this.drawer.open = false;
      this.apply();
    });
    this.addEventListener('click', (event) => {
      if (event.target.closest('[data-facets-close]') || event.target === this.drawer) {
        this.drawer.open = false;
        this.drawer.querySelector('summary')?.focus();
      }
      const link = event.target.closest('.facets__active a');
      if (link) { event.preventDefault(); this.load(new URL(link.href, window.location.origin)); }
    });
    this.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && this.drawer?.open) { this.drawer.open = false; this.drawer.querySelector('summary')?.focus(); }
    });
  }
  apply(control) {
    const params = new URLSearchParams();
    for (const [key, value] of new FormData(this.form)) if (value !== '') params.append(key, value);
    const url = new URL(this.form.action, window.location.origin);
    url.search = params.toString();
    this.load(url, control);
  }
  async load(url, control) {
    const section = this.closest('.shopify-section');
    const id = this.dataset.section;
    const keepOpen = this.drawer?.open;
    const focusName = control ? `[name="${CSS.escape(control.name)}"][value="${CSS.escape(control.value)}"], #${CSS.escape(control.id || 'none')}` : null;
    section?.setAttribute('aria-busy', 'true');
    try {
      const fetchUrl = new URL(url);
      fetchUrl.searchParams.set('section_id', id);
      const response = await fetch(fetchUrl);
      if (!response.ok) throw new Error(response.status);
      const html = new DOMParser().parseFromString(await response.text(), 'text/html');
      const fresh = html.querySelector(`#shopify-section-${CSS.escape(id)}`) || html.body.firstElementChild;
      if (!fresh || !section) throw new Error('missing');
      section.innerHTML = fresh.innerHTML;
      history.replaceState(history.state, '', url.pathname + url.search);
      const drawer = section.querySelector('.facets__drawer');
      if (keepOpen && drawer) drawer.open = true;
      if (focusName) section.querySelector(focusName)?.focus({ preventScroll: true });
    } catch {
      window.location.assign(url);
    } finally {
      section?.removeAttribute('aria-busy');
    }
  }
}
define('facet-form', FacetForm);
