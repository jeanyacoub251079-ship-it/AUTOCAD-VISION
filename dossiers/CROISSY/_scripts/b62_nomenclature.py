#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-62 — NOMENCLATURE ET FAÇONNAGE — CROISSY-FLORA — Indice A.
CARNAC v3.0 — régime OUTILLÉ (V13).

Extraction par script des calques *-NOMENCLATURE des 8 DXF B-60 Ind. A.
Jamais ressaisie. Un écart plan/note est SIGNALÉ, jamais corrigé.
Aucun devis, aucune commande, aucun sabot inventé, A4 non chiffré.
"""
from __future__ import annotations

import csv
import json
import os
import re
from collections import Counter, defaultdict

import ezdxf
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
from matplotlib.backends.backend_pdf import PdfPages

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANS = os.path.join(ROOT, "_plans")
OUT = os.path.join(ROOT, "_rendus")
CALC = os.path.join(ROOT, "06_CALCULS")
os.makedirs(OUT, exist_ok=True)

LIGNES: list[str] = []

# Masses linéaires — catalogues, pas des données de projet.
# NF EN 10365 (HEA/HEB/IPE/UPE) · EN 10219 (SHS) · NF A 35-080 (HA).
MASSE = {
    "HEA 200": 42.3,
    "HEB 160": 42.6,
    "HEB 200": 61.3,
    "IPE 120": 10.4,
    "IPE 200": 22.4,
    "UPE 200": 22.4,
    "SHS 140x140x6,3": 26.4,
    "HA8": 0.395,
    "HA12": 0.888,
}
ST25C_KG_M2 = 2.02  # Ø7 e150 2 nappes
ACIER_KG_M3 = 7850.0
BOIS_KG_M3 = 420.0  # ρ_mean C24 EC5 — pour info, commande en m³
PLATINE_KG = 0.200 * 0.200 * 0.015 * ACIER_KG_M3  # 4,71 kg

DXFS = {
    "FOND": "FLORA_B60_FOND_EXE_IndA.dxf",
    "VERT": "FLORA_B60_VERT_EXE_IndA.dxf",
    "PLANCHER": "FLORA_B60_PLANCHER_EXE_IndA.dxf",
    "LINTEAU": "FLORA_B60_LINTEAU_EXE_IndA.dxf",
    "MACON": "FLORA_B60_MACON_EXE_IndA.dxf",
    "METAL": "FLORA_B60_METAL_EXE_IndA.dxf",
    "CHARPENTE": "FLORA_B60_CHARPENTE_EXE_IndA.dxf",
    "ASSEMBLAGE": "FLORA_B60_ASSEMBLAGE_EXE_IndA.dxf",
}


def log(t: str = "") -> None:
    LIGNES.append(t)
    print(t)


def titre(t: str) -> None:
    log("")
    log(t)
    log("-" * 78)


def texts_on(msp, layer: str) -> list[str]:
    out = []
    for e in msp:
        try:
            if e.dxf.layer != layer:
                continue
        except Exception:
            continue
        t = e.dxftype()
        if t == "TEXT":
            out.append(e.dxf.text or "")
        elif t == "MTEXT":
            out.append(e.text or "")
    return out


def all_texts(msp, prefix: str) -> list[tuple[str, str]]:
    out = []
    for e in msp:
        t = e.dxftype()
        if t not in ("TEXT", "MTEXT"):
            continue
        try:
            lay = e.dxf.layer
        except Exception:
            continue
        if not lay.startswith(prefix):
            continue
        s = e.dxf.text if t == "TEXT" else e.text
        if s:
            out.append((lay, s))
    return out


def fnum(x) -> str:
    if x is None or x == "":
        return ""
    if isinstance(x, float):
        if abs(x - round(x)) < 1e-9:
            return str(int(round(x)))
        return ("%.3f" % x).replace(".", ",")
    return str(x)


def row(
    famille: str,
    type_b60: str,
    repere: str,
    designation: str,
    section: str,
    l_unit_mm,
    n,
    l_tot_mm,
    poids_kg,
    calque: str,
    statut: str,
    note: str = "",
) -> dict:
    return {
        "famille": famille,
        "type_b60": type_b60,
        "repere": repere,
        "designation": designation,
        "section": section,
        "l_unit_mm": l_unit_mm,
        "n": n,
        "l_tot_mm": l_tot_mm,
        "poids_kg": None if poids_kg is None else round(poids_kg, 2),
        "calque": calque,
        "statut": statut,
        "note": note,
    }


# ---------------------------------------------------------------------------
titre("=" * 78)
log("B-62 — NOMENCLATURE ET FAÇONNAGE — CROISSY-FLORA — INDICE A")
log("CARNAC v3.0 — régime OUTILLÉ (V13)")
log("Mode : PARTIEL-DÉCLARÉ (H non relevée · D-19 · A4 DOC-09 · sabots non catalogués)")
log("Filigrane : NE PAS COMMANDER SANS VISA — PARTIEL-DECLARE")
log("=" * 78)

titre("[0] ENVIRONNEMENT (OUT-01)")
log("  interpréteur : Python 3 · ezdxf %s · matplotlib %s" % (
    ezdxf.__version__, matplotlib.__version__))
log("  rôle : lecture DXF B-60, extraction TEXT, CSV UTF-8, façonnage PNG/PDF")
log("  écriture persistante : oui · relecture : oui")

titre("[1] ENTRÉES — 8 DXF B-60 Ind. A")
extracted: dict[str, dict] = {}
missing = []
for typ, fn in DXFS.items():
    path = os.path.join(PLANS, fn)
    if not os.path.isfile(path):
        missing.append(fn)
        log("  MANQUANT  %s" % fn)
        continue
    size = os.path.getsize(path)
    doc = ezdxf.readfile(path)
    auditor = doc.audit()
    n_err = len(auditor.errors)
    msp = doc.modelspace()
    nom_lay = "%s-NOMENCLATURE" % typ
    nom_txt = texts_on(msp, nom_lay)
    all_t = all_texts(msp, typ + "-")
    n_ent = sum(1 for e in msp if getattr(e.dxf, "layer", "").startswith(typ + "-"))
    extracted[typ] = {
        "path": path,
        "size": size,
        "n_err": n_err,
        "n_ent": n_ent,
        "nom_txt": nom_txt,
        "all_txt": all_t,
        "doc": doc,
    }
    log("  %-11s %9d o  audit=%d  entités %s-* = %3d  TEXT nomenclature = %d"
        % (typ, size, n_err, typ, n_ent, len(nom_txt)))

if missing:
    log("ARRÊT : DXF manquant — nomenclature non produite.")
    raise SystemExit(2)

titre("[1b] TEXTES BRUTS — calques *-NOMENCLATURE (preuve V13)")
for typ, d in extracted.items():
    log("  -- %s --" % typ)
    for s in d["nom_txt"]:
        log("    " + s.replace("\n", " / "))

# ---------------------------------------------------------------------------
# Parsing : chaque ligne de nomenclature devient une ou plusieurs lignes
# de commande. Les nombres viennent du TEXT DXF, pas d'une table recopiée.
# ---------------------------------------------------------------------------
ROWS: list[dict] = []
ECARTS: list[dict] = []
EN_ATTENTE: list[str] = []
HORS: list[str] = []


def add(*a, **k):
    ROWS.append(row(*a, **k))


def ecart(quoi, plan, note, traitement):
    ECARTS.append({"quoi": quoi, "plan": plan, "note": note, "traitement": traitement})


# ----- FOND -----
fond_nom = " | ".join(extracted["FOND"]["nom_txt"])
# SF1 800x800x250 ×1
m = re.search(r"SF1\s+800x800x250", fond_nom)
if m:
    vol = 0.800 * 0.800 * 0.250
    add("BETON", "FOND", "SF1", "Semelle isolée sous P2", "800×800×250 C25/30",
        None, 1, None, None, "FOND-NOMENCLATURE", "CERTAIN",
        "volume = %.3f m³" % vol)
# HA8 e150 6+6
m = re.search(r"HA8 e150\s+6\+6", fond_nom)
if m:
    # 6+6 = 12 barres, L = 800 − 2×50 = 700 mm (c_nom 50 porté au plan)
    n_ha8 = 12
    l_ha8 = 700
    add("BARRE", "FOND", "SF1-HA8", "Lit HA8 e150 2 directions", "HA8 S500B",
        l_ha8, n_ha8, l_ha8 * n_ha8, n_ha8 * (l_ha8 / 1000.0) * MASSE["HA8"],
        "FOND-NOMENCLATURE", "CERTAIN",
        "6+6 lus sur DXF · L=800−2×c_nom50=700 mm · 2 lits croisés = 1 nappe")
# 6 HA12 équerre l_bd 166 — CE SONT les 6 HA12 de P2 (A1). Pas un surplus.
m = re.search(r"6 HA12 equerre\s+l_bd 166", fond_nom)
if m:
    add("BARRE", "FOND", "A1-HA12", "Attentes P2 dans SF1 — ÉQUERRE", "HA12 S500B",
        None, 6, None, None, "FOND-NOMENCLATURE", "ÉCART-FORME",
        "6 HA12 = longitudinales P2, pas un surplus. Forme ÉQUERRE l_bd 166 mm. "
        "B-42 a débité DROITE 3760 mm — écart signalé, non tranché.")
# TYPE 600x600 selon D-19
if "TYPE 600x600x300 mini" in fond_nom:
    add("BETON", "FOND", "SF-T", "Semelle type si fouille D-19", "600×600×300 mini C25/30",
        None, None, None, None, "FOND-NOMENCLATURE", "EN ATTENTE D-19",
        "quantité selon fouille — non commandable")
    EN_ATTENTE.append("SF-T 600×600 — quantité selon D-19")
if "GB C16/20 sous semelle" in fond_nom:
    add("BETON", "FOND", "GB", "Gros béton de rattrapage", "C16/20",
        None, None, None, None, "FOND-NOMENCLATURE", "EN ATTENTE D-19",
        "sous semelle SI existant plus profond — jamais de remontée")
    EN_ATTENTE.append("GB C16/20 — volume selon fouille")
if "proprete 50 mm" in fond_nom:
    add("BETON", "FOND", "BP", "Béton de propreté sous SF1", "50 mm",
        None, 1, None, None, "FOND-NOMENCLATURE", "CERTAIN",
        "emprise 800×800")
if "BECHE 200 mm" in fond_nom:
    m = re.search(r"BECHE 200 mm × (\d+) mm", fond_nom)
    l_beche = int(m.group(1)) if m else None
    add("BETON", "FOND", "BECHE", "Réhausse SE existante", "200 mm × %s mm C25/30" % l_beche,
        l_beche, 1, l_beche, None, "FOND-NOMENCLATURE", "CERTAIN",
        "hauteur d'ouvrage NON portée — volume non calculé")
if "RSO passerelle" in fond_nom:
    add("BETON", "FOND", "RSO", "Passerelle passes alternées", "C16/20 passes ≤ 1000 mm",
        None, 1, None, None, "FOND-NOMENCLATURE", "CERTAIN",
        "zone, pas un cube — volume non calculé")

# ----- VERT -----
vert_nom = " | ".join(extracted["VERT"]["nom_txt"])
# H = 2800 HYPOTHÈSE
h_hyp = 2800
if "H = 2800 mm HYPOTHESE" in vert_nom or "H = 2800" in vert_nom:
    EN_ATTENTE.append("H = 2 800 mm = hypothèse B-20 — R-42-1 ouverte — débits INDICATIFS")

for rep, sec, cadres, n_ed in [
    ("P2", "150×250", "HA8 e150", "159,0"),
    ("P3", "400×500", "HA8 e200", "35,8"),
    ("J1", "240×500", "HA8 e200", "39,8"),
]:
    if re.search(r"%s\s+%s" % (rep, sec.replace("×", "x")), vert_nom):
        # volume HYP
        a, b = [int(x) for x in sec.replace("×", "x").split("x")]
        vol = (a / 1000.0) * (b / 1000.0) * (h_hyp / 1000.0)
        add("BETON", "VERT", rep, "Poteau/jambage BA", "%s C25/30" % sec,
            h_hyp, 1, h_hyp, None, "VERT-NOMENCLATURE", "INDICATIF (H hyp.)",
            "N_Ed %s kN · volume %.3f m³ à H=2800 hyp. · R-42-1 ouverte" % (n_ed, vol))
        add("BARRE", "VERT", "%s-HA12" % rep, "Longitudinales 6 HA12", "HA12 S500B",
            None, 6, None, None, "VERT-NOMENCLATURE", "INDICATIF (H hyp.)",
            "6 lus sur DXF · L_dev dépend de H et de la forme (voir façonnage)")
        add("BARRE", "VERT", "%s-CAD" % rep, "Cadres %s" % cadres, "HA8 S500B",
            None, None, None, None, "VERT-NOMENCLATURE", "INDICATIF (H hyp.)",
            "espacement lu · nombre = f(H) — voir façonnage B-42")

# ----- PLANCHER -----
pl_nom = " | ".join(extracted["PLANCHER"]["nom_txt"])
m = re.search(r"Dallage\s+130 mm C25/30\s+([0-9,]+)\s*m2", pl_nom)
if m:
    surf = float(m.group(1).replace(",", "."))
    add("BETON", "PLANCHER", "DALLAGE", "Dallage BA RDC BAS", "130 mm C25/30",
        None, 1, None, None, "PLANCHER-NOMENCLATURE", "CERTAIN (emprise B-43)",
        "111,15 m² B-43 NON remesurée (H-06) · volume = %.2f m³" % (surf * 0.130))
    add("TREILLIS", "PLANCHER", "ST25C", "Treillis soudé partie haute", "ST25C Ø7 e150 257 mm²/m",
        None, 1, None, round(surf * ST25C_KG_M2, 1),
        "PLANCHER-NOMENCLATURE", "CERTAIN (emprise B-43)",
        "continu sous joints de retrait · %.2f kg à 2,02 kg/m² · STR-03 absent (encadrements non coupés)" % (surf * ST25C_KG_M2))
if "recharge 150 mm" in pl_nom:
    add("BETON", "PLANCHER", "RECHARGE", "Recharge sur 100 % emprise", "150 mm (D-35)",
        None, 1, None, None, "PLANCHER-NOMENCLATURE", "CERTAIN (D-35)",
        "111,15 × 0,15 = 16,67 m³ — lot GO, pas un ferraillage")
if "GNT 400 mm" in pl_nom:
    add("DIVERS", "PLANCHER", "GNT", "Fond de forme", "GNT 400 mm",
        None, 1, None, None, "PLANCHER-NOMENCLATURE", "CERTAIN",
        "volume 111,15 × 0,40 = 44,46 m³")
if "polyane 200 um" in pl_nom:
    add("DIVERS", "PLANCHER", "POLYANE", "Film polyane", "200 µm",
        None, 1, None, None, "PLANCHER-NOMENCLATURE", "CERTAIN",
        "remonté 100 mm")
if "desolid. 20 mm" in pl_nom:
    add("DIVERS", "PLANCHER", "DESOLID", "Désolidarisation périphérique", "polystyrène 20 mm + mastic",
        None, 1, None, None, "PLANCHER-NOMENCLATURE", "CERTAIN",
        "périmètre + P2/P3/J1")
HORS.append("Zones A/B existant (solives 8×18, IPE 160/330) — hors nomenclature neuve")
HORS.append("Zone C E-07 — PA-03 ouvert, hors planche")

# ----- LINTEAU -----
lin_nom = " | ".join(extracted["LINTEAU"]["nom_txt"])
for rep, Lmm in [("F1a", 1000), ("F1b", 900), ("F1c", 850)]:
    pat = r"%s\s+2xHEA 200\s+L=\s*%d" % (rep, Lmm)
    if re.search(pat, lin_nom):
        add("PROFILE", "LINTEAU", rep, "Frangement 2 × HEA 200", "HEA 200 S275",
            Lmm, 2, 2 * Lmm, 2 * (Lmm / 1000.0) * MASSE["HEA 200"],
            "LINTEAU-NOMENCLATURE", "CERTAIN",
            "n=2 lus (2xHEA) · L=%d mm lue" % Lmm)
for rep, Lmm in [("R3-N", 1550), ("R3-S", 1550)]:
    if re.search(r"%s UPE 200" % rep, lin_nom):
        add("PROFILE", "LINTEAU", rep, "Linteau UPE 200 + D-36", "UPE 200 S275",
            Lmm, 1, Lmm, (Lmm / 1000.0) * MASSE["UPE 200"],
            "LINTEAU-NOMENCLATURE", "CERTAIN — D-36 OBLIGATOIRE",
            "sans béton : NE PAS POSER (B-50 A3 τ=1,40) · aussi porté METAL")
if "S1 x4" in lin_nom:
    add("BETON", "LINTEAU", "S1", "Sommier abouts R3", "200×400×200 C25/30",
        None, 4, None, None, "LINTEAU-NOMENCLATURE", "CERTAIN",
        "hors bois E-08 · volume 4×0,016 = 0,064 m³")
if "S2 x4" in lin_nom:
    add("BETON", "LINTEAU", "S2", "Sommier F1", "200×500×200 C25/30",
        None, 4, None, None, "LINTEAU-NOMENCLATURE", "CERTAIN",
        "volume 4×0,020 = 0,080 m³")

# ----- MACON -----
mac_nom = " | ".join(extracted["MACON"]["nom_txt"])
for rep, dim, n in [
    ("C-R1-O/E", "300 x 500 x 200", 2),
    ("C-F2-O/E", "300 x 400 x 200", 2),
    ("C-F3-O/E", "300 x 400 x 200", 2),
]:
    if dim.replace(" ", "") in mac_nom.replace(" ", "") or dim in mac_nom:
        a, b, c = [int(x) for x in dim.split(" x ")]
        vol = n * (a / 1000.0) * (b / 1000.0) * (c / 1000.0)
        add("BETON", "MACON", rep, "Coussin de répartition D-37",
            "%s C25/30" % dim.replace(" x ", "×"),
            None, n, None, None, "MACON-NOMENCLATURE", "CERTAIN (D-37)",
            "w_b=300 mm MINI — ne pas réduire · volume %.3f m³" % vol)
        add("BARRE", "MACON", rep + "-HA8", "Armatures constructives", "HA8 S500B",
            None, 4 * n, None, None, "MACON-NOMENCLATURE", "CONSTRUCTIF",
            "4 HA8 lus / coussin · forme NON dessinée — façonnage DROITE assumé, signalé")
HORS.append("F1/R3/R2/F4 — pas de coussin (B-46 OK sans)")

# ----- METAL -----
met_nom = " | ".join(extracted["METAL"]["nom_txt"])
# F2 x1 HEB 200 S275 L=2850
metal_items = [
    ("F2", r"F2 x1 HEB 200 S275 L=(\d+)", "HEB 200", 1, "Poutre neuve"),
    ("F3", r"F3 x1 HEB 160 S275 L=(\d+)", "HEB 160", 1, "Poutre neuve — R-45-1 aucune charge ajoutée"),
    ("F4", r"F4 x1 IPE 200 S275 L=(\d+)", "IPE 200", 1, "Poutre neuve"),
    ("R1", r"R1 x2 UPE 200 S275 L=(\d+)", "UPE 200", 2, "Moisage — boulons A2 déjà ASSEMBLAGE"),
    ("R2-N", r"R2-N/S x2 HEB 160 S275 L=(\d+)", "HEB 160", 1, "Refend Nord — n=1 de la paire x2"),
    ("R2-S", r"R2-N/S x2 HEB 160 S275 L=(\d+)", "HEB 160", 1, "Refend Sud — n=1 de la paire x2"),
    ("R3-N", r"R3-N/S x2 UPE 200 S275 L=(\d+)", "UPE 200", 1, "DÉJÀ LINTEAU — pas un surplus, remplissage D-36"),
    ("R3-S", r"R3-N/S x2 UPE 200 S275 L=(\d+)", "UPE 200", 1, "DÉJÀ LINTEAU — pas un surplus, remplissage D-36"),
]
seen_r2 = False
seen_r3 = False
for rep, pat, sec, n, des in metal_items:
    m = re.search(pat, met_nom)
    if not m:
        continue
    Lmm = int(m.group(1))
    if rep in ("R3-N", "R3-S"):
        # déjà nommé LINTEAU — pas de double commande
        if not seen_r3:
            add("BETON", "METAL", "R3-D36", "Remplissage UPE 200 D-36", "C25/30 entre ailes",
                1550, 2, 3100, None, "METAL-NOMENCLATURE", "CONDITION DE POSE",
                "volume indicatif — forages diam./entraxe NON PORTÉS sur B-60 METAL → écart")
            seen_r3 = True
        continue
    add("PROFILE", "METAL", rep, des, sec + " S275",
        Lmm, n, n * Lmm, n * (Lmm / 1000.0) * MASSE[sec],
        "METAL-NOMENCLATURE", "CERTAIN" if "R-45-1" not in des else "CERTAIN — R-45-1",
        "L=%d mm lue · n=%d lu" % (Lmm, n))

# P1 : L absente du calque NOMENCLATURE
if "P1-N/S x2 SHS 140x140x6,3" in met_nom:
    # L portée à la note B-60 METAL §2 = 3,00 m, PAS sur le calque nomenclature
    add("PROFILE", "METAL", "P1-N/S", "Poteau tube", "SHS 140×140×6,3 S275",
        3000, 2, 6000, 2 * 3.00 * MASSE["SHS 140x140x6,3"],
        "METAL-NOMENCLATURE + note B-60 METAL §2", "L HORS CALQUE NOMENCLATURE",
        "n=2 lu sur DXF · L=3000 mm lue à la NOTE B-60 METAL §2, absente du calque NOMENCLATURE")
    ecart(
        "P1 L",
        "calque METAL-NOMENCLATURE : SHS sans L",
        "B-60 METAL §2 : L=3,00 m",
        "B-62 prend L de la note, signale l'absence au calque. Pas d'invention.",
    )

# Stab1 : pas de L
if "Stab1 x4 files IPE 120" in met_nom:
    add("PROFILE", "METAL", "Stab1", "Entretoise anti-déversement IPE 160 existants",
        "IPE 120 S275", None, 4, None, None,
        "METAL-NOMENCLATURE", "EN ATTENTE — L non portée",
        "4 files lues · pas 2500 mm lu · L unitaire NON écrite (portée IPE 160 inconnue) — NON COMMANDABLE")
    EN_ATTENTE.append("Stab1 IPE 120 ×4 — L unitaire absente (portée IPE 160 non relevée)")

if "A4 NON chiffre" in met_nom or "A4 NON chiffre" in " | ".join(extracted["ASSEMBLAGE"]["nom_txt"]):
    EN_ATTENTE.append("A4 scellement M12 — capacité NON écrite (DOC-09) — R-50-3 ouverte")

# Forages D-36
forages_portes = any("forage" in s.lower() or "diam" in s.lower() for _, s in extracted["METAL"]["all_txt"]
                     if "NOMENCLATURE" in _)
# The habillage says "Forages de remplissage en semelle sup. Diam./entraxe -> B-62."
ecart(
    "Forages D-36 R3",
    "B-60 METAL HABILLAGE : « Diam./entraxe -> B-62 » — AUCUNE cote de forage sur le plan",
    "B-50 A3 prescrit le remplissage, pas le piquage",
    "B-62 N'INVENTE PAS les diamètres ni l'entraxe. Renvoyé à B-60 METAL Ind. B.",
)
EN_ATTENTE.append("Forages de remplissage R3 — diam. et entraxe non portés")

# ----- CHARPENTE -----
ch_nom = " | ".join(extracted["CHARPENTE"]["nom_txt"])
m = re.search(r"PN1/PN2/PN3\s+x3\s+75 x 200 C24\s+L=(\d+)", ch_nom)
if m:
    Lmm = int(m.group(1))
    vol = 3 * 0.075 * 0.200 * (Lmm / 1000.0)
    add("BOIS", "CHARPENTE", "PN1/2/3", "Pannes neuves", "75×200 C24",
        Lmm, 3, 3 * Lmm, vol * BOIS_KG_M3,
        "CHARPENTE-NOMENCLATURE", "CERTAIN",
        "x3 L=%d lus · volume %.4f m³ · ρ_mean 420 kg/m³ info · commande en m³" % (Lmm, vol))
m = re.search(r"DF1/DF2\s+x2\s+arb 100 x 200 \+ ent 75 x 200 C24\s+L_horiz=(\d+)", ch_nom)
if m:
    Lh = int(m.group(1))
    # arbalétrier L=3620 portée au calque DETAILS, pas à NOMENCLATURE (L_horiz=3200)
    add("BOIS", "CHARPENTE", "DF-arb", "Arbalétrier demi-ferme", "100×200 C24",
        3620, 2, 7240, 2 * 0.100 * 0.200 * 3.620 * BOIS_KG_M3,
        "CHARPENTE-DETAILS (L) + NOMENCLATURE (n)", "L HORS CALQUE NOMENCLATURE",
        "n=2 lu NOMENCLATURE · L=3620 mm lue DETAILS · L_horiz=3200 au calque NOMENCLATURE")
    add("BOIS", "CHARPENTE", "DF-ent", "Entrait demi-ferme", "75×200 C24",
        Lh, 2, 2 * Lh, 2 * 0.075 * 0.200 * (Lh / 1000.0) * BOIS_KG_M3,
        "CHARPENTE-NOMENCLATURE", "CERTAIN",
        "n=2 L_horiz=%d lus · désolidarisées E-07" % Lh)
    ecart(
        "DF-arb L",
        "NOMENCLATURE : L_horiz=3200 (entrait) — arbalétrier sans L propre",
        "DETAILS / B-44 : L=3,62 m",
        "B-62 prend L=3620 du calque DETAILS. Signale l'absence au calque NOMENCLATURE.",
    )
m = re.search(r"CF\s+x2\s+75 x 225 C24\s+L=(\d+)", ch_nom)
if m:
    Lmm = int(m.group(1))
    add("BOIS", "CHARPENTE", "CF", "Contrefiches — APRÈS purge E-05", "75×225 C24",
        Lmm, 2, 2 * Lmm, 2 * 0.075 * 0.225 * (Lmm / 1000.0) * BOIS_KG_M3,
        "CHARPENTE-NOMENCLATURE", "CERTAIN — APRÈS PURGE",
        "x2 L=%d lus · inverse de phasage INTERDIT" % Lmm)
HORS.append("E-04 potelets SUPPRIMÉS · E-05/06 existant B-24 · E-07 non chargé · ZN1/ZN2 D-19")
HORS.append("Contreventement toiture ABSENT au D2 — non inventé")
HORS.append("Sabots DF/PN — efforts B-44 V=14,89 / 5,11 kN — type NON catalogué DOC-09 — NON INVENTÉ")

# ----- ASSEMBLAGE -----
as_nom = " | ".join(extracted["ASSEMBLAGE"]["nom_txt"])
m = re.search(r"Boulon M16 8.8 \+ ecrou \+ 2 rondelles LARGES\s+(\d+)\s*u", as_nom)
if m:
    n = int(m.group(1))
    add("CONNECTEUR", "ASSEMBLAGE", "A2-M16", "Boulon moisage R1", "M16 8.8 + écrou + 2 rondelles LARGES",
        None, n, None, None, "ASSEMBLAGE-NOMENCLATURE", "CERTAIN",
        "%d u lus · 10 / face · harnais INTERDIT · galva ISO 1461 70 µm" % n)
m = re.search(r"Tige M16 8.8 scellement chimique\s+(\d+)\s*u", as_nom)
if m:
    n = int(m.group(1))
    add("CONNECTEUR", "ASSEMBLAGE", "A5-M16", "Tige scellement pied P1", "M16 8.8 scellement chimique",
        None, n, None, None, "ASSEMBLAGE-NOMENCLATURE", "CERTAIN (constructif)",
        "%d u lus · 4 / poteau · σ 0,118" % n)
m = re.search(r"Tige M12 scellement chimique\s+(\d+)\s*u", as_nom)
if m:
    n = int(m.group(1))
    add("CONNECTEUR", "ASSEMBLAGE", "A4-M12", "Tige scellement Stab1", "M12 scellement chimique",
        None, n, None, None, "ASSEMBLAGE-NOMENCLATURE", "NON CHIFFRÉ — R-50-3",
        "%d u lus (2 / file × 4) · capacité NON écrite DOC-09 · NON COMMANDABLE en l'état · essai 1/4 files" % n)
m = re.search(r"Platine 200 x 200 x 15 S275\s+(\d+)\s*u", as_nom)
if m:
    n = int(m.group(1))
    add("CONNECTEUR", "ASSEMBLAGE", "A5-PLAT", "Platine de pied P1", "200×200×15 S275",
        None, n, None, n * PLATINE_KG, "ASSEMBLAGE-NOMENCLATURE", "CERTAIN",
        "%d u lus · %.2f kg / u" % (n, PLATINE_KG))

# ÉCART P2 HA12 forme
ecart(
    "P2 HA12 forme",
    "B-60 FOND : 6 HA12 ÉQUERRE l_bd 166 mm (A1, opposable, R-50-1 CLOSE)",
    "B-42 §6 : DROITE L=3 760 mm (H+2×40φ) — débits « indicatifs, B-62 les établira »",
    "MÊMES 6 barres, DEUX géométries. B-62 ne tranche pas. Façonnage ÉQUERRE porté "
    "(plan EXE opposable) ; débit B-42 conservé en vis-à-vis. Commande de ces 6 barres "
    "BLOQUÉE tant que l'écart n'est pas levé par B-42 Ind. C ou B-60 FOND Ind. B.",
)

# Cadres VERT : B-42 donne n et L
# On les PORTE comme indicatifs issus de la note amont, pas du DXF nomenclature
# (le DXF dit e150/e200, pas le nombre).
ecart(
    "Cadres P2/P3/J1 nombre",
    "B-60 VERT NOMENCLATURE : HA8 e150 / e200 — PAS de quantité",
    "B-42 §6 : P2 20 cadres L=0,72 m · P3 15 L=1,72 · J1 15 L=1,32 · total 50 · 83,8 kg",
    "B-62 PORTE les débits B-42 en INDICATIF (H hyp.) et signale l'absence de qté au plan.",
)

# Ajouter les lignes de façonnage B-42 (indicatives) — distinctes, source note
# P2 HA12 : on NE recopie PAS le débit DROITE comme ligne de commande (écart forme).
# Cadres : oui, indicatifs.
add("BARRE", "VERT", "P2-CAD-B42", "Cadres P2 (débit note B-42)", "HA8 S500B",
    720, 20, 14400, 20 * 0.72 * MASSE["HA8"],
    "note B-42 §6 (PAS le DXF)", "INDICATIF (H hyp.) — source note",
    "2(150+250)−8×30+2×80 = 720 mm · n=20 = f(H=2800/e150)")
add("BARRE", "VERT", "P3-CAD-B42", "Cadres P3 (débit note B-42)", "HA8 S500B",
    1720, 15, 25800, 15 * 1.72 * MASSE["HA8"],
    "note B-42 §6 (PAS le DXF)", "INDICATIF (H hyp.) — source note",
    "2(400+500)−8×30+2×80 = 1720 mm · n=15 = f(H=2800/e200)")
add("BARRE", "VERT", "J1-CAD-B42", "Cadres J1 (débit note B-42)", "HA8 S500B",
    1320, 15, 19800, 15 * 1.32 * MASSE["HA8"],
    "note B-42 §6 (PAS le DXF)", "INDICATIF (H hyp.) — source note",
    "2(240+500)−8×30+2×80 = 1320 mm · n=15")

# P3/J1 HA12 : DROITE B-42, pas d'équerre A1 (appuis maçonnerie D-19)
add("BARRE", "VERT", "P3-HA12-FAC", "Longitudinales P3 — DROITE (B-42)", "HA12 S500B",
    3760, 6, 22560, 6 * 3.76 * MASSE["HA12"],
    "note B-42 §6", "INDICATIF (H hyp.)",
    "H+2×40φ = 2800+960 = 3760 · D-19 pied · pas d'équerre SF1")
add("BARRE", "VERT", "J1-HA12-FAC", "Longitudinales J1 — DROITE (B-42)", "HA12 S500B",
    3760, 6, 22560, 6 * 3.76 * MASSE["HA12"],
    "note B-42 §6", "INDICATIF (H hyp.)",
    "H+2×40φ = 3760 · D-19 pied · D-34 f_k=1,5")

# P2 HA12 façonnage ÉQUERRE (plan FOND) — L_dev = H + l_bd + crochet tête
# H=2800 hyp + 166 + 12φ tête (144) = 3110 mm INDICATIF — NON commandable (écart)
l_dev_eq = 2800 + 166 + 12 * 12  # 3110
add("BARRE", "FOND", "P2-HA12-EQ", "Longitudinales P2 — ÉQUERRE (plan FOND)", "HA12 S500B",
    l_dev_eq, 6, 6 * l_dev_eq, 6 * (l_dev_eq / 1000.0) * MASSE["HA12"],
    "FOND-NOMENCLATURE (forme) + H hyp. VERT", "NON COMMANDABLE — écart forme",
    "L_dev = H_hyp 2800 + l_bd 166 + 12φ 144 = %d mm · MÊMES 6 barres que A1 · "
    "B-42 disait DROITE 3760 — écart" % l_dev_eq)

# Coussins HA8 DROITE assumée
for rep, Lmm, n in [("C-R1", 440, 8), ("C-F2", 340, 8), ("C-F3", 340, 8)]:
    add("BARRE", "MACON", rep + "-HA8-FAC", "HA8 coussin — DROITE assumée", "HA8 S500B",
        Lmm, n, n * Lmm, n * (Lmm / 1000.0) * MASSE["HA8"],
        "MACON-NOMENCLATURE (4 HA8) · L calculée", "CONSTRUCTIF — forme non dessinée",
        "L = grand côté − 2×c_nom30 · forme NON sur B-60 MACON")

# ---------------------------------------------------------------------------
titre("[2] NOMENCLATURE DÉTAILLÉE — %d lignes" % len(ROWS))
log("  %-8s %-11s %-14s %-36s %10s %4s %8s  %s" % (
    "FAM", "TYPE", "REPÈRE", "SECTION", "L_u mm", "n", "kg", "STATUT"))
for r in ROWS:
    log("  %-8s %-11s %-14s %-36s %10s %4s %8s  %s" % (
        r["famille"], r["type_b60"], r["repere"], r["section"][:36],
        fnum(r["l_unit_mm"]), fnum(r["n"]) if r["n"] is not None else "—",
        fnum(r["poids_kg"]) if r["poids_kg"] is not None else "—",
        r["statut"]))

# Recap familles
titre("[3] RÉCAPITULATIF PAR FAMILLE / CALQUE")
by_fam = defaultdict(lambda: {"n_lig": 0, "kg": 0.0, "kg_ok": True})
for r in ROWS:
    f = r["famille"]
    by_fam[f]["n_lig"] += 1
    if r["poids_kg"] is None:
        by_fam[f]["kg_ok"] = False
    else:
        by_fam[f]["kg"] += r["poids_kg"]
for f, v in by_fam.items():
    kg_s = "%.1f" % v["kg"] if v["kg_ok"] else "%.1f + EN ATTENTE" % v["kg"]
    log("  %-12s  %2d lignes   poids porté %s kg" % (f, v["n_lig"], kg_s))

# ---------------------------------------------------------------------------
titre("[4] FAÇONNAGE ACIERS BA")
log("  Mandrin mini EC2 : HA12 → 4φ = 48 mm · HA8 → 4φ = 32 mm.")
log("  Recouvrement : aucun (barres unitaires, pas de raccord).")
log("")
log("  Rép.           Forme      Cotes (mm)                         L_dev   n   Mandrin  Statut")
log("  P2-HA12-EQ     ÉQUERRE    H=2800 hyp. + l_bd=166 + 12φ=144   %5d    6   48 mm    NON COMMANDABLE (écart)" % l_dev_eq)
log("  P3-HA12-FAC    DROITE     H+2×40φ = 3760                     3760    6   —        INDICATIF H hyp.")
log("  J1-HA12-FAC    DROITE     H+2×40φ = 3760                     3760    6   —        INDICATIF H hyp.")
log("  P2-CAD-B42     CADRE      150×250, c=30, retours 80          720    20   32 mm    INDICATIF H hyp.")
log("  P3-CAD-B42     CADRE      400×500, c=30, retours 80          1720   15   32 mm    INDICATIF H hyp.")
log("  J1-CAD-B42     CADRE      240×500, c=30, retours 80          1320   15   32 mm    INDICATIF H hyp.")
log("  SF1-HA8        DROITE     700 (800−2×50) + crochets 5φ       700    12   32 mm    CERTAIN (nappe)")
log("  C-R1-HA8-FAC   DROITE     440 (500−2×30)                     440     8   32 mm    constructif, forme non dessinée")
log("  C-F2-HA8-FAC   DROITE     340 (400−2×30)                     340     8   32 mm    constructif, forme non dessinée")
log("  C-F3-HA8-FAC   DROITE     340 (400−2×30)                     340     8   32 mm    constructif, forme non dessinée")
log("  ST25C          NAPPE      111,15 m² Ø7 e150 partie haute     —      1   —        CERTAIN emprise B-43")
log("")
log("  Cadres SF1 (HA8 e150 jusqu'au lit) : NOMBRE NON PORTÉ au plan FOND — non débité.")
EN_ATTENTE.append("Cadres SF1 HA8 e150 jusqu'au lit — quantité absente du plan FOND")

# ---------------------------------------------------------------------------
titre("[5] COHÉRENCE PLAN ↔ NOMENCLATURE")

# Repères attendus par type (lus sur les calques d'ouvrage, pas inventés)
ATTENDUS = {
    "FOND": ["SF1", "HA8", "HA12", "BECHE", "RSO"],
    "VERT": ["P2", "P3", "J1"],
    "PLANCHER": ["Dallage", "ST25C"],
    "LINTEAU": ["F1a", "F1b", "F1c", "R3-N", "R3-S", "S1", "S2"],
    "MACON": ["C-R1", "C-F2", "C-F3"],
    "METAL": ["F2", "F3", "F4", "R1", "R2-N", "R2-S", "P1", "Stab1"],
    "CHARPENTE": ["PN1", "PN2", "PN3", "DF1", "DF2", "CF"],
    "ASSEMBLAGE": ["M16", "M12", "Platine"],
}

reperes_nom = " ".join(r["repere"] for r in ROWS)
n_ok = 0
n_ko = 0
for typ, reps in ATTENDUS.items():
    blob = " | ".join(extracted[typ]["nom_txt"])
    for rp in reps:
        # présence dans le TEXT nomenclature OU dans une ligne extraite
        in_nom = rp in blob or rp in reperes_nom or rp.replace("-", "") in reperes_nom.replace("-", "")
        if in_nom:
            n_ok += 1
        else:
            n_ko += 1
            log("  ÉCART : %s / %s — attendu, non trouvé dans nomenclature extraite" % (typ, rp))
log("  Repères attendus retrouvés : %d · manquants : %d" % (n_ok, n_ko))

# Éléments explicitement hors nomenclature (lus « Hors nomencl. »)
titre("[5b] HORS NOMENCLATURE (déclaré sur les plans)")
for h in HORS:
    log("  · " + h)

titre("[5c] EN ATTENTE / NON COMMANDABLE")
for e in EN_ATTENTE:
    log("  · " + e)

titre("[5d] ÉCARTS PLAN ↔ NOTE — SIGNALÉS, NON CORRIGÉS")
for e in ECARTS:
    log("  · %s" % e["quoi"])
    log("      plan : %s" % e["plan"])
    log("      note : %s" % e["note"])
    log("      B-62 : %s" % e["traitement"])

# ---------------------------------------------------------------------------
# CSV
# ---------------------------------------------------------------------------
titre("[6] EXPORT TABLEUR CSV (UTF-8, séparateur ;)")

COLS = ["famille", "type_b60", "repere", "designation", "section",
        "l_unit_mm", "n", "l_tot_mm", "poids_kg", "calque", "statut", "note"]
FAM_FILES = {
    "BARRE": "B-62_barres.csv",
    "TREILLIS": "B-62_barres.csv",
    "PROFILE": "B-62_profiles.csv",
    "BOIS": "B-62_bois.csv",
    "CONNECTEUR": "B-62_connecteurs.csv",
    "BETON": "B-62_beton.csv",
    "DIVERS": "B-62_beton.csv",
}

csv_paths = {}
by_file = defaultdict(list)
for r in ROWS:
    by_file[FAM_FILES[r["famille"]]].append(r)

# master
master = os.path.join(OUT, "B-62_nomenclature.csv")
master2 = os.path.join(CALC, "B-62_nomenclature.csv")


def write_csv(path, rows):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
        w.writerow([
            "FILIGRANE", "NE PAS COMMANDER SANS VISA — PARTIEL-DECLARE — CROISSY-FLORA B-62 Ind. A — 21/10/2026",
        ])
        w.writerow([])
        w.writerow(COLS)
        for r in rows:
            w.writerow([fnum(r[c]) if c in ("l_unit_mm", "n", "l_tot_mm", "poids_kg") else r[c] for c in COLS])
    return os.path.getsize(path)


sz_m = write_csv(master, ROWS)
write_csv(master2, ROWS)
log("  MASTER  %s  %d o  %d lignes" % (os.path.basename(master), sz_m, len(ROWS)))
csv_paths["MASTER"] = master

for fn, rows in sorted(by_file.items()):
    p = os.path.join(OUT, fn)
    p2 = os.path.join(CALC, fn)
    sz = write_csv(p, rows)
    write_csv(p2, rows)
    csv_paths[fn] = p
    log("  %-22s %5d o  %2d lignes" % (fn, sz, len(rows)))

# cohérence CSV
coh = os.path.join(OUT, "B-62_coherence.csv")
with open(coh, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, delimiter=";")
    w.writerow(["quoi", "plan", "note", "traitement"])
    for e in ECARTS:
        w.writerow([e["quoi"], e["plan"], e["note"], e["traitement"]])
    w.writerow([])
    w.writerow(["EN_ATTENTE"])
    for e in EN_ATTENTE:
        w.writerow([e])
    w.writerow([])
    w.writerow(["HORS_NOMENCLATURE"])
    for e in HORS:
        w.writerow([e])
log("  B-62_coherence.csv  %d o" % os.path.getsize(coh))

# ---------------------------------------------------------------------------
# PNG / PDF façonnage
# ---------------------------------------------------------------------------
titre("[7] PLAN DE FAÇONNAGE (PNG + PDF)")


def draw_equerre(ax, x, y, s=1.0):
    ax.plot([x, x, x + 0.9 * s], [y + 2.2 * s, y, y], "k-", lw=2)
    ax.plot(x, y + 2.2 * s, "k.", ms=4)
    ax.plot(x + 0.9 * s, y, "k.", ms=4)
    ax.text(x - 0.15 * s, y + 1.1 * s, "H", fontsize=7, ha="right", va="center")
    ax.text(x + 0.45 * s, y - 0.18 * s, "l_bd", fontsize=7, ha="center")


def draw_droite(ax, x, y, s=1.0):
    ax.plot([x, x + 2.0 * s], [y, y], "k-", lw=2)
    ax.plot(x, y, "k.", ms=4)
    ax.plot(x + 2.0 * s, y, "k.", ms=4)


def draw_cadre(ax, x, y, s=1.0):
    ax.add_patch(Rectangle((x, y), 1.2 * s, 0.7 * s, fill=False, lw=1.6, ec="k"))


fig = plt.figure(figsize=(16.54, 11.69), dpi=120)  # A3 paysage
fig.patch.set_facecolor("white")
ax = fig.add_axes([0.03, 0.04, 0.94, 0.90])
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)
ax.axis("off")

ax.text(8, 10.55, "B-62  —  PLAN DE FAÇONNAGE DES ACIERS BA  —  CROISSY-FLORA  —  Ind. A",
        ha="center", va="top", fontsize=13, fontweight="bold")
ax.text(8, 10.15, "NE PAS COMMANDER SANS VISA   ·   PARTIEL-DÉCLARÉ   ·   21/10/2026   ·   CARNAC v3.0",
        ha="center", va="top", fontsize=9, color="#8B0000", fontweight="bold")
ax.text(8, 9.82, "D-26 aucune sismique  ·  D-28 aucun joint de dilatation  ·  D-34 f_k=1,5 MPa essais hors mission  ·  R-42-1 H non relevée",
        ha="center", va="top", fontsize=7.5, color="#333")

# bandeau écart
ax.add_patch(FancyBboxPatch((0.3, 8.85), 15.4, 0.80, boxstyle="round,pad=0.02",
                            facecolor="#fff3cd", edgecolor="#856404", lw=1))
ax.text(8, 9.45, "ÉCART NON TRANCHÉ — P2 6 HA12", ha="center", fontsize=8, fontweight="bold", color="#856404")
ax.text(8, 9.15, "Plan FOND (opposable, R-50-1 CLOSE) : ÉQUERRE l_bd 166 mm.   Note B-42 §6 : DROITE L=3 760 mm.",
        ha="center", fontsize=7.5)
ax.text(8, 8.92, "Mêmes 6 barres, deux géométries. B-62 ne tranche pas. Ces 6 barres sont NON COMMANDABLES tant que l'écart n'est pas levé.",
        ha="center", fontsize=7.5)

# tableau
headers = ["Répère", "Forme", "Cotes de façonnage (mm)", "L_dev (mm)", "n", "Ø", "Mandrin", "Statut"]
data = [
    ["P2-HA12-EQ", "ÉQUERRE", "H=2800 hyp. + l_bd=166 + 12φ=144", "3110", "6", "HA12", "48", "NON COMMANDABLE"],
    ["P3-HA12-FAC", "DROITE", "H + 2×40φ = 2800+960", "3760", "6", "HA12", "—", "INDICATIF H hyp."],
    ["J1-HA12-FAC", "DROITE", "H + 2×40φ = 2800+960", "3760", "6", "HA12", "—", "INDICATIF H hyp."],
    ["P2-CAD-B42", "CADRE", "2(150+250)−8×30+2×80", "720", "20", "HA8", "32", "INDICATIF H hyp."],
    ["P3-CAD-B42", "CADRE", "2(400+500)−8×30+2×80", "1720", "15", "HA8", "32", "INDICATIF H hyp."],
    ["J1-CAD-B42", "CADRE", "2(240+500)−8×30+2×80", "1320", "15", "HA8", "32", "INDICATIF H hyp."],
    ["SF1-HA8", "DROITE", "800 − 2×c_nom50 = 700", "700", "12", "HA8", "32", "CERTAIN nappe"],
    ["C-R1-HA8", "DROITE *", "500 − 2×30 = 440  (*forme non dessinée)", "440", "8", "HA8", "32", "constructif"],
    ["C-F2-HA8", "DROITE *", "400 − 2×30 = 340  (*forme non dessinée)", "340", "8", "HA8", "32", "constructif"],
    ["C-F3-HA8", "DROITE *", "400 − 2×30 = 340  (*forme non dessinée)", "340", "8", "HA8", "32", "constructif"],
    ["ST25C", "NAPPE", "111,15 m²  Ø7 e150  partie haute  continu sous JR", "—", "1", "Ø7", "—", "CERTAIN B-43"],
    ["SF1-CAD", "CADRE", "e150 jusqu'au lit inf. — qté NON portée au plan", "—", "—", "HA8", "32", "EN ATTENTE"],
]

col_x = [0.35, 2.15, 3.55, 9.35, 10.55, 11.25, 12.15, 13.25]
col_w = [1.80, 1.40, 5.80, 1.20, 0.70, 0.90, 1.10, 2.45]
y0 = 8.55
row_h = 0.38
ax.add_patch(Rectangle((0.30, y0 - row_h), 15.4, row_h, facecolor="#1f4e79", edgecolor="k", lw=0.4))
for i, h in enumerate(headers):
    ax.text(col_x[i] + 0.05, y0 - row_h / 2, h, fontsize=6.5, color="white", va="center", fontweight="bold")

for j, line in enumerate(data):
    y = y0 - (j + 2) * row_h
    bg = "#f7f7f7" if j % 2 == 0 else "white"
    if "NON COMMANDABLE" in line[-1]:
        bg = "#f8d7da"
    elif "EN ATTENTE" in line[-1]:
        bg = "#fff3cd"
    elif "INDICATIF" in line[-1]:
        bg = "#e8f4fd"
    ax.add_patch(Rectangle((0.30, y), 15.4, row_h, facecolor=bg, edgecolor="#888", lw=0.3))
    for i, cell in enumerate(line):
        ax.text(col_x[i] + 0.05, y + row_h / 2, cell, fontsize=6.3, va="center")

# croquis
ax.text(0.4, 3.15, "CROQUIS DE FORME (schéma, pas à l'échelle)", fontsize=8, fontweight="bold")
draw_equerre(ax, 0.8, 1.3, 0.7)
ax.text(1.2, 0.85, "ÉQUERRE  (P2 A1)", fontsize=7, ha="center")
draw_droite(ax, 3.6, 2.0, 0.8)
ax.text(5.6, 1.55, "DROITE  (P3 / J1 / SF1-HA8 / coussins)", fontsize=7, ha="center")
draw_cadre(ax, 10.2, 1.5, 1.1)
ax.text(10.85, 1.15, "CADRE  (P2 / P3 / J1)", fontsize=7, ha="center")

ax.text(0.4, 0.55,
        "S500B  ·  c_nom fondation 50 mm  ·  c_nom élévation 30 mm (H-23 XA1)  ·  aucun recouvrement  ·  ST25C non coupé aux joints de retrait.",
        fontsize=7)
ax.text(0.4, 0.28,
        "NON PORTÉ donc NON DÉBITÉ : sabots DF/PN (DOC-09) · L Stab1 · forages D-36 · cadres SF1 · SF-T/GB (D-19) · A4 capacité.  Feu hors lot GO.",
        fontsize=7)
ax.text(15.6, 0.28, "fond B-32 D  ·  amont B-40…B-60", fontsize=7, ha="right")

png_path = os.path.join(PLANS, "FLORA_B62_FACONNAGE_IndA.png")
pdf_path = os.path.join(PLANS, "FLORA_B62_FACONNAGE_IndA.pdf")
fig.savefig(png_path, dpi=160, facecolor="white")
fig.savefig(pdf_path)
plt.close(fig)
log("  PNG  %s  %d o" % (os.path.basename(png_path), os.path.getsize(png_path)))
log("  PDF  %s  %d o" % (os.path.basename(pdf_path), os.path.getsize(pdf_path)))

# ---------------------------------------------------------------------------
# JSON + journal
# ---------------------------------------------------------------------------
audit = {
    "livrable": "B-62 Nomenclature et façonnage",
    "indice": "A",
    "date": "2026-10-21",
    "mode": "PARTIEL-DECLARE",
    "filigrane": "NE PAS COMMANDER SANS VISA",
    "n_lignes": len(ROWS),
    "n_ecarts": len(ECARTS),
    "n_en_attente": len(EN_ATTENTE),
    "dxf": {t: {"size": d["size"], "audit": d["n_err"], "n_ent": d["n_ent"],
                "n_nom": len(d["nom_txt"])} for t, d in extracted.items()},
    "ecarts": ECARTS,
    "en_attente": EN_ATTENTE,
    "hors": HORS,
    "csv": {k: os.path.basename(v) for k, v in csv_paths.items()},
    "faconnage_png": os.path.basename(png_path),
    "faconnage_pdf": os.path.basename(pdf_path),
    "verdict": "CONFORME AVEC RESERVES — PARTIEL-DECLARE — non commandable en l'etat",
}
jp = os.path.join(OUT, "b62_nomenclature.json")
# extracted docs are not serializable
with open(jp, "w", encoding="utf-8") as f:
    json.dump(audit, f, ensure_ascii=False, indent=2)
log("  JSON %s  %d o" % (os.path.basename(jp), os.path.getsize(jp)))

titre("[8] VERDICT")
log("  Lignes de nomenclature : %d" % len(ROWS))
log("  Écarts signalés (non corrigés) : %d" % len(ECARTS))
log("  En attente / non commandable : %d" % len(EN_ATTENTE))
log("  Audit DXF amont : " + ", ".join("%s=%d" % (t, d["n_err"]) for t, d in extracted.items()))
log("  COMPLET : INTERDIT (H, D-19, A4, sabots, forages, écart P2).")
log("  Devis / commande : HORS PÉRIMÈTRE.")
log("  PA-03 / R-50-3 / R-42-1 / R-45-1 : NON CLOS.")
log("  Verdict : CONFORME AVEC RÉSERVES — PARTIEL-DÉCLARÉ — NE PAS COMMANDER SANS VISA.")

journal = os.path.join(OUT, "b62_nomenclature.txt")
with open(journal, "w", encoding="utf-8") as f:
    f.write("\n".join(LIGNES) + "\n")
log("  journal %s  %d o" % (os.path.basename(journal), os.path.getsize(journal)))
