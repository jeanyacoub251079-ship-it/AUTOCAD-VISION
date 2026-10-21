<!-- PACK CARNAC v3.0 — PACK 03 — PHASE 3 : CONCEPTION ET SYNTHÈSE STRUCTURELLE (B-20 à B-25) -->

# PACK 03 — PHASE 3 : CONCEPTION ET SYNTHÈSE STRUCTURELLE (B-20 à B-25)

**Quand coller ce pack** : Après validation de l'audit croisé.

**Ce qu'il contient** : B-20 synthèse indissociable sur fond nettoyé · B-25 stabilité globale et contreventement · B-21 descente de charges · B-22 hypothèses `H-xx` · B-23 exploitation du diagnostic · B-24 existant non sondé et `PA-xx`.

**Note d'usage** : C'est le pack qui contient les deux fiches les plus sensibles du carnet (B-20 et B-25) : c'est ici que se joue la conformité de la synthèse.

**Prérequis** : le pack `00_SOCLE.md` doit être collé avant celui-ci, dans la même discussion.

> Les fichiers ci-dessous sont reproduits **à l'octet près** depuis l'arborescence `CARNAC_v3.0` (contrôle `SHA-256` dans `PACKS_MANIFEST.json`). Ne modifiez aucun texte entre les balises : modifiez la fiche source, puis régénérez le pack.

---
**[Début du fichier : 04_PHASE_2_CONCEPTION/B-20_Conception_GO.md]**

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
**[Fin de 04_PHASE_2_CONCEPTION/B-20_Conception_GO.md]**

---

**[Début du fichier : 04_PHASE_2_CONCEPTION/B-25_Stabilite_Globale.md]**

Fichier 04_PHASE_2_CONCEPTION/B-25_Stabilite_Globale.md — CARNAC v3.0
________________


B-25 — STABILITÉ GLOBALE, CONTREVENTEMENT, JOINTS DE DILATATION ET SISMIQUE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — création de la brique (voir Journal des modifications, entrée v3.0) |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-20 (Conception ou synthèse structurelle) |
| Brique suivante | B-21 (DDC préliminaire), puis B-40 à B-50 |
| Modes d'appel | COMPLET (système de contreventement et géométrie d'ensemble établis) · HYPOTHÈSE-NOTIFIÉE (zone sismique, catégorie d'importance ou classe de sol non fournies mais bornables) · INTERNE-GO (le système de contreventement n'existe pas : nous le concevons) · SANS OBJET (aucune action horizontale à reprendre : ouvrage enterré contrebuté sur quatre faces, décision `D-xx`) |
| Entrées lues | Sortie de B-20, DDC de B-21, MPD validée (B-01), FDC (B-02), rapport géotechnique (B-12), vue nettoyée et différentielle (B-32) |
| Sortie unique | Note de stabilité globale : système de contreventement, cheminement des efforts horizontaux, excentricités et torsion, découpage `JD`, vérification sismique, stabilité des phases provisoires, schéma reporté sur les plans |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20 et avant toute brique de calcul, pour tout bâtiment de plus d'un niveau, tout ouvrage contreventé par voiles, portiques ou palées, tout bâtiment avec joints de dilatation, et systématiquement en gabarit `L-XL` (`CFG-02`). En gabarit `S`, B-25 est appelée en version abrégée si l'ouvrage ne comporte qu'un niveau et aucun contreventement dédié.

Ce que vous fournissez à l'IA : la sortie de B-20 (trame, porteurs, planches de synthèse), la DDC de B-21, la FDC (zone sismique, catégorie d'importance, classe de sol, coefficients), la vue nettoyée B-32 et le découpage `JD` (`CFG-03`). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}}, {{gabarit}} et {{mode}}.

Ce que vous validez à la sortie : le système de contreventement retenu (et son adéquation au gabarit de l'ouvrage), les excentricités et la torsion, le découpage en blocs `JD`, la position sismique et la catégorie d'importance, la stabilité des phases provisoires, et le report graphique du schéma de contreventement.

Ce que B-25 apporte de spécifique — la stabilité n'est pas un sous-produit du calcul élément par élément :
| Aspect | Sans B-25 | Avec B-25 |
| --- | --- | --- |
| Cheminement horizontal | Supposé par chaque brique locale | Explicite, continu, justifié niveau par niveau |
| Torsion | Découverte au calcul ou jamais | Calculée (excentricité structurale et accidentelle) avant les calculs locaux |
| Joints de dilatation | Subis, découverts sur plan | Décidés, dimensionnés, reportés en plan et en coupe |
| Phases provisoires | Oubliées | Vérifiées (stabilité des voiles et poteaux en phase transitoire) |
| Sismique | Mention générique | Position `EC8` explicite : zone, catégorie, classe de sol, méthode d'analyse |
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.

MODE D'EXÉCUTION APPLIQUÉ : {{mode}}.

MISSION : établir la note de stabilité globale de l'opération {{ID-01}} — {{ID-02}}, de gabarit {{gabarit}}, à partir de la conception ou de la synthèse structurelle B-20, de la descente de charges B-21 et du découpage en blocs structurels. Tu ne dimensionnes aucun élément : tu établis le système qui reprend et transmet les efforts horizontaux, et tu vérifies que ce système est continu, stable et compatible avec la géométrie différentielle du projet.

DONNÉES D'ENTRÉE À QUALIFIER AVANT CALCUL
- Zone sismique, catégorie d'importance, classe de sol, coefficient de comportement : valeur, source et norme d'appui (EC8 et arrêté national en vigueur).
- Actions du vent : site, catégorie de terrain, hauteur de référence, coefficients (EC1-1-4).
- Découpage en blocs et joints de dilatation : nombre, position, largeur, justification du découpage.
- Descente de charges horizontales et verticales par niveau et par bloc (B-21).

MÉTHODE
1. Identifie et décris le système de contreventement réellement disponible dans la géométrie du projet : voiles, portiques, noyaux, palées, triangulations, murs existants conservés, remplissages participatifs (avec la prudence requise). Si la conception B-20 ne comporte aucun système explicite, tu le conçois et tu le signales.
2. Trace le cheminement des efforts horizontaux : origine (vent, séisme, poussées, effets de second ordre), traversée de chaque niveau, reprise par les éléments verticaux, transmission aux fondations. Chaque niveau doit avoir une reprise identifiée ; toute rupture de cheminement est un défaut bloquant.
3. Calcule les centres de masse et de rigidité par niveau, l'excentricité structurale, l'excentricité accidentelle réglementaire, et l'effet de torsion associé. Vérifie les déplacements différentiels entre éléments de contreventement.
4. Vérifie la régularité (en plan et en élévation) au sens de l'EC8 ; en cas d'irrégularité, adapte la méthode d'analyse et les coefficients.
5. Décide et justifie le découpage en blocs `JD` : longueur maximale sans joint, effets de la température, retrait, tassements différentiels, phases de construction. Chaque joint est coté et reporté en plan et en coupe.
6. Vérifie la stabilité des phases provisoires : voiles ou poteaux non encore liaisonnés, planchers non coulés, stabilité au vent des éléments élancés en cours de montage, stabilité des fouilles et des talus de travail.
7. Vérifie les effets globaux du second ordre (amplification des efforts horizontaux) et la sensibilité aux déplacements.
8. Produis le schéma de contreventement et les coupes de principe, avec repères cohérents avec B-20 et report explicite sur le fond B-32.

INTERDICTIONS
- Ne dimensionne aucun élément porteur : les sections, ferraillages et assemblages relèvent de B-40 à B-50.
- Ne suppose aucune zone sismique, aucune catégorie d'importance et aucune classe de sol : chaque valeur est sourcée ou porte un repère {{DEC-05}} avec norme d'appui.
- Ne déclare jamais un bâtiment « régulier » sans avoir mesuré les excentricités.
- Ne crée aucun joint de dilatation sans justification écrite (longueur, température, retrait, tassement, phasage).
- Ne conserve pas un contreventement implicite : un remplissage en maçonnerie n'est jamais compté comme système de contreventement sans justification et sans dispositif de ductilité.
- Ne produis aucun schéma sans repères identiques à ceux de B-20.
- Ne laisse aucune discontinuité de cheminement non traitée : soit elle est reprise par un ouvrage identifié, soit elle est déclarée bloquante.

SORTIE
Pièce 1 — Système de contreventement : nature, implantation, justification du choix, éléments participants et éléments exclus.
Pièce 2 — Cheminement des efforts : tableau par niveau (origine, valeur, éléments de reprise, transmission au niveau inférieur), avec détection des ruptures.
Pièce 3 — Torsion et régularité : centres de masse et de rigidité, excentricités, effet de torsion, verdict de régularité, méthode d'analyse retenue.
Pièce 4 — Joints de dilatation : tableau des blocs `JD` (position, largeur, motif, report plan et coupe).
Pièce 5 — Phases provisoires : situations étudiées, vérifications, dispositions de stabilité.
Pièce 6 — Schéma de contreventement reporté sur le fond B-32, avec légende et renvois.

CRITÈRE D'ACCEPTATION
La note est acceptée si :
- chaque niveau dispose d'une reprise d'efforts horizontaux explicitement identifiée, jusqu'aux fondations ;
- les centres de masse et de rigidité, les excentricités et l'effet de torsion sont calculés pour chaque niveau ;
- la régularité en plan et en élévation est statuée avec la méthode d'analyse correspondante ;
- chaque zone sismique, catégorie d'importance et classe de sol est sourcée ou porte un repère d'hypothèse avec norme d'appui ;
- chaque joint de dilatation est justifié, coté et reporté en plan et en coupe ;
- les phases provisoires sont étudiées ;
- aucun élément porteur n'a été dimensionné dans cette brique.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}}, {{gabarit}} et {{mode}}, ainsi que tout repère d'hypothèse {{DEC-05}} par sa valeur ou son renvoi. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS
| Clause | Pourquoi |
| --- | --- |
| Brique distincte et non intégrée à B-20 | La conception décide de la géométrie, la stabilité globale décide du cheminement des efforts. Mélanger les deux conduit à des trames dessinées sans système de reprise, et à des calculs locaux fondés sur des hypothèses de contreventement jamais explicitées |
| « Tu ne dimensionnes aucun élément » | Frontière nette avec B-40 à B-50 (V11 et séquence bloquante). Une brique de stabilité qui dimensionne empiète sur les notes de calcul et crée des valeurs non tracées |
| Cheminement niveau par niveau | C'est le seul contrôle qui détecte une rupture de reprise : un plancher qui ne transmet pas, un voile qui s'arrête au R+1, une façade qui ne redescend pas. Sans ce tableau, la rupture n'apparaît qu'au calcul, ou jamais |
| Excentricités mesurées, jamais supposées | Un bâtiment déclaré « régulier » sans mesure est un bâtiment dont la torsion est ignorée. La mesure des centres de masse et de rigidité est la seule preuve de régularité opposable |
| Joints de dilatation justifiés | Un joint mal placé crée deux bâtiments qui se poussent ; un joint absent crée des fissures attribuées à la structure. Le joint est une décision de conception, pas un constat de chantier |
| Phases provisoires | Les effondrements de structure neuve surviennent presque toujours en phase provisoire. La stabilité au vent d'un voile non liaisonné n'est justifiée par aucun calcul d'exploitation |
| Report graphique avec repères identiques | Un schéma de contreventement qui ne partage pas les repères de B-20 est inutilisable sur chantier, et invérifiable par B-31 et B-33 |
| Sismique explicite | La mention « structure conforme » ne vaut rien. Seule compte la chaîne complète : zone, catégorie, classe de sol, régularité, méthode, coefficient de comportement |
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | La zone sismique, la catégorie d'importance, la classe de sol et les coefficients |
| B-20 (Conception structure GO) | La trame, les porteurs et les planches de synthèse |
| B-21 (Descente de charges préliminaire) | Les charges verticales et horizontales par niveau et par bloc |
| B-30 (Calage sur dxf/dwg source) | Le repère de référence dans lequel le schéma est établi |
| B-32 (Vue nettoyée par livrable) | Le fond structurel pur, support du schéma de contreventement |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-34 (Synthèse des réservations) | Les éléments de contreventement et les zones où tout percement est interdit |
| B-40 (Fondations superficielles) | Les efforts horizontaux et moments d'ensemble transmis au sol d'assise |
| B-41 (Fondations profondes) | Idem, avec les combinaisons sismiques |
| B-42 (Verticaux BA) | Les efforts tranchants et moments de torsion par élément de contreventement |
| B-44 (Charpente bois) | Les efforts horizontaux repris par les palées et triangulations |
| B-45 (Structure métallique) | Idem, avec les dispositions de ductilité |
| B-46 (Maçonnerie : vérification) | Le rôle interdit ou limité des remplissages dans le contreventement |
| B-60 (Plans d'exécution) | Le schéma de contreventement, les joints de dilatation et les dispositions parasismiques à reporter |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-25 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| CFG-02 | Gabarit d'opération (S / M / L-XL) | BLOQUANTE |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | NON BLOQUANTE (BLOQUANTE si sous-sol) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| SEC-01 | Exigences de résistance au feu (degré, durée, source) | NON BLOQUANTE |

Variables produites
B-25 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de stabilité globale) et un schéma reporté sur les plans, qui alimentent B-21, B-40 à B-50 et B-60.

Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | CFG-02, CFG-03, STR-01, STR-02, DEC-05 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Conventions de livrables | Calques, échelles, cartouche | 10_ANNEXES/A_Conventions_Livrables.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain : à la sortie de B-25, vous validez le système de contreventement et le découpage en blocs. C'est votre décision d'ingénieur : le modèle propose un système compatible avec la géométrie, vous décidez s'il est constructible avec les moyens de l'entreprise et compatible avec le phasage.

Cas particulier — bâtiment sans système de contreventement explicite : B-25 s'appelle en INTERNE-GO et conçoit le système (voiles de contreventement, palées, triangulations), avec alerte sur les conséquences contractuelles si la conception n'est pas dans la mission.

Cas particulier — **zone de sismicité 1 (très faible)** (v3.0.1) : **aucune vérification sismique**. Arrêté du 22/10/2010. B-25 mentionne « Zone 1 — sismique SANS OBJET » et **s'arrête** sur ce volet. Interdit : spectre, catégorie d'importance demandée pour un calcul sismique, `H-xx` sismique, relance MOA.

Cas particulier — données sismiques absentes **hors zone 1** : si la zone n'est pas 1 et que la catégorie d'importance n'est pas fournie, B-25 s'appelle en HYPOTHÈSE-NOTIFIÉE : elle retient l'enveloppe la plus défavorable compatible avec la localisation connue, cite l'article d'appui, reporte l'hypothèse sous nuage et la soumet au délai DEC-06. Une donnée sismique n'est jamais « supposée conforme ».

Cas particulier — **stabilité provisoire d'un bâtiment existant** (v3.0.1) : la vérification du contreventement en phase provisoire **incombe à la MOE structure de conception**. B-25 **signale** l'interface (dépose de refend, charge de chantier). Elle **ne calcule pas** la stabilité provisoire de l'existant. Elle **ne produit pas** de `T-04` bloquant à ce titre.

Cas particulier — bâtiment existant conservé : le contreventement de l'existant est qualifié avant d'être compté (continuité, liaisons, état). Un existant non qualifié n'est jamais compté comme système de reprise ; il est porté en PA-xx avec prescription ENC.

Format de sortie attendu : six pièces distinctes (système, cheminement, torsion et régularité, joints, phases provisoires, schéma reporté). Le schéma est produit sur le fond B-32 avec les repères de B-20.

Consignation : la note B-25 est annexée au RDL et le schéma reporté au jeu de plans B-60.
________________

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce.

**V15 — Différentiel temporel et continuité mécanique descendante.** Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Brique nouvelle v3.0.** B-25 est la seule brique habilitée à statuer sur la stabilité d'ensemble. Aucune brique de calcul ne peut la contourner en supposant un contreventement implicite. En gabarit `L-XL`, son exécution est obligatoire et son schéma est reporté sur chaque plan d'exécution.
**[Fin de 04_PHASE_2_CONCEPTION/B-25_Stabilite_Globale.md]**

---

**[Début du fichier : 04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md]**

Fichier 04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md — CARNAC v3.0
________________


B-21 — DESCENTE DE CHARGES PRÉLIMINAIRE
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-20 (Conception GO) |
| Brique suivante | B-22 (Note d'hypothèses) |
| Modes d'appel | COMPLET (CHG-01 à CHG-04 disponibles) · PARTIEL-DÉCLARÉ (usage ou poids propre déclaré par décision RDR) · PARAMÉTRIQUE (une charge d'exploitation manque mais les autres sont disponibles) |
| Entrées lues | CHG-01 à CHG-08, B-20 (conception, pour les porteurs à charger), DOC-02 (géométrie) |
| Sortie unique | Tableau de descente de charges préliminaire aux appuis (ELS et ELU) + surfaces d'influence + coefficients de continuité |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-20, avant B-22. B-21 est la DDC préliminaire — elle sert à choisir les sections en phase conception, pas à vérifier les sections (ce qui relève de B-40 à B-50).
Ce que vous fournissez à l'IA : les charges d'exploitation par usage (CHG-01, CHG-02), les poids propres des complexes de plancher (CHG-03) et de toiture (CHG-04), la géométrie (DOC-02), et les porteurs définis par B-20. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * les catégories d'usage EC1 par zone ;
   * les cloisons forfaitaires (NF EN 1991-1-1 §6.3.1.2) ;
   * les coefficients de continuité (1,15 sur appuis intermédiaires, 1,00 sur appuis de rive) ;
   * les tableaux ELS et ELU (distincts).
Ce que B-21 apporte de spécifique — la distinction préliminaire / exécution :

| Aspect | B-21 (DDC préliminaire) | DDC d'exécution (intégrée à B-40 à B-50) |
| --- | --- | --- |
| Objet | Choisir les sections en conception | Vérifier les sections en exécution |
| Méthode | Surfaces d'influence rectangulaires, coefficients de continuité forfaitaires | Surfaces d'influence exactes, coefficients de continuité issus du schéma statique réel |
| Précision | Approximative, mais justifiée | Exacte, cumulative |
| Usage | Alimenter B-20 (choix de sections) | Alimenter B-40 à B-50 (vérifications EC2/EC3/EC5/EC7) |

Règle de non-redondance : B-21 ne peut pas servir de DDC d'exécution. Elle est un outil de conception — elle est remplacée par les DDC détaillées des briques de calcul. Un livrable B-21 porte le titre « DDC PRÉLIMINAIRE — CONCEPTION ».
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la descente de charges PRÉLIMINAIRE de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}. Cette DDC sert à la conception (choix de sections, dimensionnement de principe). Elle NE REMPLACE PAS les DDC d'exécution des briques de calcul B-40 à B-50.


MÉTHODE
1. Pour chaque porteur (poteau, voile, semelle filante, profilé, ferme), établis la surface d'influence :
   - poteau : L_t × l_t (demi-portée adjacente dans chaque direction) ;
   - voile ou mur : largeur tributaire = somme des demi-portées des travées adjacentes, ramenée au mètre linéaire ;
   - profilé isolé : largeur tributaire = demi-entraxe de part et d'autre.
2. Décompose les charges par couche (G) et par usage (Q) :
   - charges permanentes : poids propres par couche (revêtement, chape, plancher, isolation, plafond, équipements) ;
   - charges d'exploitation : par catégorie d'usage EC1, avec cloisons forfaitaires (NF EN 1991-1-1 §6.3.1.2) ;
   - charges climatiques : neige, vent, si applicable.
3. Applique les coefficients de continuité forfaitaires :
   - 1,15 sur les charges de plancher transmises aux appuis intermédiaires (refend, transversaux, poteaux intermédiaires) ;
   - 1,00 aux appuis de rive (façades, poteaux de rive).
   Justifie le classement « appui de rive » / « appui intermédiaire » pour chaque porteur.
4. Combine selon EC0 :
   - ELS caractéristique : N_ELS = ΣG_k + Q_k,1 + Σψ₀,i·Q_k,i ;
   - ELU fondamentale : N_ELU = 1,35·ΣG_k + 1,5·Q_k,1 + 1,5·Σψ₀,i·Q_k,i.
5. Présente les résultats par porteur, en kN (poteaux) ou kN/m (murs, filantes).


INTERDICTIONS
- Ne produis AUCUNE vérification de section : c'est B-40 à B-50.
- Ne produis AUCUN ferraillage : c'est B-42, B-43, etc.
- N'utilise aucune charge « par expérience » : chaque charge est rattachée à une couche (poids propre) ou à une catégorie d'usage EC1 (exploitation).
- Ne confonds pas DDC préliminaire et DDC d'exécution : ta sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION ».
- Ne mélange pas ELS et ELU dans le même tableau : deux tableaux distincts.
- N'invente aucun coefficient de continuité : tu appliques 1,15 ou 1,00, avec justification du classement.


SORTIE
Tableau 1 — Surfaces d'influence
Porteur | L_t (m) | l_t (m) | A_inf (m²) | Justification (demi-portées adjacentes)


Tableau 2 — Charges permanentes par couche (par zone d'usage)
Zone | Couche | Épaisseur | Poids volumique | g (kN/m²) | Source (pièce ou hypothèse H-xx)


Tableau 3 — Charges d'exploitation par zone
Zone | Usage (catégorie EC1) | q_k (kN/m²) | Cloisons (kN/m²) | Total (kN/m²) | Source


Tableau 4 — Descente de charges par porteur (ELS)
Porteur | A_inf (m²) | G (kN) | Q (kN) | Coefficient de continuité | N_ELS (kN ou kN/m)


Tableau 5 — Descente de charges par porteur (ELU)
Porteur | A_inf (m²) | 1,35·G | 1,5·Q | Coefficient de continuité | N_ELU (kN ou kN/m)


Puis une synthèse de 8 lignes maximum :
- le porteur le plus chargé (en N_ELU) ;
- le porteur qui présente le plus fort ratio N/A_inf ;
- les zones où la charge d'exploitation est la plus pénalisante ;
- les hypothèses prises qui devront être confirmées en EXE.


CRITÈRE D'ACCEPTATION
La DDC préliminaire est acceptée si :
- chaque porteur a une surface d'influence justifiée ;
- chaque charge permanente est rattachée à une couche et à un poids volumique ;
- chaque charge d'exploitation est rattachée à une catégorie EC1 ;
- chaque coefficient de continuité est justifié ;
- les tableaux ELS et ELU sont distincts ;
- la sortie porte le titre « DDC PRÉLIMINAIRE — CONCEPTION » ;
- aucune vérification de section ni aucun ferraillage n'a été produit.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « DDC PRÉLIMINAIRE — CONCEPTION » | Empêche la confusion avec les DDC d'exécution des briques de calcul. Sans ce titre, une DDC préliminaire peut être prise pour une DDC d'exécution — et les sections dimensionnées sur cette base seraient fausses |
| Tableaux ELS et ELU distincts | Un modèle a tendance à mélanger les deux dans un seul tableau « pour faire court » — ce qui rend la vérification impossible et les erreurs de combinaison invisibles. Deux tableaux forcent la rigueur |
| Coefficients de continuité justifiés | Le 1,15 forfaitaire n'a de sens que si le classement rive/intermédiaire est justifié. Un modèle qui applique 1,15 partout obtient une DDC fausse de 15 % — et une DDC fausse de 15 % produit des sections surdimensionnées ou sous-dimensionnées |
| « Aucune charge par expérience » | Une charge d'exploitation « à 2,5 kN/m² comme d'usage » est une charge non défendable. Chaque charge est rattachée à EC1 — et chaque poids propre à une couche |
| Tableau 2 avec source « pièce ou hypothèse H-xx » | Les poids propres sont souvent absents du DCE : ils doivent être déclarés comme hypothèses (H-xx dans B-22) et non présentés comme des données. Sans cette colonne, on ne sait pas si la charge est sourcée ou estimée |
| « Ne mélange pas ELS et ELU » | Une DDC qui présente un seul tableau « N » sans préciser ELS ou ELU est illisible pour un vérificateur. Les combinaisons ELS et ELU ne se mélangent pas |
| Tableaux par porteur (poteau / voile / filante) | Une DDC globale sans distinction par porteur ne permet pas de dimensionner les sections. Chaque porteur a son N_ELS et son N_ELU — c'est ce qui permet à B-20 de prédimensionner |
| Synthèse en 8 lignes | La DDC préliminaire sert à orienter la conception — pas à être lue intégralement en réunion. Les 8 lignes identifient le porteur le plus chargé et les zones pénalisantes |
| « Ne produis aucune vérification de section » | Frontière B-21 / B-40 à B-50 : la DDC préliminaire calcule les charges, pas les résistances. Une note qui vérifie les sections en B-21 est une note qui se substitue à B-40 — et qui n'a pas la rigueur de B-40 |

Les coefficients de continuité — précision utile :

| Type d'appui | Coefficient | Justification |
| --- | --- | --- |
| Appui de rive | 1,00 | La charge de plancher n'est pas continue au-delà de l'appui — le moment d'encastrement est nul |
| Appui intermédiaire | 1,15 | La continuité du plancher au-delà de l'appui transmet une charge supplémentaire (moment d'encastrement) — le forfait 1,15 couvre cet effet |

Le piège du 1,15 : le coefficient de continuité est forfaitaire en phase conception. Il est exact en phase exécution (calculé par le schéma statique réel). Un modèle qui applique 1,15 partout (y compris aux appuis de rive) produit une DDC majorée de 15 % sur les rives — pas grave en conception, mais faux en exécution. C'est pourquoi la DDC préliminaire est remplacée par la DDC d'exécution dans B-40 à B-50.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte des pièces (usage des locaux, complexes de plancher) |
| B-01 (Proposition de la matrice) | Le statut de CHG-01 à CHG-08 (FOURNIE / PARTIELLE / BLOQUANTE / À PRODUIRE PAR GO) |
| B-20 (Conception structure GO) | La trame et les porteurs — B-21 calcule les surfaces d'influence sur cette base |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-20 (Conception structure GO) | Les N_ELS et N_ELU par porteur — B-20 les utilise pour prédimensionner les sections |
| B-22 (Note d'hypothèses de conception) | Les hypothèses de charges — B-22 les consigne et les numérote |
| B-24 (Vérification d'éléments existants non) | Les charges aux appuis — B-24 les utilise pour les vérifications suspendues |
| B-25 (Stabilité globale, contreventement, joints) | Les charges verticales et horizontales par niveau et par bloc |
| B-40 (Fondations superficielles) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-41 (Fondations profondes) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-42 (Verticaux BA) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-43 (Planchers et dallages) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-44 (Charpente bois) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-45 (Structure métallique) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-46 (Maçonnerie : vérification) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-47 (Escaliers) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-48 (Prédalles et planchers préfabriqués) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-49 (Linteaux et seuils) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-50 (Assemblages et ancrages) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-21 |
| --- | --- | --- |
| CHG-01 | Usage des locaux par zone (catégories EC1) | BLOQUANTE |
| CHG-02 | Surcharges d'exploitation par zone | BLOQUANTE |
| CHG-03 | Poids propres des complexes de plancher | BLOQUANTE |
| CHG-04 | Poids propres de toiture | BLOQUANTE (si toiture dans le périmètre) |
| CHG-05 | Neige | BLOQUANTE (si toiture) |
| CHG-06 | Vent | NON BLOQUANTE (B-21 n'intègre pas le vent — c'est B-44/B-45) |
| CHG-08 | Cloisons, équipements lourds, charges ponctuelles | BLOQUANTE |
| GEO-01 à GEO-04 | Géométrie et positions | BLOQUANTE (pour les surfaces d'influence) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| CFG-03 | Découpage en blocs structurels, joints de dilatation (JD) et niveaux-types | BLOQUANTE si L / XL ou R+n |
| STR-01 | Système global de contreventement, centre de torsion et descente des efforts horizontaux | BLOQUANTE en neuf et restructuration |

Variables produites
B-21 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (DDC préliminaire) qui alimente B-22 et B-40 à B-50.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | CHG-01 à CHG-08, GEO-01 à GEO-04, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-21, vous devez valider les catégories d'usage EC1 et les cloisons forfaitaires. C'est votre appréciation qui fait foi — un plateau technique kiné peut être classé C3 (activité) ou C4 (activité physique intense) selon l'usage réel. Le choix a un impact direct sur les sections.
Cas particulier — pas d'usage renseigné : si l'usage des locaux n'est pas clairement renseigné dans les pièces, B-21 s'appelle en mode PARTIEL-DÉCLARÉ (si une décision RDR a fixé un usage de travail) ou PARAMÉTRIQUE (si aucune décision n'a été prise). Dans les deux cas, l'usage retenu est explicitement déclaré.
Cas particulier — poids propres absents : si les complexes de plancher et de toiture ne sont pas détaillés dans le DCE, B-21 déclare des hypothèses H-xx (dans B-22) avec :
   * la couche (revêtement, chape, isolation, plafond) ;
   * l'épaisseur retenue ;
   * le poids volumique ;
   * la source (DTU, fiche technique, valeur usuelle — justifiée).
Ces hypothèses sont numérotées et tracées — elles seront reprises dans la DDC d'exécution.
Cas particulier — toiture (neige et vent) : si le projet comporte une toiture, B-21 intègre la neige dans les charges de toiture, mais pas le vent (le vent est traité par B-44 charpente bois et B-45 métal). Les combinaisons EC0 avec la neige comme action variable principale sont appliquées.
Cas particulier — charges ponctuelles : si des équipements lourds (chaudière, groupe de VMC, etc.) sont identifiés (CHG-08), ils sont traités comme des charges ponctuelles, avec la surface d'influence réduite au droit de l'équipement.
Format de sortie attendu : cinq tableaux distincts (surfaces d'influence, charges permanentes, charges d'exploitation, ELS, ELU), suivis d'une synthèse en 8 lignes maximum. Les tableaux ELS et ELU sont impérativement distincts.
Consignation : la DDC préliminaire B-21 est annexée au RDR (B-03) — elle alimente les hypothèses H-xx de B-22 et les discussions de choix de sections en B-20.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Descente de charges continue et différentielle.** La DDC préliminaire est établie par niveau et par bloc `JD`, en distinguant les charges de l'existant conservé, des démolitions et du projet neuf. Elle alimente directement `B-25` (stabilité globale) et l'ensemble des briques de calcul.
**[Fin de 04_PHASE_2_CONCEPTION/B-21_DDC_Preliminaire.md]**

---

**[Début du fichier : 04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md]**

Fichier 04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md — CARNAC v3.0
________________


B-22 — NOTE D'HYPOTHÈSES DE CONCEPTION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-21 (DDC préliminaire) |
| Brique suivante | B-23 (Exploitation du diagnostic), B-24 (Existant non sondé) |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | FDC (B-02), RDR (B-03), toutes les briques de la phase 2, puis toutes les briques de calcul qui introduisent une hypothèse (B-40 à B-50) |
| Sortie unique | Note d'hypothèses unique du projet, annexée à la FDC, mise à jour à chaque introduction |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * une première fois après B-21, pour consigner les hypothèses de conception (charges, matériaux, existant, sol) ;
   * à chaque fois qu'une brique introduit, modifie ou retire une hypothèse, en phases 2, 3 et 4.
Ce que vous fournissez à l'IA : la FDC (B-02), le RDR (B-03), les sorties des briques qui ont introduit des hypothèses (B-20, B-21, B-24, B-40 à B-50), et les hypothèses déjà consignées. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * chaque hypothèse H-xx (valeur, source, justification, statut) ;
   * la cohérence entre les hypothèses d'un même projet ;
   * les hypothèses abandonnées (jamais supprimées).
Ce que B-22 apporte de spécifique — la note unique :

| Aspect | Note unique B-22 | Notes éclatées (N notes) |
| --- | --- | --- |
| Cohérence | Les hypothèses se lisent ensemble — les interactions sont visibles | Les hypothèses sont isolées — les incohérences passent inaperçues |
| Vérification | Un tiers ouvre un seul document pour valider toutes les hypothèses | Un tiers doit ouvrir N documents pour valider une seule note de calcul |
| Traçabilité | Un numéro H-xx est stable dans toute la chaîne | Chaque note a ses propres numéros — les références croisées sont fragiles |
| Opposabilité | La note unique est la pièce opposable en cas de litige | Les notes éclatées rendent la défense difficile |

Règle stricte : une seule note d'hypothèses par projet — pas une par brique. Les hypothèses d'un même projet se lisent ensemble : une hypothèse de charge et une hypothèse de matériau interagissent, et leur cohérence ne se vérifie qu'en les lisant côte à côte.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : tenir à jour la note d'hypothèses UNIQUE de l'opération {{ID-01}} — {{ID-02}}. Cette note est annexée à la FDC et couvre l'ensemble du projet. Elle est mise à jour à chaque fois qu'une brique introduit, modifie ou retire une hypothèse.


RÈGLES
1. Chaque hypothèse porte un numéro unique H-xx (H-01, H-02…) et ne change plus de numéro, même si son contenu évolue. Une hypothèse révisée porte « H-xx (rév. n) ».
2. Chaque hypothèse porte :
   - la valeur retenue ;
   - la brique qui l'introduit (B-xx) ;
   - la justification (pourquoi cette valeur ?) ;
   - la source (pièce, ou « hypothèse de travail GO ») ;
   - le statut : À CONFIRMER / CONFIRMÉE / ABANDONNÉE ;
   - la brique impactée (celle qui utilise cette hypothèse).
3. Les hypothèses sont classées par famille : charges, matériaux, géométrie, existant, sol, autres.
4. Toute hypothèse non confirmée figure en filigrane sur les livrables qui l'utilisent : mention « sous hypothèse H-xx — à confirmer ».
5. Toute hypothèse abandonnée n'est jamais supprimée : elle est marquée ABANDONNÉE avec la raison, pour préserver la traçabilité.


INTERDICTIONS
- Ne crée aucune hypothèse sans justification : « valeur courante » n'est pas une justification.
- Ne supprime aucune hypothèse : tu la marques ABANDONNÉE.
- Ne fusionne jamais deux hypothèses distinctes en une seule.
- N'utilise aucune hypothèse qui ne soit pas dans la note.
- Ne recopie pas une hypothèse sans son numéro H-xx : un livrable qui cite une hypothèse doit citer son numéro.


SORTIE
Section 1 — Index des hypothèses actives
N° | Famille | Valeur | Brique introduisant | Brique impactée | Statut


Section 2 — Détail par hypothèse
Pour chaque hypothèse : H-xx, objet, valeur retenue, justification, source, statut, brique introduisant, brique impactée, date d'introduction, date de dernière révision.


Section 3 — Historique des révisions
Date | Hypothèse (H-xx) | Nature de la révision | Auteur | Motif


CRITÈRE D'ACCEPTATION
La note est acceptée si :
- chaque hypothèse a un numéro unique et stable ;
- chaque hypothèse a une justification (pas seulement une valeur) ;
- chaque hypothèse a un statut (À CONFIRMER / CONFIRMÉE / ABANDONNÉE) ;
- aucune hypothèse n'a été supprimée (les abandonnées sont conservées) ;
- l'historique des révisions est tenu ;
- l'index en section 1 est cohérent avec le détail en section 2.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Note unique par projet » | Votre choix — la cohérence des hypothèses ne se vérifie qu'en les lisant ensemble. Un éclatement en N notes rend impossible la vérification par un tiers (BC, BET, MOE) qui devrait ouvrir N documents pour valider une seule note de calcul |
| « H-xx stable, jamais renuméroté » | Un livrable cite « sous H-03 ». Si H-03 devient H-07 en cours de projet, le livrable devient faux sans que personne ne s'en aperçoive. La stabilité du numéro est la garantie de la traçabilité |
| « Toute hypothèse abandonnée est conservée » | La traçabilité est la protection en cas de litige : « pourquoi H-03 a-t-elle été abandonnée ? » doit avoir une réponse datée. Une hypothèse supprimée est une hypothèse qui ne peut plus être expliquée |
| « Ne recopie pas une hypothèse sans son numéro » | Une hypothèse non numérotée n'est pas traçable — et un livrable qui la cite sans numéro n'est pas opposable. C'est le verrou V2 (traçabilité) appliqué aux hypothèses |
| « Aucune hypothèse sans justification » | Une hypothèse « valeur courante » est indéfendable ; une hypothèse justifiée (« pas de G3 disponible, valeur plancher de la fourchette G2 ») est défendable. La justification est ce qui distingue une hypothèse de travail d'une valeur inventée |
| « Ne fusionne jamais deux hypothèses distinctes » | Une fusion d'hypothèses rend la traçabilité impossible — si l'hypothèse fusionnée est infirmée, on ne sait plus quelle partie de la valeur est fausse |
| « Toute hypothèse non confirmée figure en filigrane sur les livrables » | Un livrable qui utilise une hypothèse sans le mentionner est un livrable qui paraît certain alors qu'il est incertain. Le filigrane est la seule protection |
| « Ne supprime aucune hypothèse » | Une hypothèse supprimée est une hypothèse qui ne peut plus être expliquée en cas de litige. La conservation, même avec statut ABANDONNÉE, garantit la traçabilité |
| Section 3 — Historique des révisions | L'historique permet de savoir quand une hypothèse a changé, pourquoi, et par qui. C'est ce qui permet de comprendre une décision en cas de contestation |

Les trois statuts d'hypothèse — précision utile :

| Statut | Définition | Conséquence |
| --- | --- | --- |
| À CONFIRMER | Hypothèse de travail, non validée | Le livrable qui l'utilise porte le filigrane « sous hypothèse H-xx — à confirmer » |
| CONFIRMÉE | Hypothèse validée (par une décision RDR, une donnée reçue, ou une validation BET/BC) | Le livrable peut être en mode COMPLET (si l'hypothèse est explicitement citée) |
| ABANDONNÉE | Hypothèse qui n'est plus utilisée | Conservée pour traçabilité — le livrable qui l'utilisait doit être révisé |

Les six familles d'hypothèses — précision utile :

| Famille | Contenu | Exemples |
| --- | --- | --- |
| Charges | Poids propres, surcharges, cloisons | Poids propre d'un complexe de plancher non détaillé au CCTP |
| Matériaux | Classes de béton, nuances d'acier, classes de bois | Nuance d'acier d'un profilé Even non précisée (S235 supposé) |
| Géométrie | Sections de l'existant, épaisseurs de murs, hauteurs | Section d'une panne existante non sondée |
| Existant | Résistance des matériaux existants, état parasitaire | Résistance d'une maçonnerie ancienne non testée |
| Sol | q_adm, agressivité, ancrage | Valeur plancher de q_adm en attente du G3 |
| Autres | Classe de service, durée de vie, conditions de chantier | Durée de vie de projet non précisée |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — les valeurs À confirmer deviennent des hypothèses H-xx |
| B-03 (Registre des décisions) | Les décisions déjà prises — les hypothèses peuvent être validées par une décision D-xx |
| B-20 (Conception structure GO) | Les hypothèses de conception — B-22 les consigne et les numérote |
| B-21 (Descente de charges préliminaire) | Les hypothèses de charges — B-22 les consigne et les numérote |
| B-24 (Vérification d'éléments existants non) | Les hypothèses sur les sections inconnues de l'existant |
| B-40 (Fondations superficielles) | Les hypothèses introduites par chaque brique de calcul |
| B-41 (Fondations profondes) | Les hypothèses introduites par chaque brique de calcul |
| B-42 (Verticaux BA) | Les hypothèses introduites par chaque brique de calcul |
| B-43 (Planchers et dallages) | Les hypothèses introduites par chaque brique de calcul |
| B-44 (Charpente bois) | Les hypothèses introduites par chaque brique de calcul |
| B-45 (Structure métallique) | Les hypothèses introduites par chaque brique de calcul |
| B-46 (Maçonnerie : vérification) | Les hypothèses introduites par chaque brique de calcul |
| B-47 (Escaliers) | Les hypothèses introduites par chaque brique de calcul |
| B-48 (Prédalles et planchers préfabriqués) | Les hypothèses introduites par chaque brique de calcul |
| B-49 (Linteaux et seuils) | Les hypothèses introduites par chaque brique de calcul |
| B-50 (Assemblages et ancrages) | Les hypothèses introduites par chaque brique de calcul |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-40 (Fondations superficielles) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-41 (Fondations profondes) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-42 (Verticaux BA) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-43 (Planchers et dallages) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-44 (Charpente bois) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-45 (Structure métallique) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-46 (Maçonnerie : vérification) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-47 (Escaliers) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-48 (Prédalles et planchers préfabriqués) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-49 (Linteaux et seuils) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-50 (Assemblages et ancrages) | Les hypothèses sur la résistance des connecteurs, des résines, des nuances |
| B-64 (Notice de synthèse) | Les hypothèses H-xx actives — B-64 les liste avec leur statut |
| B-70 (Auto-contrôle déclaré de synthèse) | Les hypothèses non confirmées — B-70 vérifie que chaque hypothèse est tracée |
| B-72 (Journal de clôture) | Les hypothèses non confirmées — B-72 les liste dans les points ouverts |
| T-01 (Prompt de sincérité) | Les hypothèses H-xx — T-01 classe les éléments de principe et les éléments à lever |

Variables consommées

| Code | Libellé | Statut dans B-22 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| Toutes les variables À confirmer de la FDC | Selon la variable | BLOQUANTE (chaque valeur À confirmer doit être une hypothèse H-xx) |
| DEC-05 | Hypothèses notifiées sous nuage H-xx (valeur, norme, zone, statut) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |
| DEC-06 | Délai contractuel de contradiction des hypothèses notifiées (jours ouvrés) | BLOQUANTE si mode HYPOTHÈSE-NOTIFIÉE |

Variables produites
B-22 ne produit pas de variable au sens du dictionnaire : sa sortie est la note d'hypothèses (document unique, annexé à la FDC), qui référence toutes les hypothèses H-xx du projet.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| FDC (B-02) | Valeurs et fiabilité — les valeurs À confirmer deviennent des hypothèses | Document de projet |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-22, vous devez valider chaque hypothèse à son introduction. Une hypothèse validée trop tard est une hypothèse qui a déjà contaminé les calculs. La validation à l'introduction est la seule qui garantit que les calculs reposent sur des hypothèses connues et acceptées.
Cas particulier — hypothèse introduite par une brique de calcul : si une brique de calcul (par exemple B-42) introduit une hypothèse (par exemple, « section P1 supposée 140×140×8 »), elle est consignée en B-22 avec :
   * le numéro H-xx ;
   * la brique introduisant (B-42) ;
   * la brique impactée (B-42 elle-même, et B-50 pour les ancrages) ;
   * le statut À CONFIRMER.
La note est mise à jour à chaque introduction — pas en fin de projet.
Cas particulier — hypothèse confirmée : si une hypothèse est confirmée (par exemple, par une décision RDR D-05, ou par une donnée reçue), elle change de statut (À CONFIRMER → CONFIRMÉE), avec :
   * la date de confirmation ;
   * la source de la confirmation (décision RDR, donnée reçue, validation BET/BC).
L'historique des révisions (section 3) enregistre ce changement.
Cas particulier — hypothèse abandonnée : si une hypothèse n'est plus utilisée (par exemple, une hypothèse de charge devenue sans objet), elle est marquée ABANDONNÉE (pas supprimée), avec :
   * la raison de l'abandon ;
   * la date ;
   * la brique qui a rendu l'hypothèse obsolète.
Les livrables qui utilisaient cette hypothèse doivent être révisés (par le biais de B-32 — mise à jour incrémentale).
Cas particulier — hypothèse en conflit avec une décision RDR : si une hypothèse H-xx est en conflit avec une décision RDR (par exemple, H-03 dit « XC2 supposé » et D-05 dit « XA3 retenu »), l'hypothèse est abandonnée et remplacée par la décision RDR. La note documente ce remplacement.
Cas particulier — hypothèse liée à une donnée manquante : si l'hypothèse est liée à une donnée manquante (par exemple, « q_adm non disponible — on suppose 0,25 MPa »), elle est statuée À CONFIRMER, et elle est co-déclarée avec le verrou correspondant au RDR (V-xx). La note et le RDR se renvoient mutuellement.
Format de sortie attendu : trois sections distinctes (index, détail, historique des révisions). L'index est la vue rapide ; le détail est la vue complète ; l'historique est la vue chronologique.
Consignation : la note d'hypothèses B-22 est annexée à la FDC (B-02) — elle est la référence unique pour toutes les hypothèses du projet. Toute hypothèse utilisée dans une brique de calcul doit être présente dans cette note.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Note d'hypothèses `H-xx` unique et opposable.** Chaque hypothèse porte : valeur retenue, norme ou DTU d'appui, zone d'application, délai de contradiction (`DEC-06`), mode de report graphique (nuage). Une hypothèse sans norme d'appui n'est pas une hypothèse notifiée : c'est une valeur de repli interdite par le verrou `V3`.
**[Fin de 04_PHASE_2_CONCEPTION/B-22_Note_Hypotheses.md]**

---

**[Début du fichier : 04_PHASE_2_CONCEPTION/B-23_Exploitation_Diagnostic.md]**

Fichier 04_PHASE_2_CONCEPTION/B-23_Exploitation_Diagnostic.md — CARNAC v3.0
________________


B-23 — EXPLOITATION DU DIAGNOSTIC EXISTANT
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-11 (Audit du diagnostic), B-20 (Conception GO) |
| Brique suivante | B-24 (Existant non sondé), B-44 à B-50 (Calculs des renforts) |
| Modes d'appel | COMPLET (diagnostic audité par B-11 et zones relevées identifiées) · PARTIEL-DÉCLARÉ (zones non relevées : on cite l'emprise non couverte et on poursuit hors zone) · SANS OBJET (bâtiment neuf) |
| Entrées lues | B-11 (audit du diagnostic), sortie de B-20, DOC-05 (diagnostic), plans existants, EXI-01 à EXI-05 |
| Sortie unique | Tableau des contraintes de conception issues du diagnostic + tableau des ouvrages existants à renforcer + zones hors relevé + impacts sur B-20 |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-11 (audit du diagnostic) et B-20 (conception GO), avant B-24 (existant non sondé). B-23 est la brique qui transforme le diagnostic en contraintes de conception — elle ne réaudite pas le diagnostic (c'est B-11), elle en extrait ce qui s'impose à la conception.
Ce que vous fournissez à l'IA : la sortie de B-11 (audit du diagnostic), la sortie de B-20 (conception GO avec la trame et les renforts), le diagnostic (DOC-05), les plans existants. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * les contraintes de conception (classées en 5 catégories) ;
   * les orientations de renforcement (sans dimensionnement chiffré) ;
   * les zones hors relevé (avec emprise et impact) ;
   * les appuis sur l'existant (avec contrainte transmise estimée).
Ce que B-23 apporte de spécifique — la distinction avec B-11 :

| B-11 (Analyse) | B-23 (Conception) |
| --- | --- |
| Audite le diagnostic : que dit-il, que ne dit-il pas, que faut-il lever | Exploite le diagnostic : quelles contraintes pour la conception |
| Sortie : désordres, prescriptions à valider, données manquantes | Sortie : contraintes de conception, ouvrages à renforcer, zones hors relevé |
| Ne propose aucune solution | Propose des orientations de renforcement (moisage, sommier, contrefiche) — à valider par B-20 et les briques de calcul |
| Sortie consommée par B-20 et B-13 | Sortie consommée par B-20 |

La frontière avec B-20 : B-23 oriente (« le portique Ouest doit être renforcé par un sommier de répartition »), B-20 décide (« sommier 40×40 BA, prédimensionné par la méthode X »), B-44 à B-50 vérifient (« sommier vérifié EC2, ferraillage 4HA12 »). Trois niveaux de décision, trois briques distinctes.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : exploiter le diagnostic existant de l'opération {{ID-01}} — {{ID-02}} pour en tirer les CONTRAINTES DE CONCEPTION qui s'imposent à la conception structure GO (B-20). Tu ne produis pas un second audit (c'est B-11) : tu produis un tableau d'entrées pour la conception.


MÉTHODE
1. Reprends la liste des désordres de B-11 (numérotés). Pour chacun, identifie la contrainte qu'il impose à notre conception :
   - ouvrage à renforcer obligatoirement (désordre structurel avéré) ;
   - ouvrage à renforcer sous condition (désordre à surveiller) ;
   - contrainte de phasage (étaiement, reprise en sous-œuvre) ;
   - contrainte de coordination avec un autre lot (charpente, couverture, zinguerie) ;
   - sans impact sur notre conception.
2. Identifie les zones NON RELEVÉES ou NON COUVERTES par le diagnostic et leur emprise. Précise ce qu'on ne peut PAS concevoir dans ces zones sans relevé complémentaire.
3. Identifie les contraintes de phasage que le diagnostic impose : étaiements provisoires, reprises en sous-œuvre par passes alternées, ordre des démolitions/renforcements.
4. Identifie les appuis de notre structure sur l'existant : chaque appui doit être rattaché à un ouvrage existant identifié (mur, refend, poteau existant), avec la contrainte que cet appui impose.
5. Ne propose AUCUNE section, AUCUN ferraillage, AUCUNE nuance : tu identifies les contraintes, B-20 et les briques de calcul dimensionnent.


INTERDICTIONS
- Ne produis pas un second audit : B-11 a déjà audité, tu exploites.
- Ne propose aucune solution technique chiffrée : « moisage par profilés » est une orientation, « 2×UPE200 » est un dimensionnement (relève de B-20 puis B-45).
- Ne déclare pas un désordre « sans impact » sans le justifier.
- N'ignore aucune zone non relevée : tu la listes avec son emprise et son impact.
- Ne fusionne pas contrainte de phasage et contrainte de renforcement : ce sont deux catégories distinctes.


SORTIE
Tableau 1 — Contraintes de conception issues du diagnostic
N° désordre (réf. B-11) | Contrainte imposée | Catégorie (renforcement obligatoire / sous condition / phasage / coordination lot / sans impact) | Ouvrage concerné | Impact sur B-20


Tableau 2 — Ouvrages existants à renforcer (orientation)
Élément existant | Désordre (réf.) | Orientation de renforcement (sans dimensionnement) | Brique CARNAC qui dimensionnera | Points à valider par calcul


Tableau 3 — Zones hors relevé
Zone (localisation) | Emprise approximative | Ce qu'on ne peut pas concevoir | Relevé complémentaire requis (nature, moyen)


Tableau 4 — Appuis sur l'existant
Appui de notre structure (réf. B-20) | Ouvrage existant support | Contrainte transmise estimée | Contrainte admissible de l'existant (si connue) | Brique CARNAC qui vérifiera


Puis une synthèse de 8 lignes maximum :
- les trois contraintes les plus lourdes pour la conception ;
- les zones hors relevé qui bloquent une partie de la conception ;
- les interfaces de lots à trancher avant démarrage.


CRITÈRE D'ACCEPTATION
L'exploitation est acceptée si :
- chaque contrainte est rattachée à un désordre numéroté de B-11 ;
- chaque contrainte est classée dans l'une des cinq catégories ;
- chaque zone hors relevé identifie ce qu'on ne peut pas concevoir et le relevé nécessaire ;
- chaque appui sur l'existant est rattaché à un ouvrage existant identifié ;
- aucune solution technique chiffrée n'a été proposée ;
- la synthèse tient en 8 lignes.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Tu ne produis pas un second audit » | B-11 a déjà audité le diagnostic. Un second audit produit de la redondance et des contradictions entre B-11 et B-23 — le lecteur ne sait plus quel document fait foi. B-23 exploite B-11, elle ne le refait pas |
| Cinq catégories de contraintes | Un désordre n'est pas toujours « à renforcer » : il peut être « à surveiller » (désordre esthétique), « contrainte de phasage » (étaiement), « coordination lot » (interface charpente), ou « sans impact » (désordre hors périmètre). La catégorisation évite le réflexe « tout renforcer » qui produit des renforcements inutiles et coûteux |
| « Aucune solution technique chiffrée » | « 2×UPE200 » est un dimensionnement (B-45), pas une orientation (B-20). Confondre les deux conduit à des décisions non calculées — et à des renforcements exécutés sans vérification. La frontière B-23 / B-20 / B-44 à B-50 doit être nette |
| Tableau 3 — Zones hors relevé | Dans le projet Flora, deux zones « NON RELEVEE » du folio 02 n'ont jamais été relevées. Sans ce tableau, la conception dans ces zones est faite sur du vide — et les renforcements dimensionnés dans ces zones sont non opposables. B-23 signale les zones, B-24 produit les vérifications en PARAMÉTRIQUE pour les éléments non sondés |
| Tableau 4 — Appuis sur l'existant | Chaque appui sur l'existant est une contrainte : la contrainte transmise doit être estimée et l'existant doit être vérifié (B-46). Sans ce tableau, les appuis de nos ouvrages sur l'existant ne sont ni estimés ni vérifiés — et un appui non vérifié est un risque silencieux |
| « Ne fusionne pas contrainte de phasage et contrainte de renforcement » | Une reprise en sous-œuvre est un renforcement ET un phasage. Les deux dimensions sont distinctes et relèvent d'interlocuteurs différents (le renforcement relève de B-40, le phasage relève du plan de travaux et du PPSPS). Les fusionner masque l'une des deux dimensions |
| « Ne déclare pas un désordre "sans impact" sans le justifier » | Un désordre « sans impact » non justifié est un désordre qui peut cacher un impact réel. La justification force le modèle à expliciter pourquoi le désordre n'impacte pas notre conception |
| « Ne propose aucune section, aucun ferraillage, aucune nuance » | B-23 est une brique d'exploitation : elle oriente, elle ne dimensionne pas. Un modèle qui produit des sections en B-23 se substitue à B-20 et B-44 à B-50 — et les sections produites n'ont pas la rigueur attendue |
| Synthèse en 8 lignes | Une exploitation exhaustive sans synthèse n'est pas exploitable en réunion de lancement. Les 8 lignes forcent le modèle à hiérarchiser les contraintes |

Les cinq catégories de contraintes — précision utile :

| Catégorie | Définition | Exemple |
| --- | --- | --- |
| Renforcement obligatoire | Désordre structurel avéré : l'ouvrage existant ne peut pas rester en l'état | Poutre maîtresse fléchie (préjudice important) → moisage obligatoire |
| Renforcement sous condition | Désordre à surveiller : le renforcement dépend de l'évolution des charges ou de l'usage futur | Fissures esthétiques sur enduit → renforcement seulement si les charges augmentent |
| Phasage | Contrainte d'exécution : étaiement, reprise en sous-œuvre, ordre des travaux | Reprise en sous-œuvre par passes alternées (passerelle château) |
| Coordination lot | Contrainte d'interface : le désordre relève d'un autre lot mais impacte nos ouvrages | Chevrons altérés (lot charpente) → interface avec nos appuis |
| Sans impact | Désordre hors périmètre de notre conception | Traces d'humidité sur menuiseries (lot menuiseries) |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-11 (Audit du diagnostic structure) | Les désordres cités et les prescriptions — B-23 les exploite pour concevoir (contraintes de conception, renforcements à prévoir) |
| B-13 (Détection et qualification) | Les contradictions qui impactent les renforcements — B-23 les signale si elles bloquent une partie de la conception |
| B-14 (Clarification du périmètre) | Les prestations INCLUSES et les interfaces — B-23 s'appuie sur cette matrice pour distinguer les renforcements de notre lot des interfaces |
| B-20 (Conception structure GO) | La trame et les renforts — B-23 vérifie la cohérence avec les contraintes du diagnostic |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-20 (Conception structure GO) | Les contraintes de conception et les orientations de renforcement — B-20 les intègre dans sa trame |
| B-24 (Vérification d'éléments existants non) | Les zones hors relevé et les données manquantes — B-24 produit une vérification en mode PARAMÉTRIQUE |
| B-44 (Charpente bois) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-45 (Structure métallique) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-46 (Maçonnerie : vérification) | Les appuis sur l'existant — B-46 vérifie la contrainte transmise aux maçonneries existantes |
| B-47 (Escaliers) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-48 (Prédalles et planchers préfabriqués) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-49 (Linteaux et seuils) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| B-50 (Assemblages et ancrages) | Les orientations de renforcement — chaque brique dimensionne le renforcement dans son domaine (moisage bois → B-44 + B-45 ; sommier BA → B-42 + B-43 ; contrefiche → B-44 ; entretoise → B-45) |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-23 |
| --- | --- | --- |
| DOC-05 | Diagnostic structure de l'existant | BLOQUANTE |
| EXI-01 | Sections des éléments existants | BLOQUANTE (pour estimer les contraintes transmises) |
| EXI-02 | Pathologies relevées | BLOQUANTE |
| EXI-05 | Contrainte admissible transmise à l'existant | BLOQUANTE (pour vérifier les appuis) |
| GEO-01 à GEO-05 | Géométrie et positions | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |

Variables produites
B-23 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (tableau des contraintes de conception) qui alimente B-20, B-24 et B-44 à B-50.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DOC-05, EXI-01, EXI-02, EXI-05, GEO-01 à GEO-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-23, vous devez valider la catégorisation des contraintes (renforcement obligatoire / sous condition / phasage / coordination lot / sans impact). Un désordre classé « sans impact » qui impacte en réalité nos ouvrages est un désordre non traité — et c'est votre appréciation qui fait foi, pas celle du modèle.
Cas particulier — zone non relevée : si une zone est « non relevée » dans le diagnostic (comme les deux zones du folio 02 dans la conversation d'origine), B-23 :
   1. la liste dans le tableau 3 avec son emprise approximative ;
   2. précise ce qu'on ne peut pas concevoir dans cette zone (par exemple, « les sections de pannes dans cette zone ne peuvent pas être vérifiées ») ;
   3. identifie le relevé complémentaire nécessaire (nature, moyen : sondage, inspection visuelle, essai).
Cette zone devient soit une réserve R-xx au RDR (demande de relevé à la MOA), soit un verrou V-xx (brique suspendue dans cette zone).
Cas particulier — désordre hors lot : si un désordre relève d'un autre lot (charpente, couverture, zinguerie), B-23 le classe en « coordination lot » et identifie l'interface avec notre ouvrage. Le désordre n'est pas rejeté — il est nommé, et son impact sur nos appuis ou nos renforcements est analysé.
Cas particulier — appui sur l'existant non vérifiable : si un appui de notre structure sur l'existant ne peut pas être vérifié (parce que la contrainte admissible de l'existant n'est pas connue, ou parce que la section est inconnue), B-23 le signale dans le tableau 4 avec la mention « à vérifier par B-46 ou B-24 ». La vérification relève de la brique concernée, pas de B-23.
Cas particulier — diagnostic qui prescrit un renforcement : si le diagnostic prescrit un renforcement (par exemple, « moisage par 2×UPE200 »), B-23 le cite comme orientation (sans dimensionnement), et renvoie la vérification à B-44 (bois) et B-45 (métal). La prescription du diagnostic est un principe, pas un dimensionnement — elle doit être validée par nos calculs avant exécution.
Cas particulier — plusieurs désordres sur le même ouvrage : si plusieurs désordres concernent le même ouvrage existant (par exemple, une poutre qui a à la fois une flèche excessive et une humidité), B-23 les traite ensemble dans le tableau 2 (une ligne par ouvrage, avec plusieurs désordres cités). La fusion des désordres pour un même ouvrage est légitime — la fusion de deux ouvrages distincts ne l'est pas.
Format de sortie attendu : quatre tableaux distincts (contraintes, renforcements, zones hors relevé, appuis sur l'existant), suivis d'une synthèse en 8 lignes maximum. Chaque contrainte du tableau 1 est rattachée à un désordre numéroté de B-11 — c'est la traçabilité minimale.
Consignation : le tableau des contraintes B-23 est annexé au RDR (B-03) — il documente les contraintes de conception et alimente les réserves (R-xx) pour les zones hors relevé et les appuis non vérifiables.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).
**[Fin de 04_PHASE_2_CONCEPTION/B-23_Exploitation_Diagnostic.md]**

---

**[Début du fichier : 04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md]**

Fichier 04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md — CARNAC v3.0
________________


B-24 — VÉRIFICATION D'ÉLÉMENTS EXISTANTS NON SONDÉS
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 3 — Conception et synthèse structurelle |
| Brique précédente | B-23 (Exploitation du diagnostic) |
| Brique suivante | B-30 (Calage) — ou la première brique de calcul selon le PTD |
| Modes d'appel | PARAMÉTRIQUE uniquement (par construction : l'existant non sondé impose le littéral) |
| Entrées lues | EXI-01 (sections), EXI-03 (résistance), EXI-04 (sondages), B-11, B-23, DOC-05 |
| Sortie unique | Vérification littérale de l'élément existant + tableau de sensibilité non contractuel + liste des essais/sondages nécessaires pour fermer la vérification |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-23, quand des éléments existants sont concernés par nos travaux mais que leurs caractéristiques ne sont pas connues (sections, nuance, résistance). B-24 est la brique qui permet de travailler malgré l'incertitude — elle produit une vérification littérale qui servira dès que le sondage sera disponible.
Ce que vous fournissez à l'IA : les données disponibles sur l'existant (EXI-01 à EXI-04, si partielles), les sorties de B-11 et B-23, le diagnostic (DOC-05). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * le tableau de sensibilité (clairement identifié « NON CONTRACTUEL ») ;
   * la liste des essais (nature, référentiel, nombre, emprise) ;
   * la mention de suspension (vérification suspendue jusqu'à obtention des données).
Ce que B-24 apporte de spécifique — la brique typique du mode PARAMÉTRIQUE :

| Aspect | B-24 (mode PARAMÉTRIQUE) | B-46 (mode COMPLET) |
| --- | --- | --- |
| Données disponibles | Sections, nuances ou résistances inconnues | Sections, nuances et résistances connues |
| Méthode | Vérification littérale + tableau de sensibilité non contractuel | Vérification chiffrée avec les valeurs réelles |
| Valeur retenue | Aucune — la donnée reste en symbole | Valeur(s) issue(s) de la FDC |
| Livrable | Note suspendue, filigranée, suffixée _P | Note d'exécution, exécutable après visa |
| Conclusion | « En attente de [donnée] » | « Vérifié » ou « À renforcer » |

La règle la plus importante : B-24 ne retient aucune valeur. Elle produit des formules littérales, un tableau de sensibilité non contractuel, et la liste des essais nécessaires. C'est exactement le mode PARAMÉTRIQUE que vous avez validé au tronçon 2 : on travaille, on ne conclut pas.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : produire la vérification en mode PARAMÉTRIQUE des éléments existants non sondés de l'opération {{ID-01}} — {{ID-02}}. Tu ne retiens AUCUNE valeur : tu produis des formules littérales, un tableau de sensibilité NON CONTRACTUEL, et la liste des essais nécessaires pour fermer la vérification.


MÉTHODE
1. Pour chaque élément existant non sondé (poutre, solive, panne, ferme, poteau, mur porteur), identifie :
   - la donnée manquante (section ? nuance ? continuité ?) ;
   - la charge transmise par nos ouvrages (issue de B-21 ou B-20) ;
   - la vérification à effectuer (flexion, cisaillement, compression, flambement, déversement, ancrage).
2. Écris la vérification en littéral, avec la donnée manquante laissée en symbole :
   - flexion bois : σ_m,d = M_Ed/W = M_Ed/(b·h²/6) ≤ f_m,d ;
   - flexion métal : M_Ed/M_pl,Rd ≤ 1 avec M_pl,Rd = W_pl·f_y/γ_M0 ;
   - compression bois : N_Ed/(k_c·A·f_c,0,d) ≤ 1 avec k_c fonction de λ ;
   - compression métal : N_Ed/N_b,Rd ≤ 1 avec N_b,Rd = χ·A·f_y/γ_M1 ;
   - cisaillement : τ_d = k·V_Ed/(b·h·k_cr) ≤ f_v,d (bois) ou V_Ed/V_pl,Rd ≤ 1 (métal).
3. Produis un tableau de sensibilité sur une plage de valeurs PLAUSIBLES, clairement identifié comme NON CONTRACTUEL : chaque valeur testée est présentée comme « cas de sensibilité », jamais comme « valeur retenue ».
4. Identifie les essais ou sondages nécessaires pour fermer la vérification : nature de l'essai, référentiel (NF EN 338 pour le bois, NF EN 10025 pour l'acier), nombre, emprise.
5. Rédige la mention de suspension : la vérification est SUSPENDUE jusqu'à obtention des données, la brique reste en mode PARAMÉTRIQUE, le livrable est filigrané.


INTERDICTIONS
- Ne retiens AUCUNE valeur : aucune section, aucune nuance, aucun résultat de vérification n'est « retenu ».
- Ne déclare AUCUN élément « vérifié » : tous sont « en attente de données ».
- Ne présente le tableau de sensibilité comme contractuel : il est TOUJOURS marqué « NON CONTRACTUEL — POUR INFORMATION ».
- N'utilise aucune valeur « par expérience » : toute valeur testée est dans la plage plausible et justifiée comme telle.
- Ne réduis pas la plage plausible pour « faire joli » : si la plage est 100×200 à 200×300, tu la couvres entièrement.
- Ne produis aucun livrable exécutable : la sortie est une note de vérification suspendue, filigranée, avec mention « EN ATTENTE DE [donnée] ».
- Ne propose aucune valeur de repli : la décision de fonder sur une valeur plancher est une décision RDR (PARTIEL-DÉCLARÉ), jamais une initiative de B-24.


SORTIE
Tableau 1 — Éléments non sondés et vérifications suspendues
Élément | Donnée manquante | Charge transmise (kN, kNm) | Vérification à mener | Formule littérale | Brique de fermeture (B-44, B-45, B-46)


Tableau 2 — Tableau de sensibilité NON CONTRACTUEL
Élément | Donnée testée | Valeur testée | Résultat du calcul | Verdict (favorable / défavorable / limite) — pour information uniquement


Tableau 3 — Essais et sondages nécessaires
Élément | Essai | Référentiel | Nombre | Emprise | Responsable | Échéance


Tableau 4 — Impact sur la conception (B-20)
Élément | Conséquence si la donnée reste manquante | Solution de repli possible (décision RDR) | Brique concernée


Puis une synthèse de 6 lignes maximum :
- le nombre d'éléments en attente de données ;
- le nombre d'éléments dont la vérification est favorable pour toutes les valeurs plausibles (bonne nouvelle) ;
- les essais à commander en priorité ;
- les décisions RDR à prendre si les essais ne sont pas commandés.


CRITÈRE D'ACCEPTATION
La vérification est acceptée si :
- chaque élément non sondé a une vérification littérale écrite ;
- chaque donnée manquante est laissée en symbole (jamais remplie) ;
- le tableau de sensibilité est marqué « NON CONTRACTUEL — POUR INFORMATION » ;
- les essais nécessaires sont listés avec référentiel, nombre et emprise ;
- aucun élément n'est déclaré « vérifié » ;
- aucun livrable exécutable n'est produit ;
- la note porte le filigrane « EN ATTENTE DE [donnée] » et le suffixe _P.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Mode PARAMÉTRIQUE par construction | La brique n'a de sens que si la donnée manque. Si elle était disponible, elle relèverait de B-46 (vérification de l'existant) en mode COMPLET. Le mode unique de B-24 est ce qui la distingue de B-46 et garantit qu'elle ne se substitue pas à une vérification réelle |
| « Ne retiens AUCUNE valeur » | La tentation est forte de conclure « avec une section 100×200, ça passe ». C'est exactement ce qu'il faut interdire : une valeur testée n'est pas une valeur retenue. Une valeur retenue par B-24 serait une décision implicite non traçable — et cette décision relève d'une décision RDR (PARTIEL-DÉCLARÉ) |
| Tableau de sensibilité NON CONTRACTUEL | Un tableau de sensibilité mal identifié devient contractuel par usage — quelqu'un finit par l'exécuter. Le marquage explicite « NON CONTRACTUEL — POUR INFORMATION » est la seule protection |
| « Ne réduis pas la plage plausible » | Un modèle a tendance à ne tester que les valeurs qui « passent » — ce qui donne une fausse impression de sécurité. La plage plausible est fixée par la géométrie (sections existantes possibles), pas par le résultat. Si la section existante peut être 100×200 ou 200×300, on teste tout |
| Tableau 3 — Essais et référentiels | Sans référentiel, l'essai n'est pas commandable. NF EN 338 (bois) et NF EN 10025 (acier) sont les référentiels standards. Le nombre et l'emprise rendent l'essai chiffrable |
| « Ne propose aucune valeur de repli » | La valeur de repli est une décision RDR (PARTIEL-DÉCLARÉ), pas une proposition de B-24. C'est le verrou du mode PARAMÉTRIQUE : le modèle peut suggérer une valeur de repli dans B-04 (PTD), mais il ne peut pas l'appliquer sans une décision RDR |
| Filigrane + suffixe _P | Un livrable PARAMÉTRIQUE sans filigrane finit par être exécuté. Le filigrane et le suffixe sont les deux marqueurs qui empêchent la confusion avec un livrable exécutable |
| « Ne déclare aucun élément vérifié » | Un élément « vérifié » suppose une conclusion — et B-24 ne peut pas conclure. Déclarer « vérifié » un élément dont la section est inconnue est une affirmation fausse qui engage la responsabilité |
| Tableau 4 — Impact sur la conception | Une vérification suspendue n'est pas sans conséquence : elle impacte la conception (B-20), les calculs (B-40 à B-50) et le planning. Le tableau 4 documente cette conséquence — c'est ce qui permet à B-04 (PTD) et B-72 (clôture) de traiter les points ouverts |
| Synthèse en 6 lignes | La synthèse identifie les éléments favorables pour toutes les valeurs plausibles — une bonne nouvelle qui permet de fermer certains éléments même sans sondage. Les 6 lignes sont actionnables, pas descriptives |

Les trois verdicts de sensibilité — précision utile :

| Verdict | Définition | Conséquence |
| --- | --- | --- |
| Favorable | Le résultat de la vérification est satisfaisant pour toute la plage de valeurs plausibles | L'élément peut être considéré comme non critique — mais cette conclusion doit être validée par votre jugement (elle reste « pour information ») |
| Limite | Le résultat de la vérification est satisfaisant pour certaines valeurs de la plage, mais pas toutes | L'élément est critique : le sondage est indispensable pour conclure |
| Défavorable | Le résultat de la vérification est insuffisant pour toute la plage de valeurs plausibles | L'élément est à renforcer dans tous les cas — le sondage permettra de dimensionner le renforcement, mais la décision de renforcer est déjà acquise |

La limite de B-24 : même dans le cas « favorable », B-24 ne déclare pas l'élément vérifié — elle signale que toutes les valeurs plausibles sont favorables, ce qui est un indice fort mais qui reste non contractuel. La décision de conclure relève de votre jugement, ou d'une décision RDR.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-02 (Fiche de données) | Les données disponibles sur l'existant (EXI-01 à EXI-04) — B-24 les cite, mais ne les complète pas |
| B-11 (Audit du diagnostic structure) | Les données manquantes — B-24 produit une vérification en mode PARAMÉTRIQUE pour les éléments non sondés |
| B-20 (Conception structure GO) | Les sections à vérifier — B-24 produit des vérifications en mode PARAMÉTRIQUE |
| B-21 (Descente de charges préliminaire) | Les charges aux appuis — B-24 les utilise pour les vérifications suspendues |
| B-23 (Exploitation du diagnostic existant) | Les zones hors relevé et les données manquantes — B-24 produit une vérification en mode PARAMÉTRIQUE |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les essais à commander — B-03 les inscrit en réserves (R-xx) avec responsable et échéance |
| B-04 (Plan de travail dégradé) | Les éléments en attente de données et les essais nécessaires — B-04 les intègre dans le plan de travail dégradé |
| B-20 (Conception structure GO) | Les sections inconnues de l'existant — B-20 les prend en compte avec mention |
| B-22 (Note d'hypothèses de conception) | Les hypothèses sur les sections inconnues de l'existant |
| B-44 (Charpente bois) | Les vérifications suspendues de l'existant bois — B-44 les ferme si le sondage est disponible, sinon les reprend en mode PARAMÉTRIQUE |
| B-45 (Structure métallique) | Les vérifications suspendues de l'existant métal — B-45 les ferme si le sondage est disponible |
| B-46 (Maçonnerie : vérification) | Les vérifications suspendues des maçonneries existantes — B-46 les ferme si le sondage est disponible |
| B-49 (Linteaux et seuils) | Les vérifications suspendues des linteaux existants — B-49 les ferme si le sondage est disponible |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les essais à commander — T-04 les transforme en demande formelle à la MOA |

Variables consommées

| Code | Libellé | Statut dans B-24 |
| --- | --- | --- |
| EXI-01 | Sections des éléments existants | BLOQUANTE (si absente, c'est la donnée manquante qui justifie le mode PARAMÉTRIQUE) |
| EXI-03 | Résistance des matériaux existants | BLOQUANTE (idem) |
| EXI-04 | Résultats de sondages destructifs ou semi-destructifs | BLOQUANTE (idem) |
| DOC-05 | Diagnostic structure de l'existant | BLOQUANTE |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |

Variables produites
B-24 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (vérification suspendue) qui alimente B-44, B-45, B-46, B-04 et T-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes (en particulier PARAMÉTRIQUE) | 00_MASTER.md |
| Dictionnaire de variables | EXI-01, EXI-03, EXI-04, DOC-05, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-24, vous devez vérifier que :
   1. aucune valeur n'est retenue — chaque donnée manquante est en symbole ;
   2. le tableau de sensibilité est bien marqué « NON CONTRACTUEL » ;
   3. les essais sont listés avec référentiel, nombre et emprise ;
   4. les éléments « favorables pour toute la plage » sont bien signalés — c'est la seule bonne nouvelle que B-24 peut produire.
Cas particulier — appel en phase 4 : B-24 peut être appelée en phase 4 (calculs) pour les éléments existants non sondés — c'est la même brique, mais son appel est justifié par un besoin de vérification fine après les calculs d'exécution. Dans ce cas, B-24 reste en mode PARAMÉTRIQUE — elle ne se substitue jamais à B-46 (vérification de l'existant en mode COMPLET) quand les données sont disponibles.
Cas particulier — élément favorable pour toute la plage : si un élément est favorable pour toutes les valeurs plausibles, B-24 le signale dans la synthèse. Vous pouvez alors :
   * soit fermer l'élément (avec votre jugement, mentionné au RDR) ;
   * soit commander le sondage pour confirmation (plus rigoureux, mais plus coûteux) ;
   * soit passer en PARTIEL-DÉCLARÉ avec une valeur de repli (décision RDR).
Cas particulier — élément défavorable pour toute la plage : si un élément est défavorable pour toutes les valeurs plausibles, il est à renforcer dans tous les cas. Le sondage permettra de dimensionner le renforcement (B-44, B-45, B-46 en mode COMPLET), mais la décision de renforcer est déjà acquise — elle remonte dans B-23 (tableau 2, orientations de renforcement).
Cas particulier — élément sans plage plausible : si les données sont tellement manquantes qu'on ne peut même pas définir une plage plausible (par exemple, un élément dont on ne connaît ni la nature ni la fonction), B-24 le signale et recommande une inspection visuelle avant toute tentative de vérification. Ce cas est rare, mais il doit être explicitement traité.
Cas particulier — fermeture de la vérification : une vérification B-24 se ferme :
   * soit par un sondage (la donnée manquante arrive) → la vérification reprend en B-44/B-45/B-46 en mode COMPLET ;
   * soit par une décision RDR (valeur de repli acceptée) → la vérification reprend en mode PARTIEL-DÉCLARÉ ;
   * soit par un jugement de votre part documenté au RDR (élément favorable pour toute la plage — décision d'accepter le risque).
Format de sortie attendu : quatre tableaux distincts (éléments non sondés, sensibilité, essais nécessaires, impact sur la conception), suivis d'une synthèse en 6 lignes maximum. Le tableau de sensibilité est impérativement marqué « NON CONTRACTUEL — POUR INFORMATION ».
Consignation : la note B-24 est annexée au RDR (B-03) — elle documente les vérifications suspendues et alimente les réserves (R-xx) pour les essais à commander.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Inconnue physique = Point d'Arrêt, jamais hypothèse silencieuse.** L'existant non sondé est traité par prescription `ENC` (sondage, dépose, fouille, curage) et Point d'Arrêt `PA-xx` (`DEC-07`), avec critère de lever explicite et conséquence chiffrée en cas de découverte défavorable. Le mode `HYPOTHÈSE-NOTIFIÉE` ne s'applique jamais à une inconnue physique mesurable sur site.
**[Fin de 04_PHASE_2_CONCEPTION/B-24_Existant_Non_Sonde.md]**

<!-- FIN DU PACK — CARNAC v3.0 -->
