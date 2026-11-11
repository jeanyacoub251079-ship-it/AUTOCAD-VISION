"""Extraction géométrique du DXF AARKA (58 rue de l'Aigle) -> JSON tracé.

Sépare les 4 jeux de plans (S/Sol, Rdc, R+1, Combles) état actuel / projet
et les 6 coupes, puis relève : cotes, niveaux NGF, zones de démolition,
épaisseurs de murs, hauteurs sous plafond.
"""
from __future__ import annotations
import json, re, math, collections, os, sys
import ezdxf
from ezdxf import bbox as ezbbox

SRC = "google_drive/DCE_58 RUE DE L'AIGLE_LA GARENNE COLOMBES MODIF 05112026-export.dxf"
OUT = "affaires/GARENNE/00_SOURCES/geometrie_dxf.json"

# Origine verticale : NGF 41.46 = y DXF -7234.6 (Axe Niveau Rdc Interieur)
Y0 = -7234.6
NGF0 = 41.46
def ngf(y): return round(NGF0 + (y - Y0)/100.0, 3)
def cm(d): return round(d/100.0, 3)

CW = {  # nom court -> bbox (x0,x1,y0,y1) dans l'espace objet
  "P08a_SSOL":  (6100, 7600, -10620, -9650),
  "P08a_RDC":   (7800, 9250, -10620, -9650),
  "P08a_R1":    (9500, 11000, -9600, -8650),
  "P08a_COMBLES":(11600, 13100, -9600, -8650),
  "P08b_SSOL":  (41300, 42800, -10620, -9650),
  "P08b_RDC":   (42300, 46800, -11000, -9650),
  "P08b_R1":    (42300, 46800, -9600, -8650),
  "P08b_COMBLES":(42300, 46800, -9600, -8650),
}
COUPES = {
  "P09a": (12500, 14700, -8000, -6300),
  "P09b": (53300, 55600, -8000, -6300),
  "P10a": (41300, 42900, -6200, -4000),
  "P10b": (45500, 47800, -8200, -6800),
  "P11a": (20300, 22500, -8000, -6300),
  "P11b": (56300, 58600, -8200, -6700),
}

def inb(p, b, m=0):
    return b[0]-m <= p[0] <= b[1]+m and b[2]-m <= p[1] <= b[3]+m

def main():
    doc = ezdxf.readfile(SRC)
    msp = doc.modelspace()
    data = {
      "source": os.path.basename(SRC),
      "dxf_version": doc.dxfversion, "acad_release": doc.acad_release,
      "insunits": doc.header.get('$INSUNITS'),
      "unite_constat": "centimetres (INSUNITS=5) ; cotes annotées en cm, NGF en m",
      "origine_ngf": {"y_dxf": Y0, "ngf": NGF0, "libelle": "Axe Niveau Rdc Interieur / Point de Reference"},
      "entites_modele": len(msp),
      "calques": dict(collections.Counter(e.dxf.layer for e in msp).most_common()),
      "zones": {}, "coupes": {}, "demolitions": [], "niveaux_ngf": [],
    }

    # 1. Démolitions (hatch/polyligne du calque ARK-DEMOL)
    for e in msp.query('*[layer=="ARK-DEMOL"]'):
        if e.dxftype() not in ("HATCH", "LWPOLYLINE"): continue
        b = ezbbox.extents([e])
        if b.size.x < 10 or b.size.y < 10: continue
        data["demolitions"].append({
            "type": e.dxftype(), "x0": round(b.extmin.x,1), "y0": round(b.extmin.y,1),
            "x1": round(b.extmax.x,1), "y1": round(b.extmax.y,1),
            "largeur_cm": round(b.size.x,1), "longueur_cm": round(b.size.y,1)})

    # 2. NGF annotés
    for e in msp.query("MTEXT"):
        t = re.sub(r"\\[A-Za-z0-9.^;|]+", "", e.text.replace("\\P"," ")).strip()
        mm = re.search(r"Ngf\s*([0-9]+\.[0-9]+)", t, re.I)
        if mm:
            data["niveaux_ngf"].append({"ngf": float(mm.group(1)),
                "x": round(e.dxf.insert.x), "y": round(e.dxf.insert.y)})

    # 3. par zone : cotes, hauteurs sous plafond, epaisseurs de murs
    dims = list(msp.query("DIMENSION"))
    texts = [e for e in msp.query("MTEXT")]
    lines = list(msp.query("LINE"))
    for name, box in {**CW, **{k: v for k, v in COUPES.items()}} .items():
        dimlist = []
        for e in dims:
            p = e.dxf.defpoint2; p1 = e.dxf.defpoint
            if inb((p.x, p.y), box):
                ang = math.degrees(e.dxf.angle) % 180 if e.dxf.hasattr("angle") else 0
                dimlist.append({"m_cm": round(e.get_measurement(),1),
                                "angle": round(ang,1),
                                "x1": round(p1.x), "y1": round(p1.y),
                                "x2": round(p.x), "y2": round(p.y),
                                "ngf1": ngf(p1.y) if ang > 45 else None,
                                "ngf2": ngf(p.y) if ang > 45 else None})
        hsp = []
        for e in texts:
            t = re.sub(r"\\[A-Za-z0-9.^;|]+", "", e.text.replace("\\P"," ")).strip()
            t = re.sub(r"\s+", " ", t)
            if re.fullmatch(r"(HSP|H)\s?\d{3}", t) and inb((e.dxf.insert.x, e.dxf.insert.y), box):
                hsp.append({"txt": t, "x": round(e.dxf.insert.x), "y": round(e.dxf.insert.y)})
        # murs : lignes verticales/horizontales longues du calque ARK-MURS
        walls = []
        for e in lines:
            if e.dxf.layer != "ARK-MURS": continue
            s, t_ = e.dxf.start, e.dxf.end
            if not inb(((s.x+t_.x)/2, (s.y+t_.y)/2), box): continue
            dx, dy = abs(s.x-t_.x), abs(s.y-t_.y)
            if max(dx,dy) < 80: continue
            walls.append({"x0": round(s.x),"y0": round(s.y),"x1": round(t_.x),"y1": round(t_.y),
                          "L_cm": round(max(dx,dy),1), "sens": "V" if dy>dx else "H"})
        entry = {"bbox": box, "cotes": dimlist, "hauteurs": hsp, "murs": walls}
        if name.startswith("P08") or name.startswith("P09") or name.startswith("P10") or name.startswith("P11"):
            data["coupes" if name in COUPES else "zones"][name] = entry
        else:
            data["zones"][name] = entry

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print("ecrit", OUT, os.path.getsize(OUT), "octets")
    for k,v in data["zones"].items():
        print(f"  {k}: {len(v['cotes'])} cotes, {len(v['hauteurs'])} HSP, {len(v['murs'])} murs")
    for k,v in data["coupes"].items():
        print(f"  {k}: {len(v['cotes'])} cotes, {len(v['hauteurs'])} HSP")

if __name__ == "__main__":
    main()
