# Affaire GARENNE — 58 rue de l'Aigle, 92250 La Garenne-Colombes

Études d'exécution Gros Œuvre & Structure — réhabilitation lourde, reprises en
sous-œuvre (RSO) D1 à D6, extension en façade avant.

## Découpage séquentiel (STOP & GO)

| Tâche | Contenu | Livrables | Statut |
|---|---|---|---|
| **1** | Analyse Vision/DXF, note d'hypothèses, note méthodologique | `DOC-01`, `DOC-02` (.docx + .pdf) | ✅ **livrée** |
| 2 | Calculs structurels Python, note de calculs et avant-métré | `DOC-03` (.docx + .pdf) | ⏸ en attente de GO |
| 3 | Plans généraux d'exécution au 1/50 | `PL-01` à `PL-03` (.dxf + .pdf A3) | ⏸ |
| 4 | Détails de ferraillage BA et d'assemblages métalliques | `PL-04`, `PL-05` | ⏸ |

## Contenu du dossier

```
affaires/GARENNE/
├── 00_SOURCES/
│   ├── extract_dxf.py            # extraction géométrique du DXF AARKA
│   └── geometrie_dxf.json        # données extraites (cotes, NGF, murs, démolitions)
└── 01_TACHE_1/
    ├── common_doc.py             # moteur DOCX + PDF (A4 ISO, charte BET)
    ├── make_figures.py           # extraits des planches PDF AARKA
    ├── make_schemas.py           # figures schématiques tracées depuis le DXF
    ├── make_doc01.py             # DOC-01 — Note d'hypothèses
    ├── make_doc02.py             # DOC-02 — Note méthodologique & phasage
    ├── DOC-01_Note_Hypotheses.docx / .pdf        (11 pages)
    ├── DOC-02_Note_Methodologique_Phasage.docx / .pdf  (13 pages)
    └── figures/
        ├── fig05_reperage_rdc.png       # plan RDC + repères D1 à D6
        ├── fig06_coupe_principe.png     # coupe verticale, altimétrie NGF
        ├── fig07_extension_plan.png     # plan coté de l'extension
        └── fig08_phasage_gantt.png      # diagramme de phasage
```

## Reproduire les livrables

```bash
python -m venv venv_auto && ./venv_auto/bin/pip install ezdxf python-docx reportlab pymupdf matplotlib numpy
./venv_auto/bin/python affaires/GARENNE/01_TACHE_1/make_schemas.py
./venv_auto/bin/python affaires/GARENNE/01_TACHE_1/make_doc01.py
./venv_auto/bin/python affaires/GARENNE/01_TACHE_1/make_doc02.py
```

Les sources brutes (DXF 16 Mo et dossier PDF) sont téléchargées depuis le
dossier Google Drive « Garenne » et **ne sont pas versionnées** (dossier
`google_drive/` ignoré, cf. `.gitignore`). Les scripts attendent ces fichiers
à cet emplacement.

## Données géométriques de référence

* **Unités CAO** : `$INSUNITS = 5` → centimètres. Cote `803` = 8,03 m.
* **Point de référence** : NGF 41,46 = axe niveau RDC intérieur (Y = −7234,6 cm).
* **Niveaux** : terrain 41,11 · RDC 41,46 · S/Sol 39,26 · PH RDC 44,08 ·
  R+1 44,32 · PH R+1 46,94 · Combles 47,14 · gouttière 47,47 · faîtage 50,16 ·
  acrotère terrasse 44,75 · assise des fondations 39,02.

### Reprises en sous-œuvre

| Rep. | Localisation | Portée | Ép. mur | Hauteur libre |
|---|---|---|---|---|
| D1 | Refend entrée/bureau (zone non excavée) | 2,60 m | 16 cm | 2,62 m |
| D2 | Façade avant — salon (3 travées) | 3,80 m | 47 cm | 2,15 m |
| D3 | Refend central longitudinal (poêle) | 3,55 m | 57 cm | 2,40 m |
| D4 | Façade avant — salle à manger | 2,00 m | 49 cm | 2,15 m |
| D5 | Refend transversal salle à manger/cuisine | 3,08 m | 16 cm | 2,40 m |
| D6 | Façade arrière — cuisine | 1,54 m | 46 cm | 2,15 m |

Extension : 8,03 × 3,20 m ; poutre retroussée portée 8,03 m ; poteau BA 25 × 25
à 1,19 m du nu de la façade ; deux puits descendus à NGF 39,02.
