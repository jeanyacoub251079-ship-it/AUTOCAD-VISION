"""DOC-01 — Note d'Hypothèses Générales et Registre des Hypothèses Complémentaires.

Affaire : 58 rue de l'Aigle, 92250 La Garenne-Colombes.
Tâche 1 du découpage séquentiel.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common_doc import build  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(BASE, "figures")

META = {
    "entete_gauche": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "entete_droit": "DOC-01 — Note d'hypothèses",
    "pied_gauche": ("BET Structure · Dossier d'exécution — Tâche 1 · Indice A · "
                    "11/11/2026 · Affaire GA-2026-58AIGLE · DOC-01"),
    "titre_pdf": "DOC-01 — Note d'hypothèses générales",
    "sujet_pdf": "Réhabilitation lourde, RSO D1 à D6 et extension — 58 rue de l'Aigle, La Garenne-Colombes",
    "cover": (
        ["NOTE D'HYPOTHÈSES", "GÉNÉRALES"],
        "Registre des hypothèses complémentaires retenues par le BET (à valider sur site par sondages)",
        [
            ("Affaire", "Réhabilitation lourde, restructuration intérieure et extension en façade avant"),
            ("Adresse", "58 rue de l'Aigle — 92250 La Garenne-Colombes (Hauts-de-Seine)"),
            ("Maître d'ouvrage", "Particulier — maison individuelle existante"),
            ("Maître d'œuvre", "Cabinet AARKA — SAS d'architecture, 51 rue Saint-Louis-en-l'Île, 75004 Paris"),
            ("Bureau d'études", "BET Structure — Études d'exécution Gros Œuvre & Structure"),
            ("Mission", "RSO D1 à D6 (profilés acier + appuis BA), structure BA de l'extension, "
                        "notes méthodologiques et plans d'exécution"),
            ("Document", "**DOC-01** — Note d'hypothèses générales et registre des hypothèses complémentaires"),
            ("Livrables", "**DOC-01.docx** et **DOC-01.pdf** (ISO A4 portrait) ; note méthodologique DOC-02 en pièce jointe"),
            ("Indice / date", "**A** — 11 novembre 2026"),
            ("Phase", "DCE — Tâche 1 / 4 (analyse Vision-DXF, DOC-01, DOC-02)"),
            ("Format", "ISO A4 portrait (210 × 297 mm) — livré en .docx et .pdf"),
            ("Références", "NF EN 1990/1991/1992/1993/1996/1997 + annexes nationales françaises ; "
                           "DTU 13.1, 13.2, 20.1, 21, 32.1"),
        ],
        "**Avertissement.** La présente note constitue un document d'études d'exécution établi sur la base "
        "des pièces graphiques communiquées (planches DCE du 05.11.2026 et fichier DXF associé) et des "
        "hypothèses de calcul fixées au cahier des charges. En l'absence d'étude géotechnique G2 et de "
        "relevé structurel contradictoire, **les hypothèses du registre (chapitre 8) doivent être confirmées par "
        "sondages avant tout début de travaux**. Toute divergence relevée en phase chantier doit être "
        "portée à la connaissance du BET avant exécution ; elle fera l'objet d'un avenant indicé.",
    ),
}

# --------------------------------------------------------------------------
# Tableaux de données
# --------------------------------------------------------------------------
T_NIVEAUX = {
    "header": ["Repère", "Niveau", "Cote NGF", "Hauteur / RDC", "Source"],
    "widths": [18, 46, 15, 20, 34],
    "rows": [
        ["Jardin / terrain naturel", "Extérieur", "**41,11**", "− 0,35 m", "P09b, P10b, P11b"],
        ["Terrasse RdC extérieure", "Extérieur", "**41,35**", "− 0,11 m", "P09b"],
        ["Point de référence", "Axe niveau RDC intérieur", "**41,46**", "± 0,00", "Toutes planches"],
        ["Sol fini RDC", "RDC", "41,46 (+ 05 = 41,51)", "± 0,00", "P08b, P10b"],
        ["Sol fini Sous-sol", "S/Sol", "**39,26**", "− 2,20 m", "HSP 196 à 200 + plancher"],
        ["Sous-face plancher haut RDC", "Plafond RDC", "**44,08**", "+ 2,62 m", "P09b, P10b, P11b"],
        ["Sol fini R+1", "R+1", "**44,32**", "+ 2,86 m", "P09b, P10b, P11b"],
        ["Sous-face plancher haut R+1", "Plafond R+1", "**46,94**", "+ 5,48 m", "P09b, P11b"],
        ["Sol fini Combles", "Combles", "**47,14**", "+ 5,68 m", "P09b, P10b"],
        ["Gouttière (existant)", "Toiture", "**47,47**", "+ 6,01 m", "P09b, P10b, P11b"],
        ["Ligne de bris (projet Mansart)", "Toiture", "**49,51**", "+ 8,05 m", "P09b, P10b"],
        ["Faîtage — état actuel", "Toiture", "**49,54**", "+ 8,08 m", "P08a, P09a, P11a"],
        ["Faîtage — projet", "Toiture", "**50,16**", "+ 8,70 m", "P09b, P10b, P11b"],
        ["Gouttière basse extension", "Extension", "**44,18**", "+ 2,72 m", "P10b, P11b"],
        ["**Arase d'acrotère / poutre retroussée**", "Extension", "**44,75**", "+ 3,29 m", "P10b, P11b"],
        ["Fond de fouille des fondations existantes", "Infrastructure", "**39,02**", "− 2,44 m", "P09a, P11a"],
    ],
    "caption": "Tableau 1 — Niveaux altimétriques relevés sur les planches DCE (cotes NGF en mètres). "
               "Le niveau 41,46 constitue le point de référence unique de l'affaire (axe niveau RDC intérieur).",
}

T_GEOM = {
    "header": ["Zone", "Dimension hors-œuvre", "Valeur", "Source / méthode"],
    "widths": [30, 34, 12, 24],
    "rows": [
        ["Sous-sol", "Emprise intérieure (L × l)", "8,53 × 7,30 m", "DXF — calque ARK-MURS, plan P08a S/Sol"],
        ["RDC", "Emprise intérieure (L × l)", "12,46 × 7,30 m", "DXF — plan P08a RDC"],
        ["RDC + extension", "Profondeur totale", "7,30 + 2,00 = **9,30 m**", "Arbitrage E-02 du 11/11/2026"],
        ["Extension", "Largeur façadée", "**8,03 m**", "P08b RDC — cote 803 (chaîne 387 + 416)"],
        ["Extension", "Profondeur / avant de façade", "**2,00 m**", "E-02 — terrasse poutre-acrotère comprise"],
        ["Verrière", "Hauteur libre sous poutre", "**2,30 m**", "P10b, P11b — cote 230"],
        ["Extension", "Hauteur libre sous poutre retroussée", "2,62 m", "P11b — cote 262 (noyau)"],
        ["Extension", "Surface au sol (emprise)", "8,03 × 2,00 ≈ **16,1 m²**", "Calcul BET"],
        ["Terrasse accessible", "Surface utile (emprise)", "≈ 13,7 m²", "8,03 × (2,00 − 0,30)"],
        ["Extension", "Position du poteau BA", "**1,30 m** du nu de façade", "E-02 — console 0,70 m"],
        ["Extension", "Porte-à-faux de la dalle", "**1,70 m** depuis la façade", "nu intérieur de la poutre"],
        ["Trappe à linge", "Ouverture en plancher", "**45 × 40 cm**", "P08b R+1 et RDC — polyligne 42843/42888"],
    ],
    "caption": "Tableau 2 — Géométrie générale extraite du fichier DXF "
               "(unités de dessin : centimètres, $INSUNITS = 5).",
}

T_MURS = {
    "header": ["Élément", "Épaisseur", "Nature supposée", "Localisation"],
    "widths": [34, 12, 28, 26],
    "rows": [
        ["Mur de façade avant (RDC)", "29 à 31 cm", "Meulière / moellons + enduit", "Façade sur rue — support D2, D4"],
        ["Mur de façade avant (avec doublage)", "47 à 49 cm", "Idem + doublage intérieur", "Axe des ouvertures D2 et D4"],
        ["Mur de façade arrière", "46 cm", "Meulière / moellons", "Cuisine — support D6"],
        ["Mur de refend longitudinal D1", "**16 cm**", "Maçonnerie de briques / cloison porteuse", "Entrée / Bureau — zone non excavée"],
        ["Mur de refend central D3", "**57 cm**", "Meulière + conduit de cheminée", "Derrière le futur poêle"],
        ["Mur de refend transversal D5", "**16 cm**", "Maçonnerie de briques / cloison porteuse", "Salle à manger / Cuisine"],
        ["Murs de cave périphériques", "48 cm", "Meulière hourdée au mortier bâtard", "Sous-sol — faces enterrées"],
        ["Mur de refend de cave (PTE 73)", "**40 cm**", "Meulière hourdée", "Cave / Buanderie — sous le nœud D3/D5"],
        ["Limite de propriété est (extension)", "—", "Aucun mur existant — **voile BA à créer**", "Limite séparative est — prolongement du pignon"],
    ],
    "caption": "Tableau 3 — Épaisseurs de murs relevées ou déduites des coupes et du plan DXF. "
               "Les épaisseurs marquées en gras conditionnent directement le dimensionnement des appuis.",
}

T_OUV = {
    "header": ["Rep.", "Localisation", "Portée libre", "Ép. mur", "Hauteur libre", "Nature de la reprise"],
    "widths": [7, 28, 11, 9, 11, 34],
    "rows": [
        ["**D1**", "Refend Entrée / Bureau (longitudinal)", "**2,60 m**", "16 cm", "2,62 m",
         "Suppression de mur porteur — zone **non excavée** (Coupe 01). Fondation filante existante conservée."],
        ["**D2**", "Façade avant — Salon", "**3,80 m**", "47 cm", "2,15 m",
         "Élargissement de baie — 3 travées. Mur de façade porteur, planchers RDC et R+1 rapportés."],
        ["**D3**", "Refend central longitudinal (derrière le poêle)", "**3,55 m**", "57 cm", "2,40 m",
         "Suppression de mur de refend + conduit de cheminée. Croisement avec D5."],
        ["**D4**", "Façade avant — Salle à manger", "**2,00 m**", "49 cm", "2,15 m",
         "Élargissement de baie. Mur de façade porteur."],
        ["**D5**", "Refend transversal Salle à manger / Cuisine", "**3,08 m**", "16 cm", "2,40 m",
         "Suppression de mur porteur transversal. Croisement avec D3."],
        ["**D6**", "Façade arrière — Cuisine", "**1,54 m**", "46 cm", "2,15 m",
         "Élargissement de baie. Mur de façade porteur."],
    ],
    "caption": "Tableau 4 — Reprises en sous-œuvre : dimensions de démolition mesurées sur le DXF "
               "(zones hachurées du calque ARK-DEMOL, planche P08a) et hauteurs libres disponibles.",
}

T_CHARGES = {
    "header": ["Désignation", "Symbole", "Valeur retenue", "Base / justification"],
    "widths": [40, 10, 20, 30],
    "rows": [
        ["Poids propre plancher haut du Sous-sol", "G₀", "**400 kg/m²**", "Hypothèse imposée (cahier des charges)"],
        ["Poids propre planchers haut RDC et R+1", "G₀", "**300 kg/m²**", "Hypothèse imposée"],
        ["Dalle BA de l'extension (ép. 20 cm)", "G₀", "500 kg/m²", "25 kN/m³ × 0,20 m"],
        ["Charges permanentes rapportées (revêtements, chapes, cloisons, plafonds)", "G₁", "**150 kg/m²**",
         "Hypothèse imposée"],
        ["Surcharge d'exploitation — planchers courants (cat. A)", "Q", "**150 kg/m²**",
         "NF EN 1991-1-1 + AN : 1,5 kN/m²"],
        ["Surcharge d'exploitation — toiture-terrasse accessible", "Q", "**150 kg/m²**",
         "Catégorie A, terrasse accessible privative"],
        ["Surcharge d'exploitation — combles aménagés", "Q", "**150 kg/m²**", "Hypothèse imposée"],
        ["Complexe de charpente / couverture (neige + vent incluses)", "G + Q", "**250 kg/m²**",
         "Décomposé ci-dessous : G = 110, Q = 140"],
        ["  dont part permanente du complexe", "G", "110 kg/m²", "Charpente bois, voliges, couverture, ITE"],
        ["  dont part variable climatique (neige + vent)", "Q", "140 kg/m²",
         "Zone A2 (Hauts-de-Seine) : sₖ ≈ 0,45 kN/m² ; vent qp ≈ 0,60 kN/m² en projection"],
        ["Cloison de doublage / ITE en façade (par m² de façade)", "g", "60 kg/m²", "AARKA P08b — doublage ITE + enduit 200 mm"],
        ["Garde-corps et acrotère de la terrasse", "g", "1,00 kN/m", "NF EN 1991-1-1 — effort horizontal 1 kN/m"],
    ],
    "caption": "Tableau 5 — Charges gravitaires et climatiques retenues. Les valeurs en gras sont imposées "
               "par le cahier des charges et ne sont pas révisables sans avenant.",
}

T_MAT = {
    "header": ["Matériau", "Caractéristiques retenues", "Norme / commentaire"],
    "widths": [26, 38, 36],
    "rows": [
        ["Béton armé neuf", "**C25/30** — f<sub>ck</sub> = 25 MPa ; f<sub>cd</sub> = 16,7 MPa ; "
                            "f<sub>ctm</sub> = 2,6 MPa ; E<sub>cm</sub> = 31 000 MPa ; γ = 2 500 kg/m³",
         "NF EN 1992-1-1 + AN, NF EN 206-1 — classe d'exposition XC1 à XC4 selon localisation"],
        ["Armatures passives", "**B500B** — f<sub>yk</sub> = 500 MPa ; f<sub>yd</sub> = 435 MPa ; "
                               "E<sub>s</sub> = 200 000 MPa", "NF EN 1992-1-1 + AN — ductilité classe B"],
        ["Acier de construction (profilés RSO)", "**S275** (f<sub>y</sub> = 275 MPa) retenu par défaut ; "
                                                  "S355 (f<sub>y</sub> = 355 MPa) si encombrement réduit nécessaire ; γ = 7 850 kg/m³",
         "NF EN 1993-1-1 + AN — NF EN 10025-2"],
        ["Maçonnerie ancienne (meulière / moellons)", "γ = 2 000 kg/m³ ; f<sub>d</sub> = **1,2 MPa** "
                                                       "(compression verticale sous sommier) ; f<sub>k</sub> = 3,0 MPa",
         "NF EN 1996-1-1 + AN — valeurs à confirmer par essais pénétrométriques"],
        ["Gros béton de puits", "**C16/20** — γ = 2 300 kg/m³", "DTU 13.1 — béton de propreté et de remplissage"],
        ["Remblai / hérisson sous dallage", "Grave compactée 0/31,5 — γ = 2 000 kg/m³",
         "DTU 13.3 — portance ≥ 50 MPa (essai à la plaque)"],
        ["Mortier de calage sans retrait", "Résistance ≥ 40 MPa à 28 j — ép. 20 à 50 mm",
         "NF EN 1504-6 — calage sous platine et sous sommier"],
    ],
    "caption": "Tableau 6 — Hypothèses de matériaux. Les résistances de la maçonnerie ancienne sont des "
               "hypothèses sécuritaires à confirmer par sondages (voir registre, ligne H-08).",
}

T_GEO = {
    "header": ["Paramètre", "Valeur retenue", "Commentaire"],
    "widths": [36, 22, 42],
    "rows": [
        ["Contrainte admissible du sol à l'ELS", "**q<sub>els</sub> = 0,10 MPa** (100 kPa)", "1,0 bar = 10 t/m² — hypothèse imposée"],
        ["Contrainte ultime de calcul à l'ELU", "**q<sub>elu</sub> = 0,15 MPa** (150 kPa)", "Hypothèse imposée"],
        ["Niveau d'assise des nouvelles fondations", "**NGF 39,02** (− 2,44 m / RDC)", "Même arase que les fondations existantes"],
        ["Profondeur de fond de fouille", "2,44 m sous le sol RDC fini", "Coupes P09a / P11a"],
        ["Nature du sol supposée", "Remblais limono-sableux en tête, puis limon argileux / marnes résiduelles",
         "Sondages à la pelle mécanique avant travaux"],
        ["Nappe phréatique", "Supposée **non rencontrée** à 2,44 m", "À vérifier impérativement — H-14"],
        ["Poids volumique du sol", "18 kN/m³ (au-dessus du niveau de la nappe)", "Calcul de poussée des terres"],
        ["Coefficient de poussée au repos", "K₀ = 0,5", "NF EN 1997-1 — vérification des murs de cave existants"],
        ["Tassement admissible", "≤ 10 mm différencié entre extension et existant", "Prévention de la fissuration"],
    ],
    "caption": "Tableau 7 — Hypothèses géotechniques. En l'absence d'étude G2, ces valeurs sont "
               "sécuritaires et doivent permettre un chiffrage ferme par l'entreprise.",
}

T_CRIT = {
    "header": ["Vérification", "Critère retenu", "Référence"],
    "widths": [30, 44, 26],
    "rows": [
        ["Combinaison ELU fondamentale (STR/GEO)", "1,35 G + 1,50 Q", "NF EN 1990 + AN — tableau A1.2(B)"],
        ["Combinaison ELS caractéristique", "G + Q", "NF EN 1990 + AN"],
        ["Combinaison ELS quasi-permanente", "G + ψ₂ Q avec ψ₂ = 0,3 (cat. A)", "NF EN 1990 + AN"],
        ["**Flèche des profilés métalliques sous murs conservés**", "**w ≤ L/750 ET w ≤ 5 mm** (charges ELS)",
         "Exigence RSO du cahier des charges"],
        ["Flèche des profilés sous verrière", "**w ≤ L/750 ET w ≤ 5 mm**", "Prévention de la mise en compression des vitrages"],
        ["Flèche de la poutre retroussée BA", "w ≤ L/500 sous charges quasi-permanentes", "NF EN 1992-1-1 §7.4.1"],
        ["Fissuration des ouvrages BA", "w<sub>k</sub> ≤ 0,3 mm (XC1) — 0,2 mm en ambiance humide (XC4)",
         "NF EN 1992-1-1 §7.3"],
        ["Ouverture de fissure en maçonnerie conservée", "Aucune fissure traversante admissible", "DTU 20.1 §7"],
        ["Contrainte sous sommier sur maçonnerie ancienne", "σ ≤ f<sub>d</sub> = 1,2 MPa (local)", "NF EN 1996-1-1 + AN"],
        ["Contrainte de contact au sol", "σ<sub>ELS</sub> ≤ 0,10 MPa ; σ<sub>ELU</sub> ≤ 0,15 MPa", "NF EN 1997-1 / NF P 94-261"],
        ["Déversement des profilés métalliques", "Vérification au déversement ELU selon §6.3.2", "NF EN 1993-1-1 + AN"],
        ["Résistance au feu", "**REI 30** minimum sur les éléments porteurs (habitat individuel R+1)",
         "Arrêté du 31 janvier 1986 modifié — hypothèse H-19"],
        ["Classe de conséquence / catégorie", "CC1 — catégorie d'usage A — classe de ductilité DCL", "NF EN 1990 + AN"],
    ],
    "caption": "Tableau 8 — Critères de vérification et combinaisons d'actions.",
}

T_REGISTRE = {
    "header": ["N°", "Sujet", "Hypothèse retenue par le BET", "Justification / conséquence", "Validation sur site"],
    "widths": [6, 18, 34, 28, 14],
    "rows": [
        ["H-01", "Nature et largeur de la fondation filante existante sous D1",
         "Semelle filante **continue en meulière hourdée**, largeur 0,50 m, hauteur 0,40 m, arase inférieure "
         "NGF 39,02 ; béton de propreté absent.",
         "**Hypothèse LEVÉE par le maître d'ouvrage le 11/11/2026 : fondation de type meulière continue.** "
         "Aucune coupe ne montre la fondation sous D1 (zone non excavée, Coupe 01). La longrine de répartition BA "
         "est calculée pour reprendre la totalité des charges sur une bande de 0,50 m minimum, sans élargissement.",
         "**Dit du maître d'ouvrage** — contrôle visuel en pied de mur lors de l'ouverture des fouilles, sans "
         "caractère bloquant."],
        ["H-02", "Continuité de la fondation sous D1 au droit des poteaux BA",
         "Fondation filante **continue** sous toute la longueur du mur D1 (pas de discontinuité ni de regard).",
         "Condition de validité du schéma de longrine de répartition ; en cas de discontinuité, reprise par semelle "
         "isolée et désolidarisation.",
         "Sondage H-01 + inspection visuelle de l'assise."],
        ["H-03", "Sens de portée des planchers existants",
         "Planchers bois à solives portant **perpendiculairement** aux façades (portée 3,60 à 4,10 m), appuis sur les "
         "murs de façade et les refends longitudinaux.",
         "Détermine les bandes de chargement reprises par D1, D2, D3, D4. Le sens inverse majorerait les charges sur "
         "D5 et D6 de 15 à 20 %.",
         "Sondage destructif : dépose de 2 lames de parquet, relevé du sens des solives."],
        ["H-04", "Constitution du plancher haut du Sous-sol",
         "Plancher mixte bois-hourdis de 20 cm d'épaisseur totale, G₀ = 400 kg/m² (valeur imposée), portée 3,60 m.",
         "Valeur imposée par le cahier des charges ; cohérente avec un plancher à solives 20 × 22 cm à entraxe 45 cm.",
         "Sondage en sous-face (cave) : relevé des sections et entraxes de solives."],
        ["H-05", "Constitution et portée du plancher haut du RDC",
         "Plancher bois de 20 cm, G₀ = 300 kg/m², solives 18 × 20 cm à entraxe 45 cm, portée 3,55 à 3,65 m.",
         "Valeur imposée G₀ = 300 kg/m². Conditionne le dimensionnement des profilés D2, D3, D4, D5.",
         "Sondage en sous-face (RDC) après dépose des faux-plafonds."],
        ["H-06", "Descente de charges de la charpente bois des combles "
                 "(**validée par le maître d'ouvrage le 11/11/2026**)",
         "Charpente à fermettes / pannes sur murs gouttereaux et refends ; charge totale 250 kg/m² en projection, "
         "dont 110 kg/m² permanente et 140 kg/m² climatique.",
         "La charpente est hors mission mais ses charges sont reprises intégralement dans les descentes de charges "
         "(rappels aux murs gouttereaux : 1,2 kN/m² de rampant).",
         "Relevé de la charpente existante + note du charpentier (hors mission)."],
        ["H-07", "Surcharge d'exploitation des combles aménagés",
         "Q = 150 kg/m² sur la totalité de la surface des combles (aucun déclassement partiel).",
         "Hypothèse imposée ; les combles sont aménagés (chambres 4, 5, 6 et salle de jeux).",
         "Sans objet (hypothèse de calcul)."],
        ["H-08", "Résistance de la maçonnerie ancienne en meulière",
         "f<sub>d</sub> = **1,2 MPa** en compression locale sous sommier ; f<sub>k</sub> = 3,0 MPa ; module "
         "E = 1 000 MPa. Mortier de chaux médiocre supposé.",
         "Valeur prudente pour de la meulière hourdée au mortier de chaux. Une valeur inférieure imposerait "
         "l'élargissement des sommiers BA (rapport de 1,3).",
         "**Essais obligatoires** : 3 carottages + essais de compression, ou scléromètre + pénétromètre."],
        ["H-09", "Homogénéité et cohésion des murs de façade au droit de D2, D4 et D6",
         "Murs pleins, sans cavité ni reprise de maçonnerie masquée sur la hauteur intéressée (2,15 m).",
         "Une cavité ou un chaînage ancien non repéré modifierait le schéma d'appui des profilés et imposerait un "
         "chemisage.",
         "**Sondages obligatoires** : 2 fenêtres de sondage par ouverture (6 au total), 40 × 40 cm."],
        ["H-10", "Existence et état des conduits de cheminée dans D3",
         "Conduits de fumée **désaffectés et vides** sur toute la hauteur ; maçonnerie de briques en bon état, "
         "susceptible de recevoir un scellement structurel.",
         "Le poteau d'about D3/D5 est encastré dans l'about du refend, à proximité immédiate des conduits. Un conduit "
         "non vide ou instable interdirait le scellement.",
         "**Sondage obligatoire** : dépose du chapeau et passage caméra, plus essai de charge d'ancrage."],
        ["H-11", "Position du poteau BA de la verrière",
         "Poteau **25 × 25 cm** implanté à **1,30 m du nu de la façade existante**, à l'extrémité gauche des "
         "8,03 m, sous la poutre-acrotère perpendiculaire (arbitrage E-02 du 11/11/2026).",
         "Le DXF place l'axe à 1,19 m du nu de façade : l'écart de 11 cm est absorbé par la tolérance "
         "d'implantation de 5 cm et par la largeur du poteau (25 cm). La terrasse mesure 2,00 m de profondeur, "
         "poutre-acrotère comprise, ce qui laisse 0,70 m de porte-à-faux derrière le poteau.",
         "**Position arrêtée le 11/11/2026** — reprise dans `niveaux_retenus.py` "
         "(`POS_POTEAU_FAÇADE = 1,30 m`), source unique pour les notes et les plans."],
        ["H-12", "Nature du mur en limite de propriété est",
         "**Aucun mur mitoyen existant** : le voile BA de rive est **à créer**, en limite de propriété, dans le "
         "prolongement du mur pignon, sur une **semelle filante neuve** (65 × 30 cm) descendue à NGF 39,02.",
         "La version antérieure de la note supposait un mur mitoyen en meulière de 35 cm servant d'appui. Ce mur "
         "n'existe pas : ni la poutre-acrotère ni le voile ne peuvent s'y appuyer.",
         "**Hypothèse levée le 11/11/2026 (arbitrage E-02)** — reprise dans `niveaux_retenus.py` "
         "(`L_VOILE_RIVE`, `EP_VOILE`, `NGF_FONDATION`)."],
        ["H-13", "Altitude des fondations existantes côté extension",
         "Arase inférieure des fondations existantes à **NGF 39,02** sur tout le pourtour de l'extension.",
         "Le nivellement des deux puits de l'extension doit atteindre cette arase pour éviter toute poussée "
         "différentielle sur les murs de cave.",
         "**Fouille de reconnaissance** de 1,50 m de profondeur aux deux extrémités de l'extension."],
        ["H-14", "Présence de la nappe phréatique",
         "Nappe **non rencontrée** au niveau d'assise (39,02) ; sol non saturé.",
         "La présence d'eau imposerait un bétonnage sous eau ou un rabattement, non chiffré à ce stade.",
         "**Sondage obligatoire** : 2 piézomètres ou observation directe en fond de fouille."],
        ["H-15", "Réseaux enterrés dans l'emprise des puits de l'extension",
         "Aucun réseau enterré (EU/EP, AEP, gaz, électricité, chauffage) dans l'emprise des deux puits.",
         "Un réseau non repéré impose un dévoiement ou un fourreau, avec impact sur le planning.",
         "**DT-DICT obligatoire** + sondages manuels avant terrassement."],
        ["H-16", "Entraxe des solives pour l'implantation de la trappe à linge",
         "La trappe est **repérée sur les plans de projet** (P08b) aux trois niveaux : Combles x ≈ 46491, "
         "R+1 x ≈ 42890, RDC x ≈ 48491, avec une ouverture de 30 × 31 cm. Entraxe des solives estimé à **45 cm** "
         "(solin 40 cm).",
         "**Arbitrage du maître d'ouvrage du 11/11/2026** : la position est estimée à partir des plans, puis "
         "**entourée d'un nuage de révision sur les plans d'exécution** pour signifier qu'elle reste à confirmer. "
         "Aucune solive ne doit être coupée : l'ouverture reste calée entre deux solives.",
         "**Relevé d'entraxe obligatoire** avant tracé d'exécution ; report au nuage sur PL-01 à PL-03."],
        ["H-17", "Continuité du plancher haut du RDC au droit de l'extension",
         "Le plancher haut du RDC existant est **conservé** et prolongé par la dalle BA de terrasse, avec joint de "
         "désolidarisation et appui simple sur le mur de façade conservé.",
         "Évite de transmettre les déformations de l'extension aux planchers anciens.",
         "Sans objet (choix de conception validé en réunion)."],
        ["H-18", "Caractéristiques de la verrière (hors mission) "
                 "(**validée par le maître d'ouvrage le 11/11/2026**)",
         "Poids propre de la verrière et de son ossature aluminium : **0,60 kN/m²** en couverture, "
         "0,45 kN/m² en façade ; charges transmises ponctuellement aux appuis BA.",
         "La verrière est hors mission mais ses charges d'appui sont intégrées à la descente de charges de la "
         "poutre retroussée et du poteau BA.",
         "**Fiche technique du verriériste** à obtenir avant Tâche 2 (valeur de substitution retenue)."],
        ["H-19", "Exigence de résistance au feu des éléments porteurs",
         "**REI 30** pour les poteaux, poutres et planchers porteurs ; **EI 30** pour les parois séparatives.",
         "Maison individuelle de 2e famille, R+1 sur sous-sol : le arrêté du 31 janvier 1986 impose R 30 minimum "
         "sur la structure porteuse.",
         "À confirmer par le bureau de contrôle / l'architecte (H-19)."],
        ["H-20", "Protection des profilés métalliques contre la corrosion",
         "Profilés en ambiance intérieure sèche (XC1) : **galvanisation à chaud 50 µm** + peinture intumescente "
         "pour la protection au feu. En zone enterrée : béton d'enrobage 40 mm.",
         "Assure la durabilité de classe de conception 50 ans (NF EN 1993-1-1 §4).",
         "Sans objet (prescription d'exécution)."],
        ["H-21", "Phasage de démolition et maintien des étaiements",
         "Aucune démolition simultanée de deux ouvertures sur un même mur porteur ; étaiement provisoire maintenu "
         "**jusqu'à décoffrage complet** des appuis BA (28 jours).",
         "Le non-respect de ce phasage conduirait à un état de ruine non calculé.",
         "**Plan de phasage à viser** par le BET avant démarrage (pièce DOC-02, § 3)."],
        ["H-22", "État des planchers au-dessus des ouvertures D2 et D4",
         "Planchers haut RDC et haut R+1 en bon état, sans pourriture ni insectes, capables de reprendre les "
         "efforts après repose sur les profilés.",
         "Un plancher dégradé imposerait un remplacement local, non chiffré.",
         "**Sondage obligatoire** : ouverture de 2 trappes de visite par niveau après étaiement."],
        ["H-23", "Absence de cave sous la zone D1 (Coupe 01)",
         "La zone D1 se situe hors emprise du sous-sol : il n'y a **pas de cave** sous le Bureau et l'Entrée.",
         "Fonde l'hypothèse H-01 et le schéma de longrine de répartition sur fondation filante existante.",
         "Vérification visuelle depuis la cave et la trappe d'accès."],
        ["H-24", "Alimentation et évacuation des eaux au droit des puits",
         "Aucune descente d'eaux pluviales ni d'eaux usées traversant l'emprise des puits de l'extension.",
         "Un collecteur à dévoyer modifierait l'implantation du puits côté mitoyen.",
         "DT-DICT + inspection caméra des réseaux existants."],
    ],
    "caption": "Tableau 9 — REGISTRE DES HYPOTHÈSES COMPLÉMENTAIRES RETENUES PAR LE BET "
               "(À VALIDER SUR SITE PAR SONDAGES). Toute hypothèse non confirmée doit faire l'objet d'un "
               "avenant indicé avant exécution des travaux concernés.",
    "font": 6.8,
}

T_ECARTS = {
    "header": ["N°", "Point relevé", "Écart constaté", "Traitement proposé"],
    "widths": [6, 24, 40, 30],
    "rows": [
        ["E-01", "Position du poteau BA de la verrière",
         "Le cahier des charges indique « 2,00 m en avant de la façade existante ». Le DXF place l'axe du poteau "
         "à 1,19 m du nu de la façade existante (2,01 m du nu de la verrière).",
         "**ÉCART CADUC depuis le 11/11/2026** — l'arbitrage E-01 est **remplacé par E-02** : le poteau est "
         "implanté à **1,30 m du nu de façade** et la poutre-acrotère de 8,03 m est **isostatique**, appuyée sur "
         "le voile de rive à créer et sur l'about de la poutre perpendiculaire en console (DOC-03 §3.4)."],
        ["E-02", "Schéma structurel de l'extension",
         "Le schéma de la première version supposait un voile mitoyen **existant**, un poteau à 2,00 m sous la "
         "poutre et une terrasse de 3,20 m. Le croquis du maître d'œuvre du 11/11/2026 montre un tout autre "
         "dispositif : voile **à créer** en limite de propriété, poteau à 1,30 m de la façade, poutre "
         "perpendiculaire de 1,30 m prolongée par une console de 0,70 m, terrasse de 2,00 m de profondeur.",
         "**Schéma E-02 retenu le 11/11/2026** et appliqué à l'ensemble des notes et des plans : terrasse "
         "8,03 × 2,00 m, poutre perpendiculaire 25 × 67, poteau BA 25 × 25 à 1,30 m, voile de rive 20 cm sur "
         "semelle filante 65 × 30, dalle en console de 1,70 m. Le schéma antérieur est **définitivement "
         "abandonné**. Voir `niveaux_retenus.py` (bloc « Géométrie de l'extension — rectification 11/11/2026 »)."],
        ["E-03", "Ouverture de la trappe à linge",
         "L'ouverture dessinée (45 × 40 cm) est incompatible avec un entraxe de solives de 45 cm.",
         "Réduction à 40 × 36 cm et/ou décalage latéral dans la zone de tolérance (voir DOC-02 § 6)."],
        ["E-04", "Niveau du faîtage projeté",
         "Le faîtage passe de 49,54 à 50,16 NGF (+ 0,62 m) ; la ligne de bris apparaît à 49,51 NGF.",
         "Impact sur les charges de charpente : + 7 % de poids de couverture, intégré dans la descente de charges."],
        ["E-05", "Cote HSP des combles",
         "Hauteurs sous plafond relevées de 180 à 302 cm selon les points : la pente du rampant interdit une "
         "hauteur unique.",
         "Aucun impact structurel ; les surcharges sont appliquées sur la totalité de la surface (H-07)."],
        ["E-06", "Cotes 858,9 / 826 / 822 cm sur le plan P08b RDC",
         "Trois valeurs coexistent avec la cote de façade 803 cm, sans référence d'axe explicite.",
         "Non retenues : la cote de calcul reste **8,03 m** (façade), les autres correspondant à des cotes de "
         "nu à nu incluant le voile de rive à créer."],
    ],
    "caption": "Tableau 10 — Écarts et incohérences relevés entre les pièces du dossier et l'analyse du DXF.",
}

# --------------------------------------------------------------------------
# Blocs
# --------------------------------------------------------------------------
BLOCKS = [
    ("h1", "1. Objet et cadre de la mission"),
    ("p", "La présente note constitue le premier livrable de la mission d'études d'exécution Gros Œuvre et "
          "Structure confiée au BET pour la réhabilitation lourde, la restructuration intérieure et l'extension "
          "d'une maison individuelle située **58 rue de l'Aigle, 92250 La Garenne-Colombes**."),
    ("p", "Elle a pour objet de fixer, avant tout calcul, **l'ensemble des données d'entrée** du dimensionnement : "
          "géométrie extraite des pièces graphiques, niveaux altimétriques, hypothèses de matériaux, "
          "hypothèses de charges, critères de vérification réglementaires et hypothèses complémentaires retenues "
          "par le BET en l'absence de données. Elle constitue le document de référence contractuel auquel se "
          "rattacheront les notes de calcul (DOC-03) et les plans d'exécution (PL-01 à PL-05)."),
    ("p", "La mission est strictement limitée au périmètre suivant :"),
    ("bullets", [
        "**Reprises en sous-œuvre D1 à D6** au rez-de-chaussée : renforts horizontaux par profilés métalliques "
        "S275/S355 et renforts verticaux par poteaux, jambages et sommiers en béton armé C25/30.",
        "**Structure en béton armé de l'extension** en façade avant : dalle de toiture-terrasse, poutre-acrotère de rive, poutre "
          "perpendiculaire en console, voile de rive à créer sur semelle filante, poteau BA noyé dans la "
          "verrière, puits de gros béton et longrines.",
        "**Renforcement de la descente de charges au sous-sol** sous le nœud central D3/D5, à proximité immédiate "
        "de la porte existante PTE 73.",
        "**Définition de l'implantation de la trappe à linge** entre solives, sans chevêtre.",
        "**Méthodologie d'exécution et de phasage**, notes d'hypothèses et de calcul, avant-métré, plans "
        "d'exécution et plans de détails.",
    ]),
    ("p", "Sont **expressément exclus** de la mission, tout en étant pris en compte dans les descentes de charges : "
          "le calcul et les plans d'exécution de la **charpente bois des combles** (modification à la Mansart) ; "
          "le calcul et les plans de **menuiserie / serrurerie de la verrière** (façade avant et auvent arrière) ; "
          "les lots techniques (CVC, électricité, plomberie) ; l'étude géotechnique G2 ; le contrôle de la "
          "structure existante par essais non destructifs, qui reste à la charge du maître d'ouvrage."),

    ("h1", "2. Base documentaire analysée"),
    ("h2", "2.1 Pièces communiquées"),
    ("table", {
        "header": ["Réf.", "Intitulé", "Échelle", "Contenu exploité"],
        "widths": [10, 44, 12, 34],
        "rows": [
            ["P08a", "Plans repères Coupes — État actuel & Démolitions (S/Sol, RDC, R+1, Combles)", "1/100",
             "Zones de démolition D1 à D6, épaisseurs de murs, hauteurs sous plafond"],
            ["P08b", "Plans repères Coupes — Projet (S/Sol, RDC, R+1, Combles)", "1/100",
             "Emprise de l'extension, poteau BA, trappes à linge, cotes 803 / 826 / 320 (cote 320 reprise "
             "en cote de terrasse 200 par l'arbitrage E-02)"],
            ["P09a / P09b", "Coupe 01 — État actuel / Projet (passant par D1)", "1/50",
             "Absence de sous-sol sous D1, fondation filante, hauteurs 262"],
            ["P10a / P10b", "Coupe 02 — État actuel / Projet (Salon, extension, D2)", "1/50",
             "Poutre-acrotère, poteau BA à 1,30 m, arase 44,75, gouttière 44,18"],
            ["P11a / P11b", "Coupe 03 — État actuel / Projet (Salle à manger, extension, D3 à D6)", "1/50",
             "Croisement D3/D5, « POTEAU BÉTON », descentes de charges vers le sous-sol"],
            ["DXF", "DCE_58 RUE DE L'AIGLE_LA GARENNE COLOMBES MODIF 05112026-export.dxf", "—",
             "14 046 entités, 46 calques ARK-*, 4 présentations — extraction automatique par script"],
        ],
        "caption": "Tableau 11 — Pièces du dossier de consultation exploitées.",
        "font": 7.2,
    }),

    ("h2", "2.2 Méthode d'analyse"),
    ("p", "L'analyse a été conduite selon deux voies complémentaires :"),
    ("bullets", [
        "**Inspection visuelle** des 8 planches A3 (rendu 150 à 1100 dpi et recadrages ciblés) afin d'identifier "
        "les zones de démolition, les repères D1 à D6, les cotes de niveau NGF et les hauteurs sous plafond.",
        "**Analyse programmatique du DXF** (bibliothèque `ezdxf`) : inventaire des entités par calque, extraction "
        "des cotes natives (`DIMENSION`), des niveaux NGF (`MTEXT`), des zones hachurées de démolition "
        "(calque `ARK-DEMOL`), des épaisseurs de murs (calque `ARK-MURS`) et des repères D1 à D6 (attributs de blocs)."
    ]),
    ("note", "**Contrôle des unités CAO.** Le fichier DXF déclare `$INSUNITS = 5` (centimètres) et "
             "`$MEASUREMENT = 1` (système métrique). Toutes les cotes lues dans l'espace objet sont donc en "
             "centimètres : la cote `803` correspond bien à 8,03 m et la cote `262` à 2,62 m. Le contrôle croisé "
             "avec les cotes annotées des planches PDF (803, 826, 320, 362, 803) confirme cette lecture à ± 1 cm. "
             "Les niveaux altimétriques, eux, sont exprimés en mètres NGF."),
    ("p", "Le point de référence vertical du dessin a été identifié : l'axe « Axe Niveau Rdc Interieur / Point de "
          "Reference » est coté **NGF 41,46** et se situe en Y = −7 234,6 cm dans l'espace objet. Toutes les "
          "altitudes ont été recalculées à partir de cette origine, ce qui a permis de retrouver les cotes NGF "
          "annotées avec une précision de 1 à 2 cm."),

    ("h1", "3. Synthèse géométrique extraite"),
    ("h2", "3.1 Niveaux altimétriques"),
    ("table", T_NIVEAUX),
    ("p", "La lecture croisée des coupes permet de fixer les **hauteurs d'étage** suivantes, qui serviront de base "
          "aux schémas statiques :"),
    ("bullets", [
        "Sous-sol : hauteur sous plafond **1,96 à 2,00 m** — hauteur d'étage (sol à sol) **2,20 m**.",
        "RDC : hauteur sous plafond **2,59 à 2,63 m** — hauteur d'étage **2,86 m**.",
        "R+1 : hauteur sous plafond **2,62 m** — hauteur d'étage **2,82 m**.",
        "Combles : hauteur sous plafond variable de **1,80 à 3,02 m** (pente de rampant à 17 %).",
    ]),
    ("h2", "3.2 Géométrie générale"),
    ("table", T_GEOM),
    ("h2", "3.3 Épaisseurs de murs"),
    ("table", T_MURS),
    ("h2", "3.4 Reprises en sous-œuvre D1 à D6"),
    ("table", T_OUV),
    ("figure", os.path.join(FIG, "fig07_extension_plan.png"),
     "Figure 3 — Extension en façade avant : plan de principe coté (cotes en cm relevées au DXF). "
     "La poutre-acrotère franchit les 8,03 m entre le voile de rive à créer et l'about de la poutre "
     "perpendiculaire ; le poteau BA de 25 cm est à 1,30 m du nu de façade.", 152),
    ("figure", os.path.join(FIG, "fig05_reperage_rdc.png"),
     "Figure 1 — Plan du RDC, état actuel : repérage des six reprises en sous-œuvre D1 à D6 et des portées "
     "libres mesurées. Fond de plan extrait du DXF AARKA ; report des repères par le BET.", 120),
    ("figure", os.path.join(FIG, "fig06_coupe_principe.png"),
     "Figure 2 — Coupe verticale de principe : altimétrie NGF de l'existant et de l'extension, position de la "
     "poutre-acrotère de rive, de la console et du poteau BA à 1,30 m.", 150),
    ("h2", "3.5 Points singuliers identifiés"),
    ("p", "L'analyse met en évidence **quatre points singuliers** qui conditionnent le dimensionnement et le "
          "phasage :"),
    ("bullets", [
        "**D1 — zone non excavée (Coupe 01).** Le mur D1 repose sur une fondation filante continue, sans cave "
        "au-dessous. La démolition doit être arrêtée à l'arase supérieure de cette fondation, et les poteaux BA "
        "ancrés sur une longrine de répartition dimensionnée pour ne pas dépasser 0,10 MPa à l'ELS.",
        "**Nœud D3 / D5 (Coupe 03).** Le croisement des deux ouvertures se situe exactement au droit de l'about du "
        "mur de refend longitudinal central conservé (derrière le futur poêle). Un poteau BA d'about doit y être "
        "encastré pour recevoir les deux profilés. Sa descente de charge rencontre, au sous-sol, la **porte "
        "existante PTE 73** percée dans le mur de refend de la cave (ép. 40 cm) : un renforcement vertical et une "
        "fondation de reprise sont nécessaires de part et d'autre de cette porte.",
        "**Poteau BA noyé dans la verrière.** Sur la planche P08b, l'élément apparaît graphiquement comme un montant "
        "de menuiserie ; la coupe P11b le désigne explicitement comme « POTEAU BÉTON ». Il s'agit d'un poteau "
        "structurel de 25 × 25 cm, situé à **1,30 m du nu de la façade existante** (arbitrage E-02 du "
        "11/11/2026), qui reçoit la console de 0,70 m de la poutre-acrotère perpendiculaire.",
        "**Trappe à linge traversante.** Elle doit être positionnée entre deux solives existantes sur les trois "
        "niveaux (Combles → R+1 → RDC), sans aucun chevêtre. Cela suppose une tolérance d'implantation et un "
        "sondage préalable de l'entraxe réel des solives.",
    ]),

    ("pagebreak",),
    ("h1", "4. Hypothèses de charges"),
    ("p", "Les charges retenues sont celles fixées au cahier des charges, complétées par les valeurs des annexes "
          "nationales françaises des Eurocodes. Le tableau 5 en donne la synthèse ; la décomposition de la charge "
          "de charpente y est explicitée conformément à la demande du maître d'ouvrage."),
    ("table", T_CHARGES),
    ("note", "**Décomposition de la charge de charpente.** La valeur imposée de 250 kg/m² en projection se "
             "décompose en **110 kg/m² permanents** (charpente bois, voliges, liteaux, couverture, écran, "
             "isolation sous rampant) et **140 kg/m² variables** (neige sₖ = 0,45 kN/m² pour la zone A2 avec "
             "μ₁ = 0,8 en projection, soit 36 kg/m², majorée du vent et des effets de versant, soit une enveloppe "
             "de 140 kg/m²). Cette décomposition est indispensable au calcul des flèches ELS, qui ne mobilisent "
             "que la part permanente."),

    ("h1", "5. Hypothèses de matériaux"),
    ("table", T_MAT),

    ("h1", "6. Hypothèses géotechniques"),
    ("p", "En l'absence d'étude géotechnique de mission G2 au stade DCE, les hypothèses suivantes — imposées par "
          "le cahier des charges pour permettre un chiffrage sécuritaire par l'entreprise — sont retenues. Elles "
          "devront impérativement être confirmées par une étude G2 avant exécution ; à défaut, une campagne de "
          "sondages à la pelle mécanique et un essai de plaque seront réalisés en phase préparatoire."),
    ("table", T_GEO),

    ("h1", "7. Critères de vérification"),
    ("p", "L'ensemble des vérifications est mené selon les Eurocodes et leurs annexes nationales françaises, dans "
          "leur version en vigueur à la date du dossier. Les critères retenus sont récapitulés ci-après."),
    ("table", T_CRIT),
    ("note", "**Exigence spécifique aux reprises en sous-œuvre.** La flèche active des profilés métalliques est "
             "limitée à **L/750 et à 5 mm au maximum** sous charges ELS, aussi bien sous les murs maçonnés "
             "conservés qu'au droit des verrières. Cette double limitation, plus sévère que la flèche "
             " réglementaire de L/300, vise à prévenir toute fissuration des maçonneries anciennes et toute mise "
             "en compression des vitrages par déformation des appuis. Pour une portée de 3,80 m (D2), la "
             "limitation dimensionnante est 5 mm (L/750 = 5,07 mm) : c'est donc **5 mm** qui gouverne."),

    ("pagebreak",),
    ("h1", "8. Registre des hypothèses complémentaires retenues par le BET"),
    ("p", "Le tableau ci-après constitue le **registre contractuel** des hypothèses prises par le BET pour pallier "
          "les données manquantes des pièces graphiques. Chaque hypothèse est affectée d'un numéro, d'une "
          "justification et d'une modalité de validation sur site. Les hypothèses non validées à la date de "
          "démarrage des travaux concernés engagent la responsabilité de l'entreprise quant aux conséquences "
          "d'une exécution sur des données erronées."),
    ("table", T_REGISTRE),

    ("pagebreak",),
    ("h1", "9. Écarts et points de vigilance relevés"),
    ("table", T_ECARTS),
    ("h2", "9.1 Conséquences sur les tâches suivantes"),
    ("bullets", [
        "**Écarts E-01 et E-02 (schéma de l'extension)** : **E-01 est caduc** ; il est remplacé par **E-02** "
        "(11/11/2026). Le poteau est implanté à **1,30 m du nu de façade** et la poutre-acrotère de 8,03 m est "
        "**isostatique**, appuyée sur le **voile de rive à créer** et sur l'about d'une **console de 0,70 m**. "
        "La note de calcul de la Tâche 2 et les plans PL-01 à PL-05 sont menés avec ce schéma.",
        "**Écart E-03 (trappe à linge)** : la Tâche 3 (plans généraux) intégrera une zone de tolérance "
        "d'implantation et non une position figée, matérialisée par un nuage de révision.",
        "**Hypothèse H-01** : **levée le 11/11/2026** — fondation de type meulière continue. Le schéma de "
        "longrine de répartition est validé sans élargissement.",
        "**Hypothèses H-08, H-09, H-10, H-14, H-15** : ne conditionnent plus l'établissement de la Tâche 2 "
        "(les valeurs prudentes retenues sont suffisantes) mais restent nécessaires **avant** le démarrage de "
        "la Tâche 4 (plans de détails).",
    ]),

    ("h1", "10. Limites de prestation et réserves"),
    ("bullets", [
        "La présente note ne constitue **pas** une étude géotechnique, ni un diagnostic structurel de l'existant, "
        "ni une étude de pathology. Les désordres éventuels non visibles sur les pièces communiquées ne sont pas "
        "couverts.",
        "Les **charges de la charpente bois** et de la **verrière** sont prises en compte sous forme d'hypothèses "
        "forfaitaires (H-06 et H-18), à actualiser sur réception des notes du charpentier et du verriériste.",
        "Les **plans d'exécution** seront établis à partir du fond de plan DXF communiqué. Ils ne dispensent pas "
        "l'entreprise de procéder au **relevé contradictoire des cotes sur site**, conformément au DTU 21 et aux "
        "clauses du marché.",
        "La **résistance au feu** retenue (REI 30) est une hypothèse (H-19) à confirmer par le bureau de contrôle.",
        "Les valeurs de résistance de la maçonnerie ancienne (H-08) sont des hypothèses prudentes ; les notes de "
        "calcul de la Tâche 2 seront révisées en cas de valeurs d'essais inférieures.",
    ]),

    ("pagebreak",),
    ("h1", "11. Arbitrages du maître d'ouvrage (11 et 12 novembre 2026)"),
    ("p", "À l'issue de la remise de la Tâche 1, le maître d'ouvrage a rendu quatre arbitrages sur les "
          "hypothèses et écarts qui conditionnaient la poursuite de la mission. Ils sont repris ci-dessous et "
          "**se substituent aux hypothèses initialement retenues par le BET** ; le registre du chapitre 8 et le "
          "tableau des écarts du chapitre 9 ont été mis à jour en conséquence. Un **cinquième arbitrage**, rendu "
          "les 11 et 12 novembre 2026, **annule et remplace** la décision E-01 : il redéfinit le schéma structurel de "
          "l'ensemble de l'extension (référence **E-02**)."),
    ("table", {
        "caption": "Tableau — Arbitrages rendus par le maître d'ouvrage et incidences sur les études.",
        "header": ["Réf.", "Objet de l'arbitrage", "Décision du maître d'ouvrage",
                   "Incidences sur les études"],
        "widths": [10, 26, 34, 38],
        "rows": [
            ["**E-01**", "Position du poteau BA de la verrière",
             "**CADUC** — décision annulée par l'arbitrage E-02.",
             "La position à 2,00 m du nu de façade supposait que le poteau serve d'appui d'extrémité à une "
             "poutre de 8,03 m longeant la limite de dalle. Ce schéma est **abandonné** : voir E-02."],
            ["**E-02**", "Schéma structurel de l'extension (révision des 11 et 12/11/2026)",
             "« **Le voile à droite n'est pas existant : il est à créer, sur une semelle filante à créer "
             "également, en limite de propriété, dans le prolongement du mur pignon. Le poteau est à décaler à "
             "l'extrémité gauche des 8,03 m. Ce poteau reçoit une poutre-acrotère perpendiculaire à la façade, "
             "qui s'appuie sur le poteau et continue en console. La poutre-acrotère de 8,03 m est en limite de "
             "dalle, à 2,00 m de la façade ; elle est isostatique et s'appuie sur le nouveau mur à droite et sur "
             "la console à gauche.** » — Précision complémentaire : « **la terrasse fait 2,00 m de largeur "
             "totale, poutre comprise ; le poteau est à 1,30 m de la façade ; le porte-à-faux ne fait donc que "
             "70 cm.** »",
             "Refonte complète de la géométrie : terrasse **8,03 × 2,00 m** (poutre comprise), poutre-acrotère "
             "de rive **isostatique** à 2,00 m du nu de façade, **voile BA de rive à créer** (ép. 20 cm) sur "
             "**semelle filante neuve 65 × 30 cm**, **poteau BA 25 × 25 à 1,30 m** du nu de façade portant une "
             "**poutre perpendiculaire 25 × 67** de 1,30 m prolongée par une **console de 0,70 m**, dalle en "
             "**porte-à-faux de 1,70 m**. Contre-flèche de coffrage de 20 mm sur la poutre de 8,03 m. Incidences "
             "sur DOC-02, DOC-03 et PL-01 à PL-05."],
            ["**H-06**", "Descente de charges de la charpente bois",
             "**Accordé** — l'hypothèse forfaitaire du BET est acceptée.",
             "Les charges de charpente restent celles de la note DOC-01 (250 kg/m² répartis G/Q). Aucune reprise "
             "de calcul n'est nécessaire ; les valeurs seront actualisées sur réception de la note du charpentier."],
            ["**H-18**", "Caractéristiques de la verrière (hors mission)",
             "**Accordé** — l'hypothèse forfaitaire du BET est acceptée.",
             "Les charges d'appui de la verrière (0,60 kN/m² en couverture, 0,45 kN/m² en façade) sont intégrées "
             "telles quelles à la descente de charges de la poutre et du poteau."],
            ["**H-16**", "Position de la trappe à linge",
             "**Estimer la position à partir des plans, puis entourer la trappe d'un nuage sur les plans "
             "d'exécution.**",
             "La trappe est repérée aux trois niveaux (Combles x ≈ 46491, R+1 x ≈ 42890, RDC x ≈ 48491) avec une "
             "ouverture de 30 × 31 cm. Sur PL-01 à PL-03, la trappe sera **entourée d'un nuage de révision** "
             "signalant que la position reste à confirmer par relevé d'entraxe. Aucune solive n'est coupée."],
            ["**H-01**", "Nature de la fondation existante sous D1",
             "**Meulière continue.**",
             "La fondation filante est réputée continue sur toute la longueur du mur. Le schéma de longrine de "
             "répartition est validé sans élargissement ; le contrôle en pied de mur devient un simple contrôle "
             "visuel non bloquant (DOC-03 §4.3 et §4.5)."],
        ],
    }),
    ("note", "**Conséquence sur le déroulé de la mission.** Les arbitrages étant rendus, la **Tâche 2** "
             "(note de calculs et avant-métré) a été engagée sur cette base. Les hypothèses qui restent à lever "
             "par sondage sont : H-08 (résistance de la maçonnerie), H-09 et H-10 (constitution des planchers), "
             "H-14 et H-15 (réseaux enterrés). **Aucune d'entre elles n'est bloquante** pour la note de "
             "calculs ; elles le deviendront pour l'exécution, en particulier H-08 dont dépend la contrainte "
             "admissible sous les semelles filantes existantes (DOC-03 §4.3)."),

    ("h1", "12. Conclusion et validation"),
    ("p", "La géométrie de l'affaire est désormais **entièrement tracée et vérifiée** : les six reprises en "
          "sous-œuvre D1 à D6, l'emprise de l'extension et les niveaux altimétriques sont connus avec une "
          "précision centimétrique. Les hypothèses de charges, de matériaux et de sol sont fixées. Le registre "
          "des 24 hypothèses complémentaires constitue la feuille de route des sondages à réaliser "
          "avant exécution."),
    ("p", "Les **arbitrages du 11 novembre 2026** (chapitre 11) ont levé les points bloquants : le poteau de la "
          "verrière est déplacé à **2,00 m du nu de façade, sous la poutre-acrotère** dont il devient l'appui "
          "d'extrémité, les charges de charpente et de verrière sont acceptées, la trappe est positionnée au "
          "nuage de révision et la fondation sous D1 est confirmée en meulière continue. **La Tâche 2 a été "
          "établie sur cette base** ; la note de calculs DOC-03 en tire toutes les conséquences."),
    ("note", "**Documents du dossier d'exécution** — Tâche 1 : DOC-01 (présent document, note d'hypothèses) et "
             "DOC-02 (note méthodologique d'exécution et de phasage). Tâche 2 : DOC-03 (note de calculs et "
             "avant-métré). Tâche 3 : PL-01 à PL-03 (plans généraux au 1/50). Tâche 4 : PL-04 et PL-05 "
             "(détails de ferraillage et d'assemblages aux 1/20 et 1/10)."),
]


def main():
    outdir = BASE
    docx_path, pdf_path = build(META, BLOCKS, outdir, "DOC-01_Note_Hypotheses")
    print("DOCX :", docx_path)
    print("PDF  :", pdf_path)
    from common_doc import count_pages
    print("Pages PDF :", count_pages(pdf_path))


if __name__ == "__main__":
    main()
