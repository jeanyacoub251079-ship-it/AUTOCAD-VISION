#!/usr/bin/env python3
from __future__ import annotations

import base64
import html
import json
import threading
import urllib.parse
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from loguru import logger


TYPE_COLORS = {
    "WALL": "#e74c3c",
    "COLUMN": "#f39c12",
    "SLAB": "#3498db",
    "BEAM": "#27ae60",
    "TREMIE": "#9b59b6",
    "RESERVATION": "#1abc9c",
    "FURNITURE": "#95a5a6",
    "ANNOTATION": "#bdc3c7",
    "UNKNOWN": "#e67e22",
}
STRUCT_TYPES = list(TYPE_COLORS.keys())


def _now_iso() -> str:
    return datetime.now().isoformat()


def _safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except Exception:
        return default


def _default_output_path(input_path: Path) -> Path:
    stem = input_path.stem
    if stem.endswith("_classified"):
        stem = stem[: -len("_classified")]
    elif stem.endswith("classified"):
        stem = stem[: -len("classified")].rstrip("_- ")
    return input_path.with_name(f"{stem}_reviewed.geojson")


class ReviewSession:
    def __init__(self, input_path: Path, output_path: Optional[Path] = None, review_user: str = "operator"):
        self.input_path = input_path
        self.output_path = output_path or _default_output_path(input_path)
        self.review_user = review_user or "operator"
        self._lock = threading.Lock()

        payload = json.loads(input_path.read_text(encoding="utf-8"))
        if payload.get("type") != "FeatureCollection":
            raise ValueError(f"Invalid FeatureCollection: {input_path}")

        self.payload = payload
        self.metadata = dict(payload.get("metadata") or {})
        self.features = list(payload.get("features") or [])

        self._ensure_feature_ids()
        self.by_id: Dict[str, dict] = {str(feat.get("id", "")): feat for feat in self.features}
        self.review_scope_ids, self.review_scope_mode = self._initialize_review_scope()

    def _ensure_feature_ids(self) -> None:
        for idx, feat in enumerate(self.features, start=1):
            props = feat.setdefault("properties", {})
            fid = str(feat.get("id") or props.get("id") or f"ENT-{idx:05d}")
            feat["id"] = fid
            props["id"] = fid

    def _initialize_review_scope(self) -> tuple[set[str], str]:
        scope: set[str] = set()
        for feat in self.features:
            fid = str(feat.get("id", ""))
            props = feat.get("properties", {}) or {}
            clf = props.get("classification", {}) or {}
            history = props.get("review_history", []) or []

            if clf.get("needs_review", False) or clf.get("method") == "human_review" or history:
                scope.add(fid)

        if scope:
            return scope, "review_candidates"

        return {str(feat.get("id", "")) for feat in self.features}, "all_loaded_fallback"

    def _coords(self, geom: dict) -> List[Tuple[float, float]]:
        result: List[Tuple[float, float]] = []

        def walk(obj: Any) -> None:
            if obj is None:
                return
            if isinstance(obj, (list, tuple)):
                if len(obj) >= 2 and all(isinstance(v, (int, float)) for v in obj[:2]):
                    result.append((float(obj[0]), float(obj[1])))
                else:
                    for item in obj:
                        walk(item)

        gtype = (geom or {}).get("type", "")
        if gtype == "GeometryCollection":
            for sub in (geom or {}).get("geometries", []):
                result.extend(self._coords(sub))
            return result

        walk((geom or {}).get("coordinates"))
        return result

    def _ring_path(self, ring: list, tx, ty) -> str:
        if not ring:
            return ""
        d = f"M {tx(ring[0][0]):.1f} {ty(ring[0][1]):.1f}"
        for p in ring[1:]:
            d += f" L {tx(p[0]):.1f} {ty(p[1]):.1f}"
        return d + " Z"

    def _line_path(self, line: list, tx, ty) -> str:
        if not line:
            return ""
        d = f"M {tx(line[0][0]):.1f} {ty(line[0][1]):.1f}"
        for p in line[1:]:
            d += f" L {tx(p[0]):.1f} {ty(p[1]):.1f}"
        return d

    def _point_path(self, coords: list, tx, ty, radius: float = 3.0) -> str:
        if len(coords) < 2:
            return ""
        x, y = tx(coords[0]), ty(coords[1])
        return (
            f"M {x-radius:.1f} {y:.1f} "
            f"a {radius:.1f} {radius:.1f} 0 1 0 {2*radius:.1f} 0 "
            f"a {radius:.1f} {radius:.1f} 0 1 0 {-2*radius:.1f} 0"
        )

    def _geom_to_path(self, geom: dict, tx, ty) -> str:
        gtype = (geom or {}).get("type", "")
        coords = (geom or {}).get("coordinates", [])

        if not coords and gtype != "GeometryCollection":
            return ""

        if gtype == "Polygon":
            parts = [self._ring_path(coords[0], tx, ty)]
            for hole in coords[1:]:
                parts.append(self._ring_path(hole, tx, ty))
            return " ".join(p for p in parts if p)

        if gtype == "MultiPolygon":
            parts = []
            for poly in coords:
                if not poly:
                    continue
                parts.append(self._ring_path(poly[0], tx, ty))
                for hole in poly[1:]:
                    parts.append(self._ring_path(hole, tx, ty))
            return " ".join(p for p in parts if p)

        if gtype == "LineString":
            return self._line_path(coords, tx, ty)

        if gtype == "MultiLineString":
            return " ".join(self._line_path(seg, tx, ty) for seg in coords if seg)

        if gtype == "Point":
            return self._point_path(coords, tx, ty)

        if gtype == "MultiPoint":
            return " ".join(self._point_path(pt, tx, ty) for pt in coords if pt)

        if gtype == "GeometryCollection":
            parts = []
            for sub in (geom or {}).get("geometries", []):
                d = self._geom_to_path(sub, tx, ty)
                if d:
                    parts.append(d)
            return " ".join(parts)

        return ""

    def _is_polygonal(self, geom: dict) -> bool:
        return (geom or {}).get("type", "") in {"Polygon", "MultiPolygon"}

    def plan_svg(self, width: int = 1100, height: int = 480) -> str:
        coords: List[Tuple[float, float]] = []
        for feat in self.features:
            coords.extend(self._coords(feat.get("geometry") or {}))

        if not coords:
            return (
                f"<svg width='{width}' height='{height}' viewBox='0 0 {width} {height}' "
                f"style='background:#111'><text x='12' y='24' fill='#aaa'>Plan vide</text></svg>"
            )

        xs = [p[0] for p in coords]
        ys = [p[1] for p in coords]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        w = max(maxx - minx, 1e-6)
        h = max(maxy - miny, 1e-6)
        pad = 20
        scale = min((width - 2 * pad) / w, (height - 2 * pad) / h)
        ox = pad - minx * scale
        oy = pad + h * scale + miny * scale

        def tx(x):
            return ox + x * scale

        def ty(y):
            return oy - y * scale

        parts = [
            f"<svg width='{width}' height='{height}' viewBox='0 0 {width} {height}' style='background:#111'>"
        ]

        for feat in self.features:
            props = feat.get("properties", {}) or {}
            clf = props.get("classification", {}) or {}
            stype = str(clf.get("structural_type", "UNKNOWN") or "UNKNOWN")
            d = self._geom_to_path(feat.get("geometry") or {}, tx, ty)
            if not d:
                continue

            color = TYPE_COLORS.get(stype, "#7f8c8d")
            polygonal = self._is_polygonal(feat.get("geometry") or {})
            opacity = "0.95" if clf.get("needs_review", False) else "0.65"
            fill = color if polygonal else "none"
            fill_opacity = "0.10" if polygonal else "0"

            parts.append(
                f"<path d=\"{d}\" fill='{fill}' fill-opacity='{fill_opacity}' fill-rule='evenodd' "
                f"stroke='{color}' stroke-width='1.4' opacity='{opacity}'/>"
            )

        parts.append("</svg>")
        return "".join(parts)

    def entity_thumb_data_uri(self, feat: dict, size: int = 72) -> str:
        coords = self._coords(feat.get("geometry") or {})
        if not coords:
            svg = (
                f"<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}'>"
                f"<rect x='0' y='0' width='{size}' height='{size}' fill='#0f0f23'/>"
                "<text x='50%' y='50%' dominant-baseline='middle' text-anchor='middle' fill='#555' font-size='10'>N/A</text>"
                "</svg>"
            )
            return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("ascii")

        xs = [p[0] for p in coords]
        ys = [p[1] for p in coords]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        w = max(maxx - minx, 1e-6)
        h = max(maxy - miny, 1e-6)
        pad_world = max(w, h) * 0.45 + 1.0
        bx0, bx1 = minx - pad_world, maxx + pad_world
        by0, by1 = miny - pad_world, maxy + pad_world
        bw = max(bx1 - bx0, 1e-6)
        bh = max(by1 - by0, 1e-6)
        pad_px = 6
        scale = min((size - 2 * pad_px) / bw, (size - 2 * pad_px) / bh)
        ox = pad_px - bx0 * scale
        oy = pad_px + bh * scale + by0 * scale

        def tx(x):
            return ox + x * scale

        def ty(y):
            return oy - y * scale

        props = feat.get("properties", {}) or {}
        clf = props.get("classification", {}) or {}
        stype = str(clf.get("structural_type", "UNKNOWN") or "UNKNOWN")
        color = TYPE_COLORS.get(stype, "#7f8c8d")
        geom = feat.get("geometry") or {}
        d = self._geom_to_path(geom, tx, ty)
        polygonal = self._is_polygonal(geom)

        svg = (
            f"<svg xmlns='http://www.w3.org/2000/svg' width='{size}' height='{size}'>"
            f"<rect x='0' y='0' width='{size}' height='{size}' fill='#0f0f23'/>"
            f"<path d=\"{html.escape(d, quote=True)}\" fill='{color if polygonal else 'none'}' "
            f"fill-opacity='{'0.12' if polygonal else '0'}' fill-rule='evenodd' "
            f"stroke='{color}' stroke-width='2.0'/>"
            "</svg>"
        )
        return "data:image/svg+xml;base64," + base64.b64encode(svg.encode("utf-8")).decode("ascii")

    def _item_from_feature(self, feat: dict) -> dict:
        props = feat.get("properties", {}) or {}
        clf = props.get("classification", {}) or {}
        src = props.get("source", {}) or {}
        stype = str(clf.get("structural_type", "UNKNOWN") or "UNKNOWN")

        return {
            "id": str(feat.get("id", "")),
            "type": stype,
            "review": "YES" if clf.get("needs_review", False) else "NO",
            "reason": str(clf.get("review_reason", "") or ""),
            "color": TYPE_COLORS.get(stype, "#7f8c8d"),
            "confidence": round(_safe_float(clf.get("confidence", 0.0)), 2),
            "method": str(clf.get("method", "") or ""),
            "layer": str(src.get("layer", "") or ""),
        }

    def stats(self) -> dict:
        done = 0
        pending_current = 0

        for fid in self.review_scope_ids:
            feat = self.by_id.get(fid)
            if not feat:
                continue
            clf = (feat.get("properties", {}) or {}).get("classification", {}) or {}
            if clf.get("method") == "human_review":
                done += 1

        for feat in self.features:
            clf = (feat.get("properties", {}) or {}).get("classification", {}) or {}
            if clf.get("needs_review", False):
                pending_current += 1

        total = len(self.review_scope_ids)
        return {
            "total": total,
            "done": done,
            "remaining": max(total - done, 0),
            "loaded": len(self.features),
            "pending_current": pending_current,
            "scope_mode": self.review_scope_mode,
        }

    def table_rows_html(self) -> str:
        rows: List[str] = []
        for feat in self.features:
            item = self._item_from_feature(feat)
            thumb = self.entity_thumb_data_uri(feat, 72)
            rows.append(
                "<tr>"
                "<td><input type='checkbox' name='ids' value='{id}'/></td>"
                "<td><img src='{thumb}' width='72' height='72' style='border-radius:4px;border:1px solid #2a2a4a;background:#0b0b1a'/></td>"
                "<td>{id}</td>"
                "<td><span style='color:{color}'>{type}</span></td>"
                "<td>{confidence:.2f}</td>"
                "<td>{review}</td>"
                "<td>{method}</td>"
                "<td>{layer}</td>"
                "<td title='{reason_title}'>{reason}</td>"
                "</tr>".format(
                    id=html.escape(item["id"], quote=True),
                    thumb=thumb,
                    color=item["color"],
                    type=html.escape(item["type"]),
                    confidence=item["confidence"],
                    review=html.escape(item["review"]),
                    method=html.escape(item["method"]),
                    layer=html.escape(item["layer"]),
                    reason=html.escape(item["reason"]),
                    reason_title=html.escape(item["reason"], quote=True),
                )
            )

        if not rows:
            rows.append("<tr><td colspan='9'>Aucune entité visible.</td></tr>")
        return "".join(rows)

    def apply(self, ids: List[str], new_type: str) -> int:
        if new_type not in STRUCT_TYPES:
            return 0

        modified = 0
        now = _now_iso()

        with self._lock:
            for fid in ids:
                feat = self.by_id.get(fid)
                if not feat:
                    continue

                self.review_scope_ids.add(fid)

                props = feat.setdefault("properties", {})
                clf = props.setdefault("classification", {})
                review_history = props.setdefault("review_history", [])

                review_history.append(
                    {
                        "timestamp": now,
                        "user": self.review_user,
                        "action": "set_structural_type",
                        "from_type": clf.get("structural_type", "UNKNOWN"),
                        "to_type": new_type,
                        "previous_confidence": clf.get("confidence", 0.0),
                        "previous_method": clf.get("method", ""),
                        "previous_needs_review": clf.get("needs_review", False),
                        "previous_review_reason": clf.get("review_reason", ""),
                    }
                )

                clf["structural_type"] = new_type
                clf["confidence"] = 1.0
                clf["method"] = "human_review"
                clf["needs_review"] = False
                clf["review_reason"] = ""

                props["last_review_at"] = now
                props["last_review_user"] = self.review_user
                modified += 1

        return modified

    def _build_output_metadata(self) -> dict:
        base = dict(self.metadata)
        base["review"] = {
            "input_geojson": str(self.input_path),
            "output_geojson": str(self.output_path),
            "saved_at": _now_iso(),
            "review_user": self.review_user,
            "stats": self.stats(),
        }
        return base

    def save(self) -> Path:
        with self._lock:
            fc = {
                "type": "FeatureCollection",
                "metadata": self._build_output_metadata(),
                "features": self.features,
            }
            self.output_path.write_text(json.dumps(fc, indent=2, ensure_ascii=False), encoding="utf-8")
        return self.output_path


def _html(session: ReviewSession, message: str = "") -> str:
    options_html = "".join(f"<option value='{t}'>{t}</option>" for t in STRUCT_TYPES)
    buttons_html = "".join(
        f"<button type='submit' name='new_type' value='{t}'>{t}</button>"
        for t in STRUCT_TYPES
    )
    stats = session.stats()

    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Coffrage Review</title>
<style>
body{{font-family:Arial,sans-serif;background:#0f0f23;color:#e0e0f0;margin:0}}
#top{{padding:10px;background:#1a1a2e;display:flex;gap:12px;align-items:center;position:sticky;top:0;z-index:3;flex-wrap:wrap}}
button{{margin:2px;padding:6px 10px;background:#16213e;color:#dce3ff;border:1px solid #2a2a4a;border-radius:4px;cursor:pointer}}
button:hover{{background:#1f2a55}}
table{{width:100%;border-collapse:collapse}}
td,th{{border-bottom:1px solid #2a2a4a;padding:8px;font-size:13px;vertical-align:middle}}
th{{background:#151b35}}
#msg{{color:#9fb3ff;font-size:12px}}
</style>
</head>
<body>
<div id="top">
  <b>Review</b>
  <span>{stats["done"]}/{stats["total"]} done | remaining={stats["remaining"]} | pending_now={stats["pending_current"]} | loaded={stats["loaded"]} | mode={stats["scope_mode"]}</span>
  <form method="post" action="/export" style="display:inline">
    <button type="submit">Export final</button>
  </form>
  <a href="/" style="color:#9fb3ff;text-decoration:none">Refresh</a>
  <span id="msg">{html.escape(message)}</span>
</div>

<div style="padding:10px;background:#111;border-bottom:1px solid #2a2a4a">
  {session.plan_svg()}
</div>

<form method="post" action="/apply" style="padding:8px">
  <div style="margin-bottom:8px">{buttons_html}</div>
  <table>
    <thead>
      <tr>
        <th></th>
        <th>Thumb</th>
        <th>ID</th>
        <th>Type</th>
        <th>Conf</th>
        <th>Review</th>
        <th>Method</th>
        <th>Layer</th>
        <th>Reason</th>
      </tr>
    </thead>
    <tbody>
      {session.table_rows_html()}
    </tbody>
  </table>
</form>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    session: ReviewSession = None  # type: ignore[assignment]

    def log_message(self, *args):
        return

    def _send(self, code: int, ctype: str, payload: bytes):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def _redirect(self, location: str):
        self.send_response(303)
        self.send_header("Location", location)
        self.end_headers()

    def _read_form(self) -> Dict[str, List[str]]:
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except Exception:
            length = 0

        body = self.rfile.read(length) if length > 0 else b""
        parsed = urllib.parse.parse_qs(body.decode("utf-8"), keep_blank_values=True)
        return {k: [str(v) for v in values] for k, values in parsed.items()}

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        if parsed.path in ("/", "/index.html"):
            msg = ""
            qs = urllib.parse.parse_qs(parsed.query)
            if "msg" in qs:
                msg = qs["msg"][0]
            self._send(200, "text/html; charset=utf-8", _html(self.session, msg).encode("utf-8"))
            return

        self._send(404, "text/plain; charset=utf-8", b"Not found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        form = self._read_form()

        if parsed.path == "/apply":
            ids = form.get("ids", [])
            new_type = (form.get("new_type") or [""])[0]
            modified = self.session.apply(ids, new_type)
            self.session.save()
            self._redirect(f"/?msg={urllib.parse.quote(f'Modifié: {modified}')}")
            return

        if parsed.path == "/export":
            out = self.session.save()
            self._send(
                200,
                "text/html; charset=utf-8",
                f"<html><body style='font-family:Arial;background:#111;color:#eee'>Saved: {html.escape(str(out))}</body></html>".encode("utf-8"),
            )
            threading.Timer(0.3, self.server.shutdown).start()
            return

        self._send(404, "text/plain; charset=utf-8", b"Not found")


def _bind_server(port: int) -> Tuple[ThreadingHTTPServer, int]:
    candidates = [port] + [port + i for i in range(1, 20)]
    last_error: Optional[Exception] = None

    for candidate in candidates:
        try:
            server = ThreadingHTTPServer(("127.0.0.1", candidate), Handler)
            return server, candidate
        except OSError as exc:
            last_error = exc
            continue

    raise RuntimeError(f"Unable to bind review server near port {port}") from last_error


def run(
    input_path: Path,
    output_path: Optional[Path] = None,
    port: int = 5050,
    auto_open: bool = True,
    review_user: str = "operator",
) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"Review input file not found: {input_path}")
    if port <= 0:
        raise ValueError("Review port must be > 0")

    session = ReviewSession(input_path, output_path, review_user=review_user)
    Handler.session = session

    server, actual_port = _bind_server(port)
    url = f"http://localhost:{actual_port}"

    if actual_port != port:
        logger.warning(f"Review server requested port {port} unavailable, using {actual_port}")

    logger.info(f"Review server: {url}")
    if auto_open:
        threading.Timer(0.5, lambda: webbrowser.open(url)).start()

    try:
        server.serve_forever()
    finally:
        server.server_close()

    return session.output_path


def main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="Coffrage Review")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--port", type=int, default=5050)
    ap.add_argument("--no-browser", action="store_true")
    ap.add_argument("--review-user", default="operator")
    args = ap.parse_args()

    try:
        output = Path(args.output) if args.output else None
        run(
            Path(args.input),
            output,
            args.port,
            not args.no_browser,
            review_user=args.review_user,
        )
        return 0
    except Exception as exc:
        logger.error(f"Review failed: {exc}")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())