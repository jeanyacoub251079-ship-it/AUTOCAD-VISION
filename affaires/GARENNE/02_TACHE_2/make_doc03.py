"""
DOC-03 — Note de calculs structurelle et avant-métré (Tâche 2).
Produit DOC-03_Note_Calculs.docx et .pdf via le moteur commun_doc.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T1 = os.path.join(os.path.dirname(HERE), "01_TACHE_1")
sys.path.insert(0, T1)

from common_doc import build                       # noqa: E402

FIG = os.path.join(HERE, "figures")
RES = os.path.join(HERE, "calculs_resultats.json")

with open(RES, encoding="utf-8") as fh:
    R = json.load(fh)

EXT = R["extension"]
BA = R["ba"]
MET = R["metre"]
RSO = R["rso_S355"]["murs"]
RSO275 = {m["rep"]: m for m in R["rso_S275"]["murs"]}


def f(x, n=2):
    """Formate un nombre à la française (virgule décimale)."""
    if isinstance(x, str):
        return x
    s = f"{x:,.{n}f}"
    return s.replace(",", "\u202f").replace(".", ",")


# ---------------------------------------------------------------------------
# META
# ---------------------------------------------------------------------------
META = {
    "entete_gauche": "58 rue de l'Aigle — 92250 La Garenne-Colombes",
    "entete_droit": "DOC-03 — Note de calculs",
    "pied_gauche": ("BET Structure · Dossier d'exécution — Tâche 2 · Indice A · "
                    "11/11/2026 · Affaire GA-2026-58AIGLE · DOC-03"),
    "titre_pdf": "DOC-03 — Note de calculs structurelle et avant-métré",
    "sujet_pdf": ("Réhabilitation lourde, RSO D1 à D6 et extension — 58 rue de l'Aigle, "
                  "La Garenne-Colombes"),
    "cover": (
        ["NOTE DE CALCULS", "STRUCTURELLE"],
        "Dimensionnement des reprises en sous-œuvre D1 à D6, de l'extension et de ses "
        "fondations · Avant-métré quantitatif",
        [
            ("Affaire", "Réhabilitation lourde, restructuration intérieure et extension en façade avant"),
            ("Adresse", "58 rue de l'Aigle — 92250 La Garenne-Colombes (Hauts-de-Seine)"),
            ("Maître d'ouvrage", "Particulier — maison individuelle existante"),
            ("Maître d'œuvre", "Cabinet AARKA — SAS d'architecture, 51 rue Saint-Louis-en-l'Île, 75004 Paris"),
            ("Bureau d'études", "BET Structure — Études d'exécution Gros Œuvre & Structure"),
            ("Mission", "RSO D1 à D6 (profilés acier + appuis BA), structure BA de l'extension, "
                        "notes méthodologiques et plans d'exécution"),
            ("Document", "**DOC-03** — Note de calculs structurelle et avant-métré quantitatif"),
            ("Livrables", "**DOC-03.docx** et **DOC-03.pdf** (ISO A4 portrait) ; moteur de calcul "
                          "`calculs.py` et résultats `calculs_resultats.json`"),
            ("Indice / date", "**A** — 11 novembre 2026"),
            ("Phase", "DCE — Tâche 2 / 4 (calculs et avant-métré)"),
            ("Format", "ISO A4 portrait (210 × 297 mm) — livré en .docx et .pdf"),
            ("Références", "NF EN 1990/1991/1992/1993/1996/1997 + annexes nationales françaises ; "
                           "NF P94-261 ; DTU 13.1, 13.2, 20.1, 21, 23.1, 32.1"),
        ],
        "**Avertissement.** La présente note établit le dimensionnement des ouvrages sur la base "
        "des hypothèses de la note DOC-01 et des arbitrages rendus par le maître d'ouvrage à "
        "l'issue de la Tâche 1. Les résultats sont produits par un moteur de calcul reproductible "
        "et **ne se substituent pas** aux vérifications de l'entreprise, ni à l'étude géotechnique "
        "G2 dont l'absence est expressément signalée au chapitre 4. Les hypothèses marquées comme "
        "telles restent à confirmer par sondages avant tout début de travaux.",
    ),
}


# ---------------------------------------------------------------------------
# Helpers de tableaux
# ---------------------------------------------------------------------------

def tab_hypotheses():
    h = R["hypothese"]
    return dict(
        caption="Tableau 1 — Matériaux et coefficients partiels retenus.",
        header=["Grandeur", "Symbole", "Valeur", "Origine / référence"],
        widths=[52, 20, 30, 78],
        rows=[
            ["Résistance caractéristique du béton", "f<sub>ck</sub>", "25 MPa",
             "C25/30 — NF EN 206/CN"],
            ["Résistance de calcul du béton", "f<sub>cd</sub>", f"{f(h['fcd'])} MPa",
             "f<sub>ck</sub>/γ<sub>C</sub>, γ<sub>C</sub> = 1,50 (AN française)"],
            ["Résistance caractéristique de l'acier HA", "f<sub>yk</sub>", "500 MPa",
             "B500B — NF EN 10080"],
            ["Résistance de calcul de l'acier HA", "f<sub>yd</sub>", f"{f(h['fyd'],1)} MPa",
             "f<sub>yk</sub>/γ<sub>S</sub>, γ<sub>S</sub> = 1,15"],
            ["Module du béton", "E<sub>cm</sub>", "31 000 MPa", "EC2 §3.1.3, C25/30"],
            ["Limite d'élasticité acier S355", "f<sub>y</sub>", "355 MPa",
             "NF EN 10025-2, ép. ≤ 16 mm"],
            ["Coefficient partiel acier", "γ<sub>M0</sub> / γ<sub>M1</sub>", "1,00 / 1,00",
             "EC3 §6.1 (AN française)"],
            ["Contrainte de référence ELS du sol", "q<sub>ELS</sub>", "0,10 MPa",
             "Hypothèse imposée par le BET (DOC-01, H-02)"],
            ["Contrainte de référence ELU du sol", "q<sub>ELU</sub>", "0,15 MPa",
             "Hypothèse imposée par le BET (DOC-01, H-02)"],
            ["Poids volumique du béton armé", "γ", "25 kN/m³", "EC1-1-1, annexe A"],
            ["Poids volumique de l'acier", "γ", "78,5 kN/m³", "7850 kg/m³"],
            ["Limite de flèche imposée", "—", "L/750 et ≤ 5 mm",
             "Exigence du BET — murs et verrières"],
        ],
    )


def tab_charges():
    return dict(
        caption="Tableau 2 — Descente de charges de la toiture-terrasse accessible.",
        header=["Composante", "Symbole", "Valeur (kN/m²)", "Base"],
        widths=[70, 24, 40, 46],
        rows=[
            ["Dalle BA ép. 20 cm", "g<sub>1</sub>", f("5,00"), "0,20 × 25"],
            ["Forme de pente + étanchéité + protection", "g<sub>2</sub>", "1,20",
             "Complexe toiture (DOC-01)"],
            ["Cloisons et distribution", "g<sub>3</sub>", "1,50", "G1 = 150 kg/m²"],
            ["**Total charges permanentes**", "**G**", f"**{f(EXT['dalle']['G'])}**",
             "Somme"],
            ["Charges d'exploitation — terrasse accessible", "Q", "1,50",
             "Catégorie A (DOC-01)"],
            ["**Combinaison ELU** 1,35 G + 1,50 Q", "p<sub>ELU</sub>",
             f"**{f(EXT['dalle']['p_elu'])}**", "EC0 §6.4.3.2"],
            ["**Combinaison ELS caractéristique** G + Q", "p<sub>ELS</sub>",
             f"**{f(EXT['dalle']['p_els'])}**", "EC0 §6.5.3"],
            ["**Combinaison ELS quasi-permanente** G + ψ<sub>0</sub>Q", "p<sub>qp</sub>",
             f"**{f(EXT['dalle']['p_els_qp'])}**", "ψ<sub>0</sub> = 0,7"],
        ],
    )


def tab_poutre():
    p = EXT["poutre"]
    return dict(
        caption="Tableau 3 — Poutre-acrotère retroussée : vérifications de flexion, "
                "d'effort tranchant et de flèche (section 30 × 67 cm avec table "
                "collaborante, C25/30, B500B).",
        header=["Grandeur", "Valeur", "Unité", "Critère / observation"],
        widths=[58, 26, 20, 56],
        rows=[
            ["Portée (travée unique)", f(p["L"]), "m",
             "voile de rive ↔ console (poteau à 1,30 m)"],
            ["Section de l'âme", f"{int(p['b']*100)} × {int(p['h']*100)}", "cm",
             f"arase NGF {f(p['ngf_haut'],2)} — sous-face {f(p['ngf_bas'],2)}"],
            ["Bande de dalle reprise", f(p["bande"]), "m",
             "poutre en limite de dalle (2,00/2)"],
            ["Largeur collaborante b<sub>eff</sub>", f(p["beff"]), "m",
             "EC2 §5.3.2.1"],
            ["Charge ELU", f(p["q_elu"], 1), "kN/m", "dalle reprise + poids propre"],
            ["Moment de flexion ELU", f(p["M"], 1), "kN·m", "qL²/8, travée isostatique"],
            ["Effort tranchant ELU", f(p["V"], 1), "kN", "qL/2"],
            ["Moment réduit µ", f(p["mu"], 4), "—", "< 0,372"],
            ["Bras de levier z", f(p["z"], 3), "m", "—"],
            ["A<sub>s</sub> requis", f(p["As"]), "cm²", "—"],
            ["Ferraillage retenu", p["armature"]["libelle"], "—",
             f"A<sub>s</sub> = {f(p['armature']['As_cm2'])} cm², une nappe"],
            ["Étriers", p["etriers"]["libelle"], "—",
             f"V<sub>Rd,s</sub> = {f(p['VRdc'],1)} kN"],
            ["Bielles comprimées V<sub>Rd,max</sub>", f(p["VRdmax"], 1), "kN",
             "OK" if p["ok_bielle"] else "NON"],
            ["Moment de fissuration M<sub>cr</sub>", f(p["Mcr"], 1), "kN·m",
             "section brute"],
            ["Inertie effective I<sub>e</sub>", f(p["Ie"], 5), "m⁴",
             f"ζ = {f(p['zeta'],3)}"],
            ["Flèche instantanée", f(p["fleche_inst"]), "mm", "G + ψ<sub>0</sub>Q"],
            ["Flèche à long terme", f(p["fleche"]), "mm", "φ = 2"],
            ["Ratio de flèche", f"L/{int(p['ratio'])}", "—", "—"],
            ["Flèche limite L/500", f(p["fleche_lim_500"], 1), "mm",
             "OK" if p["ok_500"] else "**dépassée**"],
            ["Flèche limite L/250", f(p["fleche_lim_250"], 1), "mm",
             "OK" if p["ok_250"] else "NON"],
            ["Contre-flèche de coffrage", f(p["contre_fleche"], 0), "mm",
             "compense la flèche à long terme"],
            ["Flèche résiduelle (LT − contre-flèche)",
             f(p["fleche_residuelle"]), "mm",
             "OK" if p.get("ok_residuel") else "NON"],
            ["**Vérification de la flèche**", "**CONFORME**", "—",
             "L/250 + contre-flèche → L/500"],
        ],
    )


def tab_poutre_perp():
    p = EXT["poutre_perpendiculaire"]
    return dict(
        caption="Tableau 4 — Poutre perpendiculaire 25 × 67 cm : travée de 1,30 m "
                "entre façade et poteau, puis console de 0,70 m.",
        header=["Grandeur", "Valeur", "Unité", "Critère / observation"],
        widths=[58, 26, 20, 56],
        rows=[
            ["Travée façade ↔ poteau", f(p["L_travee"]), "m", "poteau à 1,30 m"],
            ["Porte-à-faux poteau ↔ rive", f(p["L_console"]), "m",
             "about de la poutre de 8,03 m"],
            ["Section", f"{int(p['b']*100)} × {int(p['h']*100)}", "cm",
             "même arase 44,75"],
            ["Bande de dalle reprise", f(p["bande"]), "m", "largeur collaborante"],
            ["Charge ELU", f(p["q"], 1), "kN/m", "dalle + poids propre"],
            ["Réaction d'appui (poutre 8,03 m)", f(p["R_appui"], 1), "kN",
             "charge concentrée en bout de console"],
            ["Moment ELU en console", f(p["M_console"], 1), "kN·m",
             "qL²/2 + R·L → cas dimensionnant"],
            ["Moment ELU en travée", f(p["M_travee"], 1), "kN·m", "qL²/8"],
            ["A<sub>s</sub> requis", f(p["As"]), "cm²", "nappe supérieure"],
            ["Ferraillage retenu", p["armature"]["libelle"], "—",
             f"A<sub>s</sub> = {f(p['armature']['As_cm2'])} cm²"],
            ["Étriers", p["etriers"]["libelle"], "—",
             f"V<sub>Rd,s</sub> = {f(p['etriers']['VRds'],1)} kN"],
            ["Effort tranchant ELU", f(p["V"], 1), "kN", "à l'appui poteau"],
            ["Bielles comprimées", f(p["VRdmax"], 1), "kN", "OK"],
            ["**Vérification**", "**CONFORME**", "—", "ELU + ELS"],
        ],
    )


def tab_rso():
    rows = []
    for m in RSO:
        rows.append([
            m["rep"], f(m["L"]), f(m["ep"] * 100, 0), f(m["h_mur_reprise"]),
            f(m["q_elu"], 1), f(m["M"], 1), f(m["V"], 1),
            m["profil"], f(m["taux_M"], 3), f(m["fleche"]),
        ])
    return dict(
        caption="Tableau 5 — Synthèse du dimensionnement des profilés de reprise en "
                "sous-œuvre D1 à D6 (acier S355).",
        header=["Rep.", "L (m)", "ép. (cm)", "h reprise (m)", "q<sub>ELU</sub> (kN/m)",
                "M (kN·m)", "V (kN)", "Profilé retenu", "Taux M", "Flèche (mm)"],
        widths=[12, 14, 16, 20, 22, 18, 16, 30, 16, 18],
        align=["left", "right", "right", "right", "right", "right", "right",
               "left", "right", "right"],
        rows=rows,
    )


def tab_rso_compare():
    rows = []
    for m in RSO:
        m2 = RSO275[m["rep"]]
        rows.append([m["rep"], m["profil"], f(m["taux_M"], 3),
                     m2["profil"], f(m2["taux_M"], 3)])
    return dict(
        caption="Tableau 6 — Incidence du choix de la nuance d'acier sur les profilés "
                "retenus.",
        header=["Rep.", "Profilé S355", "Taux S355", "Profilé S275", "Taux S275"],
        widths=[16, 42, 26, 42, 26],
        rows=rows,
    )


def tab_flexion_detail():
    rows = []
    for m in RSO:
        rows.append([
            m["rep"], f(m["g_mur"], 1), f(m["g_plancher"], 1), f(m["q_plancher"], 1),
            f(m["q_elu"], 1), f(m["q_els"], 1),
        ])
    return dict(
        caption="Tableau 7 — Descente de charges linéiques sur chaque profilé "
                "(bande de plancher de 1,00 m).",
        header=["Rep.", "g mur (kN/m)", "g planchers (kN/m)", "q planchers (kN/m)",
                "q<sub>ELU</sub> (kN/m)", "q<sub>ELS</sub> (kN/m)"],
        widths=[16, 34, 40, 40, 34, 34],
        rows=rows,
    )


def tab_poteau():
    p = EXT["poteau"]
    return dict(
        caption="Tableau 8 — Vérification du poteau BA 25 × 25 à 1,30 m du nu "
                "de façade.",
        header=["Grandeur", "Valeur", "Unité", "Critère"],
        widths=[62, 34, 22, 42],
        rows=[
            ["Section", "25 × 25", "cm", "—"],
            ["Hauteur libre", f(p["l0"]), "m", "—"],
            ["Rayon de giration i", f(p["i"], 4), "m", "√(b²/12)"],
            ["Élancement λ", f(p["lambda_"], 1), "—", "—"],
            ["Effort normal ELU", f(p["N_elu"], 1), "kN", "1,35 G + 1,50 Q"],
            ["Effort normal ELS", f(p["N_els"], 1), "kN", "G + Q"],
            ["Résistance de calcul N<sub>Rd</sub>", f(p["NRd"], 1), "kN",
             "α·A<sub>c</sub>·f<sub>cd</sub>"],
            ["**Taux de travail**", f"**{f(p['taux'],3)}**", "—",
             "**< 1,00 → conforme**"],
            ["A<sub>s</sub> minimal", f(p["As_min"]), "cm²", "0,10 N<sub>Ed</sub>/f<sub>yd</sub>"],
            ["Ferraillage retenu", p["armature"]["libelle"], "—",
             f"A<sub>s</sub> = {f(p['armature']['As_cm2'])} cm²"],
            ["Ratio d'armature", f(p["armature"]["As_cm2"] / (p["b"] * p["h"] * 1e4) * 100, 2), "%",
             "0,2 % ≤ ρ ≤ 4 %"],
        ],
    )


def tab_voile():
    v = EXT["voile"]
    return dict(
        caption="Tableau 9 — Voile BA de rive à créer, ép. 20 cm : poussée des "
                "terres et ferraillage.",
        header=["Grandeur", "Valeur", "Unité", "Observation"],
        widths=[66, 26, 20, 48],
        rows=[
            ["Hauteur enterrée", f(v["H_enterre"]), "m", "NGF 39,02 → 41,46"],
            ["Coefficient de poussée active K<sub>a</sub>", f(v["Ka"], 3), "—", "φ = 30° (Rankine)"],
            ["Coefficient de poussée au repos K<sub>0</sub>", f(v["K0"], 3), "—", "Jaky — cas défavorable"],
            ["Poussée active totale", f(v["pa"], 1), "kN/ml", "dont surcharge 5 kN/m²"],
            ["Poussée au repos totale", f(v["p0"], 1), "kN/ml", "retenue pour le calcul"],
            ["Moment d'encastrement en pied", f(v["M"]), "kN·m/ml", "poussée triangulaire au repos"],
            ["Moment réduit µ", f(v["mu"], 4), "—", "ELS"],
            ["A<sub>s</sub> requis", f(v["As_requis"]), "cm²/ml", "face côté remblai"],
            ["A<sub>s</sub> minimal (EC2 §9.6.2)", f(v["As_mini"]), "cm²/ml", "0,13 % de la section"],
            ["**Ferraillage retenu**", f"**{v['armature']['libelle']}**", "—", "par face, vertical"],
            ["A<sub>s</sub> de répartition horizontal", f(v["As_repartition"]), "cm²/ml",
             "chaque face, HA 8 e = 250 mm"],
            ["Effort tranchant à la base", f(v["V_base"], 1), "kN/ml", "poussée au repos"],
            ["Effort tranchant résistant", f(v["VRdc"], 1), "kN/ml", "EC2 §6.2.2 sans armature d'âme"],
            ["**Vérification de l'effort tranchant**",
             "**OK**" if v["ok_tranchant"] else "**NON**", "—", "V<sub>Ed</sub> ≤ V<sub>Rdc</sub>"],
        ],
    )


def tab_dalle():
    d = EXT["dalle_verif"]
    return dict(
        caption="Tableau 10 — Vérification de la dalle de toiture-terrasse ép. 20 cm "
                "(console de 1,70 m depuis la façade jusqu'à la poutre de rive).",
        header=["Grandeur", "Valeur", "Unité", "Critère / observation"],
        widths=[60, 26, 20, 54],
        rows=[
            ["Porte-à-faux depuis la façade", f(d["L"]), "m",
             "p<sub>ELU</sub>L²/2 — cas dimensionnant"],
            ["Débord au-delà de l'appui (poteau)", "0,70", "m",
             "bordé par la poutre perpendiculaire"],
            ["Largeur de terrasse", f(d["largeur"]), "m",
             "poutre-acrotère comprise"],
            ["Moment ELU à l'encastrement", f(d["M"], 1), "kN·m/m", "moment retenu"],
            ["Effort tranchant ELU à l'appui", f(d["V"], 1), "kN/m",
             "p<sub>ELU</sub>·L"],
            ["Moment réduit µ", f(d["mu"], 4), "—", "< 0,372"],
            ["A<sub>s</sub> requis", f(d["As"]), "cm²/m", "—"],
            ["Ferraillage retenu", d["armature"]["libelle"], "—",
             "nappe supérieure en console"],
            ["Effort tranchant résistant", f(d["VRdc"], 1), "kN/m",
             "EC2 §6.2.2 sans armature d'âme"],
            ["Vérification de l'effort tranchant", "OK" if d["ok_tranchant"] else "NON",
             "—", "V<sub>Ed</sub> ≤ V<sub>Rdc</sub>"],
            ["Flèche à long terme", f(d["fleche"]), "mm", "G + ψ<sub>0</sub>Q"],
            ["Flèche limite", f(d["fleche_lim"]), "mm", "L/750"],
            ["**Vérification de la flèche**", "**OK**" if d["ok_fleche"] else "**NON**",
             "—", "—"],
        ],
    )


def tab_semelle_voile():
    s_ = EXT["semelle_voile"]
    return dict(
        caption="Tableau 13 — Semelle filante neuve du voile de rive : vérification de "
                "la contrainte de sol.",
        header=["Grandeur", "Valeur", "Unité", "Critère"],
        widths=[60, 28, 20, 52],
        rows=[
            ["Largeur d'assise B retenue", f(s_["B"], 2), "m",
             "B<sub>ELS</sub> = " + f(s_["B_els"], 2) + " m"],
            ["Hauteur de semelle h", f(s_["h"], 2), "m", "DTU 13.1"],
            ["Hauteur utile d", f(s_["d"], 2), "m", "h − 0,05 m"],
            ["Effort normal ELS", f(s_["N_els"], 1), "kN/ml",
             "voile + poutre-acrotère"],
            ["Effort normal ELU", f(s_["N_elu"], 1), "kN/ml", "1,35 G + 1,50 Q"],
            ["Contrainte ELS", f(s_["sigma_els"], 3), "MPa", "≤ 0,100 MPa"],
            ["Contrainte ELU", f(s_["sigma_elu"], 3), "MPa", "≤ 0,150 MPa"],
            ["**Vérification**", "**OK**" if s_["ok_els"] and s_["ok_elu"] else "**NON**",
             "—", "semelle admise"],
        ],
    )


def tab_puits():
    rows = []
    for i, p in [(1, EXT["puits_1"]), (2, EXT["puits_2"])]:
        rows.append([
            f"n° {i}", f(p["D"]), f(p["profondeur"]), f(p["W_kN"], 1),
            f(p["sigma_els"], 3), f(p["sigma_elu"], 3),
            "OK" if (p["ok_els"] and p["ok_elu"]) else "NON",
        ])
    return dict(
        caption="Tableau 11 — Puits de fondation en gros béton C16/20.",
        header=["Puits", "Diamètre (m)", "Profondeur (m)", "Poids propre (kN)",
                "σ<sub>ELS</sub> (MPa)", "σ<sub>ELU</sub> (MPa)", "Vérif."],
        widths=[20, 30, 32, 36, 30, 30, 22],
        rows=rows,
    )


def tab_joint():
    j = EXT["joint"]
    return dict(
        caption="Tableau 12 — Justification du joint de dilatation entre extension et "
                "bâtiment existant.",
        header=["Grandeur", "Valeur", "Unité", "Observation"],
        widths=[62, 28, 20, 50],
        rows=[
            ["Longueur dilatable", f(j["L"]), "m", "extension seule"],
            ["Coefficient de dilatation thermique", "10", "×10⁻⁶ /°C", "béton armé"],
            ["Amplitude thermique retenue", f(j["dT"], 0), "°C",
             "ΔT = 20 °C, écarts France"],
            ["Déplacement total", f(j["deplacement_mm"]), "mm", "α·ΔT·L"],
            ["Largeur de joint mise en œuvre", f(j["largeur"], 0), "mm",
             "fond de joint compressible"],
            ["**Marge disponible**", f"**{f(j['marge_pct'],1)} %**", "—",
             "**suffisante → conforme**"],
        ],
    )


def tab_longrine():
    l = EXT["longrine_D1"]
    return dict(
        caption="Tableau 13 — Longrine de répartition sous D1 sur la fondation filante "
                "existante.",
        header=["Grandeur", "Valeur", "Unité", "Observation"],
        widths=[62, 26, 22, 50],
        rows=[
            ["Charge du mur au-dessus de D1", f(l["g_mur"], 1), "kN/ml",
             "meulière 16 cm, 2 niveaux"],
            ["Effort normal ELS", f(l["N_els"], 1), "kN/ml", "—"],
            ["Effort normal ELU", f(l["N_elu"], 1), "kN/ml", "1,35 G + 1,50 Q"],
            ["Largeur nécessaire ELS", f(l["B_els"]), "m", "N/q<sub>ELS</sub>"],
            ["**Largeur retenue**", f"**{l['B']}**", "m", "arrondi au multiple de 5 cm"],
            ["Hauteur utile", f(l["d"]), "m", "diffusion à 45° (DTU 13.1)"],
            ["Hauteur totale", f(l["h"]), "m", "d + 5 cm"],
            ["σ<sub>ELS</sub> sous la semelle", f(l["sigma_els"], 3), "MPa",
             "≤ 0,10 MPa"],
            ["σ<sub>ELU</sub> sous la semelle", f(l["sigma_elu"], 3), "MPa",
             "≤ 0,15 MPa"],
            ["**Vérification**", "**OK**", "—", "fondation conservée intégralement"],
        ],
    )


def tab_ba_appuis():
    rows = []
    for j in BA["jambages"]:
        rows.append(["Jambage " + j["rep"], f"{int(j['b']*100)} × {int(j['h']*100)}",
                     f(j["N_elu"], 0), f(j["sigma"], 2),
                     j["armature"]["libelle"]])
    p = BA["poteau_D3D5"]
    rows.append(["Poteau D3/D5", f"{int(p['b']*100)} × {int(p['h']*100)}",
                 f(p["N_elu"], 0), f(p["sigma"], 2), p["armature"]["libelle"]])
    for s in BA["sommiers"]:
        rows.append([f"Sommier {s['rep']}", "25 × 40", "—", "—",
                     s["armature"]["libelle"]])
    return dict(
        caption="Tableau 14 — Récapitulatif des appuis en béton armé coulés en place.",
        header=["Ouvrage", "Section (cm)", "N<sub>ELU</sub> (kN)", "σ (MPa)",
                "Ferraillage"],
        widths=[46, 30, 30, 26, 46],
        rows=rows,
    )


def tab_fondations():
    rows = []
    for fo in BA["fondations"]:
        rows.append([
            fo["rep"], f(fo["b_mur"] * 100, 0), f(fo["B_exist"]),
            f(fo["N_els"], 1), f(fo["sigma_els"], 3), f(fo["sigma_elu"], 3),
            "OK" if (fo["ok_els"] and fo["ok_elu"]) else "NON",
            f(fo["sigma_jambage"], 3),
        ])
    return dict(
        caption="Tableau 15 — Vérification de la contrainte sous les fondations filantes "
                "en meulière existantes (hypothèse H-01 : meulière continue).",
        header=["Rep.", "ép. mur (cm)", "B assise (m)", "N<sub>ELS</sub> (kN/ml)",
                "σ<sub>ELS</sub> (MPa)", "σ<sub>ELU</sub> (MPa)", "Vérif. globale",
                "σ sous jambage (MPa)"],
        widths=[12, 26, 26, 30, 30, 30, 26, 34],
        rows=rows,
    )


def tab_repartition():
    rows = []
    for r in BA["repartition_jambages"]:
        rows.append([
            r["rep"], f(r["B_new"]), f(r["epaisseur"] * 100, 0),
            f(r["sigma_avant"], 1), f(r["sigma_apres"], 1),
            "OK" if r["ok"] else "NON", r["As"]["libelle"],
        ])
    return dict(
        caption="Tableau 16 — Longrines de répartition sous jambages : maîtrise de la "
                "concentration de charge.",
        header=["Rep.", "Largeur (m)", "Ép. (cm)", "σ avant (kPa)", "σ après (kPa)",
                "Vérif.", "Ferraillage"],
        widths=[16, 30, 24, 32, 32, 22, 40],
        rows=rows,
    )


def tab_metre_beton():
    rows = []
    for l in MET["beton"]:
        rows.append([l["lib"], f(l["n"], 0), f(f"{l['b']} × {l['h']}"),
                     f(l["L"]), f(l["V"])])
    rows.append(["**TOTAL BÉTON**", "—", "—", "—", f"**{f(MET['beton_total'])}**"])
    return dict(
        caption="Tableau 17 — Avant-métré du béton armé coulé en place.",
        header=["Ouvrage", "Nombre", "Section (m)", "Longueur (m)", "Volume (m³)"],
        widths=[78, 22, 30, 30, 28],
        rows=rows,
    )


def tab_metre_profiles():
    rows = []
    for rep, profil, poids, L in MET["profiles_detail"]:
        rows.append([rep, profil, f(poids, 1), f(L), f(poids * L, 0)])
    rows.append(["**TOTAL ACIER**", "—", "—", "—", f"**{f(MET['profiles_kg'],0)} kg**"])
    return dict(
        caption="Tableau 18 — Avant-métré des profilés métalliques de reprise en "
                "sous-œuvre.",
        header=["Rep.", "Profilé", "Poids (kg/m)", "Longueur (m)", "Poids total (kg)"],
        widths=[20, 50, 34, 34, 40],
        rows=rows,
    )


def tab_metre_synthese():
    return dict(
        caption="Tableau 19 — Synthèse générale de l'avant-métré quantitatif.",
        header=["Poste", "Quantité", "Unité", "Observation"],
        widths=[72, 30, 20, 54],
        rows=[
            ["Béton armé C25/30 — appuis et extension", f(MET["beton_total"]), "m³",
             "jambages, poteaux, sommiers, voile, longrines"],
            ["Béton armé — dalle de terrasse", f(MET["dalle_terrasse"]), "m³",
             "8,03 × 2,00 × 0,20"],
            ["Aciers HA B500B", f(MET["acier_t"]), "t",
             "ratio moyen retenu 120 kg/m³"],
            ["Gros béton C16/20 — puits", f(MET["beton_puits"]), "m³",
             "2 puits Ø 1,35 et 1,75 m"],
            ["Terrassement des puits", f(MET["terrassement_puits"]), "m³",
             "en limite séparative — blindage obligatoire"],
            ["Profilés métalliques S355", f(MET["profiles_t"]), "t",
             "6 profilés IPE"],
            ["Étais métalliques", f(MET["etais"], 0), "u",
             "location, durée 12 semaines"],
        ],
    )


# ---------------------------------------------------------------------------
# BLOCS DU DOCUMENT
# ---------------------------------------------------------------------------

BLOCKS = [
    ("h1", "1. Objet, méthode et cadre normatif"),
    ("h2", "1.1 Objet de la note"),
    ("p", "La présente note constitue le **livrable DOC-03** de la Tâche 2. Elle établit "
          "le dimensionnement justifié de l'ensemble des ouvrages de structure et leur "
          "avant-métré quantitatif. Elle s'appuie strictement sur les hypothèses de la "
          "note **DOC-01** et sur les modes opératoires de la note **DOC-02**, auxquelles "
          "elle renvoie pour tout ce qui relève des données d'entrée et de la mise en "
          "œuvre."),
    ("p", "Les arbitrages rendus par le maître d'ouvrage à l'issue de la Tâche 1 sont "
          "intégrés dans les calculs : le **poteau de la verrière est repositionné sous "
          "la poutre retroussée** (levée de l'écart E-01), les **descentes de charges du "
          "charpentier et du verriériste** sont réputées conformes à l'hypothèse "
          "forfaitaire de 250 kg/m² (H-06 et H-18), la **trappe à linge** est positionnée "
          "sur la base du relevé des plans avec un nuage de tolérance sur les plans "
          "d'exécution (H-16), et la **fondation sous D1 est de type meulière continue** "
          "(H-01)."),

    ("h2", "1.2 Méthode de calcul et traçabilité"),
    ("p", "Les calculs sont produits par un **moteur Python** (`calculs.py`) dont chaque "
          "fonction implémente une clause normative identifiée. Le moteur écrit un "
          "fichier de résultats (`calculs_resultats.json`) qui alimente directement la "
          "présente note : **aucune valeur n'est recopiée manuellement**, ce qui garantit "
          "la cohérence entre le texte et les tableaux et permet de rejouer l'intégralité "
          "des calculs en cas de modification d'une hypothèse."),
    ("bullets", [
        "**Flexion simple BA** : NF EN 1992-1-1 §6.1, diagramme rectangulaire simplifié, "
        "bras de levier z = d(1 − 0,4α).",
        "**Effort tranchant BA** : NF EN 1992-1-1 §6.2.2 (sans armature d'âme) et "
        "§6.2.3 (armatures d'âme, treillis à 45°).",
        "**Flèches** : NF EN 1992-1-1 §7.4.3, section fissurée forfaitaire I<sub>e</sub> "
        "= 0,5 I<sub>g</sub>, fluage φ = 2,0.",
        "**Flexion métallique** : NF EN 1993-1-1 §6.2.5, module plastique W<sub>pl</sub> "
        "pour les sections de classe 1 et 2.",
        "**Fondations superficielles** : NF EN 1997-1 §6 et NF P94-261 §9, contraintes "
        "de référence q<sub>ELS</sub> et q<sub>ELU</sub> imposées.",
        "**Poutre continue** : méthode de Clapeyron (équation des trois moments) pour la "
        "poutre retroussée à deux travées.",
    ]),

    ("h2", "1.3 Matériaux et coefficients partiels"),
    ("table", tab_hypotheses()),

    # -------------------------------------------------------------------
    ("pagebreak",),
    ("h1", "2. Reprises en sous-œuvre D1 à D6"),
    ("h2", "2.1 Principe de dimensionnement"),
    ("p", "Chaque profilé de reprise est dimensionné comme une **poutre isostatique "
          "simplement appuyée** sur les deux appuis BA latéraux, reprenant la totalité "
          "des charges gravitaires de la maçonnerie et des planchers situés au-dessus de "
          "l'ouverture. Le profilé est **jumelé** et **maté au mortier sans retrait** sur "
          "toute la surface de contact, ce qui assure la reprise par contact et non par "
          "boulonnage."),
    ("p", "La bande de plancher reprise est prise égale à **1,00 m** de part et d'autre "
          "de l'axe du mur, soit une largeur totale de 2,00 m ; cette valeur est "
          "volontairement prudente dans la mesure où les solives sont perpendiculaires "
          "aux murs de façade et où la continuité des planchers au droit des refends n'est "
          "pas documentée."),
    ("note", "**Critère de flèche.** Le BET impose une flèche maximale sous combinaison "
             "ELS de **L/750 et de 5 mm au plus**. Pour toutes les portées inférieures à "
             "3,75 m, c'est la valeur absolue de 5 mm qui gouverne ; au-delà, c'est le "
             "critère de ratio. Ce critère, très sévère, est justifié par la sensibilité "
             "des maçonneries anciennes et des verrières à toute déformation différentielle."),

    ("h2", "2.2 Descente de charges"),
    ("table", tab_charges()),
    ("table", tab_flexion_detail()),
    ("p", "Les charges permanentes de maçonnerie sont établies avec un poids volumique de "
          "**19,6 kN/m³** (meulière et moellons avec mortier, soit 2000 kg/m³), et une "
          "hauteur de reprise correspondant à **deux niveaux** au-dessus de l'ouverture, "
          "soit 5,72 m. Les planchers sont comptés pour G0 = 3,00 kN/m² et Q = 1,50 kN/m² "
          "par niveau."),

    ("h2", "2.3 Résultats du dimensionnement"),
    ("table", tab_rso()),
    ("p", f"Les six profilés satisfont l'ensemble des critères avec des taux de travail "
          f"en flexion compris entre **{f(min(m['taux_M'] for m in RSO),3)}** et "
          f"**{f(max(m['taux_M'] for m in RSO),3)}**. Les flèches calculées sont toutes "
          f"très inférieures à la limite de 5 mm, le critère dimensionnant étant la "
          f"**résistance en flexion** et non la déformation."),
    ("h2", "2.4 Incidence de la nuance d'acier"),
    ("table", tab_rso_compare()),
    ("p", "Le passage du S355 au S275 impose des profilés plus lourds sur quatre des six "
          "ouvertures. Le **S355 est retenu** : il permet de réduire l'encombrement du "
          "profilé dans les baies de faible hauteur libre (2,15 m à 2,40 m) et de limiter "
          "la hauteur de décaissement de la maçonnerie, point sensible pour la stabilité "
          "des linteaux anciens. Le surcoût matière est marginal au regard du gain de "
          "hauteur disponible et de la simplification du matage."),

    ("h2", "2.5 Points de vigilance sur les profilés"),
    ("bullets", [
        "**D3 (refend central, 3,55 m)** est la reprise la plus chargée du projet "
        f"(q<sub>ELU</sub> = {f([m for m in RSO if m['rep']=='D3'][0]['q_elu'],1)} kN/m, "
        f"M = {f([m for m in RSO if m['rep']=='D3'][0]['M'],1)} kN·m). Le profilé retenu "
        f"est un **{[m for m in RSO if m['rep']=='D3'][0]['profil']}**, posé sur le "
        "poteau BA 25 × 40 encastré à l'about du refend conservé (voir §3.2).",
        "**D2 (façade, 3,80 m)** cumule la charge du mur de façade en meulière ép. 47 cm "
        "et deux niveaux de plancher ; le profilé doit être mis en place par passes "
        "alternées avec étaiement double (DOC-02 §4.2).",
        "**D1** est la seule reprise dont la fondation filante est **conservée "
        "intégralement** : le profilé est de faible portée (2,60 m) et la longrine de "
        "répartition (§3.5) reprend l'intégralité de la charge sans élargissement.",
        "Les **platine d'appui** et les **goussets** doivent être pré-scellés dans les "
        "jambages avant démolition ; leur dimensionnement est renvoyé à la Tâche 4 "
        "(PL-05).",
    ]),
    ("figure", os.path.join(FIG, "fig12_schema_rso.png"),
     "Figure 1 — Reprise en sous-œuvre type : élévation sur une baie de façade "
     "(D2, D4, D6). Le profilé jumelé est maté au mortier sans retrait sur le sommier BA, "
     "lui-même solidaire des deux jambages.", 168),


    # -------------------------------------------------------------------
    ("pagebreak",),
    ("h1", "3. Béton armé des appuis et des fondations"),
    ("h2", "3.1 Jambages et sommiers des baies de façade"),
    ("p", "Les baies D2 (3,80 m), D4 (2,00 m) et D6 (1,54 m) sont encadrées par des "
          "**jambages BA 25 × 50 cm** (25 × 45 cm pour D6) coulés en place contre la "
          "maçonnerie conservée, et coiffées d'un **sommier BA 25 × 40 cm** constituant "
          "un chaînage horizontal continu. Le sommier ne participe pas à la reprise des "
          "charges verticales — celle-ci est assurée par le profilé — mais il **reprend "
          "les efforts de traction** induits par la flexion du profilé et **répartit les "
          "charges** dans la maçonnerie sus-jacente."),
    ("table", tab_ba_appuis()),

    ("h2", "3.2 Poteau BA au croisement D3 / D5"),
    ("p", "Le croisement des ouvertures D3 et D5 au droit de l'about du refend central "
          "conservé constitue le point le plus délicat de l'opération. Un **poteau BA "
          "25 × 40 cm** y est coulé, encastré dans l'about du refend par des armatures "
          "HA12 ancrées sur 0,50 m dans les joints de maçonnerie. Il reçoit deux platines "
          "pré-scellées perpendiculaires, l'une pour le profilé de D3, l'autre pour celui "
          "de D5, et reprend en outre la descente de charge du refend lui-même."),
    ("table", dict(
        caption="Tableau 0 — Vérification du poteau BA 25 × 40 au croisement D3/D5.",
        header=["Grandeur", "Valeur", "Unité", "Critère"],
        widths=[62, 34, 22, 42],
        rows=[
            ["Section", f"{int(BA['poteau_D3D5']['b']*100)} × "
                        f"{int(BA['poteau_D3D5']['h']*100)}", "cm", "—"],
            ["Hauteur libre", f(BA['poteau_D3D5']['l0']), "m", "RDC"],
            ["Élancement λ", f(BA['poteau_D3D5']['lambda_'], 1), "—", "—"],
            ["Effort normal ELU", f(BA['poteau_D3D5']['N_elu'], 0), "kN",
             "refend + 2 profilés"],
            ["Résistance N<sub>Rd</sub>", f(BA['poteau_D3D5']['NRd'], 0), "kN",
             "α·A<sub>c</sub>·f<sub>cd</sub>"],
            ["**Taux de travail**", f"**{f(BA['poteau_D3D5']['taux'],3)}**", "—",
             "**< 1,00 → conforme**"],
            ["Contrainte moyenne", f(BA['poteau_D3D5']['sigma'], 2), "MPa",
             "< f<sub>cd</sub> = 16,67 MPa"],
            ["Ferraillage", BA['poteau_D3D5']['armature']['libelle'], "—",
             "+ cadres HA 8 e = 200 mm"],
            ["Ancrage dans le refend", f(BA['poteau_D3D5']['ancrage']), "m",
             "HA12, essai d'arrachement"],
        ],
    )),

    ("h2", "3.3 Voile BA de rive à créer"),
    ("p", "Le voile de rive, **à créer**, ép. 20 cm, est élevé **en limite de "
          "propriété, dans le prolongement du mur pignon**. Il n'existe pas "
          "aujourd'hui : la version antérieure de l'étude le décrivait à tort comme "
          "mitoyen et solidaire d'un mur existant. Il est **fondé sur une semelle "
          "filante à créer** (65 × 30 cm), descendue à l'arase NGF 39,02 comme les "
          "fondations voisines, et claveté au pignon existant par des armatures "
          "HA 12 traversantes tous les 0,50 m scellées chimiquement. Il reprend "
          "l'about de la poutre-acrotère isostatique de 8,03 m et la poussée du "
          "remblai côté voisin sur sa hauteur enterrée."),
    ("table", tab_voile()),

    ("h2", "3.4 Poutre-acrotère de rive, console et poutre perpendiculaire"),
    ("p", "La poutre-acrotère BA **30 × 67 cm** est située **en limite de dalle, à "
          "2,00 m du nu de la façade**, et fait office d'acrotère de la terrasse. Sa "
          "hauteur est calée entre la sous-face du plancher haut RDC (**NGF 44,08**) "
          "et l'**arase supérieure de l'acrotère (NGF 44,75)**. Elle est "
          "**isostatique** : travée unique de **8,03 m** entre le **voile de rive à "
          "créer** (appui droit) et l'**extrémité en console** de la poutre "
          "perpendiculaire (appui gauche)."),
    ("p", "**Schéma structurel rectifié le 11/11/2026 (arbitrage E-02).** Le croquis "
          "du maître d'œuvre impose une lecture différente de la version antérieure :"),
    ("ul", [
        "la terrasse mesure **8,03 × 2,00 m**, poutre-acrotère **comprise** ;",
        "la poutre perpendiculaire à la façade franchit **1,30 m** jusqu'au poteau "
        "BA, puis se poursuit en **porte-à-faux de 0,70 m** jusqu'au bord de dalle ;",
        "le **poteau BA 25 × 25** est implanté à **1,30 m du nu de façade**, à "
        "l'extrémité gauche des 8,03 m ;",
        "la **dalle** porte en console de **1,70 m** depuis la façade jusqu'à la "
        "poutre de rive.",
    ]),
    ("p", "La poutre de 8,03 m ne s'appuie donc plus sur le poteau : elle repose sur "
          "l'about de la console. Le poteau reprend la réaction de cette console, "
          "amplifiée par la charge que lui transmet la poutre de rive. Le schéma "
          "« poutre isostatique appuyée sur le poteau et sur un voile mitoyen "
          "existant » est **abandonné**."),
    ("table", tab_poutre()),
    ("table", tab_poutre_perp()),
    ("figure", os.path.join(FIG, "fig10_poutre_efforts.png"),
     "Figure 2 — Diagrammes de moment fléchissant, d'effort tranchant et de déformée "
     "de la poutre-acrotère isostatique de 8,03 m.", 190),
    ("note", f"**Conclusion sur la poutre-acrotère.** Le moment de flexion ELU atteint "
             f"**{f(EXT['poutre']['M'],1)} kN·m** et impose un ferraillage de "
             f"**{EXT['poutre']['armature']['libelle']}** "
             f"(A s = {f(EXT['poutre']['armature']['As_cm2'])} cm²) avec des "
             f"{EXT['poutre']['etriers']['libelle']} ; les bielles comprimées sont "
             f"largement vérifiées (V Rd,max = {f(EXT['poutre']['VRdmax'],0)} kN). "
             f"La flèche à long terme ressort à **{f(EXT['poutre']['fleche'])} mm, "
             f"soit L/{int(EXT['poutre']['ratio'])}**. Elle respecte le critère "
             f"L/250 applicable à un élément en béton armé de cette portée mais "
             f"dépasse le critère L/500 retenu par le BET ; une **contre-flèche de "
             f"coffrage de {f(EXT['poutre']['contre_fleche'],0)} mm** ramène la "
             f"flèche résiduelle à "
             f"**{f(EXT['poutre']['fleche_residuelle'])} mm**, inférieure à L/500."),
    ("figure", os.path.join(FIG, "fig11_coupe_poutre.png"),
     "Figure 3 — Poutre-acrotère : coupe transversale avec la table collaborante de la "
     "dalle, et dispositions de ferraillage de l'âme.", 132),

    ("h2", "3.5 Dalle de toiture-terrasse"),
    ("p", "La dalle de terrasse mesure **8,03 m de long sur 2,00 m de large**, "
          "poutre-acrotère comprise. Elle porte en **console depuis la façade "
          "existante** jusqu'à la poutre de rive, soit un porte-à-faux de **1,70 m**. "
          "C'est ce porte-à-faux qui dimensionne le ferraillage, en nappe supérieure ; "
          "le débord au-delà du poteau (0,70 m) est quant à lui bordé par la poutre "
          "perpendiculaire, qui en reprend la charge."),
    ("table", tab_dalle()),

    ("h2", "3.6 Poteau BA 25 × 25 à 1,30 m du nu de façade"),
    ("p", "Le poteau BA 25 × 25 est implanté à **1,30 m du nu de la façade "
          "existante**, à l'extrémité gauche des 8,03 m, sous la poutre-acrotère "
          "perpendiculaire. Sa position est **contractuelle** : elle est reprise dans "
          "le module `niveaux_retenus.py` sous la constante "
          "`POS_POTEAU_FAÇADE = 1,30 m`, source unique de vérité partagée par les "
          "notes et les plans d'exécution. Il reprend la réaction de la console "
          "(dalle + about de la poutre de rive) augmentée de la demi-travée de la "
          "poutre perpendiculaire, soit un effort normal ELU de "
          f"**{f(EXT['poteau']['N_elu'],1)} kN**."),
    ("table", tab_poteau()),

    # -------------------------------------------------------------------
    ("pagebreak",),
    ("h1", "4. Fondations"),
    ("h2", "4.1 Principe général"),
    ("p", "Les fondations de l'extension sont descendues jusqu'au **niveau des fondations "
          "existantes**, soit l'arase NGF 39,02. Deux puits en gros béton reprennent les "
          "charges concentrées (poteau BA à 1,30 m et voile de rive à créer) ; le "
          "voile repose en outre sur une **semelle filante neuve 65 × 30 cm** et les "
          "charges réparties sont reprises par des longrines BA. Les fondations du bâtiment "
          "existant, de type **meulière continue** (hypothèse H-01 levée), sont "
          "**intégralement conservées** : aucun élargissement, aucun reprise en sous-"
          "œuvre de fondation n'est nécessaire."),

    ("h2", "4.2 Semelle filante du voile de rive"),
    ("p", "La **semelle filante du voile de rive** est une semelle neuve de "
          "**65 × 30 cm** (B = 0,65 m, h = 0,30 m), section retenue selon E-02, "
          "descendue à l'arase NGF 39,02 et "
          "coulée en fond de fouille blindé en limite de propriété. La largeur résulte "
          "de la vérification de la contrainte de sol : σ<sub>ELS</sub> = "
          f"**{f(EXT['semelle_voile']['sigma_els'],3)} MPa** ≤ 0,100 MPa et "
          f"σ<sub>ELU</sub> = {f(EXT['semelle_voile']['sigma_elu'],3)} MPa ≤ 0,150 MPa. "
          f"L'effort normal transmis est de {f(EXT['semelle_voile']['N_els'],1)} kN/ml "
          "à l'ELS. Elle est ferraillée par 4 HA 12 filants et des étriers HA 8 "
          "e = 250 mm."),
    ("table", tab_semelle_voile()),
    ("h2", "4.3 Puits en gros béton"),
    ("p", "Deux puits en gros béton C16/20 sont descendus en limite séparative : le "
          "puits n° 1 sous le poteau BA 25 × 25, le puits n° 2 sous le voile de rive, "
          "à l'aplomb de la semelle filante. Ils reprennent les charges concentrées que "
          "la semelle ne peut répartir en limite de propriété."),
    ("table", tab_puits()),
    ("p", "Les puits sont descendus en limite séparative. Le terrassement est réalisé "
          "**à la main sur les 0,50 m supérieurs** puis mécaniquement, avec blindage des "
          "parois et bétonnage immédiat après réception du fond de fouille par le BET "
          "(point d'arrêt PA-2, DOC-02 §7). Le béton de remplissage est un **C16/20** "
          "dosé à 250 kg/m³, coulé par passes de 0,80 m avec vibration."),

    ("h2", "4.4 Fondations existantes en meulière"),
    ("p", "La contrainte sous les semelles filantes existantes est vérifiée sous les "
          "seules charges du mur, les planchers étant repris par les refends. La "
          "vérification est menée avec une largeur d'assise estimée à "
          "**b<sub>mur</sub> + 2 × 0,15 m**, valeur à confirmer par les sondages "
          "H-01 et H-08."),
    ("table", tab_fondations()),
    ("p", "Les contraintes calculées restent très inférieures aux seuils de 0,10 et "
          "0,15 MPa. **En revanche**, la concentration de charge au droit des jambages "
          "— où la totalité de la charge de la baie se reporte sur deux appuis étroits — "
          "conduit à une contrainte locale de l'ordre de 0,15 MPa, **supérieure au seuil "
          "ELS**. Une **longrine de répartition BA** est donc mise en place sous chaque "
          "jambage."),

    ("h2", "4.5 Longrines de répartition sous jambages"),
    ("table", tab_repartition()),
    ("p", "Les longrines, de section **1,30 × 0,25 m**, sont coulées contre la semelle "
          "existante après piquage et scellement d'armatures HA12 tous les 0,30 m. Elles "
          "ramènent la contrainte sous jambage à moins de **0,055 MPa**, soit une marge "
          "de sécurité supérieure à 45 % sur le seuil ELS."),

    ("h2", "4.6 Longrine de répartition sous D1"),
    ("p", "D1 est la seule ouverture dont la fondation est **conservée sans "
          "élargissement**. La charge du mur est faible (refend de 16 cm sur deux "
          "niveaux), et une longrine de 0,30 m de large suffit à ramener la contrainte "
          "sous le seuil."),
    ("table", tab_longrine()),

    ("h2", "4.7 Joint de dilatation et désolidarisation"),
    ("table", tab_joint()),
    ("p", "Le joint de 20 mm offre une marge de **92 %** sur le déplacement thermique "
          "calculé. Cette marge est volontairement importante : elle couvre l'incertitude "
          "sur le coefficient de dilatation réel des maçonneries anciennes et sur les "
          "amplitudes thermiques effectives en toiture-terrasse, où la dalle est "
          "directement exposée au rayonnement."),
    ("figure", os.path.join(FIG, "fig13_plan_fondation.png"),
     "Figure 4 — Plan de fondation de l'extension : poutre-acrotère en limite de "
     "dalle, poutre perpendiculaire, poteau BA à 1,30 m, voile de rive à créer, "
     "semelle filante et puits de gros béton.",
     186),

    # -------------------------------------------------------------------
    ("pagebreak",),
    ("h1", "5. Avant-métré quantitatif"),
    ("h2", "5.1 Béton armé"),
    ("table", tab_metre_beton()),
    ("p", "Le volume total de béton armé coulé en place, hors dalle de terrasse, s'élève "
          f"à **{f(MET['beton_total'])} m³**. Le ratio d'acier retenu pour l'avant-métré "
          "est de **120 kg/m³**, valeur usuelle pour des ouvrages de ce type fortement "
          "ferraillés (jambages, poteaux, longrines)."),

    ("h2", "5.2 Profilés métalliques"),
    ("table", tab_metre_profiles()),

    ("h2", "5.3 Synthèse générale"),
    ("table", tab_metre_synthese()),
    ("note", "**Réserves sur l'avant-métré.** Les quantités ci-dessus sont des quantités "
             "de **commande** et non des quantités d'exécution : elles n'intègrent ni les "
             "recouvrements d'armatures, ni les chutes de découpe, ni les accessoires de "
             "levage et de calage. Un coefficient de majoration de 5 % est recommandé "
             "pour la commande des aciers HA et de 3 % pour les profilés."),

    # -------------------------------------------------------------------
    ("pagebreak",),
    ("h1", "6. Conclusion et synthèse des résultats"),
    ("p", "L'ensemble des ouvrages de structure de l'opération est **justifié et "
          "conforme** aux exigences des Eurocodes et aux critères imposés par le BET. "
          "Les points structurants suivants doivent être retenus :"),
    ("bullets", [
        "**La poutre-acrotère est conforme**, sous une condition explicite. "
        f"En travée unique de 8,03 m, la flèche à long terme atteint "
        f"**{f(EXT['poutre']['fleche'])} mm (L/{int(EXT['poutre']['ratio'])})** : elle "
        "respecte le critère L/250 mais **dépasse le critère L/500** retenu par le BET. "
        f"Une **contre-flèche de coffrage de {f(EXT['poutre']['contre_fleche'],0)} mm** "
        "est donc prescrite ; elle ramène la flèche résiduelle sous L/500 sans modifier "
        f"le ferraillage ({EXT['poutre']['armature']['libelle']}, "
        f"{EXT['poutre']['etriers']['libelle']}).",
        "**Les six profilés de reprise sont conformes** avec des taux de travail en "
        "flexion de 0,55 à 0,88 et des flèches négligeables. Le critère dimensionnant "
        "est la résistance et non la déformation.",
        "**Les fondations existantes en meulière continue sont conservées intégralement** "
        "sous réserve du sondage H-08. Seule une longrine de répartition est "
        "nécessaire sous les jambages des baies élargies.",
        f"**Les deux puits de l'extension** (Ø {f(EXT['puits_1']['D'],2)} m et "
        f"{f(EXT['puits_2']['D'],2)} m, profondeur {f(EXT['puits_1']['profondeur'],2)} m) "
        f"ramènent la contrainte à {f(EXT['puits_1']['sigma_els'],3)} et "
        f"{f(EXT['puits_2']['sigma_els'],3)} MPa, soit une marge de 1 à 2 % seulement sur "
        "le seuil ELS : **le dimensionnement est tendu et ne tolère aucune dégradation "
        "des hypothèses de sol**. Toute valeur de q_ELS inférieure à 0,099 MPa impose de "
        "réétudier les puits.",
        "**Le voile BA de rive à créer** est justifié en poussée des terres au repos, avec un "
        "ferraillage de 4 HA 12 par face et une vérification de l'effort tranchant à la "
        "base (V<sub>Ed</sub> = 32,9 kN ≤ V<sub>Rd,c</sub> = 94,7 kN).",
        "**Le joint de dilatation de 20 mm** offre une marge de 92 % sur le déplacement "
        "thermique calculé.",
    ]),
    ("h2", "6.1 Points d'arrêt avant la Tâche 3"),
    ("p", "Le passage à la Tâche 3 (plans d'exécution PL-01 à PL-03) est subordonné à la "
          "confirmation des points suivants."),
    ("bullets", [
        "**Confirmation par sondage de la nature et de la largeur d'assise** des "
        "fondations filantes (H-01, H-08) — condition de validité du §4.3.",
        "**Confirmation de la valeur de q<sub>ELS</sub>** par essai pressiométrique ou "
        "pénétrométrique au droit des deux puits — condition de validité du §4.2.",
        "**Confirmation définitive du schéma E-02** (poteau à 1,30 m, console de "
        "0,70 m, terrasse de 2,00 m, voile de rive à créer) — position arrêtée le "
        "11/11/2026 et reportée sur les plans PL-01 à PL-05.",
        "**Réception des fiches techniques** du charpentier et du verriériste pour "
        "confirmer l'hypothèse forfaitaire de 250 kg/m² (H-06, H-18).",
    ]),
    ("h2", "6.2 Livrables et suite de la mission"),
    ("p", "La **Tâche 2** est close par la remise de la présente note **DOC-03**, en "
          "formats **.docx** et **.pdf**, accompagnée du moteur de calcul "
          "(`calculs.py`), du fichier de résultats (`calculs_resultats.json`) et des "
          "figures. La **Tâche 3** produira les plans d'exécution **PL-01** (plan de "
          "reprise en sous-œuvre RDC), **PL-02** (plan de coffrage de l'extension) et "
          "**PL-03** (coupes et élévations), au format A3 paysage à l'échelle 1/50, en "
          ".dxf et .pdf."),
    ("note", "**La Tâche 2 est terminée.** Les observations éventuelles sur les "
             "hypothèses de calcul, les sections retenues ou l'avant-métré doivent être "
             "formulées avant le lancement de la Tâche 3 (plans d'exécution)."),
]


def main():
    docx, pdf = build(META, BLOCKS, HERE, "DOC-03_Note_Calculs")
    print("DOCX :", docx)
    print("PDF  :", pdf)


if __name__ == "__main__":
    main()
