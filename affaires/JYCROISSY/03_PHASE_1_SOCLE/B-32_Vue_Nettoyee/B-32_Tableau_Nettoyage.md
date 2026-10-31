# B-32 — Tableau de nettoyage — SOCLE-GEOS V1

**Source** : `B-30_FLORA_RSU_calé_v1.dxf` (DXF calé V1)  
**Livrable** : SOCLE-GEOS (plan de principe / socle géométrique)  
**Mode** : COMPLET  

## Calques

| Calque | Statut | Conservé | Supprimés | Justification |
|---|---|---|---|---|
| `0` | À TRANCHER | 11 | 1 | Géométrie bâtiment (contour, axes) — non porteur explicite, conservé pour trame |
| `010_mur` | CONSERVER | 20 | 0 | Murs porteurs (détail géométrique) |
| `020_cloi` | À TRANCHER | 4 | 255 | À TRANCHER — cloisons *U* (sup) + blocs plans porteurs (cons) |
| `020_cloisons` | SUPPRIMER | 0 | 2 | Cloisons — non porteur |
| `030_menuiserie` | SUPPRIMER | 0 | 83 | Menuiseries — non porteur (PLAN DE PRINCIPE) |
| `040_meubles` | SUPPRIMER | 0 | 160 | Mobilier — non porteur |
| `050_sols` | SUPPRIMER | 0 | 2 | Sols / revêtements — non porteur |
| `051_plafonds` | SUPPRIMER | 0 | 6 | Plafonds — non porteur |
| `060_repères murs` | CONSERVER | 1 | 0 | Repères murs (marqueurs de cloisons) |
| `070_trait-fin` | À TRANCHER | 6 | 167 | Finitions — NORD conservé (orientation), reste supprimé |
| `075_cotation` | SUPPRIMER | 0 | 104 | Cotations — non porteur (PLAN DE PRINCIPE) |
| `075_cotation détails` | SUPPRIMER | 0 | 49 | Cotations détaillées — non porteur |
| `077_textes-1` | SUPPRIMER | 0 | 133 | Textes — non porteur |
| `078_textes-2` | SUPPRIMER | 0 | 339 | Textes — non porteur |
| `078_textes-3` | SUPPRIMER | 0 | 43 | Textes — non porteur |
| `079_textes-4` | SUPPRIMER | 0 | 16 | Textes — non porteur |
| `080_plomb-cvc` | SUPPRIMER | 0 | 70 | Fluides (plomberie/CVC) — non porteur |
| `090_repères-axes` | CONSERVER | 9 | 0 | Axes / zones chantier — repère structurel |
| `092_surfaces projet` | CONSERVER | 13 | 0 | Surfaces projet (trames) |
| `100 TEXTE PMR` | SUPPRIMER | 0 | 62 | Texte PMR — non porteur |
| `102_demol` | CONSERVER | 22 | 0 | Démolition — état projet |
| `31_sanitaires` | SUPPRIMER | 0 | 4 | Sanitaires — non porteur |

**Total** : 1582 entités source → 86 conservées, 1496 supprimées

## Blocs INSERT conservés

| Bloc | Calque | Position RSU (m) | Justification |
|---|---|---|---|
| Plan existant mi geometre rdc | 020_cloi | (48.57, 41.44) | Plan RDC existant — géométrie porteuse |
| NORD | 070_trait-fin | (34.58, 42.23) | Fléche nord — orientation (repère) |
| R+1 Existant | 020_cloi | (32.09, 10.26) | Plan R+1 existant — géométrie porteuse |
| NORD | 070_trait-fin | (26.84, 3.72) | Fléche nord — orientation (repère) |
| R+1 Projet | 0 | (97.73, 10.26) | Plan R+1 projet — géométrie porteuse |
| Murs porteurs selon geometre projet | 020_cloi | (179.86, 41.44) | Murs porteurs selon géométrie projet |
| R+1 Projet | 020_cloi | (163.38, 10.26) | Plan R+1 projet — géométrie porteuse |
| NORD | 070_trait-fin | (92.49, 3.72) | Fléche nord — orientation (repère) |
| NORD | 070_trait-fin | (165.87, 42.23) | Fléche nord — orientation (repère) |
| NORD | 070_trait-fin | (158.13, 3.72) | Fléche nord — orientation (repère) |
| Murs porteurs selon geometre projet | 0 | (114.22, 41.44) | Murs porteurs selon géométrie projet |
| NORD | 070_trait-fin | (100.22, 41.26) | Fléche nord — orientation (repère) |

## Limites (V4 — pas de redessin)

- Les blocs plans « mi géomètre » contiennent murs + mobilier + textes : impossible de filtrer sans redessin (verrou V2).
- Le mobilier/textes à l'intérieur des blocs plans est conservé — limitation déclarée.
- Le calage est celui de B-30 (RSU, m). Aucun ajustement visuel (V4).
