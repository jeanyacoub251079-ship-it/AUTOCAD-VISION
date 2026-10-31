# B-32 V2 — Tableau de nettoyage — SOCLE-GEOS V2

**Source** : `B-30_FLORA_RSU_calé_v1.dxf` (DXF calé V1)  
**Livrable** : SOCLE-GEOS (plan de principe / socle géométrique)  
**Mode** : COMPLET  
**Version** : V2 — FILTRE SPATIAL (2026-10-31)  

## Correctif V2 — Filtre spatial

**Problème** : le B-30 contient 3 zones spatiales (calque `090_repères-axes`) :
- **EXISTANT** : X[0, 50] m → Flora existant (gauche)
- **PROJET** : X[65.64, 115.64] m → bâtiment DIFFÉRENT (bureaux/vestiaire/salle commune/salle de sport)
- **DEMOL** : X[131.29, 181.29] m → Flora projet (droite)

**Solution** : filtre spatial — suppression des entités dont X ∈ [65.64, 115.64].
Flora (EXISTANT + PROJET) = le même bâtiment, deux états (actuel + futur).

## Calques

| Calque | Statut | Conservé | Supprimés | Suppression spatiale (milieu) | Justification |
|---|---|---|---|---|---|
| `0` | À TRANCHER | 8 | 4 | 3 | Géométrie bâtiment (contour, axes) — non porteur explicite, conservé pour trame |
| `010_mur` | À TRANCHER | 12 | 8 | 8 | Murs porteurs (détail géométrique) |
| `020_cloi` | À TRANCHER | 4 | 255 | 0 | À TRANCHER — cloisons *U* (sup) + blocs plans porteurs (cons) |
| `020_cloisons` | SUPPRIMER | 0 | 2 | 0 | Cloisons — non porteur |
| `030_menuiserie` | SUPPRIMER | 0 | 83 | 0 | Menuiseries — non porteur (PLAN DE PRINCIPE) |
| `040_meubles` | SUPPRIMER | 0 | 160 | 0 | Mobilier — non porteur |
| `050_sols` | SUPPRIMER | 0 | 2 | 0 | Sols / revêtements — non porteur |
| `051_plafonds` | SUPPRIMER | 0 | 6 | 0 | Plafonds — non porteur |
| `060_repères murs` | CONSERVER | 1 | 0 | 0 | Repères murs (marqueurs de cloisons) |
| `070_trait-fin` | À TRANCHER | 4 | 169 | 2 | Finitions — NORD conservé (orientation), reste supprimé |
| `075_cotation` | SUPPRIMER | 0 | 104 | 0 | Cotations — non porteur (PLAN DE PRINCIPE) |
| `075_cotation détails` | SUPPRIMER | 0 | 49 | 0 | Cotations détaillées — non porteur |
| `077_textes-1` | SUPPRIMER | 0 | 133 | 0 | Textes — non porteur |
| `078_textes-2` | SUPPRIMER | 0 | 339 | 0 | Textes — non porteur |
| `078_textes-3` | SUPPRIMER | 0 | 43 | 0 | Textes — non porteur |
| `079_textes-4` | SUPPRIMER | 0 | 16 | 0 | Textes — non porteur |
| `080_plomb-cvc` | SUPPRIMER | 0 | 70 | 0 | Fluides (plomberie/CVC) — non porteur |
| `090_repères-axes` | À TRANCHER | 6 | 3 | 3 | Axes / zones chantier — repère structurel |
| `092_surfaces projet` | SUPPRIMER | 0 | 13 | 13 | Surfaces projet (trames) |
| `100 TEXTE PMR` | SUPPRIMER | 0 | 62 | 0 | Texte PMR — non porteur |
| `102_demol` | CONSERVER | 22 | 0 | 0 | Démolition — état projet |
| `31_sanitaires` | SUPPRIMER | 0 | 4 | 0 | Sanitaires — non porteur |

**Total** : 1582 entités source → 57 conservées, 1525 supprimées
**Suppression spatiale (zone milieu)** : 29 entités

## Entités supprimées par le filtre spatial (zone milieu X[65.64, 115.64])

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

## Blocs INSERT conservés

| Bloc | Calque | Position RSU (m) | Zone | Justification |
|---|---|---|---|---|
| Plan existant mi geometre rdc | 020_cloi | (48.57, 41.44) | EXISTANT | Plan RDC existant — géométrie porteuse |
| NORD | 070_trait-fin | (34.58, 42.23) | EXISTANT | Fléche nord — orientation (repère) |
| R+1 Existant | 020_cloi | (32.09, 10.26) | EXISTANT | Plan R+1 existant — géométrie porteuse |
| NORD | 070_trait-fin | (26.84, 3.72) | EXISTANT | Fléche nord — orientation (repère) |
| Murs porteurs selon geometre projet | 020_cloi | (179.86, 41.44) | DEMOL | Murs porteurs selon géométrie projet |
| R+1 Projet | 020_cloi | (163.38, 10.26) | DEMOL | Plan R+1 projet — géométrie porteuse |
| NORD | 070_trait-fin | (165.87, 42.23) | DEMOL | Fléche nord — orientation (repère) |
| NORD | 070_trait-fin | (158.13, 3.72) | DEMOL | Fléche nord — orientation (repère) |

## Limites (V4 — pas de redessin)

- Les blocs plans « mi géomètre » contiennent murs + mobilier + textes : impossible de filtrer sans redessin (verrou V2).
- Le mobilier/textes à l'intérieur des blocs plans est conservé — limitation déclarée.
- Le calage est celui de B-30 (RSU, m). Aucun ajustement visuel (V4).
- Le filtre spatial V2 supprime la zone milieu (bâtiment non Flora) mais ne redessine pas les blocs.
