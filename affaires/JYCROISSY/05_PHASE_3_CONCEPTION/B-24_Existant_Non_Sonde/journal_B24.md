# Journal B-24 — Vérification d'éléments existants non sondés

**Date :** 2026-10-31
**Brique :** B-24 (Phase 3 — Conception et synthèse structurelle)
**Mode :** PARAMÉTRIQUE

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-02 FDC | ✅ lue | EXI-01, EXI-03, EXI-04 |
| B-11 Audit du diagnostic | ✅ lue | D-01, D-03, prescriptions |
| B-20 Conception GO | ✅ lue | Renforts R1 à R4 |
| B-21 DDC préliminaire | ✅ lue | Appuis P1-P3, SF1, R1 |
| B-23 Exploitation du diagnostic | ✅ lue | Appuis sur l'existant |
| DOC-05 Diagnostic structure existant | ✅ lue | Rapport de diagnostic |

## 2. Traitement

- 3 éléments non sondés (murs porteurs Ouest et Est, semelle filante SF1).
- 3 données manquantes (section du mur, résistance du matériau, épaisseur du mur).
- 3 vérifications littérales (compression de la maçonnerie existante).
- 9 valeurs testées (3 sections × 3 murs — sensibilité NON CONTRACTUEL).
- 9 essais/sondages nécessaires (carottages + essais de résistance + sondages destructifs).
- 0 élément favorable pour toutes les valeurs plausibles (σ >> f_d).
- Aucune valeur retenue — toutes les données manquantes en symbole.
- Vérification SUSPENDUE jusqu'à obtention des données.

## 3. Résultat

Livrable `B-24_Existant_Non_Sonde.md` produit. B-24 est **complète** (mode PARAMÉTRIQUE).

## 4. Non-régression

Aucune brique modifiée. B-20, B-21, B-22, B-23 intacts.

## 5. Point de contrôle humain

Valider le tableau de sensibilité (NON CONTRACTUEL). Valider les 9 essais/sondages (référentiel, nombre, emprise). Valider la suspension (vérification suspendue jusqu'à obtention des données). Valider l'impact sur la conception (B-20) — les vérifications suspendues impactent les renforcements R1 à R4.

**Phase 3 COMPLETE — B-20, B-25, B-21, B-22, B-23, B-24 livrés et commités.**
