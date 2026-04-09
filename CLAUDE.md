# Projet Jaulgonne 1918 — Instructions pour Claude

## Sujet du projet

Recherche historique sur les combats autour de **Jaulgonne** (Marne) lors de la **2e bataille de la Marne**, principalement le 15 juillet 1918 et les jours suivants. Zone géographique prioritaire : Jaulgonne – Mézy – Fossoy – Surmelin – Charmel.

L'objectif final est une valorisation de cette histoire locale (site web en cours : `index.html` et pages associées).

---

## Architecture des dossiers

```
Projet_1918/
├── Memory_and_Index/        ← Avancement du projet, index des images, idées pour plus tard
├── Recherches/              ← Toutes les recherches web aspirées ou rédigées
│   ├── Jaulgonne/           ← Sources directement sur Jaulgonne
│   │   ├── cartes_militaires/
│   │   ├── texte_miltaire_fr/
│   │   └── _hors_sujet/
│   ├── batmarn2/            ← Contenu crawlé de batmarn2.free.fr
│   │   └── _textes/
│   ├── jaulgonne_zone/      ← Pages filtrées (score ≥ 7/10) de batmarn2.free.fr
│   │   ├── pages/           ← HTML original
│   │   ├── textes/          ← Texte extrait
│   │   └── images/
│   ├── Document_interessant/  ← Documents de valeur particulière
│   │   ├── Reichsarchiv_Band34_raw/   ← Texte allemand original (HTML + TXT)
│   │   └── Reichsarchiv_Band34_FR/    ← Traduction française (Google Translate)
│   └── public_images/       ← Images libres de droits collectées
└── selection_sources/       ← Sélection finale des sources les plus pertinentes
    ├── 3rd_US/              ← Sources US (3rd Division, etc.)
    ├── AI_generated/        ← Contenus générés par IA
    ├── Illustrations_foret_de_Ris/
    ├── L'ensemble_du_front/
    ├── Moderne/
    └── Videos/
```

Les pages HTML du site (`index.html`, `bataille.html`, etc.) et `museum.css` sont à la **racine du projet**.

---

## Règles de travail

### Sources historiques
- Toujours **cadrer sur la zone Jaulgonne–Mézy–Fossoy–Surmelin**. Ne pas traiter la bataille en général mais son impact local.
- Appliquer une **hiérarchie des sources** (voir `Memory_and_Index/analyse_sources_fiabilite.md`) :
  1. Archives primaires et récits de combattants (grenadiers allemands, rapports US)
  2. Histoires officielles publiées après enquête (CMH, Reichsarchiv)
  3. Mémoires et récits a posteriori (Mondésir — à lire avec recul critique)
- Ne jamais présenter une source unique comme certitude. Croiser les points de vue FR / US / DE.

### Site web
- Style défini dans `museum.css`.
- Ne pas modifier le CSS sans demande explicite.
- Les pages HTML existantes sont : `index.html`, `bataille.html`, `carte_bataille.html`, `evenements.html`, `foret-ris.html`, `galerie.html`, `geographie.html`, `hommage-us.html`, `liberation.html`, `memoire.html`.

### Traductions
- Pour les gros volumes de texte étranger, utiliser **Google Translate via curl/Python** (API gratuite), pas Claude, pour économiser l'abonnement.
- Script type : `translate.googleapis.com/translate_a/single?client=gtx&sl=de&tl=fr&dt=t&q=...`

---

## Ce qui est dans la mémoire (ne pas dupliquer ici)

Les détails sur le profil de l'utilisateur, le feedback sur l'approche, et l'inventaire des sources sont dans le système mémoire Claude (`C:\Users\alexi\.claude\projects\...\memory\`). Ce fichier couvre uniquement l'architecture et les règles de travail.
