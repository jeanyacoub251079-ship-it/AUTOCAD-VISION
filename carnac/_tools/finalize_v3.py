#!/usr/bin/env python3
"""Finalisation de CARNAC v3.0 : annexes, historique, symétrisation du graphe amont/aval, compilation."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path("/home/user/AUTOCAD-VISION/carnac")
DST = BASE / "CARNAC_v3.0"
sys.path.insert(0, str(BASE / "_tools"))
from carnac_lint import expand_brick_range  # noqa: E402

# ---------------------------------------------------------------- nettoyage
for stale in [
    DST / "01_DICTIONNAIRE" / "CARNAC_v2.6_variables.md",
    DST / "01_DICTIONNAIRE" / "CARNAC_v2.6_variables.csv",
]:
    if stale.exists():
        stale.unlink()

# ------------------------------------------------------- corrections ciblées
def fix(path: Path, pairs: list[tuple[str, str]]) -> None:
    t = path.read_text(encoding="utf-8")
    for a, b in pairs:
        t = t.replace(a, b)
    path.write_text(t, encoding="utf-8")


fix(DST / "10_ANNEXES" / "C_Journal_Revisions.md", [
    ("> Version du document : 2.5 (carnet CARNAC v2.6)", "> Version du document : 3.0 (carnet CARNAC v3.0)"),
    ("CARNAC_v3.0_variables.csv", "CARNAC_v1.1_variables.csv"),
])
fix(DST / "10_ANNEXES" / "O_Outillage.md", [
    ("> Version du document : 2.5 (carnet CARNAC v2.6)", "> Version du document : 3.0 (carnet CARNAC v3.0)"),
    ("# Annexe O — COUCHE OUTILLAGE (nouveau en v2.0)", "# Annexe O — COUCHE OUTILLAGE ET PROTOCOLE CAO (refondue en v3.0)"),
])
fix(DST / "00_MASTER.md", [
    ("Les treize premiers verrous sont conservés depuis la v2.6 sans aucune suppression",
     "Les treize premiers verrous sont conservés depuis la version précédente sans aucune suppression"),
])
fix(DST / "10_ANNEXES" / "A_Conventions_Livrables.md", [
    ("# 10_ANNEXES/A", "# 10_ANNEXES/A"),
])

# ------------------------------------------------------------- annexe A §8
ANNEXE_A = """

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
Toute inconnue physique est portée par un encadré `ENC` (prescription opposable : sondage, dépose, fouille, curage, essai) et par un Point d'Arrêt `PA-xx` (arrêt de production avant poursuite, avec critère de lever et conséquence chiffrée). L'encadré figure **à la fois** sur le plan et en tête de la note, mot pour mot.

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
"""

p = DST / "10_ANNEXES" / "A_Conventions_Livrables.md"
p.write_text(p.read_text(encoding="utf-8").rstrip() + ANNEXE_A, encoding="utf-8")

# ------------------------------------------------------------- annexe O §9
ANNEXE_O = """

---

## 9. PROTOCOLE CAO DE NETTOYAGE STRUCTUREL (nouveau en v3.0)

Le nettoyage d'un fond de plan n'est jamais une suppression « au feeling » : c'est une suite de quatre opérations contrôlées, scriptées et journalisées.

### 9.1 Étape 1 — Reconnaissance des blocs et reclassement (`INSERT` récursif)
1. Parcours récursif de toutes les références de blocs (`INSERT`), y compris imbriquées.
2. Pour chaque entité rencontrée, détermination du calque *effectif* (calque du bloc, calque de l'insertion, calque des entités internes) : le calque porteur est celui de l'entité interne, jamais celui de l'insertion.
3. Reclassement des entités porteuses sur le calque structurel normalisé (annexe A §2) **avant** toute purge : une purge réalisée avant reclassement détruit des porteurs.
4. Journal : nombre de blocs parcourus, profondeur maximale, entités reclassées par calque d'origine et de destination.

### 9.2 Étape 2 — Retrait du complexe isolant et des doublages
1. Identification des enveloppes de doublage par épaisseur, position relative au nu porteur et calque d'origine.
2. Suppression de l'enveloppe, conservation du **nu porteur** (le plan de structure cote le nu brut, jamais le nu fini).
3. Report systématique de la correspondance `nu brut ASB / nu fini` et `Plan Archi N / PB / PH` dans la table `NIV-07` (§9.5).
4. Journal : épaisseurs retirées par façade, nu conservé, écarts de niveau induits.

### 9.3 Étape 3 — Purge spatiale des portes, cotes et hachures orphelines
1. Détection des entités non porteuses : portes, fenêtres, mobilier, hachures de revêtement, cotes de second œuvre.
2. Filtrage par distance : une entité est conservée si elle est à moins de 22 cm d'un segment porteur **et** si sa fonction est mécanique (baie, percement, trémie) ; sinon elle est purgée.
3. Contrôle inverse obligatoire : aucune ouverture mécanique réelle ne doit disparaître. Le script compare le nombre d'ouvertures avant/après et exige l'égalité sur les baies et trémies déclarées.
4. Journal : entités purgées par catégorie, ouvertures conservées, écart éventuel justifié.

### 9.4 Étape 4 — Recalage multi-sources vers le Repère Structurel Unique (`RSU`)
1. Pour chaque source vectorielle secondaire (plan structure MOE en PDF vectoriel, DXF de diagnostic, relevé géomètre), extraction des tracés et des textes.
2. Appariement des points homologues avec la source de référence, puis calcul de la transformation (similarité : translation, rotation, échelle ; affinité seulement si anisotropie justifiée).
3. Mesure du résidu sur des points témoins **non utilisés** au calage, avec seuils de l'annexe A et du document maître §5.
4. Consignation dans la matrice `GEO-13` : source, indice, points appariés, transformation, résidu maximal, résidu acceptable, statut.
5. Journal : nombre de sources recalées, résidus, sources refusées et motif.

### 9.5 Table de correspondance des niveaux et des épaisseurs (`NIV-07`)
| Plan architecte | Plancher bas (PB) | Plancher haut (PH) | Nu brut ASB | Nu fini | Épaisseur de complexe |
| --- | --- | --- | --- | --- | --- |
| Niveau `N` | cote `PB_N` | cote `PH_N` | cote `ASB_N` | cote `FINI_N` | `FINI_N − ASB_N` |

Règle : aucune cote de niveau n'est reprise d'un plan architecte sans passer par cette table. Un écart non renseigné est un écart bloquant pour B-43 et B-60.

### 9.6 Contrôle de rendu et anti-collision de textes
1. Extraction de toutes les entités texte et de leurs boîtes englobantes réelles (après rotation).
2. Détection des chevauchements deux à deux ; seuil exigé : `0` chevauchement sur tout plan diffusé.
3. Détection des cotes orphelines (aucune entité cotée à moins de 22 cm) et des entités sur le calque `0`.
4. Détection des entités de second œuvre résiduelles sur les calques de structure.
5. Journal : nombre de textes contrôlés, collisions détectées, collisions corrigées, collisions résiduelles (doit être nulles).
"""

p = DST / "10_ANNEXES" / "O_Outillage.md"
p.write_text(p.read_text(encoding="utf-8").rstrip() + ANNEXE_O, encoding="utf-8")

# ------------------------------------------------------------- annexe D
ANNEXE_D = """

---

## ORDONNANCEMENT v3.0 — MODE D'EMPLOI EN 6 PHASES (remplace l'ordre v2.x)

> L'ordre historique du présent document (cadrage → analyse → conception → calage → calculs → livrables → clôture) est conservé ci-dessus comme archive de lecture. Il est **remplacé**, pour toute exécution à compter de la v3.0, par l'ordonnancement suivant, qui remonte le socle géométrique en phase 1.

### Phase 0 — Cadrage et qualification (B-00 à B-04)
1. `B-00` : inventaire des pièces, contradictions à chaud, mission reformulée, **qualification `CFG-01`** (aucun BET MOE / PDF MOE / vecteurs MOE / mission partielle) et inventaire vectoriel de chaque pièce.
2. `B-01` : MPD, **gabarit `CFG-02`** (`S` / `M` / `L-XL`) et **découpage `CFG-03`** (blocs, joints de dilatation, niveaux-types).
3. `B-02` : FDC, avec la table `NIV-07` (PB / PH / ASB / Fini / 0,00 relatif).
4. `B-03` : RDR à quatre registres (`D-xx`, `H-xx`, `PA-xx`, `V-xx`).
5. `B-04` : PTD, blocages locaux, briques contournables.

### Phase 1 — Socle géométrique et nettoyage (B-30 → B-32 → B-31)
1. `B-30` : calage multi-sources vers le Repère Structurel Unique, matrice `GEO-13`, résidus sur points témoins.
2. `B-32` : vue nettoyée différentielle, protocole CAO en quatre temps (annexe O §9), `0` cloison et `0` isolant.
3. `B-31` : preuve de superposition multi-étages et multi-sources, détection des porteurs non portés (`V15`).
**Aucune brique des phases 2 à 6 ne s'engage sur un fond non calé et non nettoyé.**

### Phase 2 — Audit croisé multi-pièces (B-10 à B-15)
Audits sur fond calé (`B-10`, `B-11`, `B-12`), contradictions et réconciliation quantitative (`B-13`), périmètre de lot (`B-14`), risques et **Pré-Audit Flash d'Exécutabilité** (`B-15`), avec preuve d'épuisement `V14` avant toute déclaration d'absence.

### Phase 3 — Conception et synthèse structurelle (B-20 → B-25 → B-21 → B-22 → B-23 → B-24)
Synthèse indissociable sur fond nettoyé (`B-20`), stabilité globale et contreventement (`B-25`), descente de charges (`B-21`), hypothèses `H-xx` (`B-22`), exploitation du diagnostic (`B-23`), existant non sondé et `PA-xx` (`B-24`).

### Phase 4 — Calculs d'exécution (B-40 à B-50)
Notes scriptées, hypothèses actives citées, prescriptions `ENC` et `PA-xx` reportées, flèches sous maçonnerie vérifiées, assemblages renvoyés à `B-50`.

### Phase 5 — Synthèse des réservations et livrables (B-34 → B-60 → B-62 → B-64)
Carnet de réservations (`B-34`), plans d'exécution purs (`B-60`), nomenclature extraite du DXF relu (`B-62`), notice de synthèse (`B-64`).

### Phase 6 — Vérification croisée et clôture (B-33 → B-70 → B-71 → B-72)
Vérification croisée globale (`B-33`), auto-contrôle de synthèse (`B-70`), indiçage (`B-71`), journal de clôture (`B-72`).

### Points de contrôle humain par phase
| Phase | Validation humaine obligatoire |
| --- | --- |
| 0 | Qualification `CFG-01`, gabarit `CFG-02`, MPD ligne à ligne, table `NIV-07` |
| 1 | Résidus de calage, périmètre de nettoyage, différentiel `EXISTANT / DÉMOLITION / PROJET` |
| 2 | Classement gravité × nature des contradictions, risques résiduels acceptés |
| 3 | Système de contreventement, hypothèses `H-xx` et leur délai, Points d'Arrêt `PA-xx` |
| 4 | Sections et ferraillages retenus, hypothèses actives citées |
| 5 | Indice des plans, carnet de réservations, titre véridique, `0` collision |
| 6 | Verdict global, supersession, points ouverts à la clôture |
"""

p = DST / "10_ANNEXES" / "D_Mode_Emploi.md"
p.write_text(p.read_text(encoding="utf-8").rstrip() + ANNEXE_D, encoding="utf-8")

# ------------------------------------------------------------- annexe C §3.5
ANNEXE_C = """

### 3.5 Version v3.0 — refonte majeure (posture BET d'exécution)

**Nature** : version majeure d'architecture méthodologique. Aucun verrou supprimé, aucune brique supprimée.

**Contenu** :
* deux verrous nouveaux : `V14` (indissociabilité du corpus et preuve d'épuisement) et `V15` (différentiel temporel et continuité mécanique descendante) ;
* un sixième mode : `HYPOTHÈSE-NOTIFIÉE`, avec tripartition des incertitudes (Classe I normative, Classe II physique, Classe III rédhibitoire) ;
* ordonnancement inversé : socle géométrique (`B-30`, `B-32`, `B-31`) en phase 1 ; `B-33` en vérification croisée finale ;
* deux briques nouvelles : `B-25` (stabilité globale, contreventement, joints de dilatation, sismique) et `B-34` (synthèse des réservations et interfaces techniques) ;
* trois gabarits d'opération (`S`, `M`, `L-XL`) et quatre configurations d'entrée (`CFG-1` à `CFG-4`) ;
* loi d'airain graphique (zéro cloison, zéro isolation, zéro doublage), vérité du titre et contrôle `0` collision de textes ;
* dictionnaire porté de 94 à 106 variables, avec restauration des libellés `LIV-01` et `LIV-03` et douze variables nouvelles ;
* conversion intégrale des tableaux en tables Markdown normalisées, alignement des mentions de version, correction des compteurs et symétrisation intégrale du graphe amont/aval ;
* contrôle automatique obligatoire `10/10 PASS` avant publication.

**Compatibilité** : les numéros de briques existants sont conservés (aucun renumérotage), afin de ne casser ni les archives de projet antérieures ni les références documentaires en cours.
"""

p = DST / "10_ANNEXES" / "C_Journal_Revisions.md"
t = p.read_text(encoding="utf-8")
marker = "\n________________\n"
idx = t.rfind("### 3.4")
if idx == -1:
    t = t.rstrip() + ANNEXE_C
else:
    t = t.rstrip() + ANNEXE_C
p.write_text(t if t.endswith("\n") else t + "\n", encoding="utf-8")

# ------------------------------------------------------------- journal v3.0
JOURNAL = """# Journal des modifications — CARNAC v3.0
> Version du document : 3.0 (carnet CARNAC v3.0) — ce journal fait foi de la version en vigueur.

## ENTRÉE v3.0 — REFONTE MAJEURE (20/10/2026)

**Nature** : refonte majeure d'architecture méthodologique. Tous les verrous `V1` à `V13` sont conservés conformément au §8.3 du document maître (non-régression) ; aucun n'est supprimé. Aucune brique existante n'est supprimée et aucun numéro de brique n'est modifié.

### 1. Corrections d'erreurs héritées de la version précédente

| N° | Nature | Objet | Fichiers impactés |
| --- | --- | --- | --- |
| E-02 | Correction | Restauration des libellés corrompus `LIV-01` (« Conventions de calques DXF ») et `LIV-03` (« Formats de sortie »), remplacés à tort par la valeur `B-61` lors de la reconstruction v2.0 | 01_DICTIONNAIRE |
| E-03 | Correction | Restauration de la mention d'archive `CARNAC_v1.1_variables.csv` en Annexe C §3.2, écrasée par un remplacement global | 10_ANNEXES/C_Journal_Revisions.md |
| E-04 | Correction | Alignement des mentions de version résiduelles (`T-03` restée en v1.1, bandeaux en v1.5) et du compteur de verrous (« douze verrous » → quinze) | 09_TRANSVERSE/T-03, 00_MASTER, annexes |
| E-05 | Correction | Alignement des placeholders entre le bloc `2. PROMPT` et la ligne `Rappel V7` sur les fiches concernées | B-30, B-32, B-60, B-62, B-64, B-70 |

### 2. Modifications de principe

| N° | Nature | Objet | Fichiers impactés |
| --- | --- | --- | --- |
| C-06 | Ajout | Douze variables nouvelles : `CFG-01` à `CFG-03`, `DEC-05` à `DEC-07`, `GEO-13`, `GEO-14`, `NIV-07`, `STR-01` à `STR-03` | 01_DICTIONNAIRE, 39 fiches |
| C-07 | Refonte | Document maître : posture BET d'exécution, `CFG-1..4`, gabarits `S/M/L-XL`, quinze verrous, six modes, ordonnancement en 6 phases | 00_MASTER.md |
| C-08 | Enrichissement | Annexe A §8 : pureté structurelle, différentiel graphique, nuages `H-xx`, encadrés `ENC`/`PA-xx`, contrôle `0` collision | 10_ANNEXES/A_Conventions_Livrables.md |
| C-09 | Enrichissement | Annexe O §9 : protocole CAO en quatre temps, recalage multi-sources, table `NIV-07`, anti-collision | 10_ANNEXES/O_Outillage.md |
| C-10 | Refonte | Annexe D : ordonnancement v3.0 en 6 phases et points de contrôle humain par phase | 10_ANNEXES/D_Mode_Emploi.md |
| C-11 | Mise à jour | Annexe C §3.5 : version v3.0 | 10_ANNEXES/C_Journal_Revisions.md |
| C-12 | Enrichissement | Phase 0 : qualification `CFG-01`, gabarit `CFG-02`, découpage `CFG-03`, table `NIV-07`, registres `H-xx`/`PA-xx` | B-00 à B-04 |
| C-13 | Refonte | Socle géométrique remonté en phase 1 : calage multi-sources, vue nettoyée différentielle, preuve multi-étages | B-30, B-31, B-32 |
| C-14 | Enrichissement | Audit croisé : preuve d'épuisement, réconciliation quantitative, Pré-Audit Flash d'Exécutabilité | B-10 à B-15 |
| C-15 | Refonte | Conception et synthèse : transcription intégrale des porteurs MOE, synthèse indissociable sur vue unique | B-20 |
| C-16 | Création | Brique `B-25` — stabilité globale, contreventement, joints de dilatation et sismique | 04_PHASE_2_CONCEPTION/B-25 |
| C-17 | Enrichissement | Calculs : hypothèses `H-xx` actives, prescriptions `ENC`/`PA-xx`, flèches sous maçonnerie, soutènements | B-40 à B-50 |
| C-18 | Création | Brique `B-34` — synthèse des réservations et interfaces techniques | 07_PHASE_5_LIVRABLES/B-34 |
| C-19 | Enrichissement | Clôture : `B-33` en vérification croisée globale, contrôle des hypothèses et des Points d'Arrêt | B-33, B-70 |
| C-20 | Enrichissement | Contrôle automatique obligatoire : `10/10 PASS` avant publication | T-03 |
| C-21 | Assainissement | Conversion intégrale des tableaux en tables Markdown normalisées, symétrisation du graphe amont/aval, reconstruction du dictionnaire | 51 fichiers Markdown |

### 3. Archive protégée

| N° | Nature | Objet | Fichiers impactés |
| --- | --- | --- | --- |
| CC-03 | Protection | Les entrées v1.0 à v2.4 du présent journal et les exemples `12_EXEMPLES` sont conservés sans modification de fond (seuls les tableaux ont été reformatés à l'identique) | 11_HISTORIQUE, 12_EXEMPLES |

---

"""
p = DST / "11_HISTORIQUE" / "Journal_des_modifications.md"
old = p.read_text(encoding="utf-8")
# Retirer l'ancien bandeau de tête (les entrées historiques sont conservées)
idx = old.find("1.")
head_cut = old.find("\n1.")
p.write_text(JOURNAL + old[head_cut + 1 :], encoding="utf-8")

print("Annexes, historique et corrections appliqués.")
