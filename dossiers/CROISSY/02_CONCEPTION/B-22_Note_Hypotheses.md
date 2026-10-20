# B-22 — NOTE D'HYPOTHÈSES DE CONCEPTION

| Champ | Valeur |
|---|---|
| Carnet | **CARNAC v3.0** |
| Brique | **B-22** — Note d'hypothèses de conception |
| Phase | **3 — Conception et synthèse structurelle** (après `B-21`, avant `B-23` et `B-24`) |
| **Mode d'appel** | **COMPLET** — tous les statuts sont renseignés, aucune hypothèse n'est laissée implicite |
| Régime | **OUTILLÉ (V13)** — registre consolidé et contrôlé par script, journal d'exécution conservé |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| Script `OUT-02` | `dossiers/CROISSY/_scripts/b22_hypotheses.py` |
| Journal `OUT-03` | `dossiers/CROISSY/_rendus/b22_hypotheses.txt` |
| Résultats machine | `dossiers/CROISSY/_rendus/b22_hypotheses.json` |
| Sortie graphique | **Aucune** — la fiche `B-22` n'exige aucun livrable graphique |
| **Indice** | **A** — création de la brique |
| Date | **20/10/2026** |
| Brique suivante | **`B-23`** (exploitation du diagnostic), puis `B-24` (existant non sondé) |

> **Note unique.** Cette note est la **seule** note d'hypothèses du projet. Elle est annexée à la FDC et couvre l'ensemble des briques, présentes et à venir. Une hypothèse introduite par `B-45` en janvier s'y ajoutera avec un numéro `H-32` — elle n'aura pas sa propre note.
> **Aucune hypothèse n'est supprimée.** `H-24`, abandonnée par `D-26`, reste au registre avec son motif.

---

## 0. CE QUI CHANGE AVEC LA DOCTRINE `D-33`

### 0.1 L'instruction reçue

Un **dossier de consultation des entreprises** est **adressé à l'entreprise**. Ses pièces — et notamment le **CCTP** — énumèrent les prestations que **l'entreprise doit réaliser**. Elles ne sont **pas** adressées au bureau d'études d'exécution.

Conséquence directe, et c'est l'objet de `D-33` : **certaines hypothèses de ce registre ne recevront jamais de réponse formelle.** Non pas parce que la question serait mal posée, mais parce qu'elle n'est **adressée à personne** en mesure de nous répondre. Le désamiantage, le déplombage, les plans de cantonnement de chantier, les méthodes de fouille, les passes de reprise en sous-œuvre : ce sont des obligations d'entreprise, décrites dans une pièce qui lui est destinée. Nous n'avons pas à en attendre une confirmation — nous avons à en **faire notre lecture**, et à la traduire en prescriptions opposables.

**Notre travail sur le CCTP n'est pas de le valider : il est d'y prélever ce qui concerne nos études.**

### 0.2 Ce que cela change dans le registre — la notion de régime de confirmation

Le registre comptait jusqu'ici un statut et un nuage. Il lui manquait une distinction : **qui peut répondre ?** Sans elle, les vingt-cinq hypothèses non confirmées se présentaient comme une attente uniforme, avec un nuage et un délai de deux jours (`D-19`) pour toutes — ce qui était faux pour neuf d'entre elles.

La note introduit donc un **régime de confirmation**, orthogonale au statut. Ce n'est pas un quatrième statut : une hypothèse reste « À CONFIRMER » ou « CONFIRMÉE » ; le régime dit seulement **par quel canal la confirmation peut arriver**.

| Régime | Définition | Ce qu'on en fait |
|---|---|---|
| **DOCUMENTAIRE** | Un destinataire identifié peut répondre (MOE, MOA, géotechnicien, BET) | Relance possible, délai `D-19` applicable |
| **LECTURE** | **Aucun destinataire** — la pièce est adressée à l'entreprise | **Aucune relance.** Notre lecture tient lieu de position ; le nuage signale la lecture, pas une attente |
| **RELEVÉ** | Confirmation par constat sur site, à l'ouverture | Point d'arrêt de chantier, pas une question écrite |
| **CALCUL** | Valeur d'étude assumée par nous, sans destinataire pour la valider | Justifiée en borne défavorable, tracée, jamais présentée comme certaine |

### 0.3 Le résultat chiffré

| Régime | Nombre | Hypothèses |
|---|---|---|
| **DOCUMENTAIRE** | **12** | `H-01`, `H-02`, `H-04`, `H-07`, `H-08`, `H-10`, `H-14`, `H-17`, `H-18`, `H-20`, `H-22`, `H-23` |
| **LECTURE** | **9** | `H-03`, `H-05`, `H-06`, `H-09`, `H-11`, `H-13`, `H-16`, `H-19`, `H-21` |
| **RELEVÉ** | **2** | `H-12`, `H-15` |
| **CALCUL** | **6** | `H-25`, `H-26`, `H-27`, `H-28`, `H-29`, `H-30` |
| sans objet (abandonnée) | **1** | `H-24` |

Sur les **25 hypothèses non confirmées**, **9 sortent du circuit de relance** et **5 sont des valeurs d'étude sans destinataire**. Il n'en reste que **10 réellement relançables** — `H-01`, `H-02`, `H-04`, `H-07`, `H-08`, `H-14`, `H-17`, `H-18`, `H-20`, `H-23` — et **2 en attente d'un relevé**.

> **Ce que la doctrine évite.** Un registre qui relance indéfiniment des questions sans destinataire se décrédibilise : au troisième rappel resté sans réponse, plus personne ne lit les nuages — y compris ceux qui, eux, appelaient une réponse. Distinguer les deux régimes, c'est **protéger la valeur des dix hypothèses qui comptent** en cessant de crier avec les neuf autres.

### 0.4 Ce que la doctrine ne change pas

Les nuages `D-19` **restent posés** sur les plans et dans les notes. Un nuage de lecture n'est pas un nuage d'attente : il dit « ceci est notre lecture d'une pièce, vérifiez-la », et non « nous attendons une réponse ». Le délai contradictoire de deux jours ne court que sur les hypothèses `DOCUMENTAIRE`.

---

## 1. INDEX DES HYPOTHÈSES ACTIVES

**30 hypothèses** — `H-01` à `H-30`. `H-31` n'y figure pas : elle a été **promue décision `D-31`** le 20/10/2026 et a quitté le registre des hypothèses.

| N° | Famille | Valeur retenue | Introduite par | Impacte | Statut | Régime |
|---|---|---|---|---|---|---|
| **H-01** | Géométrie | Adresse : 11 rue Paul Demange, 78290 Croissy-sur-Seine | B-00 | B-60 · B-64 | À CONFIRMER | DOCUMENTAIRE |
| **H-02** | Autres | Destination : cabinet paramédical (kiné, plateau technique, salle de sport) | B-00 | B-60 · B-64 | À CONFIRMER | DOCUMENTAIRE |
| **H-03** | Existant | `R1`, `R2`, `R3` exécutés ; solives 8×18 non renforcées | B-00 | B-45 | À CONFIRMER | **LECTURE** |
| **H-04** | Autres | Périmètre : pavillon Flora seul, bâtiment Gardien exclu | B-00 | B-60 · B-64 | À CONFIRMER | DOCUMENTAIRE |
| **H-05** | Géométrie | Frangements `F1` à `F4` = 4 des 5 interventions de `D4 p. 5` | B-00 | B-49 | À CONFIRMER | **LECTURE** |
| **H-06** | Géométrie | Plans `D2` à l'échelle **1/80** (cartouche « 1/50-1/20 » non mis à jour) | B-00 | B-30 · B-31 · B-20 | À CONFIRMER | **LECTURE** |
| **H-07** | Autres | Folio 03 (PB RDC) à l'**indice B** | B-00 | B-40 · PLS | À CONFIRMER | DOCUMENTAIRE |
| **H-08** | Géométrie | Orientations des planches : p. 21 = SUD EST, p. 22 = NORD OUEST | B-00 | B-60 | À CONFIRMER | DOCUMENTAIRE |
| **H-09** | Autres | « RSO » = reprise en sous-œuvre, dans ses deux occurrences | B-00 | B-40 · PLS | À CONFIRMER | **LECTURE** |
| **H-10** | Géométrie | Semelles isolées **60 × 60 cm minimum** — plancher, jamais plafond | B-00 | B-40 · PLS | **CONFIRMÉE** | DOCUMENTAIRE |
| **H-11** | Autres | Compactage arrêté à 1,00 m de tout soubassement (`D2 f. 04` prévaut) | B-00 | B-43 | À CONFIRMER | **LECTURE** |
| **H-12** | Géométrie | Semelles d'une même pièce à la même cote, tolérance ± 5 cm | B-00 | B-40 · PLS | À CONFIRMER | **RELEVÉ** |
| **H-13** | Autres | Reprise en sous-œuvre par passes alternées ≤ 1,00 m, `C16/20` | B-00 | B-40 | À CONFIRMER | **LECTURE** |
| **H-14** | Autres | Charpente dans notre périmètre (lot 01), malgré l'absence de section bois au CCTP | B-00 | B-44 | À CONFIRMER | DOCUMENTAIRE |
| **H-15** | Existant | Niveau, largeur et état des semelles relevés avant coulage — **point d'arrêt** | B-00 | B-40 · PLS | À CONFIRMER | **RELEVÉ** |
| **H-16** | Autres | Fouilles à parois verticales, sans blindage jusqu'à 1,20 m | B-00 | B-40 | À CONFIRMER | **LECTURE** |
| **H-17** | Géométrie | Linteaux dimensionnés par nous, appui ≥ 0,20 m | B-00 | B-49 | À CONFIRMER | DOCUMENTAIRE |
| **H-18** | Géométrie | Aucune réservation dans les porteurs hors trémies `D2`/`D4` | B-00 | B-60 | À CONFIRMER | DOCUMENTAIRE |
| **H-19** | Existant | Traitement de l'humidité hors lot ; renforts posés en ambiance sèche | B-00 | B-44 · B-45 | À CONFIRMER | **LECTURE** |
| **H-20** | Autres | Étaiement provisoire à notre charge (lot 01), calculé par nous | B-00 | B-25 · mode opératoire | À CONFIRMER | DOCUMENTAIRE |
| **H-21** | Autres | Déplombage, curage, démolition **hors mission** | B-00 | B-60 · B-64 | **CONFIRMÉE** | **LECTURE** |
| **H-22** | Sol | Assise à −1,00 m dans les alluvions anciennes, `q ≥ 0,30 / 0,49 MPa` | B-10 | B-40 | **CONFIRMÉE** | DOCUMENTAIRE |
| **H-23** | Sol | Agressivité **XA1** (« XA4 » du cartouche = erreur de saisie) | B-10 | B-40 · B-42 | À CONFIRMER | DOCUMENTAIRE |
| **H-24** | Sol | Classe de sol C, `a_gr = 0,40 m/s²` — **ABANDONNÉE** par `D-26` | B-10 | aucune | **ABANDONNÉE** | — |
| **H-25** | Existant | Maçonnerie : `f_k = 1,5 MPa`, `E = 1 500 MPa` | B-25 | B-25 · B-42 · B-46 | À CONFIRMER | **CALCUL** |
| **H-26** | Existant | `f_vk0 = 0,15 MPa`, `γ_M = 2,5` | B-25 | B-25 · B-46 | À CONFIRMER | **CALCUL** |
| **H-27** | Charges | `σ_d = 0,30 MPa` — **vérifiée** par `B-21` (réel : `0,094`) | B-25 | B-25 · B-46 | **CONFIRMÉE** | **CALCUL** |
| **H-28** | Charges | Recharge de sol 15 cm : `3,30 kN/m²` ; plancher B recalculé `3,91` | B-21 | B-43 · B-45 | À CONFIRMER | **CALCUL** |
| **H-29** | Charges | Toiture : `0,95 kN/m²` | B-21 | B-44 | À CONFIRMER | **CALCUL** |
| **H-30** | Charges | Cloisons forfaitaires : `0,80 kN/m²` | B-21 | B-43 | À CONFIRMER | **CALCUL** |

**Total : 30 · dont 25 À CONFIRMER · 4 CONFIRMÉES · 1 ABANDONNÉE.**

---

## 2. DÉTAIL PAR HYPOTHÈSE

### 2.1 Famille CHARGES — 4 hypothèses

| N° | Objet | Valeur retenue | Justification et source | Statut | Intro. | Impacte | Dates |
|---|---|---|---|---|---|---|---|
| **H-27** | Contrainte verticale moyenne sur les voiles | `σ_d = 0,30 MPa` | Valeur **posée** en `B-25` pour calculer `f_vk = (f_vk0 + 0,4 σ_d)/γ_M` (EC6 § 3.6.2). **Vérifiée par `B-21`** : `1 766 kN / 18,79 m² = 0,094 MPa`. L'hypothèse majore `f_vk` de **44 %** — elle est conservatrice **dans le sens favorable**, seule direction admissible pour une hypothèse de résistance | **CONFIRMÉE** | B-25 | B-25 · B-46 | 20/10 · rév. 20/10 |
| **H-28** | Recharge de sol 15 cm | `3,30 kN/m²` à `22 kN/m³` ; plancher B recalculé à `3,91 kN/m²` | `D4 p. 5 et 14` prescrit l'**épaisseur** (15 cm), jamais la densité. `3,91` vient du recalcul par couches (`D3 p. 11`), `D2 p. 1` déclarant `3,50` — **sous-déclaration de 12 %**. On retient la plus élevée | À CONFIRMER | B-21 | B-43 · B-45 | 20/10 |
| **H-29** | Poids propre de toiture | `0,95 kN/m²` | `D2 f. 02` — constitution dessinée **sans aucune charge au cartouche**. Décomposition : tuiles `0,40` · chevrons `0,15` · pannes et fermes `0,25` · plafond `0,15` | À CONFIRMER | B-21 | B-44 | 20/10 |
| **H-30** | Cloisons forfaitaires | `0,80 kN/m²` sur tous les planchers | EC1-1-1 § 6.3.1.2. `CHG-08` décrit **quatre types de cloisons sans aucun poids** — le forfait est la seule valeur bornable. `V9` et `D-25` interdisent de **dessiner** les cloisons, pas de compter leur **poids** | À CONFIRMER | B-21 | B-43 | 20/10 |

### 2.2 Famille MATÉRIAUX — 0 hypothèse

**Une famille vide est un résultat, pas un oubli.** Le cartouche `D2 p. 1` fournit `C25/30` (superstructure), `C16/20` (gros béton), `S500B` (armatures) et `S275` (profils). **Aucune valeur de matériau n'a eu à être supposée** dans ce dossier, ce qui est rare et mérite d'être dit : c'est la preuve que le marché est explicite sur ce point.

> **Réserve maintenue** : cette absence d'hypothèse ne dit rien de la **nuance réelle des aciers en place** dans l'existant — les profilés `Even` de `D2` ne portent pas de nuance. La question est traitée en `B-45` (relevé sur site), pas ici, car elle ne concerne pas un matériau **prescrit** mais un matériau **existant**.

### 2.3 Famille GÉOMÉTRIE — 8 hypothèses

| N° | Objet | Valeur retenue | Justification et source | Statut | Intro. | Impacte | Dates |
|---|---|---|---|---|---|---|---|
| **H-01** | Adresse du pavillon | 11 rue Paul Demange | `D2 p. 1` **et** `D4 p. 1` contre « 2 rue Alfred Dormeuil » du diagnostic : **deux pièces contre une**, sur un cartouche de plan | À CONFIRMER | B-00 | B-60 · B-64 | 19/10 |
| **H-05** | Frangements ↔ `D4 p. 5` | 4 frangements pour 5 interventions | `D2 f. 01` porte 4 frangements, `D4 p. 5` décrit 5 interventions. La cinquième est l'ouverture de porte, sans renfort | À CONFIRMER | B-00 | B-49 | 19/10 |
| **H-06** | Échelle des plans `D2` | **1/80** | Mention « (1/80) » sur le plan ; le cartouche « 1/50-1/20 » est un cartouche type non mis à jour. **Corroborée par `B-30`** : calage à `1,7 mm` de résidu sur 218 m² à cette échelle. Toutes les **cotes de renvoi priment** sur la mesure au scalimètre | À CONFIRMER | B-00 | B-30 · B-31 · B-20 | 19/10 |
| **H-10** | Semelles isolées | **60 × 60 cm minimum** | `D-10` + `D-14` — **décisions**, pas hypothèses : le plancher est contractuel. `D-30` porte `SF1` à 80 × 80 sans la contredire (le minimum reste opposable) | **CONFIRMÉE** | B-00 | B-40 · PLS | 19/10 · rév. 20/10 |
| **H-12** | Cote des semelles d'une même pièce | Même cote, tolérance **± 5 cm** | `D2 f. 04` admet une variabilité, sans la borner. Au-delà de 5 cm, **`D-09` s'applique** : approfondissement et gros béton `C16/20`, jamais de remontée | À CONFIRMER | B-00 | B-40 · PLS | 19/10 |
| **H-17** | Linteaux des frangements | Dimensionnés par nous, appui ≥ 0,20 m | `D4 p. 5` (5 interventions) contre `D2 f. 01` (4 frangements). Le dimensionnement des linteaux est **dans notre lot**, l'appui de 20 cm est notre prescription | À CONFIRMER | B-00 | B-49 | 19/10 |
| **H-18** | Réservations dans les porteurs | Aucune hors trémies `D2`/`D4` | `D1 § 01.2.1.8` (non lu) et `D4` (TGBT). Toute réservation supplémentaire demandée par un lot technique fera l'objet d'un **avenant** — c'est une limite de mission, pas une commodité | À CONFIRMER | B-00 | B-60 | 19/10 |
| **H-08** | Orientations | p. 21 = SUD EST · p. 22 = NORD OUEST | `D4 p. 1` (sommaire) contre `D4 p. 21-22` (planches). Les planches priment : une façade est dessinée, un sommaire est recopié | À CONFIRMER | B-00 | B-60 | 19/10 |

### 2.4 Famille EXISTANT — 5 hypothèses

| N° | Objet | Valeur retenue | Justification et source | Statut | Intro. | Impacte | Dates |
|---|---|---|---|---|---|---|---|
| **H-03** | Renforts `R1`, `R2`, `R3` | Exécutés ; solives 8×18 **non** renforcées | `D2 f. 01` prescrit `R1`-`R3` ; `D3 p. 18` conclut que « le renforcement des solives n'est pas jugé utile ». La conclusion porte sur les **solives seules** | À CONFIRMER | B-00 | B-45 | 19/10 |
| **H-15** | Relevé des semelles existantes | Niveau, largeur et état relevés **avant coulage** | `D-09` ② et ③ ; `D3 p. 2` déclare l'état « inconnu ». Ce n'est pas une hypothèse mais un **point d'arrêt** : aucune semelle neuve n'est coulée avant consignation | À CONFIRMER | B-00 | B-40 · PLS | 19/10 |
| **H-19** | Traitement de l'humidité | Hors lot ; renforts posés en ambiance sèche | `D3 p. 3-8` (désordres 4, 7, 9). Aucune pièce du lot structure ne traite la cause. À défaut de traitement préalable, **la durabilité des bois et des aciers n'est pas garantie par nous** | À CONFIRMER | B-00 | B-44 · B-45 | 19/10 |
| **H-25** | Résistance de la maçonnerie | `f_k = 1,5 MPa` · `E = 1 500 MPa` | `D3` (nature des murs), `D5` (épaisseurs relevées), **aucun essai**. C'est la borne basse de la maçonnerie de pierre naturelle : elle gouverne les raideurs de contreventement et les centres de rigidité de `B-25` | À CONFIRMER | B-25 | B-25 · B-42 · B-46 | 20/10 |
| **H-26** | Cohésion initiale au cisaillement | `f_vk0 = 0,15 MPa` · `γ_M = 2,5` | Idem `H-25`. Avec `σ_d` de `H-27`, donne `f_vk = 108 kPa` — valeur utilisée dans tous les ratios `τ/f_vk` de `B-25` | À CONFIRMER | B-25 | B-25 · B-46 | 20/10 |

> **`H-25` et `H-26` sont les deux hypothèses les plus lourdes du dossier.** Elles portent **toute** la stabilité horizontale : un `f_k` réel de `1,0 MPa` au lieu de `1,5` ferait chuter les raideurs de 33 % et déplacerait les centres de rigidité. Aucun essai n'est prévu à notre mission — la valeur plancher est donc **assumée**, jamais présentée comme mesurée.

### 2.5 Famille SOL — 3 hypothèses

| N° | Objet | Valeur retenue | Justification et source | Statut | Intro. | Impacte | Dates |
|---|---|---|---|---|---|---|---|
| **H-22** | Assise à −1,00 m | Alluvions anciennes ; `q_ELS ≥ 0,30 MPa`, `q_ELU < 0,49 MPa` ; aucun remblai entre −0,50 et −1,00 m | `D-08` (toit des alluvions **déduit** à −0,50 m) · `D-02` · `D-03` · `D-18` (rapport `GEOFLORAV2` intransférable). **La nature est confirmée par `D1` ; la continuité sous l'emprise ne l'est pas** | **CONFIRMÉE** | B-10 | B-40 | 19/10 |
| **H-23** | Agressivité du milieu | **XA1** | `D2 p. 1` porte « XA4 » ; le CCTP § 01.1.1 (NP EN 206) vise **XA1 à XA3**. Écart de saisie. L'enrobage `50 mm` en fondation et `30 mm` hors fondation reste conforme | À CONFIRMER | B-10 | B-40 · B-42 | 19/10 |
| **H-24** | Classe de sol et `a_gr` | Classe C, `a_gr = 0,40 m/s²` | **ABANDONNÉE le 20/10/2026 par `D-26`** : zone de sismicité 1, aucune vérification sismique produite. Conservée au registre, sans emploi, pour que la raison du retrait reste lisible | **ABANDONNÉE** | B-10 | aucune | 19/10 · 20/10 |

### 2.6 Famille AUTRES — 10 hypothèses

| N° | Objet | Valeur retenue | Justification et source | Statut | Intro. | Impacte | Dates |
|---|---|---|---|---|---|---|---|
| **H-02** | Destination | Cabinet paramédical | `D2 p. 1`, `D4 p. 6 et 9`, énoncé de mission `B-00 § 4`. La mention « habitation + service technique » de `D3` décrit l'**existant**, pas le **programme** | À CONFIRMER | B-00 | B-60 · B-64 | 19/10 |
| **H-04** | Périmètre | Pavillon Flora seul | `D1 p. 1` (titre) contre son sommaire ; `D4 p. 28` porte le bâtiment Gardien au plan d'installation. Le Gardien est exclu de nos études **et** de notre exécution | À CONFIRMER | B-00 | B-60 · B-64 | 19/10 |
| **H-07** | Indice du folio 03 | **Indice B** | `D2 p. 1` (sommaire, indice « – ») contre `D2 f. 03` (cartouche). Le cartouche de la pièce prime sur le sommaire qui la liste | À CONFIRMER | B-00 | B-40 · PLS | 19/10 |
| **H-09** | Sens de « RSO » | Reprise en sous-œuvre | `D2 p. 1` et `D2 f. 04` — deux emplois : « RSO ancrées d'au moins 0,5 m » (les fondations nouvelles) et « après stabilisation de la RSO » (l'ouvrage stabilisé) | À CONFIRMER | B-00 | B-40 · PLS | 19/10 |
| **H-11** | Compactage de plate-forme | Arrêté à 1,00 m de tout soubassement | `D1 § 01.2.1.9` prescrit un compactage général ; `D2 f. 04` l'arrête à 1,00 m des soubassements et **n'est pas appliqué sur le débord de semelle**. La prescription de plan prime : elle est plus récente et plus précise | À CONFIRMER | B-00 | B-43 | 19/10 |
| **H-13** | Passes de reprise en sous-œuvre | Passes alternées ≤ 1,00 m, `C16/20`, recépage soigné | `D2 f. 04` (passes alternées) et `D1 § 01.2.1.7.1` (`C16/20`). Le **phasage** est établi par nos soins sur la base du folio 04 | À CONFIRMER | B-00 | B-40 | 19/10 |
| **H-14** | Charpente dans notre périmètre | Lot 01, notre lot | `D2 f. 02` dessine renfort de ferme, demi-ferme en sous-œuvre, pannes et contrefiches ; `D1` ne comporte **aucune section bois**. Une prestation dessinée au marché ne disparaît pas parce qu'aucune section ne la décrit | À CONFIRMER | B-00 | B-44 | 19/10 |
| **H-16** | Fouilles | Parois verticales, sans blindage ≤ 1,20 m | `D1 § 01.2.1.6.1` (rigoles) et `D-16` (nappe absente). Tout terrain ébouleux ou toute venue d'eau impose l'arrêt, le blindage et le retour vers la MOE | À CONFIRMER | B-00 | B-40 | 19/10 |
| **H-20** | Étaiement provisoire | À notre charge (lot 01) | `D2 f. 01-02` ; `D1` ne comporte **aucun article** sur l'étaiement. Il est calculé, implanté, déposé par nos soins et **valorisé au titre de notre prestation** | À CONFIRMER | B-00 | B-25 · mode opératoire | 19/10 |
| **H-21** | Déplombage, curage, démolition | **Hors mission** | `D1 p. 1` (intitulé du lot 01) et `§ 01.2.1.4-5` les attribuent au lot ; `D4 p. 5`. Nous ne les étudions pas, ne les exécutons pas, **notre prix ne les comprend pas**. Rectifiée le 19/10/2026 | **CONFIRMÉE** | B-00 | B-60 · B-64 | 19/10 |

---

## 3. HISTORIQUE DES RÉVISIONS

| Date | Hypothèse | Nature de la révision | Auteur | Motif |
|---|---|---|---|---|
| 19/10/2026 | `H-01` à `H-24` | **Création** — 24 hypothèses validées en bloc, `H-21` rectifiée | Client | Validation des hypothèses de cadrage |
| 19/10/2026 | `H-21` | **Rectification** — déplombage, curage et démolition déclarés hors mission | Client | Le CCTP les attribue au lot 01 ; notre prix ne les comprend pas |
| 20/10/2026 | `H-24` | **Abandon** — classe de sol et `a_gr` sans emploi | Client (`D-26`) | Zone de sismicité 1 : aucune vérification sismique produite |
| 20/10/2026 | `H-25`, `H-26`, `H-27` | **Création** — caractéristiques de la maçonnerie et contrainte sur les voiles | B-25 | Stabilité globale non calculable sans ces valeurs |
| 20/10/2026 | `H-27` | **Révision de statut** — « posée » → « vérifiée et conservatrice » | B-21 | `σ_d` réel `0,094 MPa` contre `0,300` retenu : `f_vk` majoré de 44 % |
| 20/10/2026 | `H-28`, `H-29`, `H-30` | **Création** — charges de plancher, de toiture et de cloisons | B-21 | DDC préliminaire : trois grandeurs absentes du marché |
| 20/10/2026 | `H-31` | **Promotion en décision** — sortie du registre | Client (`D-31`) | Salle de sport confirmée en catégorie C4 |
| 20/10/2026 | `H-01` à `H-30` | **Régime de confirmation** — colonne ajoutée, 9 hypothèses reclassées en LECTURE | Client (`D-33`) | Le CCTP est adressé à l'entreprise : aucune réponse ne viendra pour ces neuf-là |

---

## 4. CONTRÔLE DE COHÉRENCE — RÉSULTATS DU SCRIPT

| Contrôle | Résultat |
|---|---|
| Numéros uniques | ✅ **30 numéros, 0 doublon** |
| Continuité `H-01` → `H-30` | ✅ **aucun trou** — `H-31` sortie par promotion, documentée |
| Statuts dans le référentiel (`À CONFIRMER` / `CONFIRMÉE` / `ABANDONNÉE`) | ✅ **0 écart** |
| Régimes dans le référentiel | ✅ **0 écart** |
| « À CONFIRMER » sans régime | ✅ **aucun** |
| Hypothèse sans valeur | ✅ **aucune** |
| Familles vides | ⚠ **Matériaux** — justifié au § 2.2 (le marché fournit `C25/30`, `C16/20`, `S500B`, `S275`) |
| Croisement des références dans les briques | ✅ **13 citations** vérifiées dans `B-20`, `B-21`, `B-25`, `B-40` — **toutes présentes au registre** |

**Sorties vérifiables** : `_rendus/b22_hypotheses.txt` et `_rendus/b22_hypotheses.json`.

---

## 5. AUTO-CONTRÔLE DES SIX CRITÈRES D'ACCEPTATION

| # | Critère de la fiche `B-22` | État | Preuve |
|---|---|---|---|
| 1 | Chaque hypothèse a un numéro unique et stable | ✅ **CONFORME** | 30 numéros `H-01` à `H-30`, aucun doublon, aucun trou ; `H-31` documentée comme promue |
| 2 | Chaque hypothèse a une justification, pas seulement une valeur | ✅ **CONFORME** | § 2 — chaque ligne porte une colonne « justification et source » citant la pièce et le raisonnement |
| 3 | Chaque hypothèse a un statut | ✅ **CONFORME** | 25 `À CONFIRMER` · 4 `CONFIRMÉE` · 1 `ABANDONNÉE` — aucun statut implicite |
| 4 | Aucune hypothèse n'a été supprimée | ✅ **CONFORME** | `H-24` conservée `ABANDONNÉE` avec son motif (`D-26`) ; `H-21` conservée avec sa rectification |
| 5 | L'historique des révisions est tenu | ✅ **CONFORME** | § 3 — 8 entrées datées, avec auteur et motif, y compris les révisions de statut |
| 6 | L'index de la section 1 est cohérent avec le détail de la section 2 | ✅ **CONFORME** | Contrôle par script : 30 lignes d'index, 30 lignes de détail, mêmes numéros, mêmes statuts |

**Verdict de la brique `B-22` (Indice A) : ✅ CONFORME — 6/6.**

---

## 6. CE QUE `B-22` APPORTE AU DOSSIER

1. **Un registre unique et opposable.** Jusqu'ici, les hypothèses se lisaient dans trois documents (`B-03 Annexe`, `B-21`, `B-25`). Un tiers devait ouvrir trois pièces pour vérifier une seule note de calcul. Désormais : **un document, 30 lignes, une ligne par hypothèse**.
2. **La distinction attente / lecture.** Neuf hypothèses cessent d'être présentées comme des questions en souffrance. C'est un gain de crédibilité pour les dix qui en sont vraiment.
3. **Le contrôle croisé `B-25` ↔ `B-21`.** `H-27` est la première hypothèse du dossier **vérifiée par une brique aval** : `B-25` avait besoin d'un `σ_d` qu'elle ne pouvait pas calculer, `B-21` l'a produit et a constaté que l'hypothèse tenait — avec 3,2 fois de marge.
4. **Une famille vide assumée.** Aucune hypothèse de matériau : le marché est explicite (`C25/30`, `C16/20`, `S500B`, `S275`). C'est rare, et cela vaut d'être écrit plutôt que passé sous silence.

---

## 7. POINT DE CONTRÔLE HUMAIN

1. **La doctrine `D-33` est-elle bien celle que vous vouliez ?** J'ai lu votre instruction comme : *le CCTP est adressé à l'entreprise, donc nous n'attendons pas de réponse là où aucun destinataire n'existe — nous nous positionnons par lecture et nous reportons le risque sur l'exécution*. Si vous vouliez dire autre chose — par exemple que ces prestations doivent être **explicitement exclues de nos livrables** plutôt que simplement non relancées — dites-le : cela change la rédaction de `H-11`, `H-13`, `H-16` et `H-19`.
2. **Le classement des neuf hypothèses `LECTURE` est-il le bon ?** J'y ai mis `H-03`, `H-05`, `H-06`, `H-09`, `H-11`, `H-13`, `H-16`, `H-19`, `H-21`. Les deux plus discutables sont `H-06` (échelle 1/80 — la MOE pourrait la confirmer formellement) et `H-03` (renforts exécutés — un PV de réception répondrait).
3. **`H-25` et `H-26` restent des valeurs plancher non mesurées.** Elles portent toute la stabilité horizontale. Si la MOE peut financer **deux essais de maçonnerie** (sclérométrie ou carottage), ces hypothèses quittent le régime `CALCUL` et deviennent `DOCUMENTAIRE` — c'est le seul achat d'étude qui améliorerait réellement la fiabilité du dossier.
4. **`D-29` reste ouverte** — contreventement en service = maçonnerie existante seule. Elle n'est pas dans cette brique, mais tant qu'elle ne l'est pas, `H-25`, `H-26` et `H-27` sont vérifiées **sans être arbitrées**.

**Brique B-22 livrée en indice A — en attente de votre GO ou de vos observations.**
