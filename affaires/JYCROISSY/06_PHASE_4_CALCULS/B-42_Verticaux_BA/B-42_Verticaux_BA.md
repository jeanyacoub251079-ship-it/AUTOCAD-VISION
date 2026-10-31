# B-42 — Verticaux BA (poteaux, jambages, voiles)

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-42 (Phase 4 — Calculs d'exécution)
**Date :** 2026-10-31
**Mode :** PARAMÉTRIQUE documentaire (spécification du script — OUT-01 absent)
**Élément :** poteau (P1, P2, P3)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-02 FDC | ✅ lue | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03 | Béton manquant (H-03), charges connues |
| B-20 Conception GO | ✅ lue | P1/P2/P3 poteaux BA | Poteaux neufs — sections prédimensionnées |
| B-21 DDC préliminaire | ✅ lue | Appuis P1-P3 | Charges aux appuis |
| B-22 Note d'hypothèses | ✅ lue | H-01, H-03, H-05 | Sections, f_cd, charges |
| B-40 Fondations superficielles | ✅ lue | Semelles SI1-SI3 | Géométrie des semelles |

**Aucune donnée déclarée « absente » sans cette preuve.** La classe de béton (MAT-01) est manquante (H-03 à confirmer — R-08) → mode PARAMÉTRIQUE. L'environnement d'exécution (OUT-01) est absent → PARAMÉTRIQUE documentaire (spécification du script, sans livrable).

---

## ÉTAPE 1 — HYPOTHÈSES ET DONNÉES D'ENTRÉE

| Code | Valeur | Source | Statut |
|---|---|---|---|
| MAT-01 (classe béton) | f_cd = f_ck / γ_C (f_ck symbole) | H-03 — R-08 | ❌ À CONFIRMER |
| MAT-02 (exposition) | XC2 supposé | H-03 — R-08 | À CONFIRMER |
| MAT-03 (enrobage) | c_nom = c_min + Δc_dev (à calculer) | EC2 §4.4 | À calculer |
| MAT-04 (acier BA) | S500 (à confirmer) | H-03 — R-08 | À CONFIRMER |
| SEC-01 (feu) | 60 min (à confirmer) | R-14 | À CONFIRMER |
| CHG-01 à CHG-03 | Charges permanentes, d'exploitation, climatiques | B-02 | ✅ Disponibles |
| NIV-02, NIV-03 | Niveaux de plancher, hauteurs libres | B-02 | ✅ Disponibles |
| GEO-02, GEO-04, GEO-05 | Axes, positions des verticaux, baies | B-02 | ✅ Disponibles |

---

## ÉTAPE 2 — DÉSCENTE DE CHARGES AUX PIEDS DES VERTICAUX (DDC EXÉCUTION)

| Vertical | A_inf (m²) | N_ELS (kN) | N_ELU (kN) | H (kN) | M au pied (kNm) |
|---|---|---|---|---|---|
| P1 (poteau, axe B/1) | 13,5 | 149,4 | 205,5 | 0 | 0 |
| P2 (poteau, axe B/2) | 27,0 | 297,9 | 409,6 | 0 | 0 |
| P3 (poteau, axe B/3) | 13,5 | 128,0 | 179,5 | 0 | 0 |

**Justification :** DDC d'exécution distincte de B-21 (pas de forfait 1,15 systématique — coefficients de continuité réels issus du schéma statique).

---

## ÉTAPE 3 — DIMENSIONNEMENT EC2 — COMPRESSION ET FLAMBMENT (FORMULES LITTERALES)

### Élancement : λ = l₀/i, avec i = h/√12 (rectangulaire) et l₀ = k·L

- i = h/√12 (h = section du poteau — symbole).
- l₀ = k·L (k à justifier selon les liaisons — symbole).
- λ = l₀/i (symbole).

### Élancement limite : λ_lim = 20·A·B·C/√n (EC2 §5.8.3.1)

- λ_lim = 20·A·B·C/√n (A, B, C, n selon EC2 §5.8.3.1 — valeurs à calculer).

### Si λ ≤ λ_lim : effets du second ordre négligeables.

### Si λ > λ_lim : second ordre par la méthode de la courbure nominale (EC2 §5.8.8)

- e₂ = (1/r)·l₀²/c, avec 1/r = K_r·K_φ·(1/r₀) (symbole).

### Excentricités

- e₀ = max(h/30 ; 20 mm) (EC2 §6.1(4)).
- e_i = l₀/400 (EC2 §5.8.3.2).
- M_Ed = N_Ed·(e₀ + e_i + e₂) (symbole).

**Aucun dimensionnement retenu — toutes les formules sont en symbole.**

---

## ÉTAPE 4 — VERIFICATION DE LA CAPACITÉ PORTANTE (FORMULES LITTERALES)

### Diagramme d'interaction N-M par bloc rectangulaire (EC2 §6.1)

- M_Rd calculé à N_Ed donné (symbole).
- Taux de travail = M_Ed/M_Rd (symbole).

### Flexion biaxiale (EC2 §5.8.9)

- (M_Ed,z/M_Rd,z)^a + (M_Ed,y/M_Rd,y)^a ≤ 1, exposant a interpolé (symbole).

**Aucun vertical validé — tous les taux de travail sont en symbole.**

---

## ÉTAPE 5 — FERRAILLAGE EC2 (FORMULES LITTERALES)

### A_s,min = max(0,10·N_Ed/f_yd ; 0,002·A_c) (EC2 §9.5.2)

- A_s,min = max(0,10·N_Ed/f_yd ; 0,002·A_c) (symbole).

### A_s,max = 0,04·A_c (EC2 §9.5.2)

- A_s,max = 0,04·A_c (symbole).

### Cadres (poteaux, EC2 §9.5.3)

- Ø ≥ max(6 mm ; Ø_l,max/4), espacement ≤ min(20·Ø_l,min ; plus petite dimension ; 400 mm) (symbole).

**Aucun ferraillage retenu — toutes les formules sont en symbole.**

---

## ÉTAPE 6 — DISPOSITIONS CONSTRUCTIVES (BLOC A — POTEAU)

- Cadres HA6 avec espacement réduit aux extrémités (zone critique) et aux recouvrements.
- Recouvrement des barres longitudinales (EC2 §8.7) : longueur l_0 = α·l_b,rqd, justifiée.
- Attentes vers le bas : effort transmis à B-50.
- Enrobage c_nom (MAT-03) satisfaisant à la fois la durabilité et SEC-01.
- Si le poteau reçoit un profilé métallique ou une platine, réservations prévues.

---

## ÉTAPE 7 — EFFORTS À ANCRER (TRANSMIS À B-50)

| Vertical | N_Ed au pied (kN) | M_Ed au pied (kNm) | Section des barres | Nombre et diamètre | Dépassement |
|---|---|---|---|---|---|
| P1 | 205,5 | 0 | symbole | symbole | symbole |
| P2 | 409,6 | 0 | symbole | symbole | symbole |
| P3 | 179,5 | 0 | symbole | symbole | symbole |

**Aucune longueur d'ancrage calculée — c'est B-50.**

---

## ÉTAPE 8 — VERIFICATION DU LOGEMENT DES ATTENTES (SANS LES CALCULER)

La section du poteau permet de loger les barres avec l'enrobage et l'espacement requis — vérification à faire après B-50.

---

## ÉTAPE 9 — LIVRABILES GRAPHIQUES (SPÉCIFICATION DU SCRIPT — NON PRODUITS)

| Calque | Contenu | Statut |
|---|---|---|
| VERT-AXES | Axes, trames, points de calage | Non produit (OUT-01 absent) |
| VERT-COFFRAGE | Sections, cotations, positions | Non produit (OUT-01 absent) |
| VERT-ACIER-LONG | Barres longitudinales, sections, recouvrements | Non produit (OUT-01 absent) |
| VERT-ACIER-TRANS | Cadres, armatures réparties | Non produit (OUT-01 absent) |
| VERT-HABILLAGE-TEXTE | Légendes, cartouche, notes, tableaux de ferraillage | Non produit (OUT-01 absent) |

**Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA »** (à produire quand OUT-01 est disponible).

---

## ÉTAPE 10 — AUTO-CONTRÔLE DÉCLARÉ

| Point | Statut |
|---|---|
| Chaque vertical a sa DDC d'exécution | ✅ §Étape 2 (3 verticaux) |
| Chaque vertical a son dimensionnement EC2 | ❌ À calculer (classe béton manquante — formules littérales) |
| Chaque vertical a son ferraillage | ❌ À calculer (classe béton manquante — formules littérales) |
| Enrobage compatible avec SEC-01 et MAT-02 | ❌ À calculer (SEC-01 manquante — R-14) |
| Efforts à ancrer transmis à B-50 | ✅ §Étape 7 (efforts fournis — symbole) |
| Logement des attentes vérifié avec B-40 | ❌ À vérifier (logement non vérifié) |

**DE PRINCIPE :**
- Classe de béton manquante (H-03 à confirmer — R-08).
- Exposition XC2 supposé (H-03 à confirmer — R-08).
- Acier BA S500 supposé (H-03 à confirmer — R-08).
- Coupe-feu 60 min supposé (R-14 à confirmer).

**À LEVER :**
- Classe de béton (MAT-01) — R-08.
- Exposition (MAT-02) — H-03.
- Enrobage (MAT-03) — à calculer.
- Acier BA (MAT-04) — H-03.
- Coupe-feu (SEC-01) — R-14.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque donnée d'entrée est issue de la FDC (aucune valeur hors FDC) | ✅ §Étape 1 (charges CHG-01 à CHG-03 — B-02) |
| La DDC d'exécution est établie (distincte de B-21) | ✅ §Étape 2 (coefficients de continuité réels) |
| Chaque vertical satisfait flambement, second ordre, N-M, biaxial | ❌ À calculer (classe béton manquante — formules littérales) |
| Chaque ferraillage satisfait EC2 §9.5.2 | ❌ À calculer (classe béton manquante — formules littérales) |
| Enrobage compatible avec SEC-01 et MAT-02 | ❌ À calculer (SEC-01 manquante — R-14) |
| Efforts à ancrer transmis à B-50 | ✅ §Étape 7 (efforts fournis — symbole) |
| Logement des attentes vérifié avec B-40 | ❌ À vérifier (logement non vérifié) |

**Écart signalé :** B-42 est en mode PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-01 manquante). Aucune valeur n'est retenue. Le calcul est suspendu jusqu'à obtention de la classe de béton (H-03) et de l'environnement d'exécution (OUT-01).

---

**Brique B-42 exécutée en mode PARAMÉTRIQUE documentaire — en attente de votre GO ou de nouvelles observations.**
La classe de béton (MAT-01) est manquante (H-03 à confirmer — R-08). **Aucune section, aucun ferraillage, aucune valeur n'est retenu.** Le calcul est **SUSPENDU** jusqu'à obtention de la classe de béton et de l'environnement d'exécution (OUT-01). Les plans d'exécution (VERT-*) ne sont pas produits (OUT-01 absent).
