# Journal B-32 V3 — Plan d'exécution SOCLE-GEOS — PROJET seul (OUT-03)

**Date** : 2026-10-31  
**Mode** : COMPLET  
**Script** : `build_b32_v3.py`  

## Correction fondamentale (user GO 2026-10-31)

Le user a corrigé une erreur de compréhension majeure :
- **Un plan de structures ne garde qu'UNE seule vue en plan : le PROJET.**
- L'EXISTANT est la référence pour calculer les renforts, mais n'apparaît pas sur le plan livré.
- Le plan d'exécution indique à l'entreprise quels travaux réaliser.
- Les éléments de renfort (poteaux, semelles, dallage, linteaux) apparaissent sur ce plan nettoyé.

## Exécution V3

1. Lecture du DXF calé B-30 (RSU, m)
2. Filtre spatial : conserver uniquement X > 115.64 m (zone PROJET de Flora)
3. Entités EXISTANT supprimées : 27
4. Entités MILIEU supprimées : 29
5. Entités conservées : 30 | Supprimées : 1552
6. DXF nettoyé : `SOCLE-GEOS_VUE-NETTOYEE_V3.dxf`
7. Preuve : PNG + PDF produits
8. Tableau de nettoyage : produit

## Contrôles post-exécution

- DXF nettoyé relu : OK
- Aucun élément redessiné (extraction filtrée, verrou V2)
- Plan d'exécution = zone PROJET seule (X > 115.64 m)
- Aucune entité EXISTANT ou MILIEU dans le DXF V3
- Nommage conforme convention : SOCLE-GEOS_VUE-NETTOYEE_V3

## RDL — Ligne de phase 1

| Livrable | Source | Calage B-30 | Version vue nettoyée | Date |
|---|---|---|---|---|
| SOCLE-GEOS | DXF calé V1 | V1 | SOCLE-GEOS_VUE-NETTOYEE_V3 | 2026-10-31 |

## Porte suivante

En attente du GO du user pour la suite.
