# Affaire GARENNE — 58 rue de l'Aigle

Dossier structure de la réhabilitation lourde et de l'extension en façade
avant. État documentaire : DOC-01 à DOC-03 et PL-01 à PL-05 générés ; PL-04 et
PL-05 sont révisés pour le parti E-02. Ce statut ne vaut pas autorisation
d'exécution des travaux.

## STOP & GO

| Étape | Contenu | État |
|---|---|---|
| 1 | Hypothèses et méthodologie | DOC-01 / DOC-02 révisés, 13 p. chacun |
| 2 | Calculs et métrés | DOC-03, 13 p. |
| 3 | Plans généraux | PL-01 à PL-03, PDF + DXF |
| 4 | Détails | PL-04 / PL-05, PDF + DXF, 2 pages chacun |

Avant le GO chantier : lever les sondages H-08, H-09, H-10, H-14 et H-15 ;
valider les points d'arrêt géotechniques ; définir l'appareil d'appui du voile
neuf et coordonner l'appui glissant de la dalle avec le joint vertical de
20 mm, l'étanchéité et la menuiserie.

## Parti E-02 retenu

- Terrasse : 8,03 × 2,00 m (poutre-acrotère comprise) ; dalle BA 20 cm,
  portée de 1,70 m jusqu'au nu intérieur de la poutre.
- Poteau BA 25 × 25 à 1,30 m du nu de façade ; poutre perpendiculaire
  25 × 67 cm, portée 1,30 m et console 0,70 m.
- Poutre-acrotère de rive 30 × 67 cm, isostatique sur 8,03 m ; 4 HA 14,
  étriers HA 8 e = 300 mm, contre-flèche 20 mm.
- Appui droit sur un voile BA de rive de 20 cm à créer, claveté au pignon
  existant et fondé sur semelle filante 65 × 30 cm. Aucune maçonnerie
  mitoyenne existante ne sert d'appui.
- Puits de gros béton C16/20 : Ø 1,35 m et Ø 1,75 m, profondeur calculée
  2,40 m, arase NGF 39,02.

## Organisation

- `00_SOURCES/` : données de référence, dont `niveaux_retenus.py`.
- `01_TACHE_1/` : moteur documentaire, DOC-01, DOC-02 et figures.
- `02_TACHE_2/` : calculs, résultats JSON, DOC-03 et figures.
- `03_TACHE_3/` : `plan_engine.py`, `detail_lib.py`, scripts PL-01 à PL-05
  et fichiers livrables dans `plans/`.

Régénérer les plans avec les commandes du README racine. DXF en cm
(`$INSUNITS = 5`), PDF en A3 paysage. Les détails signalés « à valider » dans
PL-05/2 doivent être confirmés avant exécution.
