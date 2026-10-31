# Journal B-30 — Calage sur DXF source (OUT-03)

**Date** : 2026-10-30  
**Mode** : COMPLET  
**Script** : OUT-02 (`build_b30.py`)  

## Pièces lues (preuve d'épuisement V14)

| Pièce | Lecture | Résultat |
|---|---|---|
| DXF Plans DCE | ezdxf 1.4.5 | 1582 entités, 22 calques, 46 blocs nommés |
| PDF Pièces graphiques | pypdf | 29p, vectoriel (texte extractible) |
| PDF DIAG structure | pypdf | 19p |
| PDF CCTP LOT 01 | pypdf | 38p |
| PDF DCE indice C | **échec téléchargement (400 API)** — consulté en session antérieure |
| CARNAC v3.0.2 | markdown | Fiche B-30 |

## Exécution

1. Audit source : AC1032, unités cm
2. Extraction zones : 6 zones (EXISTANT/PROJET/DEMOL)
3. Orthogonalité : max déviation 0.000000° → rotation 0°
4. Calage : 3 points non alignés (aire triangle = 65753336.49 cm²)
5. Transformation : scale 0.01, rotation 0.0°, translation (-2.660012041860209, -1.4746853880511481) m
6. Résidu : max 0.000000 m sur 21 points témoins
7. Preuve : PNG + PDF produits
8. DXF recalé : produit et relu

## Contrôles post-exécution

- DXF recalé relu : OK, 3371528 bytes, INSUNITS=6
- Extents RSU : X [-0.2518, 181.293] m — Y [-20.7807, 81.738] m
- Résidu ≤ GEO-12 : ✅

## RDL — Ligne de phase 1

| Livrable | Source | Calage B-30 | Version vue nettoyée | Date |
|---|---|---|---|---|
| SOCLE-GEOS (à produire) | DXF calé V1 | V1 | — | 2026-10-30 |

## Porte suivante

B-32 (Vue nettoyée) — extraction filtrée du DXF recalé.
