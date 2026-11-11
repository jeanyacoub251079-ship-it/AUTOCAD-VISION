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

Réhabilitation lourde d'une maison en meulière : reprises en sous-œuvre
RDC D1 à D6, extension en façade avant (salon d'été + terrasse accessible)
et modification des combles Mansart. Livrables du BET dans `affaires/GARENNE/`.

| Tâche | Contenu | Livrables | État |
|---|---|---|---|
| 1 | Reconnaissance DXF + hypothèses | `DOC-01` (note d'hypothèses), `DOC-02` (méthodologie & phasage) | ✅ livrée |
| 2 | Calculs + métrés | `DOC-03` (note de calculs, 13 p.) + `calculs.py` | ✅ livrée |
| 3 | Plans généraux 1/50 | `PL-01`, `PL-02`, `PL-03` (.dxf + .pdf) | ✅ livrée |
| 4 | Détails 1/20 & 1/10 | `PL-04`, `PL-05` | ⏸ après GO |

### Organisation

```
affaires/GARENNE/
  00_SOURCES/   niveaux_retenus.py (source unique des NGF et de la position
                du poteau), geometrie_dxf.json, planches AARKA (Drive)
  01_TACHE_1/   common_doc.py (moteur DOCX/PDF), make_doc01.py, make_doc02.py,
                make_schemas.py, make_figures.py, DOC-01*, DOC-02*, figures/
  02_TACHE_2/   calculs.py (moteur EC0→EC7), make_doc03.py, make_figures.py,
                calculs_resultats.json, DOC-03*, figures/
  03_TACHE_3/   plan_engine.py (géométrie -> DXF + PDF), detail_lib.py,
                make_pl01..05.py, plans/PL-01..PL-05 .dxf et .pdf
```

### Arbitrages du maître d'ouvrage (11/11/2026)

* **E-01** — le poteau BA 25 × 25 de la verrière est **déplacé à 2,00 m du nu
  de la façade, sous la poutre** ; il en devient l'appui d'extrémité.
* **H-06 / H-18** — forfait charpente 250 kg/m² et charges de verrière
  acceptés tels quels.
* **H-16** — trappe à linge estimée depuis les plans, à entourer d'un
  **nuage de révision** sur les plans d'exécution.
* **H-01** — fondation sous D1 en **meulière continue**, conservée.

Sondages restant à lever avant exécution : **H-08, H-09, H-10, H-14, H-15**.

### Résultats clés de la Tâche 2

* Reprises D1–D6 : IPE 160 à IPE 300 en **S355**, taux de flexion 0,554 à
  0,880, flèches ≤ 0,05 mm.
* **Poutre-acrotère BA 30 × 67 cm**, arase NGF 44,75, travée unique de
  8,03 m entre le voile mitoyen et le poteau à 2,00 m ; M<sub>ELU</sub> =
  262,6 kN·m, **4 HA 20** + étriers HA 8 e = 175 mm ; flèche à long terme
  17,55 mm (L/458) → **contre-flèche de coffrage de 20 mm**.
* Voile mitoyen 20 cm : K<sub>0</sub> = 0,50, M = 29,23 kN·m/ml,
  **4 HA 12** par face, V<sub>Ed</sub> ≤ V<sub>Rd,c</sub>.
* Puits Ø 2,05 / 2,20 m à −2,40 m : σ<sub>ELS</sub> = 0,100 / 0,099 MPa
  (marge 1 à 2 % sur le seuil de 0,10 MPa — point sensible).
* Avant-métré : 19,79 m³ de béton armé, 2,37 t d'aciers HA, 0,45 t de
  profilés, 17,04 m³ de terrassement, 48 étais.

### Plans d'exécution (Tâche 3)

* **PL-01** — reprise en sous-œuvre RDC : existant, démolitions D1 à D6,
  jambages/sommiers BA, profilés S355, trappes au nuage de révision (1/50).
* **PL-02** — coffrage de l'extension : voile mitoyen, poteau à 2,00 m,
  poutre-acrotère 30 × 67, puits et longrines (1/50).
* **PL-03** — coupe A-A sur la terrasse (1/50) + détail d'appui 1/20.
* **PL-04** — ferraillage de la poutre-acrotère (coupes 1/10, schéma des
  étriers), du poteau, de la dalle + nomenclature des aciers (2 planches).
* **PL-05** — assemblages acier/BA : appuis de profilés sur jambages et
  sommiers, encastrement en meulière, appui glissant de la poutre-acrotère,
  ancrage de la dalle, clavetage du voile (2 planches).

A3 paysage, cartouche BET, calques `STR_*`. Un seul moteur (`plan_engine.py`)
produit le .dxf **et** le .pdf depuis la même géométrie.

### Régénérer les livrables

```bash
./venv_auto/bin/python affaires/GARENNE/02_TACHE_2/calculs.py    # résultats
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
