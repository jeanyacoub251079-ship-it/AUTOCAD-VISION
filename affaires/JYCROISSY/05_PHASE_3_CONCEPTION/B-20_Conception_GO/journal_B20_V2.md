# Journal B-20 V2 — Conception structure GO — Fond PROJET (B-32 V3)

**Date** : 2026-10-31  
**Mode** : INTERNE-GO  
**Script** : `build_b20_v2.py`  

## Correction fondamentale

B-20 V1 était positionné sur la zone EXISTANT (X=0-18). Refait sur B-32 V3 (PROJET seul).
La trame et les renforts sont maintenant implantés sur la zone PROJECT (X > 115,64 m).

## Trame structurelle (zone PROJET)

- Bâtiment : X[145.70, 156.98] Y[40.86, 60.22] — 11.28 m × 19.36 m
- Axes A/B/C (sens 1) : X = 145.70, 151.34, 156.98 m
- Axes 1/2/3 (sens 2) : Y = 40.86, 50.54, 60.22 m

## Ouvrages neufs implantés (zone PROJET)

- P1 : (151.34, 40.86)
- P2 : (151.34, 50.54)
- P3 : (151.34, 60.22)
- Pt1 : (151.34, 40.86) → (151.34, 50.54)
- Pt2 : (151.34, 50.54) → (151.34, 60.22)
- SI1 : (151.34, 40.86)
- SI2 : (151.34, 50.54)
- SI3 : (151.34, 60.22)
- SF1 : (145.70, 40.86) → (156.98, 40.86)
- Lt1 : (145.70, 40.86) → (148.70, 40.86)
- Lt2 : (153.98, 60.22) → (156.98, 60.22)
- Dg1 : dallage RDC (145.70, 40.86) à (156.98, 50.54)

## Renforts de l'existant

- R1 (Moisage) : (151.34, 43.70)
- R2 (Sommier répartition) : (145.70, 40.86)
- R3 (Entretoise) : (151.34, 50.54)
- R4 (Contrefiche) : (151.34, 60.22)

## Livrables

- DXF : B-20_Plan_Principe_P1_V2.dxf
- PNG : B-20_Plan_Principe_P1_V2.png
- PDF : B-20_Plan_Principe_P1_V2.pdf
- Journal : journal_B20_V2.md

## Contrôles

- Fond : B-32 V3 (PROJET seul, 30 entités)
- Aucun élément en zone EXISTANT ou MILIEU
- Filigrane « PRINCIPE — NE PAS EXÉCUTER — Indice P1 » appliqué
