# B-31 — PREUVE DE SUPERPOSITION

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-31** — Preuve de superposition |
| Phase | **3 — Calage et vérification** |
| Mode d'appel | **COMPLET** |
| Régime | **OUTILLÉ (V13)** — script exécuté, journal consigné, rendus relus |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Livrable prouvé | **B-32 ind. C** — `FLORA_RDC_VUE-NETTOYEE_IndC.dxf` · `FLORA_R1_VUE-NETTOYEE_IndC.dxf` |
| Paramètres B-30 | ind. C — échelle 0,010000 · rotation 0,000000° · P1 (8586,97 / 4442,70) |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b31_superposition.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b31_superposition.txt` |
| Rendu `OUT-04` | `_calage/B-31_preuve_A_fidelite.png/.pdf` · `_calage/B-31_preuve_B_empilement.png/.pdf` |
| Seuil | **GEO-12 = 2 cm** |
| Date | 19/10/2026 |
| Verdict | **VALIDÉ SOUS RÉSERVE** — voir § 4 |
| Brique suivante | **B-40** (fondations) |

---

## 1. TROIS PREUVES, TROIS QUESTIONS DIFFÉRENTES

Une preuve de superposition qui ne pose qu'une question ne prouve rien. J'en ai posé trois, et la troisième a été ajoutée en cours de route parce que les deux premières ne couvraient pas le risque réel.

| Preuve | Question | Ce qu'elle détecte |
|---|---|---|
| **A — Fidélité** | Chaque point livré existe-t-il dans la source, à la même coordonnée ? | un **redessin** déguisé en extraction |
| **B — Empilement** | Les murs existants du R+1 tombent-ils sur ceux du RDC ? | un **décalage entre niveaux** |
| **C — Confinement** | Chaque entité livrée tient-elle dans le cadre de son niveau ? | une **planche voisine** laissée passer |

---

## 2. PREUVE A — FIDÉLITÉ DE L'EXTRACTION

**Résultat : écart maximal 0,6 mm au RDC, 0,0 mm au R+1. Aucun point sans correspondance.**

| | RDC | R+1 |
|---|---|---|
| Sommets de référence (source) | 13 413 | 9 488 |
| Sommets de la vue nettoyée | 10 800 | 8 753 |
| **Sans correspondance dans la source** | **0** | **0** |
| Écart maximal | **0,0006 m** | **0,0000 m** |
| Écart moyen | 0,0000 m | 0,0000 m |
| Verdict GEO-12 (2 cm) | **CONFORME** | **CONFORME** |

**Ce que cela prouve, exactement.** Un redessin produit des écarts **diffus et répartis** : un mur recopié à 3 mm, une cote arrondie, une intersection approximée. Ici, **10 800 points sur 10 800** retombent sur un sommet de la source, avec un écart maximal de 0,6 mm — l'ordre du bruit d'arrondi. La vue nettoyée **est** la source, moins ce qui a été retiré. C'est la définition d'une extraction.

**Une correction en cours de route, qui mérite d'être dite.** Le premier passage donnait 591 points « sans correspondance », avec un écart maximal de 10 000 m. Deux causes, toutes deux de mon fait :

1. **Les blocs miroir.** Les portes insérées avec une extrusion `(0,0,−1)` — donc en miroir — ne sont pas restituées en coordonnées monde par `virtual_entities()`. Elles apparaissaient à **x négatif**, à 8 000 m du bâtiment. Le script applique désormais la réflexion lui-même : le défaut a disparu.
2. **Deux calques internes non déclarés.** Les blocs de menuiserie conservés embarquent en interne les calques `097_traits-fins-005` et `2_2-MENUISERIE-CO`. Ils voyagent avec le symbole de porte : on ne peut pas les retirer sans déchirer la porte. **B-32 ne les avait pas déclarés** — c'est un manque de mon tableau de nettoyage, pas un défaut du livrable. Corrigé au § 2.1 de B-32.

---

## 3. PREUVE C — CONFINEMENT AU CADRE

| | RDC | R+1 |
|---|---|---|
| Entités livrées | 327 | 243 |
| **Entités hors du cadre** | **0** | **0** |
| Verdict | **CONFORME** | **CONFORME** |

Le DXF source contient **six planches juxtaposées** sur 50 × 35 m chacune. Une extraction qui laisse passer la planche voisine se voit ici immédiatement. Aucune ne passe.

*(Mesure par `extents()` : la boîte réelle de l'entité, blocs compris. Une première version mesurait les points d'insertion — elle déclarait 2 200 sommets hors cadre pour le R+1, tous dus aux blocs miroir. Le défaut était dans la mesure, pas dans le livrable.)*

---

## 4. PREUVE B — EMPILEMENT DES NIVEAUX

### 4.1 B1 — les enveloppes : **NON CONFORME à 2 cm**

| | X | Y |
|---|---|---|
| Murs existants **RDC** | 84,69 → 96,16 m | 43,43 → 63,27 m |
| Murs existants **R+1** *(translatés de 37,55 m)* | 84,69 → 96,10 m | 43,44 → 63,37 m |
| **Écart sur les 4 extrémités** | **0,06 m** | **0,10 m** |

**Écart maximal : 10,1 cm.** Le seuil est de 2 cm. **La preuve est NON CONFORME.**

### 4.2 Ce que la preuve ne dit pas, et qu'il faut dire

**L'écart ne vient pas de nous.** La preuve A établit que notre extraction est fidèle au dixième de millimètre. L'écart de 10 cm existe donc **dans le fichier de l'architecte** : les deux niveaux n'y sont pas dessinés parfaitement superposés.

**Et il existe aussi dans le bâtiment.** C'est un pavillon ancien, en moellons, avec un relevé géomètre : les murs d'un étage ne sont jamais exactement à l'aplomb de ceux du dessous. **10 cm sur 20 m de long, c'est un fruit de 0,5 %** — l'ordre de grandeur d'un mur ancien qui rattrape son aplomb.

**La bonne question n'est donc pas « comment corriger ? » mais « quel calage retenir ? ».** Deux réponses possibles, et c'est un choix de BET :

- **caler le R+1 sur le RDC** par translation rigide — c'est ce que fait la preuve, et cela laisse 10 cm d'écart en bout de bâtiment ;
- **caler chaque niveau sur son propre relevé** — chaque plan est juste dans son repère, mais les deux plans ne se superposent plus exactement.

**C'est l'objet de la réserve R-64**, ouverte au RDR par cette brique.

### 4.3 B2 — le mur à mur : le constat qui compte pour la structure

| Distance des murs du R+1 aux murs du RDC | Sommets | Part |
|---|---|---|
| ≤ 2 cm | 18 | 9 % |
| ≤ 5 cm | 51 | 25 % |
| ≤ 10 cm | 72 | 36 % |
| ≤ 50 cm | 147 | 73 % |
| **> 50 cm** | **54** | **27 %** |

**Écart médian : 22 cm. Écart maximal : 1,85 m.**

**Lecture structurelle, et c'est le résultat le plus important de cette brique** : les **enveloppes** se superposent (à 10 cm près), mais **27 % des murs du R+1 ne sont pas au-dessus d'un mur du RDC**. Les cloisons du niveau haut — bureaux, salle commune, vestiaire, douche — **ne sont pas portées**.

Cela ne condamne rien : le R+1 du projet est un aménagement sous rampant, et son plancher est porté par la charpente, pas par des cloisons maçonnées. **Mais B-40 ne peut pas descendre les charges du R+1 à la verticale** : elles transitent par les poutres F1 à F4 et les poteaux, et c'est **ce chemin-là** qu'il faut vérifier. Cette brique le transmet à B-40 comme un **constat**, pas comme un écart à corriger.

---

## 5. VERDICT

| Preuve | Verdict |
|---|---|
| **A — Fidélité de l'extraction** | ✅ **CONFORME** |
| **B — Empilement des enveloppes** | ❌ **NON CONFORME** (10,1 cm pour 2 cm) |
| **C — Confinement au cadre** | ✅ **CONFORME** |
| **VERDICT GLOBAL** | ⚠️ **VALIDÉ SOUS RÉSERVE** |

**Pourquoi « validé sous réserve » et non « à corriger ».** Le carnet autorise la diffusion d'un livrable « validé sous réserve » à condition que les écarts acceptables soient justifiés explicitement. C'est le cas ici :

- **le livrable est fidèle** — preuves A et C conformes, 0 point hors source, 0 entité hors cadre ;
- **l'écart B est extérieur au livrable** — il est dans la géométrie de l'architecte, et probablement dans le bâtiment ;
- **il ne rend pas le livrable inutilisable** — les plans de B-60 seront établis niveau par niveau, dans le repère de chaque niveau.

**Ce qu'il interdit** : utiliser la superposition RDC/R+1 comme preuve de calage absolu. **Ce qu'il impose** : ouvrir la réserve R-64 et trancher la convention de calage avant B-60.

---

## 6. RÉSERVE OUVERTE

| Réf. | Objet | Suite |
|---|---|---|
| **R-64** | **Convention de calage entre niveaux** — le R+1 n'est pas à l'aplomb du RDC (10,1 cm d'écart d'enveloppe, 22 cm d'écart médian mur à mur). Deux conventions possibles : translation rigide du R+1 sur le RDC, ou calage indépendant niveau par niveau | **Décision BET** — à trancher avant B-60. N'empêche pas B-40 |

---

## 7. POINT DE CONTRÔLE HUMAIN

1. **Le verdict « validé sous réserve »** vous convient-il, ou préférez-vous que je reprenne B-31 après décision sur R-64 ?
2. **La convention de calage (R-64)** : translation rigide, ou calage indépendant de chaque niveau ?
3. **Le constat B2** — 27 % des murs du R+1 non portés — confirme que les charges du niveau haut passent par les poutres et poteaux. B-40 est engagée sur cette base.

---

*Brique B-31, **indice C**. Régime outillé : script `b31_superposition.py`, journal 5 sections, deux rendus PNG + PDF relus.*

*Preuve A : **0,6 mm** d'écart maximal sur 10 800 points — l'extraction est fidèle. Preuve C : **0 entité hors cadre**.*

*Preuve B : **10,1 cm** d'écart d'enveloppe — l'écart est dans le fichier de l'architecte, pas dans le livrable. Réserve **R-64** ouverte.*
