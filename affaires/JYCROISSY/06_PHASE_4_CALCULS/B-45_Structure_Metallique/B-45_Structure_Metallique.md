# B-45 — Structure métallique

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-45 (Phase 4 — Calculs d'exécution)
**Date :** 2026-10-31
**Mode :** PARAMÉTRIQUE documentaire (spécification du script — OUT-01 absent)
**Élément :** poutre métallique (Pt1, Pt2)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-02 FDC | ✅ lue | MAT-05, CHG-01 à CHG-03, CHG-06 | Nuance d'acier manquante (H-03), charges connues |
| B-20 Conception GO | ✅ lue | Pt1/Pt2 poutres métalliques | Poutres métalliques neuves — sections prédimensionnées |
| B-21 DDC préliminaire | ✅ lue | Charges par zone | Charges connues |
| B-22 Note d'hypothèses | ✅ lue | H-02 (poutres h≈500 mm), H-03 (f_cd) | Sections, nuance |
| B-40 Fondations superficielles | ✅ lue | Semelles | Appuis sur fondations |
| B-42 Verticaux BA | ✅ lue | Poteaux P1-P3 | Appuis sur verticaux |
| B-43 Planchers et dallages | ✅ lue | Dalles BA | Appuis sur planchers |

**Aucune donnée déclarée « absente » sans cette preuve.** La nuance d'acier (MAT-05) est manquante (À CONFIRMER — H-03) → mode PARAMÉTRIQUE. L'environnement d'exécution (OUT-01) est absent → PARAMÉTRIQUE documentaire (spécification du script, sans livrable).

---

## ÉTAPE 1 — HYPOTHÈSES ET DONNÉES D'ENTRÉE

| Code | Valeur | Source | Statut |
|---|---|---|---|
| MAT-05 (nuance acier) | f_y, f_u, γ_M0, γ_M1, γ_M2 (symbole) | H-03 — R-08 | ❌ À CONFIRMER |
| CHG-01 à CHG-03 | Charges permanentes, d'exploitation, climatiques | B-02 | ✅ Disponibles |
| CHG-06 | Vent (zone, v_b, catégorie de terrain) | B-02 | ✅ Disponibles |
| GEO-02, GEO-04 | Axes et positions des porteurs | B-02 | ✅ Disponibles |
| H-02 | Section poutres métalliques h≈500 mm (ENVELOPPE) | B-20 | À CONFIRMER |

---

## ÉTAPE 2 — DÉSCENTE DE CHARGES (PAR PROFILÉ)

| Profilé | w_ELS (kN/m) | w_ELU (kN/m) | N_Ed (kN) | V_Ed (kN) | M_Ed (kNm) |
|---|---|---|---|---|---|
| Pt1 (poutre métallique, axe A/1-2) | symbole | symbole | symbole | symbole | symbole |
| Pt2 (poutre métallique, axe A/2-3) | symbole | symbole | symbole | symbole | symbole |

**Justification :** DDC d'exécution distincte de B-21 (pas de forfait 1,15 systématique — coefficients de continuité réels issus du schéma statique).

---

## ÉTAPE 3 — CLASSIFICATION DE SECTION (EC3 §5.5)

Pour chaque profilé : classe 1, 2, 3 ou 4 selon les rapports c/t et la sollicitation. La classe détermine la résistance utilisable (plastique pour 1 et 2, élastique pour 3, efficace pour 4).

**Classification à calculer — section en symbole (h≈500 mm — H-02, à confirmer).**

---

## ÉTAPE 4 — VÉRIFICATIONS EC3 (FORMULES LITTERALES)

### Flexion

- M_Ed ≤ M_c,Rd = W_pl·f_y/γ_M0 (classe 1/2) ou W_el·f_y/γ_M0 (classe 3) — symbole.

### Cisaillement

- V_Ed ≤ V_pl,Rd = A_v·f_y/(√3·γ_M0) — symbole.

### Interaction M-V (EC3 §6.2.8) si V_Ed > 0,5·V_pl,Rd

- (M_Ed/M_pl,Rd)^a + (V_Ed/V_pl,Rd)^b ≤ 1 — symbole.

### Flambement (EC3 §6.3.1) pour les éléments comprimés

- λ̄, courbe, χ, N_b,Rd = χ·A·f_y/γ_M1 — symbole.

### Déversement (EC3 §6.3.2) si la semelle comprimée n'est pas maintenue

- λ̄_LT, χ_LT, M_b,Rd = χ_LT·W_y·f_y/γ_M0 — symbole.

### Flèche ELS

- δ ≤ L/250 ou L/300 (à justifier) — symbole.

**Aucune vérification retenue — toutes les formules sont en symbole.**

---

## ÉTAPE 5 — DISPOSITIONS CONSTRUCTIVES

- Maintien latéral des semelles comprimées (entretoises, plancher collaborant, solives) : condition du déversement.
- Entretoises anti-déversement si nécessaire (efforts fournis à B-50).
- Protection anticorrosion (galvanisation à chaud NF EN ISO 1461, peinture).
- Réservations et trémies : positions compatibles avec les semelles.
- Appuis : vérification de la pression diamétrale sur le béton (EC2 §6.7) — effort transmis à B-50.

---

## ÉTAPE 6 — EFFORTS AUX ASSEMBLAGES (TRANSMIS À B-50)

| Nœud / appui | N_Ed (kN) | V_Ed (kN) | M_Ed (kNm) | Nature de l'assemblage |
|---|---|---|---|---|
| Pt1 — appui sur poteau P1 | symbole | symbole | symbole | symbole |
| Pt2 — appui sur poteau P2 | symbole | symbole | symbole | symbole |
| Pt1 — assemblage intermédiaire | symbole | symbole | symbole | symbole |
| Pt2 — assemblage intermédiaire | symbole | symbole | symbole | symbole |

**Aucun assemblage calculé — c'est B-50.**

---

## ÉTAPE 7 — LIVRABILES GRAPHIQUES (SPÉCIFICATION DU SCRIPT — NON PRODUITS)

| Calque | Contenu | Statut |
|---|---|---|
| METAL-AXES | Axes, trames, points de calage | Non produit (OUT-01 absent) |
| METAL-COFFRAGE | Sections, positions, portées, réservations | Non produit (OUT-01 absent) |
| METAL-PROFILES | Désignation des profilés, positions, repères | Non produit (OUT-01 absent) |
| METAL-HABILLAGE-TEXTE | Légendes, cartouche, notes, tableaux | Non produit (OUT-01 absent) |

**Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA »** (à produire quand OUT-01 est disponible).

---

## ÉTAPE 8 — AUTO-CONTRÔLE DÉCLARÉ

| Point | Statut |
|---|---|
| Chaque profilé a sa classification EC3 §5.5 | ❌ À calculer (nuance manquante — H-03) |
| Chaque profilé satisfait flexion, cisaillement, interaction M-V, flambement, déversement, flèche | ❌ À calculer (nuance manquante — formules littérales) |
| Maintien latéral justifié (condition du déversement) | ❌ À justifier (section manquante — H-02) |
| Chaque nœud et appui a ses efforts transmis à B-50 | ✅ §Étape 6 (efforts fournis — symbole) |
| Pression diamétrale sur le béton (EC2 §6.7) | ❌ À vérifier (nuance manquante — H-03) |
| Plans portent filigrane, indice, mode, mention générique de protection au feu | ❌ À vérifier (plans non produits — OUT-01 absent) |

**DE PRINCIPE :**
- Nuance d'acier manquante (H-03 à confirmer — R-08).
- Section poutres métalliques h≈500 mm (H-02 à confirmer).

**À LEVER :**
- Nuance d'acier (MAT-05) — H-03.
- Section poutres métalliques (H-02).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque donnée d'entrée est issue de la FDC | ✅ §Étape 1 (charges CHG-01 à CHG-03, CHG-06 — B-02) |
| Chaque profilé a sa classification EC3 §5.5 | ❌ À calculer (nuance manquante — H-03) |
| Chaque profilé satisfait flexion, cisaillement, interaction M-V, flambement, déversement, flèche | ❌ À calculer (nuance manquante — formules littérales) |
| Maintien latéral justifié (condition du déversement) | ❌ À justifier (section manquante — H-02) |
| Chaque nœud et appui a ses efforts transmis à B-50 | ✅ §Étape 6 (efforts fournis — symbole) |
| Plans portent filigrane, indice, mode, mention générique de protection au feu | ❌ À vérifier (plans non produits — OUT-01 absent) |
| Auto-contrôle déclare chaque profilé | ✅ §Étape 8 (2 profilés) |

**Écart signalé :** B-45 est en mode PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-05 manquante). Aucune valeur n'est retenue. Le calcul est suspendu jusqu'à obtention de la nuance d'acier (H-03) et de l'environnement d'exécution (OUT-01).

---

**Brique B-45 exécutée en mode PARAMÉTRIQUE documentaire — en attente de votre GO ou de nouvelles observations.**
La nuance d'acier (MAT-05) est manquante (H-03 à confirmer — R-08). **Aucune classification, aucune vérification, aucune valeur n'est retenu.** Le calcul est **SUSPENDU** jusqu'à obtention de la nuance d'acier et de l'environnement d'exécution (OUT-01). Les plans d'exécution (METAL-*) ne sont pas produits (OUT-01 absent).
