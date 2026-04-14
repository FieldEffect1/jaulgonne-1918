/**
 * Lightbox universel — Jaulgonne 1918
 * S'auto-attache à toutes les images de la page.
 * Compatible avec les appels onclick="openLB(src, caption)" existants.
 */
(function () {

  /* ── CSS injecté ── */
  const style = document.createElement('style');
  style.textContent = `
  /* Navigation prev/next (galerie + événements) */
  #lb-overlay .lb-nav {
    display: flex; align-items: center; gap: 1.5rem; margin-top: .85rem;
  }
  #lb-overlay .lb-btn {
    background: none; border: 1px solid rgba(255,255,255,.18);
    color: #c0b0a0; font-size: 1.1rem; padding: .3rem .8rem;
    cursor: pointer; transition: background .2s, color .2s; line-height: 1;
  }
  #lb-overlay .lb-btn:hover { background: rgba(255,255,255,.1); color: #fff; }
  #lb-counter {
    font-size: .72rem; color: #9a8878; letter-spacing: .04em;
    min-width: 200px; text-align: center;
  }
  `+ `
  #lb-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(5,4,3,.94);
    z-index: 9999;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 2rem 1.5rem 1.5rem;
    cursor: zoom-out;
  }
  #lb-overlay.open { display: flex; }

  #lb-close {
    position: absolute;
    top: 1rem; right: 1.25rem;
    background: none; border: none;
    color: #c0b0a0; font-size: 1.6rem;
    cursor: pointer; line-height: 1;
    padding: .25rem .5rem;
    transition: color .2s;
    z-index: 1;
  }
  #lb-close:hover { color: #fff; }

  #lb-img {
    max-width: 92vw;
    max-height: 82vh;
    object-fit: contain;
    box-shadow: 0 8px 60px rgba(0,0,0,.7);
    cursor: default;
    display: block;
  }

  #lb-caption {
    color: #9a8878;
    font-size: .74rem;
    letter-spacing: .03em;
    line-height: 1.5;
    margin-top: .9rem;
    text-align: center;
    max-width: min(700px, 90vw);
  }

  /* Curseur loupe sur les images cliquables */
  img.lb-enabled { cursor: zoom-in; }
  `;
  document.head.appendChild(style);

  /* ── DOM lightbox ── */
  const overlay = document.createElement('div');
  overlay.id = 'lb-overlay';
  overlay.innerHTML = `
    <button id="lb-close" aria-label="Fermer">✕</button>
    <img id="lb-img" src="" alt="">
    <div id="lb-caption"></div>
  `;
  document.body.appendChild(overlay);

  const lbImg     = overlay.querySelector('#lb-img');
  const lbCaption = overlay.querySelector('#lb-caption');

  /* ── Ouverture / fermeture ── */
  function openLB(src, caption) {
    lbImg.src = src || '';
    lbCaption.textContent = caption || '';
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLB() {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
    // Vider src après la transition pour éviter le flash
    setTimeout(function () { lbImg.src = ''; }, 150);
  }

  /* ── Événements de fermeture ── */
  overlay.querySelector('#lb-close').addEventListener('click', closeLB);
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) closeLB();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeLB();
  });

  /* ── Auto-attachement à toutes les images ── */
  function attachAll() {
    // Exclure : nav, video, images trop petites (icônes/insignes)
    document.querySelectorAll('img').forEach(function (img) {
      if (img.closest('nav'))               return; // barre de navigation
      if (img.closest('video'))             return; // poster vidéo
      if (img.closest('.unit-insigne-box')) return; // insignes régiments
      if (img.classList.contains('lb-skip'))   return; // navigation propre (galerie/événements)
      if (img.classList.contains('lb-enabled')) return; // déjà traité

      img.classList.add('lb-enabled');
      img.addEventListener('click', function () {
        const fig     = img.closest('figure');
        const caption = fig
          ? (fig.querySelector('figcaption')?.textContent?.trim() || img.alt)
          : img.alt;
        openLB(img.src, caption);
      });
    });
  }

  // Lancer après chargement du DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachAll);
  } else {
    attachAll();
  }

  /* ── API globale (compat onclick="openLB(...)" existants) ── */
  window.openLB  = openLB;
  window.closeLB = closeLB;

})();
