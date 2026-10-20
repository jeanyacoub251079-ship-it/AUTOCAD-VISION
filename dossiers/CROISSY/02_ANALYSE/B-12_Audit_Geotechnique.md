# B-12 — AUDIT DES PIÈCES GÉOTECHNIQUES

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-12** — Audit des pièces géotechniques |
| Phase | 1 — Analyse |
| **Mode d'appel** | **PARTIEL-DÉCLARÉ** — le rapport **existe** (réf. **GEOFLORAV2**) mais **dépasse la capacité de transfert** de l'espace de travail ; les hypothèses de sol en sont des **extractions déclarées** |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Pièce auditée | **DOC-06** — rapport **GEOEXPERTS n° 25.13646/ES/GIF du 22/01/2026**, mission **G2 AVP** |
| Entrées lues | B-00 ind. C · B-01 ind. B · B-02 ind. F · B-03 ind. I · **D2 p. 1** (cartouche) · déclarations client D-01, D-02, D-03, D-15, D-16, **D-18** |
| Sortie | 3 tableaux + synthèse 8 lignes |
| Indice du livrable | **B** (remplace l'indice A du 19/10/2026) |
| Date | 19/10/2026 |
| Brique suivante | **B-13 (Contradictions)** |

---

## 0. CE QUE J'AI LU, ET CE QUE JE N'AI PAS LU

> **Mise à jour indice B — D-18.** Le rapport géotechnique **existe** : il porte la référence **GEOFLORAV2**. Il **n'a pas pu être transféré** dans l'espace de travail — document trop lourd. Les hypothèses de sol qui m'ont été fournies **proviennent de ce document**.

**Ce que cela change, et c'est important.** À l'indice A, q<sub>ELS</sub> et q<sub>ELU</sub> étaient des **déclarations sans source documentaire**. Elles sont désormais des **citations déclarées d'un document identifié**. La chaîne de traçabilité a un nom au lieu d'un vide : c'est un progrès réel, à enregistrer comme tel.

**Ce que cela ne change pas.** Je n'ai pas lu GEOFLORAV2. Je ne peux donc ni citer page ni paragraphe, ni vérifier la méthode, le nombre de sondages ou l'emprise couverte, ni extraire la coupe, le classement XA ou la classe de sol.

**La valeur n'est plus sans source ; elle est sans vérification.** Deux niveaux de faiblesse différents, et le second est moins grave que le premier.

Ce que je possède :

| Source | Contenu | Nature |
|---|---|---|
| **D2 p. 1** (cartouche EVEN, ind. C) | Référence du rapport, mission, date, deux valeurs, une profondeur d'ancrage, une couche de forme | **Lecture** d'une pièce contractuelle |
| **D-01** | Mission G2 AVP retenue comme référentiel | **Décision client** |
| **D-02 / D-03** | q<sub>ELS</sub> < 0,30 MPa · q<sub>ELU</sub> < 0,49 MPa | **Décision client** |
| **D-16** | Absence de nappe phréatique | **Déclaration client** |
| **D-15** | Tassements hors mission, à la charge du géotechnicien | **Décision client** |

**Aucune ligne de cet audit ne provient de la lecture du rapport lui-même.** C'est la distinction centrale de B-12 : je ne peux pas auditer un document que je n'ai pas. Ce que j'audite, c'est **ce que le dossier en dit** — et c'est suffisant pour établir que le niveau de mission ne couvre pas nos besoins.

---

## 1. TABLEAU 1 — DONNÉES DISPONIBLES ET ADÉQUATION

| Code | Libellé | Valeur **citée** *(jamais retenue)* | Unité | Référence | Adéquation |
|---|---|---|---|---|---|
| **SOL-08** | Niveau de mission | **G2 AVP** | — | D2 p. 1 ; D-01 | ⚠ **Insuffisante** — voir § 2 |
| **SOL-08b** | Référence et date du rapport | **25.13646/ES/GIF** du **22/01/2026** | — | D2 p. 1 | **Exploitable** — la pièce est identifiée |
| **SOL-01** | Contrainte admissible ELS | **« 0,3 MPa »** — soit **3 bars** | MPa | D2 p. 1 + **D-02** + **GEOFLORAV2** *(D-18)* | ⚠ **Ambiguë** — valeur unique, sans fourchette ni méthode. **Source documentaire identifiée**, contenu non vérifiable |
| **SOL-02** | Contrainte admissible ELU | **0,49 MPa** | MPa | **D-03** + **GEOFLORAV2** *(D-18)* | ⚠ **Ambiguë** — ne figure pas au cartouche D2 ; **extraite de GEOFLORAV2**, non vérifiable |
| **SOL-03** | Profondeur d'ancrage | **« RSO ancrées d'au moins 0,5 m dans les Alluvions anciennes »** | m | D2 p. 1 — *superseded par D-08 / D-09* | **Exploitable** — c'est la valeur la plus défavorable, et elle est écrite |
| **SOL-04** | Nature du sol d'assise | **« Alluvions anciennes »** — appellation seule | — | D2 p. 1 | ⚠ **Insuffisante** — l'appellation n'est pas une coupe |
| **SOL-05 / MAT-02** | Agressivité | **« XA4 »** | classe | D2 p. 1 | ❌ **Ambiguë** — la classe **XA4 n'existe pas** dans la NF EN 206/CN (XA1 à XA3) |
| **SOL-06** | Nappe | **Absence de nappe phréatique** | — | **D-16** *(déclaration)* | ⚠ **Déclarée** — non lue au rapport ; le régime retenu est le point d'arrêt en cas de venue d'eau |
| **SOL-07** | Tassements | **Hors mission** — à la charge du géotechnicien | — | **D-15** *(décision)* | ⚠ **Hors périmètre** — sortie du champ par décision, non par absence |
| **GEO-13** | Couche de forme sous dallage | **40 cm** | cm | D2 p. 1 | **Exploitable** — valeur dimensionnante pour B-43 |
| **GEO-14** | Module pressiométrique / pénétrométrique | — | — | — | ❌ **Absent** du cartouche |

**Ce que ce tableau montre.** Sur onze entrées, **deux seulement sont pleinement exploitables** : la référence du rapport et la profondeur d'ancrage. Cinq sont déclarées plutôt que lues, une est non normative, deux sont insuffisantes, une est absente.

---

## 2. LE POINT CENTRAL — UN G2 AVP NE COUVRE PAS DES CALCULS D'EXÉCUTION

**La chaîne des missions géotechniques est normée** (NF P 94-500, annexe A). Le niveau **G2 AVP** est une mission d'**avant-projet** : elle fournit des hypothèses pour un dimensionnement préliminaire, pas des valeurs pour une note de calcul d'exécution.

| Mission | Phase | Usage prévu | Suffit pour une note EXE ? |
|---|---|---|---|
| G1 | Étude préliminaire | Faisabilité, premières hypothèses | ❌ Non |
| **G2 AVP** | **Avant-projet** | **Hypothèses de dimensionnement préliminaire** | ❌ **Non** |
| G2 PRO | Projet | Dimensionnement des ouvrages géotechniques | ⚠ Partiellement |
| **G3** | **Étude géotechnique de conception** | **Dimensionnement définitif, valeurs de calcul** | ✅ **Oui** |
| G4 | Supervision d'exécution | Contrôle en cours de travaux | Complémentaire |
| G5 | Diagnostic géotechnique | Existant, avis sur un ouvrage | Cas particulier de réhabilitation |

**Le carnet le dit dans sa propre fiche B-12** : *« C'est le cas Flora : un G2 AVP ne suffit pas à des calculs EXE ; une G3 est nécessaire. »* Cette affaire est le cas d'école que le carnet a documenté.

**Et pourtant, des valeurs de calcul circulent déjà.** q<sub>ELS</sub> = 0,30 MPa et q<sub>ELU</sub> = 0,49 MPa viennent de **déclarations**, pas du rapport. Elles sont en FDC en fiabilité « Décision » — c'est-à-dire opposables parce que décidées, pas parce que vérifiées. **La FDC l'avait déjà signalé en PARTIEL-DÉCLARÉ.** B-12 confirme : le fondement documentaire de ces deux valeurs n'est pas dans nos mains.

**La conséquence n'est pas que les valeurs sont fausses** — elles sont probablement justes, 0,3 MPa figure bel et bien au cartouche. La conséquence est que **si elles sont contestées, nous ne pouvons pas produire la pièce qui les justifie.**

---

## 3. TABLEAU 2 — DONNÉES MANQUANTES ET IMPACT

| Code | Libellé | Impact sur nos calculs | Brique suspendue | Voie d'obtention |
|---|---|---|---|---|
| **SOL-04** | **Coupe géologique type** — succession des couches, toit des alluvions, épaisseur | Sans coupe, l'assise à −1,00 m repose sur une **déduction** (toit des alluvions à −0,50 m, déduit de D-08) et non sur une lecture | **B-40** | **Extrait du rapport** — 1 planche (R-13) |
| **SOL-05 / MAT-02** | **Classement d'agressivité réel** (XA1 / XA2 / XA3) | Détermine l'enrobage, donc la durabilité. « XA4 » n'existe pas ; la NF EN 206 impose XA3 au maximum | **B-40, B-42, B-43** | **Extrait du rapport** + décision (R-14) |
| **GEO-15** | **Nombre, implantation et profondeur des sondages** | Condition de validité : une campagne sur 3 sondages ne couvre pas la même emprise qu'une campagne sur 10. **Nous ne savons pas ce que la mission a couvert** | **B-40** | **Extrait du rapport** |
| **GEO-16** | **Module de déformation** (E, E<sub>M</sub>) | Nécessaire à tout calcul de tassement — **sorti du périmètre par D-15**, mais c'est aussi la donnée qui permettrait de contester un tassement si le géotechnicien ne l'a pas fait | — *(hors mission)* | **Extrait du rapport** si vérification ultérieure |
| **GEO-17** | **Sensibilité du bâti existant** au tassement différentiel | L'existant est ancien, en moellons, et déjà fissuré (désordres 1, 2, 5 de D3) | **B-40** *(résiduel)* | **Extrait du rapport** |
| **GEO-13b** | **Portance de la couche de forme** sous dallage (EV2) | B-43 ne peut pas vérifier la plate-forme | **B-43** | **Essai à la plaque** en phase travaux |
| **GEO-11b** | **Classe de sol sismique** | `a`<sub>gr</sub> et classe de sol **vides** au cartouche D2 ; la classe de sol se déduit normalement de la coupe | **B-42, B-46** | **Extrait du rapport** (R-11) |
| **SOL-03b** | **Signification de « RSO »** | Le sigle apparaît deux fois dans le cartouche, avec deux sens possibles | **B-40** | **Question à la MOE** (C-20) |

---

## 4. TABLEAU 3 — RECOMMANDATION DE MISSION

| Mission proposée | Base normative | Justification | Conséquence si non commandée |
|---|---|---|---|
| **G3 — Étude géotechnique de conception** *(prioritaire)* | **NF P 94-500, annexe A** — mission G3 | Le G2 AVP est une mission d'avant-projet. Nos calculs sont des calculs d'**exécution** : ils exigent des valeurs de dimensionnement définitives, avec méthode et hypothèses explicites. La fiche B-12 du carnet désigne explicitement ce cas | **B-40 reste en PARTIEL-DÉCLARÉ** : les valeurs q<sub>ELS</sub> et q<sub>ELU</sub> restent des **déclarations non opposables**, et la note portera un filigrane. En cas de sinistre de fondation, nous ne pourrons pas produire la pièce qui a fixé la contrainte admissible |
| **G2 PRO** *(alternative minimale)* | **NF P 94-500, annexe A** — mission G2 PRO | Suffirait si la MOA refuse une G3 : donne des valeurs de projet, mais sans le niveau de définition d'une G3 | **B-40 en PARTIEL-DÉCLARÉ**, dégradation moindre mais réelle : le dimensionnement définitif n'est pas couvert |
| **G5 — Diagnostic géotechnique de l'existant** | **NF P 94-500, annexe A** — mission G5 | L'existant est un bâtiment ancien sur moellons, sans DOE, dont le système de fondation est **inconnu** (D3 p. 2). Un G5 est la mission faite pour ce cas | **R-31bis / V-26** reste un **relevé de chantier** ; l'égalisation de D-09 restera appliquée sans connaissance préalable de l'existant |
| **Extraits du rapport existant** *(immédiat, sans mission nouvelle)* | **Aucune — simple communication de pièce** | Trois extraits suffiraient à lever R-13, R-14 et une partie de R-11 : coupe type, classement XA, classe de sol | **B-40 reste PARAMÉTRIQUE** sur la durabilité et le sismique |

> **Je ne décide pas de la commande.** La fiche B-12 l'interdit explicitement : commander une G3 est une décision **MOA**. Je la recommande, avec sa base normative, et je documente ce qui restera suspendu si elle ne l'est pas — c'est ce document qui nous protégera si les fondations s'avèrent sous-dimensionnées.

---

## 4bis. UN POINT DE TRACABILITÉ À LEVER — DEUX RÉFÉRENCES POUR LE MÊME RAPPORT ?

| Source | Référence citée |
|---|---|
| **D2 p. 1** (cartouche EVEN, ind. C) | **GEOEXPERTS — n° 25.13646/ES/GIF du 22/01/2026** |
| **D-18** (client, 19/10/2026) | **GEOFLORAV2** |

**Je ne les déclare pas identiques.** Ce serait une déduction de ma part, et elle n'est pas établie : `GEOFLORAV2` a la forme d'un **nom de fichier**, `25.13646/ES/GIF` celle d'un **numéro de rapport**. Il est probable qu'il s'agisse du même document — mais « probable » ne suffit pas dans un registre.

**Si ce sont deux documents différents**, nous avons deux jeux d'hypothèses de sol, et il faudra savoir lequel gouverne. **Si c'est le même**, il faut l'écrire une fois, sinon chaque brique reposera sur une hypothèse implicite.

**R-38 est ouverte** : établir le lien entre les deux références et confirmer laquelle fait foi. **Responsable** : MOE / GEOEXPERTS. **Échéance** : avant B-40.

---

## 5. CE QUE D-15 ET D-16 CHANGENT À CET AUDIT — ET CE QU'ELLES NE CHANGENT PAS

**D-16 (absence de nappe) est une déclaration, non une lecture.** Elle est enregistrée comme telle. Son régime est bien construit : elle sort le risque d'épuisement, et l'ENC fait de toute venue d'eau contraire un **point d'arrêt**. C'est la bonne façon de traiter une déclaration qu'on ne peut pas vérifier — on ne l'ignore pas, on l'assortit d'un filet.

**D-15 (tassements hors mission) demande une lecture précise.** « À la charge du géotechnicien » signifie que la vérification incombe au géotechnicien dans le cadre de sa mission — et c'est cohérent : les tassements relèvent bien de lui. Mais **le rapport n'étant pas transmis, nous n'avons aucune preuve que cette vérification a été faite**, ni sur quelles valeurs.

C'est une différence de nature entre :
- « les tassements sont vérifiés par le géotechnicien, dans un document que nous possédons » → nous sommes couverts ;
- **« les tassements sont à la charge du géotechnicien »** → nous sommes couverts **si le document existe et est versé au dossier**. Il ne l'est pas.

**Je ne conteste pas la décision : je signale que sa mise en œuvre suppose la production de la pièce.** Sans elle, la phrase protège le géotechnicien et pas nous.

---

## 6. SYNTHÈSE — HUIT LIGNES

- **Niveau de mission** : **G2 AVP** (NF P 94-500), soit une mission d'**avant-projet** — **insuffisante** pour des calculs d'exécution.
- **Le rapport existe** (GEOFLORAV2) mais **n'est pas transférable** : l'audit porte sur ses extractions déclarées, pas sur le document.
- **Deux valeurs seulement sont pleinement exploitables** : la référence du rapport et la profondeur d'ancrage de 0,5 m.
- **Les trois absences qui bloquent le plus** : la **coupe géologique** (SOL-04), le **classement XA réel** (SOL-05), le **nombre et l'emprise des sondages** (GEO-15).
- **q<sub>ELS</sub> et q<sub>ELU</sub> sont des décisions fondées sur GEOFLORAV2** — sourcées, mais non vérifiables par nous.
- **Recommandation** : **G3** (NF P 94-500) ; à défaut G2 PRO ; G5 pour l'existant non sondé.
- **À défaut de mission** : B-40 reste en **PARTIEL-DÉCLARÉ**, avec filigrane et valeurs déclarées non opposables.
- **Immédiatement** : demander trois extraits du rapport existant — coupe, XA, classe de sol.

---

## 7. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-12) | État | Observation |
|---|---|---|
| Le niveau de mission est identifié avec sa référence normative | ✅ | **G2 AVP**, NF P 94-500 annexe A, avec tableau de la chaîne G1 à G5 |
| Chaque donnée citée est rattachée à un paragraphe ou tableau du rapport | ⚠ **avec réserve** | Rattachée à **D2 p. 1**, aux décisions D-xx et à la référence **GEOFLORAV2** — mais **aucun paragraphe ni tableau** ne peut être cité : le document n'est pas consultable. Déclaré, non dissimulé |
| Chaque donnée manquante est rattachée à son code et à sa brique | ✅ | **8 données**, codes CARNAC, briques et voie d'obtention renseignés |
| La recommandation cite sa base normative et la conséquence de sa non-commande | ✅ | **4 lignes**, NF P 94-500 citée, conséquence écrite pour chacune |
| Aucune valeur de calcul n'a été retenue par moi | ✅ | Toutes les valeurs sont **citées** avec leur source ; aucune n'est proposée ni arbitrée |
| La synthèse tient en 8 lignes | ✅ | **8 lignes** exactement |

**Écart signalé (V4)** : l'audit porte sur un **cartouche**, pas sur un rapport. Il est livré en **PARTIEL-DÉCLARÉ**. Un audit de rapport géotechnique sans le rapport ne peut pas conclure sur la validité des valeurs — et il ne le fait pas.

**Placeholders résiduels (V7)** : aucun.

---

## 8. POINT DE CONTRÔLE HUMAIN

1. **G3** : la recommandez-vous à la MOA, ou suffit-il d'un **G2 PRO** ? *(La fiche B-12 est explicite : un G2 AVP ne couvre pas des calculs EXE. Je recommande la G3, je ne la décide pas.)*
2. **Trois extraits immédiats** : coupe type, classement XA, classe de sol. Les demandez-vous dès maintenant, sans attendre la décision sur la G3 ?
3. **G5** pour l'existant non sondé : la jugez-vous nécessaire, ou le relevé de chantier de R-31bis suffit-il ?
4. **D-15** : la vérification des tassements par le géotechnicien est-elle **matérialisée dans un document** ? Si oui, sa production nous couvre ; si non, la décision protège le géotechnicien mais pas nous.

---

*Brique B-12, **indice B**, livrée en mode **PARTIEL-DÉCLARÉ**.*

> **Note de révision** : indice B = **D-18** — le rapport existe (réf. **GEOFLORAV2**), intransférable ; les hypothèses de sol en sont **extraites**. Les valeurs passent de « déclaration sans source » à « citation déclarée d'un document identifié ». **R-38** ouverte sur la double référence.

*Brique aval **B-13 (Contradictions)** engagée dans le même mouvement.*
