"""DOC-02 — Note méthodologique d'exécution et de phasage RSO & Fondations.

Affaire : 58 rue de l'Aigle, 92250 La Garenne-Colombes. Tâche 1.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_doc import build, count_pages  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "figures")

META = {
    "entete_gauche": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "entete_droit": "DOC-02 — Note méthodologique & phasage",
    "pied_gauche": ("BET Structure · Dossier d'exécution — Tâche 1 · Indice A · "
                    "11/11/2026 · Affaire GA-2026-58AIGLE · DOC-02"),
    "titre_pdf": "DOC-02 — Note méthodologique d'exécution et de phasage",
    "sujet_pdf": "RSO D1 à D6, fondations de l'extension et phasage — 58 rue de l'Aigle",
    "cover": (
        ["NOTE MÉTHODOLOGIQUE", "D'EXÉCUTION & DE PHASAGE"],
        "Reprises en sous-œuvre D1 à D6 · Fondations de l'extension · Étauiement provisoire · "
        "Trappe à linge",
        [
            ("Affaire", "Réhabilitation lourde, restructuration intérieure et extension en façade avant"),
            ("Adresse", "58 rue de l'Aigle — 92250 La Garenne-Colombes (Hauts-de-Seine)"),
            ("Maître d'œuvre", "Cabinet AARKA — SAS d'architecture, 75004 Paris"),
            ("Bureau d'études", "BET Structure — Études d'exécution Gros Œuvre & Structure"),
            ("Document", "**DOC-02** — Note méthodologique d'exécution et de phasage RSO & fondations"),
            ("Indice / date", "**A** — 11 novembre 2026"),
            ("Phase", "DCE — Tâche 1 / 4"),
            ("Format", "ISO A4 portrait (210 × 297 mm) — livré en .docx et .pdf"),
            ("Documents liés", "DOC-01 (note d'hypothèses, à lire conjointement) ; DOC-03 (note de calculs) ; "
                               "PL-01 à PL-05 (plans d'exécution)"),
            ("Références", "NF EN 1990/1991/1992/1993/1996/1997 + AN ; DTU 13.1, 13.2, 20.1, 21, 32.1 ; "
                           "NF EN 1996-1-1 ; recommandations RSI (reprises en sous-œuvre)"),
        ],
        "**Objet.** La présente note décrit les modes opératoires, les dispositions constructives de sécurité et "
        "l'ordre chronologique d'exécution des reprises en sous-œuvre D1 à D6, des fondations de l'extension et "
        "des ouvrages en béton armé associés. Elle fixe les **règles d'arrêt**, les **points de contrôle** et les "
        "**interfaces** entre l'entreprise, le maître d'œuvre et le BET. Elle ne se substitue ni au plan "
        "d'installation de chantier, ni au plan d'assurance qualité de l'entreprise, qui doivent s'y conformer.",
    ),
}

# --------------------------------------------------------------------------
# Données
# --------------------------------------------------------------------------
T_SYNTH_RSO = {
    "header": ["Rep.", "Élément à reprendre", "Renfort horizontal (acier)", "Appuis verticaux (BA)",
               "Fondation / reprise"],
    "widths": [7, 24, 24, 20, 25],
    "rows": [
        ["**D1**", "Refend longitudinal entrée / bureau — L = 2,60 m, zone **sans sous-sol**",
         "2 profilés jumelés (voir DOC-03) — appui sur jambages BA en about de mur",
         "2 poteaux BA 20 × 25 cm + poteau intermédiaire 20 × 20 cm",
         "**Longrine de répartition BA filante** sur fondation existante, ancrée par 6 chevilles à scellement chimique"],
        ["**D2**", "Façade avant — 3 travées, L = 3,80 m, mur de 47 cm en meulière",
         "Profilé jumelé en tête de baie, assis sur sommiers BA noyés dans la maçonnerie",
         "Jambages BA 25 × 50 cm de part et d'autre + sommier central",
         "Fondations existantes conservées — descente de charge reprise par le sous-sol existant"],
        ["**D3**", "Refend central longitudinal, L = 3,55 m, mur de 57 cm avec conduits de cheminée",
         "Profilé en I S275 + platines d'about sur poteau BA encastré",
         "**Poteau BA d'about 25 × 40 cm encastré** dans l'about du refend conservé + poteau BA côté opposé",
         "**Poteau BA au sous-sol + semelle de reprise** de part et d'autre de la porte PTE 73"],
        ["**D4**", "Façade avant — 1 travée, L = 2,00 m, mur de 49 cm",
         "Profilé jumelé en tête de baie",
         "Jambages BA 25 × 50 cm",
         "Fondations existantes conservées"],
        ["**D5**", "Refend transversal, L = 3,08 m, mur de 16 cm",
         "Profilé en I S275 à platines d'about, **appui commun avec D3** sur le poteau d'about",
         "Poteau d'about mutualisé avec D3 + jambage BA côté cuisine",
         "Reprise avec D3 au sous-sol"],
        ["**D6**", "Façade arrière — 1 travée, L = 1,54 m, mur de 46 cm",
         "Profilé en I S275 assis sur sommiers BA",
         "Jambages BA 25 × 40 cm",
         "Fondations existantes conservées — zone non excavée"],
    ],
    "caption": "Tableau 1 — Synthèse des principes de reprise pour chacune des six ouvertures. "
               "Les sections définitives sont établies en Tâche 2 (DOC-03).",
    "font": 6.8,
}

T_PHASAGE = {
    "header": ["Ph.", "Opération", "Durée", "Conditions d'arrêt / points de contrôle", "Intervenants"],
    "widths": [5, 40, 8, 33, 14],
    "rows": [
        ["**0**", "Constat d'état, relevé contradictoire des cotes et sondages préalables (H-01, H-08, H-09, H-10, "
                  "H-14, H-15, H-16)", "3 j",
         "**GO BET obligatoire** avant toute démolition. Levée des hypothèses restantes (H-08, H-09, H-10, "
         "H-14, H-15).",
         "Entreprise + BET + MOE"],
        ["**1**", "Installation de chantier, étais de reprise sous planchers haut R+1 et haut RDC, purge des "
                  "cloisons non porteuses", "4 j",
         "Vérification de la descente des étaiements jusqu'au dallage du sous-sol — **aucun étai reposant sur le "
         "plancher bois**. Contrôle du serrage à la clé dynamométrique.",
         "Entreprise + BET (contrôle)"],
        ["**2**", "Terrassement des deux **puits de l'extension** et fouille de reconnaissance en limite séparative",
         "4 j",
         "Atteinte de l'arase NGF 39,02 ; **sol de fondation réceptionné par le BET** (visite contradictoire).",
         "Entreprise + BET + géotechnicien"],
        ["**3**", "Coulage des puits en **gros béton C16/20** et des **longrines BA** de l'extension",
         "6 j",
         "Contrôle des ferraillages et des enrobages avant coulage ; PV de réception des bétons.",
         "Entreprise + BET"],
        ["**4**", "Coulage du **voile BA mitoyen** et du **poteau BA 25 × 25** noyé dans la verrière",
         "5 j",
         "Contrôle d'implantation du poteau : axe à **2,00 m ± 5 mm** du nu de façade, sous l'axe de la "
         "poutre-acrotère.",
         "Entreprise + BET + MOE"],
        ["**5**", "Exécution des **jambages et poteaux BA du RDC** (D1, D2, D3, D4, D5, D6) par passes alternées",
         "10 j",
         "Contrôle du phasage : **une seule ouverture en cours par mur**. Résistance du béton ≥ 20 MPa avant "
         "dépose des étais de la zone.",
         "Entreprise + BET"],
        ["**6**", "Dépose des étais et **démolition des murs D1 à D6** par passes descendantes, après 28 j de "
                  "maturation des appuis", "8 j",
         "**PV de résistance béton** à 28 j obligatoire avant toute démolition. Contrôle des vibrations.",
         "Entreprise + BET + MOE"],
        ["**7**", "Pose des **profilés métalliques** D1 à D6, matage au mortier sans retrait, boulonnage des "
                  "platines", "6 j",
         "Contrôle du matage (contact ≥ 90 %), du serrage des boulons HR et des jeux de dilatation.",
         "Entreprise + BET"],
        ["**8**", "Coulage de la **poutre-acrotère BA** et de la **dalle de toiture-terrasse**",
         "6 j",
         "Contrôle du ferraillage, de l'enrobage, de la **contre-flèche de coffrage de 20 mm** et de la "
         "liaison mécanique avec le mur de façade existant.",
         "Entreprise + BET"],
        ["**9**", "Décoffrage, réception des ouvrages, reprise des finitions et **levé topographique final**",
         "3 j",
         "**PV de réception** ; contrôle des flèches mesurées sur les profilés sous charges réelles.",
         "Entreprise + BET + MOE"],
    ],
    "caption": "Tableau 2 — Phasage général des travaux de structure. Les durées sont indicatives et supposent "
               "un chantier linéaire à une seule équipe. Le phasage des reprises D1 à D6 est détaillé aux § 4 à 6.",
    "font": 6.8,
}

T_ETAI = {
    "header": ["Zone", "Surface étayée", "Charge à reprendre (ELU)", "Étaiement retenu", "Contrôle"],
    "widths": [18, 14, 20, 28, 20],
    "rows": [
        ["Sous plancher haut RDC — bande D2/D4 (façade)", "≈ 18 m²", "≈ 48 kN",
         "Étais métalliques réglables ∅ 48 mm à entraxe 1,00 m, semelles de répartition 20 × 20 cm",
         "Serrage à 2 kN par étai"],
        ["Sous plancher haut RDC — bande D3/D5 (refends)", "≈ 22 m²", "≈ 62 kN",
         "Étais ∅ 48 mm à entraxe 0,90 m + filants bois 75 × 100 mm en tête",
         "Contrôle hebdomadaire"],
        ["Sous plancher haut R+1 — surcharge de chantier", "≈ 45 m²", "≈ 67 kN",
         "Étais ∅ 48 mm à entraxe 1,20 m sur les seules zones de circulation",
         "Relevé de flèche"],
        ["Sous plancher haut RDC — zone D1 (bureau)", "≈ 8 m²", "≈ 21 kN",
         "Étais ∅ 48 mm à entraxe 1,00 m, **reprise directe au dallage** (pas de cave sous D1)",
         "Vérification de l'assise"],
    ],
    "caption": "Tableau 3 — Étauiement provisoire. Les valeurs de charge sont des ordres de grandeur destinés au "
               "pré-chiffrage ; le calcul complet de l'étaiement est établi en Tâche 2 (DOC-03 § 2.7).",
}

T_PUITS = {
    "header": ["Caractéristique", "Puits 1 — angle mitoyen est", "Puits 2 — poteau BA sous la poutre-acrotère"],
    "widths": [30, 35, 35],
    "rows": [
        ["Implantation", "Angle nord-est de l'extension, au droit du voile mitoyen",
         "Sous le poteau BA 25 × 25, à **2,00 m du nu de la façade existante** — position "
         "**contractuelle** depuis l'arbitrage E-01 du 11/11/2026"],
        ["Dimensions en plan", "Ø 2,20 m (puits circulaire, calcul DOC-03 §4.2)",
         "Ø 2,05 m (puits circulaire, calcul DOC-03 §4.2)"],
        ["Profondeur", "De 41,46 à **39,02 NGF** (2,44 m)", "De 41,46 à **39,02 NGF** (2,44 m)"],
        ["Nature du remplissage", "Gros béton C16/20 coulé en pleine fouille, par passes de 0,50 m",
         "Gros béton C16/20 coulé en pleine fouille, par passes de 0,50 m"],
        ["Semelle de répartition", "1,60 × 1,40 m — ép. 0,30 m, ferraillée B500B (chaînage périphérique)",
         "1,40 × 1,40 m — ép. 0,30 m, ferraillée B500B"],
        ["Longrine de liaison BA", "Section 25 × 40 cm — 4HA12 + cadres HA8 e = 20 cm",
         "Section 25 × 40 cm — 4HA12 + cadres HA8 e = 20 cm"],
        ["Précautions", "**Aucune poussée sur les murs de cave existants** : la fouille est blindée et remblayée "
                        "au plus vite ; le bétonnage du puits est réalisé avant tout terrassement de la longrine.",
         "Idem + protection du réseau EP proche (à repérer par DT-DICT)"],
    ],
    "caption": "Tableau 4 — Caractéristiques des puits de fondation de l'extension. Les sections définitives "
               "résultent du calcul géotechnique de la Tâche 2.",
}

T_CONTROLES = {
    "header": ["N°", "Point de contrôle", "Moyen", "Critère d'acceptation", "Responsable"],
    "widths": [5, 30, 22, 30, 13],
    "rows": [
        ["C-01", "Résistance du sol en fond de fouille", "Visite contradictoire + essai à la plaque",
         "q<sub>els</sub> ≥ 0,10 MPa", "BET"],
        ["C-02", "Implantation des poteaux BA", "Relevé topographique au théodolite", "± 10 mm", "Géomètre"],
        ["C-03", "Verticalité des coffrages de poteaux", "Fil à plomb / laser", "≤ 5 mm sur la hauteur", "Entreprise"],
        ["C-04", "Ferraillage avant coulage", "Contrôle visuel + fiche de ferraillage visée", "Conforme au plan PL-04",
         "BET"],
        ["C-05", "Enrobage des armatures", "Cales certifiées + contrôle visuel", "≥ 30 mm (XC1) / 40 mm (XC4)",
         "Entreprise"],
        ["C-06", "Résistance du béton à 28 j", "Éprouvettes 16 × 32 cm, 3 par gâchée", "≥ 25 MPa (C25/30)",
         "Laboratoire"],
        ["C-07", "Matage sous platine", "Contrôle du contact par bruit et ressuage", "Contact ≥ 90 % de la surface",
         "BET"],
        ["C-08", "Serrage des boulons HR", "Clé dynamométrique étalonnée", "Couple prescrit ± 5 %", "Entreprise"],
        ["C-09", "Flèche des profilés sous charges réelles", "Nivellement de précision avant/après chargement",
         "≤ L/750 et ≤ 5 mm", "BET"],
        ["C-10", "Fissuration des maçonneries conservées", "Fissuromètres + relevé photographique",
         "Aucune fissure nouvelle > 0,2 mm", "BET"],
        ["C-11", "Étanchéité de la toiture-terrasse", "Essai de mise en eau 48 h", "Aucune fuite", "Entreprise"],
        ["C-12", "Position de la trappe à linge entre solives", "Contrôle après ouverture du plancher",
         "Aucune solive coupée", "BET + MOE"],
    ],
    "caption": "Tableau 5 — Plan de contrôle qualité de la structure. Chaque point fait l'objet d'une fiche de "
               "contrôle signée et archivée au dossier d'exécution.",
}

T_TRAPPE = {
    "header": ["Niveau", "Position relevée (DXF)", "Entraxe solives supposé", "Décision"],
    "widths": [16, 30, 22, 32],
    "rows": [
        ["Combles", "Trappe repérée à x ≈ 46491 (plan P08b Combles), ouverture 30 × 31 cm", "45 cm",
         "Position **entourée d'un nuage** sur les plans ; ajustement dans la zone de tolérance"],
        ["R+1", "Trappe repérée à x ≈ 42890 (plan P08b R+1), ouverture 30 × 31 cm", "45 cm",
         "Position **entourée d'un nuage** sur les plans ; ajustement dans la zone de tolérance"],
        ["RDC", "Trappe repérée à x ≈ 48491 (plan P08b RDC), ouverture 30 × 31 cm", "45 cm",
         "Position **entourée d'un nuage** sur les plans ; ajustement dans la zone de tolérance"],
    ],
    "caption": "Tableau 6 — Positions de la trappe à linge relevées sur les plans et décision d'implantation.",
}

T_RISQUES = {
    "header": ["N°", "Risque identifié", "Criticité", "Mesure de prévention / de maîtrise"],
    "widths": [5, 34, 10, 51],
    "rows": [
        ["R-01", "Effondrement local d'un mur porteur lors de la démolition", "**Élevée**",
         "Étauiement systématique double (sous plancher et en sous-œuvre), démolition par passes de 0,50 m, "
         "interdiction de deux ouvertures simultanées sur un même mur, présence du BET lors des premières passes."],
        ["R-02", "Départ de fissure dans les maçonneries conservées", "**Élevée**",
         "Flèche limitée à L/750 et 5 mm, matage au mortier sans retrait, pose d'un chaînage BA en tête de mur "
         "conservé, pose de témoins de fissuration avant travaux."],
        ["R-03", "Poussée des terres sur les murs de cave existants lors du terrassement des puits", "**Élevée**",
         "Blindage de la fouille, bétonnage immédiat du puits, remblai compacté au plus vite, interdiction de "
         "stockage de matériaux à proximité, suivi topographique hebdomadaire des murs de cave."],
        ["R-04", "Affouillement ou sous-pression sous les fondations existantes", "Moyenne",
         "Maintien d'une distance minimale de 1,00 m entre la fouille et le nu des fondations existantes ; "
         "descente simultanée des deux puits à l'arase NGF 39,02."],
        ["R-05", "Chute d'objets / de matériaux au droit des trémies", "**Élevée**",
         "Planchers de protection en sous-œuvre, garde-corps périphériques, zones interdites balisées, "
         "port du casque obligatoire."],
        ["R-06", "Sinistre en cours de travaux (incendie, dégât des eaux)", "Moyenne",
         "Assurance dommages-ouvrage et TRC, extincteurs, consignes de sécurité, coupure des réseaux."],
        ["R-07", "Écart entre les cotes du DXF et la réalité du bâti", "**Élevée**",
         "Relevé contradictoire obligatoire (phase 0), cotation des plans d'exécution à partir du relevé réel, "
         "tolérance de 1 cm signalée comme non contractuelle."],
        ["R-08", "Instabilité du mur mitoyen", "**Élevée**",
         "Constat d'état contradictoire avec le voisin avant travaux, étaiement du mur mitoyen si nécessaire, "
         "clavetage du voile BA limité à la zone saine."],
        ["R-09", "Découverte de réseaux non repérés", "Moyenne",
         "DT-DICT, sondages manuels à la pelle, arrêt des travaux et information immédiate du MOE."],
        ["R-10", "Défaut de résistance du béton", "Moyenne",
         "Planches d'essai, prélèvement d'éprouvettes, contrôle des formulés, cure prolongée 7 jours."],
    ],
    "caption": "Tableau 7 — Analyse des risques d'exécution et mesures de maîtrise.",
}

# --------------------------------------------------------------------------
BLOCKS = [
    ("h1", "1. Objet, domaine d'application et documents de référence"),
    ("p", "La présente note méthodologique définit les **modes opératoires d'exécution** des travaux de structure "
          "de l'opération, ainsi que leur **enchaînement chronologique**. Elle s'applique à l'ensemble des "
          "interventions de reprise en sous-œuvre (D1 à D6), de fondation et de gros œuvre de l'extension, "
          "y compris les ouvrages provisoires nécessaires à leur réalisation."),
    ("p", "Elle est indissociable de la note d'hypothèses **DOC-01**, qui fixe les données d'entrée et le registre "
          "des hypothèses à lever, et de la note de calculs **DOC-03**, qui justifie les sections et les "
          "ferraillages. Les plans d'exécution **PL-01 à PL-05** en constituent la traduction graphique."),
    ("h2", "1.1 Documents de référence"),
    ("table", {
        "header": ["Domaine", "Référence", "Objet dans la présente note"],
        "widths": [22, 34, 44],
        "rows": [
            ["Reprises en sous-œuvre", "Recommandations professionnelles RSI ; DTU 20.1 § 7",
             "Principes d'étaiement, ordre des démolitions, dispositions de continuité"],
            ["Fondations", "NF EN 1997-1 + AN ; NF P 94-261 ; DTU 13.1 et 13.2",
             "Réception du sol, puits en gros béton, longrines, semelles"],
            ["Béton armé", "NF EN 1992-1-1 + AN ; DTU 21 ; NF EN 13670",
             "Coffrage, ferraillage, coulage, cure, décoffrage, tolérances"],
            ["Construction métallique", "NF EN 1993-1-1 / 1-8 + AN ; DTU 32.1",
             "Pose des profilés, assemblages boulonnés, matage, protection anticorrosion"],
            ["Maçonnerie existante", "NF EN 1996-1-1 + AN ; DTU 20.1",
             "Sommiers de répartition, scellements, reprise en sous-œuvre"],
            ["Sécurité de chantier", "Code du travail L. 4531 et s. ; arrêté du 21 décembre 2004",
             "Étaiement, travaux en hauteur, trémies, co-activité"],
        ],
        "caption": "Tableau 8 — Documents de référence mobilisés par la méthodologie.",
        "font": 7.2,
    }),

    ("h1", "2. Principes généraux de la reprise en sous-œuvre"),
    ("h2", "2.1 Principe de répartition des matériaux"),
    ("p", "Conformément au cahier des charges, la répartition des matériaux est la suivante et **ne peut être "
          "modifiée sans avenant** :"),
    ("bullets", [
        "**Tous les renforcements horizontaux** (poutres et linteaux de reprise) sont réalisés par des **profilés "
        "métalliques en acier S275 ou S355**, ce qui permet de limiter la retombée sous plafond et de mettre en "
        "œuvre des sections élancées à forte inertie.",
        "**Tous les renforts verticaux** (poteaux, jambages, raidisseurs) et **sommiers d'appui** sont réalisés en "
        "**béton armé C25/30 coulé en place**, avec armatures B500B. Le béton armé assure la continuité mécanique "
        "avec la maçonnerie existante, la possibilité de scellement et la protection au feu.",
        "**Les fondations nouvelles** (puits, longrines, semelles) sont en béton armé ou en gros béton, "
        "systématiquement descendues au niveau d'assise des fondations existantes.",
    ]),
    ("h2", "2.2 Règle des trois « jamais »"),
    ("note", "**Règle 1 — Jamais de démolition sans étaiement.** Aucune maçonnerie porteuse n'est démolie avant "
             "que l'étaiement provisoire ne soit posé, vérifié et réceptionné par le BET.\n"
             "**Règle 2 — Jamais deux ouvertures simultanées sur un même mur.** Les reprises sont exécutées "
             "ouverture par ouverture, mur par mur, et les appuis BA atteignent 28 jours avant la démolition de "
             "l'ouverture suivante sur le même mur.\n"
             "**Règle 3 — Jamais d'appui sur un plancher bois non étayé.** Tous les étais sont descendus jusqu'au "
             "dallage du sous-sol ou jusqu'au sol naturel ; aucun étai ne prend appui sur un plancher bois."),
    ("h2", "2.3 Principe de l'étaiement provisoire descendu au sous-sol"),
    ("p", "L'étaiement provisoire est **dimensionné pour reprendre la totalité des charges** transmises par les "
          "murs à démolir pendant la durée des travaux, sans participation des planchers existants. Il est "
          "constitué d'étais métalliques réglables à double filet et de filants bois, disposés en nappes "
          "croisées sous les solives les plus sollicitées."),
    ("p", "La particularité de l'affaire réside dans la **continuité de la descente de charge** : la cave "
          "n'occupe qu'une partie de l'emprise du rez-de-chaussée (environ 8,53 × 7,30 m). Les zones non "
          "excavées — dont la zone D1 — reposent sur le sol naturel, ce qui permet une reprise directe des "
          "étais au dallage. Les zones excavées nécessitent une reprise au dallage du sous-sol, lui-même "
          "vérifié et éventuellement conforté par un radier de répartition provisoire."),
    ("figure", os.path.join(FIG, "fig06_coupe_principe.png"),
     "Figure 1 — Coupe verticale de principe : la descente des étaiements jusqu'au niveau d'assise et "
     "l'altimétrie NGF qui conditionne le phasage.", 150),

    ("h1", "3. Méthodologie générale des reprises D1 à D6"),
    ("p", "Chaque reprise suit un **cycle en huit étapes** identique, adapté à la nature du mur et à la présence "
          "ou non d'un sous-sol :"),
    ("table", {
        "header": ["Étape", "Opération", "Dispositions constructives"],
        "widths": [8, 32, 60],
        "rows": [
            ["1", "Relevé et sondages", "Relevé de l'épaisseur réelle du mur, de la nature de la maçonnerie et de "
                                        "l'état des appuis ; sondage de la fondation si D1 ou D6."],
            ["2", "Étaiement provisoire", "Étais sous plancher haut, filants bois, calage au plancher bas ; "
                                          "réception par le BET."],
            ["3", "Sondage et purge des enduits", "Mise à nu de la maçonnerie sur la hauteur et la largeur de "
                                                  "l'ouverture ; repérage des conduits et canalisations."],
            ["4", "Exécution des appuis BA", "Coffrage des jambages et poteaux, ferraillage, coulage par passes de "
                                             "0,50 m avec vibration ; incorporation des platines d'appui pré-scellées "
                                             "ou des goujons d'ancrage."],
            ["5", "Maturation du béton", "28 jours de cure avant mise en charge ; contrôle par éprouvettes ; "
                                         "décoffrage à 7 jours minimum."],
            ["6", "Pose du profilé métallique", "Mise en place sur les appuis, vérification du niveau et de la "
                                                "contre-flèche, matage au mortier sans retrait, boulonnage des platines."],
            ["7", "Démolition du mur", "Démolition par passes descendantes de 0,50 m, du haut vers le bas, en "
                                       "laissant subsister une fiche de maçonnerie contre le profilé jusqu'à la fin "
                                       "du matage."],
            ["8", "Habillage et protection au feu", "Bardage coupe-feu, peinture intumescente ou encoffrement ; "
                                                    "reprise des enduits et des finitions."],
        ],
        "caption": "Tableau 9 — Cycle type d'une reprise en sous-œuvre.",
        "font": 7.2,
    }),
    ("h2", "3.1 Synthèse des principes par ouverture"),
    ("table", T_SYNTH_RSO),

    ("h1", "4. Reprises en sous-œuvre : modes opératoires détaillés"),
    ("h2", "4.1 D1 — Refend longitudinal entrée / bureau (zone non excavée)"),
    ("p", "**Contexte.** Le mur D1 est un refend longitudinal de 16 cm d'épaisseur et de 2,60 m de longueur, "
          "séparant l'entrée du bureau. La coupe 01 (planche P09b) montre que **cette zone n'est pas excavée** : "
          "il n'existe pas de cave sous D1, et le mur repose directement sur une **fondation filante continue** "
          "dont l'arase supérieure se situe à environ 0,40 m sous le sol fini."),
    ("p", "**Mode opératoire.**"),
    ("bullets", [
        "**1.** Étaiement du plancher haut du RDC de part et d'autre du mur, sur une bande de 1,50 m de largeur, "
        "avec reprise directe des étais au dallage (la zone n'étant pas excavée).",
        "**2.** Décapage de l'enduit sur les deux faces du mur et sur la hauteur totale ; repérage des "
        "canalisations encastrées.",
        "**3.** Ouverture des deux **sondages de fondation** de part et d'autre du mur et relevé de la largeur, "
        "de la hauteur et de l'état de la semelle existante.",
        "**4.** Exécution de la **longrine de répartition BA filante** (voir § 4.1.1), ancrée sur la fondation "
        "existante par des chevilles à scellement chimique et par une engravure périphérique.",
        "**5.** Coulage des **deux poteaux BA d'about** (20 × 25 cm) et du **poteau intermédiaire** (20 × 20 cm), "
        "sur la longrine, ferraillage en attente dans la longrine.",
        "**6.** Après 28 jours, pose du profilé métallique jumelé en tête de l'ouverture, sur platines pré-scellées.",
        "**7.** Démolition du mur **arrêtée à l'arase supérieure de la fondation existante** : la fondation filante "
        "est conservée dans son intégralité et n'est en aucun cas démolie, ni arasée, ni recoupée.",
        "**8.** Matage au mortier sans retrait sous le profilé et entre le profilé et la fondation conservée, puis "
        "habillage.",
    ]),
    ("h3", "4.1.1 Longrine de répartition BA sous D1"),
    ("p", "La longrine a pour fonction de **répartir les charges concentrées** apportées par les poteaux BA sur "
          "la fondation filante existante en **meulière continue** (hypothèse H-01 levée le 11/11/2026), de "
          "largeur retenue 0,50 m. "
          "Elle est dimensionnée pour que la contrainte de contact au sol reste inférieure à "
          "**q<sub>els</sub> = 0,10 MPa** et à **q<sub>elu</sub> = 0,15 MPa**."),
    ("table", {
        "header": ["Caractéristique", "Disposition retenue (à confirmer en Tâche 2)"],
        "widths": [34, 66],
        "rows": [
            ["Section", "**30 × 40 cm** (largeur × hauteur), longueur 2,80 m (débord de 0,10 m de part et d'autre)"],
            ["Ferraillage longitudinal", "**4 HA12** en nappe supérieure + **4 HA12** en nappe inférieure"],
            ["Ferraillage transversal", "Cadres **HA8 e = 20 cm** + épingles HA8"],
            ["Ancrage sur la fondation existante", "**6 chevilles à scellement chimique M16**, longueur 160 mm, "
                                                    "espacées de 0,40 m + engravure de 30 mm de profondeur sur "
                                                    "la périphérie"],
            ["Béton", "C25/30 — enrobage 40 mm (classe XC2, en contact avec le sol)"],
            ["Interface", "Film glissant ou feutre bitumineux sur la fondation existante **sauf** au droit des "
                          "scellements, afin d'éviter tout frottement parasite et de garantir la transmission "
                          "verticale des charges"],
            ["Résistance au feu", "Aucune exigence en infrastructure enterrée"],
        ],
        "caption": "Tableau 10 — Dispositions constructives de la longrine de répartition sous D1.",
        "font": 7.2,
    }),
    ("note", "**Point d'arrêt n° 1.** La démolition de D1 ne peut débuter qu'après **réception écrite de la "
             "longrine** par le BET (contrôle du ferraillage, des scellements et de la résistance du béton à 28 j). "
             "La fondation filante existante doit être **intégralement conservée** ; toute détérioration "
             "accidentelle doit être immédiatement signalée et réparée par un béton de reprise."),

    ("h2", "4.2 D2 et D4 — Baies de la façade avant"),
    ("p", "**Contexte.** Les baies D2 (3,80 m, trois travées) et D4 (2,00 m, une travée) sont percées dans le "
          "**mur de façade avant**, en meulière, d'épaisseur 47 à 49 cm. Ce mur porte le plancher haut du RDC, "
          "le plancher haut du R+1 et la retombée de la charpente, soit une charge verticale importante. Les "
          "ouvertures existantes (A 60 / F 174 et A 61 / F 177) sont élargies."),
    ("p", "**Mode opératoire.**"),
    ("bullets", [
        "**Étaiement double** : étais sous plancher haut du RDC et sous plancher haut du R+1, sur toute la largeur "
        "des baies, à entraxe 1,00 m.",
        "**Exécution des jambages BA 25 × 50 cm** par passes alternées de 0,50 m, en commençant par les appuis "
        "d'about et en terminant par les appuis intermédiaires ; incorporation des platines d'appui du profilé.",
        "**Coulage d'un sommier BA** en tête de baie, sur toute la largeur, solidaire des jambages, afin de "
        "constituer un chaînage horizontal continu et de répartir les charges sur la maçonnerie.",
        "**Pose du profilé jumelé** en tête de baie, en appui sur les platines, avec matage au mortier sans "
        "retrait sur toute la surface de contact.",
        "**Démolition par passes descendantes**, en commençant par le haut, avec conservation d'une fiche de "
        "maçonnerie de 0,20 m contre le profilé jusqu'à la fin du matage.",
        "**Reprise de la maçonnerie** au-dessus du profilé : hourdage au mortier de chaux, bâti de briques, "
        "clavetage.",
    ]),
    ("note", "**Vérification de la maçonnerie sous sommier.** La contrainte de compression sous le sommier BA est "
             "vérifiée selon NF EN 1996-1-1 + AN, avec f<sub>d</sub> = 1,2 MPa (hypothèse H-08). La longueur "
             "d'appui est au minimum de 0,50 m de part et d'autre de chaque jambage, ce qui correspond à une "
             "longueur d'appui totale de 1,00 m par appui et à une contrainte de l'ordre de 0,4 MPa pour les "
             "charges courantes — marge satisfaisante sous réserve de confirmation par les essais."),

    ("h2", "4.3 D3 et D5 — Croisement au droit du refend central"),
    ("p", "**Contexte.** Il s'agit du point le plus délicat de l'opération. Le croisement des ouvertures D3 "
          "(refend longitudinal de 57 cm, 3,55 m) et D5 (refend transversal de 16 cm, 3,08 m) se situe "
          "**exactement au droit de l'about du mur de refend longitudinal central conservé**, derrière "
          "l'emplacement du futur poêle. Les deux ouvertures se croisent en T : D3 est parallèle au refend, "
          "D5 est perpendiculaire et vient buter contre lui."),
    ("p", "**Solution retenue.** Un **poteau BA d'about 25 × 40 cm** est encastré à l'extrémité du mur conservé, "
          "de manière à recevoir simultanément :"),
    ("bullets", [
        "l'appui du profilé de **D3** (portée 3,55 m), par une platine pré-scellée en face latérale ;",
        "l'appui du profilé de **D5** (portée 3,08 m), par une seconde platine pré-scellée en face "
        "perpendiculaire ;",
        "les charges descendantes du refend conservé lui-même, qui constitue un point d'appui de la charpente.",
    ]),
    ("p", "Le poteau est **encastré** (et non simplement posé) dans l'about du refend : il est claveté par des "
          "armatures HA12 ancrées dans les joints de maçonnerie sur 0,50 m de profondeur, de part et d'autre, afin "
          "de mobiliser la raideur du refend et de reprendre le moment d'encastrement. Un essai d'arrachement "
          "sur une cheville représentative est exigé avant la pose des platines."),
    ("h3", "4.3.1 Descente de charge au sous-sol et reprise au droit de la porte PTE 73"),
    ("p", "La descente de charge du poteau d'about D3/D5 rencontre, au niveau du sous-sol, le **mur de refend de "
          "la cave** dans lequel est percée la **porte existante PTE 73**. La charge ne peut donc pas être "
          "transmise directement au sol : elle doit être reprise de part et d'autre de la porte, puis reportée "
          "sur une fondation nouvelle."),
    ("bullets", [
        "**Renforcement vertical au sous-sol** : deux poteaux BA 25 × 40 cm en applique sur les deux faces du "
        "mur de refend, de part et d'autre de la porte PTE 73, reliés en tête par un sommier BA et en pied par "
        "une semelle commune.",
        "**Semelle de reprise** : semelle filante BA de 1,40 × 1,40 m sous chaque poteau, descendue à l'arase "
        "NGF 39,02, ferraillée en B500B, dimensionnée pour q<sub>elu</sub> = 0,15 MPa.",
        "**Reprise de la maçonnerie** : le linteau existant de la porte PTE 73 est vérifié ; si sa portée est "
        "insuffisante, un linteau BA complémentaire est coulé en sous-face ou un profilé est inséré dans "
        "l'épaisseur du mur.",
        "**Contrôle de la porte** : la porte doit rester **utilisable pendant toute la durée des travaux** ; "
        "aucun étaiement ne doit la traverser.",
    ]),
    ("note", "**Point d'arrêt n° 2.** Avant tout percement du refend de cave, un **sondage de la fondation** et un "
             "**relevé précis de la position de la porte PTE 73** (largeur, hauteur, sens d'ouverture, présence "
             "d'un linteau) sont réalisés et transmis au BET. Le dimensionnement de la semelle de reprise est "
             "confirmé sur cette base (Tâche 2, § 3.4)."),

    ("h2", "4.4 D6 — Baie de la façade arrière (cuisine)"),
    ("p", "La baie D6 (1,54 m) est percée dans le **mur de façade arrière** (46 cm) au niveau de la cuisine. La "
          "zone n'est pas excavée sous la façade arrière sur cette portion : la fondation filante existante est "
          "conservée. Le mode opératoire est identique à celui de D2/D4 : étaiement, jambages BA 25 × 40 cm, "
          "sommier BA, profilé, démolition par passes descendantes. Aucune reprise de fondation n'est nécessaire "
          "au-delà de la vérification de la contrainte sous sommier."),

    ("pagebreak",),
    ("h1", "5. Fondations et structure de l'extension"),
    ("h2", "5.1 Principe général"),
    ("p", "L'extension occupe une emprise de **8,03 × 3,20 m** en façade avant. Elle est constituée :"),
    ("bullets", [
        "d'un **voile BA côté mitoyen** (est), solidaire du mur existant par clavetage ;",
        "d'un **poteau BA 25 × 25 cm** implanté à **2,00 m du nu de la façade existante**, sous la poutre ;",
        "d'une **poutre-acrotère BA** de 30 × 67 cm franchissant les 8,03 m, dont l'arase supérieure "
        "constitue l'acrotère à NGF 44,75 ;",
        "d'une **dalle BA de toiture-terrasse** (ép. 20 cm) ancrée dans le mur de façade existant au-dessus de "
        "D2 et D4, franchissant 2,00 m jusqu'à la poutre puis se poursuivant en porte-à-faux de 1,20 m "
        "jusqu'à la verrière ;",
        "d'une **verrière** (hors mission) rapportée sur la structure.",
    ]),
    ("figure", os.path.join(FIG, "fig07_extension_plan.png"),
     "Figure 2 — Plan de principe de l'extension : implantation du voile mitoyen, du poteau BA "
     "à 2,00 m du nu de façade et de la poutre-acrotère.", 156),
    ("h2", "5.2 Méthodologie des puits de fondation"),
    ("p", "Les deux puits sont **impérativement descendus jusqu'au même niveau d'assise que les fondations "
          "existantes du sous-sol (NGF 39,02)** afin de ne générer aucune poussée différentielle sur les murs de "
          "cave. Le mode opératoire est le suivant :"),
    ("bullets", [
        "**Repérage et DT-DICT** préalables, sondages manuels à la pelle mécanique sur 1,20 m de profondeur.",
        "**Terrassement par puits** de 1,20 × 1,00 m et 1,00 × 1,00 m, à la pelle mécanique de faible tonnage, "
        "avec **blindage immédiat** des parois (caisse de blindage ou chemisage bois).",
        "**Interdiction absolue** de terrasser simultanément les deux puits et la longrine : les puits sont "
        "exécutés et bétonnés l'un après l'autre.",
        "**Contrôle du fond de fouille** par le BET (visite contradictoire) : vérification de la nature du sol, "
        "de l'absence d'eau et de la profondeur d'assise.",
        "**Bétonnage en pleine fouille** au gros béton C16/20, par passes de 0,50 m, avec vibration, jusqu'à "
        "0,30 m sous le niveau bas de la semelle.",
        "**Exécution de la semelle BA** 1,60 × 1,40 m (ép. 0,30 m) ferraillée, puis des **longrines BA** "
        "25 × 40 cm reliant les puits au mur de façade existant.",
        "**Remblaiement compacté** par couches de 0,20 m dès que le béton a atteint 7 jours, afin de rétablir "
        "rapidement la butée sur les murs de cave.",
    ]),
    ("table", T_PUITS),
    ("h2", "5.3 Voile BA mitoyen et poteau BA sous la poutre"),
    ("p", "Le **voile mitoyen** (ép. 20 cm) est coulé contre le mur existant, après piquage de la surface et "
          "clavetage par des armatures HA10 tous les 0,40 m, scellées chimiquement dans la maçonnerie sur 0,25 m. "
          "Il assure à la fois la reprise des charges verticales de la poutre-acrotère et la stabilité "
          "transversale de l'extension."),
    ("p", "Le **poteau BA 25 × 25 cm** est coulé sur la semelle du puits n° 1 et reçoit, en tête, la platine "
          "d'appui de la poutre-acrotère. Il est **implanté à 2,00 m du nu de la façade existante**, position "
          "arrêtée le 11/11/2026, et se trouve **noyé dans la façade latérale de la verrière** : un "
          "**rupteur de pont thermique** (plaque de mousse polyuréthane ou de polystyrène extrudé de 40 mm) est "
          "interposé entre le poteau et la menuiserie sur toute la hauteur, afin d'éviter tout pont thermique "
          "conforme à la RE 2020."),
    ("h2", "5.4 Poutre-acrotère retroussée et dalle de toiture-terrasse"),
    ("p", "La **poutre-acrotère retroussée** est une poutre BA monolithique de section **30 × 67 cm**, calée "
          "entre la sous-face du plancher haut RDC (NGF 44,08) et l'**arase supérieure de l'acrotère "
          "(NGF 44,75)**. Elle **fait office d'acrotère** de la terrasse et constitue, avec la dalle, un "
          "ensemble monolithique en L favorable à la rigidité d'ensemble et à l'étanchéité."),
    ("note", "**Géométrie confirmée par le maître d'ouvrage le 11 novembre 2026.** La poutre s'appuie sur le "
             "**voile BA du mur mitoyen** et sur le **poteau BA 25 × 25**, déplacé à **2,00 m du nu de la "
             "façade** pour venir exactement sous la poutre. Le poteau est donc l'**appui d'extrémité** côté "
             "façade : la poutre reste une **travée unique de 8,03 m**, isostatique. Sa flèche à long terme "
             "ressort à 17,6 mm (L/457) ; elle respecte le critère L/250 et une **contre-flèche de coffrage de "
             "20 mm** est prescrite pour tenir le critère L/500 vis-à-vis de la verrière (DOC-03 §3.4)."),
    ("bullets", [
        "d'un côté, sur le **voile BA mitoyen**, par un appui encastré partiel (armatures en attente) ;",
        "de l'autre, sur le **poteau BA 25 × 25** situé à 2,00 m du nu de façade, par un appui simple "
        "(platine + appareil d'appui) ;",
        "la **dalle de terrasse** est, quant à elle, appuyée sur le **mur de façade conservé** par un appareil "
        "d'appui glissant (platine + feutre téflon) afin de permettre la libre rotation et la dilatation "
        "thermique ; elle franchit 2,00 m entre la façade et la poutre puis se poursuit en **porte-à-faux de "
        "1,20 m** jusqu'à la verrière.",
    ]),
    ("p", "Ces dispositions sont détaillées dans la note de calculs (DOC-03, chapitre 1) et sur les plans "
          "PL-02 (coffrage) et PL-04 (ferraillage)."),
    ("h2", "5.5 Joint de dilatation et désolidarisation"),
    ("p", "Un **joint de dilatation vertical de 20 mm** est ménagé entre l'extension et la maison existante, sur "
          "toute la hauteur et sur toute la profondeur de l'emprise. Il est comblé par un fond de joint "
          "compressible et un mastic élastomère de classe ISO 11600 F 25 LM, avec une **membrane d'étanchéité "
          "à soufflet** en tête. Ce joint évite que les tassements différentiels de l'extension ne fissurent "
          "les maçonneries anciennes."),
    ("p", "La **dalle de terrasse** est par ailleurs désolidarisée du plancher haut du RDC existant : elle est "
          "appuyée sur le mur de façade conservé par l'intermédiaire d'un appareil d'appui glissant, et non "
          "encastrée. Les armatures de la dalle sont **ancrées chimiquement dans le mur de façade** au-dessus "
          "des linteaux D2 et D4, selon le détail PL-05 (détail n° 3)."),

    ("pagebreak",),
    ("h1", "6. Trappe à linge : méthodologie de repérage et de pose"),
    ("h2", "6.1 Contrainte structurale"),
    ("p", "La trappe à linge traverse les trois niveaux (Combles → R+1 → RDC). Le cahier des charges impose "
          "qu'elle soit **positionnée entre deux poutrelles ou solives existantes**, afin de **ne couper aucune "
          "poutrelle** (zéro chevêtre). Cela suppose de connaître précisément l'entraxe réel des solives, qui "
          "n'est pas documenté sur les plans."),
    ("h2", "6.2 Zone de tolérance d'implantation"),
    ("p", "**Arbitrage du 11 novembre 2026.** La position de la trappe est estimée à partir des plans de projet, "
          "puis **entourée d'un nuage de révision** sur les plans d'exécution (PL-01 à PL-03) : le nuage "
          "matérialise le caractère provisoire de l'implantation et l'obligation de relevé d'entraxe avant "
          "tracé définitif. Il ne s'agit pas d'une réserve de conception mais d'une **consigne d'exécution**."),
    ("p", "Les plans d'exécution définiront non pas une position figée, mais une **zone de tolérance** à "
          "l'intérieur de laquelle la trappe peut être décalée sans conséquence structurelle. Cette zone est "
          "définie comme suit :"),
    ("bullets", [
        "**Translation longitudinale** : ± 0,60 m par rapport à la position indiquée sur les plans AARKA, dans la "
        "mesure où cela ne fait pas sortir la trappe de la pièce desservie.",
        "**Translation transversale** : ± 0,45 m, soit un module complet d'entraxe de solives.",
        "**Rotation** : aucune — la trappe reste parallèle aux solives.",
        "**Cote de sol** : l'ouverture doit être centrée sur la trémie de passage du conduit, avec un jeu "
        "minimum de 50 mm.",
    ]),
    ("h2", "6.3 Consigne de sondage préalable"),
    ("table", T_TRAPPE),
    ("p", "**Consigne.** Avant tout tracé d'exécution, l'entreprise procède au **relevé de l'entraxe réel des "
          "solives** à chaque niveau, par :"),
    ("bullets", [
        "**au R+1 et aux Combles** : dépose des lames de parquet ou ouverture d'une trappe de visite de 200 × 200 mm ;",
        "**au RDC** : sondage depuis le sous-sol, en sous-face du plancher haut du RDC, après dépose ponctuelle "
        "d'un faux plafond ;",
        "**relevé photographique** avec réglet, et report sur un schéma coté transmis au BET.",
    ]),
    ("p", "Si l'entraxe relevé ne permet pas l'insertion de l'ouverture de 45 × 40 cm (cas d'un entraxe de 45 cm "
          "avec solives de 80 mm, qui ne laisse que 37 cm de lumière libre), l'ouverture est **réduite à "
          "40 × 36 cm** et/ou décalée dans la zone de tolérance. **Aucune solive ne doit être coupée** : si "
          "aucune solution n'est trouvée, le BET est saisi et étudie un renforcement local par doublement de "
          "solives (hors mission initiale)."),

    ("pagebreak",),
    ("h1", "7. Phasage général et ordonnancement"),
    ("p", "Le phasage ci-dessous constitue le **séquencement contractuel** des travaux de structure. Toute "
          "modification de l'ordre des opérations doit être validée par le BET, car certaines étapes conditionnent "
          "la stabilité provisoire de l'ouvrage."),
    ("table", T_PHASAGE),
    ("h2", "7.1 Représentation synoptique du phasage"),
    ("figure", os.path.join(FIG, "fig08_phasage_gantt.png"),
     "Figure 3 — Diagramme de phasage : durées indicatives en jours ouvrés, chemins critiques et points "
     "d'arrêt bloquants. L'intervalle de 28 jours entre la phase 5 (appuis BA) et la phase 6 (démolition) "
     "correspond à la maturation du béton et constitue le chemin critique de l'opération.", 165),
    ("p", "Le **chemin critique** de l'opération est constitué de la séquence : appuis BA au RDC (phase 5) → "
          "maturation 28 jours → démolition des murs (phase 6) → pose des profilés (phase 7). Toute réduction du "
          "délai de 28 jours est exclue : elle conduirait à mettre en charge un béton non mature et à un risque "
          "de poinçonnement des appuis. Une **option d'accélération** consiste à recourir à un béton à hautes "
          "performances (C35/45) permettant une mise en charge à 7 jours, sous réserve d'une étude spécifique "
          "et d'un contrôle renforcé."),
    ("h2", "7.2 Règles de co-activité"),
    ("bullets", [
        "**Aucune démolition de mur porteur** n'est autorisée avant la réception des appuis BA correspondants.",
        "**Aucun coulage de béton** n'est autorisé au-dessus d'une zone en cours de démolition.",
        "**Aucun stockage** de matériaux n'est autorisé à moins de 1,00 m du nu des murs de cave pendant le "
        "terrassement des puits.",
        "**Les accès** au sous-sol et au R+1 sont maintenus en permanence ; les escaliers existants sont protégés.",
        "**Un seul front de démolition** est ouvert à la fois par niveau.",
    ]),

    ("h1", "8. Moyens et dispositions de sécurité"),
    ("h2", "8.1 Étauiement provisoire"),
    ("table", T_ETAI),
    ("h2", "8.2 Sécurité des intervenants"),
    ("bullets", [
        "**Plan de prévention** et **PPSPS** établis avant démarrage, compte tenu de la co-activité et des "
        "travaux de démolition.",
        "**Échafaudages** de pied et roulants conformes à la norme NF EN 12811 ; réception avant mise en service.",
        "**Protections collectives** : garde-corps sur les trémies, filets anti-chute, planchers de protection "
        "en sous-œuvre des zones de démolition.",
        "**EPI** : casque, chaussures de sécurité, gants anti-coupure, lunettes, protections auditives, "
        "masques FFP3 (poussières de silice).",
        "**Travaux en hauteur** : dispositifs antichute individuels si les protections collectives sont "
        "impossibles.",
        "**Balisage** des zones de chute d'objets, interdiction d'accès au public, affichage des consignes.",
    ]),
    ("h2", "8.3 Protection de l'existant"),
    ("bullets", [
        "**Constat d'état** contradictoire (photographique et descriptif) de l'ensemble du bâti et des "
        "propriétés voisines avant travaux.",
        "**Témoins de fissuration** posés sur les maçonneries sensibles et relevés hebdomadaires.",
        "**Suivi topographique** des murs de cave pendant le terrassement des puits (nivellement de précision).",
        "**Protection des réseaux** existants (fourreaux, calfeutrement).",
    ]),

    ("h1", "9. Contrôle qualité et points d'arrêt"),
    ("table", T_CONTROLES),
    ("note", "**Points d'arrêt bloquants (PA).** PA-1 : réception du sol de fondation des puits. "
             "PA-2 : contrôle du ferraillage de la longrine sous D1. PA-3 : PV de résistance du béton à 28 j "
             "avant toute démolition. PA-4 : contrôle du matage et du boulonnage des profilés. PA-5 : contrôle du "
             "ferraillage de la poutre-acrotère. PA-6 : essai de mise en eau de la terrasse. Chaque point "
             "d'arrêt fait l'objet d'une fiche signée et ne peut être levé que par le BET."),

    ("h1", "10. Analyse des risques d'exécution"),
    ("table", T_RISQUES),

    ("h1", "11. Interfaces et coordination"),
    ("table", {
        "header": ["Interface", "Objet", "Disposition"],
        "widths": [22, 38, 40],
        "rows": [
            ["BET ↔ Architecte (AARKA)", "Position du poteau BA de la verrière (écart E-01)",
             "Arbitrage écrit avant la Tâche 3 ; si la position change, révision de la portée de la poutre."],
            ["BET ↔ Charpentier", "Descentes de charges de la charpente (H-06)",
             "**Accepté le 11/11/2026** : hypothèse forfaitaire de 250 kg/m² retenue ; note à fournir pour "
             "actualisation."],
            ["BET ↔ Verriériste", "Charges d'appui de la verrière (H-18)",
             "**Accepté le 11/11/2026** : charges forfaitaires retenues ; fiche technique à fournir pour "
             "actualisation."],
            ["BET ↔ Géotechnicien", "Étude G2 et réception du sol de fondation",
             "Campagne de sondages en phase 0 ; PV de réception en phase 2."],
            ["BET ↔ Entreprise", "Modes opératoires, phasage, points d'arrêt",
             "Présentation du mode opératoire avant démarrage ; fiches de contrôle à chaque PA."],
            ["BET ↔ Bureau de contrôle", "Résistance au feu (H-19) et conformité",
             "Consultation avant dépôt du dossier ; avis à intégrer dans les plans d'exécution."],
            ["BET ↔ Voisin", "Mur mitoyen (H-12)",
             "Constat d'état contradictoire avant travaux ; autorisation d'accès pour sondage."],
        ],
        "caption": "Tableau 14 — Interfaces et coordination.",
        "font": 7.2,
    }),

    ("h1", "12. Conclusion et conditions de démarrage"),
    ("p", "La présente note fixe les modes opératoires, le phasage et les points d'arrêt qui conditionnent la "
          "bonne exécution des reprises en sous-œuvre et des fondations de l'extension. Elle met en évidence "
          "**trois exigences structurantes** :"),
    ("bullets", [
        "la **conservation intégrale** de la fondation filante existante sous D1, avec une longrine de "
        "répartition ancrée et un arrêt de démolition à son arase supérieure ;",
        "le **poteau d'about encastré** au droit du croisement D3/D5, avec reprise de sa descente de charge au "
        "sous-sol de part et d'autre de la porte PTE 73 ;",
        "la **descente des deux puits de l'extension à l'arase NGF 39,02**, sans générer de poussée sur les murs "
        "de cave existants.",
    ]),
    ("p", "**Le démarrage des travaux est subordonné à la levée des hypothèses H-08, H-09, H-10, H-14 et "
          "H-15** par les sondages décrits dans le registre de la note DOC-01. Les hypothèses **H-01, H-06, "
          "H-16 et H-18** ont été levées par les arbitrages du maître d'ouvrage du 11 novembre 2026 "
          "(DOC-01, chapitre 11)."),
    ("h2", "12.1 Livrables de la Tâche 1 et conditions de passage à la Tâche 2"),
    ("p", "La Tâche 1 est close par la remise des deux notes suivantes, établies en **ISO A4 portrait** et "
          "livrées systématiquement dans les deux formats **.docx** et **.pdf** : **DOC-01** (note d'hypothèses "
          "générales et registre des hypothèses complémentaires) et **DOC-02** (présente note méthodologique "
          "d'exécution et de phasage)."),
    ("bullets", [
        "**Conditions de passage à la Tâche 2** : **satisfaites** — les arbitrages du 11 novembre 2026 ont levé "
        "l'écart E-01 (poteau repositionné sous la poutre) et les hypothèses H-01, H-06, H-16 et H-18. Restent à "
        "programmer les sondages H-08, H-09, H-10, H-14 et H-15, non bloquants pour la Tâche 2 mais nécessaires "
        "avant exécution.",
        "**Documents à produire en Tâche 2** : DOC-03 (note de calculs structurelle détaillée et avant-métré), "
        "en .docx et .pdf.",
    ]),
    ("note", "**La Tâche 1 est terminée.** Les notes DOC-01 et DOC-02 sont livrées aux formats .docx et .pdf. "
             "Les observations éventuelles sur les hypothèses, les modes opératoires ou le phasage doivent être "
             "formulées avant le lancement de la Tâche 2 (note de calculs et avant-métré)."),
]


def main():
    docx_path, pdf_path = build(META, BLOCKS, BASE, "DOC-02_Note_Methodologique_Phasage")
    print("DOCX :", docx_path)
    print("PDF  :", pdf_path)
    print("Pages PDF :", count_pages(pdf_path))


if __name__ == "__main__":
    main()
