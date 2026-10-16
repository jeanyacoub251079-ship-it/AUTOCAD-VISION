"""Parsing DXF local (§2.4.4) + filet de sécurité anonymisation (§5.4).

- Lecture via `ezdxf` ; extraction des entités par calque (lignes, polylignes,
  arcs, cercles, splines, blocs INSÉRÉS, textes, cotes).
- Détection d'unités via $INSUNITS + heuristique de cotes.
- Rendus PNG 300 DPI : original et « nettoyé » (destiné à l'IA de vision).
- Contrôles d'anonymisation à l'import : textes suspects, images, cartouche,
  nom de fichier. Alertes NON bloquantes (sauf « mode strict »).

Aucun envoi réseau dans ce module.
"""
from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any, Optional

import ezdxf
from ezdxf.math import Vec3

from ..logging_setup import get_logger
from ..util import read_json, sha256_bytes, sha256_file, write_json

log = get_logger("structai.parsing")

# --- conversion unités DXF -> mètres --------------------------------------
INSUNITS_TO_M = {1: 0.0254, 2: 0.3048, 4: 0.001, 5: 0.01, 6: 1.0, 7: 1000.0, 10: 0.9144}
INSUNITS_NAMES = {1: "inch", 2: "foot", 4: "mm", 5: "cm", 6: "m", 7: "km", 10: "yard"}

ANNOTATION_TYPES = {"TEXT", "MTEXT", "ATTDEF", "ATTRIB", "DIMENSION", "LEADER",
                    "MULTILEADER", "PROXY_GRAPHIC", "WIPENTITY"}
IMAGE_TYPES = {"IMAGE", "OLE2FRAME", "WIPEOUT"}
GEOM_TYPES = {"LINE", "LWPOLYLINE", "POLYLINE", "ARC", "CIRCLE", "SPLINE",
              "ELLIPSE", "INSERT", "HATCH", "SOLID", "3DFACE"}

# Motifs de données identifiantes (contrôle secondaire — le nettoyage amont
# est de la responsabilité de l'utilisateur, §5.3).
SUSPICIOUS_KEYWORDS = [
    "maître d'ouvrage", "maitre d'ouvrage", "maitre d’ouvrage", "moa",
    "architecte", "client", "sarl", "sci", "sas", "eurl", "sasu", "auto-entrepreneur",
    "tel :", "tél :", "tel.", "fax", "@", "mail", "e-mail", "courriel",
    "permis de construire", "pc n°", "parcelle", "section cadastral", "cadastr",
    "proprietaire", "propriétaire", "adresse", "nom du projet",
]
POSTCODE_RE = re.compile(r"\b\d{5}\b")
PHONE_RE = re.compile(r"\b(?:\+33|0)\s?[1-9](?:[\s.-]?\d{2}){4}\b")

MAX_ENTITIES_PER_LAYER_JSON = 5000
FLATTEN_SEGMENTS = 24


class DXFImportError(Exception):
    pass


# ---------------------------------------------------------------------------
# Import + validation
# ---------------------------------------------------------------------------

def validate_and_copy(src_path: Path, dest_dir: Path, max_size: int) -> dict:
    """Vérifie l'extension/taille/version, copie sous nom horodaté + hash."""
    name = src_path.name
    if src_path.suffix.lower() != ".dxf":
        raise DXFImportError("Fichier non-DXF : seul le format .dxf est accepté en V1.")
    size = src_path.stat().st_size
    if size == 0:
        raise DXFImportError("Fichier vide ou corrompu (taille nulle).")
    if size > max_size:
        raise DXFImportError(f"Fichier trop volumineux ({size} o > {max_size} o) — nettoyez le plan.")
    dest_dir.mkdir(parents=True, exist_ok=True)
    try:
        doc = ezdxf.readfile(str(src_path))
    except ezdxf.DXFError as exc:
        raise DXFImportError(f"DXF illisible/corrompu : {exc}") from exc
    version = doc.dxfversion  # e.g. AC1032
    dest = dest_dir / f"import_{name}"
    data = src_path.read_bytes()
    h = sha256_bytes(data)
    if not dest.exists():
        dest.write_bytes(data)
    return {
        "filename": name, "path": str(dest), "size": size,
        "sha256": h, "dxf_version": version,
    }


def check_filename_suspicious(name: str) -> Optional[str]:
    base = re.sub(r"\.dxf$", "", name or "", flags=re.I).lower()
    for kw in ("client", "maître", "maitre", "nom", "adresse", "chantier"):
        if kw in base and not re.match(r"^[a-z0-9._-]+$", base):
            return f"nom de fichier contenant le mot-clé « {kw} »"
    if POSTCODE_RE.search(base):
        return "nom de fichier contenant un code postal"
    return None


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

def _entity_to_json(e, out: list) -> None:
    t = e.dxftype()
    try:
        if t == "LINE":
            out.append({"type": "LINE",
                        "debut": [round(e.dxf.start.x, 3), round(e.dxf.start.y, 3)],
                        "fin": [round(e.dxf.end.x, 3), round(e.dxf.end.y, 3)]})
        elif t == "LWPOLYLINE":
            pts = [(p[0], p[1]) for p in e.get_points("xy")]
            if pts:
                out.append({"type": "POLYLINE",
                            "points": [[round(x, 3), round(y, 3)] for x, y in pts],
                            "closed": bool(e.closed)})
        elif t == "POLYLINE":
            pts = [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]
            if pts:
                out.append({"type": "POLYLINE",
                            "points": [[round(x, 3), round(y, 3)] for x, y in pts],
                            "closed": bool(e.is_closed)})
        elif t == "ARC":
            out.append({"type": "ARC", "cercle": [round(e.dxf.center.x, 3), round(e.dxf.center.y, 3)],
                        "rayon": round(e.dxf.radius, 3),
                        "debut_deg": round(e.dxf.start_angle, 2), "fin_deg": round(e.dxf.end_angle, 2)})
        elif t == "CIRCLE":
            out.append({"type": "CIRCLE", "cercle": [round(e.dxf.center.x, 3), round(e.dxf.center.y, 3)],
                        "rayon": round(e.dxf.radius, 3)})
        elif t in ("SPLINE", "ELLIPSE"):
            from ezdxf.path import from_entity
            path = from_entity(e)
            pts = [(v.x, v.y) for v in path.flattening(diameter=max(abs(e.dxf.start_point.x - e.dxf.end_point.x) if hasattr(e.dxf, "start_point") else 1.0, 1.0) / FLATTEN_SEGMENTS)] \
                if t == "SPLINE" else [(v.x, v.y) for v in path.flattening(0.05)]
            if pts:
                out.append({"type": "POLYLINE", "points": [[round(x, 3), round(y, 3)] for x, y in pts],
                            "closed": bool(getattr(e, "closed", False))})
        elif t == "INSERT":
            for sub in e.virtual_entities():
                if sub.dxftype() in GEOM_TYPES and sub.dxf.layer == e.dxf.layer:
                    _entity_to_json(sub, out)
        elif t in ("HATCH", "SOLID", "3DFACE"):
            from ezdxf.path import from_entity
            try:
                path = from_entity(e)
                pts = [(v.x, v.y) for v in path.flattening(10)]
                if pts:
                    out.append({"type": "POLYLINE",
                                "points": [[round(x, 3), round(y, 3)] for x, y in pts], "closed": True})
            except Exception:
                pass
    except Exception as exc:  # tolérant : on saute l'entité, pas le plan
        log.debug("entité %s ignorée: %s", t, exc)


def parse_dxf(path: Path, units_override: Optional[str] = None) -> dict:
    """Extraction brute des entités par calque (§4.2). Retourne le dictionnaire
    `parsed` (entités + méta + contrôles d'anonymisation)."""
    doc = ezdxf.readfile(str(path))
    msp = doc.modelspace()

    layers: dict[str, dict[str, Any]] = {}
    texts: list[dict] = []
    dims: list[dict] = []
    image_entities = 0
    total = 0
    minx = miny = math.inf
    maxx = maxy = -math.inf

    for e in msp:
        total += 1
        t = e.dxftype()
        layer = getattr(e.dxf, "layer", "0") or "0"
        try:
            color = int(getattr(e.dxf, "color", 256))
        except Exception:
            color = 256
        lay = layers.setdefault(layer, {"nom": layer, "couleur": color,
                                        "nombre_entites": 0, "entites": []})
        lay["nombre_entites"] += 1

        if t in ("TEXT", "MTEXT", "ATTRIB", "ATTDEF"):
            content = e.text if hasattr(e, "text") else str(getattr(e.dxf, "text", ""))
            content = re.sub(r"\s+", " ", content or "").strip()
            if not content:
                continue
            pos = _safe_insert(e)
            texts.append({"contenu": content[:400],
                          "position": [round(pos.x, 2), round(pos.y, 2)] if pos else None,
                          "hauteur": round(float(getattr(e.dxf, "height", 0) or 0), 2),
                          "calque": layer})
            _bump_bbox(minx, miny, maxx, maxy, pos)
            if pos:
                minx, miny, maxx, maxy = min(minx, pos.x), min(miny, pos.y), max(maxx, pos.x), max(maxy, pos.y)
            continue
        if t == "DIMENSION":
            try:
                measurement = float(e.get_measurement())
            except Exception:
                measurement = -1.0
            dims.append({"type": t, "mesure": round(measurement, 3), "calque": layer})
            continue
        if t in IMAGE_TYPES:
            image_entities += 1
            continue
        if len(lay["entites"]) < MAX_ENTITIES_PER_LAYER_JSON:
            _entity_to_json(e, lay["entites"])
        pts = _entity_bbox_points(e)
        for p in pts:
            minx, miny = min(minx, p[0]), min(miny, p[1])
            maxx, maxy = max(maxx, p[0]), max(maxy, p[1])

    if math.isinf(minx):
        raise DXFImportError("Plan vide : aucune géométrie exploitable détectée.")

    units, units_note = _detect_units(doc, dims, (minx, miny, maxx, maxy), units_override)
    blocks = []
    for block in doc.blocks:
        if block.name.startswith("*"):
            continue
        blocks.append({"nom": block.name, "entites": len(block)})

    parsed = {
        "fichier": {
            "nom": path.name,
            "version_dxf": doc.dxfversion,
        },
        "unites": units,
        "unites_note": units_note,
        "unit_to_m": INSUNITS_TO_M.get({"mm": 4, "cm": 5, "m": 6}.get(units, 4), 0.001),
        "emprise": {"min": [round(minx, 2), round(miny, 2)], "max": [round(maxx, 2), round(maxy, 2)]},
        "nombre_total_entites": total,
        "calques": [
            {"nom": v["nom"], "couleur": v["couleur"], "nombre_entites": v["nombre_entites"],
             "entites": v["entites"], "truncated": v["nombre_entites"] > len(v["entites"])}
            for v in sorted(layers.values(), key=lambda x: -x["nombre_entites"])
        ],
        "blocs": blocks,
        "textes": texts,
        "cotes": dims,
        "images": image_entities,
    }
    parsed["anonymisation"] = anonymization_scan(parsed)
    return parsed


def _safe_insert(e) -> Vec3:
    try:
        return Vec3(e.dxf.insert)
    except Exception:
        try:
            return Vec3(e.dxf.location)
        except Exception:
            return None


def _bump_bbox(*_a):  # pragma: no cover (placeholder, bbox géré inline)
    return None


def _entity_bbox_points(e) -> list[tuple[float, float]]:
    t = e.dxftype()
    try:
        if t == "LINE":
            return [(e.dxf.start.x, e.dxf.start.y), (e.dxf.end.x, e.dxf.end.y)]
        if t == "LWPOLYLINE":
            return [(p[0], p[1]) for p in e.get_points("xy")]
        if t == "POLYLINE":
            return [(v.dxf.location.x, v.dxf.location.y) for v in e.vertices]
        if t in ("ARC", "CIRCLE"):
            cx, cy, r = e.dxf.center.x, e.dxf.center.y, e.dxf.radius
            return [(cx - r, cy - r), (cx + r, cy + r)]
        if t == "INSERT":
            try:
                ip = e.dxf.insert
                return [(ip.x, ip.y)]
            except Exception:
                return []
        from ezdxf.path import from_entity
        path = from_entity(e)
        bb = path.bbox()
        return [(bb.extmin.x, bb.extmin.y), (bb.extmax.x, bb.extmax.y)]
    except Exception:
        return []


def _detect_units(doc, dims, bbox, override) -> tuple[str, str]:
    if override:
        return override, "saisie utilisateur"
    insunits = int(doc.header.get("$INSUNITS", 0) or 0)
    if insunits in INSUNITS_NAMES:
        return INSUNITS_NAMES[insunits], f"$INSUNITS={insunits}"
    # heuristique : taille du dessin vs ordre de grandeur d'un plan d'archi
    w = abs(bbox[2] - bbox[0])
    if w > 4000:
        return "mm", "heuristique emprise (très grandes coordonnées)"
    if w > 400:
        return "cm", "heuristique emprise"
    if w > 4:
        return "m", "heuristique emprise"
    return "mm", "défaut — à confirmer"


# ---------------------------------------------------------------------------
# Filet de sécurité anonymisation (§5.4)
# ---------------------------------------------------------------------------

def anonymization_scan(parsed: dict) -> dict:
    alerts: list[dict] = []
    texts = parsed.get("textes", [])
    suspects = []
    for t in texts:
        low = (t.get("contenu") or "").lower()
        hits = [kw for kw in SUSPICIOUS_KEYWORDS if kw in low]
        if POSTCODE_RE.search(low) and any(ch.isdigit() for ch in low):
            # un code postal isolé dans une zone de texte hors cote
            pass
        if hits:
            suspects.append({"contenu": t["contenu"][:120], "motifs": hits,
                             "position": t.get("position"), "calque": t.get("calque")})
    postcode_hits = [t for t in texts
                     if POSTCODE_RE.search(t.get("contenu", "")) or PHONE_RE.search(t.get("contenu", ""))]
    if suspects:
        alerts.append({"type": "texte_suspect",
                       "message": f"{len(suspects)} texte(s) contenant un mot-clé identifiant potentiel.",
                       "exemples": suspects[:10]})
    if postcode_hits:
        alerts.append({"type": "texte_suspect",
                       "message": f"{len(postcode_hits)} texte(s) au format code postal / téléphone.",
                       "exemples": [t["contenu"][:80] for t in postcode_hits[:10]]})
    if parsed.get("images", 0):
        alerts.append({"type": "image",
                       "message": f"{parsed['images']} entité(s) IMAGE/OLE détectée(s) — logos possibles à supprimer."})
    tb = _detect_title_block(parsed)
    if tb:
        alerts.append({"type": "cartouche",
                       "message": "Cartouche probable détecté en bas à droite (zone à exclure du rendu).",
                       "zone": tb})
    fname_alert = parsed.get("_filename_check")
    if fname_alert:
        alerts.append({"type": "nom_fichier", "message": fname_alert})
    return {"alertes": alerts, "nb_alertes": len(alerts), "strict": False}


def _detect_title_block(parsed: dict) -> Optional[dict]:
    """Heuristique simple : ≥5 textes concentrés dans le quart bas-droit."""
    minx, miny = parsed["emprise"]["min"]
    maxx, maxy = parsed["emprise"]["max"]
    w, h = maxx - minx, maxy - miny
    if w <= 0 or h <= 0:
        return None
    x0, y1 = maxx - 0.35 * w, miny + 0.25 * h
    n = 0
    for t in parsed.get("textes", []):
        p = t.get("position")
        if p and p[0] >= x0 and p[1] <= y1:
            n += 1
    if n >= 5:
        return {"min": [round(x0, 1), round(miny, 1)], "max": [round(maxx, 1), round(y1, 1)], "textes": n}
    return None


# ---------------------------------------------------------------------------
# Rendus PNG (§3.5) — ezdxf + matplotlib (backend Agg)
# ---------------------------------------------------------------------------

def render_png(parsed: dict, out_path: Path, clean: bool = False,
               excluded_layers: Optional[set] = None, dpi: int = 300,
               max_px: int = 3800) -> Path:
    """Rendu 2D du plan. `clean=True` exclut annotations, cartouche et calques
    décochés -> c'est CETTE image qui est destinée à l'IA de vision."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    try:
        from ezdxf.colors import aci2rgb_float
    except ImportError:  # ezdxf >= 1.x : aci2rgb renvoie 0-255
        from ezdxf.colors import aci2rgb as _aci2rgb

        def aci2rgb_float(index: int):
            return tuple(c / 255.0 for c in _aci2rgb(int(index))[:3])

    excluded = set(excluded_layers or set())
    tb = None
    if clean:
        tb = _detect_title_block(parsed)

    fig = plt.figure(figsize=(12, 12), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_axis_off()

    def inside_tb(p) -> bool:
        if not tb:
            return False
        return tb["min"][0] <= p[0] <= tb["max"][0] and tb["min"][1] <= p[1] <= tb["max"][1]

    def draw_poly(xs, ys, color, lw=0.6):
        try:
            c = aci2rgb_float(int(color)) if isinstance(color, int) and 0 < color < 257 else (0, 0, 0)
        except Exception:
            c = (0, 0, 0)
        ax.plot(xs, ys, color=c, linewidth=lw, solid_capstyle="round")

    for lay in parsed.get("calques", []):
        if lay["nom"] in excluded:
            continue
        col = lay.get("couleur", 7)
        for ent in lay["entites"]:
            t = ent["type"]
            if t == "LINE":
                (x1, y1), (x2, y2) = ent["debut"], ent["fin"]
                if clean and (inside_tb(ent["debut"]) and inside_tb(ent["fin"])):
                    continue
                draw_poly([x1, x2], [y1, y2], col)
            elif t == "POLYLINE":
                pts = ent["points"]
                if clean and pts and all(inside_tb(p) for p in pts):
                    continue
                if ent.get("closed"):
                    pts = pts + [pts[0]]
                draw_poly([p[0] for p in pts], [p[1] for p in pts], col)
            elif t in ("ARC", "CIRCLE"):
                cx, cy = ent["cercle"]
                r = ent["rayon"]
                a0 = math.radians(ent.get("debut_deg", 0))
                a1 = math.radians(ent.get("fin_deg", 360))
                if a1 < a0:
                    a1 += 2 * math.pi
                n = max(12, int((a1 - a0) / (2 * math.pi) * 72))
                ths = [a0 + (a1 - a0) * i / n for i in range(n + 1)]
                draw_poly([cx + r * math.cos(t) for t in ths],
                          [cy + r * math.sin(t) for t in ths], col)

    if not clean:  # annotations affichées sur le rendu original
        for t in parsed.get("textes", []):
            p = t.get("position")
            if not p:
                continue
            h = t.get("hauteur") or 0
            try:
                ax.annotate(t["contenu"][:60], xy=(p[0], p[1]), fontsize=3.5 + min(9, h / 40),
                            color=(0.15, 0.15, 0.15), rotation=0, va="bottom", ha="left",
                            annotation_clip=True)
            except Exception:
                pass

    # cadrage sur l'emprise
    minx, miny = parsed["emprise"]["min"]
    maxx, maxy = parsed["emprise"]["max"]
    margin = 0.03 * max(maxx - minx, maxy - miny, 1.0)
    ax.set_xlim(minx - margin, maxx + margin)
    ax.set_ylim(miny - margin, maxy + margin)
    ax.set_aspect("equal", adjustable="box")
    fig.set_size_inches(*(min(16, 8 + (maxx - minx) / max(1.0, maxy - miny) * 4), 8))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_path), dpi=dpi, facecolor="white")
    plt.close(fig)

    # re-dimensionne si trop gros (garde-fou mémoire)
    try:
        from PIL import Image
        with Image.open(out_path) as im:
            w, h = im.size
            if max(w, h) > max_px:
                k = max_px / max(w, h)
                im2 = im.resize((int(w * k), int(h * k)))
                im2.save(out_path)
    except Exception:
        pass
    return out_path


def extract_plain_texts_for_review(parsed: dict) -> list[str]:
    """Liste des textes visibles dans l'image -> affichée à l'utilisateur
    avant tout envoi IA (§5.4.3)."""
    return [t["contenu"] for t in parsed.get("textes", []) if t.get("contenu")]


# ---------------------------------------------------------------------------
# Persistance
# ---------------------------------------------------------------------------

def save_parsed(parsed: dict, plan_dir: Path) -> Path:
    path = plan_dir / "parsed.json"
    write_json(path, parsed)
    return path


def load_parsed(plan_dir: Path) -> Optional[dict]:
    return read_json(plan_dir / "parsed.json")
