# Questions à approfondir — Recherches 1918

---

## 🔴 PRIORITÉS SITE WEB (prochains chantiers)

### A ter. Doublons de photos à corriger
- `index.html` : doublon dans la mosaïque ou les vignettes de navigation
- `foret-ris.html` : doublons de photos à identifier et remplacer

---

### A bis. Renommer "La Bataille" → "MARNE 1918"
- Changer le titre de la nav, le `<title>`, le hero et les liens vers `bataille.html` dans toutes les pages

---

### B. Timecode Jaulgonne — vidéo page d'accueil (`index.html`)
- **Vidéo** : `selection_sources/Videos/111-h-1365-r1.mp4` (Signal Corps H-1365 reel 1)
- **À faire** : visionner la vidéo et repérer le timecode exact où des images de Jaulgonne apparaissent
- **Puis** : remplacer `v.currentTime = 5` dans le script de `index.html` par ce timecode

---

### C. Mention de la 1re Bataille de la Marne (1914) — à intégrer
- La zone de Jaulgonne / vallée de la Marne est un lieu de bataille **deux fois légendaire** : 1914 et 1918
- **À faire** : ajouter une phrase d'introduction (page d'accueil ou page La Bataille) rappelant la 1re Marne de 1914, pour contextualiser l'importance historique du lieu
- Angle possible : "Quatre ans plus tôt, sur ces mêmes rives…"

---

### D. Enrichissement iconographique — page Événements
- **À faire** : ajouter des photos côté allemand dans la section Friedensturm (15 juillet) de `evenements.html`
- Soldats allemands en position, troupes d'assaut (Stosstruppen), matériel, prisonniers, etc.
- Chercher dans les fonds : Bundesarchiv, IWM, collections privées libres de droits

---

### A. Traduction anglaise complète du site
- **Pages traduites (système data-fr/data-en)** : `liberation.html` (33), `memoire.html` (29), `evenements.html` (16), `galerie.html` (10)
- **Pages sans aucune traduction** : `bataille.html`, `foret-ris.html`, `hommage-us.html`, `index.html`, `geographie.html`, `carte_bataille.html`
- **À faire** : ajouter le bouton de langue + les attributs data-fr/data-en sur les 6 pages non traduites
- **Méthode** : s'inspirer de `liberation.html` qui a l'implémentation complète (bouton + script switchLang)

---


## Vidéo Allemands a creuser d'urgence
https://youtu.be/-xH3vQqoDck?si=DY7bmaMPtiqV16f9

## 1. Informations sur Jaulgonne dans les sources batmarn2.free.fr
- Qu'apprend-on sur Jaulgonne à travers les sources récupérées du site ?
- Unités présentes, dates clés, événements notables
- **Statut** : première synthèse faite ✓ — à approfondir avec d'autres sources

## 2. Artillerie allemande au plus fort de l'offensive
- Quelle était la quantité d'artillerie allemande sur les hauteurs de Jaulgonne ?
- Quelle était la présence allemande dans la **Forêt de Ris** (positions, batteries, unités) ?
- **Statut** : première synthèse faite ✓ — données globales trouvées (1 700 batteries sur 120 km de front), mais pas de chiffres précis par position locale
- **À faire** : chercher des sources plus localisées (journaux de marche de régiments, cartes d'artillerie)

## 3. Les forces aériennes françaises et leur importance dans la bataille
- Quel rôle a joué l'aviation française dans cette bataille (appui infanterie, contre-batterie, bombardement, combats aériens) ?
- Quelles unités aériennes étaient engagées et avec quels appareils ?
- Quelle était l'importance stratégique des bombardements aériens (ponts, concentrations de troupes, ravitaillement) ?
- Les combats aériens : supériorité alliée ou allemande dans le ciel de la Marne ?
- **Statut** : à traiter — fichiers `aviatio1.txt` et `aviatio2.txt` disponibles dans les sources batmarn2

## 4. Citations à mettre en avant (Neiberg — YouTube Short)
- **[3:13]** *"You cannot, cannot, cannot write the French army out of this war"*
- **[3:50]** Les mémoires britanniques : en 1918 ils adorent les Français, dans les années 30 ils les détestent
- Source : `jaulgonne_zone/citations_neiberg_short.md`
- **Statut** : marquées ⭐ dans le fichier — à intégrer dans la présentation du projet
