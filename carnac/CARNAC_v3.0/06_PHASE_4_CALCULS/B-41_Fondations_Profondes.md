Fichier 06_PHASE_4_CALCULS/B-41_Fondations_Profondes.md — CARNAC v3.0
________________


B-41 — FONDATIONS PROFONDES (VÉRIFICATION EN MODE DÉGRADÉ)
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 4 — Calculs d'exécution |
| Brique précédente | B-20 (Conception GO), B-12 (Audit Géotechnique) |
| Brique suivante | B-50 (Assemblages et ancrages), B-60 (Plans d'exécution) |
| Modes d'appel | PARAMÉTRIQUE (mode par défaut : les données de pieux sont rarement complètes, et nous ne concevons pas de pieux) · PARTIEL-DÉCLARÉ (valeur déclarée au RDR pour une donnée manquante) · SANS OBJET (MPD a statué qu'il n'y a pas de fondations profondes dans le périmètre) |
| Note sur le mode | B-41 est une brique de vérification, pas de conception : la conception de fondations profondes est hors de notre cœur de métier et relève d'une mission géotechnique spécifique. Les modes d'appel de B-41 sont donc, par construction : PARAMÉTRIQUE (par défaut), PARTIEL-DÉCLARÉ, SANS OBJET. |
| Entrées lues | SOL-01 à SOL-07, DOC-06 (rapport géotechnique), B-12 (audit géotechnique), B-20 (conception), B-21 (DDC préliminaire), données de pieux existants (EXI-04) ou prescrits par un spécialiste |
| Sortie unique | Note de vérification des fondations profondes : hypothèses contrôlées, données manquantes, risques, recommandation de mission G3/G4 — pas de plan de pieux |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-12 (audit géotechnique) et B-20 (conception), quand le projet comporte des fondations profondes (pieux existants à vérifier, pieux prescrits par un spécialiste, micropieux). En mode SANS OBJET (pas de fondations profondes dans le périmètre), B-41 produit une ligne de justification.
Ce que vous fournissez à l'IA : le rapport géotechnique (DOC-06), l'audit B-12, la conception B-20 (si des pieux sont prévus), les données de pieux existants (EXI-04) ou prescrits par un spécialiste, la DDC préliminaire B-21. Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{mode}}.
Ce que vous validez à la sortie :
   * les hypothèses de pieux (cohérence avec la DDC, la stratigraphie, la géométrie) ;
   * les données manquantes (essais, sondages, reconnaissance) ;
   * les recommandations de mission (G3, G4, essais complémentaires) ;
   * les points à faire valider par le spécialiste.
Le périmètre exact de B-41 :

| Ce que B-41 produit | Ce que B-41 ne produit pas |
| --- | --- |
| Contrôle des hypothèses de pieux (frottement, pointe, groupe, tassement) | Calcul de pieux (capacité portante, tassement, groupe) |
| Signalement des données manquantes | Plans de pieux |
| Vérification de la cohérence avec la DDC | Choix de la technique de pieux (battus, forés, micropieux) |
| Recommandation de mission G3/G4 | Calcul des ancrages de pieux (B-50) |
| Liste des points à faire valider par le spécialiste | Dimensionnement de la protection au feu (hors CARNAC) |

La règle la plus importante : B-41 contrôle les hypothèses, elle ne recalculle pas la capacité portante. La nuance est capitale : contrôler la cohérence entre la capacité portante annoncée et les charges transmises est à notre portée ; recalculer la capacité portante ne l'est pas — c'est le métier du géotechnicien.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la note de VÉRIFICATION des fondations profondes de l'opération {{ID-01}} — {{ID-02}}, dans le mode {{mode}}. Tu ne conçois AUCUN pieu : tu contrôles les hypothèses, tu signales les manques, tu recommandes les essais nécessaires.


RÈGLES NORMATIVES
- EC7 (NF EN 1997-1) et NF P 94-262 : fondations profondes.
- NF P 94-500 : missions géotechniques (G1 à G5).
- Pour chaque contrôle, tu cites la référence normative.


MÉTHODE


Étape 1 — Inventaire des données disponibles
Identifie la nature des fondations profondes concernées :
- pieux existants à vérifier (bâtiment existant) ;
- pieux prescrits par un spécialiste (bureau d'études géotechniques, BET structure) ;
- micropieux prescrits.
Pour chaque, cite la source (rapport géotechnique, plan de pieux, note de calcul du spécialiste) et son indice.


Étape 2 — Contrôle des hypothèses
Pour chaque donnée de pieu fournie, contrôle :
- la cohérence entre la capacité portante annoncée et les charges transmises (DDC B-21 ou B-40) ;
- la cohérence entre la longueur de pieu et la stratigraphie du rapport géotechnique ;
- la cohérence entre le nombre de pieux et la géométrie de la fondation (B-20) ;
- la présence ou l'absence de vérification du groupe de pieux ;
- la présence ou l'absence de vérification du tassement.
Tu ne recalculés PAS la capacité portante : tu contrôles sa cohérence avec les autres données.


Étape 3 — Signalement des données manquantes
Identifie ce qui manque pour que la vérification soit complète :
- essais de chargement (statique, dynamique) ;
- essais pressiométriques ou pénétrométriques complémentaires ;
- reconnaissance de la stratigraphie sous la pointe ;
- vérification du groupe ;
- vérification du tassement.
Chaque donnée manquante est rattachée à son code CARNAC (SOL-xx) et à sa brique (B-41).


Étape 4 — Recommandation de mission
Si les données sont insuffisantes, recommande une mission :
- G3 (mission géotechnique d'exécution) si le suivi de chantier est nécessaire ;
- G4 (mission géotechnique de supervision) si la conception doit être revue ;
- essais complémentaires (essais de chargement, essais pressiométriques).
Chaque recommandation cite sa base normative (NF P 94-500) et la conséquence de sa non-commande (briques suspendues, réserves à porter).


Étape 5 — Points à faire valider par le spécialiste
Liste les points que nous ne pouvons pas vérifier nous-mêmes et qui doivent être validés par un spécialiste :
- capacité portante des pieux ;
- tassement du groupe ;
- interaction sol-structure ;
- choix de la technique de pieux.


INTERDICTIONS
- Ne conçois AUCUN pieu : pas de choix de section, de longueur, de technique, de ferraillage.
- Ne calcule AUCUNE capacité portante, AUCUN tassement, AUCUNE vérification de groupe.
- Ne produis AUCUN plan de pieux.
- Ne sors pas des trois modes d'appel de la fiche : PARAMÉTRIQUE (par défaut), PARTIEL-DÉCLARÉ, SANS OBJET.
- Ne retiens aucune valeur sans la rattacher à une source citée.
- Ne propose aucune valeur de repli : la décision de fonder sur une valeur déclarée est une décision RDR (PARTIEL-DÉCLARÉ).
- Ne dimensionne PAS la protection au feu.


SORTIE
Pièce 1 — Inventaire des données
Tableau : type de fondation profonde | source (réf. exacte) | données fournies | données manquantes.


Pièce 2 — Contrôle des hypothèses
Tableau : hypothèse | source (réf.) | contrôle effectué | cohérence (oui / non / à vérifier) | conséquence si incohérence.


Pièce 3 — Données manquantes
Tableau : code CARNAC | libellé | impact sur notre vérification | voie d'obtention.


Pièce 4 — Recommandation de mission
Tableau : mission recommandée (G3 / G4 / essais) | base normative | justification | conséquence si non commandée.


Pièce 5 — Points à faire valider par le spécialiste
Tableau : point | nature (capacité / tassement / groupe / technique) | spécialiste pressenti.


Pièce 6 — Synthèse
6 lignes maximum : nombre de pieux / micropieux concernés | nombre d'hypothèses contrôlées | nombre de données manquantes | nombre de points à valider par le spécialiste | recommandation de mission (oui / non) | niveau de risque (faible / moyen / élevé).


CRITÈRE D'ACCEPTATION
La note est acceptée si :
- chaque donnée de pieu est rattachée à une source citée ;
- chaque hypothèse est contrôlée (cohérence avec DDC, stratigraphie, géométrie) ;
- chaque donnée manquante est rattachée à son code CARNAC et à sa voie d'obtention ;
- chaque recommandation de mission cite sa base normative et la conséquence de sa non-commande ;
- chaque point à valider par le spécialiste est identifié ;
- aucun pieu n'a été conçu, calculé, ou dessiné ;
- la synthèse tient en 6 lignes.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{mode}} (par PARAMÉTRIQUE, PARTIEL-DÉCLARÉ ou SANS OBJET). Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Trois modes d'appel seulement | B-41 n'est pas une brique de conception : conclure sur la capacité portante en toute autonomie n'est ni notre métier ni notre mission. Le mode par défaut est PARAMÉTRIQUE — par construction |
| « Tu ne conçois AUCUN pieu » | La conception de pieux est une mission géotechnique spécifique (G3/G4) qui engage la responsabilité du spécialiste. Notre rôle est de vérifier les données et de signaler les manques — pas de nous substituer au spécialiste |
| « Tu contrôles, tu ne recalculles pas » | La nuance est capitale : contrôler la cohérence entre la capacité portante annoncée et les charges transmises est à notre portée ; recalculer la capacité portante ne l'est pas. Le contrôle de cohérence détecte les erreurs de transmission, pas les erreurs de conception |
| Recommandation de mission G3/G4 | C'est le livrable principal de B-41 : si les données sont insuffisantes, la recommandation de mission est la seule action utile. Sans elle, la note se limite à un constat stérile |
| « Conséquence si non commandée » | Comme pour B-12, c'est ce qui vous protège en cas de litige : si la MOA ne commande pas la mission, vous avez documenté ce qui restera suspendu |
| Points à faire valider par le spécialiste | Certains points ne sont pas de notre compétence : les nommer explicitement évite de les traiter par défaut (et de commettre une erreur grave) |
| Pas de plan de pieux | Un plan de pieux sans calcul de pieux est un plan qui engage notre responsabilité sur une conception que nous n'avons pas faite. B-41 ne produit pas de plan — le plan de pieux vient du spécialiste |
| Synthèse en 6 lignes | B-41 est une note courte : elle ne se substitue pas au rapport géotechnique, elle le complète par le contrôle de cohérence |

Les trois modes de B-41 — précision utile :

| Mode | Situation | Livrable |
| --- | --- | --- |
| PARAMÉTRIQUE (par défaut) | Données de pieux incomplètes (ce qui est le cas le plus fréquent) | Note de vérification suspendue, avec liste des essais nécessaires et recommandation de mission |
| PARTIEL-DÉCLARÉ | Une décision RDR a accepté une valeur déclarée pour une donnée manquante | Note avec valeur déclarée, mention de l'auteur et de la date, et réserves sur les conséquences |
| SANS OBJET | MPD a statué qu'il n'y a pas de fondations profondes dans le périmètre | Ligne de justification |

Les deux pièges de B-41 — précision utile :
Piège 1 — Recalculer la capacité portante : un modèle qui reçoit un rapport géotechnique a tendance à recalculer la capacité portante annoncée. C'est exactement ce qu'il faut interdire :
   * le recalcul peut aboutir à une valeur différente de celle du géotechnicien ;
   * si la valeur du recalcul est plus favorable, elle masque un risque ;
   * si elle est plus défavorable, elle crée un conflit avec le géotechnicien.
La seule action légitime est de contrôler la cohérence : la capacité portante annoncée est-elle compatible avec les charges transmises, la stratigraphie, la géométrie ?
Piège 2 — Proposer une valeur de repli : si les données de pieux sont insuffisantes, un modèle a tendance à proposer une valeur de repli (par exemple, « capacité portante estimée à 500 kN par pieu ») pour « faire avancer le projet ». C'est exactement ce qu'il faut interdire :
   * la valeur de repli n'est pas sourcée — elle ne peut pas être défendue ;
   * elle devient implicitement la valeur de calcul — et les pieux dimensionnés sur cette base sont faux ;
   * elle masque le besoin d'une mission G3/G4 — et la MOA ne commande pas la mission complémentaire.
Le mode PARAMÉTRIQUE est la seule réponse correcte : on produit les contrôles de cohérence, on identifie les essais nécessaires, et on laisse la décision à la MOA.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-01 (Proposition de la matrice) | Le statut de leurs variables d'entrée (FOURNIE → mode COMPLET, BLOQUANTE → mode PARAMÉTRIQUE ou suspension) |
| B-02 (Fiche de données) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-03 (Registre des décisions) | Les décisions (Section 1) — chaque brique vérifie qu'une décision RDR existe avant d'appliquer une valeur en mode PARTIEL-DÉCLARÉ |
| B-12 (Audit des pièces géotechniques) | Les valeurs relatives aux pieux — B-41 les contrôle et recommande une mission G3/G4 si nécessaire |
| B-13 (Détection et qualification) | Les contradictions qui impactent leur périmètre — chaque brique vérifie qu'une contradiction la concernant a été tranchée avant de s'exécuter en mode COMPLET |
| B-20 (Conception structure GO) | La trame et les sections de principe — chaque brique de calcul reprend la section retenue et la vérifie finement |
| B-21 (Descente de charges préliminaire) | Les ordres de grandeur des charges — chaque brique de calcul refait la DDC d'exécution, mais s'appuie sur B-21 pour vérifier la cohérence |
| B-22 (Note d'hypothèses de conception) | Les hypothèses H-xx actives — chaque brique cite les hypothèses qu'elle utilise |
| B-25 (Stabilité globale, contreventement, joints) | Idem, avec les combinaisons sismiques |
| B-40 (Fondations superficielles) | Les efforts aux semelles — B-41 vérifie la cohérence si les pieux reprennent une partie des charges |
| T-02 (Prompt de recadrage) | La version corrigée — la brique source est relancée avec la nouvelle méthode |
| T-04 (Prompt de demande) | La réponse à la demande — la brique est relancée en mode COMPLET ou PARTIEL-DÉCLARÉ |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-22 (Note d'hypothèses de conception) | Les hypothèses introduites par chaque brique de calcul |
| B-31 (Preuve de superposition) | Le livrable à vérifier et les positions prévues |
| B-33 (Vérification croisée) | Le livrable et les positions prévues — B-33 les compare aux autres livrables |
| B-50 (Assemblages et ancrages) | Les efforts aux têtes de pieux (si des ancrages sont prévus) |
| B-60 (Plans d'exécution) | Les plans de fondations — B-60 reprend les pieux existants (pas les pieux neufs, qui relèvent du spécialiste) |
| B-62 (Nomenclature et façonnage) | La note de calcul — B-62 vérifie la cohérence entre les quantités du plan et celles de la note |
| B-64 (Notice de synthèse) | La note de calcul et les décisions de calcul — B-64 les synthétise |
| B-70 (Auto-contrôle déclaré de synthèse) | Le verdict de B-41 — B-70 vérifie que les fondations profondes sont traitées |
| B-72 (Journal de clôture) | Les recommandations de mission — B-72 liste les points ouverts |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les recommandations de mission — T-04 les transforme en demande formelle à la MOA |

Variables consommées

| Code | Libellé | Statut dans B-41 |
| --- | --- | --- |
| SOL-01 à SOL-07 | Géotechnique | BLOQUANTE (chaque valeur doit être citée avec sa source) |
| SOL-04 | Nature et succession des couches | BLOQUANTE (pour la cohérence avec la longueur de pieu) |
| SOL-08 | Mission géotechnique disponible (G1/G2/G3) | BLOQUANTE (détermine la suffisance des données) |
| DOC-06 | Rapport géotechnique | BLOQUANTE |
| EXI-04 | Résultats de sondages (pieux existants) | BLOQUANTE (si pieux existants à vérifier) |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-07 | Prescriptions chantier opposables (ENC) et Points d'Arrêt (PA-xx) | BLOQUANTE si inconnue physique (Classe II) |
| STR-02 | Poussées des terres, surcharges de remblai et écrans de soutènement | BLOQUANTE si sous-sol ou soutènement |

Variables produites
B-41 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (note de vérification) qui alimente B-50, B-60, B-70, B-72 et T-04.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | SOL-01 à SOL-08, DOC-06, EXI-04, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-41, vous devez décider si la mission complémentaire doit être commandée. C'est une décision MOA, mais c'est vous qui documentez la conséquence de la non-commande. Un contrôle de cohérence qui recommande une G3 sans documenter la conséquence ne vous protège pas en cas de litige.
Cas particulier — pieux existants à vérifier : si le projet comporte des pieux existants à vérifier (par exemple, une extension sur des pieux anciens), B-41 s'appuie sur les résultats de sondages (EXI-04) pour contrôler les hypothèses. Si les sondages sont absents, B-41 recommande une inspection vidéo ou un essai de chargement — c'est la seule façon de vérifier la capacité portante d'un pieu existant.
Cas particulier — pieux prescrits par un spécialiste : si un spécialiste (BET structure, géotechnicien) a prescrit des pieux avec une note de calcul, B-41 contrôle cette note :
   * cohérence capacité portante / charges transmises ;
   * cohérence longueur de pieu / stratigraphie ;
   * cohérence nombre de pieux / géométrie de fondation ;
   * vérification du groupe et du tassement.
B-41 ne recalcule pas la note du spécialiste — elle vérifie qu'elle est cohérente avec les autres données du projet. Si une incohérence est détectée, elle est signalée et le spécialiste est consulté.
Cas particulier — micropieux : si le projet comporte des micropieux (par exemple, pour des reprises en sous-œuvre), B-41 les traite comme des fondations profondes au sens large — avec les mêmes contrôles de cohérence. La technique de micropieu est du ressort du spécialiste, pas de B-41.
Cas particulier — absence de données de pieux : si aucune donnée de pieu n'est fournie mais que le projet comporte des fondations profondes (par exemple, parce que le rapport géotechnique recommande des pieux), B-41 s'appelle en mode PARAMÉTRIQUE et :
   * signale l'absence totale de données ;
   * recommande une mission G3/G4 ;
   * liste les essais nécessaires (essais de chargement, reconnaissance complémentaire) ;
   * ne propose aucune valeur de repli.
Cas particulier — recommandation G4 : si les données sont suffisantes pour la conception mais que le suivi d'exécution est nécessaire (par exemple, pour des pieux de grande longueur, ou dans un sol hétérogène), B-41 recommande une G4 (mission géotechnique de supervision) plutôt qu'une G3. La G4 couvre le suivi de l'exécution, pas seulement la conception.
Cas particulier — mode SANS OBJET : si la MPD a statué qu'il n'y a pas de fondations profondes dans le périmètre (par exemple, travaux de superstructure sans fondations profondes), B-41 s'appelle en mode SANS OBJET et produit une ligne de justification. Elle ne calcule rien, ne vérifie rien, ne recommande aucune mission.
Format de sortie attendu : six pièces distinctes (inventaire, contrôle, données manquantes, recommandation, points à faire valider par le spécialiste, synthèse). La note est courte (3 à 5 pages) — elle ne se substitue pas au rapport géotechnique, elle le complète.
Consignation : la note B-41 est annexée au RDR (B-03) — elle documente le contrôle de cohérence et alimente les réserves (R-xx) pour les recommandations de mission.
________________
---

### COMPLÉMENT v2.0 — RÉGIME OUTILLÉ (verrou V13, annexe O)
Cette brique est en **régime outillé** pour ses contrôles chiffrés (vérification des hypothèses et des capacités portantes) : elle produit un script (OUT-02), l'exécute, relit réellement les fichiers produits et consigne le journal d'exécution (OUT-03) au format de l'annexe O §7. B-41 étant une brique de contrôle dont les seuls modes d'appel sont PARAMÉTRIQUE, PARTIEL-DÉCLARÉ et SANS OBJET, le régime outillé conditionne la déclaration d'exécution de ses contrôles : sans environnement d'exécution (OUT-01), ils ne peuvent pas être déclarés exécutés ; la brique est suspendue ou limitée à l'analyse documentaire déclarée. Toute mention d'un contrôle « simulé » est une non-conformité V13.


---

### COMPLÉMENT v2.0 — CALCULS, ELS ET TOLÉRANCES
1. **Adossage script (V13, annexe O §5)** : chaque application numérique de la note est produite par le script de calcul versionné avec la note (OUT-02) ; la note cite le script, ses entrées (codes FDC) et ses sorties. Aucun nombre n'est calculé « de tête » dans le texte.
2. **Combinaisons EC0 complètes** : ELU (fondamentale, accidentelle le cas échéant), ELS caractéristique, fréquente et quasi-permanente sont distinguées ; les coefficients ψ sont cités. Les vérifications de déformation et de fissuration utilisent les combinaisons ELS adaptées (quasi-permanente pour les déformations différées, caractéristique ou fréquente pour la fissuration selon le cas).
3. **Position EC8 explicite** : la note déclare, dans ses hypothèses, si l'EC8 s'applique (zone, catégorie d'importance, régularité) ou non — et pourquoi. « Non applicable » est une conclusion motivée, pas un silence.
4. **Tolérances d'exécution (NF EN 13670)** : la classe d'exécution est déclarée ; les tolérances qui conditionnent le calcul (position des armatures, Δc_dev) sont cohérentes avec l'enrobage retenu.
5. **Enrobage construit, pas seulement lu** : c_nom = c_min + Δc_dev, avec c_min = max(c_min,b ; c_min,dur ; 10 mm) selon l'EC2 §4.4, confronté à l'exigence de tenue au feu lorsqu'elle relève du lot (SEC-01). MAT-03 est la valeur résultante portée en FDC, pas une valeur devinée.

6. **Fissuration (EC2 §7.3)** : pour chaque élément BA, la note vérifie l'ouverture de fissures w_k ≤ w_max (classe d'exposition, tableau 7.1N) ou applique les règles indirectes (diamètres/espacements maximaux) en le déclarant. Une note BA sans position sur la fissuration est incomplète.
7. **Déformations (EC2 §7.4)** : flèches et rotations sont vérifiées lorsque l'élément y est sensible, avec les inerties fissurées ou les rapports portée/hauteur selon la méthode déclarée.

8. **Poussées et eau** : si une semelle, une bêche ou un soubassement retient des terres ou est sous nappe (SOL-06), la poussée des terres et la poussée hydrostatique sont introduites dans les combinaisons, ou leur absence est motivée.
9. **Actions d'exécution (EC1-1-6)** : les phases provisoires dimensionnantes (fouilles ouvertes, blindage, reprise en sous-œuvre, étaiement) sont identifiées ; la situation provisoire ne doit pas être plus défavorable que la situation définitive sans être vérifiée.

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).