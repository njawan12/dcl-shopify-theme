(function () {
  'use strict';
  const fixtures = window.EDGE_CROP_FIXTURES;
  const hotspotData = window.EDGE_CROP_HOTSPOTS;
  const picker = document.querySelector('#fixture');
  const hotspotRoot = document.querySelector('#hotspots');
  const canvas = document.querySelector('.edge-crop');
  let openTrigger = null;

  function element(tag, attributes = {}, text = '') {
    const node = document.createElement(tag);
    Object.entries(attributes).forEach(([name, value]) => node.setAttribute(name, value));
    if (text) node.textContent = text;
    return node;
  }

  function closeHotspot(restoreFocus = true) {
    if (!openTrigger) return;
    const article = openTrigger.closest('[data-hotspot]');
    article.classList.remove('is-open');
    openTrigger.setAttribute('aria-expanded', 'false');
    const previous = openTrigger;
    openTrigger = null;
    if (restoreFocus) previous.focus();
  }

  function buildHotspot(key, index) {
    const data = hotspotData[key];
    const id = `hotspot-panel-${key}`;
    const article = element('article', { class: `hotspot anchor-${data.anchor}`, 'data-hotspot': '' });
    const trigger = element('button', { class: 'hotspot-trigger', type: 'button', 'aria-expanded': 'false', 'aria-controls': id });
    trigger.append(element('span', { 'aria-hidden': 'true' }, String(index + 1)), element('span', { class: 'visually-hidden' }, `Open ${data.label}`));
    const panel = element('div', { class: `hotspot-panel${data.kind === 'product' ? ' product-panel' : ''}`, id });
    panel.append(element('button', { class: 'panel-close', type: 'button', 'aria-label': `Close ${data.label}` }, '×'), element('p', { class: 'panel-kicker' }, data.kicker));
    if (data.product) {
      const summary = element('div', { class: 'product-summary' });
      summary.append(element('img', { src: data.product.image, alt: '', width: '1200', height: '1200', loading: 'lazy' }));
      const copy = element('div');
      copy.append(element('h2', {}, data.product.title));
      const price = element('p', { class: 'price' });
      price.append(element('span', {}, data.product.price));
      if (data.product.compareAtPrice) price.append(' ', element('s', {}, data.product.compareAtPrice));
      copy.append(price);
      summary.append(copy);
      panel.append(summary, element('p', { class: `availability${data.product.available ? '' : ' unavailable'}` }, data.product.available ? 'Available' : 'Sold out'));
      panel.append(element('a', { href: data.product.url }, `View ${data.product.title}`));
    } else {
      panel.append(element('h2', {}, data.title), element('p', {}, data.body));
    }
    article.append(trigger, panel);
    return article;
  }

  function applyFixture(key, announce = true, hydrateInitial = false) {
    const fixture = fixtures[key] || fixtures.beauty;
    closeHotspot(false);
    document.querySelector('#eyebrow').textContent = fixture.eyebrow;
    document.querySelector('#eyebrow').hidden = !fixture.eyebrow;
    document.querySelector('#canvas-heading').textContent = fixture.heading;
    document.querySelector('#body-copy').textContent = fixture.body;
    document.querySelector('#body-copy').hidden = !fixture.body;
    const action = document.querySelector('#primary-action');
    action.textContent = fixture.action;
    action.closest('.action-wrap').hidden = !fixture.action;
    const mobileSource = document.querySelector('#mobile-source');
    if (fixture.mobileImage) { mobileSource.srcset = fixture.mobileImage; mobileSource.media = '(max-width: 47.99rem)'; }
    else { mobileSource.removeAttribute('srcset'); mobileSource.media = '(max-width: 0px)'; }
    const image = document.querySelector('#hero-image');
    image.src = fixture.image;
    image.alt = fixture.alt;
    canvas.classList.toggle('is-neutral', Boolean(fixture.neutral));
    const diagnostic = document.querySelector('#fixture-diagnostic');
    diagnostic.textContent = fixture.diagnostic || '';
    diagnostic.hidden = !fixture.diagnostic;
    if (!hydrateInitial) hotspotRoot.replaceChildren(...fixture.hotspots.map(buildHotspot));
    if (announce) document.querySelector('#fixture-status').textContent = `${fixture.label} loaded`;
    const url = new URL(window.location.href);
    url.searchParams.set('fixture', key);
    history.replaceState({}, '', url);
  }

  hotspotRoot.addEventListener('click', (event) => {
    const trigger = event.target.closest('.hotspot-trigger');
    if (trigger) {
      const wasOpen = trigger === openTrigger;
      closeHotspot(wasOpen);
      if (!wasOpen) {
        openTrigger = trigger;
        trigger.closest('[data-hotspot]').classList.add('is-open');
        trigger.setAttribute('aria-expanded', 'true');
        const panel = document.getElementById(trigger.getAttribute('aria-controls'));
        const focusTarget = panel.querySelector('button, a[href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        if (focusTarget) focusTarget.focus();
      }
      return;
    }
    if (event.target.closest('.panel-close')) closeHotspot();
  });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeHotspot(); });
  document.addEventListener('pointerdown', (event) => { if (openTrigger && !event.target.closest('[data-hotspot]')) closeHotspot(false); });
  picker.addEventListener('change', () => applyFixture(picker.value));
  const initial = new URLSearchParams(location.search).get('fixture');
  picker.value = fixtures[initial] ? initial : 'beauty';
  const canHydrateServerMarkup = picker.value === 'beauty' && hotspotRoot.querySelectorAll('[data-hotspot]').length === fixtures.beauty.hotspots.length;
  applyFixture(picker.value, false, canHydrateServerMarkup);
  document.documentElement.classList.add('js');
}());
