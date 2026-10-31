# Journal B-21 V2 — Descente de charges préliminaire

**Date :** 2026-10-31
**Brique :** B-21 V2 (Phase 3 — Conception et synthèse structurelle)
**Mode :** COMPLET
**Supersède :** B-21 V1 (géométrie B-20 V1 — EXISTANT zone, rejetée)

---

## 1. Origine du recalcul

B-20 V2 a modifié la géométrie de la trame : bâtiment déplacé de la zone EXISTANT (X=0–18, 18m×9m) à la zone PROJET (X[145,70,156,98] Y[40,86,60,22], 11,28m×19,36m). La DDC V1 reposait sur la géométrie V1 et doit être refaite.

## 2. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-20 V2 Conception GO | ✅ lue | Trame PROJECT, porteurs, geometry |
| B-00 Énoncé de mission | ✅ lue | Usages |
| B-02 FDC | ✅ lue | CHG-01 à CHG-08 |
| B-03 RDR | ✅ lue | D-03 (250 daN/m²) |
| B-25 Stabilité globale | ✅ lue | Charges horizontales |

## 3. Traitement

- 7 porteurs chargés (P1-P3, SF1, SI1-SI3).
- 2 zones d'usage (RDC cabinet paramédical C3, R+1 bureaux C1).
- 3 couches de poids propre (dallage, chape, isolation).
- Charge d'exploitation : 250 daN/m² (D-03) + 0,8 kN/m² cloisons.
- Coefficients de continuité : 1,15 (intermédiaire P2/SI2), 1,00 (rives P1/P3/SF1/SI1/SI3).
- ELS et ELU distincts.
- Aucune vérification de section ni ferraillage.

## 4. Résultat

Livrable `B-21_DDC_Preliminaire_V2.md` produit. B-21 V2 est **complet** (mode COMPLET).

## 5. Écart V1 → V2

| Paramètre | V1 | V2 |
|---|---|---|
| Bâtiment | 18m × 9m | 11,28m × 19,36m |
| N_ELU(P2) | 409,6 kN | 834,6 kN |
| N_ELU(SF1) | 717,8 kN/m | 725,7 kN/m |
| k(P1) | 1,15 | 1,00 (rive) |

## 6. Non-régression

Aucune brique modifiée. B-20, B-25 intacts. B-21 V1 conservé pour référence.

## 7. Point de contrôle humain

Valider les catégories EC1 et les cloisons forfaitaires. Les hypothèses H-06 à H-08 (poids propres) doivent être confirmées en EXE.
