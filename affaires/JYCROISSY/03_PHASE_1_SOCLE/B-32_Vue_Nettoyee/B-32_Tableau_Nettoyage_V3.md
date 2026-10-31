# B-32 V3 — Tableau de nettoyage — SOCLE-GEOS V3 — PLAN D'EXÉCUTION

**Source** : `B-30_FLORA_RSU_calé_v1.dxf` (DXF calé V1)  
**Livrable** : SOCLE-GEOS (plan d'exécution / socle géométrique)  
**Mode** : COMPLET  
**Version** : V3 — PLAN D'EXÉCUTION = PROJET seul (2026-10-31)  

## Correctif V3 — Plan d'exécution = PROJET seul

**Principe** : un plan de structures ne garde qu'**une seule vue en plan** : le PROJET.
L'EXISTANT est la référence pour calculer les renforts, mais n'apparaît pas sur le plan livré.
Le plan d'exécution indique à l'entreprise quels travaux réaliser.

**Zones du B-30** (calque `090_repères-axes`) :
- **EXISTANT** : X[0, 50] m → état actuel → **SUPPRIMÉ** (référence interne)
- **PROJET (milieu)** : X[65.64, 115.64] m → bâtiment DIFFÉRENT (bureaux/vestiaire/salle commune/salle de sport) → **SUPPRIMÉ**
- **DEMOL** : X[131.29, 181.29] m → Flora **PROJET** (plan d'exécution) → **CONSERVÉ (seule zone gardée)**

**Filtre spatial V3** : conserver uniquement X > 115.64 m (zone PROJET de Flora).

## Calques

| Calque | Statut | Conservé | Supprimés | Justification |
|---|---|---|---|---|
| `0` | SUPPRIMER | 0 | 12 | Géométrie bâtiment — non porteur explicite |
| `010_mur` | SUPPRIMER | 0 | 20 | Murs porteurs (détail géométrique) |
| `020_cloi` | À TRANCHER | 2 | 257 | Blocs plans porteurs (INSERT) |
| `020_cloisons` | SUPPRIMER | 0 | 2 | Cloisons — non porteur |
| `030_menuiserie` | SUPPRIMER | 0 | 83 | Menuiseries — non porteur |
| `040_meubles` | SUPPRIMER | 0 | 160 | Mobilier — non porteur |
| `050_sols` | SUPPRIMER | 0 | 2 | Sols — non porteur |
| `051_plafonds` | SUPPRIMER | 0 | 6 | Plafonds — non porteur |
| `060_repères murs` | CONSERVER | 1 | 0 | Repères murs |
| `070_trait-fin` | À TRANCHER | 2 | 171 | NORD conservé (orientation) |
| `075_cotation` | SUPPRIMER | 0 | 104 | Cotations — non porteur |
| `075_cotation détails` | SUPPRIMER | 0 | 49 | Cotations détaillées — non porteur |
| `077_textes-1` | SUPPRIMER | 0 | 133 | Textes — non porteur |
| `078_textes-2` | SUPPRIMER | 0 | 339 | Textes — non porteur |
| `078_textes-3` | SUPPRIMER | 0 | 43 | Textes — non porteur |
| `079_textes-4` | SUPPRIMER | 0 | 16 | Textes — non porteur |
| `080_plomb-cvc` | SUPPRIMER | 0 | 70 | Fluides — non porteur |
| `090_repères-axes` | À TRANCHER | 3 | 6 | Axes / zone chantier |
| `092_surfaces projet` | SUPPRIMER | 0 | 13 | Surfaces projet |
| `100 TEXTE PMR` | SUPPRIMER | 0 | 62 | Texte PMR — non porteur |
| `102_demol` | CONSERVER | 22 | 0 | Démolition — état projet |
| `31_sanitaires` | SUPPRIMER | 0 | 4 | Sanitaires — non porteur |

**Total** : 1582 entités source → 30 conservées, 1552 supprimées

## Blocs INSERT conservés (zone PROJET uniquement) — Plan d'exécution

| Bloc | Calque | Position RSU (m) | Justification |
|---|---|---|---|
| Murs porteurs selon geometre projet | 020_cloi | (179.86, 41.44) | Murs porteurs selon géométrie projet |
| R+1 Projet | 020_cloi | (163.38, 10.26) | Plan R+1 projet — géométrie porteuse |
| NORD | 070_trait-fin | (165.87, 42.23) | Fléche nord — orientation |
| NORD | 070_trait-fin | (158.13, 3.72) | Fléche nord — orientation |
| cloisons reperage | 060_repères murs | (115.64, 35.0) | Repère cloisons — repère structurel |

## Entités EXISTANT supprimées (zone X[0, 50] — référence interne, non livrée)

| Calque | Type | Nom | X RSU (m) |
|---|---|---|---|
| `090_repères-axes` | MTEXT | — | 0.0 |
| `010_mur` | LWPOLYLINE | — | 15.13 |
| `010_mur` | LWPOLYLINE | — | 15.94 |
| `010_mur` | LINE | — | 17.22 |
| `010_mur` | LINE | — | 17.22 |
| `010_mur` | LINE | — | 18.09 |
| `010_mur` | LWPOLYLINE | — | 18.24 |
| `010_mur` | LWPOLYLINE | — | 19.38 |
| `0` | LINE | — | 20.74 |
| `0` | LINE | — | 20.82 |
| `0` | LINE | — | 20.94 |
| `0` | LINE | — | 20.94 |
| `0` | LINE | — | 20.94 |
| `0` | LINE | — | 20.94 |
| `0` | LINE | — | 21.06 |
| `0` | LINE | — | 21.14 |
| `010_mur` | LINE | — | 21.19 |
| `010_mur` | LINE | — | 22.59 |
| `090_repères-axes` | LWPOLYLINE | — | 25.0 |
| `090_repères-axes` | LWPOLYLINE | — | 25.0 |
| `010_mur` | LINE | — | 26.0 |
| `010_mur` | LINE | — | 26.84 |
| `070_trait-fin` | INSERT | NORD | 26.84 |
| `010_mur` | LINE | — | 27.14 |
| `020_cloi` | INSERT | R+1 Existant | 32.09 |
| `070_trait-fin` | INSERT | NORD | 34.58 |
| `020_cloi` | INSERT | Plan existant mi geometre rdc | 48.57 |

**Total EXISTANT supprimé** : 27 entités

## Entités MILIEU supprimées (zone X[65.64, 115.64] — bâtiment non Flora)

| Calque | Type | Nom | X RSU (m) |
|---|---|---|---|
| `090_repères-axes` | MTEXT | — | 65.64 |
| `010_mur` | LWPOLYLINE | — | 80.77 |
| `010_mur` | LWPOLYLINE | — | 81.58 |
| `010_mur` | LWPOLYLINE | — | 83.33 |
| `010_mur` | LWPOLYLINE | — | 83.73 |
| `092_surfaces projet` | LWPOLYLINE | — | 83.93 |
| `092_surfaces projet` | LWPOLYLINE | — | 84.93 |
| `092_surfaces projet` | LWPOLYLINE | — | 84.94 |
| `010_mur` | LWPOLYLINE | — | 85.03 |
| `092_surfaces projet` | LWPOLYLINE | — | 85.06 |
| `010_mur` | LWPOLYLINE | — | 85.28 |
| `092_surfaces projet` | LWPOLYLINE | — | 85.82 |
| `092_surfaces projet` | LWPOLYLINE | — | 86.04 |
| `092_surfaces projet` | LWPOLYLINE | — | 86.44 |
| `092_surfaces projet` | LWPOLYLINE | — | 86.44 |
| `092_surfaces projet` | LWPOLYLINE | — | 88.14 |
| `092_surfaces projet` | LWPOLYLINE | — | 90.25 |
| `090_repères-axes` | LWPOLYLINE | — | 90.64 |
| `090_repères-axes` | LWPOLYLINE | — | 90.64 |
| `092_surfaces projet` | LWPOLYLINE | — | 90.69 |
| `092_surfaces projet` | LWPOLYLINE | — | 91.3 |
| `092_surfaces projet` | LWPOLYLINE | — | 92.08 |
| `070_trait-fin` | INSERT | NORD | 92.49 |
| `0` | LWPOLYLINE | — | 92.59 |
| `0` | INSERT | R+1 Projet | 97.73 |
| `070_trait-fin` | INSERT | NORD | 100.22 |
| `010_mur` | LWPOLYLINE | — | 101.12 |
| `010_mur` | LWPOLYLINE | — | 101.16 |
| `0` | INSERT | Murs porteurs selon geometre projet | 114.22 |

**Total MILIEU supprimé** : 29 entités

## Limites (V4 — pas de redessin)

- Les blocs plans « mi géomètre » contiennent murs + mobilier + textes : impossible de filtrer sans redessin (verrou V2).
- Le mobilier/textes à l'intérieur des blocs plans est conservé — limitation déclarée.
- Le calage est celui de B-30 (RSU, m). Aucun ajustement visuel (V4).
- Le plan d'exécution V3 = zone PROJET seule. Les renforts (poteaux, semelles, dallage, linteaux) seront ajoutés sur ce plan.
