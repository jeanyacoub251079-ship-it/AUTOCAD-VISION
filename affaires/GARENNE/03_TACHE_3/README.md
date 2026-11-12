# Tâches 3 et 4 — PL-01 à PL-05

Affaire GA-2026-58AIGLE — 58 rue de l'Aigle, La Garenne-Colombes.
Les plans d'extension PL-02 à PL-05 suivent l'arbitrage E-02 ; PL-04/PL-05
sont à l'indice B (révision 12/11/2026).

| Plan | Contenu | Échelle | Livrables |
|---|---|---|---|
| PL-01 | RSO RDC : démolitions D1–D6, jambages/sommiers, profils S355, trappes H-16 | 1/50 | PDF + DXF |
| PL-02 | Coffrage extension 8,03 × 2,00 m, poteau à 1,30 m, console 0,70 m, voile de rive neuf | 1/50 | PDF + DXF |
| PL-03 | Coupes, altimétrie NGF, appui du poteau et voile sur semelle | 1/40, 1/50, 1/60 | PDF + DXF |
| PL-04 | Ferraillage : poutre 4 HA 14, poutre perpendiculaire, dalle, poteau, puits et nomenclature | 1/10–1/40 | PDF 2 pages + DXF |
| PL-05 | Appuis RSO ; extension E-02 : voile neuf, console, appui glissant de dalle, clavetage au pignon | 1/12–1/40 | PDF 2 pages + DXF |

## Géométrie E-02

Terrasse BA de 8,03 × 2,00 m ; poutre-acrotère de rive 30 × 67 cm,
isostatique, 4 HA 14 + étriers HA 8 e = 300 mm. Poteau 25 × 25 cm à 1,30 m
du nu de façade ; poutre perpendiculaire 25 × 67 cm avec console de 0,70 m.
Le voile de rive BA ép. 20 cm est à créer, claveté au pignon existant et posé
sur semelle filante 65 × 30 cm. Puits : Ø 1,35 m et Ø 1,75 m, profondeur de
calcul 2,40 m, arase NGF 39,02.

Sur PL-05/2, la dimension et le type de l'appareil d'appui du voile sont
laissés à valider. L'interface de l'appui glissant de la dalle avec le joint
vertical de 20 mm, l'étanchéité et la menuiserie doit être coordonnée avant
exécution.

## Génération

`plan_engine.py` produit PDF et DXF à partir des mêmes scènes ; `detail_lib.py`
contient les cotes et symboles de ferraillage. DXF R2013 en centimètres
(`$INSUNITS = 5`), calques `STR_EXISTANT`, `STR_DEMOLITION`,
`STR_COFFRAGE_BA`, `STR_ACIER_PROFILS`, `STR_FERRAILLAGE` et
`STR_COTATIONS_TEXTES`.

```bash
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl01.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl02.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl03.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl04.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl05.py
```

Les longueurs d'ancrage/recouvrement et dispositions d'appui notées
« indicatives » ou « à valider » ne constituent pas des plans de façonnage
validés pour commande.
