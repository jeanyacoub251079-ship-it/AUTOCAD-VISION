# B-24 — EXISTANT NON SONDÉ (mode PARAMÉTRIQUE)

> **EN ATTENTE DE DONNÉES — NE PAS EXÉCUTER — Indice A — suffixe `_P`**
> Cette note ne conclut pas. Elle écrit les vérifications **en littéral**, sur des éléments dont les caractéristiques ne sont pas mesurées, et elle liste ce qu'il faut aller chercher pour pouvoir conclure.

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-24** — Vérification des éléments existants non sondés |
| Phase | **3 — Conception et synthèse structurelle** (dernière brique de la phase : après `B-23`) |
| **Mode d'appel** | **PARAMÉTRIQUE — par construction.** Si la donnée existait, la brique relèverait de `B-46` (mode COMPLET) et n'aurait pas lieu d'être |
| Régime | **OUTILLÉ (V13)** — sensibilité calculée par script, journal d'exécution conservé |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b24_existant.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b24_existant.txt` |
| Résultats machine | `dossiers/CROISSY/_rendus/b24_existant.json` |
| Sortie graphique | **Aucune** — la fiche `B-24` n'exige aucun livrable graphique |
| **Indice** | **B** — `E-03` (solives `8 x 18`) **sorti du champ** : ses données existent (`D3` p. 10, `EXI-01a`) ; il relève désormais de `B-43` |
| Date | **20/10/2026** |
| Brique suivante | **`B-42`** (poteaux et jambages BA — livrée) puis **`B-43`** (planchers et plancher haut) |

> **Révision B — 20/10/2026.** L'indice A classait `E-03` (solives `8 x 18`) parmi les éléments non sondés, avec pour données manquantes « entraxe réel, portée, classe ». **C'était faux.** `D3` p. 10 donne l'entraxe (`0,50 m`), la portée (`2,77 m`), la section (`8 x 18`) et la poutre porteuse (`20 x 15`, portée `4,34 m`) ; la classe `C18` est l'hypothèse déclarée `EXI-03`. `E-03` **sort du champ de `B-24`** et devient une vérification de `B-43`. Les **7 autres éléments** et tous les résultats de l'indice A sont **inchangés**. Ce que l'indice B ajoute : le contrôle de cohérence de `E-03` avec ses données réelles, et la question qu'il soulève — le **périmètre de la recharge de sol de `15 cm`**.

> **Ce que cette brique fait — et ce qu'elle ne fait pas.** Les éléments existants que nos travaux chargent (ou que nos renforts chargent davantage) n'ont **aucune caractéristique mesurée** — sauf les solives de plancher, dont le diagnostic donne la section, l'entraxe et la portée (voir § 2.1). `B-24` écrit pour chacun la **vérification littérale** — la donnée manquante reste en symbole — puis balaie la **plage de valeurs plausibles** et rend un **verdict de sensibilité**, jamais une conclusion. Rien de ce qui est écrit ici n'est exécutable.
>
> **Trois interdits, tenus par construction :** aucune valeur n'est retenue · aucun élément n'est déclaré conclu · aucune valeur de repli n'est proposée (elle relèverait d'une décision `RDR`).

---

## 0. RÉPONSE DIRECTE — CE QUE L'ABSENCE DE SONDAGE COÛTE EXACTEMENT

Sur les **sept éléments non sondés**, **deux sont défavorables pour toute la plage plausible** : la poutre maîtresse et la ferme de charpente. Pour ces deux-là, **la décision de renforcer est déjà acquise** — le relevé ne changera pas le « faut-il », seulement le « combien ».

| Constat | Chiffre | Conséquence |
|---|---|---|
| Éléments en attente de données | **7** (`E-01`, `E-02`, `E-04` à `E-08`) | Aucun n'est conclu |
| **Élément sorti du champ** (ind. B) | **1** — `E-03` (solives `8 x 18`) | Données disponibles : la vérification relève de `B-43`, pas de `B-24` |
| **Favorables pour toute la plage** | **1** (`E-01` maçonnerie en compression) | `sigma_d / f_d <= 0,885` même à `f_k = 0,5 MPa` — la seule bonne nouvelle, et elle ne vaut **que** pour la compression |
| **Limites** (satisfaisants pour une partie de la plage) | **3** (`E-04`, `E-06`, `E-08`) | Le sondage est **indispensable** pour trancher |
| **Défavorables pour toute la plage** | **2** (`E-02` poutre maîtresse, `E-05` ferme) | Renforcement **acquis** ; le relevé dimensionne, il ne décide plus |
| **Sans plage plausible** | **1** (`E-07` plancher haut) + **2 zones non relevées** | La nature même du support est inconnue : **inspection visuelle avant toute formule** |
| Cas de sensibilité balayés | **83** | Plage couverte entièrement, sans resserrement autour des valeurs qui arrangent |
| Éléments déclarés conclus | **0** | C'est le point du mode PARAMÉTRIQUE |

> **Le point dur n'est pas la résistance, c'est la nature.** Pour sept éléments, on sait *ce que* l'on cherche (une section, une classe) et l'on peut poser une plage. Pour le **plancher haut** (`E-07`), on ne sait même pas s'il est en bois, en béton armé ou en hourdis : aucune formule ne s'écrit sans cette réponse. Or c'est lui qui porte la charpente, et nos renforts `B-44` **augmentent** ce qu'il transmet.

---

## 1. GLOSSAIRE DES CODES — POUR LIRE CETTE NOTE SANS EN OUVRIR UNE AUTRE

| Code | Objet en clair |
|---|---|
| `E-01` à `E-08` | Élément existant **non sondé** de la présente note (numérotation propre à `B-24`) — **`E-03` en est sorti à l'indice B** |
| **PARAMÉTRIQUE** | Mode de travail où la donnée manquante reste en **symbole** : on écrit la formule, on ne conclut pas |
| **NON CONTRACTUEL** | Mention apposée au tableau de sensibilité : une valeur testée n'est **jamais** une valeur retenue, et le tableau ne s'exécute pas |
| `f_k` | Résistance caractéristique de la maçonnerie en compression — **inconnue**, hypothèse `H-25` (`1,5 MPa`), clause `D-34` |
| `f_m,d` / `f_c,0,d` | Résistances de calcul du bois en flexion / en compression axiale (EC5) |
| `k_c` | Coefficient de flambement (EC5 § 6.3.2), fonction de l'élancement `lambda` |
| `b`, `h`, `L`, `e` | Largeur, hauteur, portée, entraxe — **symboles**, jamais renseignés ici |
| `M_Ed` / `V_Ed` / `N_Ed` | Moment, effort tranchant, effort normal **de calcul** (ELU) |
| `W` | Module d'inertie de flexion, `W = b h² / 6` pour une section rectangulaire |
| `gamma_M` | Coefficient partiel de matériau : `1,30` (bois), `2,50` (maçonnerie, `H-26`) |
| `k_mod` | Coefficient modificatif EC5 : `0,80` retenu pour la sensibilité (classe de service 2, longue durée) |
| `RDR` | **Registre des décisions et réserves** (`B-03`) : seul lieu où une valeur de repli peut être tranchée |
| `PARTIEL-DÉCLARÉ` | Mode où une valeur de repli est assumée **par décision écrite** — jamais par une note de calcul |
| `MAT-06` / `EXI-04` | Donnée manquante du cadrage : classe de bois / fiches de sondage des planchers |
| `ENC` / `PA-xx` | Existant non qualifié / point d'arrêt : prescription opposable, levée en fouille ou en dépose |
| `H-15`, `H-25`, `H-26` | Hypothèses du registre `B-03` : point d'arrêt sur les semelles, `f_k = 1,5 MPa`, `f_vk0 = 0,15 MPa` |

---

## 2. TABLEAU 1 — ÉLÉMENTS NON SONDÉS ET VÉRIFICATIONS SUSPENDUES

| Élément | Donnée manquante | Charge transmise (ELU) | Vérification à mener | Formule littérale | Brique de fermeture |
|---|---|---|---|---|---|
| **`E-01`** Murs de moellons porteurs (façades et refends) | `f_k`, épaisseur réelle, présence de chaînages | `sigma_d = 0,177 MPa` sous `P1-N` / `P1-S` (`177,1 kN/m²`, `B-21`) · `0,094 MPa` en moyenne sur les voiles · `N_ELU` max `217,7 kN` sous `P2` | Compression verticale | `sigma_d = N_Ed / A_inf <= f_d = f_k / gamma_M` | **`B-46`** |
| **`E-02`** Poutre maîtresse bois (désordre 3) | `b`, `h`, classe de bois (`MAT-06`), continuité, état | `p_ELU = 57,9 kN/m` (`R1`, `B-21`) · `L = 4,3 m` (`B-11`) → `M_Ed = 133,8 kN.m` · `V_Ed = 124,5 kN` | Flexion simple, cisaillement, flèche ELS | `sigma_m,d = M_Ed / (b h² / 6) <= f_m,d` avec `M_Ed = p_ELU L² / 8` | **`B-44`** (avec `R1` : `B-45`) |
| **`E-04`** Potelets de charpente (désordre 8) | Section, hauteur libre, classe, excentrement, contreventement | `N_Ed = (1,35 G + 1,5 Q) x e x L_trib = 7,3` à `23,5 kN` | Compression + flambement | `N_Ed / (k_c A f_c,0,d) <= 1` avec `lambda = L_cr / i` | **`B-44`** |
| **`E-05`** Ferme de charpente altérée (désordre 6) | Sections d'arbalétrier et d'entrait, classe, **section résiduelle après purge**, entraxe, contreventement | `p = 4,89` à `6,85 kN/m` sur `L = 9,90 m` (`D2` f. 02) → `M_Ed = 60,0` à `84,0 kN.m` | Flexion de l'arbalétrier (borne), puis compression + flambement | `sigma_m,d = p L² / 8 / (b h² / 6) <= f_m,d` puis `N_Ed / (k_c A f_c,0,d) <= 1` | **`B-44`** |
| **`E-06`** Pannes de couverture | Section, portée entre fermes, entraxe, classe | `p = 3,43` à `4,40 kN/m` sur `L = 3,20 m` → `M_Ed = 4,4` à `5,6 kN.m` | Flexion + flèche ELS | `sigma_m,d = p L² / 8 / (b h² / 6) <= f_m,d` | **`B-44`** |
| **`E-07`** Plancher haut portant la charpente par potelets (désordre 5) | **Nature du plancher** (bois / BA / hourdis), épaisseur, sens porteur, portée, sections et entraxes (`EXI-04` absent) | Réactions des potelets, **augmentées** par les renforts `B-44` (`E-04`) | Flexion du solivage + réaction d'appui — **non formulable en l'état** | **Indéterminée** : la nature du support commande la formule (EC5 si bois, EC2 si béton armé) | **`B-43`** |
| **`E-08`** Linteaux existants au-dessus des baies (désordre 1) | Section, matériau, portée libre, longueur d'appui, état | `p = 22 h + 10,51 = 28,1` à `54,5 kN/m` (`B-21` § 5) → `M_Ed = 2,5` à `16,4 kN.m` | Flexion, cisaillement, pression d'appui | `sigma_m,d = M_Ed / (b h² / 6) <= f_m,d` et `R / (a b) <= f_d` | **`B-49`** |

> **Aucune de ces sept lignes ne porte une valeur.** Les charges sont des **effets de charge** repris de `B-21` — elles ne dépendent pas de l'existant, elles viennent de notre projet. Les résistances, elles, sont absentes : elles sont les symboles `f_k`, `f_m,d`, `f_c,0,d`.

### 2.1 `E-03` — SORTI DU CHAMP EN INDICE B : LES DONNÉES EXISTENT

| Donnée | Valeur | Source |
|---|---|---|
| Section des solives | `8 x 18 cm` (`b = 80 mm`, `h = 180 mm`) | `D3` p. 10 · `EXI-01a` |
| Entraxe | `0,50 m` | `D3` p. 10 · `EXI-01a` |
| Portée | `2,77 m` | `D3` p. 10 (`B-00` § « Plancher A ») |
| Poutre porteuse | `20 x 15 cm`, portée `4,34 m` | `D3` p. 10 et 16 · `EXI-01b` |
| Complexe | lambourde + parquet `20 daN/m²` + lattis-plâtre `20 daN/m²` | `D3` p. 10 · `EXI-01e` |
| Classe de bois | `C18` — **hypothèse de calcul du diagnostic**, pas une mesure | `D3` p. 10 · `EXI-03` |
| **Inconnue restante** | **État sanitaire des abouts** et **périmètre de la recharge `15 cm`** | `D4` p. 5 et 14 |

**Contrôle de cohérence** (et non conclusion — la vérification appartient à `B-43`) : `W = b h² / 6 = 432 000 mm³`, `f_m,d (C18) = 0,80 x 18 / 1,30 = 11,08 MPa`.

| Scénario | `p_ELU` | `M_Ed` | `sigma_m,d` | `sigma / f_m,d` | Flèche ELS (court terme) |
|---|---|---|---|---|---|
| **Sans recharge** (RDC seulement) | `3,09 kN/m` | `2,96 kN·m` | `6,86 MPa` | **`0,619`** | `4,7 mm` (`L/300 = 9,2`) |
| **Avec recharge `15 cm`** (`B-21`) | `5,32 kN/m` | `5,10 kN·m` | `11,81 MPa` | **`1,066`** | `8,3 mm` |

> **Ce que ce tableau met en évidence — et qui n'est pas un détail de `B-24`.** Le sort de la solive `8 x 18` ne dépend **pas** d'une donnée manquante sur l'existant : il dépend d'une **lecture du `D4`**. Si la recharge de `15 cm` s'applique au plancher haut, la solive est **7 % au-delà** de sa résistance de calcul à `C18` — et la flèche à long terme (`k_def = 0,6`) sort de la limite. Si elle ne s'applique qu'au sol du RDC, la solive passe avec `38 %` de marge.
>
> **Aucun de ces deux cas n'est « retenu » ici.** `B-43` les tranche, et la réponse est une **décision `RDR`** — pas une hypothèse de calcul. La question est posée au § 9 (`R-24-B1`).

---

## 3. TABLEAU 2 — SENSIBILITÉ : **NON CONTRACTUEL — POUR INFORMATION**

> **NON CONTRACTUEL — POUR INFORMATION.** Les valeurs ci-dessous sont des **cas de sensibilité**, jamais des valeurs retenues. Elles servent à répondre à une seule question : *le verdict change-t-il à l'intérieur de la plage plausible ?* Elles ne doivent pas être reprises dans une note d'exécution, ni utilisées pour dimensionner un renfort.

**Plage balayée : 83 cas**, sur toute l'étendue des valeurs plausibles — sections possibles du bâti ancien et classes `C18` à `C24`. La plage est fixée par la **géométrie et les pratiques de l'époque**, jamais par le résultat.

Paramètres de sensibilité (eux aussi non contractuels) : `k_mod = 0,80` · `gamma_M = 1,30` (bois) · `gamma_M = 2,50` (maçonnerie, `H-26`) · `f_m,d = 11,08 MPa` (`C18`) et `14,77 MPa` (`C24`).

| Élément | Cas le plus défavorable de la plage | `sigma / f` ou `N / N_Rd` (min → max) | **Verdict (pour information)** |
|---|---|---|---|
| **`E-01`** Maçonnerie | `f_k = 0,5 MPa` | `0,177 → 0,885` | **FAVORABLE** — satisfaisant pour **toute** la plage |
| **`E-02`** Poutre maîtresse | `150 x 200` en `C18` | `3,020 → 12,081` | **DÉFAVORABLE** — insuffisant pour **toute** la plage |
| **`E-04`** Potelets | `80 x 80`, surface reprise `12,00 m²` | `0,142 → 1,046` | **LIMITE** — `k_c = 0,317`, `N_b,Rd = 22,5 kN` contre `N_Ed = 23,5 kN` |
| **`E-05`** Ferme | Arbalétrier `80 x 180`, entraxe `3,5 m`, `C18` | `3,524 → 17,541` | **DÉFAVORABLE** — insuffisant pour **toute** la plage |
| **`E-06`** Pannes | `80 x 120`, entraxe `2,25 m`, `C18` | `0,458 → 2,651` | **LIMITE** — passe en `120 x 180` seulement |
| **`E-07`** Plancher haut | — | — | **SANS PLAGE** — aucune borne posable sans connaître la nature |
| **`E-08`** Linteaux existants | `200 x 200`, `h = 2,00 m`, `L = 1,55 m`, `C18` | `0,066 → 1,108` | **LIMITE** — dépend de la hauteur de maçonnerie portée |

### 3.1 Ce que les trois verdicts veulent dire

| Verdict | Définition | Conséquence pour la suite |
|---|---|---|
| **FAVORABLE** | Satisfaisant pour **toute** la plage plausible | L'élément est **non critique** — indice fort, qui **reste non contractuel** |
| **LIMITE** | Satisfaisant pour une partie de la plage | L'élément est **critique** : le sondage est indispensable pour conclure |
| **DÉFAVORABLE** | Insuffisant pour **toute** la plage | Le renforcement est **acquis** ; le sondage dimensionne, il ne décide plus |

> **Ce que je refuse de faire.** Resserrer la plage autour de valeurs qui « passent ». Si `E-06` (pannes) ne passe qu'à `120 x 180` et `1,75 m` d'entraxe, cela ne dit pas que la panne mesure `120 x 180` : cela dit qu'aux petites sections elle ne passe pas, et qu'il faut aller mesurer. Le résultat utile d'une ligne n'est jamais la valeur basse, c'est **l'étendue**.
>
> **Ce que l'indice B corrige, exactement.** Pour `E-03`, la plage n'avait pas lieu d'être : l'entraxe et la portée étaient écrits dans le diagnostic depuis le premier jour. Une plage de sensibilité sur une donnée disponible, c'est du décor. `E-03` sort donc du tableau — et c'est la seule ligne que l'indice B retire.

---

## 4. TABLEAU 3 — ESSAIS ET SONDAGES NÉCESSAIRES POUR FERMER LA VÉRIFICATION

| Élément | Essai | Référentiel | Nombre | Emprise | Responsable | Échéance |
|---|---|---|---|---|---|---|
| **`E-07`** Plancher haut | **Sondage destructif** : ouverture, composition, sens porteur, portée, sections, entraxes | `NF EN 338` (bois) / `NF EN 1992` (BA) / `NF EN 15037` (hourdis) selon la nature | **3 ouvertures** de `0,50 x 0,50 m` | Plancher haut — un point par file de potelets | MOA / bureau mandaté | **AVANT `B-43` — priorité 1** |
| **`E-01`** Maçonnerie | Essais de **compression** sur carottes | `NF EN 1996-1-1` + `NF EN 1052-1` | **6 carottes** (2 murs × 3 points) | Façade Ouest et refend central, sur `2,00 m` de haut | **MOA** (`D-34` : hors mission, à sa charge) | avant `B-46` |
| **`E-01`** Maçonnerie | Essais de **cisaillement** (cohésion initiale `f_vk0`) | `NF EN 1052-3` / `NF EN 1052-4` | **3 éprouvettes** | Même emprise que les carottages | **MOA** (`D-34`) | avant `B-46` |
| **`E-02`** / **`E-05`** / **`E-06`** Charpente | Relevé **au mètre et au calibre** : sections, classes, état sanitaire | `NF EN 338` (classement visuel) + `NF EN 1995-1-1` | **1 relevé** couvrant 2 zones non relevées + combles | Intégralité des combles, plan de repérage | MOA / bureau mandaté | avant `B-44` |
| **`E-01`** Appuis neufs | **Ouverture de fouilles** au droit des appuis | `NF EN 1997-2` | **5 fouilles** (`P1-N`, `P1-S`, `P2`, `P3`, `J1`) | Au droit de chaque appui, jusqu'au niveau d'assise | **MOA** — point d'arrêt `H-15` | avant `B-40` |

> **Cinq campagnes, plus six.** L'indice A en listait six ; `E-03` en portait une à lui seul (sondage des planchers courants). Les entraxes, sections et portées de `A` et `B` étant écrits au diagnostic, cette campagne **n'a plus lieu d'être** : il ne reste à relever que l'**état des abouts**, à l'occasion de l'ouverture du plancher haut.
>
> **Le classement de `NF EN 338` ne remplace pas un essai de résistance.** Il donne une classe visuelle : c'est ce qui est commandable pour du bois ancien, et c'est suffisant pour `B-44` **si** l'état sanitaire le permet. Une ferme altérée (désordre 6) n'a pas de classe tant qu'elle n'est pas purgée.

---

## 5. TABLEAU 4 — IMPACT SUR LA CONCEPTION (`B-20`)

**Aucune valeur de repli n'est proposée par `B-24`.** Choisir de fonder sur une valeur plancher est une décision `RDR` en mode `PARTIEL-DÉCLARÉ`, pas une initiative de note de calcul. La colonne ci-dessous nomme la **nature** de la décision à prendre — jamais son contenu.

| Élément | Conséquence si la donnée reste manquante | Solution de repli possible (décision `RDR`) | Brique concernée |
|---|---|---|---|
| **`E-01`** Maçonnerie | `B-25` reste bâti sur `f_k = 1,5 MPa` (`H-25`) et `B-46` ne peut pas conclure sur les appuis | Décision `RDR` sur la valeur de `f_k` à opposer, ou exécution des essais `D-34` | `B-46` · `B-25` |
| **`E-02`** Poutre maîtresse | Le renfort `R1` (`2×UPE 200`) reste dimensionné sur une section supposée : son ampleur peut être insuffisante | Aucune valeur : la décision porte sur **le niveau de renfort à retenir par défaut** | `B-45` · `B-44` |
| **`E-03`** Solives `8 x 18` *(sorti du champ)* | **Ne dépend plus d'un sondage** mais du **périmètre de la recharge de `15 cm`** : `0,619` si elle ne s'applique pas au plancher haut, `1,066` si elle s'y applique | Décision `RDR` sur le **périmètre de la recharge** (`R-24-B1`), puis vérification en `B-43` | `B-43` |
| **`E-04`** Potelets | Le flambement reste non tranché ; `B-44` ne peut pas conclure sur les potelets que nos renforts chargent davantage | Décision `RDR` sur le **remplacement ou le chemisage** des potelets, ou relevé | `B-44` |
| **`E-05`** Ferme | La ferme reste non concluante, y compris après purge : renfort de ferme à dimensionner sans référence | Décision `RDR` sur le **principe de reprise** de la ferme (renfort vs dépose-repose) | `B-44` · `B-23` séquence `P-2` |
| **`E-06`** Pannes | Le dimensionnement des pannes reste non tranché ; la couverture ne peut pas être réceptionnée | Décision `RDR` sur le **remplacement systématique** des pannes, ou relevé | `B-44` |
| **`E-07`** Plancher haut | **Aucune formule** : la charge de toiture n'a pas de chemin de descente démontré jusqu'au sol (`V15`) | Décision `RDR` sur la **reprise directe de la charpente** par un sommier neuf, ou sondage | `B-43` · `B-44` |
| **`E-08`** Linteaux existants | Les linteaux qui deviennent porteurs sous `F1` et `R3` n'ont pas de capacité connue | Décision `RDR` sur le **remplacement systématique** par linteaux neufs, ou relevé | `B-49` · `B-45` |

---

## 6. LE CAS SANS PLAGE PLAUSIBLE — `E-07` ET LES DEUX ZONES NON RELEVÉES

La fiche prévoit ce cas : quand on ne connaît **ni la nature ni la fonction** d'un élément, aucune plage ne peut être posée, et une vérification littérale serait une fiction.

| Cas | Ce qui manque | Action prescrite |
|---|---|---|
| **`E-07`** Plancher haut | La **nature** du support (bois, BA, hourdis) — donc la formule elle-même | **Inspection visuelle puis sondage destructif**, avant toute tentative de calcul |
| **« ZONE NON RELEVEE » n° 1** | L'**emprise** n'est pas cotée sur `D2` f. 02 | Inspection visuelle + relevé de charpente ; aucune emprise reconstituée |
| **« ZONE NON RELEVEE » n° 2** | Idem | Idem |

> **Une emprise inventée serait pire qu'une emprise absente.** Elle ferait croire à une limite qu'on pourrait franchir. C'est la règle que `B-23` a posée et que `B-24` ne contredit pas.

---

## 7. SYNTHÈSE — SIX LIGNES

1. **Sept éléments en attente de données** (et non huit), aucun conclu : la note reste en mode PARAMÉTRIQUE et porte le suffixe `_P`.
2. **Un élément sorti du champ** : `E-03` (solives `8 x 18`) — ses données existent, la vérification passe à `B-43`.
3. **Un seul élément favorable pour toute la plage** : la maçonnerie en compression (`sigma_d / f_d <= 0,885` même à `f_k = 0,5 MPa`) — bonne nouvelle fragile, qui ne vaut **pas** pour le cisaillement, traité en `B-25`.
4. **Trois éléments limites** (`E-04` potelets, `E-06` pannes, `E-08` linteaux) : le sondage est indispensable pour trancher.
5. **Deux éléments défavorables pour toute la plage** (`E-02` poutre maîtresse `3,0 → 12,1` · `E-05` ferme `3,5 → 17,5`) : le renforcement est **acquis**, seule son ampleur dépend du relevé.
6. **Un élément sans plage plausible** (`E-07` plancher haut) et **deux zones non relevées** : inspection visuelle **avant** toute formule. **Essais à commander en priorité** : sondage du plancher haut (avant `B-43`), puis essais de maçonnerie `D-34` (avant `B-46`) ; à défaut, une décision `RDR` en `PARTIEL-DÉCLARÉ` — que cette note ne prend pas à votre place.

---

## 8. AUTO-CONTRÔLE — LES SEPT POINTS DU CRITÈRE D'ACCEPTATION

| # | Point du critère | Verdict | Preuve |
|---|---|---|---|
| 1 | Chaque élément non sondé a une vérification littérale écrite | ✅ | Tableau 1 — **7 éléments**, chacun avec sa formule ; `E-03` documenté au § 2.1 |
| 2 | Chaque donnée manquante est laissée en symbole | ✅ | `f_k`, `b`, `h`, `L`, `e`, `k_c` jamais renseignés ; `E-07` explicitement indéterminé |
| 3 | Le tableau de sensibilité est marqué « NON CONTRACTUEL — POUR INFORMATION » | ✅ | § 3 — mention en tête de tableau et en légende |
| 4 | Les essais sont listés avec référentiel, nombre et emprise | ✅ | Tableau 3 — **5 campagnes** (celle de `E-03` est sans objet) |
| 5 | Aucun élément n'est déclaré conclu | ✅ | Aucune conclusion ; verdicts de sensibilité uniquement |
| 6 | Aucun livrable exécutable n'est produit | ✅ | Filigrane « EN ATTENTE DE DONNÉES — NE PAS EXÉCUTER », suffixe `_P` |
| 7 | La note porte la mention de suspension | ✅ | En-tête + § 0 |

**Contrôle machine** : `_scripts/b24_existant.py` → **7/7 CONFORME**. Journal : `_rendus/b24_existant.txt` · résultats : `_rendus/b24_existant.json`.

> **Suspension.** La présente vérification est **SUSPENDUE** jusqu'à obtention des données du tableau 3. Elle se ferme par un sondage (retour en `B-43` / `B-44` / `B-46` / `B-49` en mode COMPLET), par une décision `RDR` de repli (mode `PARTIEL-DÉCLARÉ`), ou par un jugement documenté au registre pour un élément favorable sur toute la plage (`E-01`).

---

## 9. CE QUE CETTE BRIQUE TRANSMET

| Destinataire | Ce qui est transmis | Usage |
|---|---|---|
| **`B-03`** (RDR) | Les **6 campagnes d'essais** du tableau 3, avec responsable et échéance | Inscription en réserves `R-xx` |
| **`B-04`** (PTD) | Les 8 éléments en attente et le cas sans plage `E-07` | Intégration au plan de travail dégradé |
| **`T-04`** (prompt de demande) | Les essais à commander | Demande formelle à la MOA |
| **`B-43`** | `E-07` **et `E-03` en entrée directe** (données `D3` p. 10) | Planchers et plancher haut |
| **`B-44`** | `E-02`, `E-04`, `E-05`, `E-06` | Charpente et poutre maîtresse |
| **`B-46`** | `E-01` | Maçonnerie : appuis et compression |
| **`B-49`** | `E-08` | Linteaux existants |

### 9.1 Réserves nées de l'indice B

| Réf. | Objet | Conséquence si non levée | Destinataire |
|---|---|---|---|
| **`R-24-B1`** | **Périmètre de la recharge de sol `15 cm`** (`D4` p. 5 et 14) : s'applique-t-elle aux planchers hauts ou au seul sol du RDC ? | Solive `8 x 18` : `0,619` ou `1,066` selon la réponse — l'un passe, l'autre non | Décision `RDR` |
| **`R-24-B2`** | **État sanitaire des abouts** des solives `8 x 18` (la seule donnée réellement manquante) | À relever à l'ouverture du plancher haut ; ne bloque pas le calcul, bloque la réception | `B-43` |

### 9.2 Conformité aux règles universelles `V14` et `V15`

| Règle | Application |
|---|---|
| **`V14` — épuisement des pièces** | Aucun élément n'est déclaré « introuvable » sans que les pièces aient été consommées : `D2` f. 02 (charpente, zones non cotées), `D3` p. 3-8 et p. 18 (désordres, solives `8 x 18`), `D1` (aucune section bois), `D5` (épaisseurs de murs). La preuve d'épuisement est portée par `B-11` § 2 et `B-23` § 3 |
| **`V15` — continuité mécanique descendante** | `E-07` est le point où la chaîne se rompt : la charge de toiture passe par les potelets, puis par un plancher dont la nature est inconnue. Tant que `E-07` n'est pas sondé, **aucune discontinuité d'appui n'est compensée** et aucun ouvrage de transfert n'est dessiné — c'est signalé, pas masqué |
