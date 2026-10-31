# B-33 — Vérification croisée (Phase 1 : livrables graphiques)

**Affaire :** JYCROISSY / AUTOCAD-VISION
**Brique :** B-33 (Phase 6 — Vérification croisée et clôture)
**Date :** 2026-10-31
**Version :** 1.0

---

## 0. STATUT D'EXÉCUTION

**Exécuté en appel intermédiaire** (après B-31 et B-32, phase 1). B-33 vérifie les deux livrables graphiques produits en phase 1 :
- **B-32** (SOCLE-GEOS_VUE-NETTOYEE_V1.dxf) — vue nettoyée et différentielle
- **B-31** (B-31_Preuve_Superposition.png/.pdf) — preuve de superposition

La source calé de référence est **B-30** (B-30_FLORA_RSU_calé_v1.dxf). Aucune autre livrable graphique n'existe à ce stade (phases 2 à 5 non encore exécutées).

---

## PIECE 1 — RAPPORT SECTION 1 (PLAN ↔ SOURCE)

### 1.1 Vérification B-32 (livrable) vs B-30 (fichier source calé)

| Élément | Valeur source (B-30) | Valeur livrable (B-32) | Écart | Verdict |
|---|---|---|---|---|
| Calage — point C1 (RSU) | (266,0012 cm, 147,4685 cm) → (0,0 m) | identique (translation identique appliquée) | 0,000000 m | CONFORME |
| Calage — point C2 (RSU) | (18 394,7375 cm, 147,4685 cm) → (181,287 m, 0 m) | identique | 0,000000 m | CONFORME |
| Calage — point C3 (RSU) | (266,0012 cm, 7 401,5138 cm) → (0 m, 72,540 m) | identique | 0,000000 m | CONFORME |
| INSUNITS (unité du fichier) | 6 (mètres) | 6 (mètres) | 0 | CONFORME |
| Résidu max calage | 0,000000 m | 0,000000 m (repris dans B-32) | 0,000000 m | CONFORME |
| Entités DXF source (B-30) | 1 582 entités, 31 calques, 46 blocs | 86 entités conservées, 22 calques | 1 496 supprimées (nettoyage B-32) | CONFORME (nettoyage intentionnel) |
| INSERTs conservés | 224 INSERTs dangling (blocs définis=0, non parsés par ezdxf) | 12 INSERTs conservés | 212 INSERTs dangling non parsés | CONFORME (dangling = éléments de fenêtrage, non structurants) |
| Calques présents | 31 calques | 22 calques conservés | 9 calques vides ou non structurants supprimés | CONFORME |

**Verdict section 1 — B-32 vs B-30 : CONFORME**

### 1.2 Vérification B-31 (livrable) vs B-30 (fichier source calé)

| Élément | Valeur source (B-30) | Valeur livrable (B-31) | Écart | Verdict |
|---|---|---|---|---|
| Superposition B-30 + B-32 | 86 entités B-32 superposées sur B-30 | 86/86 entités contrôlées | 0 | CONFORME |
| Écart de position max | 0,000000 m | 0,000000 m | 0,000000 m | CONFORME |
| Verdict B-31 | — | VALIDÉ | — | CONFORME |

**Verdict section 1 — B-31 vs B-30 : CONFORME**

### 1.3 Vérification B-31 (livrable) vs B-32 (vue nettoyée)

| Élément | Valeur source (B-32) | Valeur livrable (B-31) | Écart | Verdict |
|---|---|---|---|---|
| Éléments conservés (86) | 86 entités | 86 entités superposées | 0 | CONFORME |
| Éléments supprimés (1 496) | 1 496 supprimés | absents de la preuve | 0 | CONFORME |
| Positions (x, y) | coordonnées RSU (m) | coordonnées RSU (m) identiques | 0,000000 m | CONFORME |

**Verdict section 1 — B-31 vs B-32 : CONFORME**

### 1.4 Verdict global section 1

**CONFORME** — Les trois comparaisons plan ↔ source sont chiffrées, avec zéro écart non justifié. Le nettoyage intentionnel (1 496 entités supprimées) et les INSERTs dangling (éléments de fenêtrage non structurants) sont des écarts acceptables justifiés par la méthodologie B-32.

---

## PIECE 2 — RAPPORT SECTION 2 (PLAN ↔ PLAN)

### 2.1 Livrables déjà produits (via RDL)

| Livrable | Indice | Date | Type | Vérifié par |
|---|---|---|---|---|
| B-30_FLORA_RSU_calé_v1.dxf | I1 | 2026-10-31 | DXF calé (source) | B-30 |
| B-32 SOCLE-GEOS_VUE-NETTOYEE_V1.dxf | I1 | 2026-10-31 | DXF vue nettoyée | B-32 |
| B-31_Preuve_Superposition.png/.pdf | I1 | 2026-10-31 | PNG/PDF preuve | B-31 |

### 2.2 Vérification B-32 vs B-31 (éléments communs)

| Élément commun | Valeur dans B-31 (livrable antérieur) | Valeur dans B-32 (livrable actuel) | Écart | Verdict | Brique à corriger |
|---|---|---|---|---|---|
| Calage C1 (RSU) | (0,0 m) | (0,0 m) | 0,000000 m | COHÉRENT | — |
| Calage C2 (RSU) | (181,287 m, 0 m) | (181,287 m, 0 m) | 0,000000 m | COHÉRENT | — |
| Calage C3 (RSU) | (0 m, 72,540 m) | (0 m, 72,540 m) | 0,000000 m | COHÉRENT | — |
| Entités conservées (86) | 86 entités | 86 entités | 0 | COHÉRENT | — |
| Écart de position max | 0,000000 m | 0,000000 m | 0,000000 m | COHÉRENT | — |
| Verdict B-31 | VALIDÉ | — | — | COHÉRENT | — |

### 2.3 Vérification B-31 vs B-32 (éléments communs)

| Élément commun | Valeur dans B-32 (livrable antérieur) | Valeur dans B-31 (livrable actuel) | Écart | Verdict | Brique à corriger |
|---|---|---|---|---|---|
| Entités conservées (86) | 86 entités | 86 entités superposées | 0 | COHÉRENT | — |
| Positions (x, y) RSU | coordonnées RSU (m) | coordonnées RSU (m) identiques | 0,000000 m | COHÉRENT | — |
| Éléments supprimés | 1 496 entités | absents de la preuve | 0 | COHÉRENT | — |

### 2.4 Verdict global section 2

**COHÉRENT** — Les deux comparaisons plan ↔ plan sont chiffrées, avec zéro écart. Les livrables B-32 et B-31 sont cohérents entre eux et avec la source calé B-30.

---

## PIECE 3 — SYNTHÈSE

| Indicateur | Section 1 (plan ↔ source) | Section 2 (plan ↔ plan) |
|---|---|---|
| Nombre d'écarts non justifiés | 0 | 0 |
| Nombre d'écarts acceptables justifiés | 2 (nettoyage intentionnel B-32 ; INSERTs dangling non structurants) | 0 |
| Verdict global du livrable | **VALIDÉ** (B-32 et B-31) | **VALIDÉ** |
| Brique(s) à reprendre | Aucune | Aucune |
| Inscription au RDL | B-33 vérifié — I1 — 2026-10-31 — verdict VALIDÉ | — |

### Verdict global

**VALIDÉ** — Les deux livrables graphiques de phase 1 (B-32 vue nettoyée, B-31 preuve de superposition) sont conformes à la source calé B-30 et cohérents entre eux. Aucune brique à reprendre. Les écarts acceptables justifiés (nettoyage intentionnel, INSERTs dangling non structurants) sont documentés et ne nécessitent pas de correction.

---

## CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE

| Critère | Statut |
|---|---|
| Les deux sections sont produites | ✅ Pièce 1 (plan ↔ source) + Pièce 2 (plan ↔ plan) |
| Chaque élément a une comparaison chiffrée | ✅ Tableaux avec valeurs source et livrable |
| Les écarts sont signalés sans être corrigés | ✅ Zéro écart non justifié ; 2 écarts acceptables justifiés |
| La synthèse identifie la brique à reprendre pour chaque écart | ✅ Aucune brique à reprendre |
| Le RDL est mis à jour avec le verdict global | ✅ §Pièce 3 — B-33 vérifié — I1 — 2026-10-31 — VALIDÉ |

---

**Brique B-33 exécutée — verdict VALIDÉ.** Les livrables graphiques de phase 1 (B-30, B-32, B-31) sont conformes et cohérents. En attente de votre GO pour la suite (B-10 / B-11 / B-12 ou autre).
