# D5 — INVENTAIRE DU FICHIER DXF INDICE C

| Champ | Valeur |
|---|---|
| Pièce | **D5** — `208_FLORA_Plans_DCE_IndC.dxf` |
| Origine | Google Drive, dossier **Croissy** (fichier `1L_0lz6iiDve54dYDoIcAxjhNsD_8LXUd`) |
| Taille | **4 399 016 octets** |
| SHA-256 | `45f41e3113a909cef201ec4bb466d95cd82307ed6cd3fa9e016b69e53b39dcf1` |
| Format | DXF **AC1032** (AutoCAD 2018), encodage cp1252 |
| Date de relevé | **19/10/2026** |
| Méthode | **`ezdxf` 1.4.5** — script `_scripts/dxf_inventaire.py`, journal `_rendus/dxf_inventaire.txt` *(V13)* |

---

## 1. CE QUE LE FICHIER EST

**Un fichier d'architecte — plans d'aménagement intérieur, indice C.** Ce n'est **pas** un fichier de BET structure.

| Indice | Valeur relevée |
|---|---|
| Unités déclarées (`$INSUNITS`) | **5 = centimètres** — *GEO-06 soldé* |
| Unité de mesure (`$MEASUREMENT`) | 1 = métrique |
| Emprise du modèle | X 240 → 18 395 cm · Y −1 931 → 8 321 cm |
| Limites de présentation | 420 × 297 (A3, en mm) |
| Espace objet (modelspace) | **1 582 entités** |
| Calques | **31** |
| Blocs nommés | **46** |
| Textes (TEXT + MTEXT) | **513** |
| Cotes (DIMENSION) | **163** |

### 1.1 Vues présentes

| Vue | Titre relevé | Position (cm) |
|---|---|---|
| RDC FlorA — **existant** | « RDC FLORA / Existant » | (3 639 ; 4 206) |
| R+1 Flora — **existant** | « R+1 FLORA / Existant » | (2 866 ; 355) |
| RDC — **projet** | « RDC » | (10 203 ; 4 125) |
| R+1 — **projet** | « R+1 / Projet » | (9 430 ; 355) |
| Repères d'axes | « EXISTANT » / « PROJET » | (266 ; 8 265) et (6 830 ; 8 265) |

---

## 2. CE QUE LE FICHIER NE CONTIENT PAS — ET C'EST DÉCISIF

| Recherche | Résultat |
|---|---|
| Calque **fondation / semelle / coffrage** | **Aucun** |
| Calque **béton / acier / ferraillage** | **Aucun** |
| Calque **charpente / structure** | **Aucun** |
| Altimétrie (NGF, ± 0.00, cote de niveau) | **Aucune occurrence** dans les 513 textes |
| Repères d'axes nommés (A, B, C / 1, 2, 3) | **Aucun** — le calque `090_repères-axes` porte 9 entités **sans texte** |

**Vocabulaire des 22 calques effectivement peuplés :**

`020_cloi` (259) · `078_textes-2` (339) · `070_trait-fin` (173) · `040_meubles` (160) · `077_textes-1` (133) · `075_cotation` (104) · `030_menuiserie` (83) · `080_plomb-cvc` (70) · `100 TEXTE PMR` (62) · `102_demol` (22) · **`010_mur` (20 seulement)** · `092_surfaces projet` (13) · `090_repères-axes` (9) · `051_plafonds` (6) · `31_sanitaires` (4) · `050_sols` (2).

Les blocs insérés confirment la nature du fichier : `tapis yoga`, `cerceau`, `barre`, `table d'examen`, `chai`, `wc suspendu`, `mitigeur`, `CERCLE pmr`. **C'est un plan d'aménagement, pas un plan de structure.**

---

## 3. CE QUE LE FICHIER APPORTE QUAND MÊME

### 3.1 Géométrie mesurée du projet — **GEO-01**

Les **13 polylignes de surface** du calque `092_surfaces projet` donnent la géométrie réelle des pièces.

| Étage | Nombre de pièces cotées | Surface cumulée | Emprise X | Emprise Y |
|---|---|---|---|---|
| **RDC projet** | 10 | 84,77 m² ⚠ **somme de surfaces hachurées — pas une surface de plancher** *(voir erratum § 6bis)* | 85,87 → 95,77 m (**9,90 m**) | 44,43 → 62,92 m (**18,49 m**) |
| **R+1 projet** | 3 | ~~6,03 m²~~ ❌ **RETIRÉ** — 2 faux plafonds + 1 dégagement *(voir erratum § 6bis)* | 86,82 → 89,51 m (2,69 m) | 14,56 → 17,24 m (2,68 m) |

**Le RDC du projet occupe une bande de 9,90 m × 18,49 m.** C'est la première fois que cette emprise est mesurée sur une géométrie vectorielle et non lue sur un cartouche.

> **Réserve de méthode** : ces mesures sont issues des **surfaces de pièces**, non du contour extérieur des murs. Elles donnent une emprise **intérieure** et ne remplacent pas une cote d'ensemble. Elles constituent en revanche une base exploitable pour B-30 (calage) et pour vérifier les cotes de D2.

### 3.2 Le bloc `Murs porteurs selon geometre projet`

Inséré **2 fois**. C'est le seul élément du fichier qui porte une information de structure — et il provient du **géomètre**, pas du BET. Il reprend les murs porteurs relevés, ce qui **n'est pas** un plan de structure.

### 3.3 Démolition — calque `102_demol` (22 entités)

Emprise X 151,45 → 161,39 m · Y 9,46 → 57,55 m. Recoupe le plan de démolition D4 p. 5 et les murs démolis de la contradiction **C-12**.

---

## 4. CONSÉQUENCE SUR LE REGISTRE — CE QUI SE FERME ET CE QUI NE SE FERME PAS

| Réserve / verrou | État avant | **État après lecture du DXF** |
|---|---|---|
| **R-24** — DXF indice C non fourni | Ouverte | ✅ **FERMÉE** — le fichier existe, il est lu, il est exploitable |
| **GEO-06** — unités | VERROU | ✅ **FERMÉ** — `$INSUNITS = 5`, centimètres |
| **GEO-07** — transformation | VERROU | ⚠ **OUVERT** — aucune référence commune avec D2 ; c'est l'objet de **B-30** |
| **GEO-08** — points de calage | VERROU | ⚠ **OUVERT** — aucun repère d'axe nommé dans le fichier |
| **V-18** — suspension totale du calage | Actif | **RÉDUIT** — de « suspension totale » à **PARTIEL-DÉCLARÉ** : B-30 à B-33 deviennent exécutables |
| **B-60** — plans d'exécution | Suspendue | ⚠ **TOUJOURS SUSPENDUE, mais pour une autre raison** — voir ci-dessous |
| **GEO-01** — cote d'ensemble | VERROU | **RÉDUIT** — emprise intérieure mesurée (9,90 × 18,49 m) ; cote extérieure toujours absente |

### 4.1 Le point qu'il faut dire sans détour

**R-24 est fermée, mais B-60 ne se débloque pas pour autant.** La raison a changé de nature :

- avant : *« pas de fichier vectoriel, donc aucune preuve géométrique possible »* → c'était un **manque de pièce** ;
- maintenant : *« le fichier vectoriel est celui de l'architecte ; il ne contient aucune fondation, aucun coffrage, aucune altimétrie »* → c'est un **manque de contenu**.

Les fondations n'existent, dans le DCE, que sur **D2 folio 03** — un PDF. Le DXF ne les porte pas. Produire un plan de fondations exigerait donc de **vectoriser D2**, ce qui est possible mais qui reste une **reconstruction**, pas une extraction.

**Je ne présente donc pas R-24 comme un déblocage complet.** Elle libère le calage (B-30 à B-33) et la géométrie d'architecte ; elle ne libère pas les plans de structure.

---

## 5. NOUVELLE RÉSERVE PROPOSÉE — **R-37**

**« Absence de contenu structurel et altimétrique dans D5 »** — le DXF indice C est un fichier d'architecte : aucun calque de fondation, de coffrage, de béton armé ou de charpente ; aucune altimétrie ; aucun repère d'axe nommé. **Conséquence** : les plans d'exécution de structure (B-60) ne peuvent pas être dérivés de D5 et devront être reconstruits depuis D2 (PDF). **Criticité** : Production. **Responsable** : MOE. **Échéance** : avant B-60.

---

## 6. TRAÇABILITÉ V13

| Élément | Valeur |
|---|---|
| Script d'inventaire | `_scripts/dxf_inventaire.py` |
| Script de découpage | `_scripts/dxf_feuilles.py` |
| Journal d'inventaire | `_rendus/dxf_inventaire.txt` |
| Journal de découpage | `_rendus/dxf_feuilles.txt` |
| Bibliothèque | `ezdxf` **1.4.5**, installée le 19/10/2026 |
| Empreinte d'entrée | SHA-256 consigné ci-dessus |
| Avertissements d'ouverture | ezdxf signale des `FIELD` et `ACDB_BLOCKREPRESENTATION_DATA` ignorés au chargement — **sans effet** sur la géométrie, les calques et les textes |

> Le fichier est stocké dans `google_drive/`, **exclu du versionnement** (`.gitignore`) mais **persisté dans l'espace de travail**. Il ne doit pas être déplacé hors de l'espace : la persistance en dépend.

---

*Inventaire établi le 19/10/2026 — pièce **D5**, à reporter en B-00 (indice C), B-03 (indice G) et B-04 (indice B).*

---

## 6bis. ERRATUM DU 19/10/2026 — LES DEUX SURFACES ÉTAIENT FAUSSES

**Ce que l'inventaire indiquait** : « RDC 84,77 m² », « R+1 6,03 m² ».

**Ce que le calage B-30 indice B a établi** :

| Valeur | Statut | Motif |
|---|---|---|
| **84,77 m²** (RDC) | ⚠ **N'est pas une surface de plancher** | Somme de 10 polygones du calque `092_surfaces projet`, qui mélange des **pièces** (9,60 · 5,10 · 4,75 · 5,19 m², étiquetées) et des **faux plafonds** (16,08 m² « fp demontable », 5,49 m²) |
| **6,03 m²** (R+1) | ❌ **FAUX — retiré** | Somme de 3 polygones : **1,49 m²** faux plafond fixe · **2,37 m²** faux plafond (sèche-serviettes) · **2,16 m²** dégagement avec trappe combles. **Deux sur trois ne sont pas des sols** |

**Le calque `092_surfaces projet` n'est pas un plan de surfaces de plancher.** C'est un calque de **hachures de projet** — pièces et plafonds mêlés. Aucune surface de plancher ne peut en être déduite par sommation.

**Surface réelle du RDC** : **111,15 m²** — somme des 9 locaux des planches de détail D4 (p. 11 à 15), dont le **Plateau technique 33,14 m²** et l'**Entrée 9,24 m²** qui **ne figurent sur aucune hachure** de ce calque. Le calque omet donc deux des locaux les plus grands.

**Surface réelle du R+1** : **106,92 m²** (10 espaces nommés ; **101,79 m²** hors palier de 2,97 m² et dégagement de combles de 2,16 m²) — somme des 8 locaux du programme **D4 p. 6 et 9** (B-00 § 2.9), concordante avec les 8 étiquettes de surface de la vue R+1 de D5. Ce n'est pas une surface de plancher au sens réglementaire (murs et circulations non comptés), mais c'est le chiffre opposable.

**Double assurance** : les 11 cotes Z relevées dans D5 sont **identiques au centimètre** à celles des PDF de D4 (p. 4, 6, 9, 10, 23-25), qui portent en outre l'altimétrie de toiture (p. 26-27) **absente de D5**. Le DXF est donc **moins complet que le PDF**.

**Ce qui reste valide dans cet inventaire** : la géométrie (emprise 9,90 × 18,49 m), les comptages d'entités, les calques, les 13 étiquettes d'aire — toutes vérifiées au centième par le script B-30 (écart maximal 0,005 m²).

**Source de la correction** : `03_CALAGE/B-30_Calage.md`, indice B, § 0 et § 3.
