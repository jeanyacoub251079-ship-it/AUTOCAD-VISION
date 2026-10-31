# Journal B-43 — Planchers et dallages

**Date :** 2026-10-31
**Brique :** B-43 (Phase 4 — Calculs d'exécution)
**Mode :** PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-01 manquante)

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-02 FDC | ✅ lue | MAT-01 à MAT-04, SEC-01, CHG-01 à CHG-03, CHG-08 |
| B-20 Conception GO | ✅ lue | Dg1 dalle, Pt1/Pt2 poutres métalliques |
| B-21 DDC préliminaire | ✅ lue | Charges par zone |
| B-22 Note d'hypothèses | ✅ lue | H-03, H-06 à H-08 |
| B-40 Fondations superficielles | ✅ lue | Semelles |
| B-42 Verticaux BA | ✅ lue | Poteaux P1-P3 |

## 2. Traitement

- 2 zones chargées (RDC, R+1 — dalles BA).
- Dallage sur terre-plein — SANS OBJET (pas de dallage sur terre-plein).
- Plancher bois — SANS OBJET (pas de plancher bois).
- Classe de béton manquante (H-03 à confirmer — R-08).
- DDC d'exécution établie (distincte de B-21 — coefficients de continuité réels).
- Formules littérales (flexion, effort tranchant, poinçonnement, flèche) — aucune valeur retenue.
- Efforts aux appuis transmis à B-50 (symbole).
- Plans d'exécution non produits (OUT-01 absent).
- Calcul suspendu jusqu'à obtention de la classe de béton et de OUT-01.

## 3. Résultat

Livrable `B-43_Planchers_Dallages.md` produit. B-43 est **complète** (mode PARAMÉTRIQUE documentaire).

## 4. Non-régression

Aucune brique modifiée. B-20, B-21, B-22, B-40, B-42 intacts.

## 5. Point de contrôle humain

Valider la classe de béton (H-03 à confirmer — R-08). Valider l'environnement d'exécution (OUT-01). Le calcul est suspendu jusqu'à obtention de ces données.
