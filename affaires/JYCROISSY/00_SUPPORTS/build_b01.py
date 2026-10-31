#!/usr/bin/env python3
"""JYCROISSY / B-01 — Générateur et validateur de la MPD (CARNAC v3.0.2).

Entrées :
  * data/JYCROISSY/extraction/dictionnaire_carnac.csv (106 variables extraites
    du carnet par extraction_b00.py, colonne consommateurs officielle) ;
  * STATUTS ci-dessous : une proposition de statut par variable, fondée sur
    B-00 Ind B, le pré-RDR (D-01…D-06, PA-01) et les pièces lues.

Sorties :
  * affaires/JYCROISSY/02_PHASE_0_CADRAGE/MPD_jycroissy.csv (machine-readable) ;
  * affaires/JYCROISSY/02_PHASE_0_CADRAGE/B-01_MPD_IndA.md (livrable).

Règles validées (fiche B-01 §2) :
  1. les 106 variables reçoivent exactement un des cinq statuts ;
  2. tout NON NÉCESSAIRE porte un motif de périmètre (jamais la disponibilité) ;
  3. tout BLOQUANTE est rattaché à une brique consommatrice identifiée ;
  4. tout À PRODUIRE PAR GO identifie la brique INTERNE-GO productrice ;
  5. aucune variable BLOQUANTE ne se voit affecter un mode COMPLET.
"""
from __future__ import annotations

import csv
import os
from collections import Counter

DICT_CSV = "data/JYCROISSY/extraction/dictionnaire_carnac.csv"
OUT_CSV = "affaires/JYCROISSY/02_PHASE_0_CADRAGE/MPD_jycroissy.csv"
OUT_MD = "affaires/JYCROISSY/02_PHASE_0_CADRAGE/B-01_MPD_IndB.md"

F, P, G, B, N = "FOURNIE", "PARTIELLE", "À PRODUIRE PAR GO", "BLOQUANTE", "NON NÉCESSAIRE"

# code -> (statut, motif (si N ou G), source ou raison d'absence, mode induit)
STATUTS: dict[str, tuple[str, str, str, str]] = {
    # ---- AC ----
    "AC-01": (F, "", "UNIVI retenu MOA (D-05) ; CCTP P1 p1, cartouches P4", "COMPLET (référence)"),
    "AC-02": (F, "", "Truelle Architectes (S. Iglesias), P3/P4/P1", "COMPLET (référence)"),
    "AC-03": (F, "", "EVEN STRUCTURES, BET structure MOE existant (P2 DIAG, P3 DCE) ; CFG-2 : livraisons PDF sans vecteur coffrage (voir DOC-03)", "COMPLET transcription CFG-2 ; compléments locaux INTERNE-GO (B-20)"),
    "AC-06": (P, "", "Rôle « Bureau de contrôle » aux cartouches P3 mais organisme non nommé dans aucune pièce reçue ; variable de référence, ne suspend aucune brique", "PARTIEL-DÉCLARÉ (demande à émettre)"),
    # ---- CFG ----
    "CFG-01": (F, "", "CFG-2 qualifiée en B-00 Ind B §5", "COMPLET"),
    "CFG-02": (F, "", "Gabarit M validé (D-07) : bâtiment unitaire, emprise < 2 500 m², plus de 5 porteurs, sans JD ni sous-sol Flora", "COMPLET (validé D-07)"),
    "CFG-03": (P, "", "Découpage corrigé (D-13) : bloc unique « Flora », niveaux **PB RDC** (premier bas) / **PH R+1** (plancher haut) / charpente-combles ; la nomenclature architecturale « PH RDC » (P3 f1) = sous-face du plancher haut PH R+1 ; vue unique FONDATIONS + PB RDC acceptable ; statut PARTIELLE, formalisation B-20/B-30", "PARTIEL-DÉCLARÉ ; formalisation B-20/B-30"),
    # ---- CHG ----
    "CHG-01": (P, "", "Usages nommés par pièce (P4 p6, P5 : box kiné, bureaux, plateau technique, salle de sport) ; catégories EC1 non attribuées formellement", "PARTIEL-DÉCLARÉ ; B-21/B-22"),
    "CHG-02": (P, "", "250 daN/m² global officiel (D-03) ; toiture 80 daN/m² (P2 p16) ; ventilation par zone (sanitaires, circulations, stockage) non établie", "PARTIEL-DÉCLARÉ (D-03 au RDR) ; B-21"),
    "CHG-03": (P, "", "Complexes existants A/B documentés et chiffrés (P2 p10-13) ; dallage neuf décrit (P1 p34-36) ; récapitulatif EXE à produire", "PARTIEL-DÉCLARÉ ; B-21"),
    "CHG-04": (P, "", "Charge charpente 150 daN/ml reprise (P2 p16-17) ; complexe de couverture (tuiles/étanchéité) non décrit", "PARTIEL-DÉCLARÉ ; B-21/B-44"),
    "CHG-05": (F, "", "Neige A1, sk 45 daN/m², altitude < 200 m (P3 p1, P1 p13)", "COMPLET"),
    "CHG-06": (F, "", "Vent zone 2, vb 24 m/s, coefficients direction/saison (P3 p1, P1 p13)", "COMPLET"),
    "CHG-07": (F, "", "Séisme zone 1, classe de sol III, classe bâtiment II (P3 p1, P1 p13)", "COMPLET"),
    "CHG-08": (P, "", "Cloisons 7/10/12 cm dessinées (P4 p9, P5) ; équipements lourds et charges ponctuelles non chiffrés", "PARTIEL-DÉCLARÉ ; B-21"),
    # ---- DEC ----
    "DEC-01": (G, "Modes des briques fixés par la MPD validée", "Aucune source projet : produit de la présente MPD", "INTERNE-GO (B-01, suivi B-70)"),
    "DEC-02": (G, "RDR officiel à ouvrir", "Pré-RDR existant (D-01…D-06, PA-01) ; RDR à quatre registres non encore ouvert", "INTERNE-GO (B-03)"),
    "DEC-03": (G, "Registre des verrous à ouvrir", "Aucun verrou formel encore enregistré hors pré-RDR", "INTERNE-GO (B-03/B-04)"),
    "DEC-04": (G, "Suivi des documents supersédés", "Aucun document supersédé à ce jour ; suivi de vie série plus tard", "INTERNE-GO (B-71/B-72)"),
    "DEC-05": (G, "Hypothèses notifiées H-xx à produire", "Aucune H-xx à ce jour (les inconnues sont passées en D-xx/PA-01)", "INTERNE-GO (B-22)"),
    "DEC-06": (P, "", "Délai carnet par défaut 2 jours ouvrés (CARNAC §3) ; délai contractuel réel dans CCAP non reçu", "PARTIEL-DÉCLARÉ"),
    "DEC-07": (P, "", "PA-01 ouvert (contrôle d'arase de fouille, D-06) ; prescriptions ENC complètes à produire au fil des briques", "PARTIEL-DÉCLARÉ ; B-24/B-34/B-40"),
    # ---- DOC ----
    "DOC-01": (F, "", "Inventaire B-00 Ind B (5 pièces de projet + carnet)", "COMPLET"),
    "DOC-02": (P, "", "DXF P5 natif R2018 mais limité à Flora RDC/R+1 (écart C-08) ; les autres planches n'existent qu'en PDF vectoriel P4", "PARTIEL-DÉCLARÉ ; B-30"),
    "DOC-03": (P, "", "Plans BET P3 en PDF seulement, 4 folios, indices hétérogènes C/-/-/B (C-09), sans vecteur coffrage ni notes PRO-DCE", "PARTIEL-DÉCLARÉ ; CFG-2, B-10/B-11/B-20"),
    "DOC-04": (F, "", "CCTP P1, V1 stade PRO, 38 pages, intégralement lu", "COMPLET ; B-10/B-14"),
    "DOC-05": (F, "", "Diagnostic P2 DIAG, 19 pages : 9 désordres, sondages, vérifications EC3/EC5", "COMPLET ; B-11/B-23/B-24"),
    "DOC-06": (P, "", "G2 AVP GEOEXPERTS n° 25.13646/ES/GIF non reçu (volume) ; paramètres clés officialisés par D-06", "PARTIEL-DÉCLARÉ (D-06 au RDR) ; B-12"),
    "DOC-07": (N, "Périmètre : désamiantage et déplombage exclus des livrables CARNAC (§1.4) ; seules les contraintes de phasage/coordination sont remontées", "Rapports amiante (31/12/2024) et plomb cités P1 p14-20 mais non joints ; exclusion de périmètre, pas défaut de disponibilité", "SANS OBJET (confirmé D-08)"),
    "DOC-08": (G, "Récolement/DOE à produire en clôture de mission", "Aucun plan de récolement existant reçu ; P1 p37 exige le DOE avec plans DXF/DWG", "INTERNE-GO (B-72) ; B-11 s'appuie sur P2/P4/P5"),
    "DOC-09": (N, "Périmètre : aucune prédalle ni plancher préfabriqué dans l'opération (dallage coulé en place P1 p35 ; planchers existants conservés/renforcés)", "Fiches techniques sans objet dans le projet", "SANS OBJET (confirmé D-09) ; B-48 SANS OBJET corrélatif"),
    # ---- EXI ----
    "EXI-01": (P, "", "Sections connues des seuls éléments sondés/calculés (P2 : solives 8×18, poutre 20×15, IPE160, IPE330, portiques 23×15/15×15) ; inventaire exhaustif et fondations inconnus", "PARTIEL-DÉCLARÉ ; B-23/B-24"),
    "EXI-02": (F, "", "Neuf désordres D1-D9 localisés et décrits (P2 p5-9)", "COMPLET ; B-23"),
    "EXI-03": (P, "", "Caractéristiques conventionnelles C18/C24 posées par le diag sur critère d'âge, sans essais ; aucune mesure de résistance", "PARTIEL-DÉCLARÉ ; essais ENC/PA si inconnue physique (B-24)"),
    "EXI-04": (P, "", "Campagne de sondages des planchers réalisée (P2 §4) ; aucun sondage de fondations ou de maçonneries porteuses", "PARTIEL-DÉCLARÉ ; B-24"),
    "EXI-05": (G, "Contraintes admissibles transmises à l'existant à établir par nos vérifications", "Non fournie : résulte des calculs B-23/B-46 sur base EXI-03, avec ENC si inconnue physique", "INTERNE-GO (B-23/B-46)"),
    # ---- GEO ----
    "GEO-01": (F, "", "Emprise et contour dans P4/P5, blocs géomètre du DXF", "COMPLET"),
    "GEO-02": (P, "", "Calque 090_repères-axes (9 entités) mais pas de trame structurelle formelle", "PARTIEL-DÉCLARÉ ; B-20/B-30"),
    "GEO-03": (P, "", "Épaisseurs de cloisons 7/10/12 cm (P4 p9, P5) ; épaisseur des murs porteurs non éprouvée partout", "PARTIEL-DÉCLARÉ ; B-20/B-32"),
    "GEO-04": (P, "", "Positions P1/P2/P3 graphiques (P3) et bloc « Murs porteurs selon geometre projet » (P5) ; coordonnées EXE à établir", "PARTIEL-DÉCLARÉ ; B-30"),
    "GEO-05": (F, "", "Baies et menuiseries : nomenclatures P4 p23-25, calque 030_menuiserie P5", "COMPLET"),
    "GEO-06": (P, "", "$INSUNITS = 5 (cm) détecté par script ; confirmation obligatoire au calage", "PARTIEL-DÉCLARÉ ; B-30"),
    "GEO-07": (G, "Transformation de recalage à déterminer", "Non connue avant calage des sources", "INTERNE-GO (B-30)"),
    "GEO-08": (G, "Points de calage ≥ 3 non alignés à identifier", "Aucun point de calage encore posé", "INTERNE-GO (B-30/B-31)"),
    "GEO-09": (F, "", "Échelles aux cartouches 1/500, 1/100, 1/50, 1/50-1/20 (P3/P4)", "COMPLET (référence)"),
    "GEO-10": (G, "Seuils d'épaisseur de présomption porteuse à fixer", "Paramètre méthode d'exploitation vectorielle, non fourni par le client", "INTERNE-GO (B-32)"),
    "GEO-11": (G, "Recouvrement minimal et écart d'axe entre niveaux à fixer", "Paramètre méthode de superposition", "INTERNE-GO (B-32)"),
    "GEO-12": (G, "Seuils géométriques (résidu de calage, superposition) à fixer", "Paramètre méthode de calage", "INTERNE-GO (B-30)"),
    "GEO-13": (G, "Matrice de recalage multi-sources vers le RSU à construire", "RSU non encore créé", "INTERNE-GO (B-30/B-31)"),
    "GEO-14": (P, "", "Trois états EXISTANT/DÉMOLITION/PROJET présents (P4 p4-6 ; blocs R+1 Existant/Projet et calque 102_demol P5) ; différentiel formel non produit", "PARTIEL-DÉCLARÉ ; B-31/B-32"),
    # ---- ID ----
    "ID-01": (F, "", "JYCROISSY ; codes projet 208 / EVEN 24.09.356E / EICP 014-2024-08", "COMPLET"),
    "ID-02": (F, "", "Aménagement d'un cabinet paramédical dans le pavillon Flora", "COMPLET"),
    "ID-03": (F, "", "11 rue Paul Demange, 78290 Croissy-sur-Seine (D-04)", "COMPLET (référence)"),
    "ID-04": (F, "", "Réhabilitation de bâtiment existant, mission EXE/PAC", "COMPLET (référence)"),
    "ID-05": (P, "", "Indices hétérogènes (C-09) : archi Ind C, CCTP V1, DIAG « - », folios BET C/-/-/B ; indice EXE à créer", "PARTIEL-DÉCLARÉ"),
    "ID-06": (F, "", "Pièces au stade DCE/PRO ; mission EXE/PAC (P1 §01.2.1.1.6)", "COMPLET (référence)"),
    "ID-07": (F, "", "Pièces datées 2025-2026 ; étude en cours depuis le 23/10/2026", "COMPLET"),
    # ---- LIV ----
    "LIV-01": (G, "Conventions de calques DXF des livrables à définir", "Aucune convention client reçue ; référence annexe A CARNAC", "INTERNE-GO (B-60)"),
    "LIV-02": (G, "Échelles autorisées des livrables à définir", "À bâtir à partir des échelles des pièces reçues", "INTERNE-GO (B-60)"),
    "LIV-03": (G, "Formats et nommage des fichiers à définir", "DOE en DXF/DWG exigé (P1 p37) mais charte non fournie", "INTERNE-GO (B-60)"),
    "LIV-04": (P, "", "Cartouches Truelle/EVEN existants comme référence ; cartouche EXE entreprise à créer", "PARTIEL-DÉCLARÉ ; B-60"),
    "LIV-05": (F, "", "Langue française, unités SI (cm dans le DXF, daN/m², MPa)", "COMPLET"),
    # ---- MAT ----
    "MAT-01": (F, "", "Bétons C25/30 (structure) et C16/20 (gros béton), P3 p1", "COMPLET"),
    "MAT-02": (F, "", "XC1/XC2/XF1/XC4 (P3 p1) et agressivité sol XA4 (P3, P1 p33)", "COMPLET"),
    "MAT-03": (P, "", "Classe structurale S4 et enrobage nominal 30 mm lisibles de façon fragmentée P3 p1 ; donnée à confirmer", "PARTIEL-DÉCLARÉ ; B-42"),
    "MAT-04": (F, "", "HA S500 (fyk 500 MPa), aciers lisses S220, P3 p1", "COMPLET"),
    "MAT-05": (F, "", "Acier de charpente S275, P3 p1", "COMPLET"),
    "MAT-06": (P, "", "Bois C18 (planchers) et C24 (portiques) : hypothèses du diag P2 sur critère d'âge, sans essais", "PARTIEL-DÉCLARÉ ; B-44"),
    "MAT-07": (P, "", "Natures connues (briques, agglomérés, pierre dure en soubassement) ; résistances non mesurées", "PARTIEL-DÉCLARÉ ; B-46 avec ENC si besoin"),
    "MAT-08": (P, "", "EC5 appliqué par P2 ; classe de service non explicitée (présomption classe 1 en intérieur chauffé)", "PARTIEL-DÉCLARÉ ; B-43/B-44"),
    "MAT-09": (F, "", "Blocs pleins 30/40 B80 et blocs creux 50 B40, P1 p9", "COMPLET"),
    "MAT-10": (P, "", "Mortiers hydrofugé/bâtard/chaux cités ; classe M2,5-M10 non spécifiée", "PARTIEL-DÉCLARÉ ; B-46"),
    "MAT-11": (P, "", "Maçonnerie neuve avec chaînages BA (P1 p23, p36) ; typologie formelle à confirmer au calcul", "PARTIEL-DÉCLARÉ ; B-46"),
    "MAT-12": (P, "", "Maçonnerie existante non sondée, présomption d'absence de chaînage (bâtiment ancien)", "PARTIEL-DÉCLARÉ ; ENC B-24/B-46"),
    # ---- NIV ----
    "NIV-01": (P, "", "TN déclaré variable (P1 p14) ; altimétrie Z ≈ 201 mais niveau TN précis non coté", "PARTIEL-DÉCLARÉ ; B-40"),
    "NIV-02": (P, "", "Z par pièce 201,0-201,3 (RDC) et 203,6-204,4 (R+1) ; table de niveaux formelle non établie", "PARTIEL-DÉCLARÉ ; B-42/B-43"),
    "NIV-03": (F, "", "Hauteurs hsp/hsfp recensées 2,16 à 3,25 m (P4/P5)", "COMPLET"),
    "NIV-04": (P, "", "Assise en alluvions anciennes, ancrage prescrit 50 cm (D-01/D-06) ; niveau réel vérifié en fouille (PA-01)", "PARTIEL-DÉCLARÉ (PA-01) ; B-40"),
    "NIV-05": (P, "", "Fini dallage RDC Z ≈ 201,0 avec pentes et décaissés (P4 p5) ; niveau fini formel à établir", "PARTIEL-DÉCLARÉ ; B-43"),
    "NIV-06": (P, "", "Épaisseurs des planchers A/B connues (P2) ; épaisseur du dallage neuf « selon étude BA » non fixée", "PARTIEL-DÉCLARÉ ; B-43/B-48"),
    "NIV-07": (G, "Table de correspondance Plan Archi N ↔ PB/PH et épaisseurs ASB/Fini à produire", "Nomenclature P3 (PH RDC, PB RDC, Charpente) disponible mais table de correspondance inexistante", "INTERNE-GO (B-02)"),
    # ---- OUT ----
    "OUT-01": (F, "", "Environnement démontré : venv, pypdf 6.21.2, ezdxf 1.4.5, persistance workspace", "COMPLET (référence)"),
    "OUT-02": (F, "", "Scripts versionnés extraction_b00.py et build_b01.py", "COMPLET (référence)"),
    "OUT-03": (F, "", "Journaux journal_B00.md et pré-RDR", "COMPLET (référence)"),
    "OUT-04": (P, "", "Aucun rendu PNG pleine page 300 dpi encore produit ; à venir B-30/B-31", "PARTIEL-DÉCLARÉ"),
    # ---- SEC ----
    "SEC-01": (P, "", "Principe encoffrement (P3), peinture intumescente et vermiculite (P1) ; degrés CF/SF non chiffrés (champs vierges P3 p1) ; dimensionnement de la protection feu exclu CARNAC", "PARTIEL-DÉCLARÉ (mention seule)"),
    "SEC-02": (P, "", "Activité ERP cabinet paramédical ; catégorie et effectif non indiqués", "PARTIEL-DÉCLARÉ (référence)"),
    "SEC-03": (P, "", "Barrière anti-termites prescrite P1 p34 (présomption de zone exposée) ; classement préfectoral non cité ; donnée normative bornable", "PARTIEL-DÉCLARÉ ; H-xx éventuelle B-22"),
    "SEC-04": (P, "", "Classe structurale S4 lisible de façon fragmentée P3 p1 ; à confirmer", "PARTIEL-DÉCLARÉ (référence)"),
    "SEC-05": (F, "", "Sanitaire PMR (P4 p14), rampe (P1 p36), cercles PMR dans le DXF", "COMPLET (référence)"),
    # ---- SIT ----
    "SIT-01": (F, "", "EHPAD en exploitation pendant les travaux (P1, P4 p28)", "COMPLET (référence)"),
    "SIT-02": (F, "", "Base vie dans le Gardien, PGC/PPSPS, constat d'huissier, mitoyenneté (P1 p10-12, P4 p28)", "COMPLET (référence)"),
    "SIT-03": (F, "", "Accès par la rue Paul Demange, plan d'installation P4 p28", "COMPLET (référence)"),
    "SIT-04": (P, "", "Mitoyenneté signalée P1 p10 ; nature précise des mitoyens non détaillée", "PARTIEL-DÉCLARÉ ; B-40"),
    "SIT-05": (P, "", "Fouilles en rigoles selon plans BET ; emprise précise à dessiner", "PARTIEL-DÉCLARÉ ; B-40"),
    # ---- SOL ----
    "SOL-01": (F, "", "qELS ≤ 0,30 MPa, officialisé D-06 (cohérent P3/P1)", "COMPLET (D-06) ; B-40"),
    "SOL-02": (F, "", "qELU ≤ 0,49 MPa, officialisé D-06 (P1 p13)", "COMPLET (D-06) ; B-40"),
    "SOL-03": (F, "", "Ancrage 50 cm dans les alluvions anciennes (D-01/D-06), contrôle d'arase PA-01", "COMPLET (prescrit) + PA-01 ; B-40"),
    "SOL-04": (N, "Périmètre : vérification de l'assise et de la succession des couches déléguée au géotechnicien dans sa mission propre ; notre mission se limite au dimensionnement aux contraintes D-06 et au contrôle en fouille PA-01", "Le G2 complet ne peut être transmis (bug technique signalé par le client) ; paramètres D-06 suffisants pour notre dimensionnement ; D-12", "SANS OBJET (périmètre)"),
    "SOL-05": (F, "", "Agressivité XA4, géotextile anti-contaminant (P3 p1/p4, P1 p33)", "COMPLET ; B-40/B-43"),
    "SOL-06": (N, "Périmètre : absence de nappe phréatique confirmée par le client — pas de drainage/hydrologie à dimensionner", "Absence de nappe phréatique (CR utilisateur) ; D-12", "SANS OBJET (périmètre)"),
    "SOL-07": (N, "Périmètre : calcul de tassement délégué au géotechnicien dans sa mission propre ; notre dimensionnement porte sur les contraintes seules", "Sans calcul de tassement (CR utilisateur) ; D-12", "SANS OBJET (périmètre)"),
    "SOL-08": (P, "", "G2 AVP existant chez le client mais non reçu ; G3 absent (commande éventuelle hors production CARNAC, exclusion G1-G3)", "PARTIEL-DÉCLARÉ ; B-12"),
    # ---- STR ----
    "STR-01": (P, "", "Éléments Stab1 (entretoises anti-dévers IPE) repérés P3 ; contreventement global et centre de torsion non synthétisés", "PARTIEL-DÉCLARÉ ; B-25"),
    "STR-02": (N, "Périmètre : pas de sous-sol ni d'écran de soutènement — notre périmètre se limite au bâtiment Flora (Gardien/Bagatelle hors périmètre structure CARNAC ; C-07 tranchée par D-10)", "Aucun ouvrage de soutènement décrit dans les pièces Flora ; périmètre Flora uniquement confirmé", "SANS OBJET (confirmé D-10)"),
    "STR-03": (P, "", "Percements et réservations dispersés (P1 p23-24, calque 080_plomb-cvc P5) ; carnet consolidé tous corps d'état inexistant", "PARTIEL-DÉCLARÉ ; B-34"),
}

FAMILLE = {
    "AC": "Acteurs", "CFG": "Configuration", "CHG": "Charges", "DEC": "Décision/pilotage",
    "DOC": "Documents", "EXI": "Existant", "GEO": "Géométrie", "ID": "Identité",
    "LIV": "Livrables", "MAT": "Matériaux", "NIV": "Niveaux", "OUT": "Outillage",
    "SEC": "Sécurité/incendie", "SIT": "Site", "SOL": "Sol/géotechnique", "STR": "Structure",
}


def main() -> None:
    with open(DICT_CSV, newline="", encoding="utf-8") as fh:
        dictionnaire = {row["code"]: row for row in csv.DictReader(fh)}
    assert len(dictionnaire) == 106, f"dictionnaire inattendu : {len(dictionnaire)}"

    manquants = sorted(set(dictionnaire) - set(STATUTS))
    en_trop = sorted(set(STATUTS) - set(dictionnaire))
    assert not manquants, f"variables sans statut : {manquants}"
    assert not en_trop, f"statuts inconnus : {en_trop}"

    # Validations des règles de la fiche B-01
    for code, (statut, motif, source, mode) in STATUTS.items():
        if statut == N:
            assert motif and "Périmètre" in motif, f"{code}: NON NÉCESSAIRE sans motif de périmètre"
            assert mode.startswith("SANS OBJET"), f"{code}: mode incohérent"
        if statut == B:
            assert "B-" in dictionnaire[code]["consommateurs"], f"{code}: BLOQUANTE sans brique identifiée"
            assert "COMPLET" not in mode, f"{code}: COMPLET interdit sur BLOQUANTE"
        if statut == G:
            assert "INTERNE-GO" in mode, f"{code}: À PRODUIRE sans brique INTERNE-GO"
        assert statut in (F, P, G, B, N), f"{code}: statut illégal"

    lignes = []
    for code in sorted(dictionnaire, key=lambda c: (c.split("-")[0], int(c.split("-")[1]))):
        statut, motif, source, mode = STATUTS[code]
        lignes.append({
            "famille": FAMILLE[code.split("-")[0]], "code": code,
            "libelle": dictionnaire[code]["libelle"], "statut": statut,
            "motif": motif, "source": source,
            "consommateurs": dictionnaire[code]["consommateurs"], "mode": mode,
        })

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Famille", "Code", "Libellé", "Statut", "Motif", "Source/raison d'absence",
                    "Briques consommatrices", "Mode induit"])
        for r in lignes:
            w.writerow([r["famille"], r["code"], r["libelle"], r["statut"], r["motif"],
                        r["source"], r["consommateurs"], r["mode"]])

    compte = Counter(r["statut"] for r in lignes)
    print("MPD écrite :", OUT_CSV)
    print("Décompte :", dict(compte), "| total =", sum(compte.values()))

    # ---- Rendu Markdown ----
    md = []
    md.append("# B-01 — MATRICE DE PÉRIMÈTRE ET DE DISPONIBILITÉ (MPD) — JYCROISSY\n")
    md.append("| Champ | Valeur |")
    md.append("|---|---|")
    md.append("| Opération | JYCROISSY — Aménagement d'un cabinet paramédical, pavillon Flora, EHPAD La Roseraie, 11 rue Paul Demange, Croissy-sur-Seine (D-04) |")
    md.append("| Carnet | CARNAC v3.0.2 — fiche `02_PHASE_0_CADRAGE/B-01_MPD.md` |")
    md.append("| Indice | **Ind B — 2026-10-23** (intégration des décisions D-07 à D-13 : gabarit M validé, NON NÉCESSAIRE confirmés, géotechnique D-12, nomenclature CFG-03 corrigée) |")
    md.append("| Entrées | B-00 Ind B, pré-RDR (D-01…D-13, PA-01), dictionnaire des 106 variables |")
    md.append("| CFG-01 | **CFG-2** (BET structure MOE en PDF, sans vecteur coffrage) — repris de B-00 |")
    md.append("| CFG-02 | **Gabarit M** — **validé (D-07)** : bâtiment unitaire, emprise très inférieure à 2 500 m², plus de cinq porteurs (P1/P2/P3, F1-F4, R1-R3, sommiers), sans joint de dilatation ni sous-sol pour Flora ; voie standard en six phases |")
    md.append("| CFG-03 | Un bloc structurel unique « Flora », sans JD ; niveaux **corrigés (D-13)** : fondations/soubassements → **PB RDC** (premier bas) → **PH R+1** (plancher haut) → charpente/combles. Nomenclature architecturale « PH RDC » (P3 f1) = sous-face du plancher haut PH R+1. **Vue unique « FONDATIONS + PB RDC »** acceptable. Statut PARTIELLE, formalisation en B-20/B-30 |")
    md.append("| Statut des propositions | **Tu PROPOSES, je VALIDE** : Ind B — les décisions D-07 à D-13 sont consignées au pré-RDR ; les 6 NON NÉCESSAIRE sont tranchées (§2.3) |\n")
    md.append("> Règles tenues : jamais de NON NÉCESSAIRE justifié par une indisponibilité (motif de périmètre obligatoire) ; aucun mode COMPLET sur variable BLOQUANTE ; aucune valeur de repli ; chaque ligne cite sa source ou sa raison d'absence. Machine-readable : `MPD_jycroissy.csv` ; générateur/validateur : `../00_SUPPORTS/build_b01.py`.\n")
    md.append("---\n")
    md.append("## 1. MATRICE COMPLÈTE (106 variables, 8 colonnes)\n")
    famille_courante = None
    for r in lignes:
        if r["famille"] != famille_courante:
            famille_courante = r["famille"]
            md.append(f"\n### Famille {famille_courante}\n")
            md.append("| Code | Libellé | Statut | Motif (si NON NÉCESSAIRE / À PRODUIRE) | Source ou raison d'absence | Briques consommatrices | Mode induit |")
            md.append("|---|---|---|---|---|---|---|")
        md.append("| {code} | {libelle} | **{statut}** | {motif} | {source} | {cons} | {mode} |".format(
            code=r["code"], libelle=r["libelle"], statut=r["statut"], motif=r["motif"] or "—",
            source=r["source"], cons=r["consommateurs"], mode=r["mode"]))
    md.append("\n---\n")
    md.append("## 2. SYNTHÈSE RÉGLEMENTAIRE (trois paragraphes)\n")
    bloq = [r for r in lignes if r["statut"] == B]
    md.append("### 2.1 Variables BLOQUANTES et briques suspendues")
    md.append(f"**{len(bloq)} variable bloquante à ce stade** (levée par D-12 : le G2 complet n'est pas transmissible, mais la mission se limite au dimensionnement aux contraintes D-06, le tassement et l'assise sont délégués au géotechnicien dans sa mission propre, et l'absence de nappe phréatique est confirmée) :\n")
    for r in bloq:
        md.append(f"- **{r['code']} — {r['libelle']}** : {r['source']} Briques impactées : {r['consommateurs']}. Mode : {r['mode']}.")
    md.append("\nConséquences (D-12, D-11) : **B-12** exécutable en PARTIEL-DÉCLARÉ (paramètres D-06, tassement/assise délégués au géotechnicien) ; **B-40 (fondations superficielles)** **non bloquante** — dimensionnement aux contraintes + contrôle en fouille **PA-01** ; **B-41 (fondations profondes)** **SANS OBJET confirmé (D-11)** — aucune fondation profonde dans aucune pièce.\n")
    prod = [r for r in lignes if r["statut"] == G]
    md.append(f"### 2.2 Variables À PRODUIRE PAR GO ({len(prod)}) et briques INTERNE-GO")
    for r in prod:
        md.append(f"- **{r['code']} — {r['libelle']}** : {r['motif']} → {r['mode']}.")
    md.append("\nPour mémoire (CFG-2) : AC-03 reste FOURNIE (le BET MOE existe) ; l'INTERNE-GO ne porte que sur les ouvrages non conçus par le BET et sur les productions d'exécution, en aucun cas sur une réclamation de DXF de coffrage MOE, interdite par la configuration.\n")
    nn = [r for r in lignes if r["statut"] == N]
    md.append(f"### 2.3 Variables NON NÉCESSAIRE ({len(nn)}) — **toutes tranchées par décision (D-08, D-09, D-10, D-12)**")
    md.append("Chaque ligne porte un motif de périmètre (jamais une indisponibilité) et a reçu une décision explicite de votre part. Aucune n'est en attente de validation.\n")
    for r in nn:
        md.append(f"- [x] **{r['code']} — {r['libelle']}** : {r['motif']}. Effet : {r['mode']}.")
    md.append("\nCorrélats briques : **B-48 (prédalles) SANS OBJET** (DOC-09, D-09) ; **B-41 (fondations profondes) SANS OBJET** (D-11) ; **B-40** non bloquante (SOL-04/06/07, D-12) ; périmètre = **bâtiment Flora uniquement** (STR-02, D-10 ; C-07 tranchée).\n")
    md.append("---\n")
    md.append("## 3. DÉCISIONS PRISES ET PORTE SUIVANTE\n")
    md.append("**Décisions prises dans ce message (consignées D-07 à D-13 au pré-RDR) :** gabarit **M** validée (D-07) ; NON NÉCESSAIRE confirmés DOC-07 (D-08), DOC-09 (D-09, B-48 SANS OBJET), STR-02 (D-10, périmètre Flora uniquement, C-07 tranchée) ; B-41 SANS OBJET (D-11) ; géotechnique D-12 (G2 non transmissible, dimensionnement contraintes, tassement délégué, absence nappe → SOL-04/06/07 NON NÉCESSAIRE) ; nomenclature CFG-03 corrigée (D-13, PB RDC / PH R+1).\n")
    md.append("**Porte suivante :** un **GO B-02** explicite déclenche la Fiche de Données de Conception (table NIV-07 avec la correspondance PB/PH corrigée). Toute nouvelle correction relance B-01 en indice incrémenté, sans avancer sur B-02.\n")
    md.append("## 4. CRITÈRE D'ACCEPTATION — AUTO-CONTRÔLE\n")
    md.append("| Critère de la fiche | Statut |")
    md.append("|---|---|")
    md.append("| Toute variable lue par une brique activée figure (106/106) | ✅ validé par build_b01.py |")
    md.append("| Tout NON NÉCESSAIRE porte un motif de périmètre | ✅ les 6 lignes sont motivées (périmètre, pas disponibilité) |")
    md.append("| Tout BLOQUANTE rattaché à une brique identifiée | ✅ **0 BLOQUANTE** à ce stade (levées par D-12) |")
    md.append("| Tout À PRODUIRE PAR GO identifie la brique INTERNE-GO | ✅ contrôlé par script |")
    md.append("| Aucune décision SANS OBJET sans validation explicite | ✅ toutes tranchées §2.3 (D-08 à D-12) |")
    md.append("| Aucun mode COMPLET sur variable BLOQUANTE | ✅ contrôlé par script |")
    md.append("| Zéro placeholder (V7) | ✅ |\n")
    md.append("**Brique B-01 re-livrée en Ind B (intégration des décisions D-07 à D-13) — en attente de votre GO.** Un **GO B-02** explicite déclenchera la Fiche de Données de Conception (table NIV-07 avec correspondance PB/PH corrigée) ; la MPD validée sera annexée au RDR (B-03) comme décision D-xx datée.")
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    print("Livrable écrit :", OUT_MD)


if __name__ == "__main__":
    main()
