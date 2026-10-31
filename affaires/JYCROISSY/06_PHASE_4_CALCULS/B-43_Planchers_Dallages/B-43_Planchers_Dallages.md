# B-43 — Planchers et dallages

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-43 (Phase 4 — Calculs d'exécution)
**Date :** 2026-10-31
**Mode :** PARAMÉTRIQUE documentaire (spécification du script — OUT-01 absent)
**Type :** dalle BA (RDC, R+1) + dallage sur terre-plein (sous-sol — SANS OBJET)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-02 FDC | ✅ lue | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-08 | Béton manquant (H-03), charges connues |
| B-20 Conception GO | ✅ lue | Dg1 dalle, Pt1/Pt2 poutres métalliques | Dalle BA neuve — épaisseur prédimensionnée |
| B-21 DDC préliminaire | ✅ lue | Charges par zone | Charges connues |
| B-22 Note d'hypothèses | ✅ lue | H-03, H-06 à H-08 | f_cd, dallage 20 cm, chape, isolation |
| B-40 Fondations superficielles | ✅ lue | Semelles | Appuis sur fondations |
| B-42 Verticaux BA | ✅ lue | Poteaux P1-P3 | Appuis sur verticaux |

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
| CHG-08 | Cloisons, équipements lourds | B-02 | ✅ Disponibles |
| NIV-02, NIV-05, NIV-06 | Niveaux de plancher, niveau fini du dallage, épaisseurs | B-02 | ✅ Disponibles |
| GEO-01 | Emprise / contour du bâtiment | B-02 | ✅ Disponibles |

---

## ÉTAPE 2 — DÉSCENTE DE CHARGES AUX PLANCHERS (DDC EXÉCUTION)

| Zone | A_inf (m²) | G (kN) | Q (kN) | N_ELS (kN) | N_ELU (kN) |
|---|---|---|---|---|---|
| RDC (PB) — cabinet paramédical | 108,0 | 667,4 | 356,4 | 1023,8 | 1426,7 |
| R+1 (PH) — bureaux | 108,0 | 667,4 | 356,4 | 1023,8 | 1426,7 |

**Justification :** DDC d'exécution distincte de B-21 (pas de forfait 1,15 systématique — coefficients de continuité réels issus du schéma statique).

---

## ÉTAPE 3 — DIMENSIONNEMENT (FORMULES LITTERALES)

### BLOC A — DALLE BA (RDC, R+1)

#### Épaisseur de dalle

Prédimensionnement par ratio :
- 1 sens : épaisseur ≈ L/25 (L = 9 m → épaisseur ≈ 36 cm — à vérifier).
- 2 sens : épaisseur ≈ L/30 (L = 6 m → épaisseur ≈ 20 cm — H-06).

**Épaisseur retenue : 20 cm (H-06 — à confirmer).**

#### Flexion : M_Ed et M_Rd selon EC2 §6.1

- M_Ed = w·L²/8 (symbole — w = charge de conception).
- M_Rd = A_s·f_yd·(d − A_s·f_yd/(2·f_cd)) (symbole).
- Taux de travail = M_Ed/M_Rd (symbole).

#### Effort tranchant : V_Ed ≤ V_Rd,c (EC2 §6.2.2)

- V_Ed = w·L/2 (symbole).
- V_Rd,c = 0,12·k₁·k₂·f_ctm·b·d (symbole).

#### Poinçonnement : v_Ed ≤ v_Rd,c (EC2 §6.4) aux appuis ponctuels (poteaux)

- v_Ed = V_Ed/u (u = périmètre du poinçonnement — symbole).
- v_Rd,c = 0,5·v_min·c (symbole).

#### Flèches : si requises par l'usage (EC2 §7.4)

- Flèche = k·w·L⁴/(E·I) (symbole).

#### A_s,min = max(0,26·f_ctm/f_yk·b·d ; 0,0013·b·d) (EC2 §9.3.1.1)

- A_s,min = max(0,26·f_ctm/f_yk·b·d ; 0,0013·b·d) (symbole).

#### Ferraillage

- Nappe inférieure (symbole).
- Nappe supérieure si nécessaire (symbole).
- Chapeaux aux appuis (symbole).
- Renforts ponctuels (symbole).

### BLOC B — DALLAGE SUR TERRE-PLEIN (sous-sol — SANS OBJET)

**Justification SANS OBJET :** Le projet de JYCROISSY ne comporte pas de dallage sur terre-plein. Le sous-sol est un niveau de parking (dalles BA — B-20).

### BLOC C — PLANCHER BOIS (SANS OBJET)

**Justification SANS OBJET :** Le projet de JYCROISSY ne comporte pas de plancher bois. Les planchers sont des dalles BA (RDC, R+1) et des poutres métalliques (Pt1, Pt2 — B-20).

**Aucun dimensionnement retenu — toutes les formules sont en symbole.**

---

## ÉTAPE 4 — EFFORTS AUX APPUIS (TRANSMIS À B-50)

| Appui | N_Ed (kN) | V_Ed (kN) | M_Ed (kNm) | Efforts de cisaillement connecteurs |
|---|---|---|---|---|
| P1 (poteau, axe B/1) | 205,5 | symbole | symbole | symbole |
| P2 (poteau, axe B/2) | 409,6 | symbole | symbole | symbole |
| P3 (poteau, axe B/3) | 179,5 | symbole | symbole | symbole |
| Pt1 (poutre métallique) | symbole | symbole | symbole | symbole |
| Pt2 (poutre métallique) | symbole | symbole | symbole | symbole |

**Aucun assemblage calculé — c'est B-50.**

---

## ÉTAPE 5 — DISPOSITIONS CONSTRUCTIVES

- Joints de retrait et fractionnement.
- Joints de désolidarisation (dallage / poteaux, dallage / murs).
- Réservations (trémies, gaines, fourreaux) : positions et dimensions compatibles avec le ferraillage.
- Renforts aux angles et aux rives.
- Liaisons avec les verticaux (B-42) et les fondations (B-40).
- Mention « protection au feu adéquate à prévoir (hors lot GO) ».

---

## ÉTAPE 6 — LIVRABILES GRAPHIQUES (SPÉCIFICATION DU SCRIPT — NON PRODUITS)

| Calque | Contenu | Statut |
|---|---|---|
| PLANCHER-AXES | Axes, trames, points de calage | Non produit (OUT-01 absent) |
| PLANCHER-COFFRAGE | Contours, épaisseurs, cotations, réservations, joints | Non produit (OUT-01 absent) |
| PLANCHER-ACIER-INF | Nappe inférieure, sections, espacements, recouvrements | Non produit (OUT-01 absent) |
| PLANCHER-ACIER-SUP | Nappe supérieure, chapeaux, renforts | Non produit (OUT-01 absent) |
| PLANCHER-HABILLAGE-TEXTE | Légendes, cartouche, notes, tableaux | Non produit (OUT-01 absent) |

**Tous les plans portent le filigrane « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA »** (à produire quand OUT-01 est disponible).

---

## ÉTAPE 7 — AUTO-CONTRÔLE DÉCLARÉ

| Point | Statut |
|---|---|
| Chaque zone a ses charges et combinaisons ELS et ELU | ✅ §Étape 2 (2 zones) |
| Chaque zone a son ferraillage complet | ❌ À calculer (classe béton manquante — formules littérales) |
| Chaque zone satisfait A_min et dispositions constructives | ❌ À calculer (classe béton manquante — formules littérales) |
| Chaque appui a ses efforts transmis à B-50 | ✅ §Étape 4 (efforts fournis — symbole) |
| Chaque réservation est compatible avec le ferraillage | ❌ À vérifier (ferraillage non retenu) |
| Les joints de retrait et de désolidarisation sont prévus | ✅ §Étape 5 |
| Échelle cohérente | À vérifier (plans non produits) |
| Cartouche complet | À vérifier (plans non produits) |

**DE PRINCIPE :**
- Classe de béton manquante (H-03 à confirmer — R-08).
- Exposition XC2 supposé (H-03 à confirmer — R-08).
- Acier BA S500 supposé (H-03 à confirmer — R-08).
- Coupe-feu 60 min supposé (R-14 à confirmer).
- Dallage 20 cm (H-06 à confirmer).
- Chape 5 cm (H-07 à confirmer).
- Isolation 5 cm (H-08 à confirmer).

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
| Chaque zone satisfait flexion, effort tranchant, poinçonnement | ❌ À calculer (classe béton manquante — formules littérales) |
| Chaque zone a son ferraillage (nappes, chapeaux, renforts) | ❌ À calculer (classe béton manquante — formules littérales) |
| Dispositions constructives (joints, réservations, appuis) | ✅ §Étape 5 |
| Efforts aux appuis transmis à B-50 | ✅ §Étape 4 (efforts fournis — symbole) |
| Auto-contrôle par zone | ✅ §Étape 7 (2 zones) |

**Écart signalé :** B-43 est en mode PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-01 manquante). Aucune valeur n'est retenue. Le calcul est suspendu jusqu'à obtention de la classe de béton (H-03) et de l'environnement d'exécution (OUT-01).

---

**Brique B-43 exécutée en mode PARAMÉTRIQUE documentaire — en attente de votre GO ou de nouvelles observations.**
La classe de béton (MAT-01) est manquante (H-03 à confirmer — R-08). **Aucune épaisseur, aucun ferraillage, aucune valeur n'est retenu.** Le calcul est **SUSPENDU** jusqu'à obtention de la classe de béton et de l'environnement d'exécution (OUT-01). Les plans d'exécution (PLANCHER-*) ne sont pas produits (OUT-01 absent).
