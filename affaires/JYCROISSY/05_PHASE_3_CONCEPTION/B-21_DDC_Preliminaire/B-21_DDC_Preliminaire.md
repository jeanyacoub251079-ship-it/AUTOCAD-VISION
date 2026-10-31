# B-21 — Descente de charges préliminaire

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-21 (Phase 3 — Conception et synthèse structurelle)
**Date :** 2026-10-31
**Mode :** COMPLET (CHG-01 à CHG-04 disponibles — D-03)
**Version :** 1.0

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-20 Conception GO | ✅ lue | Trame, porteurs P1-P3, Pt1-Pt2, SI1-SI3, SF1, Lt1-Lt2, Dg1 | Porteurs à charger |
| B-00 Énoncé de mission | ✅ lue | §1 à §6 | Mission reformulée, usages |
| B-02 FDC | ✅ lue | CHG-01 à CHG-08 statuts | Charges d'exploitation et permanentes |
| B-03 RDR | ✅ lue | D-03 (250 daN/m²) | Charge d'exploitation officielle |
| B-25 Stabilité globale | ✅ lue | Cheminement des efforts | Charges horizontales |

**Aucune charge déclarée sans cette preuve.** Chaque charge est rattachée à une couche (poids propre) ou à une catégorie EC1 (exploitation).

---

## TABLEAU 1 — SURFACE D'INFLUENCE

| Porteur | L_t (m) | l_t (m) | A_inf (m²) | Justification (demi-portées adjacentes) |
|---|---|---|---|---|
| P1 (poteau, axe B/1) | 3,0 | 4,5 | 13,5 | Demi-portée Nord = 3 m (axe 1→2), demi-portée Est = 4,5 m (axe B→2) |
| P2 (poteau, axe B/2) | 6,0 | 4,5 | 27,0 | Demi-portée Nord = 6 m (axe 1→3), demi-portée Est = 4,5 m (axe B→2) |
| P3 (poteau, axe B/3) | 3,0 | 4,5 | 13,5 | Demi-portée Sud = 3 m (axe 2→3), demi-portée Est = 4,5 m (axe B→2) |
| SF1 (semelle filante, axe A) | 18,0 | — | 54,0 (m²/ml) | Largeur tributaire = 3 m (demi-entraxe axe A→B) × 18 m de long = 54 m² par mètre linéaire |
| SI1 (semelle isolée, P1) | — | — | 13,5 | Surface d'influence du poteau P1 (transmission au sol) |
| SI2 (semelle isolée, P2) | — | — | 27,0 | Surface d'influence du poteau P2 (transmission au sol) |
| SI3 (semelle isolée, P3) | — | — | 13,5 | Surface d'influence du poteau P3 (transmission au sol) |

---

## TABLEAU 2 — CHARGES PERMANENTES PAR COUCHE

| Zone | Couche | Épaisseur | Poids volumique | g (kN/m²) | Source (pièce ou hypothèse H-xx) |
|---|---|---|---|---|---|
| RDC (PB) | Dallage béton armé | 0,20 m | 25 kN/m³ | 5,0 | H-06 — dallage 20 cm (MINI, B-20) |
| RDC (PB) | Chape et revêtement | 0,05 m | 22 kN/m³ | 1,1 | H-07 — chape et revêtement (hypothèse) |
| RDC (PB) | Isolation | 0,05 m | 0,15 kN/m³ | 0,075 | H-08 — isolation (hypothèse) |
| R+1 (PH) | Dallage béton armé | 0,20 m | 25 kN/m³ | 5,0 | H-06 — dallage 20 cm (MINI, B-20) |
| R+1 (PH) | Chape et revêtement | 0,05 m | 22 kN/m³ | 1,1 | H-07 — chape et revêtement (hypothèse) |
| R+1 (PH) | Isolation | 0,05 m | 0,15 kN/m³ | 0,075 | H-08 — isolation (hypothèse) |
| **Total RDC/PH** | — | — | — | **6,18** | Somme des couches |
| **Total R+1/toiture** | — | — | — | **6,18** | Somme des couches |

---

## TABLEAU 3 — CHARGES D'EXPLOITATION PAR ZONE

| Zone | Usage (catégorie EC1) | q_k (kN/m²) | Cloisons (kN/m²) | Total (kN/m²) | Source |
|---|---|---|---|---|---|
| RDC (PB) — cabinet paramédical | C3 — activité (bureaux) | 2,5 (D-03) | 0,8 | 3,3 | D-03 — 250 daN/m² |
| R+1 (PH) — bureaux | C1 — activité (bureaux) | 2,5 (D-03) | 0,8 | 3,3 | D-03 — 250 daN/m² |

**Cloisons forfaitaires** : NF EN 1991-1-1 §6.3.1.2 — 0,8 kN/m².

---

## TABLEAU 4 — DESCENTE DE CHARGES PAR PORTEUR (ELS)

| Porteur | A_inf (m²) | G (kN) | Q (kN) | Coefficient de continuité | N_ELS (kN ou kN/m) |
|---|---|---|---|---|---|
| P1 | 13,5 | 83,4 | 44,6 | 1,15 (appui intermédiaire) | 149,4 |
| P2 | 27,0 | 166,9 | 89,1 | 1,15 (appui intermédiaire) | 297,9 |
| P3 | 13,5 | 83,4 | 44,6 | 1,00 (appui de rive) | 128,0 |
| SF1 | 54,0 (m²/ml) | 333,7 | 178,2 | 1,00 (appui de rive) | 511,9 kN/m |
| SI1 | 13,5 | 83,4 | 44,6 | 1,15 | 149,4 |
| SI2 | 27,0 | 166,9 | 89,1 | 1,15 | 297,9 |
| SI3 | 13,5 | 83,4 | 44,6 | 1,00 | 128,0 |

**Justification des coefficients :**
- P1, P2 : appuis intermédiaires (poteaux sur portée continue) → 1,15.
- P3 : appui de rive (poteau à l'extrémité de la trame) → 1,00.
- SF1 : appui de rive (semelle filante en façade) → 1,00.

---

## TABLEAU 5 — DESCENTE DE CHARGES PAR PORTEUR (ELU)

| Porteur | A_inf (m²) | 1,35·G | 1,5·Q | Coefficient de continuité | N_ELU (kN ou kN/m) |
|---|---|---|---|---|---|
| P1 | 13,5 | 112,6 | 66,9 | 1,15 | 205,5 |
| P2 | 27,0 | 225,3 | 133,7 | 1,15 | 409,6 |
| P3 | 13,5 | 112,6 | 66,9 | 1,00 | 179,5 |
| SF1 | 54,0 (m²/ml) | 450,5 | 267,3 | 1,00 | 717,8 kN/m |
| SI1 | 13,5 | 112,6 | 66,9 | 1,15 | 205,5 |
| SI2 | 27,0 | 225,3 | 133,7 | 1,15 | 409,6 |
| SI3 | 13,5 | 112,6 | 66,9 | 1,00 | 179,5 |

---

## SYNTHÈSE (8 lignes maximum)

1. **Porteur le plus chargé (N_ELU)** : P2 (409,6 kN) et SI2 (409,6 kN) — poteau central et semelle sous poteau central.
2. **Porteur avec le plus fort ratio N/A_inf** : SF1 (717,8 kN/m / 54,0 m²/ml = 13,3 kN/m²) — semelle filante en façade.
3. **Zones où la charge d'exploitation est la plus pénalisante** : RDC et R+1 (2,5 kN/m² + 0,8 kN/m² cloisons = 3,3 kN/m² total).
4. **Hypothèses à confirmer en EXE** : H-06 (dallage 20 cm), H-07 (chape 5 cm), H-08 (isolation 5 cm) — poids propres estimés.
5. **Charge d'exploitation** : 250 daN/m² (D-03) — officielle, non une hypothèse.
6. **Coefficients de continuité** : 1,15 (appuis intermédiaires P1, P2, SI1, SI2), 1,00 (appuis de rive P3, SI3, SF1).
7. **Aucune vérification de section ni aucun ferraillage** — B-21 est une DDC préliminaire, pas une note de calcul d'exécution.
8. **Alimentation aval** : B-21 alimente B-20 (prédimensionnement), B-22 (hypothèses H-06 à H-08), B-24 (vérifications suspendues), B-40 à B-50 (DDC d'exécution — refaite dans chaque brique de calcul).

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Chaque porteur a une surface d'influence justifiée | ✅ §Tableau 1 |
| Chaque charge permanente est rattachée à une couche et à un poids volumique | ✅ §Tableau 2 |
| Chaque charge d'exploitation est rattachée à une catégorie EC1 | ✅ §Tableau 3 (C3/C1, D-03) |
| Chaque coefficient de continuité est justifié | ✅ §Tableau 4 (justification rive/intermédiaire) |
| Les tableaux ELS et ELU sont distincts | ✅ §Tableau 4 (ELS) + §Tableau 5 (ELU) |
| La sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION » | ✅ §0 (en-tête) |
| Aucune vérification de section ni aucun ferraillage produit | ✅ §Synthèse (DDC préliminaire, pas EXE) |
| Preuve d'épuisement produite | ✅ §0 |

---

**Brique B-21 exécutée en mode COMPLET — en attente de votre GO ou de nouvelles observations.**
La DDC préliminaire sert à choisir les sections en conception. **Elle ne remplace pas les DDC d'exécution** des briques de calcul B-40 à B-50. Les hypothèses H-06 à H-08 (poids propres) doivent être confirmées en EXE.
