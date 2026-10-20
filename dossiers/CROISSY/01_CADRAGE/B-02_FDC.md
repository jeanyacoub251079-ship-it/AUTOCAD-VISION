# B-02 — FICHE DE DONNÉES DE CONCEPTION (FDC)

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-02** — Fiche de Données de Conception |
| Phase | 0 — Cadrage |
| Modes d'appel | **COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE** selon la ligne |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Entrée | MPD B-01 indice **B** + pièces D1 à D4 + décisions client du 19/10/2026 |
| **Indice du livrable** | **G** (remplace l'indice F du 19/10/2026 — `D-26` : sismique sans objet) |
| Date | 19/10/2026 |
| Brique suivante | B-03 (RDR) — non engagée |

> **Indice G (20/10/2026)** : **`D-26`** — la vérification sismique est **sortie du périmètre** (zone 1, Île-de-France, séisme très faible). `CHG-07a` passe en « contractuelle sans emploi », `CHG-07b` passe en **SANS OBJET**, `H-24` est **neutralisée**.
> **Indice F** : intègre **D-14** (dimension minimale de fondation **60 × 60 cm** — la semelle isolée passe de 25 × 25 à **60 × 60 minimum**), **D-15** (tassements **hors mission**) et **D-16** (**absence de nappe phréatique**). **Prescription ENC révisée en version 3** (douze alinéas), **SOL-03, SOL-06 et SOL-07** mises à jour, **une réserve ouverte (R-36)** sur la justification de l'encastrement.
> *Indice E : D-10 (semelle isolée 25 × 25), D-11 (« PLS »), D-12 (D-09 = plancher) ; ENC v2.*
> *Indice D : décision D-09 — référence au terrain naturel, prescription ENC créée.*
> *Indice C : décision D-08 — encastrement des fondations.*
> **Indice C (historique)** : intègre la décision **D-08** du 19/10/2026 sur l'encastrement des fondations (arase inférieure à −1,00 m, 50 cm dans le bon sol). **SOL-03 passe de VERROU à FOURNIE.** Voir § 0quater.
> *Indice B : décision D-06 sur l'enrobage (50 mm fondations / 30 mm autres structures), § 0ter.*

> **Principe directeur** : la FDC porte les **valeurs** et leur **source**, pas des renvois. Un lecteur de note de calcul doit pouvoir la lire **sans ouvrir le CCTP**.

---

## 0. ACTE DE VALIDATION DE LA MPD — à consigner en B-03

**D-P5 — Validation de la MPD indice B par GO du 19/10/2026.**

Le GO reçu le 19/10/2026 vaut validation de la MPD dans son ensemble, **y compris les trois SANS OBJET proposés** (B-41, B-47, B-48) et le NON NÉCESSAIRE DOC-09. Cette interprétation est retenue faute de validation ligne par ligne distincte ; elle est **réversible** par décision RDR datée.

| Réf. | Objet de la validation | Effet |
|---|---|---|
| D-P5a | B-41 Fondations profondes → SANS OBJET | SOL-04 reste toutefois portée aussi par B-40 (§ 5.4 de B-01) |
| D-P5b | B-47 Escaliers → SANS OBJET | Aucune variable de B-47 en FDC |
| D-P5c | B-48 Prédalles → SANS OBJET | DOC-09 exclue de la FDC (non lue par une brique activée) |
| D-P5d | DOC-09 → NON NÉCESSAIRE (périmètre) | — |

> **Réserve de forme** : cette validation est **globale**, pas ligne par ligne. La fiche B-01 qualifie la validation ligne par ligne de « seul moment où vous pouvez empêcher une brique de s'exécuter à tort ». Le présent acte est donc tracé comme une **validation globale réversible**, et non comme les validations individuelles recommandées.

---

## 0ter. DÉCISION D-P6 — ENROBAGE DES ARMATURES

**Décision du client, 19/10/2026, reçue en cours de B-02.**

| Réf. | Décision | Auteur | Date | Portée |
|---|---|---|---|---|
| **D-P6** | **Enrobage nominal c<sub>nom</sub> = 50 mm pour les fondations** · **c<sub>nom</sub> = 30 mm pour les autres structures** | Client | 19/10/2026 | MAT-03, B-40, B-42, B-43, B-46 |

**Effet sur la FDC** : MAT-03 est scindée en deux lignes distinctes, chacune portant sa valeur et sa fiabilité « Décision ». La valeur de 30 mm du cartouche D2 reste attachée aux structures courantes ; la valeur de 50 mm pour les fondations est **nouvelle** et n'a pas d'équivalent dans les pièces.

**Ce que cette décision tranche** : la valeur d'enrobage des fondations était absente du dossier (le cartouche D2 annonçait « c<sub>nom</sub> = 30 mm (enrobage) » **globalement, sans distinction**), alors que les fondations sont en **XC2 — béton armé au contact de la terre**. La décision apporte une valeur différenciée qui manquait.

**Ce que cette décision ne tranche pas** — voir § 4.5 : la maîtrise de l'écart d'exécution Δc<sub>dev</sub>, et le sort des éléments classés **XC4**.

---

## 0quater. DÉCISION D-08 — ENCASTREMENT DES FONDATIONS

**Décision du client, 19/10/2026, reçue en cours de B-03.**

| Réf. | Décision | Auteur | Date | Portée |
|---|---|---|---|---|
| **D-08** | **Arase inférieure des fondations à −1,00 m**, afin de respecter **50 cm d'encastrement dans le bon sol** (alluvions anciennes) | Client | 19/10/2026 | SOL-03, B-40, B-43, B-46 |

**Effet sur la FDC** : **SOL-03 quitte le tableau 2 et entre au tableau 1** avec fiabilité « Décision ». Le toit des alluvions anciennes se déduit à **−0,50 m** — déduction de la décision, non lecture du rapport.

**Ce que cette décision tranche** : le conflit d'ancrage qui opposait 40 cm (D-04) à ≥ 50 cm (D2 p. 1). La valeur retenue est celle du **BET**, la plus défavorable des deux.

**Ce que cette décision laissait ouvert — et qui est tranché depuis** : la **référence altimétrique** (R-30, fermée par **D-09**), l'**interface avec les semelles existantes** (R-31, fermée par **D-09**), la **géométrie du « 25×25 »** (R-32, fermée par **D-10**) et la **lecture de D-09** (R-34, fermée par **D-12**). Voir § 4.6 et § 4.7.

### Correspondance des numérotations D-P / D-xx

La FDC ayant d'abord utilisé une numérotation provisoire (D-P1 à D-P6), la correspondance avec le RDR est fixée une fois pour toutes :

| Provisoire (FDC ind. B) | Registre (RDR B-03) |
|---|---|
| D-P1 | **D-01** — référentiel G2 AVP |
| D-P2 | **D-02** — q<sub>ELS</sub> 0,30 MPa |
| D-P3 | **D-03** — q<sub>ELU</sub> 0,49 MPa |
| D-P4 | **D-04** — fondations superficielles *(ancrage 40 cm, supersédé par D-08)* |
| D-P5 | **D-05** — validation MPD |
| D-P6 | **D-06** — enrobage 50 / 30 mm |
| — | **D-07** — validation FDC |
| — | **D-08** — encastrement des fondations |

> **La numérotation du RDR fait foi** à compter de l'indice C. Les références D-P subsistantes dans les sections antérieures sont conservées pour la traçabilité de l'indice B et se lisent au moyen de ce tableau.

---

## 0quinquies. DÉCISIONS D-09 À D-16 — NIVEAUX, GÉOMÉTRIE, HYDROGÉOLOGIE ET TERMINOLOGIE

**Décision du client, 19/10/2026, reçue en cours de B-03.**

| Réf. | Décision | Auteur | Date | Portée |
|---|---|---|---|---|
| **D-09** | **Arase inférieure des fondations à −1,00 m par rapport au terrain naturel.** En plan, l'entreprise doit **systématiquement vérifier que les nouvelles fondations sont au même niveau que les fondations existantes** ; dans le cas contraire, elle **ajoute du gros béton pour atteindre le même niveau**. **Cette note doit figurer sur les plans et sur la note de calcul.** | Client | 19/10/2026 | SOL-03, B-40, B-60 |

**Effet sur la FDC** :
- La **référence altimétrique** qui manquait est fixée : c'est le **terrain naturel**. **R-30 fermé.**
- L'**interface avec les fondations existantes** reçoit une méthode : égalisation par gros béton. **R-31 fermé** au niveau conception ; il subsiste une réserve de relevé sur site.
- Une **prescription d'exécution obligatoire** est créée (§ 0sexies) — elle doit être reportée telle quelle sur **tous les plans de fondations (B-60)** et sur **toutes les notes de calcul (B-40)**.
- La cote devient un **minimum** et non une cote fixe (**D-12**, ci-dessous).

### Réponses du 19/10/2026 — D-10, D-11, D-12

| Réf. | Décision | Auteur | Date | Portée |
|---|---|---|---|---|
| **D-10** | **La semelle « 25×25 » est une semelle ISOLÉE** — 25 × 25 cm en plan, et non une semelle filante de section 25 × 25. | Client | 19/10/2026 | SOL-03, B-40 |
| **D-11** | **Le terme « PLS » est maintenu tel quel** ; il désigne le **plan de fondations**, celui qui doit porter la prescription ENC. | Client | 19/10/2026 | B-60 |
| **D-12** | **D-09 est un plancher, pas un plafond** : l'arase à −1,00 m / TN est un **minimum**, jamais une cote fixe. Le nivellement ne s'obtient **jamais par remontée** ; il s'obtient par **approfondissement** et gros béton. | Client | 19/10/2026 | § 0sexies, B-40, B-60 |

**Effet de D-10 — la géométrie change le dimensionnement, pas la cote.** La surface d'assise n'est plus de 2 500 cm² par mètre linéaire mais de **625 cm² par semelle**. À q<sub>ELS</sub> = 0,30 MPa, la charge ELS admissible plafonne à **18,75 kN par semelle** (≈ 1,9 t). B-40 doit vérifier ce seuil par descente de charges : c'est la **condition de validité de D-10**. Si la charge le dépasse, la géométrie doit être revue — et la révision repasse par une décision.

**Effet de D-11 — une prescription n'est opposable que si elle est localisable.** Le sigle n'est développé dans **aucune des pièces dépouillées** ; la recherche du 19/10/2026 sur la couche texte de D2 et D4 donne **zéro occurrence**. Il est donc conservé tel quel, et **B-60** doit porter « PLS » en titre du plan de fondations, faute de quoi le renvoi de D-09 ④ ne désigne rien d'identifiable.

**Effet de D-12 — la cote devient un minimum.** Trois conséquences : ① la cote s'écrit « **−1,00 m / TN mini** » ; ② si l'existant est **plus profond**, on descend et on égalise par gros béton ; ③ si l'existant est **moins profond**, on **ne remonte pas** — l'assise reste à −1,00 m minimum et le raccordement est traité par la structure en B-40. Un plan portant « −1,00 m » sans la règle d'approfondissement est **incomplet**.

### Réponses du 19/10/2026 — D-14, D-15, D-16

| Réf. | Décision | Auteur | Date | Portée |
|---|---|---|---|---|
| **D-14** | **La dimension minimale d'une fondation est de 60 × 60 cm.** La semelle isolée retenue par D-10 passe de 25 × 25 à **60 × 60 cm minimum** | Client | 19/10/2026 | SOL-03, B-40 |
| **D-15** | **Les tassements sont hors mission** — « à la charge du géotechnicien ». Aucune information de tassement ne sera fournie ni vérifiée par nos soins | Client | 19/10/2026 | SOL-07, B-40 |
| **D-16** | **Absence de nappe phréatique** sur le site | Client | 19/10/2026 | SOL-06, B-40, mode d'exécution |

**Effet de D-14 — le dimensionnement change d'échelle, et il change de nature.**

| Grandeur | Semelle 25 × 25 (D-10, ind. E) | **Semelle 60 × 60 (D-14)** | Facteur |
|---|---|---|---|
| Surface d'assise | 625 cm² | **3 600 cm²** | × 5,76 |
| Charge ELS admissible à 0,30 MPa | 18,75 kN | **108 kN** (≈ 11 t) | × 5,76 |
| Charge ELU admissible à 0,49 MPa | 30,6 kN | **176 kN** (≈ 18 t) | × 5,76 |

La condition de validité posée à l'indice E (18,75 kN par semelle) **disparaît** : le seuil passe à **108 kN**, ce qui couvre l'ordre de grandeur d'un poteau reprenant un plancher courant. **D-14 lève donc l'objection technique que l'indice E avait signalée**, sans qu'il ait été besoin d'y revenir.

**Mais D-14 crée un point nouveau, et il est important.** Le rapport d'élancement de l'encastrement s'écarte :

- avec une semelle de **25 cm** de côté, 50 cm d'encastrement donnaient **h/B = 2** — argument de justification de D-08 ;
- avec une semelle de **60 cm** de côté, les mêmes 50 cm donnent **h/B = 0,83**.

Le mécanisme de rupture d'une semelle de 60 cm développe un bulbe qui s'étend sur environ 1,5 B, soit **90 cm** — au-delà des 50 cm de bon sol disponibles au-dessus de l'assise. **L'argument « h/B = 2 » ne tient plus et ne doit plus être invoqué.** La justification de l'encastrement repose désormais sur un autre fondement, qui reste valable : l'assise est **entièrement dans les alluvions**, dont le toit est déduit à **−0,50 m**. C'est suffisant pour porter, ce n'est plus suffisant pour revendiquer h/B = 2. **R-36** est ouverte pour que le BET tranche — approfondir, ou justifier autrement.

**Effet de D-15 — un transfert de risque qui doit être écrit, pas subi.** La mission G2 AVP couvre normalement les tassements. En les déclarant hors mission, le client place cette vérification **chez le géotechnicien** — ce qui est cohérent avec sa mission, mais crée une conséquence pour nos livrables : **B-40 ne vérifiera pas les tassements**, et devra le porter explicitement, en toutes lettres, avec la mention du report de responsabilité. Un silence sur ce point serait plus grave qu'une vérification absente. La prescription ENC (alinéa 9) l'inscrit.

**Effet de D-16 — la nappe sort du risque de chantier.** L'absence de nappe retire l'épuisement, le blindage hydraulique et le risque de délavage sous les soubassements, qui avaient motivé la requalification **V-R3**. Cette requalification est **annulée par décision client** (V-R4), tracée au RDR. Une réserve de méthode subsiste : une fouille à −1,00 m en fond de vallée de la Seine ne rencontre pas de nappe **selon la déclaration**, et toute venue d'eau contraire à cette déclaration devient un **point d'arrêt** (alinéa 8 de l'ENC).

---

## 0sexies. PRESCRIPTION D'EXÉCUTION À REPORTER SUR LES PLANS ET NOTES DE CALCUL

> **Texte à reproduire intégralement et sans modification** sur le plan de fondations (« **PLS** », D-11) et **en tête** de chaque note de calcul de fondation. C'est un livrable au sens du carnet : il porte un numéro, il est opposable, il ne se reformule pas.

**ENC — PRESCRIPTION FONDATIONS — CROISSY-FLORA — 19/10/2026 — version 3 (indice F)**

1. **Arase inférieure des fondations nouvelles : −1,00 m par rapport au terrain naturel, MINIMUM.** Cette cote n'est **jamais une cote fixe** : elle peut être approfondie, jamais remontée.
2. **Encastrement minimal dans les alluvions anciennes : 0,50 m** sous l'arase inférieure.
3. Les fondations sont **superficielles**, de type **semelles isolées de 60 × 60 cm au minimum** ; contrainte admissible **q<sub>ELS</sub> < 0,30 MPa**, **q<sub>ELU</sub> < 0,49 MPa** (G2 AVP GEOEXPERTS). Le minima de 60 × 60 cm est une **dimension plancher** : elle peut être augmentée par le calcul, jamais réduite.
4. **L'entreprise vérifie systématiquement, à l'ouverture des fouilles, que chaque fondation nouvelle se trouve au même niveau que la fondation existante correspondante.**
5. **Lorsque la fondation existante est PLUS PROFONDE**, l'entreprise descend au niveau de celle-ci et **complète par du gros béton C16/20**. Le gros béton est coulé **sous** la nouvelle semelle ; il ne se substitue jamais à la semelle.
6. **Le nivellement ne s'obtient jamais par remontée.** Si la fondation existante est **moins profonde**, la fondation nouvelle **reste à −1,00 m / TN minimum** ; l'écart est rattrapé par la structure (B-40). Le gros béton ne sert jamais à remonter une assise.
7. **Aucune fondation nouvelle ne peut être laissée à un niveau supérieur à celui de la fondation existante.**
8. **Absence de nappe phréatique déclarée. Les fouilles sont réputées hors nappe.** Toute venue d'eau contraire à cette déclaration constitue un **point d'arrêt** : arrêt de la fouille, constat contradictoire, reprise de la méthode d'exécution.
9. **Les tassements ne sont pas vérifiés par nos soins** : ils sont hors mission et relèvent du géotechnicien (mission G2 AVP GEOEXPERTS). La présente note ne vaut pas vérification de tassement, ni absolu, ni différentiel.
10. La conformité du niveau et de la nature du fond de fouille fait l'objet d'une **réception contradictoire (point d'arrêt)** avant coulage.
11. **Béton de structure C25/30** · **gros béton C16/20** · **aciers S500B** · **enrobage 50 mm en fondation**.
12. **Report obligatoire** : la présente note figure **intégralement** sur le plan de fondations (« PLS », B-60) et **en tête** de la note de calcul (B-40). Un plan portant la seule cote « −1,00 m » est **incomplet** par omission.

> **Note de portée** : cette prescription est une **règle d'exécution**, pas une variante de conception. Elle ne crée aucune valeur : la géométrie vient de **D-14**, la cote de **D-08 / D-09**, son caractère de minimum de **D-12**, l'absence de nappe de **D-16**, le hors-mission des tassements de **D-15**. Elle fixe le **critère de conformité** du fond de fouille et le rend **opposable**.

---

## 1. TABLEAU 1 — VARIABLES RÉSOLUES

### 1.1 Identification et documents

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| ID-01 | Code projet | `CROISSY-FLORA` | — | Décision D-P0, B-00 ind. B | **Décision** | toutes |
| ID-02 | Intitulé de l'opération | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical | — | D1 p. 1 · D2 p. 1 · D4 p. 1 (ind. C) | **Contractuelle** | toutes |
| ID-07 | Date de l'étude | 19/10/2026 | — | Session | **Décision** | B-03 |
| DOC-01 | Inventaire des pièces | 5 pièces : C0 carnet, D1 CCTP, D2 plans BET, D3 diagnostic, D4 pièces graphiques | — | B-00 ind. B | **Contractuelle** | B-00, B-01 |
| DOC-03 | Plans BET structure | 4 folios + cartouche de données d'études, affaire **24.09.356E**, indice **C** du 16/03/2026 — **2 zones « non relevées »** (folio 02) | — | D2 p. 1 à 5 | **Contractuelle** *(réserve C-19)* | B-10, B-11, B-20 |
| DOC-04 | CCTP / pièces contractuelles | Lot 01 GO – Structure – Déplombage – Installation de chantier, **V1 stade PRO**, 13/03/2026, 38 pages, affaire EICP **014-2024-08** | — | D1 p. 1 à 4 | **Contractuelle** *(réserve C-07 : aucune section charpente bois)* | B-10, B-14 |
| DOC-05 | Diagnostic structure | **18 pages**, EVEN STRUCTURES, **24/03/2025**, 9 désordres, vérifications EC5 et EC3 | — | D3 p. 1 à 18 | **Contractuelle** | B-11, B-23, B-24 |
| DOC-06 | Rapport géotechnique | **G2 AVP** — GEOEXPERTS, rapport **n° 25.13646/ES/GIF** du **22/01/2026** *(référence seule ; contenu non transmis)* | — | D2 p. 1 + **D-P1** (19/10/2026) | **Décision** | B-12, B-41 |

### 1.2 Existant — géométrie et sections

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| EXI-01a | Solives plancher A | **8 × 18** cm, entraxe **0,50** m | cm / m | D3 p. 10 | **Contractuelle** | B-23, B-24, B-44 |
| EXI-01b | Poutre plancher A | **20 × 15** cm (b = 200, h = 150 mm) | cm | D3 p. 10 et 16 | **Contractuelle** | B-23, B-24, B-44 |
| EXI-01c | Solives plancher B | **IPE 160**, entraxe **0,72** m | mm / m | D3 p. 11 | **Contractuelle** | B-23, B-24, B-44 |
| EXI-01d | Poutre plancher B | **IPE 330** — réaction d'appui centrale **6,9 t** | mm / t | D3 p. 12 | **Contractuelle** | B-23, B-24, B-44 |
| EXI-01e | Complexe plancher A | Lambourde + parquet **20** daN/m² · lattis-plâtre **20** daN/m² | daN/m² | D3 p. 10 | **Contractuelle** | B-21 |
| EXI-01f | Complexe plancher B | Hourdis briques creuses **7** cm (900 daN/m³) · polystyrène **8** cm · chape béton **10** cm | cm | D3 p. 11 | **Contractuelle** | B-21 |
| EXI-02 | Pathologies relevées | **9 désordres** localisés et décrits (D1 à D9) | — | D3 p. 3 à 8 | **Contractuelle** | B-23 |
| EXI-03 | Résistance des matériaux existants | Bois massif **C18** à 12 % d'humidité — **hypothèse de calcul** du diagnostic | — | D3 p. 10 | **À confirmer** | B-24, B-44 |
| NIV-02a | Niveaux RDC | **Z = 201,03 à 201,26** m | m | D4 p. 4 et 6 | **Contractuelle** | B-43 |
| NIV-02b | Niveaux R+1 | **Z = 203,59 à 204,43** m | m | D4 p. 4 et 6 | **Contractuelle** | B-43 |
| NIV-02c | Faîtages et gouttières | Faîtages **Z = 209,19 à 210,32** m · gouttières **Z = 205,41 à 206,57** m | m | D4 p. 26 et 27 | **Contractuelle** | B-44 |
| NIV-03 | Hauteurs libres | RDC hsp **2,16 à 3,25** m · R+1 hsp **2,31 à 2,62** m | m | D4 p. 4 et 6 | **Contractuelle** | B-42, B-43 |

### 1.3 Ouvrages projetés — renforcements (D2 folio 01)

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| MAT-05a | Frangement F1 | **2 × HEA 200**, en renfort du linteau bois existant | — | D2 folio 01 (ind. C) | **Contractuelle** | B-45, B-49, B-50 |
| MAT-05b | Frangements F2 / F3 / F4 | **HEB 200** / **HEB 160** / **IPE 200** | — | D2 folio 01 | **Contractuelle** | B-45, B-49, B-50 |
| MAT-05c | Renforts R1 / R2 / R3 | **2 × UPE 200** / **HEB 160** / **UPE 200** | — | D2 folio 01 | **Contractuelle** | B-45, B-50 |
| MAT-05d | Poteau P1 | **Tube carré 140 × 140** | mm | D2 folio 01 | **Contractuelle** | B-42, B-45, B-50 |
| MAT-05e | Stab1 | Entretoises anti-déversement IPE, **incorporées dans le voutain brique**, saignée ponctuelle | — | D2 folio 01 | **Contractuelle** | B-45 |
| MAT-01a | Béton de structure | **C25/30** | — | D2 p. 1 | **Contractuelle** | B-40, B-42, B-46 |
| MAT-01b | Gros béton | **C16/20** | — | D2 p. 1 | **Contractuelle** | B-40 |
| MAT-04 | Nuance d'acier BA | **S500B** — f<sub>yk</sub> = 500 MPa · **S220B** — f<sub>yk</sub> = 220 MPa | MPa | D2 p. 1 | **Contractuelle** | B-40, B-42, B-46 |
| MAT-05f | Nuance d'acier de charpente | **S275** | — | D2 p. 1 | **Contractuelle** | B-45, B-49, B-50, B-62 |
| **MAT-03a** | **Enrobage nominal — fondations** | **c<sub>nom</sub> = 50** mm — éléments en **XC2** (au contact de la terre) | mm | **D-P6** (19/10/2026) — *valeur absente des pièces ; le cartouche D2 ne distinguait pas les fondations* | **Décision** | B-40, B-43 |
| **MAT-03b** | **Enrobage nominal — autres structures** | **c<sub>nom</sub> = 30** mm — classe structurale **S4** | mm | **D-P6** (19/10/2026) + D2 p. 1 | **Décision** *(résiduel : Δc<sub>dev</sub> et éléments XC4 — voir § 4.5)* | B-42, B-46 |

### 1.4 Ouvrages projetés — fondations (D2 folio 03)

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| EXI-07a | Semelle neuve | **Semelle BA 25 × 25** — « remplacement poteau et allège pour création d'une semelle BA 25×25 sur soubassement moellons existant » | cm | D2 folio 03 (ind. B) | **Contractuelle** | B-40 |
| EXI-07b | Arase | « arase béton à prévoir pour alignement avec dallage » | — | D2 folio 03 | **Contractuelle** | B-40, B-43 |
| EXI-07c | Bêche | « bêche pour réhausse niveau dallage » | — | D2 folio 03 | **Contractuelle** | B-40 |
| EXI-07d | Débord existant | « débord de semelle, rendu apparent à conserver en l'état » | — | D2 folio 03 | **Contractuelle** | B-40, B-46 |
| EXI-07e | Reprise en sous-œuvre | « reprise en sous-œuvre des semelles existantes par **passes alternées de gros béton** » | — | D2 folio 04 (ind. B) | **Contractuelle** | B-40, B-46 |
| EXI-07f | Soubassement existant | **Moellons** — « pierre dure », bon état apparent | — | D2 folio 03 · D3 p. 17 · D4 p. 19 | **Contractuelle** | B-46 |

### 1.5 Actions

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| CHG-05 | Neige | Zone **A1** · altitude **< 200 m** · **sk = 45** · **sAd non renseigné (« – »)** | daN/m² | D2 p. 1 | **Contractuelle** *(sAd absent)* | B-21, B-44 |
| CHG-06 | Vent | Zone **2** · **vb = 24** · c<sub>d</sub> = **1** (10°-150° : 0,70) · saison **1** (avril-sept. : 0,80) · terrain **III** | m/s | D2 p. 1 | **Contractuelle** | B-21, B-44, B-45 |
| CHG-07a | Zone de sismicité | **Zone 1** · catégorie d'importance **II** — **AUCUNE VÉRIFICATION SISMIQUE PRODUITE** (zone 1, séisme très faible — `D-26`) | — | D2 p. 1 + **D-26** | **Contractuelle — sans emploi** | *aucune brique : sortie de périmètre* |

### 1.6 Sol et fondations

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| SOL-01 | Contrainte admissible ELS | **q<sub>ELS</sub> < 0,30** | MPa | D2 p. 1 **+ D-02** (19/10/2026) | **Décision** | B-12, B-40, B-43 |
| SOL-02 | Contrainte admissible ELU | **q<sub>ELU</sub> < 0,49** | MPa | **D-03** (19/10/2026) | **Décision** | B-40 |
| **SOL-06** | **Nappe, hydrologie, drainage** | **Absence de nappe phréatique** sur le site. Fouilles réputées hors nappe ; toute venue d'eau contraire = point d'arrêt | — | **D-16** (19/10/2026) — *déclaration client, non lue au rapport GEOEXPERTS* | **Décision** | B-40, mode d'exécution |
| **SOL-03** | **Profondeur de bon sol et ancrage** | **Arase inférieure des fondations à −1,00 m par rapport au TERRAIN NATUREL, MINIMUM — jamais une cote fixe (D-12)** · **encastrement 50 cm dans les alluvions anciennes** · toit des alluvions **déduit à −0,50 m** · **semelles isolées 60 × 60 cm au minimum (D-10 + D-14)** · **égalisation avec les fondations existantes par gros béton C16/20, par approfondissement seulement** | m | **D-08 + D-09 + D-10 + D-12 + D-14** (19/10/2026) — *valeur absente des pièces ; D2 p. 1 indiquait seulement « au moins 0,5 m »* | **Décision** | B-40, B-60 |
| SOL-08 | Mission géotechnique disponible | **G2 AVP** — **pas de G2 PRO, pas de G3** | — | D-01 (19/10/2026) · D2 p. 1 | **Décision** | B-12 |
| SOL-09 | Type de fondation retenu | **Fondations superficielles** | — | **D-04** (19/10/2026) | **Décision** | B-40 |

### 1.7 Programme et démolition (D4)

| Code | Libellé | Valeur | Unité | Source | Fiabilité | Brique(s) |
|---|---|---|---|---|---|---|
| CHG-01a | Programme RDC | Plateau technique **33,14** · Box kiné 1/2/3 **11,20 / 9,60 / 9,15** · Bureau 1/2 **16,08 / 12,80** · Sanitaire PMR **5,19** | m² | D4 p. 6 et 9 | **Contractuelle** | B-21 |
| CHG-01b | Programme R+1 | **Salle de sport 34,25** · Salle commune **11,75** · Vestiaire **9,32** · Douche **2,37** · Bureau consult. 3/4 **13,26 / 16,50** · Dégagement **5,96** · Attente **8,38** | m² | D4 p. 6 et 9 | **Contractuelle** | B-21 |
| GEO-05 | Baies et ouvertures | Nomenclatures portes et menuiseries **M0-02 à M0-11 · M1-01 à M1-10 · M2-01 à M2-05 · PV-01 à PV-10 · PL73 / PL83 / PL93 · PG80 / PG90** | — | D4 p. 23 à 25 | **Contractuelle** | B-49 |
| EXI-08 | Travaux de démolition prescrits | **3 murs démolis** · **1 ouverture mur** · **1 ouverture agrandie** · passage **90 × 210 cm** · « dépose des dalles » · sol à décaisser **6 cm** · sol à recharger **15 cm** · décaissements en pente **10 % (16,8 cm)** et **6 % (3,2 cm)** | — | D4 p. 5 | **Contractuelle** | B-43, B-46 *(contrainte de coordination, hors périmètre CARNAC)* |

---

## 2. TABLEAU 2 — VERROUS

### 2.1 Verrous par conflit entre pièces — **non arbitrés** (règle 6 de B-02)

| Code | Brique suspendue | Voie d'obtention proposée | Responsable pressenti |
|---|---|---|---|
| ~~**SOL-03** — ancrage~~ | ~~B-40~~ | **FERMÉ par D-08 le 19/10/2026** — ancrage fixé à **50 cm** dans le bon sol, arase inférieure à **−1,00 m**. La valeur est portée au tableau 1 | — |
| **MAT-02 / SOL-05** — classe d'exposition | B-40, B-42, B-43, B-47 | **Décision MOA / BET.** « **XA4** » (D2 p. 1) **n'existe pas** dans la NF EN 206/CN, qui ne définit que **XA1, XA2, XA3**. Le rapport GEOEXPERTS donnera le classement réel | EVEN Structures / GEOEXPERTS |
| **CHG-02** — surcharges d'exploitation | B-21 | **Décision MOA.** Deux valeurs incompatibles :<br>· **250 daN/m²** — D2 p. 1 (cabinet paramédical / bureaux)<br>· **150 daN/m²** — D3 p. 10-11 (logement) | MOE / MOA |
| **CHG-03** — poids propres de plancher | B-21 | **Décision MOE.** Hypothèses D2 : plancher métallique **350**, plancher bois **100** daN/m². Or D4 p. 5 et 14 prescrit « **sol à recharger de 15 cm** », soit **255 à 330 daN/m²** non intégrés | MOE / BET |
| **MAT-03b (résiduel)** — écart d'exécution Δc<sub>dev</sub> et éléments XC4 | B-42, B-46 | **Décision MOE / BET.** Deux points restent ouverts après D-P6 :<br>· la valeur de **Δc<sub>dev</sub>** n'est pas fixée — c'est elle qui rend 30 mm cohérent ou non (voir § 4.5) ;<br>· les **éléments en XC4** (« béton soumis au contact de l'eau ») restent couverts par 30 mm alors qu'ils relèvent d'une exigence plus forte | EVEN Structures / MOE |
| **ID-05** — indice du dossier | B-03, B-64, B-71 | **Décision MOE.** Trois indicages non concordants : D1 « V1 » (13/03/2026) · D2 « C » (16/03/2026) · D4 « C » (13/03/2026) | MOE |

### 2.2 Verrous par donnée absente ou non transmise

| Code | Brique suspendue | Voie d'obtention proposée | Responsable pressenti |
|---|---|---|---|
| **DOC-06** — contenu du rapport géotechnique | B-12 *(partiellement)* | **Mission G** — demander 3 extraits : coupe type + toit des alluvions, niveau de nappe, tassements admissibles | MOE auprès de GEOEXPERTS |
| **SOL-04** — nature et succession des couches | B-40 *(en sus du rattachement B-41)* | **Mission G** — coupe géologique type | GEOEXPERTS |
| **EXI-04** — sondages destructifs | B-24 | **Relevé** — fiches de sondage et emplacements cotés | EVEN Structures |
| **EXI-05** — contrainte admissible transmise à l'existant | B-23, B-46 | **Essai** — caractérisation de la maçonnerie de moellons (compression, module) | Mission diagnostic / laboratoire |
| **EXI-01g** — sections de charpente | B-44 | **Relevé** — sections des pannes, fermes et poteaux ; 2 zones « non relevées » au folio 02 | Géomètre / BET |
| **MAT-06** — classe de bois de charpente | B-44, B-50, B-62 | **Relevé / essai** — classement visuel ou mécanique des bois en place | BET bois / contrôle |
| **MAT-07** — résistance de la maçonnerie existante | B-46, B-49, B-50 | **Essai** — résistance des moellons et du mortier | Laboratoire |
| **MAT-09** — classe de bloc NF EN 771-3 | B-46 | **Décision MOE** — CCTP § 01.2.1.7.5 : « blocs pleins ou semi-pleins », sans classe | BET structure |
| **MAT-10** — classe de mortier | B-46 | **Décision MOE** — CCTP : « mortier hydrofugé », sans classe (M2,5 à M10) | BET structure |
| **MAT-11** — type de maçonnerie | B-46 | **Décision MOE** — chaînée / armée / non armée non précisé | BET structure |
| **MAT-12** — chaînages existants | B-46 | **Relevé** — aucun chaînage relevé au diagnostic ni représenté | BET / ouverture de sondages |
| **MAT-08** — classe de service et durée de charge | B-44 | **Décision BET** — produite par B-22 ; les désordres d'humidité 4, 6, 7 et 8 imposent de trancher classe 1 ou 2 | B-22 |
| **CHG-04** — poids propres de toiture | B-21, B-44 | **Relevé** — couvertures identifiées (tuiles, ardoises, béton, zinc) **sans aucune charge** | BET / MOE |
| **CHG-08** — cloisons et équipements lourds | B-21, B-43 | **Relevé + Décision** — 4 types de cloisons sans poids ; ballon ECS 300 L, chaudière ADe Dietrich GT 413, chambre froide | MOE / BET |
| ~~**CHG-07b** — a<sub>gr</sub> et classe de sol~~ | ~~B-42, B-46~~ | **SANS OBJET par `D-26`** — aucune vérification sismique n'est produite. `H-24` (sol C, `a_gr = 0,40`) est **neutralisée mais conservée** au registre, réactivable en cas de reclassement de zone | — |
| **SEC-01** — degré coupe-feu par élément | B-42, B-43, B-49 | **Décision MOE** — section SECURITE INCENDIE **intégralement vide** (catégorie, CF, SF, locaux à risques) | MOE / bureau d'études incendie |
| **SEC-03** — classement termites | B-43 | **Décision MOE** — traitement prescrit sans arrêté préfectoral ni classement de la commune | MOE |
| **DOC-08** — plans de récolement / DOE | B-11 | **Relevé** — aucun DOE ; fondations décrites « inconnues » au diagnostic | MOA |
| **GEO-01** — emprise cotée | B-43, B-44 | **Relevé** — contour existant graphiquement (D4 p. 6 et 9) mais **aucune cote d'ensemble** ; extraction sur DXF | Géomètre / B-30 |
| **GEO-06 / GEO-07 / GEO-08** — unités, transformation, points de calage | B-30, B-31, B-32, B-33 | **Relevé** — **DXF non fourni** ; aucun point de calage commun entre D2 et D4 | MOE |
| **DEC-01 à DEC-04** | B-70, B-71, B-72 | **Décision** — produits par B-03 (RDR) et B-71 (indiçage) | B-03 |
| **GEO-10 / GEO-11 / GEO-12** — seuils | B-30, B-31, B-32, B-33 | **Décision** — existant ancien et irrégulier : le maître §5 impose une **valeur déclarée au RDR** | B-03 |
| **OUT-01 à OUT-04** | B-30 à B-62 | **Décision / production** — environnement : Python 3.11 + PyMuPDF ; **ezdxf 1.4.5 installé le 19/10/2026 sur instruction client**, en attente du fichier DXF. Scripts et journaux à produire | B-30 à B-62 |

---

## 3. SYNTHÈSE

| Indicateur | Valeur |
|---|---|
| Variables portées au **tableau 1** (avec valeur et source) | **40** |
| Variables portées au **tableau 2** (VERROU) | **27** |
| dont verrous **par conflit** entre pièces | **4** (MAT-02/SOL-05, CHG-02, CHG-03, ID-05) — *SOL-03 fermé par D-08* |
| dont verrous **par données de terrain** | **9** (SOL-04, EXI-04, EXI-05, EXI-01g, MAT-06, MAT-07, MAT-12, CHG-04, DOC-08) — *SOL-06 soldé par D-16, SOL-07 sorti du périmètre par D-15* |
| dont verrous **par décision à prendre** | **14** *(dont MAT-03b résiduel, ouvert par D-P6)* |
| Variables **NON NÉCESSAIRE** exclues de la FDC | **2** — DOC-09 (aucune prédalle) et **SOL-07** (tassements **hors mission**, motif de périmètre : D-15) |
| **Décisions client intégrées** | **15** (D-01 à D-16, dont D-13 = validation sans valeur) |

**Lecture** : près de la moitié du tableau de données est verrouillée, et **onze de ces verrous sont des données de terrain** que nulle relecture de pièce ne produira. Ce n'est pas un défaut du dossier : c'est la nature d'une réhabilitation d'existant non sondé.

---

## 4. OBSERVATIONS D'INGÉNIEUR

### 4.1 Ce carnet a été écrit sur ce projet — et le dit

La fiche B-02 cite **deux fois le « projet Flora »** comme cas d'origine :

- « le traitement explicite de la contradiction **XC2/35 mm vs XA3/50 mm du projet Flora** » ;
- « **40 mm d'enrobage** "au titre des exigences de tenue au feu" ont été retenus **sans que ces exigences existent** ».

Autrement dit, ce carnet est un retour d'expérience : il a été construit **contre les erreurs commises sur cette affaire**. Cela donne deux consignes opérationnelles précises pour la suite :

1. **Ne jamais retenir un enrobage au titre du feu** tant que SEC-01 est vide. C'est exactement le piège documenté. Le cartouche D2 annonce « stabilité au feu obtenue par encoffrement » sans aucune exigence — l'encoffrement se dimensionne sur un CF/SF qui n'existe pas encore.
2. **L'exposition béton est l'autre piège.** Le carnet cite « XA3/50 mm » ; le DCE de Croissy écrit « XA4 » avec 30 mm. Le rapport GEOEXPERTS tranchera — et s'il annonce XA3, c'est l'enrobage qui devra être revu, pas seulement la classe d'exposition.

### 4.2 SOL-03 est passé de VERROU à décision — la discipline est la même

À l'indice A, SOL-03 restait un **VERROU** : la règle 6 interdisait d'arbitrer le conflit entre 40 cm (déclaration D-04) et ≥ 50 cm (D2 p. 1), et une note reprenant 0,50 m sans arbitrage aurait porté une hypothèse non tracée.

**Le verrou est levé, non contourné** : c'est **D-08** qui a tranché, puis **D-09**, **D-10** et **D-12** qui l'ont completé. SOL-03 est au **tableau 1** en fiabilité « Décision ». La valeur n'est pas plus « sûre » qu'avant — elle est **opposable**, ce qui n'est pas la même chose.

### 4.3 La contrainte admissible est désormais complète

C'est le gain principal de vos informations : **q<sub>ELS</sub> = 0,30 MPa** et **q<sub>ELU</sub> = 0,49 MPa** permettent à B-40 de mener une vérification complète ELS + ELU, ce qui n'était pas possible avec le seul cartouche D2. B-40 n'est plus suspendue que par **SOL-04** (coupe type) : la **nappe** est déclarée absente (D-16) et les **tassements** sont hors mission (D-15). Aucun des deux n'affectait la portance.

### 4.4 Une correction assumée sur GEO-01

La MPD B-01 indiquait GEO-01 « FOURNIE ». À l'établissement de la FDC, force est de constater qu'**aucune cote d'ensemble** ne figure dans la couche texte de D4 : les plans portent des cotes de détail, pas une cote de bâtiment. GEO-01 passe donc en **VERROU** au tableau 2. L'écart est signalé, non dissimulé.

### 4.5 La décision D-P6 est juste sur les fondations, incomplète sur le reste

C'est le point le plus important de cet indice, et il demande une décision complémentaire de votre part.

**Ce qui est cohérent.** Le vérifier demande de confronter les deux valeurs à la classe structurale **S4** que porte le cartouche D2 et à l'exposition **XC2** des fondations.

| Élément | Exposition | c<sub>min,dur</sub> (EC2, générique) | Δc<sub>dev</sub> | c<sub>nom</sub> requis | D-P6 | Verdict |
|---|---|---|---|---|---|---|
| **Fondations** (semelle, bêche, arase) | **XC2** | **40 mm** | 10 mm | **50 mm** | **50 mm** | ✅ **exactement conforme** |
| Structures courantes, voiles intérieurs | **XC1** | **25 mm** | **5 mm** | **30 mm** | **30 mm** | ✅ conforme **si** Δc<sub>dev</sub> = 5 mm |
| Structures courantes, voiles intérieurs | **XC1** | 25 mm | **10 mm** | **35 mm** | 30 mm | ❌ **insuffisant de 5 mm** |
| Éléments en contact avec l'eau | **XC4** | **45 mm** | 10 mm | **55 mm** | 30 mm | ❌ **insuffisant de 25 mm** |

> *Valeurs c<sub>min,dur</sub> lues sur la table 4.4N de l'EN 1992-1-1 (valeurs génériques). L'Annexe Nationale française modifie cette table : les valeurs doivent être recoupées sur l'AN FR avant figage en note de calcul. Elles sont citées ici comme **référence de cohérence**, non comme données de projet — elles ne figurent donc pas au tableau 1.*

**Trois conséquences.**

1. **Votre valeur de 50 mm pour les fondations n'est pas un choix de confort : c'est la valeur normative.** Pour XC2 en classe S4 avec Δc<sub>dev</sub> = 10 mm, l'EC2 exige précisément 50 mm. Cela confirme, a posteriori, que le cartouche D2 était **structurellement faux** en annonçant 30 mm « sauf indications contraires » pour l'ensemble de l'ouvrage, fondations comprises. D-P6 corrige une erreur de conception, pas une préférence.

2. **Les 30 mm pour les autres structures ne tiennent que si Δc<sub>dev</sub> = 5 mm.** L'EC2 n'autorise cette réduction que si le bétonnage est couvert par un **système qualité** garantissant un écart d'exécution réduit (maîtrise renforcée, contrôle des cales, tolérances de coffrage). Sans cette mention, la valeur à retenir est **35 mm**. C'est exactement le type d'écart que le carnet cherche à empêcher : une valeur juste en apparence, fausse faute d'hypothèse déclarée.

3. **Les éléments classés XC4 ne sont pas couverts.** Le cartouche D2 liste « **XC4 — béton soumis au contact de l'eau** » parmi les classes du projet. À 30 mm, ils seraient sous-dimensionnés de 25 mm. Or le programme comporte **douche, sanitaire PMR, local de nettoyage** et, en infrastructure, une **bêche pour réhausse de niveau de dallage** — éléments susceptibles de relever de XC4. Il faut **nommer les éléments XC4**, ou constater qu'il n'y en a pas.

**Ce que je recommande, sans le décider** (les deux points relèvent du RDR) :

| Point ouvert | Décision attendue |
|---|---|
| **MAT-03b résiduel (a)** — valeur de Δc<sub>dev</sub> | Fixer **Δc<sub>dev</sub> = 5 mm** avec mention explicite du système qualité, **ou** porter l'enrobage des structures courantes à **35 mm** |
| **MAT-03b résiduel (b)** — éléments XC4 | **Nommer les éléments** concernés et leur appliquer un enrobage propre (55 mm en XC4/S4), **ou** acter qu'aucun élément n'est en XC4 et retirer cette classe du cartouche |

Tant que ces deux points ne sont pas tranchés, **MAT-03b reste au tableau 1** — la valeur de 30 mm existe et est décidée — **mais assortie du verrou résiduel** qui interdit à B-42 et B-46 de la consommer en mode COMPLET.

### 4.6 La géométrie est désormais doublement tranchée — 60 × 60 minimum, et cela change l'argument de l'encastrement

> **Mise à jour indice F** : R-32 (géométrie) était fermée par **D-10** à 25 × 25 cm. **D-14** porte la dimension minimale à **60 × 60 cm**. Le point ouvert n'est plus la géométrie mais sa **conséquence sur la justification de l'encastrement** — **R-36**.

| Point | État à l'indice F | Conséquence |
|---|---|---|
| ~~Référence altimétrique~~ (R-30) | ✅ Fermé par D-09 — terrain naturel | Terme de surcharge calculable |
| ~~Interface avec l'existant~~ (R-31) | ✅ Fermé par D-09 — égalisation gros béton | Méthode à appliquer et contrôler |
| ~~Géométrie du « 25×25 »~~ (R-32) | ✅ Fermée par D-10, **redimensionnée par D-14** | Semelle **isolée 60 × 60 cm minimum** |
| **Justification de l'encastrement** (R-36) | ⚠ **OUVERTE** | Voir ci-dessous — l'argument h/B = 2 tombe |

**Ce que D-14 apporte, chiffré.** À q<sub>ELS</sub> = 0,30 MPa, une semelle de 3 600 cm² porte **108 kN** à l'ELS et **176 kN** à l'ELU (0,49 MPa). Le seuil de 18,75 kN qui rendait D-10 fragile est effacé : la semelle isolée devient dimensionnante pour un poteau courant, et le risque de rejet de la géométrie par la descente de charges s'éloigne fortement.

**Ce que D-14 retire, et qu'il faut dire.** L'encastrement de 50 cm avait été justifié, à l'indice B, par le rapport **h/B = 2** obtenu avec une semelle de 25 cm de large — « suffisant pour que le mécanisme de rupture se développe dans la couche portante ». Avec **B = 60 cm**, ce rapport tombe à **0,83**. Le bulbe de contrainte d'une semelle de 60 cm s'étend sur environ 1,5 B ≈ **90 cm**, soit au-delà des 50 cm de bon sol disponibles au-dessus de l'assise.

**La conséquence n'est pas que la fondation ne porte pas** : elle porte, et les 108 kN le montrent. La conséquence est que **l'argument de justification employé jusqu'ici n'est plus valable** et ne doit plus être repris dans la note de calcul. Le fondement qui reste est celui du **toit des alluvions déduit à −0,50 m** : l'assise à −1,00 m est entièrement dans le bon sol, avec 50 cm de portance sous la base.

**R-36 est ouverte** pour que le BET tranche entre deux voies : approfondir l'assise pour retrouver un encastrement proportionné à 60 cm, ou maintenir −1,00 m en justifiant la portance sur la seule qualité du sol d'assise. **Je ne tranche pas** : les deux sont défendables et le choix appartient au BET.

**Sur l'erreur de l'indice D** : le rapport des surfaces d'assise y était annoncé « d'un facteur 40 » ; il valait **4** (2 500 cm²/m contre 625 cm²). Cette erreur reste tracée ici. Elle est désormais sans effet, D-14 ayant porté la géométrie à 3 600 cm².

### 4.7 D-08 et D-09 divergeaient — l'arbitrage D-12 tient, et D-14 ne le change pas

**Ces critères ne coïncident que si les fondations existantes ont elles-mêmes leur arase à −1,00 m / TN.**

| Situation rencontrée | Ce que demandait une lecture littérale de D-09 | Issue sous D-12 | Issue sous D-14 |
|---|---|---|---|
| Existantes **plus profondes** | Descendre au niveau de l'existante, gros béton sous la semelle | **Appliquer** | **Appliquer** — le gros béton reste sous la semelle 60 × 60 |
| Existantes **moins profondes** | Remonter au niveau de l'existante | **Ne pas remonter** — assise maintenue à −1,00 m mini | **Ne pas remonter** — idem |
| Existantes **à −1,00 m** | Rien à faire | **Appliquer** | **Appliquer** |

**D-14 ne modifie pas la règle de niveau** : elle ne change que l'emprise de la semelle, donc le volume de gros béton d'égalisation. Un point pratique en découle, à porter en B-40 : avec une semelle de 60 cm de côté, le massif de gros béton sous-jacent est plus large qu'avec 25 cm — **le volume d'égalisation croît d'un facteur 5,76** à épaisseur égale, et la fouille s'élargit d'autant au droit des soubassements existants. C'est un point de **mode d'exécution**, pas de calcul.

**Conséquence sur les plans (D-09 ④).** Un plan portant la seule cote « −1,00 m » reste **incomplet** : il laisse croire à une cote fixe. B-60 doit porter « **−1,00 m / TN mini** », la règle d'approfondissement et l'ENC intégrale.

**Nappe et tassements — ce qui change à l'indice F.** La nappe est **déclarée absente** (D-16) : le risque d'épuisement, de blindage hydraulique et de délavage sous les soubassements, qui motivait V-R3, **sort du dossier**. Les **tassements sont hors mission** (D-15) : ils ne sont pas vérifiés par nos soins et la note de calcul doit le porter explicitement. Le risque de **tassement différentiel** entre l'assise neuve et l'existant, signalé au § 5.2 du RDR, n'est donc **pas** couvert par un calcul — il est traité par la règle de nivellement de D-09, qui impose de ne pas laisser une fondation au-dessus de l'autre. C'est une réponse constructive, pas une vérification : la différence doit être dite.

## 5. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-02) | État | Observation |
|---|---|---|
| Chaque ligne a une source citée ou est marquée VERROU | ✅ | **40** lignes sourcées (fichier + page + indice) ; **27** VERROU ; **2** NON NÉCESSAIRE |
| Aucun champ renseigné sans niveau de fiabilité | ✅ | Contractuelle / Décision / À confirmer sur chaque ligne |
| Les VERROU sont en fin de fiche avec voie d'obtention | ✅ | Tableau 2, deux sous-ensembles, voie et responsable par ligne |
| Aucune contradiction tranchée silencieusement | ✅ | 4 conflits listés en VERROU ; le 5e (SOL-03) est **tranché par décision D-08**, tracé en Section 1 du RDR |
| Aucune variable non lue par une brique n'est présente | ✅ | Les 31 variables sans consommateur sont exclues ; DOC-09 exclue (B-48 sans objet) |

**Placeholders résiduels (V7)** : aucun.
**Valeurs de repli ou « pratique courante »** : aucune. Toutes les valeurs proviennent d'une pièce citée ou d'une décision datée.

---

## 6. POINT DE CONTRÔLE HUMAIN

**Sur les trois décisions du 19/10/2026 :**

1. **D-14 (60 × 60 minimum)** — enregistrée. Confirmez-vous que 60 × 60 est bien une **dimension plancher** (augmentable par le calcul, jamais réductible), et non la dimension définitive de toutes les semelles ?
2. **R-36** — l'encastrement de 50 cm ne peut plus être justifié par h/B = 2 avec une semelle de 60 cm. Retenez-vous d'**approfondir** l'assise, ou de **maintenir −1,00 m** en justifiant la portance par la seule qualité du sol d'assise ? *(Le BET doit trancher ; je ne le fais pas à sa place.)*
3. **D-15 (tassements hors mission)** — la note de calcul portera explicitement qu'aucun tassement n'est vérifié. Cette mention suffit-elle, ou souhaitez-vous une exclusion formalisée au marché ?
4. **D-16 (absence de nappe)** — enregistrée comme **déclaration client**. Une venue d'eau en fouille devient un point d'arrêt. Confirmez-vous ce régime ?

**Sur les valeurs :**

5. Le tableau 1 passe à **40 valeurs**, le tableau 2 à **27 VERROU**, et **SOL-07** est exclue comme NON NÉCESSAIRE (motif de périmètre : D-15). Cette exclusion est-elle validée ?
6. Les autres valeurs (39 lignes antérieures) sont-elles inchangées à votre sens ?

---

*Brique B-02, **indice F**, livrée. Aucune brique aval engagée.*

> **Note de révision** : **indice F** = intégration de **D-14** (dimension minimale de fondation **60 × 60 cm**), **D-15** (tassements hors mission) et **D-16** (absence de nappe). **ENC révisée en version 3** (douze alinéas), **SOL-03 / SOL-06 / SOL-07** mises à jour, **R-36** ouverte sur la justification de l'encastrement (h/B passe de 2 à 0,83 avec une semelle de 60 cm).

> *Indice E : D-10, D-11, D-12 ; ENC v2 ; R-32/R-33/R-34 fermées.*
> *Indice D : décision D-09 — référence terrain naturel, prescription ENC créée.*
> *Indice C : décision D-08 — encastrement à −1,00 m, SOL-03 entrée au tableau 1.*
> *Indice B : décision D-06 — enrobage 50 / 30 mm.*