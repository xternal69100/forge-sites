(() => {
  'use strict';
  const presets = {
    title: 'Écrire le mouvement, tailler la lumière.',
    paragraph: 'Deux dessins historiques restent disponibles provisoirement pendant leur contre-revue qualité. Les cinq éditions récentes ont été rappelées et ne doivent plus être proposées au téléchargement.',
    glyphs: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789 ÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸ œŒæÆ'
  };
  const cards = [...document.querySelectorAll('.font-card')];
  const search = document.querySelector('#search');
  const category = document.querySelector('#category');
  const preview = document.querySelector('#previewText');
  const size = document.querySelector('#fontSize');
  const sizeOut = document.querySelector('#sizeOut');
  const count = document.querySelector('#resultCount');
  const empty = document.querySelector('#emptyState');
  let mode = 'title';

  function syncSpecimens(text) {
    document.querySelectorAll('.specimen').forEach(item => {
      if (item !== document.activeElement) item.textContent = text;
      item.style.fontSize = `${size.value}px`;
      item.style.lineHeight = mode === 'paragraph' ? '1.35' : '1.02';
    });
    document.querySelectorAll('.mode-label').forEach(item => { item.textContent = `${{title:'Titre',paragraph:'Paragraphe',glyphs:'Glyphes'}[mode]} · ${size.value} px`; });
    sizeOut.textContent = `${size.value} px`;
  }
  function renderPreview() { syncSpecimens(preview.value.trim() || presets[mode]); }
  function renderFilter() {
    const query = search.value.trim().toLocaleLowerCase('fr');
    const chosen = category.value;
    let visible = 0;
    cards.forEach(card => {
      const haystack = `${card.dataset.name} ${card.dataset.category}`.toLocaleLowerCase('fr');
      const show = (!query || haystack.includes(query)) && (chosen === 'all' || card.dataset.category === chosen);
      card.hidden = !show;
      if (show) visible += 1;
    });
    count.textContent = `${visible} famille${visible > 1 ? 's' : ''}`;
    empty.style.display = visible ? 'none' : 'block';
  }
  document.querySelectorAll('[data-mode]').forEach(button => button.addEventListener('click', () => {
    mode = button.dataset.mode;
    document.querySelectorAll('[data-mode]').forEach(item => {
      const active = item === button;
      item.classList.toggle('active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    preview.value = presets[mode];
    size.value = mode === 'paragraph' ? '26' : mode === 'glyphs' ? '42' : '72';
    renderPreview();
  }));
  document.querySelectorAll('.specimen[contenteditable]').forEach(specimen => specimen.addEventListener('input', () => {
    preview.value = specimen.textContent.slice(0, 220);
    syncSpecimens(preview.value);
  }));
  preview.addEventListener('input', renderPreview);
  size.addEventListener('input', renderPreview);
  search.addEventListener('input', renderFilter);
  category.addEventListener('change', renderFilter);
  document.querySelectorAll('[data-dialog]').forEach(button => {
    const dialog = document.querySelector(`#${button.dataset.dialog}`);
    button.addEventListener('click', () => dialog.showModal());
    dialog.querySelector('.close').addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
    dialog.addEventListener('close', () => button.focus());
  });
  renderPreview();
  renderFilter();
})();
