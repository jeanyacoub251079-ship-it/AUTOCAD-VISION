Fichier 03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md — CARNAC v3.0
________________


B-15 — FICHE DE SYNTHÈSE DES RISQUES
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | 2 — Audit croisé multi-pièces |
| Brique précédente | B-13 (Contradictions) — ou l'ensemble de la phase 1 |
| Brique suivante | B-20 (Conception GO) — ou la première brique de la phase 2 selon le PTD |
| Modes d'appel | COMPLET (périmètre d'analyse complet) · PARTIEL-DÉCLARÉ (périmètre limité à B-13 seule, décidé par vous) |
| Paramètre d'appel | {{périmètre_analyse}} = « B-13 seule » ou « ensemble de la phase Analyse » (B-10 à B-14) |
| Entrées lues | Selon {{périmètre_analyse}} : B-13 seule, ou B-10 + B-11 + B-12 + B-13 + B-14 |
| Sortie unique | Fiche de synthèse hiérarchisée des risques : cotation P×I, responsable, mesure de maîtrise, échéance |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique : après B-13 (ou après l'ensemble de la phase 1, selon votre choix). B-15 est la dernière brique de la phase 1 — elle synthétise les constats, contradictions et données manquantes en registre de risques hiérarchisé.
Ce que vous fournissez à l'IA : selon le paramètre {{périmètre_analyse}} :
   * « B-13 seule » : uniquement la sortie de B-13 (tableau des contradictions qualifiées) ;
   * « ensemble de la phase Analyse » : les sorties de B-10, B-11, B-12, B-13, B-14.
Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}}, {{ID-02}} et {{périmètre_analyse}}.
Ce que vous validez à la sortie :
   * la cotation P × I de chaque risque (avec justification) ;
   * la mesure de maîtrise (action de pilotage, pas solution technique) ;
   * le responsable et l'échéance ;
   * les risques résiduels acceptés (c'est l'engagement qui vous engage).
Ce que B-15 apporte de spécifique — la distinction risque / contradiction :

| Notion | Ce qu'elle est | Ce qu'elle produit |
| --- | --- | --- |
| Contradiction (B-13) | Un état du dossier : deux pièces affirment des choses incompatibles | Un tableau qualifié, des verrous et réserves |
| Risque (B-15) | Un événement redouté : probabilité × impact, avec conséquence possible | Un registre hiérarchisé, avec mesures de maîtrise |

Une contradiction produit un ou plusieurs risques. Mais un risque peut aussi naître d'une lacune (B-10, B-11, B-12) ou d'une imprécision, pas seulement d'une contradiction. C'est pourquoi B-15 est une brique distincte, pas un simple sous-produit de B-13.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : établir la fiche de synthèse des risques de l'opération {{ID-01}} — {{ID-02}}, à partir du périmètre d'analyse que je t'indique ci-dessous.


PÉRIMÈTRE D'ANALYSE (paramètre obligatoire)
{{périmètre_analyse}} = « B-13 seule » ou « ensemble de la phase Analyse ».
Si « B-13 seule » : tu ne lis QUE la sortie de B-13. Tu n'inventes aucun risque hors B-13.
Si « ensemble de la phase Analyse » : tu lis B-10, B-11, B-12, B-13 et B-14.


DÉFINITIONS
- RISQUE : événement redouté, avec une probabilité et un impact, et un rattachement obligatoire à une source (une ligne de B-10, B-11, B-12, B-13 ou B-14).
- Un risque n'est PAS une contradiction, une lacune ou une imprécision : c'est la conséquence possible de cette contradiction, lacune ou imprécision sur nos études, notre planning ou notre responsabilité.
- MESURE DE MAÎTRISE : action de pilotage (demande d'information, décision RDR, production en PARAMÉTRIQUE, confirmation écrite, inscription au RDR, commande de mission complémentaire). Ce N'EST PAS une solution technique.


COTATION
Probabilité (P) et impact (I) sur une échelle 1 à 3 :
- P1 : improbable (< 20 %)
- P2 : possible (20-60 %)
- P3 : probable (> 60 %)
- I1 : faible (retard < 1 semaine, ou impact mineur sur la note de calcul)
- I2 : moyen (retard 1 à 4 semaines, ou impact limité sur un livrable)
- I3 : fort (retard > 4 semaines, ou impact sur la sécurité, la conformité, ou notre responsabilité)
Criticité = P × I : 1-2 faible / 3-4 moyenne / 6-9 élevée.
Chaque cotation P et I doit être justifiée en une phrase courte — une cotation sans justification est rejetée.


MÉTHODE
1. Extrais tous les risques rattachables aux sources du périmètre d'analyse.
2. Élimine les doublons : deux formulations d'un même risque = un seul risque.
3. Cote chaque risque (P, I), en justifiant chaque cote en une phrase.
4. Identifie pour chaque risque : la brique CARNAC impactée, la mesure de maîtrise, le responsable (MOE / MOA / BET / BC / GO / OPC), et l'échéance (avant remise / avant démarrage / pendant EXE / à surveiller).
5. Hiérarchise par criticité décroissante.
6. Identifie les risques résiduels : ceux qu'on accepte de porter, avec justification.


INTERDICTIONS
- N'invente aucun risque : tout risque est rattaché à une source citée (B-xx, ligne n°).
- Ne confonds pas risque et contradiction : une contradiction produit un ou plusieurs risques, mais un risque peut naître d'une lacune ou d'une imprécision.
- Ne propose aucune solution technique comme mesure de maîtrise.
- Ne cote pas sans justifier : « P3 parce que la donnée est absente depuis deux mois » est une justification ; « P3 » seul ne l'est pas.
- Ne mets pas un risque sans responsable et sans échéance.
- Ne fusionne pas deux risques distincts pour « faire court » : la fiche peut faire plusieurs pages.


SORTIE
Tableau principal — Registre des risques :
N° | Risque (formulation en une phrase, au conditionnel) | Source (B-xx, ligne n°) | Nature (technique / contractuelle / d'interface / planning / réglementaire) | P (1-3) | Justification P | I (1-3) | Justification I | Criticité (P×I) | Brique impactée | Mesure de maîtrise | Responsable | Échéance


Tableau secondaire — Risques résiduels acceptés :
N° | Risque | Justification de l'acceptation | Responsable du suivi


Puis une synthèse de 10 lignes maximum :
- les trois risques de criticité élevée ;
- les risques qui impactent directement la remise de nos livrables ;
- les risques qui impactent notre responsabilité contractuelle ;
- les risques résiduels acceptés et leur justification.


CRITÈRE D'ACCEPTATION
La fiche est acceptée si :
- chaque risque est rattaché à une source citée ;
- chaque cotation P et I est justifiée ;
- chaque risque a un responsable et une échéance ;
- la mesure de maîtrise est une action de pilotage, pas une solution technique ;
- les risques résiduels sont identifiés et justifiés ;
- la synthèse tient en 10 lignes ;
- si le périmètre est « B-13 seule », aucun risque n'est introduit hors B-13.
Si un seul de ces sept points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}}, {{ID-02}} et {{périmètre_analyse}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| Paramètre {{périmètre_analyse}} explicite | Votre arbitrage : B-15 peut tourner seule sur B-13, ou sur toute la phase 1. Sans paramètre explicite, le modèle prend l'initiative — et sur B-13 seule, il peut « enrichir » avec des risques inventés hors B-13 |
| « Si B-13 seule : tu ne lis QUE B-13 » | Verrou anti-hallucination pour le mode limité. Le périmètre d'analyse est le seul qui définit ce qui peut être dit — un risque hors périmètre est un risque inventé |
| Définition RISQUE ≠ CONTRADICTION | Le risque est un événement redouté (probabilité × impact), la contradiction est un état du dossier. Confondre les deux produit une fiche illisible et sans hiérarchisation utile — et fait perdre la valeur ajoutée de B-15 (qui est d'identifier les conséquences possibles) |
| « MESURE DE MAÎTRISE : action de pilotage, pas solution technique » | Empêche B-15 de devenir une brique de conception. La maîtrise d'un risque « G3 non commandée » est « demander la commande du G3 », pas « utiliser 0,25 MPa au lieu de 0,30 ». C'est la frontière avec B-20 et B-40 à B-50 |
| Cotation P et I avec justification obligatoire | Une cotation sans justification est une note arbitraire — elle ne se défend pas en réunion. « P3 parce que la donnée est absente depuis deux mois » est une justification ; « P3 » seul ne l'est pas |
| Échelle P×I 1-3 plutôt que 1-5 | Sur des études d'exécution, une échelle fine (1-5) donne une fausse précision. Le 1-3 est plus robuste (moins de subjectivité) et plus rapide à coter en réunion de lancement |
| Tableau des risques résiduels | Un risque non identifié comme résiduel est un risque qu'on oublie. Le tableau l'oblige à être nommé et accepté formellement — c'est l'engagement qui vous engage |
| « Responsable + échéance » obligatoires | Un risque sans responsable ne se traite jamais ; un risque sans échéance est traité trop tard. Les deux colonnes rendent la fiche actionnable |
| « Ne fusionne pas deux risques distincts pour faire court » | La tentation de fusionner pour « faire propre » produit des fiches courtes mais inutilisables — un risque fusionné perd son responsable et son échéance. Une fiche longue et exacte vaut mieux qu'une fiche courte et fausse |
| Synthèse en 10 lignes | La fiche de synthèse est faite pour la réunion de lancement, pas pour la lecture exhaustive. Les 10 lignes forcent la hiérarchisation et permettent une présentation orale |

Les cinq natures de risque — précision utile :

| Nature | Définition | Exemple |
| --- | --- | --- |
| Technique | Risque lié à une incertitude technique (donnée manquante, méthode non validée, hypothèse non confirmée) | « Si q_adm n'est pas confirmée, les semelles dimensionnées en PARAMÉTRIQUE ne seront pas exécutables » |
| Contractuelle | Risque lié à un périmètre ambigu ou à une prestation non tranchée | « Si la prestation de reprise en sous-œuvre de la passerelle est refusée par la MOA, notre prix est faux » |
| D'interface | Risque lié à une interface entre lots | « Si le lot charpente n'est pas attribué avant notre démarrage, nos sommiers sont posés sans appuis » |
| Planning | Risque lié à un délai (donnée tardive, visa tardif, décision tardive) | « Si le visa BET n'est pas obtenu avant le 15/11, le livrable est remis en PARAMÉTRIQUE » |
| Réglementaire | Risque lié à une exigence réglementaire non satisfaite | « Si SEC-01 n'est pas fourni, l'enrobage de nos poteaux n'est pas conforme ERP » |

________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-03 (Registre des décisions) | Les décisions et verrous déjà inscrits — B-15 en tient compte pour ne pas dupliquer un risque déjà traité |
| B-10 (Audit critique du CCTP) | Les points à lever et les prescriptions à confirmer — B-15 les intègre dans le registre des risques |
| B-11 (Audit du diagnostic structure) | Les zones non relevées et les données manquantes — B-15 les intègre dans le registre des risques |
| B-12 (Audit des pièces géotechniques) | Les données manquantes et les recommandations de mission — B-15 les intègre dans le registre des risques |
| B-13 (Détection et qualification) | Les contradictions qualifiées — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise, responsable) |
| B-14 (Clarification du périmètre) | Les prestations À TRANCHER — B-15 les transforme en risques (probabilité × impact, mesure de maîtrise) |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| B-03 (Registre des décisions) | Les risques identifiés — chaque risque de criticité élevée devient une réserve R-xx (ou un verrou V-xx si le risque est déjà bloquant) |
| B-20 (Conception structure GO) | Les risques techniques (incertitudes sur les hypothèses) — B-20 les intègre dans sa note d'hypothèses (B-22) |
| B-72 (Journal de clôture) | Les risques résiduels — B-72 les intègre dans la section « points ouverts » |
| T-01 (Prompt de sincérité) | Le livrable à vérifier — T-01 s'applique à n'importe quel livrable |
| T-04 (Prompt de demande) | Les risques avec responsable et échéance — T-04 les transforme en demande formelle à la MOE / BET / MOA |

Variables consommées

| Code | Libellé | Statut dans B-15 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-03 | Verrous ouverts (via B-03) | NON BLOQUANTE (si B-03 n'est pas encore consultée, B-15 peut encore identifier les risques, mais elle doit signaler l'absence) |

Variables produites
B-15 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (fiche de synthèse des risques) qui alimente B-03, B-20, T-04 et B-72.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | DEC-03, ID-01, ID-02 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de B-15, vous devez valider les risques résiduels acceptés. C'est l'engagement qui vous engage — un risque que vous acceptez de porter est un risque que vous ne pourrez plus reprocher à la MOE en cas de réalisation. C'est votre décision, pas celle du modèle.
Cas particulier — périmètre « B-13 seule » : si vous choisissez le périmètre limité à B-13, B-15 ne lit que les contradictions qualifiées par B-13. Elle ne voit pas les lacunes de B-10, les zones non relevées de B-11, les données manquantes de B-12, ni les prestations À TRANCHER de B-14. Le périmètre limité est utile en cours de projet (après B-13, avant que les autres briques de la phase 1 ne soient terminées), mais il ne remplace pas une synthèse complète.
Cas particulier — périmètre « ensemble de la phase Analyse » : si vous choisissez le périmètre complet, B-15 lit l'ensemble de la phase 1. C'est la synthèse de référence, à utiliser en fin de phase 1 avant de passer à la phase 2.
Cas particulier — risque de criticité élevée sans mesure de maîtrise : si un risque est coté criticité 6 à 9 (élevée) mais qu'aucune mesure de maîtrise n'est identifiée, B-15 le signale explicitement. Un risque de criticité élevée sans mesure de maîtrise est une anomalie — soit le risque n'est pas correctement coté, soit il manque une action de pilotage.
Cas particulier — risque résiduel accepté : un risque résiduel est un risque qu'on accepte de porter parce que :
   * la mesure de maîtrise coûte plus cher que le risque lui-même ;
   * le risque est en dehors de notre périmètre mais on décide de le porter quand même ;
   * la MOA a explicitement accepté le risque.
Le tableau des risques résiduels documente pourquoi le risque est accepté, et qui le suit.
Cas particulier — risque déjà traité par une décision RDR : si un risque est déjà couvert par une décision RDR (par exemple, « risque de q_adm insuffisante — décision D-03 de produire en PARAMÉTRIQUE »), B-15 le mentionne avec la référence à la décision. Il n'est pas recopié sans mention — c'est la règle de non-redondance avec B-03.
Format de sortie attendu : un tableau principal (registre des risques) à 13 colonnes, un tableau secondaire (risques résiduels) à 4 colonnes, suivis d'une synthèse en 10 lignes maximum.
Consignation : la fiche B-15 est annexée au RDR (B-03) — chaque risque de criticité élevée devient une réserve (R-xx) avec responsable et échéance ; les risques résiduels acceptés sont consignés dans une section dédiée du RDR.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Pré-Audit Flash d'Exécutabilité obligatoire.** Avant toute production, B-15 contrôle par ratios l'exécutabilité de l'ensemble du dossier, **y compris lorsqu'un BET structure MOE existe** : élancement de flèche sous maçonnerie (`L/h`), portance et dimension minimale des semelles (`q_Ed` vs `q_adm`, `B_min`), élancement des poteaux (`H_0/b`), compression locale sous appuis et sous appareils d'appui. Un ratio hors bornes produit un risque de criticité élevée et une demande de complément `T-04`, jamais un silence.