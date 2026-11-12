# StructAI

Application personnelle **locale** de conception structurelle assistée par IA
(bâtiments courants en béton armé, France), conforme au cahier des charges
« StructAI » : pipeline en 10 phases, calculs normatifs Eurocodes + Annexes
Nationales FR, traçabilité complète, **IA en ligne exclusivement via
Anthropic (Claude Opus) et OpenAI (ChatGPT/GPT)** — aucun autre fournisseur
n'est activable (contrainte codée en dur).

> ⚠️ **Usage** : outil d'aide à la conception pour ingénieur/étudiant
> francophone. Les livrables sont des **propositions** à vérifier et valider
> par un ingénieur habilité. L'application ne produit ni document signé, ni
> garantie réglementaire, ni dossier de permis, ni certification.

## Démarrage

```bash
./start.sh              # venv + dépendances + build web + lancement
# ou, environnement déjà prêt :
pip install -r requirements.txt
cd web && npm install && npm run build && cd ..
python -m structai      # http://localhost:8000 (port suivant si occupé)
```

Le lancement ouvre le navigateur ; le test d'acceptation « Backend connecté »
est visible via `/api/ping`. **Hors appels IA, l'application ne sort jamais du
réseau local** (pas de télémétrie, pas de cloud).

## Pipeline (10 phases, 5 points de contrôle humains)

1. **Accueil** — feux verts fournisseurs, budget IA, projets récents.
2. **Projet** — identité, localisation (commune/adresse **jamais** envoyées à
   l'IA, déduction des zones sismicité/neige/vent), typologie R+n, matériaux,
   normes (EC0/EC1-1-2-8 + AN FR cochables), paramètres de calcul, critères de
   génération et seed.
3. **Import DXF** — extension/taille (≤100 Mo)/version (R12→R2018), copie
   horodatée + SHA-256, contrôle « filet de sécurité » des textes/images/
   cartouche/nom de fichier (alertes **non bloquantes**, mode strict
   optionnel). *L'anonymisation en amont reste votre responsabilité.*
4. **Parsing local** — entités/calques/unités, rendu PNG 300 DPI, version
   nettoyée (annotations/cartouche exclus) pour l'IA, filtrage calques,
   alerte > 500 000 entités.
5. **Interprétation IA de vision** — estimation de coût + aperçu +
   confirmation explicite avant envoi ; sortie JSON stricte (bâtiment, murs
   porteurs, ouvertures, incertitudes) validée par schéma ; retry + bascule
   de fournisseur ; **saisie manuelle possible (mode dégradé)**.
6. **Validation/correction obligatoire** — superposition des détections sur
   le plan, corrections horodatées *avec raison obligatoire*, bloc de
   validation ; sans validation, la génération reste bloquée.
7. **Génération d'options** — exploration déterministe locale (seed), 3–5
   options **toutes calculées et conformes** (sinon diagnostic), IA créative
   facultative nourrie uniquement du **JSON abstrait** (jamais du plan) ;
   annulation en cours de route, journal live.
8. **Comparateur** — vignettes, tri par colonne, filtres de conformité,
   bouton « Retenir ».
9. **Éditeur structurel** — 2D zoom/pan/grille + isométrie ; déplacer /
   ajouter / supprimer des éléments, sections, recalcul complet à chaque
   édition, Ctrl+Z, alerte rouge de non-conformité, **« Figer cette
   version »** = snapshot ZIP immuable.
10. **Livrables** — plans DXF (fondations, coffrage, ferraillage ; AC2013,
    mm, calques figés), note de calcul PDF en 11 sections (les sections
    narratives peuvent être rédigées par l'IA depuis un JSON local, alors
    marquées « assistance IA »), quantitatifs CSV/XLSX (béton m³, acier kg
    long+transversal, coffrage m²), aperçu avant export, **rapport de
    traçabilité** complet.

## Moteur de calcul

* Assemblage **PyNite** (FEM 3D) : portiques + voiles, charges EC1 + AN FR
  (poids propre, revêtements 1.5 kN/m², cloisons 0.8, exploitation, neige,
  vent, séisme statique équivalent ag·γI·sol), combinaisons ELU/ELS
  (caract./quasi-perm.) + accidentelles ; repli analytique si solveur KO.
* Vérifications EC2 : flexion, effort tranchant, flambement (second ordre
  simplifié), flèche, fissuration, dispositions constructives ; EC8 :
  hiérarchie des efforts, capacité des voiles, dérives. Chaque vérification
  journalise `{élément, vérification, combinaison, sollicitation, capacité,
  taux, statut}` — taux > 1.0 ⇒ **non_conforme**.
* Béton C25/30, aciers B500B par défaut (éditables). Notations « 4HA20 »,
  « HA8 e=15 » dans plans et note.

*Auto-validation* : tests pytest — poutre isostatique à ±2 % du calcul à la
main, reproductibilité par seed, DXF relu par ezdxf, totaux quantitatifs,
PDF non vides :

```bash
python -m pytest            # ~1 min (FE) ; python -m pytest -m "not slow" sinon
```

## Sécurité & RGPD (résumé du §5)

* **Anonymisation en amont par l'utilisateur** — l'app est un filet de
  sécurité (scan TEXT/MTEXT mots-clés, IMAGE/OLE, cartouche, nom de fichier),
  pas une machine à anonymiser.
* Aucun secret en clair : clés API dans le **trousseau système** (keyring,
  repli fichier 0600 + avertissement jamais loggé) ; mots de passe local +
  session 30 min ; écoute localhost uniquement (0.0.0.0 seulement pour la
  démo via `STRUCTAI_HOST`).
* Les réponses IA **ne sont jamais stockées en clair** : journal `ai_calls`
  avec horodatage UTC, fournisseur, modèle, finalité, tokens, coût et
  **hashs SHA-256 tronqués** requête/réponse.
* Plafonds de dépense (jour / projet), mode paranoïaque (bloque tout envoi
  sans confirmation), vérification des engagements ZDR/no-training déclarés.
* Suppression définitive par projet avec **saisie du nom exact** ; purge
  automatique des snapshots > 90 j au lancement (les figeages sont
  conservés) ; journaux conservés 3 ans.
* Registre des traitements + modèle d'accord client générables en PDF
  (écran Paramètres). SQLCipher : option prévue au lot 7, non activée.

## Architecture

```
structai/
  api.py            routes FastAPI + montage du build React + session
  __main__.py       port 8000 (suivant si occupé), navigateur, purge au lancement
  config.py         paramètres persistés (settings.json) + ALLOWED_PROVIDERS
  security.py       keyring, mot de passe local, sessions, journal d'accès
  db.py             SQLite (projects, plans, interpretations, options, edits,
                    deliverables, ai_calls, alerts, incidents, snapshots, access_log)
  projects.py       CRUD, snapshots ZIP, purge, alertes/incidents
  tasks.py          jobs de fond (progression/cancel pour génération & livrables)
  parsing/dxf.py    import contrôlé, lecture ezdxf, rendu PNG, scan anti-PII
  calc/             codes EC2/EC8 AN FR, sections, modèle FEM, engine
  gen/generator.py  espace d'exploration déterministe + classement + seeds
  ai/               providers (Anthropic/OpenAI uniquement), schemas JSON,
                    orchestrator (prompts YAML, retry/fallback, budget, journal),
                    prompts/*.yaml éditables
  export/           dxf_plans (fondations/coffrage/ferraillage), quantities
                    (CSV/XLSX), pdf_docs (note, traçabilité, accord client,
                    registre)
  visu.py           rendus PNG/SVG (vignettes, iso)
web/src/            React (Vite) — build servi par FastAPI (web/dist)
tests/              pytest — moteur, génération, exports, flux API complet
```

## Limitations connues (volontaires, cf. cahier)

Calcul préliminaire (poutres sur 2 appuis + FEM portiques, voiles en
cisaillement), pas de descente de charges fine ni d'interaction sol-structure,
pas de PSMT/computation sismique modale, un seul matériau (BA), pas de
signature électronique ni d'hébergement multi-utilisateurs. Les valeurs
normatives codées sont indicatives et éditables dans `structai/calc/codes.py`
— la responsabilité du dimensionnement reste à l'ingénieur.

## Affaire GARENNE — 58 rue de l'Aigle, 92250 La Garenne-Colombes

Dossier d'étude structurelle de la réhabilitation de la maison en meulière :
RSO D1 à D6 et extension en façade avant. Les documents et scripts sont dans
`affaires/GARENNE/`.

| Tâche | Livrables | État |
|---|---|---|
| 1 — hypothèses et méthode | DOC-01, DOC-02 (DOCX + PDF, 13 p. chacun) | Révisés selon E-02 |
| 2 — calculs et métrés | DOC-03 (DOCX + PDF, 13 p.), `calculs.py`, résultats JSON | Générés |
| 3 — plans généraux | PL-01 à PL-03 (DXF + PDF A3) | Générés |
| 4 — détails | PL-04 et PL-05 (DXF + PDF A3, 2 planches chacun) | Révisés selon E-02 |

### Arbitrage E-02 retenu

E-01 (poteau à 2,00 m, voile mitoyen existant et poutre 4 HA 20) est caduc.
Le parti d'extension retenu est : terrasse 8,03 × 2,00 m, poteau BA 25 × 25
à 1,30 m du nu de façade, poutre perpendiculaire 25 × 67 cm avec travée de
1,30 m et console de 0,70 m, poutre-acrotère de rive 30 × 67 cm isostatique sur
8,03 m, dalle BA 20 cm portée sur 1,70 m, voile de rive BA neuf de 20 cm sur
semelle filante 65 × 30 cm. Le voile est claveté au pignon existant ; il ne
s'agit pas d'un mur mitoyen existant.

Calculs de référence : poutre de rive 4 HA 14 et étriers HA 8 e = 300 mm
(M<sub>ELU</sub> = 140,3 kN·m, V<sub>ELU</sub> = 69,9 kN, flèche LT
22,48 mm, contre-flèche 20 mm) ; poutre perpendiculaire 2 HA 12 ; dalle
4 HA 10 ; poteau 6 HA 8 ; voile 4 HA 12 par face et HA 8 e = 250 mm. Puits
n° 1 Ø 1,35 m et n° 2 Ø 1,75 m, profondeur de calcul 2,40 m, arase NGF 39,02.
Les détails d'appui du voile et l'interface appui glissant / joint vertical
20 mm restent à coordonner et à valider par le BET avant exécution.

### Contenu et régénération

- `00_SOURCES/` : niveaux retenus et données DXF extraites.
- `01_TACHE_1/` : DOC-01, DOC-02 et figures.
- `02_TACHE_2/` : calculs, figures et DOC-03.
- `03_TACHE_3/` : moteur DXF/PDF (`plan_engine.py`), plans PL-01 à PL-05,
  bibliothèque de détails (`detail_lib.py`). Les DXF sont en centimètres
  (`$INSUNITS = 5`) et utilisent les calques `STR_*`.

```bash
./venv_auto/bin/python affaires/GARENNE/02_TACHE_2/calculs.py
./venv_auto/bin/python affaires/GARENNE/02_TACHE_2/make_figures.py
./venv_auto/bin/python affaires/GARENNE/02_TACHE_2/make_doc03.py
./venv_auto/bin/python affaires/GARENNE/01_TACHE_1/make_doc01.py
./venv_auto/bin/python affaires/GARENNE/01_TACHE_1/make_doc02.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl01.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl02.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl03.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl04.py
./venv_auto/bin/python affaires/GARENNE/03_TACHE_3/make_pl05.py
```

Les sources graphiques AARKA originales sont externes au dépôt et doivent être
présentes sous `google_drive/` pour régénérer les plans dépendant du fond DXF.
Les plans d'exécution restent soumis aux sondages et points d'arrêt listés dans
DOC-02/DOC-03 ; leur production ne vaut pas autorisation de travaux.
