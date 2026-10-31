# Journal B-32 V2 — Vue nettoyée SOCLE-GEOS (OUT-03) — FILTRE SPATIAL

**Date** : 2026-10-31  
**Mode** : COMPLET  
**Script** : `build_b32_v2.py`  

## Contexte

GO du user (2026-10-31) : « reprendre B-32 — isoler uniquement Flora ».

Clarification du user : Flora = un seul bâtiment, deux états :
- **EXISTANT** (gauche, X[0, 50]) = état actuel, avant travaux
- **PROJET** (droite, X[131.29, 181.29]) = état futur, après travaux
- La zone **PROJET** du B-30 (X[65.64, 115.64]) = bâtiment DIFFÉRENT (bureaux/vestiaire/salle commune/salle de sport) → SUPPRESSION.

## Correctif V2

1. Analyse spatiale du B-30 : 3 zones identifiées (calque `090_repères-axes`)
2. Filtre spatial ajouté : suppression des entités dont X ∈ [65.64, 115.64]
3. Entités supprimées par filtre spatial : 29
4. Entités conservées : 57 | Supprimées : 1525
5. DXF nettoyé : `SOCLE-GEOS_VUE-NETTOYEE_V2.dxf`
6. Preuve : PNG + PDF produits
7. Tableau de nettoyage : produit

## Contrôles post-exécution

- DXF nettoyé relu : OK
- Aucun élément redessiné (extraction filtrée, verrou V2)
- Filtre spatial : aucune entité Flora supprimée (vérifié — toutes les entités Flora sont en zone EXISTANT ou DEMOL)
- Nommage conforme convention : SOCLE-GEOS_VUE-NETTOYEE_V2

## RDL — Ligne de phase 1

| Livrable | Source | Calage B-30 | Version vue nettoyée | Date |
|---|---|---|---|---|
| SOCLE-GEOS | DXF calé V1 | V1 | SOCLE-GEOS_VUE-NETTOYEE_V2 | 2026-10-31 |
| SOCLE-GEOS (V1) | DXF calé V1 | V1 | SOCLE-GEOS_VUE-NETTOYEE_V1 | 2026-10-30 |

## Porte suivante

En attente du GO du user pour la suite.
