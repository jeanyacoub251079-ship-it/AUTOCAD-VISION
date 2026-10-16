"""Quantitatifs matériaux CSV / Excel (§4.10, Lot 6).

Cohérence stricte avec les JSON de structure : chaque élément compté une
fois, totaux vérifiables.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

from ..logging_setup import get_logger

log = get_logger("structai.export.qty")

BAR_MASS_KG_M2 = {6: 0.222, 8: 0.395, 10: 0.617, 12: 0.888, 14: 1.208,
                  16: 1.578, 20: 2.466, 25: 3.854, 32: 6.313}


def quantities_rows(option: dict, proj: dict) -> list[dict]:
    st = option.get("structure", {})
    dims = option.get("resultats_calcul", {}).get("dimensionnement_armatures", {})
    niveaux = int(proj.get("niveaux", 1) or 1)
    h = float(proj.get("hauteur_etage", 2.8) or 2.8)
    rows: list[dict] = []

    def add(cat, det, unit, qty):
        if qty <= 0:
            return
        rows.append({"Categorie": cat, "Detail": det, "Unite": unit,
                     "Quantite": round(qty, 2)})

    betons: dict[str, float] = {}
    aciers: dict[str, float] = {}
    coff: dict[str, float] = {}

    # dalle : volume = Σ surface × épaisseur (par niveau)
    slab_t = max((d.get("epaisseur", 0.2) for d in st.get("dalles", [])), default=0.2)
    for d in st.get("dalles", []):
        poly = d.get("polygone", [])
        if len(poly) < 3:
            continue
        n = len(poly)
        area = abs(sum(poly[i][0] * poly[(i + 1) % n][1] - poly[(i + 1) % n][0] * poly[i][1]
                       for i in range(n))) / 2
        t = float(d.get("epaisseur", 0.2))
        bt = d.get("materiau", "beton_C25/30").replace("beton_", "") or "C25/30"
        betons[f"dalles {bt}"] = betons.get(f"dalles {bt}", 0) + area * t
        coff["Dalles"] = coff.get("Dalles", 0) + area
        dd = dims.get(d["id"], {})
        as_m2 = float(dd.get("section_longitudinale_cm2_m", 2.0))
        aciers["Dallé (long.)"] = aciers.get("Dallé (long.)", 0) + as_m2 * area * 0.785
    # poutres : âtre hors dalle
    for b in st.get("poutres", []):
        L = math.dist(tuple(b["debut"]), tuple(b["fin"]))
        bw, bh = b["section"]
        bt = b.get("materiau", "beton_C25/30").replace("beton_", "") or "C25/30"
        betons[f"poutres {bt}"] = betons.get(f"poutres {bt}", 0) + bw * max(bh - slab_t, 0.05) * L
        coff["Poutres"] = coff.get("Poutres", 0) + (2 * max(bh - slab_t, 0.05) + bw) * L
        dd = dims.get(b["id"], {})
        n, dmm = _bars(dd.get("barres", ""))
        if n:
            aciers["Poutres (long.)"] = aciers.get("Poutres (long.)", 0) + n * BAR_MASS_KG_M2.get(dmm, 1.578) * (L + 0.9)
        aciers["Cadres (transv.)"] = aciers.get("Cadres (transv.)", 0) + _cadres_kgm(dd.get("cadres", "HA8 e=250")) * L
    # poteaux
    for c in st.get("poteaux", []):
        lv = c.get("niveaux", [0, niveaux - 1])
        H = (max(lv) - min(lv) + 1) * h
        w, hh = c["section"]
        bt = c.get("materiau", "beton_C25/30").replace("beton_", "") or "C25/30"
        betons[f"poteaux {bt}"] = betons.get(f"poteaux {bt}", 0) + w * hh * H
        coff["Poteaux"] = coff.get("Poteaux", 0) + 2 * (w + hh) * H
        dd = dims.get(c["id"], {})
        n, dmm = _bars(dd.get("barres", ""))
        if n:
            aciers["Poteaux (long.)"] = aciers.get("Poteaux (long.)", 0) + n * BAR_MASS_KG_M2.get(dmm, 1.578) * H
        aciers["Cadres (transv.)"] = aciers.get("Cadres (transv.)", 0) + _cadres_kgm(dd.get("cadres", "HA8 e=200")) * H
    # voiles
    for w_ in st.get("voiles", []):
        Lw = math.dist(tuple(w_["debut"]), tuple(w_["fin"]))
        t = float(w_.get("epaisseur", 0.2))
        lv = w_.get("niveaux", [0, niveaux - 1])
        H = (max(lv) - min(lv) + 1) * h
        bt = w_.get("materiau", "beton_C25/30").replace("beton_", "") or "C25/30"
        betons[f"voiles {bt}"] = betons.get(f"voiles {bt}", 0) + t * Lw * H
        coff["Voiles"] = coff.get("Voiles", 0) + 2 * Lw * H
        aciers["Voiles (min 0.2%×2)"] = aciers.get("Voiles (min 0.2%×2)", 0) + 0.004 * t * Lw * H * 7850
    # fondations
    for f in st.get("fondations", []):
        dims_ = f.get("dimensions", [1.5, 1.5, 0.4])
        B, L, H = (dims_ + [1.5, 1.5, 0.4])[:3]
        if f.get("type") == "radier":
            vol = B * L * H
        else:
            vol = B * L * H
        betons[f"fondations {f.get('type', '')}"] = betons.get(f"fondations {f.get('type','')}", 0) + vol
        if f.get("type") != "radier":
            coff["Fondations"] = coff.get("Fondations", 0) + 2 * (B + L) * H
        dd = dims.get(f["id"], {})
        as_m = float(dd.get("section_longitudinale_cm2_m", 5.0))
        aciers["Fondations (long.)"] = aciers.get("Fondations (long.)", 0) + as_m * 0.785 * (B + L)

    for k, v in betons.items():
        add("Béton", k, "m³", v)
    add("Béton", "TOTAL béton", "m³", sum(betons.values()))
    for k, v in aciers.items():
        add("Acier", k, "kg", v)
    add("Acier", "TOTAL acier", "kg", sum(aciers.values()))
    for k, v in coff.items():
        add("Coffrage", k, "m²", v)
    add("Coffrage", "TOTAL coffrage", "m²", sum(coff.values()))
    add("Repères", "Nombre de poteaux", "u", len(st.get("poteaux", [])))
    add("Repères", "Nombre de poutres", "u", len(st.get("poutres", [])))
    add("Repères", "Nombre de voiles", "u", len(st.get("voiles", [])))
    return rows


def _bars(notat: str):
    try:
        return int(notat.split("HA")[0]), int(notat.split("HA")[1])
    except Exception:
        return 0, 0


def _cadres_kgm(notation: str) -> float:
    try:
        d = int(notation.split("HA")[1].split()[0])
        e = float(notation.split("e=")[1])
    except Exception:
        return 2 * BAR_MASS_KG_M2[8] / 0.25
    return 2 * BAR_MASS_KG_M2.get(d, 0.395) / max(e / 1000.0, 0.05)


def export_csv(rows: list[dict], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=["Categorie", "Detail", "Unite", "Quantite"],
                           delimiter=";")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return path


def export_xlsx(rows: list[dict], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import pandas as pd
        df = pd.DataFrame(rows)
        df.to_excel(path, index=False)
    except Exception:
        # fallback : CSV renommé .xlsx non — on écrit un CSV à la place
        path = path.with_suffix(".csv")
        export_csv(rows, path)
    return path
