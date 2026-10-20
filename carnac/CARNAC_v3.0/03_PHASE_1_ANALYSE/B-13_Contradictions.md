Fichier 03_PHASE_1_ANALYSE/B-13_Contradictions.md — CARNAC v3.0
________________


B-13 — DÉTECTION ET QUALIFICATION DES CONTRADICTIONS INTER-PIÈCES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-10, B-11, B-12 (les trois audits) |
| Brique suivante | B-15 (Synthèse des risques) |
| Modes d'appel | COMPLET (B-10, B-11, B-12 tous exécutés en COMPLET) · PARTIEL-DÉCLARÉ (un des trois audits en mode dégradé : on signale les pièces non auditées et on limite la détection aux pièces couvertes) |
| Entrées lues | Sorties de B-10, B-11, B-12, inventaire B-00, MPD validée (B-01) |
| Sortie unique | Tableau des contradictions classées (gravité × nature) + tableau des briques impactées + inscription au RDR (B-03) |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-10, B-11 et B-12. B-13 est la brique de synthèse transversale des écarts entre les pièces — c'est elle qui qualifie les contradictions détectées à chaud par B-00, et qui en détecte de nouvelles.
Ce que vous fournissez à l'IA : les sorties de B-10, B-11 et B-12 (audits CCTP, diagnostic, géotechnique), l'inventaire B-00 (contradictions détectées à chaud), la MPD validée. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * le double classement (gravité × nature) de chaque contradiction ;
   * la brique impactée et le mode induit ;
   * l'inscription au RDR (V-xx si bloquante, R-xx si à lever ou à surveiller).
Ce que B-13 apporte de spécifique — la qualification systématique :

| Aspect | B-00 (détection à chaud) | B-13 (traitement systématique) |
| --- | --- | --- |
| Détection | Pendant l'inventaire | Après les trois audits, de manière exhaustive |
| Qualification | Non (liste brute) | Oui (gravité × nature) |
| Rattachement | Non | Oui (brique impactée, mode induit) |
| Inscription RDR | Non | Oui (V-xx ou R-xx) |
| Sortie | Liste de contradictions | Tableau qualifié + briques impactées |

Distinction fondamentale à respecter : B-13 ne traite que les contradictions au sens strict. Une lacune (une pièce ne dit rien sur un objet) ou une imprécision (une pièce dit quelque chose d'ambigu) ne sont pas des contradictions — elles relèvent de B-10, B-11 ou B-12. C'est ce qui évite que B-13 se transforme en second audit du CCTP.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : détecter et qualifier TOUTES les contradictions inter-pièces du DCE de l'opération {{ID-01}} — {{ID-02}}, à partir des audits B-10 (CCTP), B-11 (diagnostic existant) et B-12 (géotechnique). Tu ne tranches AUCUNE contradiction : tu les qualifies, tu les classes, tu les rattaches aux briques CARNAC concernées.


DÉFINITIONS STRICTES
- CONTRADICTION : deux pièces (ou deux passages) affirment des choses incompatibles sur un même objet. Les deux affirmations ne peuvent pas être vraies en même temps.
- LACUNE : une pièce ne dit rien sur un objet attendu. Ce N'EST PAS une contradiction. Traitée par B-10, B-11 ou B-12 — elle ne figure pas dans ta sortie.
- IMPRÉCISION : une pièce dit quelque chose d'ambigu. Ce N'EST PAS une contradiction. Traitée par B-10 — elle ne figure pas dans ta sortie.


CLASSEMENT OBLIGATOIRE EN DEUX COLONNES INDÉPENDANTES
Gravité :
- BLOQUANTE — empêche un calcul opposable, rend un livrable inexploitable, ou met en cause la sécurité structurale.
- À LEVER AVANT DÉMARRAGE — n'empêche pas les études mais doit être tranchée avant travaux.
- À SURVEILLER — ni bloquante ni critique, à documenter et suivre.
Nature :
- TECHNIQUE — deux valeurs, hypothèses ou prescriptions techniques incompatibles.
- CONTRACTUELLE — deux pièces du marché affirment des périmètres ou prestations incompatibles.
- D'INTERFACE — deux lots se renvoient la même prestation, ou aucun ne la prend.


MÉTHODE
1. Confronte systématiquement chaque paire de pièces auditée : CCTP ↔ plans BET, CCTP ↔ diagnostic, plans BET ↔ diagnostic, géotechnique ↔ plans BET, géotechnique ↔ CCTP, etc.
2. Confronte aussi chaque pièce à elle-même : une prescription du CCTP contredit-elle un autre article du CCTP ? Un désordre du diagnostic contredit-il un plan du même diagnostic ?
3. Élimine les doublons : une même contradiction vue sous deux angles reste UNE ligne.
4. Ne confonds pas contradiction et lacune/imprécision : si tu hésites, applique le test « les deux affirmations peuvent-elles être vraies en même temps ? ». Si oui, ce n'est pas une contradiction.
5. Pour chaque contradiction retenue : identifie la ou les briques CARNAC impactées (B-40 à B-50, ou B-20 à B-24) et le mode induit (COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE / INTERNE-GO).
6. Propose l'inscription au RDR : V-xx si BLOQUANTE, R-xx si À LEVER ou À SURVEILLER.


INTERDICTIONS
- Ne tranche AUCUNE contradiction : tu listes, c'est moi qui décide.
- N'invente aucune contradiction : chaque ligne cite les DEUX sources avec leur référence exacte (fichier + folio/page + indice).
- N'accepte aucune contradiction sur la foi d'une des deux pièces seule.
- Ne recopie pas les contradictions déjà détectées par B-00 sans les qualifier (gravité + nature + brique impactée) : B-00 a détecté à chaud, B-13 traite systématiquement.
- Ne mélange pas lacune ou imprécision dans la sortie : elles relèvent de B-10, B-11 ou B-12.


SORTIE
Tableau principal — Contradictions qualifiées :
N° | Objet | Source A (réf. exacte) | Source B (réf. exacte) | Nature de l'écart (en une phrase) | Gravité (B / ALVD / AS) | Nature (T / C / I) | Brique(s) impactée(s) | Mode induit | Inscription RDR proposée


Tableau secondaire — Répartition par brique :
Brique | Nombre de contradictions bloquantes | Nombre à lever avant démarrage | Nombre à surveiller | Mode consolidé induit


Puis une synthèse de 8 lignes maximum :
- les trois contradictions qui engagent le plus nos études (par gravité et par nombre de briques impactées) ;
- les contradictions qui ne sont pas nouvelles (déjà au RDR depuis B-00) et celles qui sont nouvelles ;
- le nombre total par gravité et par nature.


CRITÈRE D'ACCEPTATION
Le tableau est accepté si :
- chaque ligne cite les DEUX sources avec référence exacte ;
- chaque ligne porte un classement gravité et un classement nature ;
- aucune ligne ne relève d'une lacune ou d'une imprécision (test « les deux affirmations peuvent-elles être vraies ? ») ;
- chaque ligne identifie la brique impactée et le mode induit ;
- aucune contradiction n'a été tranchée par toi ;
- la synthèse tient en 8 lignes.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Définitions strictes de CONTRADICTION / LACUNE / IMPRÉCISION | Sans ces définitions, un modèle produit des « contradictions » qui sont en réalité des manques — et l'on retombe sur un second audit du CCTP au lieu d'un traitement ciblé. C'est la clause qui borne le périmètre de B-13 |
| Test « les deux affirmations peuvent-elles être vraies en même temps ? » | Test objectif qui permet de trancher entre contradiction et imprécision sans arbitrage subjectif. C'est le seul critère qui rend le classement reproductible — deux ingénieurs doivent aboutir au même résultat |
| « Ne tranche AUCUNE contradiction » | Verrou V1 — la contradiction est signalée, jamais résolue par le modèle. Un modèle qui tranche une contradiction en B-13 fausse toute la chaîne aval (B-40 à B-50 s'appuient sur les contradictions pour fixer leurs modes) |
| « Ne recopie pas les contradictions de B-00 sans les qualifier » | Empêche la redondance stérile : B-00 signale, B-13 qualifie et rattache aux briques. Une contradiction recopiée sans qualification est une contradiction qui ne sera jamais traitée |
| Double classement gravité × nature | Votre choix : les deux interlocuteurs ne sont pas les mêmes (le BET traite la technique, la MOE le contractuel, l'OPC l'interface). Un classement unique masque cette réalité |
| « Élimine les doublons » | Une même contradiction vue sous deux angles (par exemple, « XA4 du CCTP vs XA3 de la décision » et « enrobage 30 vs 50 ») est UNE seule ligne avec deux conséquences, pas deux lignes. Sans cette clause, le tableau explose en doublons |
| Mode induit | Chaque contradiction doit savoir à quoi elle conduit : si BLOQUANTE, brique suspendue ; si À LEVER, mode dégradé ; sinon, mode complet possible. Sans le mode induit, le tableau est descriptif mais non actionnable |
| « Ne mélange pas lacune ou imprécision dans la sortie » | Une contradiction, une lacune et une imprécision ont trois traitements différents (B-13, B-10, B-10). Les mélanger dans le même tableau rend le tri impossible |
| « chaque ligne cite les DEUX sources » | Verrou V2 — une contradiction qui ne cite qu'une source est une affirmation unilatérale, pas une contradiction. La double citation est la preuve qu'il y a bien deux affirmations incompatibles |
| Synthèse en 8 lignes | Un tableau de contradictions sans synthèse n'est pas exploitable en réunion. Les 8 lignes forcent la hiérarchisation |

Les trois niveaux de gravité — précision utile :

| Gravité | Définition objective | Action induite | Inscription RDR |
| --- | --- | --- | --- |
| BLOQUANTE | Empêche un calcul opposable, rend un livrable inexploitable, ou met en cause la sécurité structurale | Inscription immédiate au Registre des Verrous (V-xx) ; demande de décision MOE/MOA ; brique suspendue | V-xx |
| À LEVER AVANT DÉMARRAGE | N'empêche pas les études (on peut produire en PARAMÉTRIQUE ou PARTIEL-DÉCLARÉ), mais doit être tranchée avant le démarrage des travaux | Inscription au RDR avec échéance avant démarrage | R-xx |
| À SURVEILLER | Ne bloque ni les études ni le démarrage, mais doit être documentée et suivie (risque de dérive en phase travaux) | Inscription au RDR sans échéance ferme, revue à chaque réunion de chantier | R-xx |

Les trois natures — précision utile :

| Nature | Définition | Interlocuteur habituel |
| --- | --- | --- |
| TECHNIQUE | Deux valeurs, deux hypothèses ou deux prescriptions techniques incompatibles (ex. : deux classes d'exposition, deux sections, deux niveaux) | BET / MOE technique |
| CONTRACTUELLE | Deux pièces du marché affirment des périmètres ou des prestations incompatibles (ex. : CCTP et DPGF, CCTP et plan) | MOE / MOA |
| D'INTERFACE | Deux lots se renvoient la même prestation, ou aucun ne la prend (ex. : appuis de charpente sur nos sommiers) | MOE / OPC |

Une contradiction peut être BLOQUANTE et D'INTERFACE, ou À SURVEILLER et TECHNIQUE — les deux classements sont indépendants.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La liste des contradictions détectées à chaud par B-00 — B-13 les reprend pour les qualifier (gravité × nature) et les rattacher aux briques |
| B-01 (Proposition de la matrice) | Les décisions de périmètre — elles permettent de savoir si une contradiction est dans notre périmètre ou hors périmètre |
| B-10 (Audit critique du CCTP) | Les contradictions internes détectées par B-10 — B-13 les qualifie (gravité × nature) et les rattache aux briques |
| B-11 (Audit du diagnostic structure) | Les désordres cités et les données manquantes — B-13 les qualifie et les rattache aux briques |
| B-12 (Audit des pièces géotechniques) | Les écarts entre les données géotechniques et les autres pièces |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les propositions d'inscription (V-xx ou R-xx) — B-03 les inscrit dans la section correspondante |
| B-04 (Plan de travail dégradé) | Les briques suspendues par une contradiction BLOQUANTE — B-04 les intègre au plan de travail dégradé |
| B-14 (Clarification du périmètre) | Les contradictions d'interface identifiées — B-14 les intègre dans le tableau 3 |
| B-15 (Fiche de synthèse) | Les contradictions qualifiées — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise, responsable) |
| B-20 (Conception structure GO) | Les contradictions qualifiées — B-20 les signale et suspend les parties concernées |
| B-23 (Exploitation du diagnostic existant) | Les contradictions qui impactent les renforcements — B-23 les signale si elles bloquent une partie de la conception |
| B-40 (Fondations superficielles) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-41 (Fondations profondes) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-42 (Verticaux BA) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-43 (Planchers et dallages) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-44 (Charpente bois) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-45 (Structure métallique) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-46 (Maçonnerie : vérification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-47 (Escaliers) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-48 (Prédalles et planchers préfabriqués) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-49 (Linteaux et seuils) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-50 (Assemblages et ancrages) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |

Variables consommées

| Code | Libellé | Statut dans B-13 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE (B-13 ne peut pas qualifier une contradiction sans savoir si elle est déjà au registre) |
| Toutes les variables statuées FOURNIE, PARTIELLE, BLOQUANTE par B-01 | Selon la variable | Selon le statut |
| GEO-13 | Matrice de recalage multi-sources vers le Repère Structurel Unique (RSU) | BLOQUANTE |
| GEO-14 | Différentiel géométrique EXISTANT / DÉMOLITION / PROJET et continuités N+1 → N | BLOQUANTE en existant et en R+n |

Variables produites
B-13 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (tableau des contradictions qualifiées) qui alimente B-15, B-03 et B-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DEC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-13, vous devez valider le classement gravité × nature de chaque contradiction. C'est votre appréciation qui fait foi, notamment pour les À SURVEILLER que vous pourriez requalifier en À LEVER (verrou V12, sens unique : une fois requalifiée en À LEVER, une contradiction ne redevient jamais À SURVEILLER).
Cas particulier — contradiction déjà détectée par B-00 : si une contradiction a déjà été détectée à chaud par B-00, B-13 la reprend et la qualifie (gravité + nature + brique impactée). Elle ne la recopie pas sans qualification — c'est la règle de non-redondance.
Cas particulier — contradiction entre deux pièces contractuelles : si le CCTP et le marché se contredisent (par exemple, le CCTP inclut une prestation que le marché exclut), la contradiction est de nature CONTRACTUELLE et de gravité BLOQUANTE — elle doit être tranchée par la MOE avant de poursuivre. B-13 la liste, B-03 l'inscrit en V-xx, B-04 suspend les briques concernées.
Cas particulier — contradiction d'interface entre lots : si deux lots se renvoient la même prestation (par exemple, la charpente s'appuie sur nos sommiers BA mais le lot charpente n'est pas dans notre marché), la contradiction est de nature D'INTERFACE et de gravité À LEVER AVANT DÉMARRAGE — elle doit être tranchée par la MOE ou l'OPC avant travaux. B-13 la liste, B-03 l'inscrit en R-xx.
Cas particulier — contradiction interne au CCTP : si deux articles du CCTP se contredisent (par exemple, §01.2.1.5.5.1 prescrit une peinture intumescente et §01.2.1.5.5.2 mentionne un encoffrement), la contradiction est de nature CONTRACTUELLE et de gravité variable selon l'enjeu. B-13 la liste avec les deux articles.
Cas particulier — contradiction sans impact sur nos briques : si une contradiction existe entre deux pièces mais n'impacte aucune brique CARNAC (par exemple, deux revêtements de sol incompatibles dans le lot finitions), B-13 la liste quand même dans le tableau, avec la mention « brique impactée : aucune — hors périmètre CARNAC ». Le fait qu'elle soit hors périmètre ne dispense pas de la signaler : elle peut avoir un impact indirect sur la coordination.
Format de sortie attendu : un tableau principal (contradictions qualifiées) à 10 colonnes, un tableau secondaire (répartition par brique) à 4 colonnes, suivis d'une synthèse en 8 lignes maximum.
Consignation : le tableau des contradictions est annexé au RDR (B-03) — les contradictions BLOQUANTE deviennent des verrous (V-xx), les À LEVER et À SURVEILLER deviennent des réserves (R-xx).
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Réconciliation quantitative multi-pièces.** Le tableau de contradictions intègre une matrice de réconciliation `Plans Archi ↔ Plans Structure ↔ CCTP/DPGF ↔ Diagnostic ↔ Géotechnique` : surfaces, linéaires de voiles, nombres d'ouvertures, sections annoncées. Un écart quantitatif est une contradiction au même titre qu'un écart de valeur.

**Recalage commun.** Toute contradiction de position est arbitrée sur le `RSU` (`GEO-13`) : deux cotes divergentes sont comparées après recalage, jamais sur des fonds différents.