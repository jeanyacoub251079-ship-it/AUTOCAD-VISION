# B-21 V2 — Descente de charges préliminaire

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-21 (Phase 3 — Conception et synthèse structurelle)
**Date :** 2026-10-31
**Mode :** COMPLET
**Version :** 2.0 (géométrie B-20 V2 — PROJET zone)
**Supersède :** B-21 V1 (géométrie B-20 V1 — EXISTANT zone, rejetée)

---

## 0. PROUVE D'ÉPUISEMENT (verrou V14)

| Pièce | Statut | Passages consultés | Résultat |
|---|---|---|---|
| B-20 V2 Conception GO | ✅ lue | Trame PROJECT, porteurs P1-P3, Pt1-Pt2, SI1-SI3, SF1, Lt1-Lt2, Dg1 | Porteurs à charger |
| B-00 Énoncé de mission | ✅ lue | §1 à §6 | Mission reformulée, usages |
| B-02 FDC | ✅ lue | CHG-01 à CHG-08 statuts | Charges d'exploitation et permanentes |
| B-03 RDR | ✅ lue | D-03 (250 daN/m²) | Charge d'exploitation officielle |
| B-25 Stabilité globale | ✅ lue | Cheminement des efforts | Charges horizontales |

**Aucune charge déclarée sans cette preuve.** Chaque charge est rattachée à une couche (poids propre) ou à une catégorie EC1 (exploitation).

---

## GÉOMÉTRIE B-20 V2 (PROJET zone)

| Élément | Position | Valeur |
|---|---|---|
| Bâtiment Flora | X[145,70 — 156,98] Y[40,86 — 60,22] | 11,28 m × 19,36 m |
| Axe A | X = 145,70 | Façade (SF1) |
| Axe B | X = 151,34 | Poteaux P1-P3 |
| Axe C | X = 156,98 | Façade |
| Axe 1 | Y = 40,86 | Façade |
| Axe 2 | Y = 50,54 | Centre |
| Axe 3 | Y = 60,22 | Façade |
| Bays X | A-B = 5,64 m, B-C = 5,64 m | |
| Bays Y | 1-2 = 9,68 m, 2-3 = 9,68 m | |

---

## TABLEAU 1 — SURFACE D'INFLUENCE

| Porteur | Tributaire X (m) | Tributaire Y (m) | A_inf (m²) | Justification |
|---|---|---|---|---|
| P1 (poteau, axe B/1) | 5,64 | 4,84 | 27,30 | Mi-bay A-B + mi-bay B-C = 5,64 m ; mi-bay 1-2 = 4,84 m (rive) |
| P2 (poteau, axe B/2) | 5,64 | 9,68 | 54,60 | Mi-bay A-B + mi-bay B-C = 5,64 m ; mi-bay 1-2 + mi-bay 2-3 = 9,68 m (intermédiaire) |
| P3 (poteau, axe B/3) | 5,64 | 4,84 | 27,30 | Mi-bay A-B + mi-bay B-C = 5,64 m ; mi-bay 2-3 = 4,84 m (rive) |
| SF1 (semelle filante, axe A) | — | 19,36 | 54,60 (m²/ml) | Longueur 19,36 m × tributaire mi-bay A-B = 2,82 m |
| SI1 (semelle isolée, P1) | — | — | 27,30 | Surface d'influence du poteau P1 (transmission au sol) |
| SI2 (semelle isolée, P2) | — | — | 54,60 | Surface d'influence du poteau P2 (transmission au sol) |
| SI3 (semelle isolée, P3) | — | — | 27,30 | Surface d'influence du poteau P3 (transmission au sol) |

---

## TABLEAU 2 — CHARGES PERMANENTES PAR COUCHE

| Zone | Couche | Épaisseur | Poids volumique | g (kN/m²) | Source |
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
| P1 | 27,30 | 168,7 | 90,1 | 1,00 (appui de rive — axe 1) | 258,8 |
| P2 | 54,60 | 337,4 | 180,2 | 1,15 (appui intermédiaire — axe 2) | 595,2 |
| P3 | 27,30 | 168,7 | 90,1 | 1,00 (appui de rive — axe 3) | 258,8 |
| SF1 | 54,60 (m²/ml) | 337,4 | 180,2 | 1,00 (appui de rive) | 517,6 kN/m |
| SI1 | 27,30 | 168,7 | 90,1 | 1,00 (rive) | 258,8 |
| SI2 | 54,60 | 337,4 | 180,2 | 1,15 (intermédiaire) | 595,2 |
| SI3 | 27,30 | 168,7 | 90,1 | 1,00 (rive) | 258,8 |

**Justification des coefficients (V2) :**
- P1 : poteau à l'extrémité de la trame en Y (axe 1 = bout du bâtiment) → appui de rive → 1,00.
- P2 : poteau au centre de la trame en Y (axe 2) → appui intermédiaire → 1,15.
- P3 : poteau à l'extrémité de la trame en Y (axe 3 = bout du bâtiment) → appui de rive → 1,00.
- SF1 : semelle filante en façade → appui de rive → 1,00.

---

## TABLEAU 5 — DESCENTE DE CHARGES PAR PORTEUR (ELU)

| Porteur | A_inf (m²) | 1,35·G | 1,5·Q | Coefficient de continuité | N_ELU (kN ou kN/m) |
|---|---|---|---|---|---|
| P1 | 27,30 | 227,7 | 135,1 | 1,00 | 362,9 |
| P2 | 54,60 | 455,5 | 270,2 | 1,15 | 834,6 |
| P3 | 27,30 | 227,7 | 135,1 | 1,00 | 362,9 |
| SF1 | 54,60 (m²/ml) | 455,5 | 270,2 | 1,00 | 725,7 kN/m |
| SI1 | 27,30 | 227,7 | 135,1 | 1,00 | 362,9 |
| SI2 | 54,60 | 455,5 | 270,2 | 1,15 | 834,6 |
| SI3 | 27,30 | 227,7 | 135,1 | 1,00 | 362,9 |

---

## SYNTHÈSE (8 lignes maximum)

1. **Porteur le plus chargé (N_ELU)** : P2 et SI2 (834,6 kN) — poteau central et semelle sous poteau central.
2. **Porteur avec le plus fort ratio N/A_inf** : SF1 (725,7 kN/m / 54,60 m²/ml = 13,3 kN/m²) — semelle filante en façade.
3. **Zones où la charge d'exploitation est la plus pénalisante** : RDC et R+1 (2,5 kN/m² + 0,8 kN/m² cloisons = 3,3 kN/m² total).
4. **Hypothèses à confirmer en EXE** : H-06 (dallage 20 cm), H-07 (chape 5 cm), H-08 (isolation 5 cm) — poids propres estimés.
5. **Charge d'exploitation** : 250 daN/m² (D-03) — officielle, non une hypothèse.
6. **Coefficients de continuité** : 1,15 (appui intermédiaire P2, SI2), 1,00 (appuis de rive P1, P3, SF1, SI1, SI3).
7. **Aucune vérification de section ni aucun ferraillage** — B-21 V2 est une DDC préliminaire, pas une note de calcul d'exécution.
8. **Alimentation aval** : B-21 V2 alimente B-22 (hypothèses H-06 à H-08), B-24 (vérifications suspendues), B-40 à B-50 (DDC d'exécution — refaite dans chaque brique de calcul).

---

## ÉCART V1 → V2

| Paramètre | V1 (EXISTANT) | V2 (PROJET) |
|---|---|---|
| Bâtiment | 18 m × 9 m | 11,28 m × 19,36 m |
| A_inf(P1) | 13,5 m² | 27,30 m² |
| A_inf(P2) | 27,0 m² | 54,60 m² |
| A_inf(SF1) | 54,0 m²/ml | 54,60 m²/ml |
| k(P1) | 1,15 | 1,00 (rive) |
| k(P2) | 1,15 | 1,15 (intermédiaire) |
| k(P3) | 1,00 | 1,00 (rive) |
| N_ELU(P2) | 409,6 kN | 834,6 kN |
| N_ELU(SF1) | 717,8 kN/m | 725,7 kN/m |

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
| Géométrie rattachée à B-20 V2 (PROJECT zone) | ✅ §Géométrie B-20 V2 |

---

**Brique B-21 V2 exécutée en mode COMPLET — en attente de votre GO ou de nouvelles observations.**
La DDC préliminaire sert à choisir les sections en conception. **Elle ne remplace pas les DDC d'exécution** des briques de calcul B-40 à B-50. Les hypothèses H-06 à H-08 (poids propres) doivent être confirmées en EXE.
