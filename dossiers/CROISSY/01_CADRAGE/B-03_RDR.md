# B-03 — REGISTRE DES DÉCISIONS ET RÉSERVES (RDR)

## En-tête de traçabilité

| Champ | Valeur |
|---|---|
| **Code projet `ID-01`** | `CROISSY-FLORA` |
| **Intitulé `ID-02`** | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| **Indice du dossier en vigueur `ID-05`** | ⚠ **NON UNIFIÉ — voir R-01.** Trois indicages coexistent : **D1 « V1 »** (13/03/2026) · **D2 « C »** (16/03/2026) · **D4 « C »** (13/03/2026) |
| **Date de l'étude `ID-07`** | **19/10/2026** |
| Carnet | CARNAC v2.6 |
| Brique | **B-03** — Registre des Décisions et Réserves |
| Phase | 0 — Cadrage *(puis mis à jour à chaque décision, réserve ou verrou)* |
| **Indice du livrable** | **P** (remplace l'indice O du 19/10/2026 — mise à jour 20/10/2026) |
| Brique suivante | B-04 (PTD) — non engagée |

> **Indice P (20/10/2026)** : **D-25 adoptée** — validation des **Articles méthodologiques P1 à P8 (« Synthèse structurelle du dossier »)** et révision coordonnée des trois briques graphiques :
> - **B-32 révisée en Indice D** : purge intégrale des cloisons et complexes d'isolation (`020_cloi`, `020_cloisons` = `0 entité`), filtrage des portes et cotes de cloisons ;
> - **B-20 révisée en Indice B** (mode **PARTIEL-DÉCLARÉ**) : inscription vectorielle exacte `D2 ↔ D5` au `1/80` (**résidu médian `21,0 mm`**, levant l'ancienne limite D5↔D2), implantation complète de **tous** les ouvrages neufs EVEN (`F1a/b/c, F2, F3, F4, R1, R2-N/S, R3-N/S, Stab1, P1-N/S, P2, P3, J1, S1, S2, SF1, Bêche, RSO passerelle, Charpente`) sur 3 planches + 2 coupes `A-A` et `B-B`, et rectificatifs factuels (`S275` fourni en D2 p. 1, `2×P1`, sommiers `S1/S2`, sondages Planchers A & B dans D3 p. 10) ;
> - **B-40 révisée en Indice E** : implantation complète « PLS » sur vue nettoyée sans cloisons, justification attachée à **D-24** (**R-36 close**), et matérialisation graphique des **nuages `D-19`** sur plans.
>
> *Indice O : **D-22**, **D-23**, **D-24** adoptées ; **R-64 fermée par D-23** et **R-36 arbitrée par D-24**.*
>
> *Indice N : **R-64** ouverte par **B-31** — le R+1 n'est pas à l'aplomb du RDC (**10,1 cm** d'écart d'enveloppe, **22 cm** d'écart médian mur à mur, 27 % des murs du R+1 non portés). Convention de calage à trancher avant B-60. **B-40 livrée en PARTIEL-DÉCLARÉ** : semelle 60 × 60 = **108 kN ELS / 176 kN ELU**, couvre **11,3 m²** ; **R-36 relancée** (h/B = 0,83 au lieu de 2).
> *Indice M : **D-21** — le niveau du RDC existant est **0,00 RELATIF** ; la cote exacte, à réception, sera notifiée par « **0,00 RELATIF = cote reçue** ». L'ambiguïté 201,03 / 201,23 m **disparaît du chemin critique**. **B-30 corrigée en indice C** : surfaces reconstruites sur **D4 + D5 concordants** — **RDC 111,15 m²** / **R+1 106,92 m²**.
> *Indice L : **D-20** — **niveau 0,00 = plancher bas du RDC existant**. Effet : l'axe Z de B-30 dispose enfin d'une origine, mais **D-09 référençait l'arase au terrain naturel** — l'écart entre les deux repères n'est mesuré nulle part (**H-25 proposée**). **B-30 corrigée en indice B** : surface du R+1 **6,03 → 101,79 m²**, altimétrie de D5 **avérée** (11 cotes Z), témoin de calage refondu. **D5_Inventaire erraté**.
> *Indice K : **24 hypothèses validées** le 19/10/2026 (annexe `B-03_Annexe_Hypotheses.md`, ind. B). **H-21 rectifiée** : déplombage, curage et démolition **hors mission** → reclassée **C3**. **H-22, H-23 et H-24 ajoutées** (coupe, XA, classe de sol). **R-39 à R-60 retirées définitivement** de la file d'inscription. **B-40 débloquée** en mode « hypothèse notifiée ». **B-30 engagée**.
> *Indice J : **D-19** — **régime d'hypothèses notifiées**. Le donneur d'ordre autorise formellement la production sous hypothèses, **notifiées par nuage** sur les plans et notes de calcul, avec **délai de contradiction de deux jours** à peine d'exonération. Les **22 propositions de réserves R-39 à R-60 sont retirées** de la file d'inscription et converties en **21 hypothèses H-01 à H-21** (annexe `B-03_Annexe_Hypotheses.md`). **Seules R-61 à R-63 subsistent** comme propositions. Aucune réserve n'est fermée : le mécanisme n'agit qu'après notification et expiration du délai.
> *Indice I : **D-18** — le rapport géotechnique **existe** (réf. **GEOFLORAV2**), intransférable ; les hypothèses de sol en sont extraites. **R-38 ouverte** (double référence). **B-12 révisée en indice B**, **B-13 livrée**.
> *Indice H : **D-17** — il n'existe **aucun DXF de coffrage** ; **c'est à nous de le produire**. **R-37 fermée**. **B-60 et B-62 ne sont plus suspendues** : elles deviennent exécutables, séquencées après B-40 à B-50. **B-12 livrée**. PTD révisé en indice C.
> *Indice G : intègre la **pièce D5** — DXF indice C**, retrouvée dans le Drive le 19/10/2026 et inventoriée par script (`ezdxf` 1.4.5). **R-24 fermée**, **GEO-06 fermé**, **V-18 réduit**, **R-37 ouverte** (absence de contenu structurel). B-04 (PTD) révisée en indice B.
> *Indice F : intègre **D-14** (dimension minimale de fondation **60 × 60 cm**), **D-15** (tassements **hors mission**) et **D-16** (**absence de nappe phréatique**). Conséquences : **R-13 réduite** à la seule coupe type, **V-12 réduit**, **V-R3 annulée** (V-R4), **R-36 ouverte** sur la justification de l'encastrement. FDC révisée en **indice F**.
> *Indice E : validation des quatre points du point de contrôle de l'indice D — D-13 ; R-35 fermée.*
> **Indice E (détail)** : intègre la validation du 19/10/2026 des quatre points du point de contrôle de l'indice D — **D-13** : procédure de dépassement des 18,75 kN, lecture « PLS », alinéa 6 de l'ENC, **point d'arrêt de réception du fond de fouille retenu** (R-35 fermée). **PTD annexé** (§ Annexe).
> *Indice D : réponses aux trois questions laissées ouvertes à l'indice C — D-10, D-11, D-12 ; R-32, R-33 et R-34 fermées ; V-27 fermé.*
> **Indice D (détail)** : intègre les réponses du 19/10/2026 aux trois questions laissées ouvertes à l'indice C — **D-10** (semelle **isolée** 25 × 25), **D-11** (terme « PLS »), **D-12** (**D-09 = plancher, pas plafond**). Conséquences : **R-32, R-33 et R-34 fermées**, **V-27 fermé**, FDC révisée en **indice E**. **Comptage des réserves corrigé** (36 et non 37).
> *Indice C : décision D-09 — référence terrain naturel, prescription ENC, R-30/R-31 et V-24/V-25 fermés.*
> *Indice B : décision D-08 — encastrement des fondations, R-05 et V-03 fermés.*

> **Nature du document** : le RDR n'est pas un document administratif, c'est l'instrument de défense du projet. Il prouve trois choses en cas de litige : les décisions ont été prises par qui de droit (Section 1), les données manquantes ont été demandées dans les délais (Section 2), et tout ce qui était faisable a été exécuté malgré les blocages (Section 3).

---

## SECTION 1 — DÉCISIONS

> **Règle appliquée** : une décision sans auteur et sans date n'existe pas. **Aucune ligne ci-dessous n'est une décision du rédacteur** — toutes émanent du client, identifié comme **« Client »**, dans les échanges du 19/10/2026.

| N° | Date | Objet | Décision | Auteur | Effet sur les briques |
|---|---|---|---|---|---|
| **D-01** | 19/10/2026 | Référentiel géotechnique | Les hypothèses de référence sont celles d'une mission **G2 AVP GEOEXPERTS** (rapport n° 25.13646/ES/GIF du 22/01/2026) | Client | **Ferme V-01** : DOC-06 de BLOQUANTE à PARTIELLE. **B-12** engagée en PARTIEL-DÉCLARÉ |
| **D-02** | 19/10/2026 | Contrainte admissible ELS | **q<sub>ELS</sub> < 0,30 MPa** | Client | SOL-01 → **FOURNIE**. B-40 et B-43 débloquées sur l'ELS |
| **D-03** | 19/10/2026 | Contrainte admissible ELU | **q<sub>ELU</sub> < 0,49 MPa** | Client | **Ferme V-02** (SOL-02). B-40 dispose d'ELS **et** d'ELU |
| **D-04** | 19/10/2026 | Type de fondation | **Fondations superficielles** ; ancrage initialement déclaré à **40 cm** dans les alluvions anciennes | Client | B-41 proposée SANS OBJET. ⚠ **Modifiée par D-08 sur le seul point de l'ancrage** — la valeur 40 cm est **supersédée**, la décision reste au registre pour traçabilité |
| **D-05** | 19/10/2026 | Validation de la MPD indice B | **Validation globale** de la MPD, y compris les 3 SANS OBJET (B-41, B-47, B-48) et le NON NÉCESSAIRE DOC-09 | Client | Désactive B-41, B-47, B-48. Active B-20 à B-50 selon §1 de la MPD *(validation globale, non ligne par ligne — R-02)* |
| **D-06** | 19/10/2026 | Enrobage des armatures | **c<sub>nom</sub> = 50 mm pour les fondations** · **c<sub>nom</sub> = 30 mm pour les autres structures** | Client | MAT-03 scindée en MAT-03a et MAT-03b. **Ouvre V-04** (Δc<sub>dev</sub> et XC4) |
| **D-07** | 19/10/2026 | Validation de la FDC indice B | **Validation** de la FDC, annexée au présent RDR | Client | Les 38 valeurs du tableau 1 deviennent opposables à leur niveau de fiabilité |
| **D-08** | 19/10/2026 | **Encastrement des fondations** | **L'arase inférieure des fondations est fixée à −1,00 m**, afin de respecter **50 cm d'encastrement dans le bon sol** (alluvions anciennes) | Client | **Ferme R-05 et V-03.** SOL-03 → **FOURNIE**. Le toit des alluvions se déduit à **−0,50 m**. **Ouvre R-30, R-31, R-32 et V-24, V-25.** **Relève la criticité de R-13** (nappe). FDC révisée en indice C |
| **D-09** | 19/10/2026 | **Référence altimétrique et égalisation avec l'existant** | ① L'arase inférieure des fondations est à **−1,00 m par rapport au TERRAIN NATUREL**. ② **En plan, l'entreprise doit systématiquement vérifier que les nouvelles fondations sont au même niveau que les fondations existantes.** ③ **Dans le cas contraire, elle ajoute du gros béton pour atteindre le même niveau.** ④ **Cette note doit figurer sur les plans et sur la note de calcul.** | Client | **Ferme R-30** (référence = TN) et **R-31** (méthode d'interface prescrite). **Ferme V-24 et V-25.** **Crée la prescription ENC** (§ 0sexies de la FDC), à reporter sur **B-60 (plans)** et **B-40 (note de calcul)**. **Ouvre R-33, R-34, R-35 et V-26, V-27.** FDC révisée en indice D |
| **D-10** | 19/10/2026 | **Géométrie de la semelle « 25×25 »** | **Semelle isolée** de **25 × 25 cm en plan** — et non semelle filante de section 25 × 25 | Client | **Ferme R-32.** Surface d'assise = **625 cm² par semelle**. **Condition de validité** : charge ELS ≤ **18,75 kN** par semelle à q<sub>ELS</sub> = 0,30 MPa, vérifiée par descente de charges en **B-40**. FDC révisée en indice E |
| **D-11** | 19/10/2026 | **Terminologie « EN PLS »** | Le terme **« PLS » est maintenu tel quel** ; il désigne le **plan de fondations**, celui qui doit porter la prescription ENC | Client | **Ferme R-33.** Le sigle n'est développé dans **aucune pièce dépouillée** (0 occurrence dans la couche texte de D2 et D4, recherche du 19/10/2026). **B-60** doit porter « PLS » en titre du plan de fondations, sinon le renvoi de D-09 ④ ne désigne rien |
| **D-12** | 19/10/2026 | **Lecture de D-09** | **D-09 est un plancher, pas un plafond** : l'arase à −1,00 m / TN est un **minimum**, jamais une cote fixe. Le nivellement ne s'obtient **jamais par remontée** ; il s'obtient par **approfondissement** et gros béton. La fondation neuve peut être plus basse que l'existante, jamais plus haute | Client | **Ferme R-34 et V-27.** Précise D-09 sans la modifier. **Prescription ENC révisée en version 2** (§ 0sexies de la FDC, dix alinéas). **B-60** : « −1,00 m / TN **mini** » + règle d'approfondissement. FDC révisée en indice E |
| **D-13** | 19/10/2026 | **Validation du point de contrôle de l'indice D** | **OUI sur les quatre points** : ① tout dépassement des **18,75 kN** par semelle en B-40 revient devant le client comme **décision de géométrie** ; ② la lecture **« PLS = plan de fondations »** est confirmée, à inscrire en titre de **B-60** ; ③ l'**alinéa 6** de l'ENC (« jamais de remontée ») est conforme ; ④ le **point d'arrêt de réception contradictoire du fond de fouille** est **retenu** | Client | **Ferme R-35.** Confirme D-10, D-11 et D-12 sans les modifier. **Aucune valeur de la FDC ne change** — pas de nouvel indice de B-02. **B-04 (PTD) engagée** |
| **D-14** | 19/10/2026 | **Dimension minimale des fondations** | **La dimension minimale d'une fondation est de 60 × 60 cm.** La semelle isolée de D-10 passe de 25 × 25 à **60 × 60 cm minimum** | Client | Surface d'assise **3 600 cm²** → **108 kN** à l'ELS, **176 kN** à l'ELU. **Lève l'objection des 18,75 kN.** **Ouvre R-36** : avec B = 60 cm, h/B = **0,83** et non plus 2 — l'argument de justification de D-08 tombe. FDC révisée en indice F |
| **D-15** | 19/10/2026 | **Tassements — hors mission** | **Aucune information sur le tassement. C'est hors mission, à la charge du géotechnicien** | Client | **SOL-07 → NON NÉCESSAIRE** (motif de périmètre). **Réduit V-12** et **R-13**. B-40 doit porter la **mention explicite** qu'aucun tassement n'est vérifié — ni absolu, ni différentiel |
| **D-16** | 19/10/2026 | **Hydrogéologie** | **Absence de nappe phréatique** sur le site | Client | **SOL-06 → FOURNIE.** **Annule V-R3** (V-R4) — le risque d'épuisement, de blindage et de délavage sort du dossier. Toute venue d'eau contraire devient **point d'arrêt** (ENC alinéa 8). FDC révisée en indice F |
| **D-17** | 19/10/2026 | **Production du DXF de coffrage** | **Il n'existe aucun DXF de coffrage. C'est à nous de le produire** | Client | **Ferme R-37.** **B-60 et B-62 quittent la liste des briques suspendues** : elles deviennent **exécutables**, séquencées après B-40 à B-50. La production du DXF de coffrage est **intégrée à notre mission** — c'est une extension de périmètre, tracée. PTD révisé en indice C |
| **D-18** | 19/10/2026 | **Source des hypothèses géotechniques** | **Le rapport géotechnique existe et porte la référence GEOFLORAV2.** Il est **trop lourd pour être transféré** dans l'espace de travail. **Les hypothèses relatives au sol fournies proviennent de ce document** | Client | **DOC-06 reste PARTIELLE**, mais sa source est nommée. SOL-01 et SOL-02 passent de « déclaration sans source » à « **citation déclarée d'un document identifié** ». **Ouvre R-38** : deux références coexistent (GEOFLORAV2 et 25.13646/ES/GIF) sans lien établi. B-12 révisée en indice B |
| **D-20** | 19/10/2026 | **Origine altimétrique du projet** | **Le niveau du plancher bas du RDC existant est retenu comme le niveau 0,00.** | Client | **Donne une origine à l'axe Z** de B-30, jusqu'ici conventionnel. **Ne remplace pas D-09** : celle-ci référence l'arase au **terrain naturel**. L'écart entre plancher bas et TN **n'est mesuré nulle part** → **H-25 proposée**. **Laisse une question non tranchée** : D5 porte deux cotes pour ce plancher, **201,03 m** et **201,23 m** (écart 20 cm, brut / fini) |
| **D-21** | 19/10/2026 | **Régime de la cote de niveau** | **Le niveau du RDC existant est le 0,00 RELATIF.** Une fois la cote exacte reçue, elle sera **notifiée** en écrivant : **« 0,00 RELATIF = [cote exacte reçue] »**. | Client | **Supprime le choix 201,03 / 201,23 m** du chemin critique : les plans portent **0,00 RELATIF** jusqu'à réception. **Impose une traçabilité de la cote** (document, date, auteur) faute de quoi la substitution serait sans source. **Ne règle pas** l'écart avec le **terrain naturel** de D-09 → **H-25 reproposée** (objet restreint : écart TN ↔ plancher bas), en attente de validation. **B-30 révisée en indice C** |
| **D-19** | 19/10/2026 | **Régime d'hypothèses notifiées** | ① **Le donneur d'ordre a demandé officiellement, dans le compte rendu, que nous prenions des hypothèses.** ② **Ces hypothèses sont clairement notifiées par un nuage sur nos plans et notes de calcul.** ③ **Les autres intervenants sont dans l'obligation de les confirmer ou de les rectifier dans un délai de deux jours.** ④ **À défaut, nous sommes exonérés de toute responsabilité.** | Client *(via compte rendu)* | **Change le régime des réserves :** une hypothèse notifiée n'est plus une réserve à lever, c'est une valeur opposable par silence. **R-39 à R-60 retirées** de la file d'inscription et converties en **H-01 à H-21**. **Débloque B-40** sur les points couverts par une hypothèse. **Crée trois obligations pour nous** : matérialisation du nuage, preuve de transmission datée, tenue d'un registre des délais. Annexe : `B-03_Annexe_Hypotheses.md` |
| **D-22** | 19/10/2026 | **Production de B-20 avant diffusion de B-40** | **B-20 est produite et livrée avant toute diffusion de B-40.** La conception de principe précède la note d'exécution | Client | **B-20 livrée indice A** en mode **INTERNE-GO**. **Débloque la diffusion de B-40** sous les réserves portées par B-20 |
| **D-23** | 19/10/2026 | **Convention de calage entre niveaux** | **Translation rigide du R+1 sur le RDC.** Aucune correction d'aplomb n'est appliquée ; l'écart mesuré par B-31 est porté comme **donnée de projet**, pas corrigé | Client | **Ferme R-64.** L'écart d'enveloppe **10,1 cm** et l'écart médian mur à mur **22 cm** restent des **faits à porter en B-60** (27 % des murs du R+1 non portés) |
| **D-24** | 19/10/2026 | **Profondeur d'assise des fondations** | **−1,00 m / TN est maintenu.** L'assise n'est **pas approfondie** ; la portance est réputée suffisante au vu de la nature du sol (alluvions anciennes, H-22) | Client | **Arbitre R-36** : l'argument h/B = 2 est abandonné. La justification de portance **reste à produire** par note — reportée en **B-40 indice suivant** |
| **D-25** | 20/10/2026 | **Synthèse structurelle du dossier (Articles P1 à P8) & refonte graphique sans cloisons/isolation** | Validation par **« GO »** du 20/10/2026 : ① adoption des **Articles P1 à P8** (corpus indissociable D1–D5, synthèse EXISTANT/PROJET, interdiction de déclarer un élément non localisable sans épuisement de toutes les pièces) ; ② suppression intégrale des cloisons et isolants sur **tous** les plans (**B-32 Ind. D**) ; ③ implantation de tous les ouvrages neufs métalliques, BA, charpente et fondations (**B-20 Ind. B** et **B-40 Ind. E**) avec **nuages D-19** | Client | **Lève la pseudo-limite D5↔D2** (calage `1/80` à `21,0 mm`). **Ferme techniquement R-36** en B-40 Ind. E. Livre 6 planches propres sans cloisons ni isolation |

### 1.0bis Articles méthodologiques ajoutés au référentiel projet (`P1` à `P8` — Décision `D-25` du 20/10/2026)

| Article | Intitulé | Règle opposable pour toute la suite de l'affaire |
|---|---|---|
| **P1** | **Un seul corpus** | Le dossier du marché (`D1 + D2 + D3 + D4 + D5`) forme un **tout indissociable**. La hiérarchie des pièces arbitre une contradiction ; elle n'autorise jamais à ignorer une pièce. |
| **P2** | **Planche de synthèse** | Tout plan de principe / d'implantation projette sur **un fond structurel pur** (sans cloisons ni isolation) l'existant conservé, les démolitions et **tous** les ouvrages neufs du dossier. |
| **P3** | **Écart `EXISTANT → PROJET`** | Chaque ouvrage neuf est rattaché à un écart architectural (`102_demol`) ou à un désordre diagnostiqué (`D3`). |
| **P4** | **Procédure `INTERNE-GO`** | En l'absence de BET de conception sur un futur projet : ① comparaison AVANT/APRÈS → ② dérivation des porteurs → ③ prédimensionnement → ④ vérification de l'existant → ⑤ déclaration explicite des limites d'estimation. |
| **P5** | **Limite déclarée ≠ arrêt** | Lorsqu'une donnée relève d'un sondage ou d'une reconnaissance en fouille, la brique **livre** en matérialisant un **nuage `D-19`** sur le plan. |
| **P6** | **Épuisement du dossier** | Toute déclaration d'absence énumère au préalable chaque pièce consultée et son contenu effectif. |
| **P7** | **Vérité du titre** | Un plan intitulé *« principe structurel »* ou *« fondations »* doit effectivement porter les éléments structurels et leur implantation. |
| **P8** | **Frontière de responsabilité** | En l'absence de BET de conception amont, l'extension de responsabilité de conception doit être formalisée par écrit dans la commande. |

### 1.0ter Registre des Nuages `D-19` matérialisés sur les plans (`B-20 Ind. B` & `B-40 Ind. E`)

| Code nuage | Planche(s) | Objet notifié (confirmation/rectification sous 2 jours ouvrés — D-19) |
|---|---|---|
| **`Z-P1N` / `Z-P1S`** | `B-20 Planche 2` · `B-40 Ind. E` | Pieds des 2 poteaux `P1` (`tube 140×140 S275`) en façade Ouest Sud : appui sur soubassement moellons vérifié en fouille (`D2 f.03`), sinon création de semelles `60×60×30 BA` (`D-14`) + gros béton (`D-09`) |
| **`Z-P3`** | `B-20 Planche 2` · `B-40 Ind. E` | Pied du poteau `P3 (50×40 BA)` : reconnaissance du soubassement du refend Nord du hall à l'ouverture de fouille + rattrapage gros béton `C16/20` (`D-09`) |
| **`Z-J1`** | `B-20 Planche 2` · `B-40 Ind. E` | Pied du jambage `J1 (24×50 BA)` : reconnaissance du soubassement du refend central moellons `50 cm` (`D-09`) |
| **`PH-HALL`** | `B-20 Planche 1` | Zone centrale *« Plancher haut non sondé »* (`D3 p. 4 & 10`) : sondage destructif contradictoire préalable avant travaux |
| **`CHARP-1 / CHARP-2`** | `B-20 Planche 3` | Deux *« ZONES NON RELEVÉES »* de charpente (`D2 Folio 02`) : relevé contradictoire après dépose des faux-plafonds avant exécution `B-44` |

### 1.1 Effet des décisions D-08 à D-12 — ce qui est tranché, ce qui se déduit

> **Mise à jour indice D** : les quatre points soumis au client sont **tous tranchés** — R-30 et R-31 par **D-09**, la géométrie par **D-10**, la lecture de D-09 par **D-12**. Le tableau conserve la trace de l'évolution depuis l'indice B.

**Tranché par la décision :**

| Élément | Valeur | Nature |
|---|---|---|
| Arase inférieure des fondations | **−1,00 m** | Décision client |
| Encastrement dans le bon sol | **0,50 m** | Décision client |
| Toit des alluvions anciennes | **−0,50 m** | **Déduit** de la décision (et non lu au rapport) |

**Ce qui reste ouvert — et ne doit pas être lu comme tranché :**

| Point | Statut | Renvoi |
|---|---|---|
| ~~Référence altimétrique du −1,00 m~~ | ✅ **TRANCHÉ par D-09** — terrain naturel | ~~R-30~~ |
| ~~Interaction fondations neuves / semelles existantes~~ | ✅ **TRANCHÉ par D-09** — égalisation par gros béton C16/20 | ~~R-31~~ → **R-31bis** (relevé sur site) |
| ~~**Géométrie exacte de la semelle « 25×25 »**~~ | ✅ **TRANCHÉ par D-10** — semelle **isolée** 25 × 25 cm | ~~R-32~~ |

### 1.2 Points non décidés — récapitulatif

| Point | Statut réel |
|---|---|
| **Δc<sub>dev</sub>** (écart d'exécution) | **NON DÉCIDÉ** → **R-03** |
| **Éléments classés XC4** | **NON DÉCIDÉ** → **R-04** |
| **Surcharge d'exploitation 250 ou 150 daN/m²** | **NON DÉCIDÉ** → **R-06** |
| **Catégorie d'usage de la salle de sport** | **NON DÉCIDÉ** → **R-07** |
| ~~Référence du −1,00 m~~ | ✅ **TRANCHÉ par D-09** — terrain naturel |
| ~~Traitement de l'interface avec l'existant~~ | ✅ **TRANCHÉ par D-09** — égalisation par gros béton |
| ~~Géométrie de la semelle 25×25~~ | ✅ **TRANCHÉ par D-10** — semelle isolée 25 × 25 en plan |
| ~~Terminologie « EN PLS »~~ | ✅ **TRANCHÉ par D-11** — sigle maintenu, = plan de fondations (B-60) |
| ~~Conciliation D-08 / D-09 sur les niveaux~~ | ✅ **TRANCHÉ par D-12** — D-09 = plancher |
| ~~Point d'arrêt de réception du fond de fouille~~ | ✅ **TRANCHÉ par D-13** — point d'arrêt retenu, à formaliser (PA/PC) |

---

## SECTION 2 — RÉSERVES

> **Règle appliquée** : une réserve ne se ferme que par une **entrée en FDC** ou une **décision en Section 1**. Aucune fermeture orale.
> **Échéances** : exprimées en **jalons de production** — la fixation de dates calendaires relève de la MOE.
> **Criticité** : ajoutée à l'indice B pour distinguer ce qui bloque un calcul de ce qui bloque le chantier.

| N° | Objet | Statut | Criticité | Responsable | Date de demande | Échéance (jalon) |
|---|---|---|---|---|---|---|
| **R-01** | Indice du dossier unifié | Ouverte | Contractuelle | **MOE** (TRUELLE) | 19/10/2026 | Avant B-60 |
| **R-02** | Validation ligne par ligne de la MPD | Ouverte | Documentaire | **Client** | 19/10/2026 | Avant B-04 |
| **R-03** | **Δc<sub>dev</sub>** — 5 mm avec système qualité, ou 35 mm d'enrobage | Ouverte | **Calcul** | **Client / BET** | 19/10/2026 | Avant B-42, B-46 |
| **R-04** | **Éléments en XC4** — nommer, ou retirer la classe | Ouverte | **Calcul** | **Client / BET** | 19/10/2026 | Avant B-42, B-46 |
| ~~**R-05**~~ | ~~Ancrage des fondations — 40 vs 50 cm~~ | **FERMÉE** | — | BET / MOE | 19/10/2026 | **Fermée par D-08** (50 cm) |
| **R-06** | Surcharge d'exploitation — 250 vs 150 daN/m² | Ouverte | **Calcul** | **MOE / MOA** | 19/10/2026 | Avant B-21 |
| **R-07** | Catégorie d'usage — salle de sport 34,25 m² et plateau technique 33,14 m² | Ouverte | **Calcul** | **MOE** | 19/10/2026 | Avant B-21 |
| **R-08** | Poids propres de plancher vs recharge 15 cm | Ouverte | **Calcul** | **MOE / BET** | 19/10/2026 | Avant B-21 |
| **R-09** | Poids propres de toiture | Ouverte | **Calcul** | **BET / MOE** | 19/10/2026 | Avant B-21, B-44 |
| **R-10** | Cloisons et équipements lourds | Ouverte | **Calcul** | **MOE / BET** | 19/10/2026 | Avant B-21, B-43 |
| **R-11** | Action sismique — a<sub>gr</sub> et classe de sol | Ouverte | **Calcul** | **BET** | 19/10/2026 | Avant B-42, B-46 |
| **R-12** | Sécurité incendie — CF, SF, catégorie | Ouverte | **Calcul** | **MOE / BE incendie** | 19/10/2026 | Avant B-42, B-43, B-49 |
| **R-13** | **Coupe type et toit des alluvions** — *réduite de l'ex-« 3 extraits »* : la **nappe** est soldée par **D-16**, les **tassements** sortent du périmètre par **D-15**. Il ne reste que la coupe géologique | Ouverte | **Calcul** *(criticité ramenée de CHANTIER à CALCUL par D-16)* | **MOE / GEOEXPERTS** | 19/10/2026 | **Avant B-40** |
| **R-14** | Classement XA réel (« XA4 » inexistante) | Ouverte | **Calcul** | **GEOEXPERTS / BET** | 19/10/2026 | Avant B-40, B-43 |
| **R-15** | Contrainte admissible de la maçonnerie | Ouverte | **Calcul** | **BET / laboratoire** | 19/10/2026 | Avant B-23, B-46 |
| **R-16** | Résistance des moellons et du mortier | Ouverte | **Calcul** | **Laboratoire** | 19/10/2026 | Avant B-46, B-49 |
| **R-17** | Classes de maçonnerie neuve (bloc, mortier, type) | Ouverte | **Calcul** | **BET** | 19/10/2026 | Avant B-46 |
| **R-18** | Chaînages existants | Ouverte | **Calcul** | **BET / sondages** | 19/10/2026 | Avant B-46 |
| **R-19** | Fiches de sondage des planchers | Ouverte | **Calcul** | **BET (EVEN)** | 19/10/2026 | Avant B-24 |
| **R-20** | Sections de charpente + 2 zones « non relevées » | Ouverte | **Calcul** | **BET / géomètre** | 19/10/2026 | Avant B-44 |
| **R-21** | Classement des bois de charpente | Ouverte | **Calcul** | **BET bois / contrôle** | 19/10/2026 | Avant B-44, B-50 |
| **R-22** | **Charpente absente du CCTP** | Ouverte | ⚠ **CONTRACTUELLE** | **MOE / économiste** | 19/10/2026 | **Avant consultation** |
| **R-23** | **Maître d'ouvrage divergent** — UNIVI (D1) vs SCI GEMS RC (D4) | Ouverte | ⚠ **CONTRACTUELLE** | **MOE** | 19/10/2026 | **Avant B-64** |
| ~~**R-24**~~ | ~~DXF indice C non fourni~~ | **FERMÉE** | — | MOE | 19/10/2026 | **Fermée le 19/10/2026** — pièce **D5** `208_FLORA_Plans_DCE_IndC.dxf` retrouvée dans le Drive (4 399 016 o, AC1032) et inventoriée par script. **Mais voir R-37** : le fichier ne porte aucune donnée de structure |
| **R-25** | Cote d'ensemble du bâtiment | Ouverte | **Calcul** | **MOE** | 19/10/2026 | Avant B-43, B-44 |
| **R-26** | Classement termites | Ouverte | **Calcul** | **MOE** | 19/10/2026 | Avant B-43 |
| **R-27** | DOE / plans de récolement | Ouverte | **Production** | **MOA** | 19/10/2026 | Avant B-11 |
| **R-28** | Classe de service du bois (MAT-08) | Ouverte | **Calcul** | **Production interne (B-22)** | 19/10/2026 | Avant B-44 |
| **R-29** | Seuils GEO-10, GEO-11, GEO-12 | Ouverte | **Production** | **Client / BET** | 19/10/2026 | Avant B-30 à B-33 |
| ~~**R-30**~~ | ~~Référence altimétrique du −1,00 m~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-09** — référence = **terrain naturel** |
| ~~**R-31**~~ | ~~Interface fondations neuves / existant~~ | **FERMÉE** *(au niveau conception)* | — | Client | 19/10/2026 | **Fermée par D-09** — méthode prescrite : égalisation par gros béton C16/20. Le **relevé sur site** subsiste en **R-31bis / V-26** |
| ~~**R-32**~~ | ~~Géométrie de la semelle « 25×25 »~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-10** — semelle **isolée** 25 × 25 cm en plan. Condition de validité portée en D-10 : charge ELS ≤ 18,75 kN/semelle, vérifiée en B-40 |

| **R-31bis** | **Relevé des niveaux réels des semelles et soubassements existants** — D-09 prescrit l'égalisation, mais le niveau de l'existant n'est connu qu'à l'ouverture des fouilles. Relevé contradictoire obligatoire | Ouverte | ⚠ **CRITIQUE — CHANTIER** | **Entreprise / MOE** | 19/10/2026 | **À chaque ouverture de fouille** |
| ~~**R-33**~~ | ~~Terminologie « EN PLS »~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-11** — sigle maintenu tel quel, désigne le plan de fondations. Le sigle n'étant développé nulle part, **B-60 doit l'inscrire en titre** |
| ~~**R-34**~~ | ~~Conciliation D-08 / D-09 sur les niveaux~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-12** — D-09 = **plancher, pas plafond**. La cote −1,00 m / TN est un minimum ; le nivellement ne s'obtient jamais par remontée |
| ~~**R-36**~~ | ~~Justification de l'encastrement pour une semelle de 60 cm~~ — D-08 justifiait 50 cm d'encastrement par h/B = 2, obtenu avec une semelle de 25 cm. **D-14 porte B à 60 cm : h/B = 0,83** | **ARBITRÉE — fermée par D-24** | **Calcul — justification à produire** | Client | 19/10/2026 | **−1,00 m maintenu, assise non approfondie.** La portance est réputée suffisante au vu du sol (H-22). **La justification écrite reste due** : reportée à B-40 indice suivant, § portance |
| **R-38** | **Double référence du rapport géotechnique** — `GEOFLORAV2` (D-18) et `GEOEXPERTS 25.13646/ES/GIF du 22/01/2026` (D2 p. 1). Le lien n'est **pas établi** ; si ce sont deux documents, deux jeux d'hypothèses de sol coexistent | Ouverte | **Calcul** | **MOE / GEOEXPERTS** | 19/10/2026 | **Avant B-40** |
| ~~**R-37**~~ | ~~Absence de contenu structurel dans D5~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-17** — la production du DXF de coffrage **nous incombe**. Ce n'est plus une réserve, c'est une **tâche de production** (B-60) |
| ~~**R-35**~~ | ~~Point d'arrêt de réception du fond de fouille~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-13** — point d'arrêt retenu. Reste à le **formaliser** (plan de contrôle, PA/PC) : c'est une production, pas une décision |

| ~~**R-64**~~ | ~~**Convention de calage entre niveaux** — B-31 mesure **10,1 cm** d'écart d'enveloppe entre les murs existants du RDC et du R+1, et **22 cm** d'écart médian mur à mur (27 % des murs du R+1 ne sont pas portés). Deux conventions : translation rigide du R+1 sur le RDC, ou calage indépendant niveau par niveau~~ | **FERMÉE** | — | Client | 19/10/2026 | **Fermée par D-23** — translation rigide du R+1 sur le RDC. L'écart de 10,1 cm n'est pas corrigé : il est **porté comme donnée** en B-60 |

**Total : 40 réserves — 29 ouvertes, 11 fermées (R-05, R-24, R-30, R-31, R-32, R-33, R-34, R-35, R-37, R-36, R-64).**

> **Correction de comptage** : l'indice C affichait « 37 réserves — 34 ouvertes ». Le décompte ligne à ligne du registre donne **36 réserves et 33 ouvertes** à cet indice — l'écart d'une unité venait d'un total saisi sans recomptage. Corrigé ici, et signalé au client plutôt que corrigé en silence.

---

## SECTION 3 — REGISTRE DES VERROUS

> **Règle appliquée** : le registre liste **toujours ce qui a été fait malgré tout**. C'est la pièce qui établit, en cas de reproche sur un délai, que le retard est imputable à l'obtention d'une donnée et non à la production.

### 3.1 Verrous ouverts

| N° | Donnée (code) | Brique suspendue | Date | Responsable | Briques exécutées malgré tout | Mode de contournement |
|---|---|---|---|---|---|---|
| **V-04** | **MAT-03b résiduel** — Δc<sub>dev</sub> et XC4 (R-03, R-04) | B-42, B-46 | 19/10/2026 | Client / BET | B-40 avec MAT-03a (50 mm, **décidé et conforme XC2**) ; B-45 | PARTIEL-DÉCLARÉ sur B-40 ; PARAMÉTRIQUE sur B-42, B-46 |
| **V-05** | **MAT-02 / SOL-05** — classe XA (R-14) | B-40, B-42, B-43 | 19/10/2026 | GEOEXPERTS / BET | B-40 en partie courante sur XC2 ; B-45 | PARAMÉTRIQUE |
| **V-06** | **CHG-02** — surcharge 250 vs 150 (R-06) | B-21 | 19/10/2026 | MOE / MOA | B-22, B-23, B-24 | PARAMÉTRIQUE — les deux valeurs en parallèle |
| **V-07** | **CHG-03** — recharge 15 cm (R-08) | B-21 | 19/10/2026 | MOE / BET | B-22 à B-24 | PARAMÉTRIQUE |
| **V-08** | **CHG-04** — poids propres de toiture (R-09) | B-21, B-44 | 19/10/2026 | BET / MOE | B-45, B-49 | PARAMÉTRIQUE |
| **V-09** | **CHG-08** — cloisons et équipements lourds (R-10) | B-21, B-43 | 19/10/2026 | MOE / BET | B-45, B-49 | PARAMÉTRIQUE |
| **V-10** | **CHG-07b** — a<sub>gr</sub> et classe de sol (R-11) | B-42, B-46 | 19/10/2026 | BET | B-40 (non sismique), B-45 | PARAMÉTRIQUE |
| **V-11** | **SEC-01** — coupe-feu (R-12) | B-42, B-43, B-49 | 19/10/2026 | MOE / BE incendie | B-40, B-45 ; **aucun encoffrement dimensionné** | PARAMÉTRIQUE — mention obligatoire : « une protection au feu adéquate doit être prévue » |
| **V-12** | **SOL-04** — nature et succession des couches *(réduit : SOL-06 soldé par D-16, SOL-07 hors périmètre par D-15)* | B-40 | 19/10/2026 | MOE / GEOEXPERTS | B-40 sur la **portance** (ELS + ELU par D-02/D-03) | **PARTIEL-DÉCLARÉ** — la portance ne dépend pas de la coupe au-delà de la confirmation qu'on atteint bien les alluvions |
| **V-13** | **EXI-05, MAT-07** — contrainte de la maçonnerie (R-15, R-16) | B-23, B-46 | 19/10/2026 | BET / laboratoire | B-45, B-49 | PARAMÉTRIQUE |
| **V-14** | **MAT-09, MAT-10, MAT-11** — maçonnerie neuve (R-17) | B-46 | 19/10/2026 | BET | B-40, B-42, B-45 | PARAMÉTRIQUE |
| **V-15** | **MAT-12** — chaînages existants (R-18) | B-46 | 19/10/2026 | BET / sondages | B-45 | PARAMÉTRIQUE |
| **V-16** | **EXI-01g, MAT-06** — sections et classement des bois (R-20, R-21) | B-44, B-50 | 19/10/2026 | BET / géomètre | B-45, B-49, B-40 | PARAMÉTRIQUE |
| **V-17** | **EXI-04** — fiches de sondage (R-19) | B-24 | 19/10/2026 | BET (EVEN) | B-23 exécutable (9 désordres décrits) | PARTIEL-DÉCLARÉ |
| **V-18** | **GEO-07, GEO-08** — transformation et calage *(GEO-06 **soldé** : `$INSUNITS = 5` = cm)* | B-30 à B-33, B-60 | 19/10/2026 | MOE | B-00 à B-29, B-40 à B-50, B-62 | **PARTIEL-DÉCLARÉ** — *réduit le 19/10/2026 par la fourniture de D5* : B-30 à B-33 deviennent exécutables ; le calage D2↔D5 reste à établir |
| **V-19** | **GEO-01** — cote d'ensemble (R-25) | B-43, B-44 | 19/10/2026 | MOE | Relevé graphique sur PDF vectoriel D4 (non contractuel) | PARAMÉTRIQUE |
| **V-20** | **ID-05** — indice du dossier (R-01) | B-03, B-64, B-71 | 19/10/2026 | MOE | Toutes les briques documentaires, avec mention d'indice en cartouche | PARTIEL-DÉCLARÉ |
| **V-21** | **DOC-08** — DOE / récolement (R-27) | B-11 | 19/10/2026 | MOA | B-10, B-12 à B-15 | PARAMÉTRIQUE |
| **V-22** | **SEC-03** — termites (R-26) | B-43 | 19/10/2026 | MOE | B-40, B-45 | PARTIEL-DÉCLARÉ |
| **V-23** | **Périmètre contractuel — charpente hors CCTP** (R-22) | B-44 *(blocage contractuel)* | 19/10/2026 | MOE / économiste | B-44 techniquement exécutable en PARAMÉTRIQUE | PARAMÉTRIQUE + réserve contractuelle |
| ~~**V-24**~~ | ~~Interface fondations neuves / existant~~ | — | 19/10/2026 | Client | — | **FERMÉ par D-09** — méthode d'égalisation prescrite (voir V-26 pour le résiduel) |
| ~~**V-25**~~ | ~~Référence altimétrique du −1,00 m~~ | — | 19/10/2026 | Client | — | **FERMÉ par D-09** — référence = terrain naturel. Le terme de surcharge redevient calculable |

| **V-26** | **Niveau réel des semelles et soubassements existants** (R-31bis) | **B-40 — volet reprise en sous-œuvre** | 19/10/2026 | Entreprise / MOE | Le reste de B-40 (semelle neuve, portance) | **PARTIEL-DÉCLARÉ** — la méthode est prescrite, la donnée (niveau de l'existant) n'existe qu'à l'ouverture des fouilles |
| ~~**V-27**~~ | ~~Conciliation D-08 / D-09 (R-34)~~ | — | 19/10/2026 | Client | — | **FERMÉ par D-12** — lecture tranchée : D-09 = plancher. La règle de nivellement n'est plus paramétrique (voir § 3.2) |

### 3.2 Verrous fermés — traçabilité des fermetures

| N° | Donnée | Fermé le | Fermé par | Motif |
|---|---|---|---|---|
| **V-01** | DOC-06 — rapport géotechnique | 19/10/2026 | **D-01** | Référentiel G2 AVP et valeurs de synthèse fournis. Statut ramené de BLOQUANTE à **PARTIELLE** — les 3 extraits restent en **R-13** |
| **V-02** | SOL-02 — contrainte admissible ELU | 19/10/2026 | **D-03** | Valeur **q<sub>ELU</sub> < 0,49 MPa** entrée en FDC avec source et auteur |
| **V-03** | SOL-03 — ancrage des fondations | 19/10/2026 | **D-08** | Valeur tranchée : **50 cm dans le bon sol, arase inférieure à −1,00 m**. Entrée en FDC (B-02 indice C) |
| **V-24** | Interface fondations neuves / existant | 19/10/2026 | **D-09** | Méthode d'égalisation prescrite : gros béton C16/20 pour atteindre le niveau de la fondation existante |
| **V-25** | Référence altimétrique du −1,00 m | 19/10/2026 | **D-09** | Référence fixée : **terrain naturel** |
| **V-27** | Conciliation D-08 / D-09 (R-34) | 19/10/2026 | **D-12** | Lecture tranchée : **D-09 = plancher, pas plafond**. La cote devient un minimum ; le nivellement ne s'obtient jamais par remontée |
| **V-F1** | B-41 SANS OBJET | 19/10/2026 | **D-04 + D-05** | Fondations superficielles déclarées |
| **V-F2** | B-47 SANS OBJET | 19/10/2026 | **D-05** | Aucun escalier neuf |
| **V-F3** | B-48 SANS OBJET | 19/10/2026 | **D-05** | Aucune prédalle ; DOC-09 NON NÉCESSAIRE |

### 3.3 Requalifications inscrites — verrou V12

> Le verrou V12 autorise **NON BLOQUANTE → BLOQUANTE** et **interdit l'inverse** par décision du modèle.

| N° | Donnée | Requalification | Date | Raison | Effet |
|---|---|---|---|---|---|
| **V-R1** | **SOL-04** — nature et succession des couches | de « B-41 seulement » → **« B-41 + B-40 »** | 19/10/2026 | Le dictionnaire rattache SOL-04 à B-41. Mais avec des fondations **superficielles**, la nature des couches conditionne directement B-40 : c'est elle qui confirme qu'on atteint les alluvions et non des remblais. **Renforcée par D-08** : à −1,00 m, il faut savoir ce qu'on traverse de −0,50 à −1,00 | B-40 suspendue sur ce point |
| **V-R2** | **GEO-01** — emprise cotée | de **FOURNIE** → **VERROU** | 19/10/2026 | Les plans D4 portent des **cotes de détail**, aucune **cote d'ensemble**. La MPD indiquait « FOURNIE » à tort | B-43 et B-44 suspendues |
| **V-R3** | **R-13** — nappe | de « réserve de calcul » → **« réserve critique chantier »** | 19/10/2026 | **D-08 porte la fouille à −1,00 m.** En fond de vallée de la Seine, sur alluvions, une fouille d'un mètre peut atteindre le toit de la nappe | ⚠ **Annulée par V-R4** |
| **V-R4** | **R-13** — nappe | **annulation de V-R3** — retour à une criticité **CALCUL** | 19/10/2026 | **D-16 : absence de nappe phréatique déclarée.** Le risque d'épuisement, de blindage hydraulique et de délavage sous soubassement n'a plus d'objet | **Décision client**, non une décision du rédacteur (V12 : la levée d'une criticité n'est admise que par décision tracée). Résidu : toute venue d'eau en fouille = **point d'arrêt** (ENC al. 8) |

---

## 4. SYNTHÈSE DU REGISTRE

| Section | Nombre | Évolution depuis l'indice A |
|---|---|---|
| **Décisions (D-xx)** | **24** | +3 (D-22, D-23, D-24) |
| **Hypothèses (H-xx)** | **24** — validées, **aucune notifiée** | H-01 à H-24 · 17 C1 · 4 C2 · **3 C3** (H-10, H-11, H-21) |
| **Propositions de réserves restantes** | **3** — R-61, R-62, R-63 | R-39 à R-60 **retirées** par D-19 |
| **Réserves (R-xx)** | **40** dont **29 ouvertes** et **11 fermées** | indice N : +1 ouverte (**R-64**) — *indice I : +1 ouverte (R-38) ; fermées : R-05, R-24, R-30, R-31, R-32, R-33, R-34, R-35, R-37 |
| **Verrous (V-xx)** | **30** dont **21 ouverts** | inchangé en nombre ; **V-18 réduit** de « suspension totale » à PARTIEL-DÉCLARÉ ; 9 fermetures (V-01, V-02, V-03, V-24, V-25, V-27, V-F1, V-F2, V-F3) |
| **Requalifications** | **4** | V-R1, V-R2, **V-R3 (annulée)**, **V-R4 (annulation)** |

**Comptage vérifié le 19/10/2026** — 38 lignes au registre, **9 fermées** (R-05, R-24, R-30, R-31, R-32, R-33, R-34, R-35, R-37), soit **29 ouvertes**. Une valeur de 30 ouvertes avait été annoncée à l'indice G : elle omettait que R-24 venait d'être fermée **après** le décompte. Corrigé ici.

> **Correction de comptage (indice D).** L'indice C affichait **37 réserves / 34 ouvertes** : c'était faux. Le décompte ligne à ligne donnait **36 réserves et 33 ouvertes**. Le total avait été saisi sans recomptage après l'ajout de R-31bis. Corrigé ici. Les verrous, eux, se réconciliaient : 27 numérotés + 3 verrous de fait (V-F1 à V-F3) = **30**, dont 21 ouverts à ce jour.

### 4.1 Ce qui a été exécuté malgré les verrous

**Quatre briques produites à ce jour** alors que 21 verrous sont ouverts : **B-00, B-01, B-02, B-03**. Aucune n'est un livrable de calcul — les quatre sont documentaires. Les verrous mordront sur la production à partir de B-21.

### 4.2 L'effet cumulé de D-08, D-09 et D-12

| Mouvement | Verrous fermés | Verrous ouverts |
|---|---|---|
| **D-08** — encastrement −1,00 m | V-03 (ancrage) | V-24 (interface existant), V-25 (référence de cote) |
| **D-09** — référence TN + égalisation gros béton | V-24, V-25 | V-26 (niveau réel de l'existant), V-27 (conciliation des critères) |
| **D-12** — D-09 = plancher | **V-27** | — *(V-26 reste : c'est un relevé de terrain, pas une décision)* |

**Indice F — l'effet de D-14, D-15 et D-16 sur les verrous** : aucun verrou fermé, un **verrou réduit** (V-12 ne porte plus que sur SOL-04) et une **requalification annulée** (V-R3 → V-R4). Ce n'est pas un recul : c'est le constat que les décisions de l'indice F portent sur la **géométrie et le périmètre**, pas sur des données manquantes — sauf D-16, qui solde SOL-06 et allège le mode d'exécution.

**Bilan net sur les fondations : trois verrous de conception fermés** (l'ancrage, la référence, l'arbitrage des critères), **un seul verrou résiduel**, et il est de chantier : le niveau réel des semelles existantes, qui n'existe qu'à l'ouverture des fouilles.

C'est la signature d'un dossier de fondation arrivé à son terme documentaire. Ce qui reste ne se lève pas par une réunion : cela se lève par une pelle.

**Ce qui reste à B-40 pour être COMPLET** : la **descente de charges** et le contrôle des **18,75 kN** par semelle (condition de validité de D-10), **R-13** (nappe), **R-14** (classement XA), et le relevé **R-31bis / V-26** qui restera partiel par nature. Le point d'arrêt (R-35) est acquis depuis D-13.

---

## 5. OBSERVATIONS D'INGÉNIEUR SUR D-08, D-09 ET D-12

### 5.1 La décision est cohérente sur trois plans

**Plan géométrique.** Un encastrement de 50 cm pour une semelle de 25 cm de large donne un rapport **h/B = 2**. C'est le rapport qui permet au mécanisme de rupture de se développer entièrement dans la couche portante plutôt que de remonter dans la couche sus-jacente. Le choix est **techniquement fondé**.

**Plan de la cohérence documentaire.** D-08 tranche en faveur de la valeur du **BET** (D2 p. 1 : « ancrées d'au moins 0,5 m ») et non de la déclaration initiale (D-04 : 40 cm). Le DCE n'est donc pas remis en cause sur ce point — c'est la déclaration orale qui s'aligne sur la pièce écrite.

**Plan de la durabilité.** L'assise à −1,00 m place les fondations **hors de la zone de variation saisonnière** et sous la profondeur de gel. C'est favorable pour un ouvrage ancien dont on ne connaît pas le degré de dessiccation des alluvions.

### 5.2 Mais la décision crée un différentiel de profondeur avec l'existant — et c'est un risque réel

Le DCE prescrit de conserver « **le débord de semelle rendu apparent à conserver en l'état** » (D2 folio 03). Une fondation existante en moellons sur alluvions à −0,50 m se trouve donc **50 cm au-dessus** de la nouvelle assise.

Trois conséquences qui appellent une réponse du BET (R-31) :

1. **Effet de fond de fouille.** Creuser à −1,00 m au droit d'un soubassement qui n'est enterré que de 0,50 m met à nu la base de ce soubassement. C'est exactement le mécanisme de déstabilisation que la nota du DCE cherchait à prévenir (« au risque de déstabiliser les fondations »).
2. **Réaction asymétrique.** Une semelle neuve 50 cm plus bas que l'ancienne ne se comporte pas mécaniquement comme l'ancienne : les tassements absolus diffèrent, et le bâti ancien est sensible au **tassement différentiel**, pas au tassement absolu.
3. **Continuité.** La « reprise en sous-œuvre par passes alternées de gros béton » (D2 folio 04) répond précisément à ce cas — mais elle est dessinée sur le folio de la **passerelle**, pas sur celui du pavillon. Il faut la **transposer explicitement** au Flora.

### 5.3 La nappe devient le premier risque du chantier — pas un point de calcul

Croissy-sur-Seine se situe en fond de vallée de la Seine, sur **alluvions**. Avec une assise portée à **−1,00 m**, la fouille approche la zone où la nappe peut apparaître, notamment en période de hautes eaux.

Cela change la nature de R-13 : ce n'était qu'un extrait de rapport à demander pour vérifier un tassement ; c'est désormais une donnée de **mode d'exécution** — épuisement, blindage, risque de délavage des alluvions sous le soubassement existant. Le coût d'un arrêt de chantier pour nappe non anticipée n'a rien à voir avec celui d'une reprise de note de calcul.

**R-13 est relevée en criticité « chantier »**, et V-R3 est inscrite au registre.

### 5.4 Une cote sans référence n'est pas une cote

La décision dit « arase inférieure à −1,00 m ». Par rapport à quoi ?

| Référence possible | Conséquence |
|---|---|
| **Terrain naturel actuel** | La cote varie le long du bâtiment : D4 montre des décaissements de 6 cm, des recharges de 15 cm, des pentes à 10 % et des « sols à recharger » — le TN n'est pas une surface plane |
| **Niveau fini de dallage** | Il n'est pas coté (NIV-05 non fourni) et le projet le **modifie** (« bêche pour réhausse niveau dallage ») |
| **Cote Z absolue** | Les plans donnent Z = 201,03 à 201,26 au RDC. Une cote absolue serait non ambiguë — mais elle n'a pas été exprimée ainsi |

Tant que la référence n'est pas fixée, B-40 peut calculer une **capacité portante** correcte (elle ne dépend que de la largeur et des caractéristiques du sol), mais **pas le terme de surcharge lié à l'encastrement**. La note portera donc la cote en symbole et un filigrane **PROVISOIRE**. C'est V-25.

### 5.5 La semelle est isolée et mesure 60 × 60 minimum — l'ordre de grandeur a changé deux fois

Le folio 03 mentionne « **semelle BA 25×25** » sans préciser la géométrie. **D-10 tranche : semelle isolée**, 25 × 25 cm en plan.

| Lecture | Surface d'assise | Charge ELS admissible à q<sub>ELS</sub> = 0,30 MPa |
|---|---|---|
| Semelle filante, 25 cm de large | 2 500 cm² par mètre linéaire | 75 kN par mètre linéaire |
| Semelle isolée 25 × 25 (D-10, indice E) | 625 cm² par semelle | 18,75 kN par semelle (≈ 1,9 t) |
| **Semelle isolée 60 × 60 (D-14, retenue)** | **3 600 cm² par semelle** | **108 kN par semelle** (≈ 11 t) |

**Le rapport est de 4 entre filante et isolée 25 × 25, et de 12 par poteau à 3 m d'entraxe.** Mais D-14 a depuis porté la semelle à 60 × 60 : l'isolée offre désormais **3 600 cm²**, soit **5,76 fois** la surface de l'indice E. **Ce n'est pas un détail de dessin** : c'est le paramètre qui commande le dimensionnement de B-40 — et il a changé deux fois en une journée, ce qui justifie qu'il soit désormais figé au registre.

**Un ordre de grandeur à confronter.** Un poteau HEA200 reprenant quelques mètres carrés de plancher mobilise plusieurs dizaines de kN à l'ELS. Le seuil de **108 kN** couvre désormais cet ordre de grandeur — là où les 18,75 kN de la semelle 25 × 25 ne le couvraient pas. **L'objection technique de l'indice E est levée par D-14.**

**Ce que cela implique, et qui doit être écrit avant B-40 :**

1. **D-14 fixe un plancher**, pas un dimensionnement : 60 × 60 cm est le minimum, la semelle peut être plus grande si le calcul l'exige.
2. **B-40 calcule** la charge ELS par semelle et la compare à **108 kN**.
3. **Si le seuil est dépassé**, la semelle s'agrandit — et cet agrandissement reste dans le cadre de D-14, puisqu'il va dans le sens du minimum. **Aucune nouvelle décision n'est requise pour agrandir ; une réduction, si.**

*(Correction assumée : l'indice C annonçait un « facteur 40 » entre les deux lectures. Le facteur réel est **4** à surface comparable et **12** par poteau à 3 m. L'erreur est corrigée ici et signalée au client.)*

---

### 5.6 D-09 règle la question posée en 5.2 — et transforme la nappe en point de méthode

**La question de 5.2 était :** comment traiter le différentiel de profondeur entre une assise neuve à −1,00 m et des soubassements qui n'étaient enterrés que de 0,50 m ?

**D-09 apporte la réponse attendue** sous forme d'une règle d'exécution :

- relever systématiquement le niveau de l'existant ;
- compléter par **gros béton C16/20** pour atteindre ce niveau ;
- ne jamais laisser une fondation neuve **au-dessus** de l'existant.

C'est exactement le traitement de l'interface qui manquait, et il a le mérite d'être **vérifiable sur site**, pas seulement sur plan. C'est la bonne échelle pour ce type de décision : nul ne connaît le niveau des moellons avant d'avoir ouvert la fouille.

**Ce que D-09 ne règle pas, et qui reste au registre :**

| Point | Pourquoi il subsiste |
|---|---|
| ~~**R-34**~~ | ✅ **FERMÉ par D-12** — D-09 = plancher. Le nivellement ne s'obtient jamais par remontée ; l'approfondissement est la seule voie d'égalisation |
| **R-36** | L'encastrement de 50 cm était justifié par h/B = 2. D-14 porte B à 60 cm : h/B = 0,83. La justification doit être reprise — **je ne l'ai pas fait à la place du BET** |
| **R-31bis / V-26** | Le niveau réel n'existe qu'à l'ouverture. Tant qu'il n'est pas relevé, la reprise en sous-œuvre reste en PARTIEL-DÉCLARÉ |
| **R-35** | La prescription devient un **point d'arrêt** : sans réception contradictoire formalisée, la règle n'a pas de dispositif de contrôle |
| ~~R-13 — nappe~~ | ✅ **Soldée par D-16** (absence de nappe). La réserve R-13 ne porte plus que sur la **coupe type** |

**Le point de vigilance que je souligne le plus fortement :** la règle d'égalisation peut conduire à **descendre plus bas que −1,00 m** là où l'existant est profond. La cote de −1,00 m doit donc être lue comme un **minimum**, jamais comme une cote fixe. Un plan de fondations qui porterait « −1,00 m » sans mentionner la règle d'approfondissement serait **faux par omission** — et c'est précisément ce que le ④ de D-09 cherche à éviter en imposant la note sur les plans.

### 5.7 La prescription ENC est un livrable, pas une annotation

Le ④ de D-09 — « cette note est à indiquer sur les plans et note de calcul » — a une conséquence que je veux souligner : la note devient **opposable**. Elle n'est plus une intention de l'ingénieur, elle est une pièce du dossier au même titre qu'un plan.

C'est pourquoi je l'ai formalisée en **prescription ENC** numérotée, avec **dix alinéas figés** (§ 0sexies de la FDC, version 2), plutôt que rédigée en prose. Une prescription qui se reformule à chaque plan est une prescription qui se perd.

**La version 2 (indice E) intègre D-12 et D-11** : l'alinéa 1 porte « −1,00 m / TN **minimum** — jamais une cote fixe » ; l'alinéa 6 interdit explicitement la remontée ; l'alinéa 10 impose le report intégral sur le plan **« PLS »** et en tête de note de calcul. **Une prescription dont le support n'est pas nommé n'est pas opposable** : c'est tout l'objet de D-11.

**Deux obligations en découlent :**

1. **B-60** devra porter l'ENC **intégralement** sur chaque plan de fondations — pas un renvoi, pas un résumé. Le carnet interdit les renvois en matière de livrable.
2. **B-40** devra porter l'ENC **en tête** de la note de calcul, et non en annexe : c'est elle qui fixe les hypothèses de niveau, donc elle précède les résultats.

---

## 6. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-03) | État | Observation |
|---|---|---|
| Chaque décision a un auteur, une date et un effet identifié | ✅ | **19 décisions**, toutes datées du 19/10/2026, toutes attribuées au **Client**, effet explicité brique par brique |
| Chaque réserve a un responsable et une date de demande | ✅ | **39 réserves** (30 ouvertes, 9 fermées), responsable nommé, date du 19/10/2026, criticité ajoutée. **Total recompté ligne à ligne** |
| Chaque verrou identifie la brique suspendue et ce qui est exécuté malgré tout | ✅ | **21 verrous ouverts**, colonne remplie ; **9 fermetures** tracées ; 3 requalifications inscrites |
| Aucune décision prise à la place du client sans source citée | ✅ | **Aucune ligne de la Section 1 n'émane du rédacteur.** Les trois points soumis étaient des **questions** ; les réponses sont enregistrées en D-10 à D-12 **sans être extrapolées** — la lecture de « PLS » est signalée comme une lecture, et la condition de validité de D-10 est posée comme telle |

**Placeholders résiduels (V7)** : aucun.
**Traçabilité de la supersession** : D-04 n'est pas supprimée du registre. Elle est marquée **« modifiée par D-08 sur le seul point de l'ancrage »** — une décision supersédée reste au registre, c'est la preuve de l'historique.

---

## 7. POINT DE CONTRÔLE HUMAIN

**Sur les trois décisions du 19/10/2026 :**

1. **D-14 (60 × 60 minimum)** — enregistrée comme **plancher** : la semelle peut être agrandie par le calcul, jamais réduite. Confirmez-vous cette lecture ?
2. **R-36** — l'argument h/B = 2 ne tient plus avec B = 60 cm. **Approfondir l'assise**, ou **maintenir −1,00 m** en justifiant la portance par la seule qualité du sol d'assise ? *(Choix du BET ; le registre attend la réponse, il ne la produit pas.)*
3. **D-15 (tassements hors mission)** — B-40 portera la mention explicite qu'aucun tassement n'est vérifié, ni absolu ni différentiel. Cette mention suffit-elle ?
4. **D-16 (absence de nappe)** — enregistrée comme déclaration client ; toute venue d'eau en fouille devient un point d'arrêt. Confirmez-vous ce régime ?

**Sur le registre :**

5. **R-13 est réduite** à la coupe type (nappe soldée par D-16, tassements sortis par D-15). **V-12 est réduit** à SOL-04. Cette décomposition est-elle la bonne façon de tracer la chose ?
6. **V-R3 est annulée par V-R4** : c'est la première fois qu'une requalification est levée. La traçabilité vous convient-elle ?
7. **37 réserves (30 ouvertes) · 16 décisions · 30 verrous (21 ouverts) · 4 requalifications.** Ces compteurs sont recomptés ligne à ligne.

**Sur l'outillage :**

8. **ezdxf 1.4.5 est installé** sur votre instruction. **Aucun fichier DXF n'est présent** dans l'espace de travail ni dans les pièces transmises. L'instruction est enregistrée et l'outil prêt : dès que R-24 est fournie, B-30 à B-33 s'exécutent par script, conformément à V13.

---

*Brique B-03, **indice F**, livrée. Le RDR reste ouvert en tant que registre vivant.*

*Propagation : **B-02 révisée en indice F** · **B-11 livrée** · B-04 inchangée (le PTD ne dépend pas de la géométrie de semelle, seulement des données manquantes).*

> **Note de procédure** : votre message portait trois **décisions**, une **instruction d'outillage** et le mot **GO**. Les décisions ont été consignées (D-14 à D-16) et propagées à la FDC ; le GO a été consommé par **B-11**. La brique suivante — **B-12** — attend un nouveau GO.
