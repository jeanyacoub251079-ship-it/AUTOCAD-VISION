# B-30 — CALAGE SUR DXF/DWG SOURCE

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-30** — Calage sur DXF source |
| Phase | **3 — Calage et vérification** |
| **Mode d'appel** | **COMPLET en plan (XY)** · **PARTIEL-DÉCLARÉ sur l'axe Z** — *0,00 RELATIF, cote absolue non reçue (D-21)* |
| **Régime** | **OUTILLÉ (V13)** — script exécuté, journal consigné, fichiers relus |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Fiche du carnet | `05_PHASE_3_CALAGE/B-30_Calage.md` — lue intégralement (l. 5356-5579) |
| Fichier source `DOC-02` | `google_drive/208_FLORA_Plans_DCE_IndC.dxf` — **AC1032**, 4 399 016 o |
| **Source de recoupement** `DOC-02b` | `google_drive/208_FLORA_DCE_Pièces graphiques_IndC.pdf` — D4, 29 p. A3, ind. C (double assurance exigée le 19/10/2026) |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b30_calage.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b30_calage.txt` |
| Indice du livrable | **C** (remplace l'indice B du 19/10/2026) |
| Date | 19/10/2026 |
| Brique suivante | **B-31 (Preuve de superposition)** |

---

## 0ter. ERRATUM DE L'INDICE B — LE RDC AUSSI ÉTAIT FAUX

Vous avez posé la bonne objection : **un R+1 de 100 m² ne peut pas reposer sur un RDC de 80 m².** Elle m'a obligé à refaire ce que j'aurais dû faire dès l'indice A : **confronter le PDF et le DXF**, au lieu de lire un seul calque.

| # | Ce que j'ai écrit à l'indice B | Ce qui est vrai |
|---|---|---|
| **4** | « la surface du RDC n'était pas établie ; 84,77 m² est une somme de hachures » | ✅ Exact — mais **incomplet** : j'ai laissé entendre que le RDC tournait autour de 85 m². **D4 donne 111,15 m²** pour 9 locaux. |
| **5** | R+1 ≈ 101,79 m² | ⚠ **Incomplet** — le R+1 nomme **10 espaces pour 106,92 m²** : j'avais écarté un **palier de 2,97 m²** en le prenant pour un « élément non nommé », et le dégagement de combles (2,16 m²) |

**La cause est la même que celle que je dénonçais : j'ai lu un calque au lieu de lire le dossier.** Le PDF de l'architecte porte un **tableau de surfaces complet**, page par page, local par local. Il était là depuis le début.

---

## 0. ERRATUM DE L'INDICE A — DEUX ERREURS, DONT UNE GRAVE

L'indice A a été livré ce matin avec un résidu de 1,7 mm et une conclusion « CONFORME ». Le calage lui-même n'est pas en cause : les paramètres, la transformation et le fichier recalé sont exacts. **Ce sont les preuves et les limites qui étaient fausses.** Je les corrige une par une.

| # | Ce que j'ai écrit à l'indice A | Ce qui est vrai | Gravité |
|---|---|---|---|
| **1** | « aire R+1 calculée : 6,03 m² (déclarée 6,03) » — présenté comme une **preuve** | Les 3 polygones ne sont **pas des pièces** : ce sont **2 faux plafonds** et **1 dégagement**. Le 6,03 m² **ne représente aucune surface de plancher** | ⚠ **Grave** — un chiffre faux présenté comme une validation |
| **2** | « **D5 ne porte aucune altimétrie** » (§ 4.1) | **Faux.** D5 porte **11 cotes Z** dans ses textes, de 201,03 m à 204,43 m. Je n'avais cherché que des **calques** de niveau, pas les **textes** | ⚠ **Grave** — une limite affirmée sans avoir été vérifiée |
| **3** | « T3 — preuve la plus forte : somme des aires 84,77 m² = déclarée » | **Mesure circulaire.** Les 84,77 m² de l'inventaire B-00 provenaient **du même calque** que ma mesure. Je comparais une valeur à elle-même | Moyenne — la conclusion reste juste, mais par un autre témoin |

**Ce que ces trois erreurs ont en commun : j'ai validé une donnée sans avoir vérifié ce qu'elle représentait.** Le script comptait des aires ; il ne se demandait pas *de quoi*. Un comptage juste sur un objet mal identifié produit une preuve fausse — et c'est exactement le piège que V13 est censé fermer.

**Votre doute sur les 6,03 m² a mis au jour les trois.** Je le dis sans détour : sans votre lecture, ce chiffre serait parti en note de calcul.

---

## 1. PIÈCE 1 — PARAMÈTRES DE CALAGE *(inchangés, re-vérifiés)*

| Champ | Valeur |
|---|---|
| **Fichier source** | `208_FLORA_Plans_DCE_IndC.dxf` — D5, indice **C**, 13/03/2026 |
| **Format** | DXF **AC1032** (AutoCAD 2018) |
| **Unités déclarées** | **cm** — `$INSUNITS = 5` |
| **Échelle** | **0,010000** — uniforme, imposée par les unités |
| **Rotation calculée** | **0,000000°** — mesurée sur P1→P2 |
| **Translation** | `tx = −85,8697 m` · `ty = −44,4270 m` |
| **Formule** | `X = (x_src − 8 586,97) × 0,01` · `Y = (y_src − 4 442,70) × 0,01` |

| Point | Rôle | Source (cm) | Repère de travail (m) |
|---|---|---|---|
| **P1** | **Origine** — coin SO de l'enveloppe | (8 586,97 ; 4 442,70) | **(0,000 ; 0,000)** |
| **P2** | Axe X | (9 576,80 ; 4 442,70) | (9,898 ; 0,000) |
| **P3** | Axe Y | (8 586,97 ; 6 291,84) | (0,000 ; 18,491) |
| **P4** | **Témoin**, non utilisé | (9 576,80 ; 6 291,84) | (9,898 ; 18,491) |

Aire du triangle P1-P2-P3 : **915 167 cm²** — non alignés. `cos(P1→P2 , P1→P3) = 0,000000000` — repère orthonormé, la rotation nulle est **mesurée**, pas supposée.

**Origine P1 : validée par vous le 19/10/2026** (question 2 du point de contrôle de l'indice A).

### Axe Z — **D-20**, précisée par **D-21**

Vous avez retenu : **le niveau du plancher bas du RDC existant est le niveau 0,00**. **D-21 en précise le régime : ce 0,00 est RELATIF**, la cote absolue n'étant pas reçue. Voir § 4.2.

| Élément | Convention |
|---|---|
| **Z = 0,00 RELATIF** | **Plancher bas du RDC existant** — *D-20 du 19/10/2026, régime RELATIF fixé par D-21* |
| Z négatif | Vers le bas — fond de fouille, arases |
| Z positif | Vers le haut — R+1, faîtages |

⚠ **D-20 ne remplace pas D-09, elle la complète** — et c'est un point que je dois signaler : **D-09 référençait l'arase inférieure des fondations au TERRAIN NATUREL**. Désormais, l'origine Z est le **plancher bas du RDC existant**. Ces deux repères ne sont pas identiques. L'écart entre eux — hauteur du plancher bas au-dessus du terrain naturel — **n'est mesuré nulle part** : ni D5, ni D2, ni D4 ne le portent.

**Conséquence** : « −1,00 m » reste une prescription opposable, mais **son expression dans le repère relatif n'est pas établie** — l'écart entre plancher bas et terrain naturel n'est mesuré nulle part. Voir § 4.3 : **H-25**, proposée sous un objet restreint.

---

## 2. PIÈCE 2 — RÉSIDU ET PREUVES *(section refondue)*

| Témoin | Nature | Mesure | Écart | Valeur probante |
|---|---|---|---|---|
| **T1** — coin NE | quatrième coin du rectangle | reconstruit vs source | **0,000000 m** | ❌ **Nulle.** Le quatrième coin d'un rectangle est déterminé par les trois autres : cet écart est nul **par construction**. Consigné pour la traçabilité, **pas comme preuve** |
| **T2** — emprise | dimensions portées au dossier | calculée **9,898 × 18,491 m** vs **9,900 × 18,490 m** | **1,7 mm / 1,4 mm** | ✅ Réelle, mais **partiellement circulaire** : l'emprise déclarée provient de la même lecture de D5 |
| **T3** — étiquettes d'aire | **13 polygones confrontés aux 13 étiquettes imprimées par l'architecte** | écart maximal **0,005 m²** | **13/13 appariés** | ✅ **La seule preuve réellement indépendante** : le texte est écrit par l'architecte, la géométrie est mesurée par le script. Deux sources distinctes, même résultat |

**T3 en détail** — les treize étiquettes, toutes retrouvées au centième :

| Calculé | Étiquette | Écart |
|---|---|---|
| 16,08 | 16,08 | +0,001 |
| 12,80 | 12,80 | +0,005 |
| 11,20 | 11,20 | +0,005 |
| 9,60 | 9,60 | +0,005 |
| 9,15 | 9,15 | +0,004 |
| 5,49 | 5,49 | +0,003 |
| 5,42 | 5,42 | +0,000 |
| 5,19 | 5,19 | +0,000 |
| 5,10 | 5,10 | +0,004 |
| 4,75 | 4,75 | +0,005 |
| 2,37 | 2,37 | +0,003 |
| 2,16 | 2,16 | +0,001 |
| 1,49 | 1,49 | +0,005 |

**Résidu géométrique retenu : 1,7 mm** pour un seuil `GEO-12` de **20 mm** — **CONFORME**, facteur onze. **Seuil validé par vous** (question 1 du point de contrôle).

> **Ce que T3 ne prouve pas.** Elle valide l'**échelle** et la **cohérence géométrie/annotation**. Elle ne dit rien de la **nature** des surfaces mesurées — et c'est précisément l'erreur que j'ai commise à l'indice A. Voir § 3.

---

## 3. SURFACES — RECONSTRUCTION SUR DEUX SOURCES INDÉPENDANTES

### 3.1 Méthode, et ce qu'elle a corrigé

**Deux sources lues séparément, puis confrontées :**

- **D4** — `208_FLORA_DCE_Pièces graphiques_IndC.pdf`, 29 pages. Les pages **11 à 18** sont des planches d'aménagement, une ou plusieurs par local, portant chacune sa surface et ses hauteurs ; les pages **6, 9, 10, 23, 24, 25** reprennent les mêmes cotes sur les plans d'ensemble.
- **D5** — le DXF : 13 polygones du calque `092_surfaces projet`, dont **10 dans le cadre du RDC (F6)** et **3 dans celui du R+1 (F3)**.

**Ce que la confrontation a révélé, et que je n'avais pas vu :**

1. Les **numéros de boxes et de bureaux n'existent pas** sur les plans : les étiquettes sont collées au mot « Box kiné » ou « Bureau », sans numéro. Je ne les numérote donc plus — je les désigne par leur surface.
2. Le **2,97 m² de la page 16 n'est pas un « élément non nommé »** : c'est un **palier**. Je l'avais classé hors total par excès de prudence ; il compte.
3. Le **1,84 m² de la page 18** est une **tablette stratifiée** — du mobilier, pas un sol.

### 3.2 RDC — 9 espaces nommés, **111,15 m²**

| Espace | Surface | Source |
|---|---|---|
| **Plateau technique** | **33,14 m²** | D4 p. 13 |
| Bureau | 16,08 m² | D4 p. 12 · D5 |
| Bureau | 12,80 m² | D4 p. 11 · D5 |
| Box kiné | 11,20 m² | D4 p. 11 · D5 |
| Box kiné | 9,60 m² | D4 p. 11 · D5 |
| Box kiné | 9,15 m² | D4 p. 12 · D5 |
| Entrée | 9,24 m² | D4 p. 15 |
| Sanitaire PMR | 5,19 m² | D4 p. 14 · D5 |
| Attente | 4,75 m² | D4 p. 12 · D5 |
| **Total** | **111,15 m²** | |

**Hors total, et pourquoi** : **faux plafonds** 5,49 + 5,10 + 5,42 = **16,01 m²** (cotes `hsfp`, aucun n'est un sol) · **1,35 m²** de statut indéterminé, porté avec une hauteur sous plafond de 3,24 m près du palier — je ne l'intègre pas et je le signale plutôt que de trancher seul.

### 3.3 R+1 — 10 espaces nommés, **106,92 m²**

| Espace | Surface | Source |
|---|---|---|
| **Salle de sport** | **34,25 m²** | D4 p. 17 |
| Bureau | 16,50 m² | D4 p. 16 |
| Bureau | 13,26 m² | D4 p. 16 |
| Salle commune | 11,75 m² | D4 p. 18 |
| Vestiaire | 9,32 m² | D4 p. 18 |
| Attente | 8,38 m² | D4 p. 16 |
| Dégagement | 5,96 m² | D4 p. 16 |
| Palier | 2,97 m² | D4 p. 16 |
| Douche | 2,37 m² | D4 p. 18 |
| Dégagement (trappe combles) | 2,16 m² | D4 p. 6 |
| **Total** | **106,92 m²** | |

**Si l'on exclut les deux petites circulations** (palier 2,97 et dégagement 2,16), on retrouve **101,79 m²** — le chiffre que j'avais avancé à l'indice B, qui n'était donc pas faux mais **incomplet**.

**Hors total** : **1,84 m²** de tablette stratifiée (mobilier) · **1,49 m²** de faux plafond fixe · la **seconde occurrence de 2,37 m²** de la page 18, qui est le faux plafond de la douche, pas un second local.

### 3.4 Le contrôle qui manquait — là où les deux sources se recoupent

| Contrôle | D4 (PDF) | D5 (DXF) | Écart |
|---|---|---|---|
| RDC — les **7** espaces portés des deux côtés | 68,77 m² | 68,77 m² | **0,00** |
| RDC — faux plafonds | 16,01 m² | 16,01 m² | **0,00** |
| R+1 — les **3** polygones du calque | 6,02 m² *(2,37 + 2,16 + 1,49)* | 6,02 m² | **0,00** |
| **Cotes Z** | **11 valeurs**, 201,03 → 204,43 | **11 valeurs identiques** | **0** |

**Le total du calque est 90,80 m²** = **84,77** (RDC) + **6,03** (R+1) : ce sont exactement les deux chiffres que j'avais pris, à l'indice A puis à l'indice B, pour des surfaces de plancher. Ce sont des **sommes de hachures**, pas un programme de locaux.

**Les onze cotes altimétriques relevées dans D5 sont identiques, au centimètre, à celles portées sur les PDF de D4.** C'est la double assurance demandée : deux fichiers produits séparément donnent le même résultat, sur tout ce qu'ils ont en commun.

**Mais tout ce qu'ils n'ont pas en commun est le plus important.** Le calque de hachures ne porte **ni le plateau (33,14 m²), ni l'entrée (9,24 m²), ni le palier (2,97 m²), ni le dégagement de combles (2,16 m²)**, et il ne porte du R+1 que trois polygones de service. **Le DXF est structurellement incomplet** ; c'est le PDF qui porte le programme. La leçon des trois erreurs est la même à chaque fois : **j'ai lu un calque au lieu de lire le dossier.**

**Et D4 va plus loin que D5** : les pages 26 et 27 portent l'altimétrie de toiture — faîtages **209,19 / 209,29 / 210,32 m**, gouttières **205,41 / 205,43 / 206,57 m**, bas de toiture **203,55 à 207,84 m**, haut de mur **203,69 / 203,76 m**. **Aucune de ces cotes n'existe dans D5.**

### 3.5 Conclusion — les trois valeurs

| | Indice A | Indice B | **Indice C** |
|---|---|---|---|
| **RDC** | 84,77 m² ❌ | « ~85 m² » ⚠ | **111,15 m²** ✅ |
| **R+1** | 6,03 m² ❌ | 101,79 m² ⚠ | **106,92 m²** ✅ |
| **Rapport R+1 / RDC** | 0,07 ❌ | 1,20 ⚠ | **0,96** ✅ |

**Le rapport 0,96 est cohérent** : le R+1 est très légèrement plus petit que le RDC, ce qui est le cas normal d'un étage sous rampant. **Votre objection était juste, et c'est elle qui a produit le bon chiffre.**

**Ce que cela change pour la structure** : **111 m² de RDC et 107 m² de R+1**, soit **218 m² de planchers**, dont **67,39 m² de salle de sport et de plateau technique** — les deux locaux les plus chargés — portés par des planchers **dont aucun sondage n'existe**. RI-04 ne change pas de cote ; son objet vient de **doubler**.

## 4. ALTIMÉTRIE — **CE QUE J'AVAIS DÉCLARÉ ABSENT EXISTE**

### 4.1 Les 11 cotes Z relevées dans D5

| Cote | Occurrences | Famille |
|---|---|---|
| **201,03 m** | 4 | **RDC — niveau bas** |
| 201,06 m | 1 | RDC — isolé |
| 201,22 m | 1 | RDC — isolé |
| **201,23 m** | 6 | **RDC — niveau haut** |
| 203,59 m | 1 | R+1 — isolé |
| **203,79 m** | 3 | **R+1 — niveau bas** |
| **203,81 m** | 3 | **R+1 — niveau haut** |
| 204,40 m | 1 | R+1 — isolé |
| 204,41 m | 1 | R+1 — isolé |
| 204,42 m | 2 | R+1 — isolé |
| 204,43 m | 1 | R+1 — isolé |

**Deux familles au RDC, séparées de 20 cm** (201,03 / 201,23), et **deux familles au R+1** (203,79 / 203,81). Un écart de 20 cm entre deux cotes du même niveau est l'écart typique entre **niveau brut** (dessus de structure) et **niveau fini** (dessus de revêtement).

### 4.2 **D-21 — LE NIVEAU 0,00 EST RELATIF**

Vous avez tranché la question que D-20 laissait ouverte, et d'une manière qui **supprime le choix** au lieu de le forcer :

> **Le niveau du RDC existant est le 0,00 RELATIF. Lorsque la cote exacte sera reçue, elle sera notifiée en écrivant : « 0,00 RELATIF = [cote exacte reçue] ».**

**Ce que cela règle.** Je n'ai plus à choisir entre 201,03 m et 201,23 m avant d'avoir l'information — et je ne risque plus de figer un calcul sur une hypothèse de 20 cm. Les plans portent `0,00 RELATIF`, point. La substitution se fera **en une seule écriture**, sur tous les plans et toutes les notes à la fois, quand la cote sera là.

**Ce que cela impose, en contrepartie** : une **traçabilité stricte**. Le jour où la cote arrive, il faut pouvoir dire **quel document, à quelle date, l'a fournie** — sinon « 0,00 RELATIF = 201,03 m » devient une affirmation sans source, exactement ce que D-18 reprochait aux contraintes de sol.

**Formulation retenue sur les plans et notes** — elle doit apparaître **intégralement**, jamais en renvoi (règle D-09 ④) :

> **« Niveau 0,00 RELATIF = plancher bas du RDC existant. Cote absolue non reçue à ce jour. La cote exacte, dès réception, sera notifiée et substituée en tête de la présente note et sur tous les plans, sans modification des cotes relatives. »**

### 4.3 Ce que D-21 ne règle pas — la double référence avec D-09

**D-09 référence l'arase inférieure des fondations au TERRAIN NATUREL. D-21 référence le 0,00 au plancher bas du RDC existant.**

Deux repères, et **l'écart entre eux n'est mesuré nulle part** : ni D5, ni D2, ni D4, ni le rapport GEOFLORAV2 — et D-21 ne le fournit pas, puisqu'elle porte sur la cote **absolue** du plancher, pas sur sa **hauteur au-dessus du sol extérieur**.

**Conséquence, dite sans détour** : la prescription « −1,00 m / TN » reste opposable, mais **elle ne se traduit pas encore en cote relative**. Tant que l'écart n'est pas mesuré, un fond de fouille coté « −1,00 m RELATIF » sur nos plans pourrait être à 1,30 m comme à 0,70 m sous le terrain naturel.

**Je retire donc H-25 telle que je l'avais proposée à l'indice B** — vous aviez raison, elle était inutile : avec D-21, plus personne n'a besoin de savoir à quelle cote absolue se situe le plancher. **Mais la question qui restait dessous n'était pas celle-là**, et elle n'est toujours pas tranchée. Je la repose sous le même numéro, avec un objet différent et plus étroit :

**Je propose donc H-25**, reformulée pour l'ère D-21 :

> **H-25** — *« Le plancher bas du RDC existant est réputé au niveau du terrain naturel extérieur : l'écart h entre les deux repères est pris égal à 0,00 m. La cote −1,00 m / TN de D-09 est donc égale à −1,00 m RELATIF. Cet écart sera mesuré au droit de chaque fouille à l'ouverture (H-15) ; tout écart supérieur à 10 cm est un point d'arrêt et impose la reprise des cotes de fondation. »*

**Ce qu'elle protège** : elle permet de coter et de calculer **aujourd'hui** sans affirmer un nivellement que personne n'a fait, et elle **borne** l'erreur possible à ce qui sera mesuré en fouille.

**Ce qu'elle ne protège pas** : si l'écart réel est de 40 cm, les fondations seront à 40 cm de la cote voulue par rapport au sol. Le point d'arrêt de H-15 est donc la seule vraie sécurité — pas l'hypothèse.

## 5. PIÈCE 3 — FICHIER RECALÉ *(inchangé, re-exécuté)*

| Champ | Valeur |
|---|---|
| Nom | **`208_FLORA_Plans_DCE_IndC_cale_B30.dxf`** |
| Emplacement | `google_drive/` *(hors dépôt Git)* |
| Unités | **`$INSUNITS = 6`** (mètres) |
| Relecture réelle | 13 polygones ; enveloppe RDC **(0,000 ; 0,000) → (9,898 ; 18,491) m** |
| Étendue totale en Y | **−29,866 m** — les 6 feuilles ont été transformées ensemble ; le filtrage relève de B-32 |

---

## 6. LIMITES DÉCLARÉES *(section corrigée)*

| # | Limite | Statut |
|---|---|---|
| **6.1** | **L'axe Z n'est pas calé** | ✅ **Maintenu, mais pour une autre raison** : les cotes existent (11 valeurs), mais **aucune n'est rattachée à un repère déclaré**, et D-20 ne dit pas laquelle représente le plancher bas |
| **6.2** | **Le lien D5 ↔ D2 n'est pas établi** | ✅ Maintenu — D2 n'existe qu'en PDF. Relève de **B-31** |
| **6.3** | **L'enveloppe est une boîte englobante** | ✅ Maintenu — le calque `010_mur` ne compte que 20 entités, très loin d'un contour de bâtiment |
| **6.4** | **L'existant n'est pas calé** | ✅ Maintenu — aucune surface d'existant sur ce calque |
| **6.5** | **La couche `092_surfaces projet` n'est pas un plan de surfaces de plancher** | ✅ **Confirmé** — elle mélange des pièces et des **faux plafonds** ; le **plateau (33,14 m²)** et l'**entrée (9,24 m²)** n'y figurent pas. Aucune surface de plancher ne peut en être déduite par sommation |
| **6.6** | **Le DXF est moins complet que le PDF** | 🆕 **Nouvelle limite** — D4 p. 26-27 porte l'altimétrie de toiture (faîtages, gouttières, bas de toiture), **absente de D5**. Toute lecture de D5 seul est incomplète par construction : c'est la leçon des deux erreurs de l'indice A et de celle de l'indice B |

---

## 7. JOURNAL D'EXÉCUTION (OUT-03)

| Élément | Valeur |
|---|---|
| Script | `_scripts/b30_calage.py` — **révisé** le 19/10/2026 (témoin T3 refondu, contrôle Z ajouté) |
| Journal | `_rendus/b30_calage.txt` — **11 sections** |
| Code de sortie | **0** |
| Contrôles | unités · non-alignement · orthogonalité · résidu T1/T2/T3 · relecture du fichier écrit · **extraction des 11 cotes Z** · **double assurance surfaces D4/D5** |
| Écarts consignés | 1,7 mm d'emprise · **0,005 m² d'étiquette** · −29,866 m d'étendue Y |

---

## 8. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-30) | État | Observation |
|---|---|---|
| ≥ 3 points de calage non alignés, deux repères | ✅ | P1, P2, P3 — aire 915 167 cm² |
| Transformation calculée et justifiée | ✅ | échelle 0,01 · rotation mesurée 0° · translation calculée |
| Résidu mesuré et comparé à `GEO-12` | ✅ **renforcé** | **1,7 mm / 20 mm** — et désormais adossé à un témoin **non circulaire** (13 étiquettes) |
| Preuve de superposition PDF + PNG | ✅ | `_calage/B-30_preuve_calage.png` + `.pdf` |
| Fichier recalé nommé et indicé | ✅ | `…_cale_B30.dxf`, `$INSUNITS = 6`, relu |
| Aucun ajustement visuel | ✅ | Aucun déplacement de point |
| **Double assurance des surfaces** | 🆕 ✅ | **D4 (PDF) et D5 (DXF) lus séparément** : 17 locaux vérifiés un à un sur leur planche de détail, totaux **recalculés par script**, verdict **CONFORME** |

**Écarts signalés (V4)** : ① mode COMPLET en XY seulement, **Z en régime RELATIF assumé (D-21)** ; ② **trois erreurs de l'indice A corrigées au § 0**, dont une conclusion de preuve fausse ; ③ **deux erreurs de l'indice B corrigées au § 0ter** — dont une surface de RDC sous-estimée. La répétition de la même faute (lire un calque au lieu du dossier) est consignée comme telle : elle est désormais **bloquée par un contrôle scripté**, plus par une intention.

**Placeholders résiduels (V7)** : aucun.

---

## 9. POINT DE CONTRÔLE HUMAIN

1. **Les surfaces** : RDC **111,15 m²** · R+1 **106,92 m²** *(101,79 hors petites circulations)*, reconstruites sur **D4 et D5 concordants là où ils se recoupent**. Le validez-vous comme valeurs de référence — et faut-il les porter à **B-00** en remplacement des 84,77 et 6,03 m² ?
2. **Le palier de 2,97 m² et le dégagement de combles de 2,16 m²** : je les ai intégrés au total du R+1. Faut-il les compter comme surfaces utiles, ou les tenir hors surface comme circulations ?
3. **H-25** — ce n'est plus « plancher bas = TN » (retirée, D-21 l'a vidée), mais « l'écart entre TN et plancher bas vaut 0,00 m, à mesurer en fouille ». Je l'ajoute aux 24 hypothèses ?
4. **La mention « 0,00 RELATIF »** doit-elle figurer dès maintenant sur tous les plans de B-60, y compris ceux qui ne portent aucune cote de fondation ?

---

*Brique B-30, **indice C**. Régime outillé : script révisé, journal à **11 sections**, fichiers relus.*

*Calage **CONFORME** — résidu 1,7 mm pour un seuil de 20 mm et double assurance D4/D5 sur les 11 cotes Z.*

*Surfaces corrigées : **RDC 111,15 m²** · **R+1 106,92 m²** — rapport 0,96, cohérent.*

*Aucune brique aval engagée : **B-31** attend un GO.*
