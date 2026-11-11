# Tâches 3 et 4 — Plans d'exécution (PL-01 à PL-05)

Affaire GA-2026-58AIGLE — 58 rue de l'Aigle, 92250 La Garenne-Colombes
BET Structure — Indice A — 11/11/2026

## Livrables

| Plan | Objet | Échelle | Fichiers |
|---|---|---|---|
| **PL-01** | Reprise en sous-œuvre RDC : existant conservé, démolitions D1 à D6, jambages/sommiers BA, profilés S355, trappes à linge au nuage de révision | 1/50 | `plans/PL-01_Reprise_Sous_Oeuvre_RDC.dxf` / `.pdf` |
| **PL-02** | Plan de coffrage de l'extension : voile mitoyen, poteau BA à 2,00 m, poutre-acrotère 30 × 67, puits de gros béton, longrines, dalle | 1/50 | `plans/PL-02_Coffrage_Extension.dxf` / `.pdf` |
| **PL-03** | Coupes et élévations : coupe A-A sur la terrasse (altimétrie NGF) + détail d'appui poutre/poteau | 1/50 et 1/20 | `plans/PL-03_Coupes_Elevations.dxf` / `.pdf` |
| **PL-04** | Ferraillage (2 planches) : coupes A-A/B-B de la poutre, schéma des étriers, poteau, dalle, façonnage, nomenclature | 1/10 et 1/20 | `plans/PL-04_Ferraillage_Details.dxf` / `.pdf` |
| **PL-05** | Assemblages acier/BA (2 planches) : appuis sur jambage/sommier, encastrement meulière, jonction poteau, appui glissant voile, ancrage dalle, clavetage | 1/10 | `plans/PL-05_Assemblages_Acier_BA.dxf` / `.pdf` |

Format ISO A3 paysage (420 × 297 mm), cartouche BET, calques normalisés.

## Principe de génération

`plan_engine.py` décrit **une seule fois** la géométrie de chaque plan
(primitives `line`, `rect`, `poly`, `circle`, `arc`, `text`, `dim_h`, `dim_v`,
`leader`), puis la rend par deux back-ends :

* `DxfBackend` — ezdxf, DXF R2013, `$INSUNITS = 5` (centimètres) ;
* `PdfBackend` — reportlab, feuille A3 en millimètres, échelle exacte.

Le `.dxf` et le `.pdf` sont donc **strictement identiques** : aucune
divergence possible entre les deux fichiers livrés.

Les trois scripts `make_pl01.py`, `make_pl02.py`, `make_pl03.py` ne
contiennent que le contenu métier (géométrie, cotes, notes).

## Calques normalisés (cahier des charges)

| Calque | Couleur ACI | Épaisseur | Type de ligne | Usage |
|---|---|---|---|---|
| `STR_EXISTANT` | 7 (blanc) | 0,18 mm | continu | existant conservé |
| `STR_DEMOLITION` | 1 (rouge) | 0,25 mm | tirets | maçonneries démolies |
| `STR_COFFRAGE_BA` | 6 (magenta) | 0,50 mm | continu | coffrage béton armé + hachures |
| `STR_ACIER_PROFILS` | 6 (magenta) | 0,50 mm | continu | profilés S355 |
| `STR_FERRAILLAGE` | 6 (magenta) | 0,40 mm | continu | armatures |
| `STR_COTATIONS_TEXTES` | 7 (blanc) | 0,25 mm | continu | cotes, axes, textes ≥ 2,5 mm |

## Sources de vérité

* `../00_SOURCES/niveaux_retenus.py` — niveaux NGF et `POS_POTEAU_FAÇADE = 2,00 m` ;
* `../00_SOURCES/rdc_plan.json` — fond de plan RDC extrait du DXF AARKA
  (258 lignes + 97 polylignes, calques `ARK-MURS` / `ARK-CLOIS` / `ARK-VITRE`) ;
* `../02_TACHE_2/calculs_resultats.json` — sections, ferraillages et profilés.

## Régénérer

```bash
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl01.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl02.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl03.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl04.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl05.py
```

PL-04 et PL-05 sont des **jeux de 2 planches** (un seul `.pdf` multi-pages,
un seul `.dxf` regroupant les cadres).

`detail_lib.py` contient les symboles de détail : flèches pleines, hachures
polygonales, cotes adaptées aux grandes échelles, étriers, barres avec
crochets, sections de barres, lignes de rupture.

## Points de vigilance reportés

1. **Trappes à linge (H-16)** : position estimée depuis les plans et entourée
   d'un nuage de révision sur PL-01. Le relevé de l'entraxe réel des solives
   reste à faire avant tracé définitif (DOC-02 §6.3).
2. **Contre-flèche de 20 mm** de la poutre-acrotère : prescrite sur PL-02 et
   PL-03, à contrôler à la pose des étais.
3. **Sondages H-08, H-09, H-10, H-14, H-15** : non bloquants pour les plans,
   nécessaires avant exécution.
