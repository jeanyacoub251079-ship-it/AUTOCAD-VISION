"""Génération des plans structurels DXF (§4.8, Lot 6).

Trois plans : fondations, coffrage, ferraillage — unités mm, DXF AC1027,
calques normalisés, cartouche (projet anonymisé, date, échelle), cotes.
"""
from __future__ import annotations

import math
from pathlib import Path

import ezdxf

from ..logging_setup import get_logger

log = get_logger("structai.export.dxf")

M2MM = 1000.0

LAYERS = {
    "FONDATIONS": 3, "POTEAUX": 4, "POUTRES": 5, "VOILES": 6, "DALLES": 2,
    "OUVERTURES": 1, "COTES": 7, "CARTOUCHE": 7, "ARMATURES_LONG": 5,
    "ARMATURES_TRANS": 3, "DETAILS": 6, "NOTES": 7,
}


def _doc():
    doc = ezdxf.new("R2013", setup=True)
    for name, color in LAYERS.items():
        if name not in doc.layers:
            doc.layers.add(name, color=color)
    return doc


def _rect(msp, x, y, w, h, layer, lw=0.35):
    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]
    msp.add_lwpolyline([(p[0], p[1]) for p in pts], dxfattribs={"layer": layer,
                                                                 "const_width": lw * 1000})


def _txt(msp, s, x, y, h=100.0, layer="COTES", align="LEFT"):
    from ezdxf.enums import TextEntityAlignment
    msp.add_text(s, dxfattribs={"layer": layer, "height": h}) \
       .set_placement((x, y), align=TextEntityAlignment[align])


def _cartouche(msp, x0, y0, infos: dict):
    W, H = 7000.0, 2400.0
    _rect(msp, x0, y0, W, H, "CARTOUCHE", 0.5)
    msp.add_line((x0, y0 + H * 0.66), (x0 + W, y0 + H * 0.66), dxfattribs={"layer": "CARTOUCHE"})
    msp.add_line((x0, y0 + H * 0.33), (x0 + W, y0 + H * 0.33), dxfattribs={"layer": "CARTOUCHE"})
    _txt(msp, "STRUCTAI — PROPOSITION À VALIDER PAR L'INGÉNIEUR", x0 + 150, y0 + H - 300,
         160, "CARTOUCHE")
    _txt(msp, infos.get("projet", ""), x0 + 150, y0 + H * 0.66 - 300, 130, "CARTOUCHE")
    _txt(msp, infos.get("plan", ""), x0 + 150, y0 + H * 0.33 - 300, 130, "CARTOUCHE")
    _txt(msp, infos.get("date", ""), x0 + W - 150, y0 + H - 300, 110, "CARTOUCHE", "RIGHT")
    _txt(msp, infos.get("echelle", "Échelle 1:100 (unités mm)"), x0 + W - 150,
         y0 + H * 0.66 - 300, 110, "CARTOUCHE", "RIGHT")
    _txt(msp, infos.get("option", ""), x0 + W - 150, y0 + H * 0.33 - 300, 110,
         "CARTOUCHE", "RIGHT")


def _cotes(msp, pts, y_base):
    for a in pts:
        msp.add_line(a[:2] + (0,), (a[0], y_base, 0), dxfattribs={"layer": "COTES"})
    ordered = sorted(pts, key=lambda p: p[0])
    for i in range(len(ordered) - 1):
        x1, x2 = ordered[i][0], ordered[i + 1][0]
        dim = msp.add_linear_dim(base=(y_base, y_base - 900), p1=(x1, y_base, 0),
                                 p2=(x2, y_base, 0),
                                 override={"dimtxt": 100, "dimasz": 80, "dimexe": 60},
                                 dxfattribs={"layer": "COTES"})
        dim.render()


# ---------------------------------------------------------------------------

def plan_fondations(option: dict, emprise: dict, out_path: Path, infos: dict) -> Path:
    doc = _doc()
    msp = doc.modelspace()
    st = option["structure"]
    for c in st.get("poteaux", []):
        x, y = c["position"][0] * M2MM, c["position"][1] * M2MM
        _rect(msp, x - 150, y - 150, 300, 300, "POTEAUX", 0.3)
    for f in st.get("fondations", []):
        B, L, H = (f["dimensions"] + [1.5, 1.5, 0.4])[:3]
        cid = f.get("poteau")
        pos = None
        for c in st.get("poteaux", []):
            if c["id"] == cid:
                pos = c["position"]
                break
        if pos is None:
            # radier
            if f.get("type") == "radier":
                x0 = emprise["x0"] * M2MM - 300
                y0 = emprise["y0"] * M2MM - 300
                _rect(msp, x0, y0, (emprise["x1"] - emprise["x0"]) * M2MM + 600,
                      (emprise["y1"] - emprise["y0"]) * M2MM + 600, "FONDATIONS", 0.5)
                _txt(msp, f"RADIER ep={H*100:.0f} cm", x0 + 200, y0 + 200, 120, "NOTES")
            continue
        x, y = pos[0] * M2MM, pos[1] * M2MM
        _rect(msp, x - B * M2MM / 2, y - L * M2MM / 2, B * M2MM, L * M2MM,
              "FONDATIONS", 0.5)
        _txt(msp, f"{f['id']} {B*100:.0f}×{L*100:.0f}×{H*100:.0f}", x + B * 500 + 100,
             y - 60, 90, "NOTES")
    for w in st.get("voiles", []):
        (x1, y1), (x2, y2) = w["debut"], w["fin"]
        msp.add_lwpolyline([(x1 * M2MM, y1 * M2MM), (x2 * M2MM, y2 * M2MM)],
                           dxfattribs={"layer": "VOILES", "const_width": w["epaisseur"] * M2MM})
    xs = sorted({c["position"][0] * M2MM for c in st.get("poteaux", [])})
    if xs:
        _cotes(msp, [(x, emprise["y0"] * M2MM - 1500, 0) for x in xs],
               emprise["y0"] * M2MM - 1500)
    _cartouche(msp, emprise["x1"] * M2MM + 1000, emprise["y0"] * M2MM - 3000,
               {**infos, "plan": "PLAN DE FONDATIONS"})
    doc.saveas(str(out_path))
    return out_path


def plan_coffrage(option: dict, emprise: dict, out_path: Path, infos: dict) -> Path:
    doc = _doc()
    msp = doc.modelspace()
    st = option["structure"]
    for d in st.get("dalles", []):
        poly = [(p[0] * M2MM, p[1] * M2MM) for p in d.get("polygone", [])]
        if len(poly) >= 3:
            msp.add_lwpolyline(poly + [poly[0]], close=True,
                               dxfattribs={"layer": "DALLES"})
            cx = sum(p[0] for p in poly) / len(poly)
            cy = sum(p[1] for p in poly) / len(poly)
            _txt(msp, f"ep {d.get('epaisseur', 0.2)*100:.0f} cm", cx - 400, cy, 90, "DALLES")
            # sens de portée : flèche horizontale si dalle portée dans le sens court
            xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
            if (max(xs) - min(xs)) <= (max(ys) - min(ys)):
                msp.add_line((min(xs) + 200, cy), (max(xs) - 200, cy),
                             dxfattribs={"layer": "DALLES"})
    for b in st.get("poutres", []):
        (x1, y1), (x2, y2) = b["debut"], b["fin"]
        b_w = b["section"][0] * M2MM
        msp.add_lwpolyline([(x1 * M2MM, y1 * M2MM), (x2 * M2MM, y2 * M2MM)],
                           dxfattribs={"layer": "POUTRES", "const_width": b_w, "lineweight": 60})
        cx, cy = (x1 + x2) / 2 * M2MM, (y1 + y2) / 2 * M2MM
        _txt(msp, f"{b['id']} {b['section'][0]*100:.0f}×{b['section'][1]*100:.0f}",
             cx - 500, cy + 150, 80, "NOTES")
    for c in st.get("poteaux", []):
        x, y = c["position"][0] * M2MM, c["position"][1] * M2MM
        w, h = c["section"]
        _rect(msp, x - w * M2MM / 2, y - h * M2MM / 2, w * M2MM, h * M2MM, "POTEAUX", 0.5)
    for w in st.get("voiles", []):
        (x1, y1), (x2, y2) = w["debut"], w["fin"]
        msp.add_lwpolyline([(x1 * M2MM, y1 * M2MM), (x2 * M2MM, y2 * M2MM)],
                           dxfattribs={"layer": "VOILES", "const_width": w["epaisseur"] * M2MM})
    _cartouche(msp, emprise["x1"] * M2MM + 1000, emprise["y0"] * M2MM - 3000,
               {**infos, "plan": "PLAN DE COFFRAGE"})
    doc.saveas(str(out_path))
    return out_path


def plan_ferraillage(option: dict, emprise: dict, out_path: Path, infos: dict) -> Path:
    doc = _doc()
    msp = doc.modelspace()
    st = option["structure"]
    dims = option.get("resultats_calcul", {}).get("dimensionnement_armatures", {})
    for b in st.get("poutres", []):
        (x1, y1), (x2, y2) = b["debut"], b["fin"]
        d = dims.get(b["id"], {})
        txt = f"{b['id']}: {d.get('barres', '?')} + cadres {d.get('cadres', '?')}"
        cx, cy = (x1 + x2) / 2 * M2MM, (y1 + y2) / 2 * M2MM
        _txt(msp, txt, cx - 900, cy - 60, 80, "ARMATURES_LONG")
        msp.add_line((x1 * M2MM, y1 * M2MM - 60), (x2 * M2MM, y2 * M2MM - 60),
                     dxfattribs={"layer": "ARMATURES_LONG"})
    for c in st.get("poteaux", []):
        x, y = c["position"][0] * M2MM, c["position"][1] * M2MM
        d = dims.get(c["id"], {})
        _txt(msp, f"{c['id']}: {d.get('barres', '?')} / {d.get('cadres', '?')}",
             x + 250, y - 40, 80, "ARMATURES_LONG")
        w, h = c["section"]
        _rect(msp, x - w * 500 + 50, y - h * 500 + 50, w * M2MM - 100, h * M2MM - 100,
              "ARMATURES_TRANS", 0.25)
        n, _ = _bars(d.get("barres", "4HA12"))
        for i in range(n):
            ang = math.pi / 4 + i * 2 * math.pi / max(n, 1)
            px = x + math.cos(ang) * (w * M2MM / 2 - 200)
            py = y + math.sin(ang) * (h * M2MM / 2 - 200)
            msp.add_circle((px, py), 40, dxfattribs={"layer": "ARMATURES_LONG"})
    for d in st.get("dalles", []):
        poly = [(p[0] * M2MM, p[1] * M2MM) for p in d.get("polygone", [])]
        if len(poly) >= 3:
            cx = sum(p[0] for p in poly) / len(poly)
            cy = sum(p[1] for p in poly) / len(poly)
            dd = dims.get(d["id"], {})
            _txt(msp, f"{d['id']}: {dd.get('barres', '?')} e={dd.get('espacement_cm', 20):.0f}cm",
                 cx - 800, cy + 250, 80, "ARMATURES_LONG")
    # détail type poteau
    _txt(msp, "DÉTAIL TYPE — POTEAU : noyau béton, cadres attachés, recouvrement "
              "1.5·lb hors zone critique (EC8 5.4.1)",
         emprise["x0"] * M2MM, emprise["y1"] * M2MM + 1200, 110, "DETAILS")
    _cartouche(msp, emprise["x1"] * M2MM + 1000, emprise["y0"] * M2MM - 3000,
               {**infos, "plan": "PLAN DE FERRAILLAGE (synthèse)"})
    doc.saveas(str(out_path))
    return out_path


def _bars(notat: str) -> tuple[int, int]:
    try:
        return int(notat.split("HA")[0]), int(notat.split("HA")[1])
    except Exception:
        return 0, 0
