Fichier 08_PHASE_6_CLOTURE/B-72_Journal_Cloture.md — CARNAC v3.0
________________


B-72 — JOURNAL DE CLÔTURE DU PROJET
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 6 — Vérification croisée et clôture |
| Brique précédente | B-70 (Auto-contrôle de synthèse), B-71 (Indiçage) |
| Brique suivante | Aucune — B-72 clôt la production. Les points ouverts sont traités par T-04, les incidents par T-03 |
| Fréquence | Une fois en fin de projet (après B-70 et B-71 pour l'ensemble du projet) |
| Modes d'appel | COMPLET uniquement (le journal de clôture est un document formel) |
| Entrées lues | RDL (registre des livrables), RDR (décisions, réserves, verrous), B-70 (verdicts de cohérence par livrable), B-71 (état documentaire), toutes les briques exécutées et leurs modes |
| Sortie unique | Journal de clôture en trois sections : (1) livrables produits, (2) points ouverts, (3) synthèse et recommandations |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : une seule fois en fin de projet, après B-70 (tous les livrables sont cohérents) et B-71 (tous les documents sont indicés). C'est le document qui clôt la production — il liste ce qui a été fait, ce qui reste à faire, et il récapitule les points ouverts à traiter.
Ce que vous fournissez à l'IA : le RDL, le RDR, les verdicts B-70 pour chaque livrable, l'état documentaire B-71, et la liste des briques exécutées (avec leur mode). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * la section 1 (livrables produits, avec mode d'exécution) ;
   * la section 2 (points ouverts, en quatre sous-sections : verrous, réserves, décisions en attente, hypothèses à confirmer) ;
   * la section 3 (synthèse, points de vigilance, recommandations) ;
   * la mention finale (les points ouverts restent à traiter).
Ce que B-72 produit — le périmètre exact :

| Section | Contenu | Fonction |
| --- | --- | --- |
| Section 1 — Livrables produits | Liste exhaustive : code, intitulé, indice, date, brique source, mode d'exécution, statut | Ce qui a été remis |
| Section 2 — Points ouverts | Quatre sous-sections : verrous V-xx, réserves R-xx, décisions en attente, hypothèses à confirmer | Ce qui reste à traiter |
| Section 3 — Synthèse | Bilan de la production, points de vigilance pour l'exécution, recommandations | Ce qui est à retenir |

Ce que B-72 ne produit jamais :

| Exclu | Renvoyé à |
| --- | --- |
| Révision des documents | Brique responsable |
| Indiçage et supersession | B-71 |
| Auto-contrôle de cohérence | B-70 |
| Suivi de l'exécution des travaux | Hors périmètre CARNAC |
| Nouvelle analyse du projet | Hors périmètre de B-72 (B-72 clôt, il ne réouvre pas) |

La règle la plus importante : B-72 clôt la production formelle — les études sont remises. Il ne clôt pas substantiellement le projet : les points ouverts (verrous, réserves, décisions en attente, hypothèses à confirmer) restent à traiter. C'est cette distinction qui vous protège en cas de litige — elle prouve que vous avez remis les études et signalé les réserves.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir le journal de clôture du projet {{ID-01}} — {{ID-02}}, à partir du RDL, du RDR, des verdicts B-70 et de l'état documentaire B-71. Le journal comporte trois sections distinctes : livrables produits, points ouverts, synthèse et recommandations.


MÉTHODE — DANS CET ORDRE


SECTION 1 — LIVRABLES PRODUITS
Tableau : code | intitulé | indice | date | brique source | mode d'exécution | statut (en vigueur / superseded / annulé).
Regroupe par famille : notes de calcul, plans, nomenclatures, notices, auto-contrôles.
Pour chaque famille, une ligne de total (nombre de documents émis).
Signale les documents émis en mode PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE : ce sont les documents qui portent une réserve intrinsèque.


SECTION 2 — POINTS OUVERTS
Quatre sous-sections obligatoires, aucune ne peut être vide sans justification.


2.1 — Verrous (V-xx)
Tableau : n° verrou | donnée manquante | brique suspendue | responsable de l'obtention | échéance | briques exécutées malgré tout.


2.2 — Réserves (R-xx)
Tableau : n° réserve | objet | statut (ouverte / fermée) | responsable | échéance.


2.3 — Décisions en attente
Tableau : objet de la décision | brique concernée | destinataire (MOE / MOA / BET / BC) | conséquence de la décision sur les livrables.


2.4 — Hypothèses à confirmer (H-xx)
Tableau : n° hypothèse | valeur retenue | brique impactée | voie de confirmation (essai / décision / relevé).


SECTION 3 — SYNTHÈSE ET RECOMMANDATIONS
- Bilan de la production : nombre de livrables, nombre de briques exécutées, modes d'exécution respectés ou non.
- Points de vigilance pour l'exécution : ce que l'entreprise doit savoir avant de commencer (hypothèses actives, réserves, points de principe).
- Recommandations pour la suite : essais à commander, visas à obtenir, décisions à prendre, missions complémentaires à recommander.
- Mention finale : « Le présent journal clôture la production des études d'exécution. Il ne clôt pas le projet : les points ouverts en section 2 restent à traiter. »


INTERDICTIONS
- Ne produis pas un journal sans les trois sections : une section vide sans justification est une anomalie.
- N'omets aucun point ouvert : un point ouvert omis est un point qui sera oublié.
- Ne mets pas une section 2 vide « parce qu'il n'y a pas de verrou » : même sans verrou, tu écris « aucun verrou ouvert à la date de clôture ».
- Ne déclare pas le projet clos si des points ouverts restent à traiter : la clôture est formelle, pas substantielle.
- Ne mentionne pas de visas non requis : seuls les visas effectivement nécessaires sont listés.
- Ne fusionne pas les livrables et les points ouverts dans une seule section : ce sont deux vues distinctes de l'état du projet.


SORTIE
Pièce unique — Journal de clôture, structuré en sections 1, 2 et 3, avec tableaux et mention finale.


CRITÈRE D'ACCEPTATION
Le journal est accepté si :
- la section 1 liste tous les livrables avec indice, date, brique source, mode et statut ;
- les livrables en mode PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE sont signalés ;
- la section 2 comporte les quatre sous-sections (verrous, réserves, décisions en attente, hypothèses à confirmer), chacune renseignée ou explicitement vide ;
- chaque point ouvert a un responsable et une échéance ;
- la section 3 contient le bilan, les points de vigilance et les recommandations ;
- la mention finale figure et rappelle que les points ouverts restent à traiter ;
- le journal ne déclare pas le projet clos substantiellement tant que des points ouverts subsistent.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Trois sections distinctes | Votre choix — un journal qui ne liste que les livrables émis omet les points ouverts, alors que ce sont précisément ces points qui conditionnent la suite (exécution, réception) |
| Section 2 divisée en quatre sous-sections | Verrous, réserves, décisions en attente, hypothèses à confirmer : quatre natures différentes, avec quatre interlocuteurs différents. Les fusionner conduit à des oublis |
| Signalement des modes PARTIEL-DÉCLARÉ et PARAMÉTRIQUE | Un livrable en mode dégradé porte une réserve intrinsèque qui doit être vue en clôture. Sinon, l'entreprise reçoit un livrable qu'elle croit ferme alors qu'il ne l'est pas |
| Chaque point ouvert avec responsable et échéance | Un point ouvert sans responsable ne se traite jamais. Sans échéance, il se traite trop tard |
| « Ne déclare pas le projet clos si des points ouverts subsistent » | La clôture est formelle (les études sont remises), pas substantielle (les points ouverts restent). Confondre les deux est la principale source de litige en fin de projet |
| Mention finale explicite | La mention qui rappelle que les points ouverts restent à traiter est la protection de l'entreprise : elle prouve qu'elle a remis les études et signalé les réserves |
| « Ne fusionne pas livrables et points ouverts » | Ce sont deux vues distinctes : ce qui est remis, et ce qui reste à traiter. Les fusionner brouille la lecture en réunion de clôture |
| « Ne produis pas un journal sans les trois sections » | Une section vide sans justification est une anomalie — elle masque un défaut de production. Le journal doit couvrir les trois sections, même si l'une est explicitement vide |
| « Ne mets pas une section 2 vide parce qu'il n'y a pas de verrou » | Même sans verrou, la section 2 doit être renseignée avec la mention « aucun verrou ouvert à la date de clôture ». C'est la preuve que la vérification a été faite |
| « Ne déclare pas le projet clos substantiellement » | La clôture formelle (remise des études) n'est pas la clôture substantielle (tous les points ouverts traités). Le journal doit refléter cette distinction — sinon, il engage votre responsabilité sur des points non traités |

Les quatre sous-sections de la section 2 — précision utile :

| Sous-section | Nature | Interlocuteur habituel |
| --- | --- | --- |
| Verrous (V-xx) | Données manquantes qui suspendent des briques | Responsable de l'obtention (MOA, BET, GO) |
| Réserves (R-xx) | Objets à lever, avec statut ouvert/fermé | Responsable de l'obtention |
| Décisions en attente | Décisions à prendre (auteur, conséquence) | MOE, MOA, BET, BC |
| Hypothèses à confirmer (H-xx) | Hypothèses de travail non encore validées | Voie de confirmation (essai, décision, relevé) |

Le piège de la clôture substantielle : un modèle qui reçoit le RDL et le RDR a tendance à déclarer le projet clos parce que tous les livrables ont été produits. C'est exactement ce qu'il faut interdire :
   * les livrables ont été produits, mais les points ouverts (verrous, réserves, décisions, hypothèses) restent à traiter ;
   * la clôture est formelle (les études sont remises) — pas substantielle (tous les points sont traités) ;
   * déclarer le projet clos substantiellement engage votre responsabilité sur des points qui ne sont pas traités.
La mention finale est la protection : elle prouve que vous avez remis les études et signalé les réserves.
Le piège du mode PARAMÉTRIQUE : si un livrable est en mode PARAMÉTRIQUE (par exemple, un plan de fondations avec q_adm manquante), le journal doit explicitement le signaler dans la section 1. L'entreprise doit savoir que ce livrable n'est pas exécutable en l'état — sinon, elle risque de l'exécuter et de commettre une erreur grave.
Le piège de l'omission des points ouverts : un modèle a tendance à minimiser les points ouverts (par exemple, « quelques points à traiter ») pour présenter un projet « propre ». C'est exactement ce qu'il faut interdire :
   * chaque point ouvert omis est un point qui sera oublié à l'exécution ;
   * le journal est le document qui rassemble tous les points ouverts en un seul endroit lisible ;
   * c'est ce qui permet à la MOA de décider si le projet est suffisamment mûr pour être exécuté.
Le journal doit lister tous les points ouverts, pas les minimiser.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les réserves et verrous — B-72 liste les points ouverts qui restent à traiter après remise |
| B-04 (Plan de travail dégradé) | L'historique des PTD — B-72 liste les points ouverts qui restent à traiter après remise |
| B-15 (Fiche de synthèse) | Les risques résiduels — B-72 les intègre dans la section « points ouverts » |
| B-22 (Note d'hypothèses de conception) | Les hypothèses non confirmées — B-72 les liste dans les points ouverts |
| B-41 (Fondations profondes) | Les recommandations de mission — B-72 liste les points ouverts |
| B-64 (Notice de synthèse) | La notice — B-72 la cite dans la liste des livrables produits |
| B-70 (Auto-contrôle déclaré de synthèse) | Le verdict de B-70 — B-72 liste les points ouverts à traiter avant remise |
| B-71 (Indiçage et supersession documentaire) | La liste des documents en vigueur — B-72 la cite dans le journal |
| T-04 (Prompt de demande) | Les demandes non répondues à la date de clôture — B-72 les cite dans les points ouverts |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-03 (Prompt de méta-amélioration) | Le journal de clôture — T-03 s'appuie dessus pour proposer des corrections au carnet |
| T-04 (Prompt de demande) | Les points ouverts (verrous, réserves, décisions en attente) — T-04 les transforme en demandes formelles à la MOE/BET/MOA |

Variables consommées

| Code | Libellé | Statut dans B-72 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| ID-05 | Indice du dossier en vigueur | BLOQUANTE |
| DEC-02 | Décisions inscrites au RDR | BLOQUANTE |
| DEC-03 | Verrous ouverts | BLOQUANTE |
| DEC-04 | Documents supersédés | BLOQUANTE |

Variables produites
B-72 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (journal de clôture) qui alimente T-04, T-03 et les destinataires externes.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, ID-05, DEC-02, DEC-03, DEC-04 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-72, vous devez valider la liste des points ouverts avant transmission à la MOA. Certains points peuvent être acceptés par votre décision (par exemple, un verrou dont la donnée est arrivée après la production du journal), d'autres non. C'est votre appréciation qui fait foi — et c'est vous qui décidez quels points doivent être traités avant la remise.
Cas particulier — aucun point ouvert : si le projet n'a aucun point ouvert (ce qui est rare, mais possible), la section 2 est renseignée avec la mention « aucun verrou ouvert, aucune réserve ouverte, aucune décision en attente, aucune hypothèse à confirmer à la date de clôture ». Ce n'est pas une section vide — c'est une section explicitement sans point ouvert.
Cas particulier — livrables en mode dégradé : si des livrables ont été émis en mode PARTIEL-DÉCLARÉ ou PARAMÉTRIQUE, la section 1 les signale explicitement, et la section 2 les reprend (hypothèses à confirmer, décisions en attente). Un livrable PARAMÉTRIQUE qui n'apparaît pas dans la section 2 est une anomalie — il porte une réserve intrinsèque qui doit être tracée.
Cas particulier — plusieurs livrables du même type : si le projet comporte plusieurs livrables du même type (par exemple, plusieurs plans de fondations pour des zones différentes), la section 1 les liste tous, avec leur code et leur indice. Un livrable regroupé (par exemple, « plans de fondations : 3 plans ») est une anomalie — chaque livrable doit être identifiable.
Cas particulier — projet multi-lots : si le projet comporte plusieurs lots (par exemple, lot GO et lot charpente), le journal de clôture est propre au lot GO — il ne couvre pas les autres lots. Les interfaces avec les autres lots sont mentionnées dans les points ouverts (section 2.3 — décisions en attente), mais le journal ne clôt pas les autres lots.
Cas particulier — clôture partielle : si le projet est clôturé par phases (par exemple, phase 1 : fondations, phase 2 : superstructure), chaque phase a son propre journal de clôture. Le journal de la phase 1 liste les points ouverts pour la phase 1 — et les interfaces avec la phase 2. Le journal de clôture final agrège les journaux des phases.
Format de sortie attendu : journal unique (5 à 10 pages), structuré en sections 1, 2 (avec 4 sous-sections), 3, et mention finale. Le journal porte le filigrane si un ou plusieurs livrables sont en mode PARAMÉTRIQUE.
Consignation : le journal de clôture B-72 est consigné au RDL (comme document de clôture) et transmis aux destinataires (MOA, MOE, BC, BET). C'est le document qui prouve que les études ont été remises et que les réserves ont été signalées.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).