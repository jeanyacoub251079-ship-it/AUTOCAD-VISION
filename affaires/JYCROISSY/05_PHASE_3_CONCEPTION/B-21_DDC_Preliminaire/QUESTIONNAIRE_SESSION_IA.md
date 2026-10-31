# Questionnaire de capacités IA — Début de session

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Date :** 2026-10-31
**Contexte :** Échec de visualisation géométrique — B-20 V2, B-21 V2, B-22 V2 invalidés. Leçons tirées.
**Usage :** À poser à l'IA en début de toute nouvelle session de projet.

---

## SECTION 1 — CAPACITÉS DE VISUALISATION

**Q1.** Peux-tu visualiser les fichiers DXF, PDF, PNG ?
- [ ] Oui — je peux les afficher et les interpréter visuellement
- [ ] Non — je ne peux que les parsing textuellement (coordonnées, entités)
- [ ] Partiellement — je peux extraire des données mais pas vérifier visuellement

**Q2.** Si tu ne peux pas visualiser, comment vas-tu interpréter la géométrie ?
- [ ] Calculs de coordonnées par analyse textuelle
- [ ] Interprétation des blocs et entités DXF
- [ ] Autre : ________________

**Q3.** Peux-tu distinguer un mur porteur d'un mur non porteur dans un DXF ?
- [ ] Oui
- [ ] Non
- [ ] J'ai besoin d'informations supplémentaires (couche, nom de bloc, etc.)

**Q4.** Peux-tu identifier les axes, travées et cotes dans un plan ?
- [ ] Oui
- [ ] Non
- [ ] Partiellement — seulement si les informations sont explicitement étiquetées

---

## SECTION 2 — FIABILITÉ DES DONNÉES EXTRAITES

**Q5.** Quand tu extrais des coordonnées d'un DXF, à quel niveau de fiabilité ?
- [ ] Fiabilité élevée — les coordonnées sont exactes et vérifiées
- [ ] Fiabilité moyenne — les coordonnées sont extraites mais non vérifiées visuellement
- [ ] Fiabilité faible — je ne peux pas garantir que l'interprétation correspond à la réalité

**Q6.** Si je te demande de « vérifier » un fichier DXF, qu'est-ce que cela signifie pour toi ?
- [ ] Je peux afficher le fichier et vérifier visuellement
- [ ] Je peux parsing le fichier et vérifier la cohérence des données
- [ ] Je ne peux pas vérifier — je peux seulement extraire des données

**Q7.** Comment vais-tu me communiquer une incertitude sur la géométrie ?
- [ ] Je vais explicitement dire « je ne suis pas sûr de cette interprétation »
- [ ] Je vais produire le livrable avec une note d'incertitude
- [ ] Je ne vais pas communiquer l'incertitude — je vais produire le livrable comme si j'étais certain

---

## SECTION 3 — LIMITATIONS ET PROTOCOLE

**Q8.** Quelles sont les situations où tu ne peux pas travailler correctement ?
- [ ] Plans complexes avec géométrie non explicite
- [ ] Fichiers avec couches non standardisées
- [ ] Projets où la visualisation est essentielle
- [ ] Autre : ________________

**Q9.** Si tu ne peux pas interpréter correctement la géométrie, que vas-tu faire ?
- [ ] Tu vas m'arrêter et demander des informations supplémentaires
- [ ] Tu vas produire un livrable avec une note d'incertitude
- [ ] Tu vas produire un livrable sans communiquer l'incertitude

**Q10.** Quel est le protocole pour valider un livrable avant de continuer ?
- [ ] Je peux vérifier visuellement et confirmer
- [ ] Je peux vérifier les calculs mais pas la géométrie
- [ ] Je ne peux pas vérifier — je vais produire et attendre ta validation

---

## SECTION 4 — COMMANDE DES INFORMATIONS

**Q11.** Quelles informations minimales dois-je te fournir pour que tu puisses travailler ?
- [ ] Plan avec axes et cotes explicites
- [ ] Tableau des murs porteurs avec coordonnées
- [ ] Tableau des travées
- [ ] Fichiers DXF avec couches standardisées
- [ ] Autre : ________________

**Q12.** Si je te fournis un plan sans annotations, peux-tu travailler ?
- [ ] Oui — je peux extraire la géométrie
- [ ] Non — je ne peux pas interpréter la géométrie sans annotations
- [ ] Partiellement — je peux extraire certains éléments mais pas tous

---

## SECTION 5 — VÉRIFICATION DES LIVRABILES

**Q13.** À quel moment dois-je vérifier tes livrables ?
- [ ] Après chaque brique
- [ ] Après chaque phase
- [ ] À la fin du projet

**Q14.** Si je dois vérifier, quelle est la méthode la plus fiable ?
- [ ] Je peux afficher les livrables et vérifier visuellement
- [ ] Je peux vérifier les calculs seulement
- [ ] Je ne peux pas vérifier efficacement

**Q15.** Si je découvre une erreur après la validation, comment corriger ?
- [ ] Je peux corriger et re-produire
- [ ] Je ne peux pas corriger — il faut repartir de zéro

---

## SECTION 6 — COMMENTAIRES DU MOE SUR LA SESSION ÉCHOUÉE

**Contexte :** B-20 V2, B-21 V2, B-22 V2 ont été invalidés car l'IA n'avait pas la capacité de visualiser les plans DXF.

**Erreurs commises :**
1. L'IA a produit des livrables basés sur une interprétation géométrique non vérifiée.
2. L'IA n'a pas communiqué son incapacité à visualiser les plans.
3. Les erreurs se sont propagées : B-20 V2 → B-21 V2 → B-22 V2.
4. Le user a passé 2 jours à corriger des erreurs qui n'auraient jamais eu lieu.

**Leçons :**
1. Toujours demander les capacités de l'IA en début de session.
2. Ne jamais produire un livrable sans s'assurer que la géométrie est correcte.
3. Communiquer explicitement les incertitudes.
4. Arrêter immédiatement si l'IA ne peut pas travailler correctement.

---

## UTILISATION

**Pour la prochaine session :**

1. **Posez ces 15 questions à l'IA** en début de session.
2. **Documentez les réponses** dans un journal de session.
3. **Ne commencez pas le travail** si les réponses ne sont pas satisfaisantes.
4. **Vérifiez après chaque livrable** — ne pas attendre la fin.

**Si l'IA ne peut pas visualiser :**
- Fournissez des informations géométriques explicites (tableaux, croquis, coordonnées).
- Ne fournissez pas seulement des fichiers DXF sans annotations.
- Demandez à l'IA de produire des livrables avec des notes d'incertitude.

---

**Document créé suite à l'échec de visualisation géométrique — Phase 3, B-20/B-21/B-22.**
**Usage :** À intégrer dans le carnet CARNAC ou le mode d'emploi de la prochaine session.
