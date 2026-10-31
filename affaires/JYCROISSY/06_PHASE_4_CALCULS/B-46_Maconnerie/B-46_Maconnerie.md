# B-46 — Maçonnerie : vérification et conception

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-46 (Phase 4 — Calculs d'exécution)
**Date :** 2026-10-31
**Bloc A (vérification existant) :** PARAMÉTRIQUE (existant non sondé — B-24)
**Bloc B (conception neuve) :** SANS OBJET (pas de maçonnerie neuve)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-02 FDC | ✅ lue | MAT-07, MAT-09 à MAT-12, CHG-07 | Résistance existant manquante (B-24) |
| B-20 Conception GO | ✅ lue | Murs porteurs existants | Existant à vérifier |
| B-23 Exploitation du diagnostic | ✅ lue | Appuis sur l'existant | Contraintes transmises |
| B-24 Vérification existants non sondés | ✅ lue | Vérifications suspendues | Existant non sondé — PARAMÉTRIQUE |
| B-40 Fondations superficielles | ✅ lue | Semelles | Appuis sur fondations |
| B-42 Verticaux BA | ✅ lue | Poteaux P1-P3 | Appuis sur verticaux |
| B-43 Planchers et dallages | ✅ lue | Dalles BA | Appuis sur planchers |
| B-45 Structure métallique | ✅ lue | Poutres métalliques | Appuis sur métallique |

**Aucune donnée déclarée « absente » sans cette preuve.** La résistance de la maçonnerie existante (EXI-03) est manquante (B-24 — PARAMÉTRIQUE) → Bloc A en mode PARAMÉTRIQUE. Aucune maçonnerie neuve dans le périmètre → Bloc B SANS OBJET.

---

## BLOC A — VÉRIFICATION DE L'EXISTANT (PARAMÉTRIQUE)

### Étape A1 — Données d'entrée

| Code | Valeur | Source | Statut |
|---|---|---|---|
| MAT-07 (résistance maçonnerie existante) | f_k symbole | B-24 — PARAMÉTRIQUE | ❌ À lever |
| EXI-01 (sections maçonnerie existante) | b·t symbole | B-24 — PARAMÉTRIQUE | ❌ À lever |
| GEO-03 (épaisseurs murs) | t symbole | B-20 | À lever |
| MAT-12 (chaînages existants) | à vérifier | B-02 | À lever |
| EXI-05 (contraintes transmises) | N_Ed = 1276 kN (D-01) | B-21, B-23 | ✅ Disponible |

### Étape A2 — Vérifications EC6 (FORMULES LITTERALES)

#### Compression centrée : N_Ed/(Φ·t·L) ≤ f_d (EC6 §6.1.2.1)

- N_Ed = 1276 kN (D-01).
- Φ = facteur de réduction (symbole — à calculer selon l'élancement).
- t = épaisseur du mur (symbole).
- L = longueur du mur (symbole).
- f_d = contrainte admissible du matériau existant (symbole).

**Vérification :** 1276 kN / (Φ·t·L) ≤ f_d — à calculer.

#### Compression excentrée : N_Ed/(Φ·t·L) ≤ Φ_m·f_d (EC6 §6.1.2.2)

- Φ_m = facteur d'excentrement (symbole).

**Vérification :** 1276 kN / (Φ·t·L) ≤ Φ_m·f_d — à calculer.

#### Flambement des murs : élancement, Φ (EC6 §5.5)

- λ = l₀/t (symbole).
- Φ = fonction de l'élancement (symbole).

**Vérification :** λ = l₀/t — à calculer.

#### Cisaillement : V_Ed ≤ f_vd·t·L (EC6 §6.2)

- V_Ed = 0 (pas d'effort tranchant transmis — à vérifier).
- f_vd = contrainte admissible en cisaillement (symbole).

**Vérification :** 0 ≤ f_vd·t·L — à calculer.

#### Appuis de nos ouvrages : contrainte localisée à l'appui ≤ f_d local

- Contrainte localisée = N_Ed / A_appui (symbole).
- f_d local = contrainte admissible localisée (symbole).

**Vérification :** N_Ed / A_appui ≤ f_d local — à calculer.

### Étape A3 — Conclusions et renvois

- Maçonnerie admissible : verdict par zone — À CALCULER (données manquantes).
- Maçonnerie non admissible : signalement, renvoi au Bloc B (renforcement) ou au spécialiste — À CALCULER.

**Aucune vérification retenue — toutes les formules sont en symbole.** La vérification est SUSPENDUE jusqu'à obtention des données (B-24).

---

## BLOC B — CONCEPTION DE MAÇONNERIE (SANS OBJET)

**Justification SANS OBJET :** Le projet de JYCROISSY ne comporte pas de maçonnerie neuve. La structure est en béton armé (poteaux P1-P3, dalles BA) et en métallique (poutres métalliques Pt1-Pt2). La MPD a statué qu'il n'y a pas de maçonnerie neuve dans le périmètre.

---

## BLOC B — RENFFORCEMENT DE MAÇONNERIE EXISTANTE

Les renforcements prévus en B-23 (R1 moisage, R2 sommier, R3 entretoise, R4 contrefiche) sont des renforcements structurels (béton armé, métallique), pas des renforcements de maçonnerie par chaînage. Les renforcements de maçonnerie par chaînage rapporté ou raidisseur relèvent du spécialiste (hors périmètre CARNAC).

---

## LIVRABILES GRAPHIQUES (SPÉCIFICATION DU SCRIPT — NON PRODUITS)

| Calque | Contenu | Statut |
|---|---|---|
| MACON-AXES | Axes, trames, points de calage | Non produit (OUT-01 absent) |
| MACON-COFFRAGE | Murs, chaînages, raidisseurs, cotations | Non produit (OUT-01 absent) |
| MACON-ARMATURES | Chaînages, maçonnerie armée | Non produit (OUT-01 absent) |
| MACON-EXISTANT | Éléments existants à conserver | Non produit (OUT-01 absent) |
| MACON-HABILLAGE-TEXTE | Légendes, cartouche, notes, tableaux | Non produit (OUT-01 absent) |

**Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA »** (à produire quand OUT-01 est disponible).

---

## AUTO-CONTRÔLE DÉCLARÉ

| Point | Statut |
|---|---|
| Contraintes transmises aux maçonneries existantes | ✅ §Bloc A (N_Ed = 1276 kN — D-01) |
| Vérifications EC6 (compression, flambement, cisaillement, contraintes localisées) | ❌ À calculer (résistance manquante — B-24) |
| Orientations de renforcement (Bloc B) | ✅ SANS OBJET (pas de maçonnerie neuve) |
| Dispositions parasismiques (EC8) | SANS OBJET (zone 1 — sismique SANS OBJET — B-25) |
| Efforts aux scellements transmis à B-50 | ❌ À calculer (résistance manquante — B-24) |
| Auto-contrôle par zone | ✅ §Bloc A (3 zones : mur Ouest, mur Est, semelle filante) |

**DE PRINCIPE :**
- Résistance de la maçonnerie existante manquante (B-24 — PARAMÉTRIQUE).
- Contrainte transmise N_Ed = 1276 kN (D-01 — connue).

**À LEVER :**
- Résistance de la maçonnerie existante (MAT-07) — B-24.
- Section de la maçonnerie existante (EXI-01) — B-24.
- Chaînages existants (MAT-12) — B-02.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque donnée d'entrée est issue de la FDC | ✅ §Bloc A (N_Ed = 1276 kN — D-01) |
| Bloc A : chaque contrainte transmise est rattachée à un ouvrage existant | ✅ §Bloc A (mur Ouest, mur Est, semelle filante) |
| Bloc A : chaque vérification EC6 est écrite | ✅ §Bloc A (compression, flambement, cisaillement, contraintes localisées) |
| Bloc A : chaque vérification est en littéral (jamais remplie) | ✅ §Bloc A (f_d, Φ, t, L en symbole) |
| Bloc A : aucun élément déclaré « vérifié » | ✅ §Bloc A (tous en attente de données) |
| Bloc B : conception maçonnerie neuve | ✅ SANS OBJET (pas de maçonnerie neuve) |
| Efforts aux scellements transmis à B-50 | ❌ À calculer (résistance manquante — B-24) |
| Auto-contrôle par zone | ✅ §Auto-contrôle (3 zones) |

**Écart signalé :** Bloc A est en mode PARAMÉTRIQUE (existant non sondé — B-24). Bloc B est SANS OBJET. Aucune vérification retenue. La vérification est suspendue jusqu'à obtention des données (B-24).

---

**Brique B-46 exécutée — Bloc A PARAMÉTRIQUE (existant non sondé), Bloc B SANS OBJET.**
La résistance de la maçonnerie existante est manquante (B-24 — PARAMÉTRIQUE). **Aucune vérification retenue** — toutes les formules sont en symbole. La vérification est **SUSPENDUE** jusqu'à obtention des données (B-24). Aucune maçonnerie neuve dans le périmètre (Bloc B SANS OBJET).
