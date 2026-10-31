# Journal B-42 — Verticaux BA

**Date :** 2026-10-31
**Brique :** B-42 (Phase 4 — Calculs d'exécution)
**Mode :** PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-01 manquante)

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-02 FDC | ✅ lue | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03 |
| B-20 Conception GO | ✅ lue | P1/P2/P3 poteaux BA |
| B-21 DDC préliminaire | ✅ lue | Appuis P1-P3 |
| B-22 Note d'hypothèses | ✅ lue | H-01, H-03, H-05 |
| B-40 Fondations superficielles | ✅ lue | Semelles SI1-SI3 |

## 2. Traitement

- 3 verticaux chargés (P1, P2, P3 — poteaux neufs).
- Classe de béton manquante (H-03 à confirmer — R-08).
- DDC d'exécution établie (distincte de B-21 — coefficients de continuité réels).
- Formules littérales (flambement, N-M, ferraillage) — aucune valeur retenue.
- Efforts à ancrer transmis à B-50 (symbole).
- Plans d'exécution non produits (OUT-01 absent).
- Calcul suspendu jusqu'à obtention de la classe de béton et de OUT-01.

## 3. Résultat

Livrable `B-42_Verticaux_BA.md` produit. B-42 est **complète** (mode PARAMÉTRIQUE documentaire).

## 4. Non-régression

Aucune brique modifiée. B-20, B-21, B-22, B-40 intacts.

## 5. Point de contrôle humain

Valider la classe de béton (H-03 à confirmer — R-08). Valider l'environnement d'exécution (OUT-01). Le calcul est suspendu jusqu'à obtention de ces données.
