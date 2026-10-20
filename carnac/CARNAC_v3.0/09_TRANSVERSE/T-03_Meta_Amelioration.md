Fichier 09_TRANSVERSE/T-03_Meta_Amelioration.md — CARNAC v3.0
________________


T-03 — PROMPT DE MÉTA-AMÉLIORATION
1. EN-TÊTE

| Champ | Valeur |
| --- | --- |
| Version | 3.0 |
| Dernière révision | v3.0 — refonte majeure (voir Journal des modifications, entrée v3.0) ; fond de la fiche conservé et enrichi |
| Phase | Transverse — à tout moment |
| Brique précédente | B-72 (Journal de clôture) — ou T-02 (Recadrage) en cas d'incident significatif |
| Brique suivante | Nouvelle version du carnet CARNAC (v3.x) — voir Annexe C |
| Modes d'appel | COMPLET uniquement |
| Entrées lues | Le carnet CARNAC (v3.0), le journal de clôture du projet (B-72), les corrections effectuées (T-02), les points ouverts (RDR) |
| Sortie unique | Proposition de correction au carnet : brique(s) concernée(s), nature de la correction, justification, impact, classement GÉNÉRALE / PROJET / À ÉTUDIER |
| Critère d'acceptation | Voir section 2 (dernier bloc du prompt) |

Quand appeler cette brique :
   * après chaque projet terminé — pour transformer les incidents en améliorations ;
   * après un incident significatif (T-02 déclenché) — pour éviter que l'incident se reproduise sur un autre projet ;
   * après l'ajout ou la suppression d'une brique — pour maintenir la cohérence du carnet.
Ce que vous fournissez à l'IA : le carnet CARNAC (version en vigueur), le journal de clôture du projet (B-72), les corrections effectuées (T-02), les points ouverts (RDR). Vous copiez uniquement le bloc de code de la section 2, en ayant remplacé {{ID-01}} et {{ID-02}}.
Ce que vous validez à la sortie :
   * l'inventaire des incidents et corrections ;
   * l'analyse de chaque incident (brique concernée, nature du problème, conséquence) ;
   * les propositions de correction (brique, clause, justification, impact) ;
   * le tri en trois catégories : GÉNÉRALE (à intégrer au carnet), PROJET (reste dans le RDR du projet), À ÉTUDIER (nécessite validation) ;
   * la proposition de version (si des corrections générales sont retenues).
Ce que T-03 apporte de spécifique — la boucle d'apprentissage :

| Aspect | Correction de projet (T-02) | Méta-amélioration (T-03) |
| --- | --- | --- |
| Objet | Corriger un livrable défaillant | Améliorer le carnet qui a produit le livrable |
| Périmètre | Un livrable, un projet | Tous les projets futurs |
| Sortie | Version corrigée du livrable | Proposition de correction au carnet |
| Effet | Résout le problème actuel | Évite que le problème se reproduise |
| Boucle | Fermée (le livrable est corrigé) | Ouverte (le carnet évolue) |

T-03 est la brique qui transforme un incident en amélioration générale. C'est la boucle d'apprentissage qui fait progresser CARNAC d'une version à l'autre, par incréments de version mineure puis majeure.
La règle la plus importante : une correction n'entre au carnet que si elle est générale. Une correction propre à un projet reste dans le RDR de ce projet — elle ne pollue pas le carnet.
________________


2. PROMPT
text
Tu es ingénieur senior en études d'exécution gros œuvre/structure.


MISSION : analyser le projet {{ID-01}} — {{ID-02}} terminé (ou l'incident survenu) et proposer les corrections à apporter au carnet CARNAC. Tu ne modifies pas le carnet : tu proposes des corrections, à valider par l'utilisateur.


MÉTHODE


Étape 1 — Inventaire des incidents et corrections
Liste tous les incidents survenus pendant le projet :
- défauts de livrable (T-02 déclenchés) ;
- points ouverts qui n'auraient pas dû l'être (données non demandées, données demandées inutilement) ;
- blocages non anticipés (données manquantes non identifiées à la MPD) ;
- corrections manuelles effectuées (où le carnet n'a pas couvert un besoin).


Étape 2 — Analyse de chaque incident
Pour chaque incident :
- brique concernée (B-xx, T-xx) ;
- nature du problème (méthode, données, clause manquante, clause mal formulée) ;
- conséquence sur le livrable.


Étape 3 — Proposition de correction
Pour chaque incident, propose une correction générale (applicable à tous les projets) :
- brique(s) à modifier (version actuelle → version proposée) ;
- clause à ajouter, à modifier ou à supprimer ;
- justification (en quoi la correction évite la reproduction de l'incident) ;
- impact sur les autres briques (une correction à B-40 peut avoir un impact sur B-42 ou B-50).


Étape 4 — Tri des corrections
Classe les corrections en trois catégories :
- GÉNÉRALE : la correction s'applique à tous les projets, elle entre au carnet.
- PROJET : la correction est propre à ce projet, elle reste dans le RDR.
- À ÉTUDIER : la correction semble générale mais nécessite une validation ou un test avant d'entrer au carnet.


Étape 5 — Proposition de version
Si des corrections GÉNÉRALES sont retenues, propose une nouvelle version du carnet :
- numéro de version (vX.Y) ;
- liste des corrections intégrées ;
- entrée au journal des révisions (annexe C) ;
- impact sur les fiches existantes.


INTERDICTIONS
- Ne propose aucune correction propre à un seul projet comme correction générale.
- Ne propose aucune correction sans justification (en quoi elle évite la reproduction de l'incident).
- Ne propose pas de correction qui supprime un verrou sans le remplacer : la règle de non-régression (document maître §9) interdit la suppression sans remplacement.
- Ne modifie pas le carnet : tu proposes, l'utilisateur valide.
- Ne fusionne pas corrections GÉNÉRALE et corrections PROJET : ce sont deux destins différents.


SORTIE
Pièce 1 — Inventaire des incidents.
Pièce 2 — Analyse par incident.
Pièce 3 — Propositions de correction.
Pièce 4 — Tri GÉNÉRALE / PROJET / À ÉTUDIER.
Pièce 5 — Proposition de version (si corrections générales).


CRITÈRE D'ACCEPTATION
La proposition est acceptée si :
- chaque incident est listé et analysé ;
- chaque correction est justifiée ;
- chaque correction est classée en GÉNÉRALE / PROJET / À ÉTUDIER ;
- aucune correction projet n'est présentée comme générale ;
- aucune correction ne supprime un verrou sans remplacement ;
- la proposition de version est cohérente avec les corrections retenues.
Si un seul de ces six points n'est pas satisfait, tu signales l'écart et tu t'arrêtes.
Rappel V7 — zéro placeholder résiduel : avant d'envoyer ce prompt, remplacez {{ID-01}} et {{ID-02}}. Aucun {{...}} ne doit subsister.
________________


3. JUSTIFICATION DES CLAUSES CLÉS

| Clause | Pourquoi |
| --- | --- |
| « Ne modifie pas le carnet » | T-03 propose, l'utilisateur décide. Un modèle qui modifie son propre carnet est un modèle qui dérive — il peut introduire des corrections non validées, ou supprimer des clauses qui le gênent |
| Tri GÉNÉRALE / PROJET / À ÉTUDIER | La distinction est cruciale : une correction spécifique à un projet ne doit pas polluer le carnet. Sans ce tri, le carnet se remplit de cas particuliers et perd sa généralité — il devient inutilisable |
| Justification obligatoire | Une correction sans justification est une modification arbitraire. La justification (« en quoi elle évite la reproduction de l'incident ») est la seule protection contre les corrections « cosmétiques » |
| Non-suppression de verrou sans remplacement | La règle de non-régression protège le carnet contre les régressions. Une correction qui supprime un verrou sans le remplacer est une régression déguisée — elle peut sembler améliorer le carnet, mais elle le fragilise |
| Inventaire des points ouverts « qui n'auraient pas dû l'être » | Certains points ouverts sont légitimes (données manquantes réelles), d'autres sont des défauts du carnet (données non demandées, données demandées inutilement). C'est la distinction qui permet d'améliorer le carnet |
| Inventaire des corrections manuelles | Les corrections manuelles (où le carnet n'a pas couvert un besoin) sont les meilleurs indicateurs de lacunes du carnet. Elles révèlent ce que le carnet aurait dû faire mais n'a pas fait |
| Impact sur les autres briques | Une correction à B-40 peut avoir un impact sur B-42 ou B-50 (par exemple, si B-40 change la façon de calculer les semelles, B-50 doit être cohérent). L'impact doit être identifié pour éviter les incohérences |
| Proposition de version | Une correction générale sans proposition de version est une correction qui ne sera jamais intégrée. La proposition de version (vX.Y) est le mécanisme qui permet d'intégrer les corrections au carnet |
| « Ne fusionne pas GÉNÉRALE et PROJET » | Les deux catégories ont des destins différents : GÉNÉRALE entre au carnet, PROJET reste dans le RDR. Les fusionner conduit à des corrections qui entrent au carnet sans justification (ou qui restent dans le RDR alors qu'elles devraient être générales) |
| « Ne propose pas de correction qui supprime un verrou » | Les 15 verrous sont la protection du carnet contre les dérives. Une correction qui supprime un verrou est une régression — même si elle semble simplifier le carnet |

Les trois catégories de corrections — précision utile :

| Catégorie | Définition |
| --- | --- |
| Destin | GÉNÉRALE |
| La correction s'applique à tous les projets, elle corrige une lacune du carnet | Entre au carnet dans la prochaine version (vX.Y) |
| PROJET | La correction est propre à ce projet (par exemple, une donnée spécifique, une contrainte de site particulière) |
| Reste dans le RDR du projet | À ÉTUDIER |
| La correction semble générale, mais elle doit être testée ou validée avant d'entrer au carnet | Entre au carnet après validation (ou après un projet de test) |

Le piège de la « correction spécifique » : un modèle qui reçoit un incident de projet a tendance à proposer une correction spécifique (par exemple, « ajouter une clause pour le cas où le fichier DXF a des calques non nommés ») comme correction générale. C'est exactement ce qu'il faut interdire :
   * une correction spécifique à un projet pollue le carnet (elle ajoute une clause qui ne s'appliquera jamais ailleurs) ;
   * elle rend le carnet plus complexe sans le rendre plus utile ;
   * elle peut même être contradictoire avec d'autres clauses.
La règle est : une correction n'entre au carnet que si elle est générale — c'est-à-dire si elle s'applique à tous les projets, pas seulement à celui qui a révélé l'incident.
Le piège de la suppression de verrou : un modèle a tendance à proposer de supprimer un verrou qui le gêne (par exemple, « supprimer le verrou V7 sur les placeholders pour simplifier la rédaction »). C'est exactement ce qu'il faut interdire :
   * les 15 verrous sont la protection du carnet contre les dérives ;
   * supprimer un verrou, c'est supprimer une protection — c'est une régression ;
   * si un verrou est problématique, il doit être remplacé (par une clause équivalente ou meilleure), pas supprimé.
La règle de non-régression est la seule protection contre les corrections qui fragilisent le carnet.
Le piège de la « correction cosmétique » : un modèle a tendance à proposer des corrections cosmétiques (par exemple, « reformuler la clause X pour la rendre plus claire ») sans justification réelle. C'est exactement ce qu'il faut interdire :
   * une correction cosmétique sans justification est une modification arbitraire ;
   * elle peut introduire des ambiguïtés (la reformulation peut changer le sens) ;
   * elle ne résout aucun problème réel.
La règle est : une correction doit être justifiée — elle doit résoudre un problème identifié dans l'inventaire.
________________


4. RÉFÉRENCES
Briques amont

| Brique | Ce qu'elle fournit |
| --- | --- |
| B-72 (Journal de clôture) | Le journal de clôture — T-03 s'appuie dessus pour proposer des corrections au carnet |
| T-01 (Prompt de sincérité) | Les éléments à lever récurrents — T-03 propose des corrections au carnet |
| T-02 (Prompt de recadrage) | Le diagnostic et la nouvelle méthode — T-03 propose des corrections au carnet si le défaut est récurrent |

Briques aval

| Brique | Ce qu'elle consomme |
| --- | --- |
| Aucune — dernière brique de la chaîne | — |

Variables consommées

| Code | Libellé | Statut dans T-03 |
| --- | --- | --- |
| ID-01 | Code projet | BLOQUANTE |
| ID-02 | Intitulé de l'opération | BLOQUANTE |
| DEC-02 | Décisions inscrites au RDR | NON BLOQUANTE (si absentes, T-03 fonctionne sur les incidents seuls) |
| DEC-03 | Verrous ouverts | NON BLOQUANTE (si absents, T-03 fonctionne sur les incidents seuls) |

Variables produites
T-03 ne produit pas de variable au sens du dictionnaire : sa sortie est un document (proposition de correction) qui alimente la nouvelle version du carnet et l'annexe C.
Documents de référence

| Document | Contenu | Fichier |
| --- | --- | --- |
| Document maître | Principes, verrous, modes | 00_MASTER.md |
| Dictionnaire de variables | ID-01, ID-02, DEC-02, DEC-03 | 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv |
| Journal des révisions | Versions du carnet | 10_ANNEXES/C_Journal_Revisions.md |
| Journal des modifications | Journal des modifications (11_HISTORIQUE) | 11_HISTORIQUE/Journal_des_modifications.md |

Notes d'utilisation
Point de contrôle humain — le plus critique : à la sortie de T-03, vous devez valider les corrections GÉNÉRALES à intégrer au carnet. C'est vous qui décidez si une correction est générale (elle entre au carnet) ou spécifique (elle reste dans le RDR du projet). Un modèle qui classe une correction spécifique en GÉNÉRALE pollue le carnet.
Cas particulier — plusieurs projets : si T-03 est appelée après plusieurs projets (par exemple, après trois projets avec la même version en vigueur), elle peut proposer une correction globale (v3.x) qui intègre les corrections récurrentes. La règle est : une correction qui apparaît dans plusieurs projets est probablement générale — elle doit entrer au carnet.
Cas particulier — incident isolé : si un incident apparaît dans un seul projet, il peut être :
   * soit spécifique au projet (correction PROJET) ;
   * soit général (correction GÉNÉRALE) — dans ce cas, il doit être testé sur un autre projet avant d'entrer au carnet (classification À ÉTUDIER).
La règle est : un incident isolé est À ÉTUDIER avant d'être intégré au carnet — sauf s'il est manifestement général (par exemple, un défaut de méthode qui se reproduira sur tous les projets).
Cas particulier — correction qui supprime un verrou : si une correction proposée supprime un verrou (par exemple, « supprimer le verrou V7 sur les placeholders »), elle doit être refusée — sauf si elle est remplacée par une clause équivalente. La règle de non-régression est absolue.
Cas particulier — correction qui ajoute une brique : si une correction propose d'ajouter une nouvelle brique (par exemple, « ajouter une brique B-51 pour les ancrages de garde-corps »), elle doit être étudiée :
   * la nouvelle brique est-elle vraiment nécessaire ? (une brique existante peut-elle couvrir le besoin ?)
   * son numéro est-il disponible ? (la numérotation doit être stable)
   * son intégration dans la chaîne est-elle cohérente ?
Une nouvelle brique est une modification majeure — elle doit être justifiée et validée.
Cas particulier — correction qui supprime une brique : si une correction propose de supprimer une brique (par exemple, « supprimer B-41 fondations profondes car jamais utilisée »), elle doit être étudiée :
   * la brique est-elle vraiment inutile ? (peut-elle être nécessaire sur un projet futur ?)
   * son numéro doit-il rester vacant ? (la règle de stabilité de numérotation)
   * l'impact sur les autres briques est-il nul ?
La suppression d'une brique est une modification majeure — elle doit être justifiée et validée.
Cas particulier — correction qui modifie un mode : si une correction propose de modifier un mode (par exemple, « ajouter un mode VALIDÉ PAR TIERS »), elle doit être étudiée :
   * le mode existant ne suffit-il pas ? (les 6 modes sont COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE / INTERNE-GO / SANS OBJET)
   * le nouveau mode est-il vraiment distinct ? (ou peut-il être traité par une décision RDR ?)
   * l'impact sur les briques existantes est-il nul ?
Un nouveau mode est une modification majeure — elle doit être justifiée et validée.
Format de sortie attendu : cinq pièces distinctes (inventaire, analyse, propositions, tri, version). Chaque pièce est explicite — pas de déclaration vague.
Consignation : la proposition T-03 est consignée au journal des révisions (annexe C) comme proposition de nouvelle version. Si la nouvelle version est validée par vous, elle est intégrée au carnet et le journal est mis à jour.
________________

---

### 5. COMPLÉMENT v3.0 — RÈGLES UNIVERSELLES APPLICABLES À CETTE FICHE

**V14 — Indissociabilité du corpus et preuve d'épuisement.** Les pièces du marché forment un corpus unique : cette fiche ne peut jamais déclarer une donnée « absente », une valeur « introuvable » ou un ouvrage « non localisable » avant d'avoir consommé 100 % des pièces reçues (texte, cartouches, notes générales, coupes, nomenclatures et vecteurs PDF/DXF recalés). La preuve d'épuisement est consignée : pièces lues, passages consultés, résultat par pièce. Une déclaration d'absence sans cette preuve est une non-conformité de la fiche.

**V15 — Différentiel temporel et continuité mécanique descendante.** En existant comme en neuf, tout élément produit par cette fiche est rattaché au différentiel superposé `EXISTANT − DÉMOLITION + PROJET`. Tout effort vertical ou horizontal est suivi sans interruption de la toiture jusqu'au sol d'assise : toute discontinuité d'appui entre un niveau `N+1` et le niveau `N` impose un ouvrage de transfert explicitement conçu, calculé et reporté au plan.

**Modes applicables.** Les six modes du document maître (§3) s'appliquent : `COMPLET`, `PARTIEL-DÉCLARÉ`, `HYPOTHÈSE-NOTIFIÉE`, `PARAMÉTRIQUE`, `INTERNE-GO`, `SANS OBJET`. Le mode `HYPOTHÈSE-NOTIFIÉE` autorise la production sous hypothèse conservatrice **à condition** que chaque hypothèse porte un repère `H-xx` (valeur, norme, zone d'application), figure sous nuage graphique sur les plans concernés et soit soumise au délai contractuel de contradiction `DEC-06` (délai par défaut : 2 jours ouvrés ; silence = acceptation). Les inconnues physiques (Classe II) ne sont jamais des hypothèses : elles sont levées en fouille, curage ou dépose et portées par une prescription `ENC` et un Point d'Arrêt `PA-xx` (`DEC-07`).

**Position dans la chaîne v3.0.** Cette fiche s'exécute dans la phase indiquée en en-tête, selon l'ordonnancement du document maître §9 : `Phase 0` cadrage → `Phase 1` socle géométrique et nettoyage (`B-30` → `B-32` → `B-31`) → `Phase 2` audit croisé → `Phase 3` conception et synthèse (`B-20` → `B-25` → `B-21` → `B-22` → `B-23` → `B-24`) → `Phase 4` calculs → `Phase 5` synthèse et livrables (`B-34` → `B-60` → `B-62` → `B-64`) → `Phase 6` vérification croisée et clôture (`B-33` → `B-70` → `B-71` → `B-72`).

**Passage obligatoire du compilateur.** Aucune version du carnet n'est publiée sans exécution du compilateur de cohérence (`T1` à `T10`) et sans résultat `10/10 PASS` (zéro erreur, zéro avertissement). Le journal d'exécution est annexé à la version publiée.