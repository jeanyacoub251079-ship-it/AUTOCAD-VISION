Fichier 02_PHASE_0_CADRAGE/B-02_FDC.md — CARNAC v3.0
________________


B-02 — FICHE DE DONNÉES DE CONCEPTION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 0 — Cadrage et qualification |
| Brique précédente | B-01 (MPD validée) |
| Brique suivante | B-03 (RDR) |
| Modes d'appel | COMPLET (valeurs disponibles) · PARTIEL-DÉCLARÉ (décision RDR déclarée pour une valeur) · PARAMÉTRIQUE (variable restant en symbole) |
| Entrées lues | MPD validée (B-01), toutes les pièces du projet, décisions RDR déjà inscrites (le cas échéant) |
| Sortie unique | FDC complète (tableau valeurs + sources + fiabilité) + tableau des verrous en fin de fiche |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après validation de la MPD par vous. B-02 transforme la MPD en document exploitable : elle rassemble les valeurs effectivement lues par les briques, avec leurs sources et leur niveau de fiabilité.
Ce que vous fournissez à l'IA : la MPD validée, les pièces du projet, les décisions RDR déjà prises (s'il y en a). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} par le code projet.
Ce que vous validez à la sortie :
* chaque valeur et sa source ;
* le niveau de fiabilité (Contractuelle / Décision / À confirmer) ;
* la liste des verrous (variables BLOQUANTE qui n'ont pas de valeur).
Principe clé de la FDC : la FDC porte les valeurs et leur source, pas seulement des renvois. Un lecteur de note de calcul doit pouvoir lire la FDC sans ouvrir le CCTP. C'est ce qui garantit qu'une note de calcul reste opposable — chaque valeur qui y figure est traçable jusqu'à sa source.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la Fiche de Données de Conception (FDC) de l'opération {{ID-01}}, à partir de la MPD validée et des pièces du projet. La FDC porte les VALEURS et leur SOURCE — elle doit pouvoir être lue sans ouvrir le CCTP.


RÈGLES
1. Seules les variables lues par au moins une brique activée figurent en FDC. Une variable non lue n'apparaît pas.
2. Chaque ligne porte : code, libellé, valeur, unité, source (fichier + folio/page + indice) OU mention « VERROU » si la valeur est absente.
3. Niveau de fiabilité obligatoire pour chaque valeur :
   - Contractuelle — valeur issue d'une pièce du marché ;
   - Décision — valeur issue du RDR (numéro, auteur, date cités) ;
   - À confirmer — valeur de travail, non validée.
4. Aucune valeur de repli n'est proposée. Aucune « pratique courante » n'est invoquée comme source.
5. Les variables VERROU sont listées en fin de FDC avec la brique suspendue et la voie d'obtention.
6. Les conflits entre pièces (deux valeurs incompatibles pour le même code) ne sont PAS arbitrés : ils sont listés comme VERROU et inscrits au RDR (B-03).


INTERDICTIONS
- Ne remplis aucun champ sans source citée.
- Ne retiens aucune valeur sur la base d'une pratique courante, d'un ordre de grandeur ou d'une « valeur usuelle ».
- Ne tranche aucune contradiction entre pièces.
- Ne propose aucune décision qui appartient au RDR.


SORTIE
Tableau 1 : Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) consommatrice(s)
Tableau 2 (fin de fiche) : Code VERROU | Brique suspendue | Voie d'obtention proposée (relevé / essai / mission G / décision MOA) | Responsable pressenti


CRITÈRE D'ACCEPTATION
La FDC est acceptée si :
- chaque ligne a une source citée ou est marquée VERROU ;
- aucun champ n'est renseigné sans niveau de fiabilité ;
- les VERROU sont en fin de fiche avec voie d'obtention ;
- aucune contradiction n'a été tranchée silencieusement ;
- aucune variable non lue par une brique n'est présente en FDC.
Si un seul de ces cinq points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} par le code projet. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « lisible sans ouvrir le CCTP » | La FDC est la référence des notes de calcul. Si elle ne porte pas les valeurs, chaque vérificateur (BC, BET, MOE) doit ouvrir le CCTP pour vérifier une note de calcul — ce qui est ingérable en pratique. La FDC porteuse des valeurs et de leurs sources est la seule forme opposable |
| « Aucune valeur de repli… aucune pratique courante » | C'est la faille la plus coûteuse de la conversation d'origine : 40 mm d'enrobage « au titre des exigences de tenue au feu du projet » ont été retenus sans que ces exigences existent. Cette clause interdit ce type de valeur non sourcée |
| « deux valeurs incompatibles → VERROU + RDR » | Traitement explicite de la contradiction XC2/35 mm vs XA3/50 mm du projet Flora : l'arbitrage est une décision RDR, pas une décision du modèle. Sans cette clause, un modèle peut « choisir » la valeur la plus favorable |
| « aucune variable non lue n'apparaît » | Évite la FDC « pour faire complet » qui vous obligeait à remplir des champs inutiles. Une FDC courte et exacte est plus utile qu'une FDC longue et remplie de champs vides |
| « tu signales l'écart et tu t'arrêtes » | Pas de FDC partielle silencieuse. Une FDC partielle présentée comme complète est une FDC qui sera lue comme complète — et les notes de calcul qui s'appuient dessus seront fausses |
| Niveau de fiabilité obligatoire | Un vérificateur doit pouvoir distinguer d'un coup d'œil une valeur contractuelle (que personne ne peut contester) d'une valeur de travail (qui peut être révisée). Sans cette distinction, toutes les valeurs sont traitées au même niveau — ce qui est faux |

Les trois niveaux de fiabilité — précision utile :

| Niveau | Signification | Conséquence en cas de désaccord |
| --- | --- | --- |
| Contractuelle | Issue d'une pièce du marché (CCTP, plan, marché) | Ne se conteste pas unilatéralement ; doit passer par un avenant ou une décision MOA |
| Décision | Issue d'un arbitrage inscrit au RDR (auteur, date, justification) | Peut être révisée par une nouvelle décision RDR, avec traçabilité |
| À confirmer | Hypothèse de travail, non validée | Doit être confirmée avant exécution ; le livrable qui l'utilise porte une réserve |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-00 (Inventaire des pièces) | La référence exacte des pièces (fichier + folio + indice) |
| B-01 (Proposition de la matrice) | La MPD validée — B-02 ne remplit que les variables que B-01 a statuées FOURNIE, PARTIELLE, BLOQUANTE ou À PRODUIRE PAR GO |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les VERROU listés en fin de FDC — B-03 les inscrit au Registre des Verrous (section 3) |
| B-04 (Plan de travail dégradé) | Les VERROU et les briques suspendues — B-04 produit le plan de travail dégradé à partir de ces informations |
| B-22 (Note d'hypothèses de conception) | Les valeurs et leur fiabilité — les valeurs À confirmer deviennent des hypothèses H-xx |
| B-24 (Vérification d'éléments existants non) | Les données disponibles sur l'existant (EXI-01 à EXI-04) — B-24 les cite, mais ne les complète pas |
| B-25 (Stabilité globale, contreventement, joints) | La zone sismique, la catégorie d'importance, la classe de sol et les coefficients |
| B-40 (Fondations superficielles) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-41 (Fondations profondes) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-42 (Verticaux BA) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-43 (Planchers et dallages) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-44 (Charpente bois) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-45 (Structure métallique) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-46 (Maçonnerie : vérification) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-47 (Escaliers) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-48 (Prédalles et planchers préfabriqués) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-49 (Linteaux et seuils) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-50 (Assemblages et ancrages) | Les valeurs et leur fiabilité — chaque brique de calcul vérifie qu'une valeur est Contractuelle ou Décision avant de l'utiliser en mode COMPLET |
| B-60 (Plans d'exécution) | Les valeurs utilisées dans les plans (matériaux, niveaux, positions) |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les variables BLOQUANTE — T-04 les cite comme objets de demande |

Variables consommées

| Code | Libellé | Statut dans B-02 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE (pour l'en-tête de sortie) |
| Toutes les variables statuées FOURNIE, PARTIELLE, BLOQUANTE ou À PRODUIRE PAR GO par B-01 | Selon la variable | Selon le statut |
| NIV-07 | Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB / Fini | BLOQUANTE |

Variables produites
B-02 ne produit pas une variable au sens du dictionnaire : sa sortie est la FDC, qui contient les valeurs de toutes les variables retenues. La FDC est un document, pas une variable.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | Les 106 variables, avec leur nature (bloque/mentionnée) | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| MPD (sortie B-01) | Statut de chaque variable pour le projet en cours | Document de projet |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus important de cette brique : à la sortie de B-02, vous devez valider chaque valeur et valider son niveau de fiabilité. C'est le moment où vous décidez ce qui est contractuel, ce qui est votre décision, et ce qui est votre hypothèse de travail. Un modèle qui remplit la FDC avec des valeurs non sourcées produit une FDC qui ne vaut rien.
Cas particulier — valeur déclarée en mode PARTIEL-DÉCLARÉ : si vous avez déjà pris une décision RDR (par exemple, retenir XA3 en lieu et place de XC2), la FDC porte la valeur (XA3), la source (« Décision D-01 du 17/10/2026 ») et la fiabilité (« Décision »). La valeur XC2 du CCTP n'est pas effacée : elle est listée en VERROU (« contradiction XC2 vs XA3 »), et la décision RDR est citée dans la ligne.
Cas particulier — variable À PRODUIRE PAR GO : si AC-03 (BET structure de conception) est À PRODUIRE PAR GO, la FDC ne porte pas de valeur pour cette variable — elle est listée en VERROU avec la brique B-20 en mode INTERNE-GO comme producteur. La sortie de B-20 deviendra l'entrée des briques de calcul, sans passer par une nouvelle FDC (B-20 produit son propre dossier de conception).
Cas particulier — conflit entre deux pièces : si le CCTP dit XA4 et la décision RDR dit XA3, la FDC porte XA3 en valeur, Décision D-xx en fiabilité, et XA4 (CCTP, réf.) en VERROU. Le conflit n'est pas tranché en silence : il est tracé.
Format de sortie attendu : deux tableaux distincts — tableau 1 (variables résolues avec valeur, source, fiabilité), tableau 2 (VERROU avec brique suspendue et voie d'obtention). Chaque ligne du tableau 1 a impérativement une source citée.
Consignation : la FDC validée est annexée au RDR (B-03) comme décision D-xx (« validation de la FDC en date du … »). Elle est mise à jour à chaque nouvelle décision RDR qui modifie une valeur.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).