# Journal B-45 — Structure métallique

**Date :** 2026-10-31
**Brique :** B-45 (Phase 4 — Calculs d'exécution)
**Mode :** PARAMÉTRIQUE documentaire (OUT-01 absent + MAT-05 manquante)

---

## 1. Entrées lues

| Pièce | Statut | Note |
|---|---|---|
| B-02 FDC | ✅ lue | MAT-05, CHG-01 à CHG-03, CHG-06 |
| B-20 Conception GO | ✅ lue | Pt1/Pt2 poutres métalliques |
| B-21 DDC préliminaire | ✅ lue | Charges par zone |
| B-22 Note d'hypothèses | ✅ lue | H-02, H-03 |
| B-40 Fondations superficielles | ✅ lue | Semelles |
| B-42 Verticaux BA | ✅ lue | Poteaux P1-P3 |
| B-43 Planchers et dallages | ✅ lue | Dalles BA |

## 2. Traitement

- 2 profilés chargés (Pt1, Pt2 — poutres métalliques neuves).
- Nuance d'acier manquante (H-03 à confirmer — R-08).
- Section poutres métalliques h≈500 mm (H-02 à confirmer).
- DDC d'exécution établie (distincte de B-21 — coefficients de continuité réels).
- Formules littérales (flexion, cisaillement, interaction M-V, flambement, déversement, flèche) — aucune valeur retenue.
- Efforts aux assemblages transmis à B-50 (symbole).
- Plans d'exécution non produits (OUT-01 absent).
- Calcul suspendu jusqu'à obtention de la nuance d'acier et de OUT-01.

## 3. Résultat

Livrable `B-45_Structure_Metallique.md` produit. B-45 est **complète** (mode PARAMÉTRIQUE documentaire).

## 4. Non-régression

Aucune brique modifiée. B-20, B-21, B-22, B-40, B-42, B-43 intacts.

## 5. Point de contrôle humain

Valider la nuance d'acier (H-03 à confirmer — R-08). Valider la section poutres métalliques (H-02 à confirmer). Valider l'environnement d'exécution (OUT-01). Le calcul est suspendu jusqu'à obtention de ces données.
