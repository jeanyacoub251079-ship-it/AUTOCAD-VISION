# B-15 — FICHE DE SYNTHÈSE DES RISQUES

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-15** — Synthèse des risques |
| Phase | **1 — Analyse** — *dernière brique de la phase* |
| **Paramètre d'appel** | `{{périmètre_analyse}}` = **« ensemble de la phase Analyse » (B-10, B-11, B-12, B-13, B-14)** |
| **Mode d'appel** | **COMPLET** au sens du paramètre — les cinq briques de la phase 1 sont lues intégralement. **Mais les entrées sont dégradées** : B-10 PARTIEL-DÉCLARÉ (8 p./38), B-12 sans accès au rapport. B-15 ne peut pas être plus solide que ce qu'elle synthétise — voir § 2 |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Fiche du carnet | `03_PHASE_1_ANALYSE/B-15_Synthese_Risques.md` — lue intégralement (l. 3814-3995 de `CARNAC_v2.6_compile.md`) |
| Entrées lues | **B-10** ind. A (§ 2 à § 6) · **B-11** ind. A (§ 2 à § 6) · **B-12** ind. B (§ 1 à § 5) · **B-13** ind. A (tableaux A et B) · **B-14** ind. A (§ 2 à § 6) · **B-03** ind. I (réserves, verrous, décisions) · **B-01** ind. B |
| Sortie | Registre de **23 risques** cotés + **4 risques résiduels** proposés + synthèse 10 lignes |
| Indice du livrable | **A** |
| Date | 19/10/2026 |
| Brique suivante | **B-20 (Conception GO)** — ou B-30 à B-33 selon le PTD |

---

## 0. ACCUSÉ DE RÉCEPTION

| Entrée | Lue | Ce que j'en ai tiré |
|---|---|---|
| **B-10** — Audit CCTP | intégralement | 15 constats, 12 lacunes, 10 contradictions, 12 points à lever |
| **B-11** — Audit diagnostic | intégralement | 9 désordres, 9 données manquantes, 5 zones non relevées |
| **B-12** — Audit géotechnique | intégralement | G2 AVP insuffisant, 8 données manquantes, G3 recommandée, R-38 |
| **B-13** — Contradictions | intégralement | 24 contradictions qualifiées, 14 bloquantes |
| **B-14** — Périmètre de lot | intégralement | 14 INCLUSES, 4 EXCLUES, 9 À TRANCHER dont 8 silences |
| **B-03** — RDR ind. I | réserves R-01 à R-38, verrous V-01 à V-26 | Base de non-redondance : un risque déjà couvert est signalé, pas recréé |

**Ce que je n'ai pas** : le rapport **GEOFLORAV2** (D-18), les **30 pages non lues** du CCTP, le **DPGF**, le **CCTP des autres lots**, les **sondages** de planchers, les **sections** de charpente.

---

## 1. MÉTHODE — RISQUE N'EST PAS CONTRADICTION

Une contradiction est un **état du dossier** ; un risque est un **événement redouté**. Une contradiction peut produire trois risques distincts, et une lacune peut en produire un sans qu'aucune contradiction existe. C'est la raison d'être de cette brique, et j'ai refusé de la traiter comme un sous-produit de B-13.

**Trois règles que je me suis imposées :**

1. **Aucun risque sans source citée** — brique + référence de ligne ou de constat.
2. **Aucune fusion pour faire court.** Vingt-trois lignes plutôt qu'un tableau de dix qui perdrait les responsables et les échéances.
3. **Aucune solution technique en mesure de maîtrise.** La maîtrise d'un « G3 non commandée » est *demander la commande du G3*, pas *choisir 0,25 MPa au lieu de 0,30*.

**Numérotation.** Les risques sont numérotés **RI-01 à RI-23**, volontairement distincts des **R-xx** du RDR pour qu'aucune confusion ne soit possible entre un risque et une réserve.

---

## 2. CE QUE LA DÉGRADATION DES ENTRÉES FAIT À CETTE FICHE

Je dois le dire avant le tableau, parce que cela change la lecture de chaque cote.

**B-10 est PARTIEL-DÉCLARÉ sur 8 pages sur 38.** Un risque que je ne vois pas parce qu'il est écrit page 20 n'est pas un risque absent : c'est un **risque hors de mon champ de vision**. Le registre est donc **complet au sens de la méthode, incomplet au sens de la couverture documentaire**.

**B-12 n'a pas lu le rapport.** Les contraintes admissibles sont des citations déclarées. Toute la branche fondations du registre repose sur une donnée que personne, dans cette chaîne, n'a vérifiée.

**Conséquence de méthode, et elle est importante** : les risques **RI-22** (CCTP non relu) et **RI-01** (contraintes non vérifiées) ne sont pas des risques parmi d'autres. Ce sont les **deux risques qui rendent tous les autres incertains**. Je les ai cotés au maximum, mais leur vraie particularité est qu'ils **conditionnent la validité du registre lui-même**.

---

## 3. REGISTRE DES RISQUES — 23 LIGNES

> **Échelles.** P1 improbable (< 20 %) · P2 possible (20-60 %) · P3 probable (> 60 %). I1 faible (< 1 sem. ou impact mineur) · I2 moyen (1-4 sem. ou impact limité à un livrable) · I3 fort (> 4 sem., ou sécurité, conformité, responsabilité). Criticité : 1-2 faible · 3-4 moyenne · **6-9 élevée**.

| N° | Risque *(au conditionnel)* | Source | Nat. | P | Justification P | I | Justification I | P×I | Brique | Mesure de maîtrise | Resp. | Échéance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **RI-01** | Si les contraintes admissibles ne sont pas vérifiées sur pièce, les fondations seraient dimensionnées sur une valeur non opposable | B-12 § 1-2 (SOL-01, SOL-02) + D-18 | Techn. | **3** | Un G2 AVP ne couvre pas des calculs d'exécution (NF P 94-500), et nous n'avons pas lu le rapport : l'insuffisance est **structurelle**, pas accidentelle | **3** | En cas de sinistre de fondation, nous ne pourrions produire aucune pièce ayant fixé q<sub>adm</sub> | **9** | B-40 | Demande écrite des extraits (coupe, XA, classe de sol) **et** commande d'une G3 — décision MOA à provoquer | **MOA / MOE** | Avant B-40 |
| **RI-02** | Si l'assise à −1,00 m n'atteint pas les alluvions, la portance retenue serait sans fondement | B-12 SOL-04 · B-02 D-08 (toit **déduit** à −0,50 m) | Techn. | **2** | Le toit des alluvions est déduit, non lu ; en fond de vallée de la Seine la couche utile peut être plus profonde | **3** | Une semelle posée sur remblai au lieu d'alluvions est un désordre de fondation, pas un écart de calcul | **6** | B-40 | Extrait de la **coupe type** du rapport ; à défaut, sondage de contrôle avant coulage | **MOE / GEOEXPERTS** | Avant B-40 |
| **RI-03** | Si le classement XA réel est XA3, l'enrobage de 50 mm serait à revoir sur les ouvrages en fondation | B-12 SOL-05 · B-13 C-15 · B-03 V-05 | Techn. | **2** | « XA4 » n'existe pas ; la vraie classe est inconnue, les deux hypothèses (XA2/XA3) restent ouvertes | **3** | Touche la durabilité et la conformité NF EN 206, donc la réception de l'ouvrage | **6** | B-40, B-42, B-43 | Obtenir le classement réel ; à défaut, conserver l'hypothèse majorante et la déclarer en note | **GEOEXPERTS / BET** | Avant B-40 |
| **RI-04** | Si le plancher haut n'est pas sondé, le renfort de charpente reposerait sur un porteur dont la constitution est inconnue | B-11 désordre 5 + EXI-04 (§ 4) | Techn. | **3** | Aucun sondage, aucune ouverture, aucune fiche : la donnée **n'existe pas** | **3** | Ce plancher porte la charpente par potelets : toute reprise de toiture transite par lui | **9** | B-43, B-44 | Commander les **fiches de sondage** (R-19) avant tout calcul de charpente | **BET (EVEN) / MOE** | Avant B-24 |
| **RI-05** | Si la ferme altérée est renforcée sans purge, la charge serait transférée sur du bois mort | B-11 désordre 6 + MAT-06 · B-03 R-21 | Techn. | **3** | L'altération est **constatée** par le diagnostic ; l'absence de purge est l'état actuel du dossier | **3** | Rupture d'un élément porteur de toiture au-dessus d'un bâtiment occupé | **9** | B-44 | Prescrire la purge avant renfort et obtenir le classement des bois (R-21) | **BET bois / MOE** | Avant B-44 |
| **RI-06** | Si les potelets sont effectivement instables, les renforts aggraveraient leur flambement | B-11 désordre 8 | Techn. | **2** | Le diagnostic écrit « théoriquement instables » : c'est une hypothèse non vérifiée, pas un constat | **3** | Ajouter de la charge sur un potelet instable est un risque de ruine locale | **6** | B-44 | Vérifier le flambement **avant** d'augmenter la charge ; relever les sections (R-20) | **BET** | Avant B-44 |
| **RI-07** | Si la flèche de la poutre maîtresse est déjà consommée, le renfort arrêterait l'évolution sans la reprendre | B-11 désordre 3 (L/h ≈ 29) | Techn. | **3** | Le désordre est structurel, constaté à vue, et le sous-dimensionnement d'origine est établi | **2** | N'affecte pas la sécurité immédiate mais fixe le phasage et le niveau de reprise d'un livrable | **6** | B-45 | Porter la flèche résiduelle et le phasage d'étaiement dans la note de calcul | **BET** | Avant B-45 |
| **RI-08** | Si les deux zones « non relevées » restent sans relevé, une partie de la charpente serait calculée sur hypothèse | B-11 § 5 · B-03 R-20 | Techn. | **3** | Le BET a lui-même déclaré le relevé partiel, sur le plan | **2** | Le calcul resterait faisable mais partiellement non justifiable | **6** | B-44 | Relevé complémentaire des deux zones avant B-44 | **BET / géomètre** | Avant B-44 |
| **RI-09** | Si le calage D2 ↔ D5 n'est pas établi, les plans d'exécution seraient cotés sur une géométrie non vérifiée | B-03 V-18 · D5 (aucune altimétrie) · B-13 C-12, C-14, C-24 | Techn. | **3** | Deux échelles annoncées, quatre orientations, aucune altimétrie : le calage n'est pas seulement à faire, il est à **fonder** | **2** | Impact limité au livrable B-60, mais systématique sur toutes ses planches | **6** | B-30, B-60 | Exécuter B-30 à B-33 puis faire viser le calage ; lever C-12 et C-14 | **GO / MOE** | Avant B-60 |
| **RI-10** | Si la reprise en sous-œuvre n'est pas prescrite, nous exécuterions un phasage que nous aurions inventé | B-14 AT-01 · B-13 C-11 | Contract. | **3** | Le seul phasage dessiné figure sur le folio de la **passerelle**, un autre bâtiment | **3** | Le mode opératoire devient notre responsabilité, sans prescription pour nous couvrir | **9** | B-40, B-60 | Demande écrite de prescription + position de prix sur le phasage | **MOE / BET** | Avant B-40 |
| **RI-11** | Si la charpente bois n'est pas contractualisée, nous l'étudierions sans être payés ni couverts | B-14 AT-02 · B-13 C-07 · B-03 R-22 | Contract. | **3** | Aucune section bois au CCTP, alors que le plan folio 02 prescrit des travaux de charpente | **3** | Prestation non prescrite exécutée = charge financière et responsabilité sans contrat | **9** | B-44, B-50 | Confirmation écrite de périmètre + valorisation avant consultation | **MOE / économiste** | **Avant consultation** |
| **RI-12** | Si le déplombage, le curage et la démolition restent dans notre lot sans être étudiés, l'écart se solderait en fin de chantier | B-14 § 5 · H-01 à H-03 | Contract. | **3** | Le lot 01 les inclut **nommément**, notre énoncé de mission les exclut : le désaccord est déjà écrit | **3** | Un lot de démolition non chiffré dans un bâtiment occupé se paie deux fois | **9** | B-14, B-60 | Arbitrage de direction + position de prix écrite avant remise | **MOA / direction** | **Avant remise** |
| **RI-13** | Si le CCTP n'est pas mis à jour, nous produirions des semelles que le marché ne décrit pas | B-13 C-22 · D-10 / D-14 | Contract. | **3** | Le CCTP dit *filante*, la décision dit *isolée 60×60* : l'écart est acté, pas résolu | **3** | Autre ouvrage, autre métré, autre prix : l'écart se discutera après exécution | **9** | B-40, B-60, B-62 | Mise à jour du CCTP ou note d'écart validée par la MOE | **MOE / MOA** | **Avant remise** |
| **RI-14** | Si le bâtiment Gardien entre dans le marché, notre périmètre d'études serait incomplet d'un bâtiment | B-14 AT-03 · B-13 C-06 | Contract. | **2** | Le titre l'annonce, le sommaire l'ignore, le plan d'installation le montre : trois pièces, trois réponses | **3** | Un bâtiment entier non étudié dans un marché signé | **6** | B-14, B-62 | Confirmation écrite du périmètre par la MOA | **MOA / MOE** | **Avant remise** |
| **RI-15** | Si les linteaux des frangements F1-F4 ne sont pas nommés, nous dimensionnerions des ouvrages non prescrits | B-14 AT-06 · B-13 C-09 | Contract. | **3** | Le CCTP ne comporte aucun article linteau ; les frangements ne sont pas cotés | **3** | Reprise de charge sur murs porteurs : sécurité et conformité | **9** | B-49, B-45 | Prescription écrite + relevé coté des frangements | **MOE / BET** | Avant B-49 |
| **RI-16** | Si l'étaiement provisoire reste implicite, il serait exécuté sans être chiffré | B-14 AT-09 | Contract. | **3** | Aucun article du CCTP ne le vise ; il est pourtant indissociable de la pose des renforts | **2** | Prestation réelle, montant limité, mais **invisible** une fois réalisée | **6** | B-40, B-44 | Inscrire l'étaiement au périmètre et le chiffrer | **MOE** | Avant démarrage |
| **RI-17** | Si la liste des réservations techniques n'est pas fournie, nos voiles et dallages seraient coulés sans attentes | B-14 AT-07 | Contract. | **2** | Le CCTP renvoie au § 01.2.1.8, non lu ; aucune liste n'existe | **2** | Carottages et reprises à nos frais, sans impact structurel majeur | **4** | B-60 | Obtenir la liste des réservations par lot technique | **MOE / BET technique** | Avant B-60 |
| **RI-18** | Si les désordres d'humidité ne sont pas traités, nos renforts seraient posés sur une structure active | B-11 désordres 4, 7, 9 · B-14 AT-08 | Interface | **3** | Trois désordres d'humidité constatés, aucune pièce du lot structure ne les traite | **2** | Dégradation accélérée des bois et des aciers, sans ruine immédiate | **6** | B-23, B-44 | Désigner le lot qui traite la cause **avant** nos renforts | **MOE** | Avant démarrage |
| **RI-19** | Si les prescriptions propres du diagnostic ne sont pas restituées, nous ignorerions ce qui a été prescrit hors DCE | B-11 § 3 (écart V4) | Interface | **2** | Aucune des cinq prescriptions n'est restituée : ni confirmée, ni infirmée | **2** | Impact limité à la validation de nos choix en B-44/B-45 | **4** | B-44, B-45 | Demander à la MOE la restitution des prescriptions du diagnostic | **MOE** | Avant B-45 |
| **RI-20** | Si le degré coupe-feu n'est pas fixé, l'encoffrement prescrit resterait non dimensionné | B-13 C-17 · B-03 V-11 / R-12 · B-12 SEC | Réglem. | **3** | La section SECURITE INCENDIE du cartouche est **intégralement vide** alors que l'encoffrement est prescrit | **3** | Exigence réglementaire ERP non satisfaite à la réception | **9** | B-42, B-43, B-49 | Obtenir le degré CF/SF ; à défaut, mention obligatoire « protection au feu adéquate à prévoir » | **MOE / BE incendie** | Avant B-42 |
| **RI-21** | Si a<sub>gr</sub> et la classe de sol restent vides, l'action sismique ne serait pas calculable | B-13 C-18 · B-03 V-10 / R-11 | Réglem. | **2** | Zone 1 et catégorie II sont renseignées ; seules les deux valeurs dérivées manquent | **3** | Non-conformité Eurocode 8 sur un bâtiment recevant du public | **6** | B-42, B-46 | Extraire la classe de sol du rapport ; faire calculer a<sub>gr</sub> | **BET** | Avant B-42 |
| **RI-22** | Si le CCTP n'est pas relu intégralement, une prescription écrite dans les 30 pages non lues nous échapperait | B-10 § 5, point à lever n° 1 | Planning | **3** | 30 pages sur 38 n'ont pas été lues : ce n'est pas un aléa, c'est un **état** | **3** | Une prescription ignorée engage notre responsabilité sans que nous l'ayons vue | **9** | **Toutes** | Relecture intégrale du CCTP avant toute remise exécutable | **GO interne / MOE** | **Avant remise** |
| **RI-23** | Si les deux références du rapport désignent deux documents, deux jeux d'hypothèses de sol coexisteraient | B-12 § 4bis · B-03 R-38 | Techn. | **2** | `GEOFLORAV2` et `25.13646/ES/GIF` ont des formes différentes ; le lien n'est pas établi | **2** | Impact limité à la traçabilité, mais il contamine toute la branche fondations | **4** | B-12, B-40 | Confirmation écrite de la correspondance entre les deux références | **MOE / GEOEXPERTS** | Avant B-40 |

---

## 4. LECTURE DU REGISTRE — CE QUE LA COTATION DIT MALGRÉ ELLE

**Dix risques atteignent la criticité maximale (9).** Un registre où 43 % des lignes saturent l'échelle ne hiérarchise plus rien — et c'est précisément l'information à retenir : **ce dossier n'a pas un problème prioritaire, il a dix problèmes simultanés de même gravité.**

**Mais leur nature les sépare en deux familles, et c'est là que la décision se joue :**

| Famille | Risques | Ce qu'ils demandent |
|---|---|---|
| **Ce qui manque** | RI-01, 02, 04, 05, 20, 22 | Des **pièces** : extraits, sondages, degré coupe-feu, relecture |
| **Ce qui n'est pas écrit** | RI-10, 11, 12, 13, 15 | Des **mots** : une prescription, une confirmation de périmètre, une mise à jour de marché |

**Les six « pièces » se lèvent par une demande à la MOE** — c'est du temps, pas de l'arbitrage. **Les cinq « mots » se lèvent par une décision de votre part** — et ils ne se lèveront pas si personne ne les pose. Un extrait de rapport arrive en trois jours ; une prescription de charpente peut ne jamais venir.

**Deux risques ne sont pas à leur place dans un registre de risques.** RI-22 et RI-01 ne décrivent pas un aléa : ils décrivent l'**état de notre propre connaissance**. Les coter à 9 est exact, mais les traiter comme les autres serait une erreur — ils doivent être levés **avant** que les autres cotations aient un sens.

---

## 5. RISQUES RÉSIDUELS — **PROPOSÉS, NON ACCEPTÉS**

> La fiche B-15 est explicite : *« un risque que vous acceptez de porter est un risque que vous ne pourrez plus reprocher à la MOE »*. **Je ne peux pas accepter à votre place.** Ce tableau est une **proposition d'acceptation**, à valider ou refuser ligne par ligne.

| N° | Risque | Justification de l'acceptation proposée | Suivi |
|---|---|---|---|
| **RR-01** | **Tassements non vérifiés** | **D-15** les sort du périmètre : la vérification est à la charge du géotechnicien. L'acceptation est **déjà actée par décision tracée** — elle n'est pas nouvelle | **MOA** (via GEOEXPERTS) |
| **RR-02** | **Venue d'eau en fouille malgré D-16** (nappe déclarée absente) | Risque résiduel **borné par une règle** : toute venue d'eau est un **point d'arrêt** (B-02 ENC al. 8). On n'accepte pas l'aléa, on accepte de s'arrêter s'il se produit | **GO** |
| **RR-03** | **Aucune donnée structurelle dans D5** | **D-17** : le DXF de coffrage est à produire par nous. L'absence de contenu structurel n'est plus un risque subi, c'est une **charge de production acceptée** (R-37 fermée) | **GO** |
| **RR-04** | **Enrobage de 50 mm sans justification du Δc<sub>dev</sub>** | 50 mm est **majorant** pour XC2 / S4 (EC2 4.4N) : l'écart est conservateur. Le risque résiduel est un **sur-enrobage**, pas un sous-enrobage | **BET** |

**Un risque que je refuse de proposer à l'acceptation.** **RI-22** (CCTP non relu) ne figure pas dans ce tableau et ne doit pas y figurer : accepter de travailler sans avoir lu le marché n'est pas un risque résiduel, c'est une **faute**. Si vous le refusez, il reste une mesure à exécuter.

---

## 6. SYNTHÈSE — DIX LIGNES

- **23 risques** : **10 de criticité 9**, 10 de criticité 6, 3 de criticité 4. Le registre sature en haut — 43 % des lignes à l'échelle maximale — et c'est en soi le constat.
- **Les trois plus lourds** : **RI-22** (30 pages du CCTP non lues — il invalide la portée de tous les autres), **RI-01** (fondations sur contrainte non vérifiée), **RI-12** (déplombage et curage dans notre lot, hors de nos études).
- **Les deux risques qui conditionnent la validité du registre** : RI-22 et RI-01 ne sont pas des aléas mais l'état de notre connaissance — à lever **avant** toute cotation définitive.
- **Cinq risques impactent directement la remise** : RI-12, RI-13, RI-14, RI-22 et RI-11 — tous contractuels, tous dépendant d'une décision qui n'est pas la nôtre.
- **Cinq risques engagent notre responsabilité contractuelle** : RI-10, RI-11, RI-12, RI-13, RI-15 — et **quatre d'entre eux sont des « silences »** : rien n'a été écrit, donc rien ne nous protège.
- **Quatre risques sont purement techniques et se lèvent par une pièce** : RI-02, RI-03, RI-20, RI-21 — un extrait de rapport ou un degré coupe-feu suffit.
- **Le plus sous-estimé** : **RI-16** (étaiement, criticité 6) — montant faible, mais invisible dès la première pose de renfort.
- **Quatre risques résiduels proposés à l'acceptation**, dont trois déjà couverts par une décision (D-15, D-16, D-17) et un majorant de calcul (RR-04).
- **Aucun risque de criticité élevée n'est sans mesure de maîtrise** — l'anomalie signalée par la fiche B-15 ne se présente pas ici.
- **Conclusion** : la phase 1 se clôt sur **dix risques bloquants dont cinq exigent une décision de votre part avant toute production**. La phase 2 peut commencer sur les briques documentaires ; **B-40 ne le peut pas**.

---

## 7. CONSIGNATION AU RDR — CE QUI EST DÉJÀ COUVERT, ET CE QUI NE L'EST PAS

La fiche prescrit que chaque risque de criticité élevée devienne une réserve. **Je n'en crée pas vingt-trois** : la règle de non-redondance avec B-03 l'interdit, et un registre de 62 réserves ne se lit plus.

| Risque | Réserve ou verrou existant | Statut |
|---|---|---|
| RI-01 | **R-13** (coupe type) · V-01 · **R-61 proposée** *(commande G3 / extraits certifiés)* | Partiellement couvert |
| RI-02 | **R-13** | Couvert |
| RI-03 | **R-14** · V-05 | Couvert |
| RI-04 | **R-19** · V-17 | Couvert |
| RI-05 | **R-21** | Couvert |
| RI-06, RI-08 | **R-20** · V-16 | Couvert |
| RI-07 | *Aucune* — point de conception, traité en B-45 | **Pas de réserve** *(n'est pas une donnée manquante)* |
| RI-09 | **V-18** · R-44 et R-46 proposées (C-12, C-14) | Couvert |
| RI-10 | **R-51 proposée** (AT-01) | Proposé |
| RI-11 | **R-22** (existante) + **R-52 proposée** | Couvert |
| RI-12 | **R-60 proposée** | Proposé |
| RI-13 | **R-48 proposée** (C-22) | Proposé |
| RI-14 | **R-42 / R-53 proposées** | Proposé |
| RI-15 | **R-43 / R-56 proposées** | Proposé |
| RI-16 | **R-59 proposée** | Proposé |
| RI-17 | **R-57 proposée** | Proposé |
| RI-18 | **R-58 proposée** | Proposé |
| RI-19 | **R-62 proposée** *(prescriptions du diagnostic non restituées)* | **Non couvert** |
| RI-20 | **R-12** · V-11 | Couvert |
| RI-21 | **R-11** · V-10 | Couvert |
| RI-22 | **R-63 proposée** *(relecture intégrale du CCTP)* | **Non couvert — et c'est une lacune du RDR** |
| RI-23 | **R-38** (ouverte à l'indice I) | Couvert |

**Trois créations seulement** : **R-61**, **R-62**, **R-63**. Les vingt autres risques sont adossés à une réserve ou à un verrou existant.

**Le RDR reste à l'indice I.** Ni R-39 à R-50 (B-13), ni R-51 à R-60 (B-14), ni R-61 à R-63 (B-15) ne sont inscrites. **En attente de votre validation, trente-six propositions** — et un registre qui ne peut pas se clore sur trente-six propositions non arbitrées est un registre qui ne protège personne.

---

## 8. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-15) | État | Observation |
|---|---|---|
| Chaque risque rattaché à une source citée | ✅ | **23/23** — brique + référence (constat, désordre, code variable, article) |
| Chaque cotation P et I justifiée | ✅ | **46 justifications**, une phrase chacune, jamais une note seule |
| Chaque risque a un responsable et une échéance | ✅ | 23/23 ; échéances prises dans les quatre valeurs admises |
| Mesure de maîtrise = action de pilotage, pas solution technique | ✅ | Vérifié ligne à ligne. Aucune mesure ne prescrit de valeur, de section ni de matériau |
| Risques résiduels identifiés et justifiés | ✅ *(proposés)* | 4 lignes, **explicitement proposées**, non acceptées. RR-01 à RR-03 s'appuient sur D-15, D-16, D-17 |
| Synthèse en 10 lignes | ✅ | **10 lignes** |
| Périmètre « B-13 seule » : aucun risque hors B-13 | — | **Sans objet** — paramètre = ensemble de la phase 1 |
| Aucun risque de criticité élevée sans mesure | ✅ | 10 risques à 9, **10 mesures de maîtrise** |

**Placeholders résiduels (V7)** : aucun. `ID-01`, `ID-02` et `périmètre_analyse` renseignés en en-tête.

---

## 9. POINT DE CONTRÔLE HUMAIN — LE DERNIER DE LA PHASE 1

La fiche le dit : ce point est **le plus critique** de la brique. Quatre questions :

1. **Les quatre risques résiduels** (RR-01 à RR-04) : acceptés, refusés, ou à renégocier ? *Votre réponse engage — c'est écrit dans la fiche, et c'est exact.*
2. **R-61, R-62, R-63** : je les inscris ? Et que fait-on des **33 propositions antérieures** (R-39 à R-60) ? Un RDR à l'indice I avec 36 propositions en attente n'est plus un registre, c'est un brouillon.
3. **RI-01 et RI-22** : acceptez-vous de **conditionner la phase 2** à la commande d'une G3 et à la relecture intégrale du CCTP ? Si non, la suite se produira sur un socle que nous savons incomplet — et ce sera écrit.
4. **L'ordre de la phase 2** : le PTD prévoit **B-30 à B-33** (calage, désormais exécutables) avant B-22 et B-20. Confirmez-vous, ou passez-vous directement à B-20 ?

---

*Brique B-15, **indice A**. **Phase 1 — Analyse : close.***

*Aucune réserve inscrite : 3 créations proposées, 4 risques résiduels proposés à l'acceptation. RDR à l'indice I.*

*Aucune brique aval engagée : **B-30 (ou B-20)** attend un GO.*
