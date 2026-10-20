Fichier 04_PHASE_2_CONCEPTION/B-20_Conception_GO.md — CARNAC v3.0
________________


B-20 — CONCEPTION STRUCTURE GO
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-15 (Synthèse des risques) — ou la première brique exécutable selon le PTD |
| Brique suivante | B-21 (DDC préliminaire), B-22 (Note d'hypothèses), B-23 (Exploitation du diagnostic), B-24 (Existant non sondé) |
| Modes d'appel | INTERNE-GO (aucun BET de conception, diagnostic + plans de principe seulement — cas type Flora) · PARTIEL-DÉCLARÉ (BET partiel : on complète ce qui manque, on cite ce qui existe) · SANS OBJET (BET complet fourni : la conception n'est pas à nous) |
| Entrées lues | MPD (AC-03, DOC-03), B-11, B-12, B-23, B-24 (si exécutée), DOC-02 (plans archi), énoncé de mission (B-00) |
| Sortie unique | Dossier de conception : (1) note de prédimensionnement, (2) plans de principe graphiques (DXF + PDF + PNG), (3) liste des points à faire valider par un tiers |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : au début de la phase 2, quand AC-03 (BET structure de conception) est À PRODUIRE PAR GO ou PARTIELLE. En mode SANS OBJET, B-20 est appelée uniquement pour produire une ligne de justification.
Ce que vous fournissez à l'IA : la MPD validée (statut de AC-03 et DOC-03), les audits B-11 et B-12, les sorties de B-23 et B-24 (si disponibles), les plans architecte (DOC-02), l'énoncé de mission. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * la trame structurelle et sa justification par la géométrie archi et les contraintes existantes ;
   * les sections de principe et leur méthode de prédimensionnement (jamais « par expérience ») ;
   * les renforts de l'existant et le désordre qu'ils corrigent (renvoi B-11) ;
   * les plans de principe (filigrane « PRINCIPE — NE PAS EXÉCUTER ») ;
   * la liste des points à faire valider par un tiers.
Ce que B-20 produit — le périmètre exact :

| Élément | Nature | Renvoi |
| --- | --- | --- |
| Trame structurelle (axes, entraxes, positions) | Choix de conception justifié | — |
| Sections de principe des porteurs neufs | Prédimensionnement par ratios et formules | Calculs d'exécution : B-40 à B-50 |
| Nature des renforts de l'existant | Choix de principe | Validation : B-44 à B-50 |
| Plans de principe graphiques | Fond archi + ajouts en couleur | Plans d'exécution : B-60 |
| Note d'hypothèses | Renvoi à B-22 | — |
| Liste des points à faire valider | Sections à confirmer, hypothèses à viser, choix à confirmer | BET, BC, MOE |

Ce que B-20 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Notes de calcul d'exécution (EC2, EC3, EC5, EC7 avec ferraillage détaillé) | B-40 à B-50 |
| Plans d'exécution cotés avec ferraillage | B-60 |
| Nomenclatures et façonnage | B-62 |
| Calage fin et preuve de superposition | B-30, B-31 |
| Dimensionnement de la protection au feu | Hors périmètre CARNAC (mention générique seule) |

________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire le dossier de conception structure GO de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}.


CONTEXTE DU MODE
- INTERNE-GO : aucun BET de conception. Tu produis l'intégralité de la conception à partir des plans architecte, du diagnostic existant (B-11, B-23) et de la géotechnique (B-12).
- PARTIEL-DÉCLARÉ : un BET partiel existe. Tu cites ce qu'il fournit et tu complètes ce qui manque. Tu ne redessines jamais ce que le BET a déjà produit.
- SANS OBJET : un BET complet existe. Tu produis une ligne de justification et tu t'arrêtes — la conception n'est pas à nous.


MÉTHODE
1. Établis la trame structurelle : axes, entraxes, positions des porteurs neufs et des appuis sur l'existant. Justifie chaque position par la géométrie archi et les contraintes existantes (murs porteurs, baies, refends, poutres existantes).
2. Prédimensionne les sections de principe par ratios et formules approchées, en explicitant la méthode utilisée (ex. : poteau BA prédimensionné à A_c ≥ N_Ed/(0,3·f_cd) ; poutre métallique prédimensionnée à h ≈ L/20 en plancher, L/15 en toiture ; semelle à B ≥ N/q_adm). La méthode est TOUJOURS citée ; tu n'inventes aucune section « au feeling ».
3. Identifie les renforts de l'existant nécessaires : moisage, sommier de répartition, entretoise anti-déversement, contrefiche, etc. Justifie chaque choix par le désordre qu'il corrige (renvoi au diagnostic B-11).
4. Produis les plans de principe : plan de trame, plan des porteurs neufs et des renforts, coupes schématiques. Fond archi conservé (pas de redessin de l'empreinte). Ajouts en couleur avec légende. Filigrane « PRINCIPE — NE PAS EXÉCUTER » systématique.
5. Rédige la note de prédimensionnement : hypothèses, formules, sections retenues, ratios utilisés. Chaque section retenue est justifiée par le calcul approché ou par le ratio. Aucune section « par expérience ».
6. Liste les points à faire valider par un tiers : sections à confirmer par calcul d'exécution, hypothèses à viser par BET ou bureau de contrôle, choix constructifs à confirmer par la MOE.


INTERDICTIONS
- Ne produis AUCUN calcul d'exécution (EC2, EC3, EC5, EC7 avec ferraillage détaillé) : tu prédimensionnes, tu ne vérifies pas finement.
- Ne redessine JAMAIS l'empreinte du bâtiment : tu utilises le fond archi (DOC-02) tel qu'il t'est fourni.
- N'invente aucun porteur : tout élément dessiné est rattaché à la géométrie archi, au diagnostic, ou à une contrainte explicitement citée.
- N'utilise aucune section « par expérience », « par habitude », « comme d'usage » : la méthode de prédimensionnement est TOUJOURS citée.
- Ne tranche aucune contradiction entre pièces : si une contradiction bloque la conception, tu la signales et tu suspends la partie concernée.
- Ne dimensionne PAS la protection au feu : tu mentionnes « une protection au feu adéquate doit être prévue » sans autre précision.
- Ne produis aucun plan sans filigrane « PRINCIPE — NE PAS EXÉCUTER ».
- Ne propose aucun mode COMPLET : B-20 est INTERNE-GO ou PARTIEL-DÉCLARÉ.


SORTIE
Pièce 1 — Note de prédimensionnement (document texte, 3 à 10 pages selon complexité) :
Section 1 : Hypothèses de conception (renvoi B-22).
Section 2 : Trame structurelle retenue et justification.
Section 3 : Sections de principe des porteurs neufs (tableau : élément, section retenue, méthode de prédimensionnement, formule, valeur de calcul approchée, ratio de contrôle).
Section 4 : Renforts de l'existant (tableau : élément existant, désordre corrigé, renfort retenu, méthode de prédimensionnement).
Section 5 : Points à faire valider par un tiers (tableau : point, brique CARNAC qui validera, tiers viseur).


Pièce 2 — Plans de principe (DXF + PDF + PNG) :
- Plan de trame ;
- Plan des porteurs neufs et renforts ;
- Coupes schématiques (2 minimum) ;
Tous filigranés « PRINCIPE — NE PAS EXÉCUTER — Indice P ».


Pièce 3 — Liste des points à lever
Points de conception non tranchés à la sortie de B-20 : objet, raison, brique qui tranchera (B-40 à B-50), échéance.


CRITÈRE D'ACCEPTATION
Le dossier est accepté si :
- chaque position de porteur est justifiée par la géométrie archi, le diagnostic ou une contrainte citée ;
- chaque section retenue est justifiée par une méthode de prédimensionnement citée et un calcul approché chiffré ;
- chaque renfort est rattaché au désordre qu'il corrige (référence B-11) ;
- chaque plan porte le filigrane « PRINCIPE — NE PAS EXÉCUTER » et un indice P ;
- aucun calcul d'exécution n'a été produit ;
- aucune protection au feu n'a été dimensionnée ;
- la liste des points à faire valider est complète (sections, hypothèses, choix constructifs).
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}} (par INTERNE-GO, PARTIEL-DÉCLARÉ ou SANS OBJET). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Trois modes (INTERNE-GO / PARTIEL-DÉCLARÉ / SANS OBJET) | B-20 est la brique qui s'active quand le BET de conception est absent — mais elle doit aussi savoir s'effacer quand le BET existe, et compléter quand il est partiel. Un mode unique forcerait B-20 à produire de la conception là où elle n'est pas nécessaire |
| « Tu ne redessines jamais ce que le BET a déjà produit » | En mode PARTIEL-DÉCLARÉ, un modèle a tendance à « refaire » le travail du BET — ce qui introduit des écarts incontrôlés entre le BET et nous. Le respect du travail du BET est une règle de collaboration |
| « La méthode de prédimensionnement est TOUJOURS citée » | Une section retenue sans méthode est une décision non justifiée. La formule approchée (ratio, formule de prédimensionnement) rend la section défendable et reproductible — deux ingénieurs doivent aboutir à la même section |
| « Aucune section "par expérience", "par habitude", "comme d'usage" » | C'est la faille typique d'un modèle qui produit « 20×40 » sans pouvoir le justifier — et qu'on ne peut pas défendre en réunion de chantier. Une section sans méthode est une section qui sera contestée |
| Filigrane « PRINCIPE — NE PAS EXÉCUTER » | Un plan de principe se diffuse toujours, et finit toujours par être lu par quelqu'un qui ne sait pas que c'est un principe. Le filigrane est la seule protection — sans lui, un plan de principe peut être exécuté tel quel |
| « Ne produis aucun calcul d'exécution » | Frontière B-20 / B-40 à B-50 : la conception prédimensionne, l'exécution vérifie. Confondre les deux conduit à des notes de calcul « prédimensionnées » qui n'ont pas la rigueur attendue en EXE |
| « Ne dimensionne PAS la protection au feu » | Exclusion CARNAC explicite. La mention générique est autorisée, le dimensionnement ne l'est pas — la protection au feu relève d'un autre lot |
| Pièce 3 « Points à faire valider » | En mode INTERNE-GO, notre conception doit être visée — par un BET, un BC, ou par vous-même en tant que concepteur. Sans cette liste, le visa se perd et la conception est exécutée sans validation |
| « Ne tranche aucune contradiction entre pièces » | Verrou V1 — si une contradiction bloque la conception, B-20 la signale et suspend la partie concernée. Un modèle qui tranche une contradiction en B-20 fausse la conception en silence |

Le point le plus sensible — la frontière avec B-40 à B-50 :
Un modèle qui reçoit B-20 a tendance à produire des notes de calcul complètes (vérifications EC2, EC3, ferraillage, ancrages). C'est exactement ce qu'il ne doit pas faire : B-20 prédimensionne, B-40 à B-50 vérifient.

| Ce que fait B-20 | Ce que fait B-40 à B-50 |
| --- | --- |
| « Poteau BA 15×25, prédimensionné par A_c ≥ N_Ed/(0,3·f_cd), ratio 0,85 » | « Poteau BA 15×25, vérifié EC2 §5.8 (flambement), §6.1 (N-M), biaxial, ferraillage 4HA14 + cadres HA6 e=150 » |
| « Semelle 90×90×30, prédimensionnée par B ≥ N/q_adm avec q_adm = 0,30 MPa » | « Semelle 90×90×30, vérifiée EC7 portance ELS/ELU, ferraillage A_min EC2 §9.2.1.1, poinçonnement EC2 §6.4 » |
| « Renfort de poutre bois par moisage 2×UPE200, méthode : ratio I/UPE ≈ I/bois » | « Moisage vérifié EC3 (flexion, cisaillement, interaction M-V) + EC5 (assemblage boulonné), notes de calcul jointes » |

Le piège : un modèle qui produit une note de calcul complète en B-20 croit bien faire. En réalité, il produit une note qui n'a pas la rigueur attendue (pas de vérification de tous les cas EC2/EC3/EC5/EC7), et qui sera reprise en B-40 à B-50 — ou pire, qui ne sera pas reprise et sera exécutée telle quelle. Les deux sont des échecs.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | L'énoncé de mission, les exclusions |
| B-01 (Proposition de la matrice) | Le statut de AC-03 (BET structure de conception) et DOC-03 (plans BET) — INTERNE-GO si AC-03 est À PRODUIRE PAR GO |
| B-11 (Audit du diagnostic structure) | Les désordres cités, les prescriptions — B-20 les utilise pour identifier les renforts |
| B-12 (Audit des pièces géotechniques) | Les données exploitables (SOL-01 à SOL-05) — B-20 les utilise pour prédimensionner les fondations |
| B-13 (Détection et qualification) | Les contradictions qualifiées — B-20 les signale et suspend les parties concernées |
| B-15 (Fiche de synthèse) | Les risques techniques (incertitudes sur les hypothèses) — B-20 les intègre dans sa note d'hypothèses (B-22) |
| B-21 (Descente de charges préliminaire) | Les N_ELS et N_ELU par porteur — B-20 les utilise pour prédimensionner les sections |
| B-23 (Exploitation du diagnostic existant) | Les contraintes de conception et les orientations de renforcement — B-20 les intègre dans sa trame |
| B-24 (Vérification d'éléments existants non) | Les sections inconnues de l'existant — B-20 les prend en compte avec mention |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-21 (Descente de charges préliminaire) | La trame et les porteurs — B-21 calcule les surfaces d'influence sur cette base |
| B-22 (Note d'hypothèses de conception) | Les hypothèses de conception — B-22 les consigne et les numérote |
| B-23 (Exploitation du diagnostic existant) | La trame et les renforts — B-23 vérifie la cohérence avec les contraintes du diagnostic |
| B-24 (Vérification d'éléments existants non) | Les sections à vérifier — B-24 produit des vérifications en mode PARAMÉTRIQUE |
| B-25 (Stabilité globale, contreventement, joints) | La trame, les porteurs et les planches de synthèse |
| B-30 (Calage sur dxf/dwg source) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-31 (Preuve de superposition) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-32 (Vue nettoyée par livrable) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-33 (Vérification croisée) | La trame et les plans de principe — B-30 calcule le calage sur cette base |
| B-34 (Synthèse des réservations) | La trame, les porteurs et les zones sensibles |
| B-40 (Fondations superficielles) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-41 (Fondations profondes) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-42 (Verticaux BA) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-43 (Planchers et dallages) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-44 (Charpente bois) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-45 (Structure métallique) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-46 (Maçonnerie : vérification) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-47 (Escaliers) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-48 (Prédalles et planchers préfabriqués) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-49 (Linteaux et seuils) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-50 (Assemblages et ancrages) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-60 (Plans d'exécution) | Les plans de principe — B-60 les transforme en plans d'exécution cotés |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-20 |
| --- | --- | --- |
| AC-03 | BET structure de conception | BLOQUANTE (détermine le mode : INTERNE-GO si absent, PARTIEL-DÉCLARÉ si partiel, SANS OBJET si complet) |
| DOC-03 | Plans BET structure | BLOQUANTE en PARTIEL-DÉCLARÉ (B-20 doit les lire), SANS OBJET en INTERNE-GO |
| DOC-02 | Plans architecte vectoriels | BLOQUANTE (trame de référence) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| GEO-01 à GEO-05 | Géométrie (emprise, axes, murs, poteaux, baies) | BLOQUANTE |
| SOL-01 à SOL-05 | Géotechnique (pour les fondations) | BLOQUANTE si fondations à concevoir |
| EXI-01, EXI-03 | Sections et résistance de l'existant | BLOQUANTE si renforts à concevoir |
| CFG-01 | Configuration de maturité MOE (CFG-1 à CFG-4) | BLOQUANTE (dès B-00) |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE si L / XL ou R+n |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE en neuf et restructuration |

Variables produites
B-20 ne produit pas de variable au sens du dictionnaire : sa sortie est un dossier de conception (note, plans, liste des points à valider) qui alimente B-21, B-22, B-23, B-24, B-30 et B-40 à B-50.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | AC-03, DOC-02, DOC-03, GEO-01 à GEO-05, SOL-01 à SOL-05, EXI-01, EXI-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-20, vous devez viser la conception (par vous-même, par un BET, ou par le BC) avant que les briques de calcul ne s'appuient dessus. Sans ce visa, les briques de calcul reprennent une conception non validée — et vous engagez votre responsabilité sur une conception qui n'a pas été visée.
Cas particulier — mode INTERNE-GO : si aucun BET de conception n'existe, B-20 est la seule source de conception. La sortie de B-20 (trame, sections de principe, plans de principe filigranés) devient l'entrée de toutes les briques de calcul. Le visa est indispensable — sans lui, vous exécutez une conception non validée.
Cas particulier — mode PARTIEL-DÉCLARÉ : si un BET partiel existe, B-20 cite ce qu'il fournit et complète ce qui manque. Les plans du BET sont repris tels quels (pas de redessin). Les plans de B-20 portent le filigrane « PRINCIPE — NE PAS EXÉCUTER » et la mention « complément à l'étude BET [référence] ».
Cas particulier — mode SANS OBJET : si un BET complet existe, B-20 produit une ligne de justification et s'arrête. La conception n'est pas à nous. Les briques de calcul reprennent directement les plans du BET.
Cas particulier — contradiction bloquante : si une contradiction (issue de B-13) empêche la conception d'une partie de l'ouvrage, B-20 suspend cette partie et la signale dans la liste des points à lever. Elle produit les plans de principe pour les parties non bloquées.
Cas particulier — existant non sondé : si les sections de l'existant ne sont pas connues (EXI-01 manquante), B-20 prédimensionne les renforts sous hypothèse de section (mention « à confirmer par B-24 »). La vérification fine relève de B-24 (mode PARAMÉTRIQUE) et de B-44 à B-50.
Format de sortie attendu : trois pièces distinctes (note de prédimensionnement, plans de principe, liste des points à lever). Les plans portent tous le filigrane « PRINCIPE — NE PAS EXÉCUTER » et un indice P.
Consignation : le dossier de conception B-20 est annexé au RDR (B-03) comme décision D-xx (« visa de la conception structure en date du … »). Il est mis à jour si la conception évolue en cours de projet (nouvel indice P2, P3…).
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Synthèse indissociable sur fond nettoyé.** B-20 travaille exclusivement sur le fond `B-32` (vue nettoyée : zéro cloison, zéro isolation, zéro doublage, zéro menuiserie de distribution) et produit une **synthèse structurelle complète sur une même vue** superposant `EXISTANT`, `DÉMOLITION` et `PROJET`. Il est interdit de traiter les pièces en silos, d'exclure un ouvrage du périmètre de la vue ou de déclarer un ouvrage « non plaçable ».

**Transcription vectorielle intégrale.** En `CFG-2` et `CFG-3`, les porteurs conçus par le BET MOE sont transcrits vectoriellement à 100 % sur le fond structurel pur, avec leurs interfaces et les ouvrages manquants (reprises, transferts, fondations non dessinées). En `CFG-1`, B-20 conçoit l'ensemble de la structure en `INTERNE-GO` et porte l'alerte contractuelle d'extension de mission et d'assurance.

**Continuité descendante et stabilité globale.** Toute trame produite est justifiée par une descente de charges continue `Toiture → Fondations` (`V15`), un système de contreventement identifié (`STR-01`) et, en `L-XL`, un découpage `JD` explicite. L'absence de fondations MOE n'autorise ni l'impasse ni la reproduction d'un modèle type : les fondations sont conçues ou transcrites, jamais omises.