Fichier 10_ANNEXES/A_Conventions_Livrables.md — CARNAC v3.0
> Version du document : 3.0 (carnet CARNAC v3.0) — historique des modifications : 11_HISTORIQUE/Journal_des_modifications.md.
1. OBJET
Ce document fixe les conventions de production des livrables graphiques du carnet CARNAC. Elles s'appliquent à toutes les briques de production graphique (B-20, B-31, B-32, B-60) et à toutes les briques de calcul qui produisent des plans (B-40 à B-50).
Règle de stabilité : ces conventions sont figées. Une modification passe par une révision de carnet (voir 11_HISTORIQUE/Journal_des_modifications.md), jamais par une décision de brique.
Règle de non-ambiguïté : un élément graphique (cote, ferraillage, profilé, texte) ne peut exister que sur un seul calque. Un élément partagé entre deux calques est une anomalie de production.
________________


2. CALQUES DXF NORMALISÉS
2.1 Structure de nommage
{{TYPE}}-{{FONCTION}}
* {{TYPE}} : préfixe lié au type de livrable (voir §2.2)
* {{FONCTION}} : suffixe lié à la fonction du calque (voir §2.3)
2.2 Préfixes par type de livrable

| Type de livrable | Préfixe | Brique source |
| --- | --- | --- |
| Fondations | FOND- | B-40, B-41 |
| Verticaux BA | VERT- | B-42 |
| Planchers et dallages | PLANCHER- | B-43 |
| Charpente bois | CHARPENTE- | B-44 |
| Structure métallique | METAL- | B-45 |
| Maçonnerie | MACON- | B-46 |
| Escaliers | ESCALIER- | B-47 |
| Prédalles | PREDALLE- | B-48 |
| Linteaux et seuils | LINTEAU- | B-49 |
| Assemblages et ancrages | ASSEMBLAGE- | B-50 |
| Coupes et détails transverses | DETAIL- | B-60 |

2.3 Suffixes par fonction

| Suffixe | Contenu | Présence obligatoire |
| --- | --- | --- |
| -AXES | Axes, trames, points de calage, cotes de référence | Oui |
| -COFFRAGE | Contours, épaisseurs, cotations, réservations, joints | Oui |
| -ACIER-INF | Ferraillage inférieur (nappes, sections, espacements, recouvrements) | Oui si BA |
| -ACIER-SUP | Ferraillage supérieur (nappes, chapeaux, renforts) | Oui si BA |
| -ACIER-LONG | Barres longitudinales (verticaux BA) | Oui si verticaux BA |
| -ACIER-TRANS | Cadres et armatures transversales (verticaux BA) | Oui si verticaux BA |
| -PROFILES | Profilés métalliques (sections, positions, repères) | Oui si métal |
| -EXISTANT | Éléments existants à conserver (gris, trait fin) | Oui (même vide) |
| -DETAILS | Détails à grande échelle (1/20, 1/10, 1/5) | Oui |
| -NOMENCLATURE | Nomenclature des aciers, profilés, connecteurs | Oui |
| -HABILLAGE-TEXTE | Textes, légendes, cartouche, notes, tableaux | Oui |
| -COTATION | Cotations isolées (si volumineuses) | Non (optionnel) |

2.4 Règles d'usage
1. Un élément = un seul calque. Pas de calque fourre-tout, pas d'élément partagé entre deux calques.
2. Les calques -EXISTANT sont toujours présents, même vides. Leur absence est une anomalie de traçabilité.
3. Les calques -HABILLAGE-TEXTE et -NOMENCLATURE sont toujours présents et renseignés.
4. Aucun élément du livrable sur le calque 0 (calque par défaut AutoCAD).
5. Les calques de travail interne (DEFPOINTS, _Construction, _Grille) sont supprimés à l'export.
6. Les calques vides (sauf -EXISTANT) sont supprimés à l'export.
2.5 Exemple complet — Plan de fondations
text
FOND-AXES
FOND-COFFRAGE
FOND-ACIER-INF
FOND-ACIER-SUP
FOND-EXISTANT
FOND-DETAILS
FOND-NOMENCLATURE
FOND-HABILLAGE-TEXTE
________________


3. ÉCHELLES AUTORISÉES

| Échelle | Usage | Exemples |
| --- | --- | --- |
| 1/500 | Vue d'ensemble, plan de situation | Plan masse |
| 1/200 | Vue d'ensemble, plan d'étage | Plan de structure d'ensemble |
| 1/100 | Plans courants | Plan de coffrage d'étage |
| 1/50 | Plans d'exécution courants | Plan de fondations, plan de plancher |
| 1/20 | Détails courants, coupes de principe | Coupe de semelle, coupe de poteau |
| 1/10 | Détails d'assemblage | Détail de platine, détail de sabot |
| 1/5 | Détails singuliers | Ferraillage d'about, ancrage de barre |

Règle : une échelle hors de cette liste doit être justifiée dans le cartouche (mention « échelle exceptionnelle : [motif] »).
Règle de cohérence : sur un même plan, l'échelle du plan général et celles des détails sont indiquées séparément dans le cartouche.
________________


4. FORMATS DE SORTIE
4.1 Trois formats obligatoires
Chaque livrable graphique est produit en trois formats :

| Format | Usage | Nommage |
| --- | --- | --- |
| DXF | Échange avec outils, réutilisation par B-62 et B-64 | {{TYPE}}_EXE_{{indice}}.dxf |
| PDF | Impression, archivage, diffusion officielle | {{TYPE}}_EXE_{{indice}}.pdf |
| PNG | Diffusion rapide, insertion dans comptes rendus | {{TYPE}}_EXE_{{indice}}.png |

4.2 Cas particuliers

| Cas | Suffixe ajouté | Exemple |
| --- | --- | --- |
| Mode PARAMÉTRIQUE | _P | FOND_EXE_A_P.pdf |
| Mode PARTIEL-DÉCLARÉ | _D | FOND_EXE_B_D.pdf |
| Version provisoire (avant clôture B-71) | _PROV | FOND_EXE_A_PROV.pdf |
| Vue nettoyée (B-32) | _NET | FOND_VUE-NETTOYEE_A_NET.pdf |
| Preuve de superposition (B-31) | _SUP | FOND_PREUVE-SUP_A_SUP.pdf |

4.3 Résolution et qualité

| Format | Paramètre |
| --- | --- |
| PDF | Vectoriel, pas de rasterisation sauf pour les images importées |
| PNG | 300 dpi minimum, fond blanc, transparence désactivée |
| DXF | Version AutoCAD 2013 minimum (compatibilité descendante), unités en millimètres |

________________


5. CARTOUCHE TYPE
5.1 Zones du cartouche
Le cartouche comporte sept zones obligatoires :

| Zone | Position | Contenu |
| --- | --- | --- |
| Zone 1 | Haut gauche | Code projet (ID-01) et intitulé (ID-02) |
| Zone 2 | Haut droite | Logo ou nom de l'entreprise GO |
| Zone 3 | Centre | Intitulé du plan, type de livrable, niveau concerné |
| Zone 4 | Bas gauche | Indice, date, échelle, format |
| Zone 5 | Bas centre | Brique source (B-xx), mode d'exécution |
| Zone 6 | Bas droite | Numéro de plan, révision, visas |
| Zone 7 | Bandeau | Mentions obligatoires |

5.2 Contenu des zones
Zone 1 :
text
Code projet : {{ID-01}}
Intitulé : {{ID-02}}
Zone 2 :
text
Logo / nom entreprise GO
Zone 3 :
text
Intitulé : {{intitulé du plan}}
Type : {{type livrable}}
Niveau : {{niveau}}
Zone 4 :
text
Indice : {{A/B/C...}}
Date : {{JJ/MM/AAAA}}
Échelle : {{1/50, 1/20...}}
Format : {{A0/A1/A2/A3/A4}}
Zone 5 :
text
Brique source : {{B-xx}}
Mode : {{COMPLET / PARTIEL-DÉCLARÉ / PARAMÉTRIQUE / INTERNE-GO}}
Zone 6 :
text
N° plan : {{numéro}}
Révision : {{xx}}
Visas : {{BET / BC / MOE / MOA}}
Zone 7 (bandeau, texte fixe) :
text
NE PAS EXÉCUTER SANS EXE COTÉ ET VISA
Protection au feu adéquate à prévoir (hors lot GO)
[Si PARAMÉTRIQUE] PROVISOIRE — EN ATTENTE DE [donnée]
[Si PARTIEL-DÉCLARÉ] Établi sous hypothèse(s) déclarée(s) — voir RDR
5.3 Mentions fixes
Certaines mentions sont toujours présentes, quelle que soit la brique :

| Mention | Position |
| --- | --- |
| « NE PAS EXÉCUTER SANS EXE COTÉ ET VISA » | Zone 7 (bandeau) |
| « Protection au feu adéquate à prévoir (hors lot GO) » | Zone 7 (bandeau) |
| Indice et date | Zone 4 |
| Échelle | Zone 4 |
| Brique source et mode | Zone 5 |

________________


6. NOMENCLATURE TYPE
6.1 Structure de la nomenclature graphique
La nomenclature graphique intégrée au plan (produite par B-60) comporte au minimum les colonnes suivantes :

| Colonne | Contenu | Exemple |
| --- | --- | --- |
| Repère | Identifiant du repère sur le plan | F1, P2, S/P3 |
| Désignation | Nature de l'élément | Semelle filante, Poteau BA, Profilé HEB200 |
| Section / diamètre | Section ou diamètre | HA12, HEB200, 140×140×8 |
| Longueur / quantité | Longueur ou nombre | 3200 mm, 4 |
| Observations | Notes spécifiques | équerre, avec platine |

6.2 Structure de la nomenclature détaillée (B-62)
La nomenclature détaillée produite par B-62 comporte les colonnes suivantes :

| Colonne | Contenu | Unité |
| --- | --- | --- |
| Repère | Identifiant du repère | — |
| Désignation | Nature détaillée | — |
| Section / diamètre | Section ou diamètre | mm |
| Longueur unitaire | Longueur d'une barre ou d'un élément | mm |
| Nombre | Nombre d'occurrences | — |
| Longueur totale | Longueur cumulée | mm |
| Poids | Poids cumulé (acier uniquement) | kg |
| Calque source | Calque du plan B-60 d'où l'élément est extrait | — |

6.3 Nomenclature de façonnage (aciers BA)
Pour chaque type de barre, la nomenclature de façonnage comporte :

| Colonne | Contenu |
| --- | --- |
| Repère | Identifiant |
| Diamètre | HA6, HA8, HA10, HA12, HA14, HA16, HA20, HA25, HA32 |
| Forme | Droite, équerre, U, cadre, épingle, chapeau |
| Cotes de façonnage | Longueurs de chaque segment, angles |
| Longueur développée | Longueur totale dépliée (mm) |
| Longueur de recouvrement | Si applicable (mm) |
| Diamètre de mandrin | Si cintrage (mm) |
| Quantité | Nombre d'occurrences |

________________


7. UNITÉS ET PRÉCISIONS
7.1 Unités par type de valeur

| Type de valeur | Unité | Précision |
| --- | --- | --- |
| Cotes de plan | Millimètres (mm) | Entier |
| Cotes de niveau | Mètres (m) | 3 décimales |
| Sections de barres | Millimètres (mm) | Entier (HA12) |
| Sections de profilés | Millimètres (mm) | Entier (HEB200) |
| Longueurs développées d'acier | Millimètres (mm) | Entier |
| Poids d'acier | Kilogrammes (kg) | 1 décimale |
| Charges linéiques | kN/m | 2 décimales |
| Charges ponctuelles | kN | 2 décimales |
| Moments | kNm | 2 décimales |
| Contraintes | MPa | 1 décimale |
| Résistances | MPa | 1 décimale |
| Niveaux NGF | mètres | 3 décimales |

7.2 Règle de non-ambiguïté
Toute valeur numérique dans un livrable est suivie de son unité, sauf dans les tables où la colonne indique l'unité.
7.3 Arrondis

| Type de valeur | Règle d'arrondi |
| --- | --- |
| Cotes de plan | Arrondi à l'entier (mm) |
| Niveaux | Arrondi au millimètre |
| Sections d'acier | Arrondi à la section commerciale supérieure |
| Résultats de calcul | Arrondi à la précision affichée, jamais d'arrondi intermédiaire |

________________


8. RÈGLES DE NOMMAGE DES FICHIERS LIVRÉS
8.1 Format général
{{TYPE}}_EXE_{{indice}}.{{extension}}
8.2 Exemples

| Fichier | Contenu |
| --- | --- |
| FOND_EXE_A.dxf | Plan de fondations, indice A, DXF |
| FOND_EXE_A.pdf | Plan de fondations, indice A, PDF |
| FOND_EXE_A.png | Plan de fondations, indice A, PNG |
| VERT_EXE_B_P.pdf | Plan de verticaux, indice B, mode PARAMÉTRIQUE |
| PLANCHER_EXE_A_D.pdf | Plan de plancher, indice A, mode PARTIEL-DÉCLARÉ |
| FOND_VUE-NETTOYEE_A_NET.dxf | Vue nettoyée du plan de fondations |
| FOND_PREUVE-SUP_A_SUP.pdf | Preuve de superposition du plan de fondations |

8.3 Règles complémentaires
1. Pas d'espaces dans les noms de fichiers (remplacer par _).
2. Pas d'accents dans les noms de fichiers.
3. Pas de caractères spéciaux autres que _ et -.
4. Indice en majuscule (A, B, C...).
5. Extension en minuscule (dxf, pdf, png).
________________


9. RÈGLES DE VERSIONNAGE DES LIVRABLES
9.1 Indice des livrables
* Indice A : première émission
* Indice B, C, D... : révisions successives
* Un indice ne se saute pas : on ne passe jamais de A à C sans B
9.2 Motifs de révision
Une révision de livrable est justifiée par :
* une correction d'erreur (motif : correction)
* une modification de conception (motif : modification)
* un ajout d'élément (motif : ajout)
* une suppression d'élément (motif : suppression)
* une mise à jour de donnée source (motif : maj_source)
Le motif est consigné dans le RDL (B-71).
9.3 Supersession
Un nouveau livrable remplace et annule l'indice précédent. La mention figure dans le cartouche :
text
Ce livrable remplace et annule l'indice {{précédent}} du {{date}}.
________________


10. GESTION DES RÉSERVES SUR LES LIVRABLES
10.1 Livrables en mode dégradé

| Mode | Marque visuelle | Mention au cartouche |
| --- | --- | --- |
| COMPLET | Aucune | — |
| PARTIEL-DÉCLARÉ | Filigrane jaune | « Établi sous hypothèse(s) déclarée(s) — voir RDR » |
| PARAMÉTRIQUE | Filigrane rouge | « PROVISOIRE — EN ATTENTE DE [donnée] » |
| INTERNE-GO | Aucune (mode de conception, pas d'exécution) | Mention « Étude de conception — ne se substitue pas à l'EXE » |
| SANS OBJET | Pas de livrable | Ligne de justification au RDR |

10.2 Livrables en attente de données
Un livrable en mode PARAMÉTRIQUE :
* porte le filigrane « PROVISOIRE — EN ATTENTE DE [donnée] » ;
* est suffixé _P dans son nom de fichier ;
* mentionne la donnée manquante dans le cartouche (zone 7) ;
* n'est jamais diffusé comme livrable exécutable.
10.3 Livrables en attente de visa
Un livrable dont les visas ne sont pas obtenus porte la mention :
text
VISA EN ATTENTE : [BET / BC / MOE / MOA]
NE PAS EXÉCUTER
________________


11. CAS PARTICULIERS
11.1 Plans de principe (B-20)
Un plan de principe (B-20, mode INTERNE-GO) porte :
* le filigrane « PRINCIPE — NE PAS EXÉCUTER » ;
* un indice P (premier principe, P2, P3... pour les suivants) ;
* la mention « Étude de conception — ne se substitue pas à l'EXE ».
11.2 Vues nettoyées (B-32)
Une vue nettoyée (B-32) porte :
* la mention « Vue nettoyée — fond de plan uniquement » ;
* un nommage {{TYPE}}_VUE-NETTOYEE_{{indice}} ;
* un indice de version de la vue nettoyée, distinct de l'indice du livrable.
11.3 Preuves de superposition (B-31)
Une preuve de superposition (B-31) porte :
* la mention « Preuve de superposition » ;
* la mention du livrable vérifié (code + indice) ;
* la mention du fichier source utilisé (code + indice) ;
* un nommage {{TYPE}}_PREUVE-SUP_{{indice}}.
11.4 Notes de calcul
Une note de calcul (B-40 à B-50) porte :
* en en-tête : code projet, intitulé, indice, date, mode, brique source ;
* en pied : visas requis et mention « NE PAS EXÉCUTER SANS VISA » ;
* en annexe : liste des pièces jointes (plans, nomenclatures, preuves).
________________


12. RÈGLES DE DIFFUSION
12.1 Diffusion interne (GO)
Tous les livrables sont diffusés en interne, y compris les modes dégradés (PARTIEL-DÉCLARÉ, PARAMÉTRIQUE).
12.2 Diffusion externe (MOE, BC, MOA)
Seuls les livrables en mode COMPLET ou PARTIEL-DÉCLARÉ sont diffusés en externe. Les livrables PARAMÉTRIQUE ne sont diffusés qu'à titre informatif, avec mention explicite « provisoire, ne pas exécuter ».
12.3 Diffusion pour exécution (entreprise)
Seuls les livrables visés (BET, BC, MOE, MOA) sont diffusés pour exécution. Un livrable non visé porte la mention « NE PAS EXÉCUTER ».
________________


13. FICHIERS DE RÉFÉRENCE

| Fichier | Contenu |
| --- | --- |
| 01_DICTIONNAIRE/CARNAC_v3.0_variables.csv | Variables, dont LIV-01 à LIV-05 (conventions) |
| 11_HISTORIQUE/Journal_des_modifications.md | Modifications de ces conventions |
| 07_PHASE_5_LIVRABLES/B-60_Plans_Execution.md | Brique de production graphique |
| 07_PHASE_5_LIVRABLES/B-62_Nomenclature.md | Brique de nomenclature détaillée |

________________
---

## 11. COMPLÉMENT v2.0 — TOLÉRANCES D'EXÉCUTION ET ENROBAGE
1. Les plans d'exécution sont établis pour la classe d'exécution déclarée en note d'hypothèses (NF EN 13670) ; les tolérances qui affectent le calcul sont celles de cette classe.
2. L'enrobage figuré sur les plans est l'enrobage nominal c_nom = c_min + Δc_dev (EC2 §4.4), avec Δc_dev = 10 mm sauf justification contraire portée en FDC (MAT-03).
3. Les cotes de plan sont en millimètres (entiers) ; les cotes de niveau en mètres (3 décimales). Aucune autre convention d'unités n'est admise sur un livrable (corrige la contradiction d'unités historique entre la présente annexe et la fiche B-60).

---

## 8. PURETÉ STRUCTURELLE, HYPOTHÈSES NOTIFIÉES ET CONTRÔLE DE RENDU (nouveau en v3.0)

### 8.1 Loi d'airain graphique — zéro second œuvre
Sur **tout** plan de structure produit par le carnet (plans de principe, plans de coffrage, plans d'implantation, plans de ferraillage, coupes et détails), sont **interdits** :
* les cloisons, doublages, contre-cloisons et complexes de finition ;
* les isolants thermiques et acoustiques, y compris les complexes isolants périphériques des façades ;
* les menuiseries de distribution intérieure, les revêtements, les faux plafonds et le mobilier.

Sont **autorisés et attendus** : les éléments porteurs (existants, conservés, démolis, neufs), les ouvertures mécaniques (baies, trémies, percements, réservations), la trémie et l'escalier, la structure neuve, les attentes et scellements, les axes et trames, les cotations et les repères.

### 8.2 Différentiel graphique `EXISTANT / DÉMOLITION / PROJET`
Chaque vue structurelle porte trois états graphiques distincts et une légende normalisée :
| État | Calque | Convention graphique |
| --- | --- | --- |
| EXISTANT conservé | `*-EXISTANT` | trait fin, gris |
| EXISTANT démoli | `*-EXISTANT` + suffixe `-DEM` | trait pointillé, gris clair, hachures de démolition |
| PROJET neuf | calques de fonction (`-COFFRAGE`, `-ACIER-*`, `-PROFILES`) | trait fort, noir ou couleur de fonction |

Une vue qui ne permet pas de distinguer les trois états est refusée (V15).

### 8.3 Hypothèses notifiées `H-xx`
Toute valeur issue du mode `HYPOTHÈSE-NOTIFIÉE` est reportée :
1. sur les plans, par un **nuage graphique** fermé entourant la zone concernée, avec le repère `H-xx` en texte lisible ;
2. en tête de note, par un encadré listant valeur, norme d'appui, zone d'application et délai de contradiction (`DEC-06`) ;
3. dans le tableau des hypothèses du livrable, avec le statut (active, expirée, acceptée, contredite).

Une hypothèse sans norme d'appui n'est pas notifiée : c'est une valeur de repli interdite (V3).

### 8.4 Prescriptions chantier `ENC` et Points d'Arrêt `PA-xx`
Toute inconnue physique est portée par un encadré `ENC` (prescription opposable : sondage, dépose, fouille, curage, essai) et par un Point d'Arrêt `PA-xx` (arrêt de production avant poursuite, avec critère de lever et conséquence chiffrée).

**v3.0.1.** Le mot-pour-mot vit **en note**. Sur le plan : **un** encadré `ENC` de **cinq lignes maximum**, lisible à 1 m. Un mur de douze alinéas sur le dessin est une non-conformité de présentation (`LIV-06`, addendum A1).

### 8.7 Présentation (v3.0.1 — `LIV-06` / `LIV-07`)
- Fond blanc, existant gris léger extrait, ouvrages neufs en couleur simple.
- Implantation obligatoire sur le niveau concerné ; coupe type hachurée.
- Notes : ordre §0 hypothèses → matériaux → charges → géométrie → DDC → vérifs → points à lever ; codes CARNAC en annexe.
- Voir `10_ANNEXES/A1_Addendum_v3.0.1.md`.

### 8.5 Contrôle de rendu obligatoire (`0` collision)
Aucun plan n'est diffusé avant contrôle automatisé, journalisé au format de l'annexe O §7 :
| Contrôle | Seuil |
| --- | --- |
| Chevauchement de textes | 0 |
| Cote orpheline (sans entité cotée à moins de 22 cm) | 0 |
| Entité sur le calque `0` | 0 |
| Entité de second œuvre sur un calque de structure | 0 |
| Titre du plan non couvert par le contenu géométrique | 0 (vérité du titre) |
| Réservation non reportée depuis le carnet B-34 | 0 |

### 8.6 Plan de réservations (B-34)
Le plan de réservations est établi sur le fond structurel pur, avec tableau intégré (repère, niveau, élément porteur, position, dimensions, altitude, lot, statut). Il porte les mêmes axes et les mêmes repères que les plans de coffrage, et il est référencé dans la notice de synthèse.
