# B-01 — PROPOSITION DE LA MATRICE DE PÉRIMÈTRE ET DE DISPONIBILITÉ (MPD)

| Champ | Valeur |
|---|---|
| Carnet | CARNAC v2.6 |
| Brique | **B-01** — Proposition de MPD |
| Phase | 0 — Cadrage |
| Mode d'appel | **COMPLET** |
| Code projet `ID-01` | `CROISSY-FLORA` |
| Intitulé `ID-02` | EHPAD La Roseraie — Pavillon Flora — aménagement d'un cabinet paramédical |
| **Indice du livrable** | **B** (remplace l'indice A du 19/10/2026) |
| Date | 19/10/2026 |
| Brique suivante | B-02 (FDC) — non engagée |

> **Statut du document** : **PROPOSITION**. Aucun statut n'est définitif avant validation ligne par ligne.
> Les **NON NÉCESSAIRE** et les **SANS OBJET** restent soumis à décision explicite du client.

---

## 0. CE QUI CHANGE À L'INDICE B — décisions client intégrées

Le client a transmis le **19/10/2026** les hypothèses géotechniques de synthèse, le dossier GEOEXPERTS étant trop lourd pour être transmis intégralement. Ces informations sont traitées comme des **déclarations client** et non comme des données lues dans une pièce.

| Code | Indice A | **Indice B** | Effet |
|---|---|---|---|
| **SOL-02** — contrainte admissible ELU | BLOQUANTE | **FOURNIE — 0,49 MPa** | **B-40 débloquée sur ce point** |
| **SOL-01** — contrainte admissible ELS | FOURNIE | **FOURNIE — confortée** | Source élargie : D2 **et** déclaration client |
| **SOL-03** — ancrage | PARTIELLE (≥ 0,50 m) | **PARTIELLE — valeur contradictoire** | **Nouvelle contradiction C-21** : 0,40 m vs 0,50 m |
| **DOC-06** — rapport géotechnique | BLOQUANTE | **PARTIELLE** | Synthèse disponible, rapport non transmis |
| **B-41** — Fondations profondes | activée, suspendue | **proposée SANS OBJET** | « Fondations superficielles » déclarées |

**Comptage révisé : 63 variables à consommateur**

| Statut | Indice A | **Indice B** |
|---|---|---|
| BLOQUANTE | 18 | **16** |
| PARTIELLE | 20 | **21** |
| FOURNIE | 13 | **14** |
| À PRODUIRE PAR GO | 11 | **11** |
| NON NÉCESSAIRE (périmètre) | 1 | **1** |
| **Total** | **63** | **63** |

---

## 0bis. DÉCISIONS CLIENT REÇUES — à consigner au RDR (B-03)

Conformément au § 0.2 de la règle des portes (« une correction conversationnelle non consignée est une décision perdue »), ces quatre décisions sont enregistrées provisoirement. Elles seront reportées au **Registre des Décisions** dès l'ouverture de B-03.

| Réf. provisoire | Décision | Auteur | Date | Portée |
|---|---|---|---|---|
| **D-P1** | Les hypothèses géotechniques de référence sont celles d'une mission **G2 AVP GEOEXPERTS** | Client | 19/10/2026 | SOL-08, DOC-06 |
| **D-P2** | **q<sub>ELS</sub> < 0,30 MPa** (contrainte admissible à l'ELS) | Client | 19/10/2026 | SOL-01 |
| **D-P3** | **q<sub>ELU</sub> < 0,49 MPa** (contrainte admissible à l'ELU) | Client | 19/10/2026 | SOL-02 |
| **D-P4** | **Fondations superficielles ancrées de 40 cm dans les alluvions anciennes** | Client | 19/10/2026 | SOL-03, B-41 |

> **Réserve de forme** : ces valeurs sont **retenues pour les calculs** conformément à votre instruction, mais elles sont traitées en **PARTIEL-DÉCLARÉ** : leur origine est une déclaration client, pas l'extraction du rapport GEOEXPERTS n° 25.13646/ES/GIF. Si le rapport transmis ultérieurement diffère, la décision D-P2/P3/P4 devra être révisée par décision datée.

---

## 0ter. CONTRÔLE DE COHÉRENCE DES DONNÉES DÉCLARÉES

Deux vérifications d'ordre de grandeur, sans application numérique de dimensionnement (celles-ci relèvent de B-40) :

| Contrôle | Résultat | Conclusion |
|---|---|---|
| Rapport q<sub>ELU</sub> / q<sub>ELS</sub> | 0,49 / 0,30 = **1,63** | Cohérent : un rapport de 1,5 à 1,7 est usuel entre ELU et ELS pour une fondation superficielle. Les deux valeurs sont **compatibles entre elles** |
| q<sub>ELS</sub> déclarée vs cartouche D2 | 0,30 MPa (client) = 0,3 MPa (D2 p. 1) | **Concordant** — la déclaration reproduit exactement la valeur du cartouche |

> En revanche, l'**ancrage ne concorde pas** : c'est l'objet de la contradiction C-21 ci-dessous.

---

## 1. PÉRIMÈTRE TECHNIQUE PROPOSÉ

| Brique | Intitulé | État proposé | Justification |
|---|---|---|---|
| **B-20** | Conception GO | **INTERNE-GO** | AC-03 partielle : repères fournis, pas de note de calcul |
| **B-21** | DDC préliminaire | **ACTIVÉE** | DDC à reprendre (250 daN/m², C-02) |
| **B-22** | Note d'hypothèses | **ACTIVÉE** | — |
| **B-23** | Exploitation diagnostic | **ACTIVÉE** | 9 désordres (D3 p. 3-8) |
| **B-24** | Existant non sondé | **ACTIVÉE** | EXI-04, EXI-05 partielles |
| **B-30 à B-33** | Calage et preuves | **ACTIVÉES — SUSPENDUES** | DXF non fourni |
| **B-40** | **Fondations superficielles** | **ACTIVÉE — PRIORITAIRE** | Devient la brique pivot : qELS et qELU désormais connues |
| **B-41** | Fondations profondes | **⚠ PROPOSÉE SANS OBJET** | Fondations superficielles déclarées (D-P4) |
| **B-42** | Verticaux BA | **ACTIVÉE** | P2 15×25, P3 50×40, J1 |
| **B-43** | Planchers / dallages | **ACTIVÉE** | Dallage, recharge 15 cm |
| **B-44** | Charpente bois | **ACTIVÉE** | Pannes, demi-ferme, contrefiches |
| **B-45** | Structure métallique | **ACTIVÉE** | F1-F4, R1-R3, P1, Stab1 |
| **B-46** | Maçonnerie | **ACTIVÉE** | Moellons, briques, jambages |
| **B-47** | Escaliers | **⚠ PROPOSÉE SANS OBJET** | Aucun escalier neuf |
| **B-48** | Prédalles | **⚠ PROPOSÉE SANS OBJET** | Aucun plancher préfabriqué |
| **B-49** | Linteaux / seuils | **ACTIVÉE** | F1 2×HEA200 sur linteau bois |
| **B-50** | Assemblages / ancrages | **ACTIVÉE** | Interface S275 / C18 / C25-30 |

---

## 2. MPD — TABLEAU PRINCIPAL (63 variables)

### 2.1 Actions et charges (CHG)

| Code | Libellé | Statut | Motif | Source ou raison d'absence | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| CHG-01 | Usage des locaux par zone (cat. EC1) | **PARTIELLE** | Catégorie de la **salle de sport 34,25 m²** non tranchée | D4 p. 6 et 9 ; C-10 | B-21 | PARTIEL-DÉCLARÉ |
| CHG-02 | Surcharges d'exploitation par zone | **PARTIELLE** | 250 daN/m² global, non décliné ; DIAG retient 150 | D2 p. 1 ; D3 p. 10-11 ; C-02 | B-21 | PARTIEL-DÉCLARÉ |
| CHG-03 | Poids propres des complexes de plancher | **PARTIELLE** | « Sol à recharger de 15 cm » non intégré (255 à 330 daN/m²) | D2 p. 1 ; D4 p. 5 et 14 ; C-08 | B-21 | PARAMÉTRIQUE |
| CHG-04 | Poids propres de toiture | **BLOQUANTE** | Couvertures décrites **sans aucune charge** | D4 p. 26-27 | B-21, B-44 | PARAMÉTRIQUE |
| CHG-05 | Neige | **FOURNIE** | Zone A1, < 200 m, sk = 45 daN/m² | D2 p. 1 | B-21, B-44 | COMPLET |
| CHG-06 | Vent | **FOURNIE** | Zone 2, vb = 24 m/s, terrain III | D2 p. 1 | B-21, B-44, B-45 | COMPLET |
| CHG-07 | Sismique | **BLOQUANTE** | **a<sub>gr</sub> vide**, classe de sol vide | D2 p. 1 ; C-18 | B-42, B-46 | PARAMÉTRIQUE |
| CHG-08 | Cloisons, équipements lourds | **BLOQUANTE** | 4 types de cloisons sans poids ; ballon ECS, chaudière non inventoriés | D4 p. 9 et 18 | B-21, B-43 | PARAMÉTRIQUE |

### 2.2 Décisions et traçabilité (DEC)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| DEC-01 | Mode attribué à chaque brique | **À PRODUIRE PAR GO** | Découle de la validation de la MPD | **B-03** | B-70 | INTERNE-GO |
| DEC-02 | Décisions inscrites au RDR | **À PRODUIRE PAR GO** | 4 décisions client déjà reçues (§ 0bis) + 21 contradictions | **B-03** | B-03, B-64, B-70, B-72, T-03 | INTERNE-GO |
| DEC-03 | Verrous ouverts | **À PRODUIRE PAR GO** | 16 variables bloquantes à inscrire | **B-03 / B-04** | B-03, B-04, B-13, B-15, B-64, B-70, B-72, T-03, T-04 | INTERNE-GO |
| DEC-04 | Documents supersédés | **À PRODUIRE PAR GO** | Indices A et B de D2 supersédés par C | **B-71** | B-71, B-72 | INTERNE-GO |

### 2.3 Documents (DOC)

| Code | Libellé | Statut | Motif | Source ou raison d'absence | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| DOC-01 | Inventaire des pièces | **FOURNIE** | — | B-00 ind. **B** | B-00, B-01 | COMPLET |
| DOC-02 | Plans architecte vectoriels | **PARTIELLE** | 29 pages PDF ; **DXF non fourni** | D4 ; D5 absent | B-20, B-30, B-31, B-32, B-33, B-60 | PARAMÉTRIQUE |
| DOC-03 | Plans BET structure | **PARTIELLE** | 2 zones « non relevées » ; aucun plan de coffrage/ferraillage | D2 ; C-13, C-19 | B-10, B-11, B-20 | PARTIEL-DÉCLARÉ |
| DOC-04 | CCTP / pièces contractuelles | **PARTIELLE** | 8 pages lues sur 38 ; **aucune section charpente bois** | D1 ; C-07 | B-10, B-14 | PARTIEL-DÉCLARÉ |
| DOC-05 | Diagnostic structure | **FOURNIE** | 18 pages, 9 désordres | D3 | B-11, B-23, B-24 | COMPLET |
| **DOC-06** | **Rapport géotechnique** | **PARTIELLE** *(était BLOQUANTE)* | **Hypothèses de synthèse transmises le 19/10/2026** (D-P1 à D-P4) ; **rapport GEOEXPERTS n° 25.13646/ES/GIF non transmis** — coupes, sondages, nappe, agressivité réelle, tassements absents | Déclaration client 19/10/2026 ; D2 p. 1 | B-12, B-41 | PARTIEL-DÉCLARÉ |
| DOC-08 | Plans de récolement / DOE | **BLOQUANTE** | Aucun DOE ; fondations décrites « inconnues » au DIAG | D3 p. 2 | B-11 | PARAMÉTRIQUE |
| DOC-09 | Fiches techniques des prédalles | **NON NÉCESSAIRE (périmètre)** | **Aucun plancher préfabriqué** : planchers existants conservés et renforcés, seul plancher neuf = dallage | Périmètre ; B-48 sans objet | B-48 *(non activée)* | SANS OBJET |

### 2.4 Existant (EXI)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| EXI-01 | Sections des éléments existants | **PARTIELLE** | Planchers A et B fournis ; **pas de sections de poteaux, pannes, fermes, moellons** | D3 p. 10-12 ; D2 folio 02 | B-23, B-24, B-44 | PARTIEL-DÉCLARÉ |
| EXI-02 | Pathologies relevées | **FOURNIE** | 9 désordres localisés | D3 p. 3-8 | B-23 | COMPLET |
| EXI-03 | Résistance des matériaux existants | **PARTIELLE** | Bois C18 **hypothèse** ; acier IPE non qualifié ; maçonnerie non caractérisée | D3 p. 10 | B-24, B-44 | PARAMÉTRIQUE |
| EXI-04 | Sondages destructifs | **PARTIELLE** | Campagne réalisée, 2 types identifiés ; **aucune fiche ni emplacement coté** | D3 p. 9 | B-24, B-41 | PARTIEL-DÉCLARÉ |
| EXI-05 | Contrainte admissible transmise à l'existant | **BLOQUANTE** | Pieds de poteaux « à la limite » **sans valeur d'admissible** | D3 p. 17 | B-23, B-46 | PARAMÉTRIQUE |

### 2.5 Géométrie (GEO)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| GEO-01 | Emprise / contour | **FOURNIE** | Emprise cotée, niveaux Z | D4 p. 2-3, 6, 9, 19-27 | B-43, B-44, B-48 | COMPLET |
| GEO-06 | Unités du fichier source | **BLOQUANTE** | Aucun fichier CAO fourni | D5 absent | B-30, B-32 | SUSPENDUE |
| GEO-07 | Transformation du fichier | **BLOQUANTE** | Aucune transformation mesurable | D5 absent | B-30, B-31 | SUSPENDUE |
| GEO-08 | Points de calage (≥ 3) | **BLOQUANTE** | Aucun point de calage entre D2 et D4 | D5 absent | B-30, B-31 | SUSPENDUE |
| GEO-10 | Seuils de présomption porteuse | **À PRODUIRE PAR GO** | Donnée de projet | **RDR (B-03)** | B-32 | INTERNE-GO |
| GEO-11 | Superposition des niveaux | **À PRODUIRE PAR GO** | Donnée de projet | **RDR (B-03)** | B-32 | INTERNE-GO |
| GEO-12 | Seuils géométriques du projet | **À PRODUIRE PAR GO** | Existant ancien et irrégulier → **valeur déclarée au RDR** exigée par le maître §5 | **RDR (B-03)** | B-30, B-31, B-33 | INTERNE-GO |

### 2.6 Identification (ID)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| ID-01 | Code projet | **FOURNIE** | `CROISSY-FLORA` | B-00 | *toutes* | COMPLET |
| ID-02 | Intitulé de l'opération | **FOURNIE** | EHPAD La Roseraie — Pavillon Flora | D1, D2, D4 | *toutes* | COMPLET |
| ID-05 | Indice du dossier en vigueur | **PARTIELLE** | Trois indicages non concordants (D1 V1 / D2 C / D4 C) | D1, D2, D4 | B-03, B-64, B-71, B-72 | PARTIEL-DÉCLARÉ |
| ID-07 | Date de l'étude | **FOURNIE** | 19/10/2026 | Session | B-03 | COMPLET |

### 2.7 Matériaux (MAT)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| MAT-01 | Classe de résistance du béton | **FOURNIE** | C25/30 · C16/20 | D2 p. 1 | B-40, B-42, B-46, B-47 | COMPLET |
| MAT-02 | Classe d'exposition | **PARTIELLE** | **« XA4 » inexistante** en NF EN 206/CN | D2 p. 1 ; C-15 | B-40, B-42, B-47 | PARTIEL-DÉCLARÉ |
| MAT-03 | Enrobage nominal | **PARTIELLE** | c<sub>nom</sub> 30 mm avec S4 + XC4 : cohérence non démontrée | D2 p. 1 ; C-16 | B-40, B-42, B-47 | PARTIEL-DÉCLARÉ |
| MAT-04 | Nuance d'acier BA | **FOURNIE** | S500B / S220B | D2 p. 1 | B-40, B-42, B-46, B-47 | COMPLET |
| MAT-05 | Nuance d'acier de charpente | **FOURNIE** | S275 | D2 p. 1 | B-45, B-49, B-50, B-62 | COMPLET |
| MAT-06 | Classe de bois | **PARTIELLE** | C18 en hypothèse ; **charpente non classée** | D3 p. 10 | B-44, B-50, B-62 | PARAMÉTRIQUE |
| MAT-07 | Nature et résistance de la maçonnerie | **PARTIELLE** | Moellons et briques identifiés ; **aucune résistance** | D2 folio 03 ; D4 p. 19 | B-46, B-49, B-50 | PARAMÉTRIQUE |
| MAT-08 | Classe de service et durée de charge | **À PRODUIRE PAR GO** | Désordres d'humidité → classe 1 ou 2 à trancher | **B-22** | B-44 | INTERNE-GO |
| MAT-09 | Classe de bloc NF EN 771-3 | **BLOQUANTE** | « blocs pleins ou semi-pleins » sans classe | D1 § 01.2.1.7.5 | B-46 | PARAMÉTRIQUE |
| MAT-10 | Classe de mortier | **BLOQUANTE** | « mortier hydrofugé » sans classe | D1 § 01.2.1.7.5 | B-46 | PARAMÉTRIQUE |
| MAT-11 | Type de maçonnerie | **BLOQUANTE** | Chaînée / armée / non armée non précisé | D1 § 01.2.1.7.5 | B-46 | PARAMÉTRIQUE |
| MAT-12 | Chaînages existants | **BLOQUANTE** | Aucun chaînage relevé | D3 ; D2 | B-46 | PARAMÉTRIQUE |

### 2.8 Outillage (OUT)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| OUT-01 | Environnement d'exécution | **PARTIELLE** | Python 3.11 + PyMuPDF opérationnels ; **ezdxf absent**, DXF non fourni | Constat de session | B-30, B-31, B-32, B-33, B-60, B-62 | PARAMÉTRIQUE |
| OUT-02 | Script versionné | **À PRODUIRE PAR GO** | Aucun script de brique n'existe | B-30 à B-62 | B-30 à B-62 | INTERNE-GO |
| OUT-03 | Journal d'exécution | **À PRODUIRE PAR GO** | Idem | B-30 à B-62, B-70 | B-31, B-33, B-60, B-70 | INTERNE-GO |
| OUT-04 | Rendu de contrôle PNG 300 dpi | **À PRODUIRE PAR GO** | Idem | B-31, B-32, B-60 | B-31, B-32, B-60 | INTERNE-GO |

### 2.9 Sécurité (SEC)

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| SEC-01 | Degré coupe-feu par élément | **BLOQUANTE** | Section SECURITE INCENDIE **intégralement vide** | D2 p. 1 ; C-17 | B-42, B-43, B-49 | PARAMÉTRIQUE |
| SEC-03 | Classement termites de la commune | **PARTIELLE** | Traitement prescrit **sans arrêté préfectoral** | D1 § 01.2.1.9.2 | B-43 | PARTIEL-DÉCLARÉ |

### 2.10 Sol et géotechnique (SOL) — **section révisée à l'indice B**

| Code | Libellé | Statut | Motif | Source | Brique(s) | Mode induit |
|---|---|---|---|---|---|---|
| **SOL-01** | Contrainte admissible ELS | **FOURNIE** | **q<sub>ELS</sub> < 0,30 MPa** — concordant entre D2 et déclaration client | D2 p. 1 **+ D-P2 (19/10/2026)** | B-12, B-40, B-43 | **COMPLET** |
| **SOL-02** | Contrainte admissible ELU | **FOURNIE** *(débloquée)* | **q<sub>ELU</sub> < 0,49 MPa** — valeur absente du cartouche D2, apportée par le client | **D-P3 (19/10/2026)** | B-40 | **COMPLET** |
| **SOL-03** | Profondeur de bon sol / ancrage | **PARTIELLE** | **Valeurs contradictoires** : **0,40 m (D-P4)** vs **≥ 0,50 m (D2 p. 1)** → **C-21**. Profondeur du toit des alluvions non donnée | D-P4 ; D2 p. 1 | B-40 | **PARTIEL-DÉCLARÉ** |
| SOL-04 | Nature et succession des couches | **BLOQUANTE** | Rapport absent : seule l'appellation « alluvions anciennes » est connue | D-P1 ; D2 p. 1 | B-41 · **et B-40** (voir § 5.4) | PARAMÉTRIQUE |
| SOL-05 | Classe d'agressivité du sol (XA) | **PARTIELLE** | « XA4 » non normative : XA1 à XA3 seulement existent | D2 p. 1 ; C-15 | B-40, B-43 | PARAMÉTRIQUE |
| SOL-06 | Nappe, hydrologie, drainage | **BLOQUANTE** | **Non transmis** — le rapport GEOEXPERTS la contient | DOC-06 non transmis | B-40 | PARAMÉTRIQUE |
| SOL-07 | Tassements admissibles / différentiels | **BLOQUANTE** | **Non transmis** ; ouvrage ancien sur moellons, sensibilité maximale | DOC-06 non transmis | B-40 | PARAMÉTRIQUE |
| SOL-08 | Mission géotechnique disponible | **PARTIELLE** | **G2 AVP** confirmée (D-P1) ; **pas de G2 PRO ni de G3** | D-P1 ; D2 p. 1 | B-12, B-41 | PARTIEL-DÉCLARÉ |

---

## 3. ANNEXE — 31 variables sans brique consommatrice

| Code | Libellé | État factuel constaté | Renvoi |
|---|---|---|---|
| AC-01 | MOA | Divergeant : UNIVI (D1) vs SCI GEMS RC (D4) | **C-04** |
| AC-02 | Architecte | TRUELLE Architectes | D1, D2, D4 |
| AC-06 | Bureau de contrôle | **Non désigné** — case vide au cartouche | À lever |
| DOC-07 | Diagnostic amiante / plomb | Cité au CCTP, non fourni | Hors périmètre |
| GEO-02 | Axes et trames | Non relevés | — |
| GEO-03 | Épaisseurs murs | Non relevées | — |
| GEO-04 | Positions poteaux | Non relevées (« ZONE NON RELEVEE ») | **C-19** |
| GEO-05 | Baies et ouvertures | Fournies (nomenclatures M0/M1/M2) | D4 p. 23-25 |
| GEO-09 | Échelle tracé | 1/50-1/20 au cartouche vs (1/80) au plan | **C-12** |
| ID-03 | Adresse | 2 rue Alfred Dormeuil / 11 rue Paul Demange | **C-01** |
| ID-04 | Nature | Réhabilitation lourde d'un existant | D3 p. 2 |
| ID-06 | Phase | DCE (PRO) | D1 p. 1 |
| LIV-01 à LIV-05 | Livrables, échelles, cartouche, langue, unités | À figer en annexe A au moment de B-60 | Annexe A |
| NIV-01 | Niveau TN | **Non fourni** | À lever |
| NIV-02 | Niveaux planchers | RDC 201,03-201,26 · R+1 203,59-204,43 | D4 p. 4 et 6 |
| NIV-03 | Hauteurs libres | hsp 2,16 à 3,25 m | D4 p. 4 et 6 |
| NIV-04 | Niveau assise | **Non fourni** — le rapport GEOEXPERTS le donne | À lever |
| NIV-05 | Niveau fini dallage | « bêche pour réhausse » sans cote | D2 folio 03 |
| NIV-06 | Épaisseurs plancher | Fournies pour A et B | D3 p. 10-11 |
| SEC-02 | Catégorie ERP | **Vide au cartouche** | **C-17** |
| SEC-04 | Classe structurale | S4 | D2 p. 1 |
| SEC-05 | PMR | Programme PMR identifié | D4 p. 3 et 14 |
| SIT-01 | Site occupé | Installations, compte prorata, constat d'huissier | D1 p. 10-12 |
| SIT-02 | Contraintes de site | FLORA + GARDIEN sur site | D4 p. 28 |
| SIT-03 | Accès | Véhicule + piéton rue Paul Demange | D4 p. 28 |
| SIT-04 | Voisinage | Mitoyenneté à repérer | D1 § 01.1.2 |
| SIT-05 | Emprise fouille | **Non fournie** | À lever |

---

## 4. SYNTHÈSE — les trois paragraphes exigés

### 4.1 Variables BLOQUANTES et briques suspendues — **16 variables**

Seize variables sont nécessaires à une brique activée mais absentes ou inexploitables :

- **B-30, B-31, B-32, B-33** — suspendues par **GEO-06, GEO-07, GEO-08** : aucun fichier CAO, aucun point de calage commun entre D2 et D4.
- **B-21, B-44** — suspendues par **CHG-04** : aucune charge de toiture.
- **B-21** — suspendue par **CHG-08** : ni poids des cloisons, ni inventaire des équipements lourds.
- **B-42, B-46** — suspendues par **CHG-07** : action sismique non calculable.
- **B-40** — suspendue par **SOL-04, SOL-06, SOL-07** : ni coupes de sol, ni nappe, ni tassements admissibles.
- **B-46** — suspendue par **MAT-09, MAT-10, MAT-11, MAT-12, EXI-05** : la maçonnerie n'a ni classe de bloc, ni mortier, ni type, ni chaînage, ni contrainte admissible.
- **B-11** — suspendue par **DOC-08** : aucun DOE.
- **B-42, B-43, B-49** — suspendues par **SEC-01** : section incendie vide.

> **Ce qui a changé** : B-12 n'est plus suspendue par DOC-06 (devenue PARTIELLE) ; B-41 sort du décompte, proposée sans objet.

### 4.2 Variables À PRODUIRE PAR GO — **11 variables**

- **DEC-01 à DEC-04** → **B-03** (RDR), et **B-71** pour la supersession.
- **GEO-10, GEO-11, GEO-12** → seuils de présomption et seuils géométriques. Le maître §5 impose, pour un **existant ancien et irrégulier**, une **valeur déclarée au RDR** et non le défaut « existant régulier ».
- **MAT-08** → classe de service et durée de charge du bois, par **B-22** ; déterminante vu les désordres d'humidité 4, 6, 7 et 8.
- **OUT-02, OUT-03, OUT-04** → scripts, journaux et rendus, par les briques outillées.

### 4.3 Variables NON NÉCESSAIRE — **1 variable**

| Code | Libellé | Motif de périmètre | Conséquence si validation |
|---|---|---|---|
| **DOC-09** | Fiches techniques des prédalles | **Aucun plancher préfabriqué** : planchers existants conservés et renforcés, seul plancher neuf = dallage sur terre-plein | **B-48 SANS OBJET** |

**Trois SANS OBJET proposés, à valider séparément :**

| Brique | Proposition | Motif de périmètre | Réserve |
|---|---|---|---|
| **B-41 — Fondations profondes** | **SANS OBJET** *(nouveau)* | **D-P4 : « fondations superficielles ancrées de 40 cm dans les alluvions anciennes »** — aucune fondation profonde au projet | Le sigle « RSO » reste non défini ; voir § 5.3 |
| **B-47 — Escaliers** | **SANS OBJET** | Aucun escalier neuf ; « modification escalier » = dépose et second œuvre, exclu du périmètre | Si la modification est structurelle, réactiver |
| **B-48 — Prédalles** | **SANS OBJET** | Voir DOC-09 | Aucune |

---

## 5. OBSERVATIONS D'INGÉNIEUR

### 5.1 Un déblocage réel, mais partiel

Les valeurs transmises débloquent **exactement deux variables** : SOL-01 (confortée) et surtout **SOL-02**, qui était la seule contrainte ELU manquante. C'est un gain substantiel : B-40 peut désormais calculer une capacité portante complète, ELS **et** ELU.

Mais trois variables de la même famille restent bloquantes, et **elles sont dans le même rapport** : SOL-06 (nappe), SOL-07 (tassements), SOL-04 (coupes). Or pour une reprise en sous-œuvre sur moellons anciens, la nappe et les tassements différentiels sont **au moins aussi déterminants que q**. Un ouvrage ancien supporte mal un tassement différentiel ; c'est précisément ce que le DIAG signale aux pieds de poteaux (« à la limite de l'admissible »).

### 5.2 L'ancrage : 40 cm ou 50 cm ? — **C-21**

C'est le point qui demande votre arbitrage immédiat.

| Pièce | Valeur | Formulation exacte |
|---|---|---|
| **D-P4** (client, 19/10/2026) | **0,40 m** | « Fondations superficielles ancrées de **40 cm** dans les alluvions anciennes » |
| **D2 p. 1** (EVEN, ind. C) | **≥ 0,50 m** | « RSO ancrées d'au moins **0,5 m** dans les Alluvions anciennes, capacité 3 bars ELS » |

L'écart n'est pas cosmétique : **10 cm représentent 25 % de la hauteur d'encastrement**. Sur une fondation superficielle en alluvions, l'encastrement intervient dans la capacité portante (terme de surcharge) et dans la protection contre l'érosion et le gel.

**Je ne tranche pas** (V1 : une contradiction se signale, elle ne s'arbitre pas en silence). Je propose la conduite suivante :

1. **Retenir provisoirement 0,50 m** pour les calculs B-40 — c'est la valeur la plus défavorable des deux, et elle émane du BET qui a rédigé le DCE ;
2. **Inscrire C-21 au RDR** et faire confirmer par EVEN Structures ou par le rapport GEOEXPERTS ;
3. Si le rapport confirme 0,40 m, B-40 sera recalculée — la différence de capacité portante sera quantifiée à ce moment.

### 5.3 Le sigle « RSO » — la déclaration client l'éclaire sans le résoudre

Votre précision « **fondations superficielles** » **écarte l'hypothèse de pieux ou micropieux** : c'est ce qui permet de proposer B-41 sans objet. Le sigle lui-même reste non défini (C-20), mais son effet pratique est désormais tranché. Il subsiste une ambiguïté résiduelle sur la seconde occurrence — « après stabilisation de la **RSO** » — qui pourrait désigner un ouvrage existant ; cela relève de B-23, pas de B-41.

### 5.4 Une observation sur le dictionnaire

Le dictionnaire rattache **SOL-04** (nature et succession des couches) à **B-41** uniquement. Or avec des fondations superficielles ancrées de 40 à 50 cm, la nature des couches est **directement nécessaire à B-40** : c'est elle qui confirme qu'on atteint bien les alluvions anciennes à cette profondeur, et non des remblais.

Je maintiens donc SOL-04 en **BLOQUANTE pour B-40 également**, en marge du rattachement du dictionnaire. Cette observation est consignée ici pour être reportée au journal des modifications (T-03) si vous la validez.

### 5.5 Ce qu'il reste à demander au rapport GEOEXPERTS

Trois extraits suffiraient, sans transmettre le dossier complet :

1. la **coupe géologique type** avec la profondeur du toit des alluvions anciennes (SOL-04, SOL-03) ;
2. le **niveau de nappe** et ses variations (SOL-06) ;
3. les **tassements admissibles** et le **classement XA réel** — le rapport dira XA1, XA2 ou XA3, jamais « XA4 » (SOL-07, C-15).

Avec ces trois éléments, **B-40 et B-43 passeraient en COMPLET**, et la seule réserve restante sur les fondations serait C-21.

---

## 6. AUTO-CONTRÔLE DU CRITÈRE D'ACCEPTATION

| Critère (fiche B-01) | État | Observation |
|---|---|---|
| Toute variable lue par une brique activée figure | ✅ | **63/63** traitées ; les 31 restantes listées en annexe § 3 |
| Tout NON NÉCESSAIRE porte un motif de périmètre | ✅ | 1 seul (DOC-09), motif de périmètre, jamais de disponibilité |
| Tout BLOQUANTE est rattaché à une brique identifiée | ✅ | 16 bloquantes, chacune rattachée |
| Tout À PRODUIRE PAR GO identifie la brique productrice | ✅ | 11 variables, producteur nommé |
| Aucune décision SANS OBJET prise sans validation | ✅ | **3 propositions** (B-41, B-47, B-48), aucune appliquée |

**Placeholders résiduels (V7)** : aucun.
**Valeurs de repli** : aucune. Les valeurs client sont **déclarées avec leur auteur et leur date** (§ 0bis), ce qui les distingue d'une valeur inventée.

---

## 7. POINT DE CONTRÔLE HUMAIN — validation ligne par ligne

**Sur les décisions client (§ 0bis) :**

1. Les quatre décisions **D-P1 à D-P4** sont-elles correctement retranscrites ? — *à confirmer mot pour mot*
2. **C-21** : retenez-vous provisoirement **0,50 m** pour les calculs, dans l'attente de la confirmation ?

**Sur les statuts :**

3. **DOC-09** → NON NÉCESSAIRE (aucune prédalle) — **oui / non**
4. **B-41 Fondations profondes** → SANS OBJET — **oui / non**
5. **B-47 Escaliers** → SANS OBJET — **oui / non**
6. **B-48 Prédalles** → SANS OBJET — **oui / non**
7. **Les 16 BLOQUANTES** → confirmez-vous qu'aucune ne peut être déclarée non nécessaire au périmètre ?
8. **SOL-04 rattachée aussi à B-40** (§ 5.4) — **oui / non**

**Décisions de fond encore ouvertes :**

9. **C-08** — recharge de sol de 15 cm : maintenir 100 daN/m², réviser, ou commander une note de charge ?
10. **C-10** — salle de sport 34,25 m² : quelle catégorie EC1 ?
11. **D5 (DXF)** — peut-il être fourni ?

Après validation, la MPD est **annexée au RDR (B-03)** comme décision D-xx et ne se modifie plus sans nouvelle décision datée.

---

*Brique B-01, indice B, livrée en proposition. Aucune brique aval engagée.*
