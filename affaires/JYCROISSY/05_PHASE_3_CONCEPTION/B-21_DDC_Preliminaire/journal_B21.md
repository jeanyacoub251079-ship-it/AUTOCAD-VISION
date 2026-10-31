# Journal B-21 — Descente de charges préliminaire

**Date :** 2026-10-31
**Brique :** B-21 (Phase 3 — Conception et synthèse structurelle)
**Mode :** COMPLET

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-20 Conception GO | ✅ lue | Trame, porteurs |
| B-00 Énoncé de mission | ✅ lue | Usages |
| B-02 FDC | ✅ lue | CHG-01 à CHG-08 |
| B-03 RDR | ✅ lue | D-03 (250 daN/m²) |
| B-25 Stabilité globale | ✅ lue | Charges horizontales |

## 2. Traitement

- 7 porteurs chargés (P1-P3, SF1, SI1-SI3).
- 2 zones d'usage (RDC cabinet paramédical C3, R+1 bureaux C1).
- 3 couches de poids propre (dallage, chape, isolation).
- Charge d'exploitation : 250 daN/m² (D-03) + 0,8 kN/m² cloisons.
- Coefficients de continuité : 1,15 (intermédiaires), 1,00 (rives).
- ELS et ELU distincts.
- Aucune vérification de section ni ferraillage.

## 3. Résultat

Livrable `B-21_DDC_Preliminaire.md` produit. B-21 est **complet** (mode COMPLET).

## 4. Non-régression

Aucune brique modifiée. B-20, B-25 intacts.

## 5. Point de contrôle humain

Valider les catégories EC1 et les cloisons forfaitaires. Les hypothèses H-06 à H-08 (poids propres) doivent être confirmées en EXE.
