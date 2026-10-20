# B-11 — AUDIT DU DIAGNOSTIC STRUCTURE EXISTANT

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-11** — Audit du diagnostic structure existant |
| Phase | 1 — Analyse |
| **Mode d'appel** | **PARTIEL-DÉCLARÉ** — prescriptions du diagnostic partiellement restituées |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Pièce auditée | **D3** — Diagnostic structure **EVEN**, 18 pages, visite du **20/02/2025**, rapport du **24/03/2025** |
| Entrées lues | B-00 ind. B · B-01 ind. B (DOC-05 **FOURNIE**) · B-02 ind. F · B-03 ind. F · note d'analyse du 19/10/2026 |
| Sortie | 4 tableaux + zones non relevées + 8 lignes de synthèse |
| Indice du livrable | **A** |
| Date | 19/10/2026 |
| Brique suivante | **B-12 (Audit géotechnique)** |

---

## 1. PÉRIMÈTRE ET RÈGLE DE LECTURE

**Trois niveaux sont distingués dans tout le document, et jamais mélangés dans une même cellule :**

| Niveau | Nature | Marqueur |
|---|---|---|
| **CITATION** | Ce que le diagnostic affirme, mot pour mot | *(réf. D3 p. x)* |
| **PRESCRIPTION** | Ce que le diagnostic préconise comme travaux | *[PRESCRIPTION DIAGNOSTIC — réf. p. x]* |
| **ANALYSE GO** | Ce que j'en conclus pour **nos** travaux | **[ANALYSE GO]** |

**Ce qui n'est pas restitué, et qui doit l'être dit.** Les neuf désordres sont établis avec leur nature, leur localisation et le préjudice retenu. En revanche, **les prescriptions propres du diagnostic par désordre ne sont pas restituées dans le corpus dépouillé** : la note d'analyse du 19/10/2026 décrit les renforts du **DCE indice C** (F1, R1-R3, S1), qui sont les prescriptions du **BET**, pas celles du diagnostic EVEN.

Cette distinction n'est pas une nuance de forme : **ce sont deux auteurs différents, qui engagent deux responsabilités différentes.** Elle fonde le point à lever n° 1.

**Folios établis** : la liste des désordres est citée **D3 p. 3-8**. Le folio individuel n'est établi que pour le **désordre 5 (D3 p. 6)**. Les autres sont marqués « folio non établi » plutôt que reconstitués.

---

## 2. TABLEAU 1 — DÉSORDRES ET ANALYSE GO

| N° | Nature du désordre — **CITATION** | Préjudice *(tel que cité)* | Localisation | Conséquence pour NOS travaux — **[ANALYSE GO]** | Prescription du diagnostic | Lot concerné |
|---|---|---|---|---|---|---|
| **1** | « Déformation de deux linteaux non porteurs » *(D3 p. 3-8)* | **Faible** | Façade Ouest | **[ANALYSE GO]** Un linteau non porteur déformé ne porte pas : le renfort F1 (2×HEA200) prévu au DCE le **change de statut** et le rend porteur. Nous exécuterions donc un ouvrage dont la charge n'est justifiée par aucun calcul amont. À valider en B-45 | Non restituée | **GO** (F1) |
| **2** | « Fissuration à mi-niveau des façades, à la jonction bois/brique » *(D3 p. 3-8)* | **Faible (esthétique) → risque d'infiltration** | Façades Est | **[ANALYSE GO]** Le diagnostic qualifie le préjudice d'esthétique ; il mentionne lui-même un risque d'infiltration. Une fissure à la jonction de deux matériaux est un **chemin d'eau** avant d'être un défaut visuel. Si elle n'est pas traitée, elle alimentera les désordres 4, 6, 7 et 8. **Interface de lot à trancher** : façades, hors structure | Non restituée | **Façades / second œuvre** — interface |
| **3** | « Fléchissement à vue d'œil de la poutre maîtresse » *(D3 p. 3-8)* | **Structurel** | Intérieur Est | **[ANALYSE GO]** C'est le désordre qui commande le renfort R1/R2/R3 et qui fixe l'étaiement. Une poutre 20×15 sur ~4,3 m donne L/h ≈ 29 : sous-dimensionnement d'origine, aggravé par le fluage. **La flèche est déjà consommée** : le renfort ne la reprend pas, il arrête son évolution. Le phasage d'étaiement et le niveau de reprise sont à définir en B-45 | Non restituée | **GO** (R1, R2, R3) |
| **4** | « Humidité et mousses au droit des descentes d'eaux pluviales » *(D3 p. 3-8)* | **Moyen → structurel à terme** | Façades | **[ANALYSE GO]** L'eau entre par la **zinguerie**, pas par le sol. Aucun renfort ne règle une descente EP bouchée. Ce désordre est **hors de notre lot** mais conditionne la durabilité de tous nos ouvrages bois | Non restituée | **Couverture / zinguerie** — interface |
| **5** | « Fissures en plafond du plancher haut étage, qui reprend la charpente par potelets » *(D3 p. 6)* | **À surveiller** | Intérieur | **[ANALYSE GO]** Le plancher haut n'est pas un plancher : c'est un **plafond portant la charpente par potelets**. Toute reprise de charge de toiture (B-44) transite par lui. Aucune fiche de sondage n'existe (EXI-04) : nous ne connaissons ni sa composition ni sa portée | Non restituée | **GO** (B-43) + charpente |
| **6** | « Ferme de charpente altérée par l'humidité » *(D3 p. 3-8)* | **Structurel** | Combles | **[ANALYSE GO]** Une ferme altérée a perdu de la section **et** de la classe de bois. Le renforcement prévu au DCE (renfort de ferme traditionnelle + contrefiches) suppose une matière saine sur laquelle s'appuyer. **Purge et traitement d'abord, renfort ensuite** — l'ordre inverse transfère la charge sur du bois mort. Classe de bois à établir (MAT-06) | Non restituée | **GO** partiel / **charpente hors CCTP (C-07)** |
| **7** | « Traces d'humidité intérieures, salle d'eau et menuiseries » *(D3 p. 3-8)* | **Faible → moyen** | Intérieur | **[ANALYSE GO]** Relève de l'étanchéité et de la ventilation, pas de la structure. Mais une salle d'eau à créer (programme D4) aggravera l'exposition : le **calepinage des ouvrages neufs** doit éviter d'encastrer de l'acier dans une zone humide active | Non restituée | **Second œuvre / fluides** — interface |
| **8** | « Chevrons très altérés, potelets théoriquement instables » *(D3 p. 3-8)* | **Structurel** | Charpente Est | **[ANALYSE GO]** « Théoriquement instables » est une **hypothèse de calcul**, pas un constat : le diagnostic n'a pas vérifié le flambement. Nos renforts vont **augmenter** les charges sur ces potelets. À vérifier impérativement en B-44, avec la classe de bois réelle | Non restituée | **GO** partiel / **charpente hors CCTP (C-07)** |
| **9** | « Doublage lattis-plâtre fissuré, chevrons visibles » *(D3 p. 3-8)* | **Flèche + infiltrations** | Intérieur | **[ANALYSE GO]** Le lattis fissuré est le **symptôme visible** de la flèche du désordre 3, pas un désordre indépendant. Le traiter sans traiter la poutre revient à replâtrer un mouvement qui continue | Non restituée | **Second œuvre** — interface |

**Ce que le tableau montre.** Sept désordres sur neuf touchent nos ouvrages, directement ou par interface. **Deux seulement (3 et 5) sont des désordres de structure pure** ; les autres sont des **causes** — eau, façades, charpente — qui produiront des désordres structurels si elles ne sont pas traitées avant nos renforts.

---

## 3. TABLEAU 2 — PRESCRIPTIONS DU DIAGNOSTIC REPRISES

| N° désordre | Prescription citée | Ce que cette prescription implique pour nos ouvrages | Briques CARNAC à exécuter pour la valider |
|---|---|---|---|
| **1** | **[PRESCRIPTION DIAGNOSTIC — non restituée]** — le DCE indice C prescrit F1 (2×HEA200) en renfort du linteau bois *(D2 f. 01)* | Le linteau passe de non porteur à porteur : charge à justifier, appuis à vérifier | **B-45** *(à valider par nos calculs)* |
| **3** | **[PRESCRIPTION DIAGNOSTIC — non restituée]** — le DCE prescrit R1 (2×UPE200), R2 (HEB160), R3 (UPE200) *(D2 f. 01)* | Moisage d'une poutre déjà fléchie : étaiement, reprise de flèche, cisaillement aux abouts, assemblage bois/acier | **B-45** *(à valider par nos calculs)* |
| **6** | **[PRESCRIPTION DIAGNOSTIC — non restituée]** — le DCE prescrit le renfort de la ferme traditionnelle et l'ajout de contrefiches *(D2 f. 02)* | Renfort sur bois altéré : purge préalable obligatoire, classe de bois à établir | **B-44, B-22** *(à valider par nos calculs)* |
| **8** | **[PRESCRIPTION DIAGNOSTIC — non restituée]** — le DCE prescrit une demi-ferme en sous-œuvre et l'ajout de pannes *(D2 f. 02)* | Stabilité des potelets à vérifier au flambement **avant** d'augmenter leur charge | **B-44** *(à valider par nos calculs)* |
| **—** (fondations) | **[PRESCRIPTION DIAGNOSTIC — non restituée]** ; le diagnostic décrit le système de fondations comme **inconnu** *(D3 p. 2)* | Aucune base pour dimensionner la reprise en sous-œuvre : c'est **R-31bis / V-26** | **B-40** *(à valider par nos calculs)* |

> **Aucune de ces prescriptions n'est reprise à notre compte.** Toutes sont marquées « à valider par nos calculs ». Un diagnostic de BET tiers n'est pas un visa : il engage l'entreprise qui l'exécute, pas celui qui l'a écrit.

---

## 4. TABLEAU 3 — DONNÉES MANQUANTES POUR NOS TRAVAUX

| Donnée (code CARNAC) | Ce que le diagnostic aurait dû fournir | Impact sur nos calculs | Brique concernée |
|---|---|---|---|
| **EXI-04** — fiches de sondage des planchers | Composition, épaisseur, portée du plancher haut (désordre 5) | B-43 ne peut pas vérifier un plancher dont il ignore la constitution | **B-24, B-43** |
| **EXI-05 / MAT-07** — résistance de la maçonnerie | Contrainte admissible des moellons et du mortier | Aucune vérification possible des appuis et des jambages | **B-23, B-46** |
| **EXI-01g** — sections de charpente | Sections réelles des pannes, fermes, chevrons, potelets | « Deux zones non relevées » au folio 02 ; sans sections, pas de vérification | **B-44** |
| **MAT-06** — classe de bois | Essence, classe, état sanitaire | Une ferme altérée (désordre 6) n'a pas de classe : le calcul est indéterminé | **B-44, B-50** |
| **MAT-12** — chaînages existants | Présence, position, continuité | Aucun chaînage relevé ni représenté : la stabilité d'ensemble de la maçonnerie n'est pas démontrable | **B-46** |
| **GEO-01** — cote d'ensemble | Dimensions du bâtiment | Impossible de coter un plan d'exécution | **B-43, B-44, B-60** |
| **DOC-08** — DOE / récolement | Géométrie d'origine, plans de structure | L'existant est décrit, pas mesuré | **B-11** *(cette brique)*, **B-60** |
| **SOL-04** — coupe de sol | Nature des couches sous l'assise | Voir B-12 | **B-40** |
| **MAT-08** — classe de service du bois | Exposition des bois (humide ?) | Les désordres 4, 6, 7, 8 imposent de trancher : classe 1 ou 2 | **B-22, B-44** |

---

## 5. ZONES NON RELEVÉES ET EMPRISE

| Zone | Emprise | Source | Conséquence |
|---|---|---|---|
| **« ZONE NON RELEVEE » n° 1** | **Emprise non établie** — non cotée sur le folio | **D2 folio 02** (charpente) | Toute vérification de charpente sur cette zone reposerait sur une hypothèse non déclarée |
| **« ZONE NON RELEVEE » n° 2** | **Emprise non établie** — non cotée sur le folio | **D2 folio 02** (charpente) | Idem |
| **Combles** | Non couverts par une reconnaissance visuelle exhaustive | D3 p. 3-8 | Les désordres 6 et 8 sont constatés **sans** lever de doute sur l'ensemble de la charpente |
| **Fondations** | **Intégralement non relevées** | D3 p. 2 : système « inconnu » | Aucune donnée de niveau, de largeur ni d'état — **R-31bis** |
| **Planchers** | Aucun sondage, aucune ouverture | D3 | Le plancher haut porte la charpente : c'est le point aveugle le plus lourd |

**Aucune de ces emprises n'est reconstituée par moi.** Elles sont déclarées non établies, ce qui est la seule formulation honnête : une emprise inventée serait pire qu'une emprise absente.

---

## 6. CE QUE LES DÉCISIONS DU 19/10/2026 CHANGENT À CET AUDIT

**D-16 (absence de nappe) ne règle aucun des désordres d'humidité — et il faut le dire.** Quatre désordres (4, 6, 7, 8) et une partie du 9 proviennent de l'**eau qui tombe** : descentes EP, couverture, zinguerie, étanchéité de salle d'eau. Ce n'est pas l'eau du sol. **Supprimer la nappe supprime un risque de fondation, pas un risque de charpente.** Les deux eaux sont indépendantes, et le raisonnement inverse — « plus de nappe, donc plus d'humidité » — serait une faute de lecture.

**D-14 (60 × 60 minimum) aggrave ponctuellement le risque de déchaussement.** Une semelle de 60 cm de côté au droit d'un soubassement existant ouvre une fouille **5,76 fois plus large** qu'une semelle de 25 cm. Le DCE prescrit de conserver « le débord de semelle apparent » : la marge de sécurité autour de l'existant se réduit d'autant. **[ANALYSE GO]** C'est un point de **mode d'exécution** à porter en B-40 et au plan de coffrage : passes alternées, étaiement, distance minimale à l'existant.

**D-15 (tassements hors mission) laisse un vide qu'il faut nommer.** Les désordres 1, 3 et 5 sont, pour partie, des **mouvements différentiels** déjà consommés — flèche de poutre, fissures de plafond, linteaux déformés. En sortant les tassements du périmètre, on renonce à vérifier que nos fondations neuves n'en ajouteront pas. La règle de nivellement de D-09 en limite l'effet, elle ne le vérifie pas.

---

## 7. SYNTHÈSE — HUIT LIGNES

- **Impact maximal** : désordre 3 (poutre maîtresse, préjudice structurel) commande R1/R2/R3, l'étaiement et le phasage.
- **Impact maximal** : désordre 8 (potelets « théoriquement instables ») — nos renforts **augmentent** leur charge sans que le flambement ait été vérifié.
- **Impact maximal** : désordre 6 (ferme altérée) — renforcer du bois mort est un transfert de charge, pas un renfort.
- **Insuffisance pour nos calculs** : aucune section de charpente, aucune classe de bois, aucune fiche de plancher — trois données sans lesquelles B-44 et B-43 sont indéterminées.
- **Insuffisance pour nos calculs** : le diagnostic qualifie les fondations d'« inconnues » et s'arrête là.
- **Interfaces à trancher** : charpente **hors CCTP** alors que deux désordres structurels y siègent ; façades et zinguerie hors lot mais causes directes.
- **Interface à trancher** : le plancher haut porte la charpente par potelets — il relève de notre lot et n'a jamais été sondé.
- **Conclusion** : l'audit est exploitable, mais **aucun renfort ne peut être exécuté avant purge des bois et validation par nos calculs**.

---

## 8. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-11) | État | Observation |
|---|---|---|
| Chaque désordre est numéroté et cité à sa source | ✅ | **9 désordres**, cités D3 p. 3-8 ; folio individuel établi pour le n° 5 (p. 6), « non établi » ailleurs |
| Chaque cellule du tableau 1 distingue CITATION et ANALYSE GO | ✅ | Deux colonnes séparées ; **aucune cellule ne mélange** les deux niveaux |
| Chaque prescription reprise est marquée « à valider par B-xx » | ✅ | Tableau 2, colonne dédiée ; **aucune prescription n'est reprise à notre compte** |
| Les données manquantes sont rattachées à leur code et à leur brique | ✅ | **9 données**, codes CARNAC et briques renseignés |
| Les zones non relevées sont identifiées avec leur emprise | ✅ **avec réserve** | **5 zones**, emprises déclarées **non établies** — aucune n'est inventée |
| Aucun renforcement n'a été proposé par moi | ✅ | Aucune section, aucun profilé, aucun dimensionnement |
| La synthèse tient en 8 lignes | ✅ | **8 lignes** exactement |

**Écart signalé (V4)** : les **prescriptions propres du diagnostic** ne sont pas restituées dans le corpus dépouillé. Le tableau 2 les référence comme « non restituée » plutôt que de les reconstituer. C'est un **PARTIEL-DÉCLARÉ**, pas un COMPLET.

**Placeholders résiduels (V7)** : aucun.

---

## 9. POINT DE CONTRÔLE HUMAIN

1. **Prescriptions du diagnostic** : acceptez-vous que B-11 soit exploité avec des prescriptions marquées « non restituées », ou faut-il obtenir les **folios de prescriptions** de D3 avant B-13 ?
2. **Charpente hors CCTP** : les désordres 6 et 8 sont structurels et la charpente n'est pas au marché. Confirmez-vous que notre lot s'arrête aux **appuis** et que les bois relèvent d'un autre lot — ou faut-il l'ouvrir ?
3. **Ordre d'intervention** : je retiens que la **purge et la mise hors d'eau précèdent** tout renfort. Confirmez-vous cet ordre, ou souhaitez-vous renforcer d'abord et traiter ensuite ?
4. **Zones non relevées** : les deux zones du folio 02 n'ont pas d'emprise cotée. Faut-il les faire relever par géomètre avant B-44 ?

---

*Brique B-11, **indice A**, livrée en mode **PARTIEL-DÉCLARÉ**.*

*Aucune brique aval engagée : **B-12 (Audit géotechnique)** attend un GO.*
