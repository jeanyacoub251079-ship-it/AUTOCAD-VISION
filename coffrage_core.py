#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict, dataclass, field, fields
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type, TypeVar, Union

import ezdxf
from loguru import logger
from shapely.geometry import LineString, Point, Polygon, box, mapping, shape

try:
    from ezdxf.math import bulge_to_arc
    HAS_BULGE_TO_ARC = True
except Exception:
    bulge_to_arc = None
    HAS_BULGE_TO_ARC = False


T = TypeVar("T")

_DXF_UNIT_TO_CM: dict[int, tuple[str, float]] = {
    0: ("unitless", 1.0),
    1: ("inch", 2.54),
    2: ("foot", 30.48),
    3: ("mile", 160934.4),
    4: ("mm", 0.1),
    5: ("cm", 1.0),
    6: ("m", 100.0),
    7: ("km", 100000.0),
    8: ("microinch", 0.00000254),
    9: ("mil", 0.00254),
    10: ("yard", 91.44),
}

_ANNOTATION_TYPES = {"TEXT", "MTEXT", "DIMENSION", "LEADER", "MULTILEADER", "ATTDEF", "ATTRIB"}
_SUPPORTED_DXF_TYPES = {
    "LINE",
    "LWPOLYLINE",
    "POLYLINE",
    "CIRCLE",
    "ARC",
    "ELLIPSE",
    "SPLINE",
    "POINT",
    "TEXT",
    "MTEXT",
    "INSERT",
    "DIMENSION",
    "LEADER",
    "MULTILEADER",
    "ATTDEF",
    "ATTRIB",
    "HATCH",
}


@dataclass
class PipelineConfig:
    units: str = "cm"
    tolerance_mode: str = "NORMAL"
    snap_distance_cm: float = 2.0
    min_segment_cm: float = 0.5
    confidence_auto: float = 0.75
    confidence_review: float = 0.40
    default_input_unit: str = "cm"
    expand_inserts: bool = True
    insert_virtual_depth: int = 2

    def apply_tolerance_mode(self) -> "PipelineConfig":
        table = {"STRICT": 0.5, "NORMAL": 2.0, "LOOSE": 5.0}
        self.snap_distance_cm = table.get(self.tolerance_mode, 2.0)
        return self


@dataclass
class SourceMeta:
    handle: str = ""
    layer: str = "0"
    color: int = 256
    linetype: str = "BYLAYER"
    entity_type: str = ""
    original_file: str = ""
    original_format: str = "DXF"
    original_units: str = ""
    scale_to_cm: float = 1.0
    block_name: str = ""
    parent_insert_handle: str = ""


@dataclass
class GeomProps:
    thickness_cm: Optional[float] = None
    length_cm: Optional[float] = None
    area_m2: Optional[float] = None
    orientation_deg: Optional[float] = None
    is_closed: bool = False
    centroid_x: Optional[float] = None
    centroid_y: Optional[float] = None
    was_reconstructed: bool = False
    reconstruction_method: str = ""


@dataclass
class ClassificationResult:
    structural_type: str = "UNKNOWN"
    sub_type: str = ""
    confidence: float = 0.0
    method: str = "unclassified"
    needs_review: bool = False
    review_reason: str = ""
    scores: Dict[str, float] = field(default_factory=dict)


@dataclass
class TopologyInfo:
    adjacent_ids: List[str] = field(default_factory=list)
    zone_label: str = ""


@dataclass
class CoffrageAttrs:
    repere: Optional[str] = None
    section_label: Optional[str] = None


@dataclass
class CoherenceFlags:
    passed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


@dataclass
class RawEntity:
    id: str
    geometry_geojson: dict = field(default_factory=dict)
    source: SourceMeta = field(default_factory=SourceMeta)
    geom_props: GeomProps = field(default_factory=GeomProps)
    classification: ClassificationResult = field(default_factory=ClassificationResult)
    topology: TopologyInfo = field(default_factory=TopologyInfo)
    coffrage: CoffrageAttrs = field(default_factory=CoffrageAttrs)
    coherence: CoherenceFlags = field(default_factory=CoherenceFlags)
    issues: List[str] = field(default_factory=list)
    geom_hash: str = ""
    _geometry_cache: Any = field(default=None, init=False, repr=False, compare=False)

    def geometry(self):
        if self._geometry_cache is None and self.geometry_geojson:
            self._geometry_cache = shape(self.geometry_geojson)
        return self._geometry_cache

    def set_geometry(self, geom) -> None:
        self.geometry_geojson = mapping(geom) if geom is not None else {}
        self._geometry_cache = geom
        self.geom_hash = _geom_hash(geom) if geom is not None else ""

    def to_geojson_feature(self) -> dict:
        return {
            "type": "Feature",
            "id": self.id,
            "geometry": self.geometry_geojson,
            "properties": {
                "id": self.id,
                "source": asdict(self.source),
                "geom_props": asdict(self.geom_props),
                "classification": asdict(self.classification),
                "topology": asdict(self.topology),
                "coffrage": asdict(self.coffrage),
                "coherence": asdict(self.coherence),
                "issues": list(self.issues),
                "geom_hash": self.geom_hash,
            },
        }

    @classmethod
    def from_geojson_feature(cls, feature: dict) -> "RawEntity":
        props = feature.get("properties", {}) or {}
        entity = cls(
            id=str(feature.get("id") or props.get("id") or ""),
            geometry_geojson=feature.get("geometry") or {},
            source=_dataclass_from_dict(SourceMeta, props.get("source")),
            geom_props=_dataclass_from_dict(GeomProps, props.get("geom_props")),
            classification=_dataclass_from_dict(ClassificationResult, props.get("classification")),
            topology=_dataclass_from_dict(TopologyInfo, props.get("topology")),
            coffrage=_dataclass_from_dict(CoffrageAttrs, props.get("coffrage")),
            coherence=_dataclass_from_dict(CoherenceFlags, props.get("coherence")),
            issues=list(props.get("issues") or []),
            geom_hash=str(props.get("geom_hash") or ""),
        )
        if not entity.geom_hash and entity.geometry_geojson:
            entity.geom_hash = _geom_hash(entity.geometry())
        return entity


def _dataclass_from_dict(cls: Type[T], payload: Optional[dict]) -> T:
    payload = payload or {}
    allowed = {f.name for f in fields(cls)}
    filtered = {k: v for k, v in payload.items() if k in allowed}
    return cls(**filtered)  # type: ignore[arg-type]


def compute_mrr(poly: Polygon) -> Tuple[Optional[float], Optional[float], Optional[float]]:
    try:
        mrr = poly.minimum_rotated_rectangle
        pts = list(mrr.exterior.coords)
        if len(pts) < 4:
            return None, None, None
        a = Point(pts[0]).distance(Point(pts[1]))
        b = Point(pts[1]).distance(Point(pts[2]))
        t = min(a, b)
        l = max(a, b)
        if a >= b:
            dx, dy = pts[1][0] - pts[0][0], pts[1][1] - pts[0][1]
        else:
            dx, dy = pts[2][0] - pts[1][0], pts[2][1] - pts[1][1]
        ang = math.degrees(math.atan2(dy, dx)) % 180
        return round(t, 2), round(l, 2), round(ang, 1)
    except Exception:
        return None, None, None


def _geom_hash(geom) -> str:
    try:
        payload = json.dumps(mapping(geom), sort_keys=True)
    except Exception:
        payload = "{}"
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()


def _line_orientation_deg(g: LineString) -> Optional[float]:
    try:
        coords = list(g.coords)
        if len(coords) < 2:
            return None
        x0, y0 = coords[0][:2]
        x1, y1 = coords[-1][:2]
        if x0 == x1 and y0 == y1:
            return None
        return round(math.degrees(math.atan2(y1 - y0, x1 - x0)) % 180, 1)
    except Exception:
        return None


def _props_from_geom(g) -> GeomProps:
    props = GeomProps()

    try:
        c = g.centroid
        props.centroid_x = round(c.x, 2)
        props.centroid_y = round(c.y, 2)
    except Exception:
        pass

    if isinstance(g, Polygon):
        props.is_closed = True
        props.area_m2 = round(g.area / 10000.0, 4)
        t, l, a = compute_mrr(g)
        props.thickness_cm = t
        props.length_cm = l
        props.orientation_deg = a
    elif isinstance(g, LineString):
        props.length_cm = round(g.length, 2)
        props.orientation_deg = _line_orientation_deg(g)

    return props


def _read_dxf(filepath: Path) -> ezdxf.document.Drawing:
    if not filepath.exists():
        raise FileNotFoundError(f"Input file not found: {filepath}")
    if filepath.suffix.lower() != ".dxf":
        raise ValueError("Fresh start pipeline currently supports DXF input.")
    try:
        return ezdxf.readfile(str(filepath))
    except Exception as exc:
        raise RuntimeError(f"Unable to read DXF file: {filepath}") from exc


def _entity_points_raw(ent, *, depth: int = 0, max_depth: int = 2) -> list[Tuple[float, float]]:
    et = ent.dxftype()
    points: list[Tuple[float, float]] = []

    try:
        if et == "LINE":
            points.append((float(ent.dxf.start.x), float(ent.dxf.start.y)))
            points.append((float(ent.dxf.end.x), float(ent.dxf.end.y)))
            return points

        if et == "LWPOLYLINE":
            for p in ent.get_points("xy"):
                points.append((float(p[0]), float(p[1])))
            return points

        if et == "POLYLINE":
            try:
                for v in ent.vertices:
                    points.append((float(v.dxf.location.x), float(v.dxf.location.y)))
            except Exception:
                pass
            return points

        if et == "CIRCLE":
            c = ent.dxf.center
            r = float(ent.dxf.radius)
            for dx, dy in ((-r, 0.0), (r, 0.0), (0.0, -r), (0.0, r)):
                points.append((float(c.x) + dx, float(c.y) + dy))
            return points

        if et == "ARC":
            c = ent.dxf.center
            r = float(ent.dxf.radius)
            start = math.radians(float(ent.dxf.start_angle))
            end = math.radians(float(ent.dxf.end_angle))
            for ang in (start, end):
                points.append((float(c.x) + r * math.cos(ang), float(c.y) + r * math.sin(ang)))
            return points

        if et in {"TEXT", "MTEXT", "ATTDEF", "ATTRIB"}:
            insert = getattr(ent.dxf, "insert", None)
            if insert is not None:
                points.append((float(insert.x), float(insert.y)))
            return points

        if et == "POINT":
            points.append((float(ent.dxf.location.x), float(ent.dxf.location.y)))
            return points

        if et == "INSERT":
            insert = getattr(ent.dxf, "insert", None)
            if insert is not None:
                points.append((float(insert.x), float(insert.y)))
            if depth < max_depth:
                try:
                    for child in ent.virtual_entities():
                        points.extend(_entity_points_raw(child, depth=depth + 1, max_depth=max_depth))
                except Exception:
                    pass
            return points

    except Exception:
        return points

    return points

def _safe_bbox_from_points(points: list[tuple[float, float]]) -> Optional[tuple[float, float, float, float]]:
    if not points:
        return None
    xs = [p[0] for p in points if math.isfinite(p[0])]
    ys = [p[1] for p in points if math.isfinite(p[1])]
    if not xs or not ys:
        return None
    return min(xs), min(ys), max(xs), max(ys)


def _union_bounds(boxes: list[tuple[float, float, float, float]]) -> tuple[float, float, float, float]:
    min_x = min(b[0] for b in boxes)
    min_y = min(b[1] for b in boxes)
    max_x = max(b[2] for b in boxes)
    max_y = max(b[3] for b in boxes)
    return min_x, min_y, max_x, max_y


def _infer_unitless_scale(doc: ezdxf.document.Drawing, cfg: PipelineConfig) -> tuple[str, float]:
    boxes: list[Tuple[float, float, float, float]] = []

    for ent in doc.modelspace():
        if ent.dxftype() in _ANNOTATION_TYPES:
            continue
        pts = _entity_points_raw(ent, depth=0, max_depth=min(2, cfg.insert_virtual_depth))
        bbox = _safe_bbox_from_points(pts)
        if bbox is not None:
            boxes.append(bbox)

    if not boxes:
        assumed = (cfg.default_input_unit or "cm").strip().lower()
        for _, (name, factor) in _DXF_UNIT_TO_CM.items():
            if name == assumed:
                return f"assumed_{name}", factor
        return "assumed_cm", 1.0

    bounds = _union_bounds(boxes)
    max_dim = max(abs(bounds[2] - bounds[0]), abs(bounds[3] - bounds[1]))

    if max_dim <= 120.0:
        return "inferred_m", 100.0
    if max_dim >= 8000.0:
        return "inferred_mm", 0.1
    return "inferred_cm", 1.0


def _resolve_units(doc: ezdxf.document.Drawing, config: Optional[PipelineConfig]) -> tuple[str, float, int]:
    cfg = config or PipelineConfig()
    insunits_code = int(doc.header.get("$INSUNITS", 0) or 0)

    if insunits_code in _DXF_UNIT_TO_CM and insunits_code != 0:
        unit_name, factor = _DXF_UNIT_TO_CM[insunits_code]
        return unit_name, factor, insunits_code

    unit_name, factor = _infer_unitless_scale(doc, cfg)
    return unit_name, factor, insunits_code


def _xy(pt: Any, scale_to_cm: float) -> tuple[float, float]:
    if hasattr(pt, "x") and hasattr(pt, "y"):
        x = float(pt.x)
        y = float(pt.y)
    elif isinstance(pt, (tuple, list)) and len(pt) >= 2:
        x = float(pt[0])
        y = float(pt[1])
    else:
        raise TypeError("Unsupported point representation")
    return round(x * scale_to_cm, 6), round(y * scale_to_cm, 6)


def _safe_linestring(coords: List[tuple[float, float]]) -> Optional[LineString]:
    if len(coords) < 2:
        return None
    try:
        line = LineString(coords)
        if line.is_empty or line.length <= 0:
            return None
        return line
    except Exception:
        return None


def _largest_polygon(geom) -> Optional[Polygon]:
    if geom is None or geom.is_empty:
        return None
    if isinstance(geom, Polygon):
        return geom
    if geom.geom_type == "MultiPolygon":
        polygons = [g for g in geom.geoms if isinstance(g, Polygon) and not g.is_empty]
        if polygons:
            return max(polygons, key=lambda p: p.area)
    return None


def _safe_polygon(coords: List[tuple[float, float]]) -> Optional[Polygon]:
    if len(coords) < 3:
        return None
    if coords[0] != coords[-1]:
        coords = coords + [coords[0]]
    try:
        poly = Polygon(coords)
        if poly.is_empty:
            return None
        if not poly.is_valid:
            repaired = poly.buffer(0)
            poly = _largest_polygon(repaired) or poly
        if poly.is_empty or not poly.is_valid or poly.area <= 0:
            return None
        return poly
    except Exception:
        return None


def _sample_arc_points(
    center_xy_cm: tuple[float, float],
    radius_cm: float,
    start_deg: float,
    end_deg: float,
    *,
    min_segments: int = 12,
    max_segments: int = 96,
) -> List[tuple[float, float]]:
    cx, cy = center_xy_cm
    span = (end_deg - start_deg) % 360.0
    if math.isclose(span, 0.0, abs_tol=1e-9):
        span = 360.0
    segments = max(min_segments, min(max_segments, int(abs(span) / 8.0) + 1))
    points: List[tuple[float, float]] = []
    for i in range(segments + 1):
        ang = math.radians(start_deg + span * (i / segments))
        points.append((round(cx + radius_cm * math.cos(ang), 6), round(cy + radius_cm * math.sin(ang), 6)))
    return points


def _approximate_bulge_segment(
    p1: tuple[float, float],
    p2: tuple[float, float],
    bulge: float,
) -> List[tuple[float, float]]:
    if math.isclose(bulge, 0.0, abs_tol=1e-12) or not HAS_BULGE_TO_ARC:
        return [p1, p2]

    try:
        center, start_angle, end_angle, radius = bulge_to_arc(p1, p2, bulge)
        start_deg = math.degrees(start_angle)
        end_deg = math.degrees(end_angle)
        span = (end_deg - start_deg) % 360.0
        if bulge < 0 and span > 0:
            span -= 360.0
        segments = max(8, min(64, int(abs(span) / 8.0) + 1))
        pts: List[tuple[float, float]] = []
        for i in range(segments + 1):
            ang = math.radians(start_deg + span * (i / segments))
            pts.append(
                (
                    round(float(center[0]) + float(radius) * math.cos(ang), 6),
                    round(float(center[1]) + float(radius) * math.sin(ang), 6),
                )
            )
        if pts:
            pts[0] = p1
            pts[-1] = p2
        return pts
    except Exception:
        return [p1, p2]


def _lwpolyline_coords(ent, scale_to_cm: float) -> tuple[List[tuple[float, float]], bool, List[str]]:
    raw = list(ent.get_points("xyb"))
    if not raw:
        return [], False, []

    closed = bool(ent.closed)
    issues: List[str] = []
    coords: List[tuple[float, float]] = []

    for idx, item in enumerate(raw):
        x, y, bulge = float(item[0]), float(item[1]), float(item[2] or 0.0)
        p1 = (round(x * scale_to_cm, 6), round(y * scale_to_cm, 6))
        next_idx = (idx + 1) % len(raw)

        if idx == len(raw) - 1 and not closed:
            if not coords or coords[-1] != p1:
                coords.append(p1)
            continue

        nx, ny, _ = raw[next_idx]
        p2 = (round(float(nx) * scale_to_cm, 6), round(float(ny) * scale_to_cm, 6))

        if math.isclose(bulge, 0.0, abs_tol=1e-12):
            if not coords or coords[-1] != p1:
                coords.append(p1)
        else:
            if not HAS_BULGE_TO_ARC and "LWPL_BULGE_IGNORED" not in issues:
                issues.append("LWPL_BULGE_IGNORED")
            seg = _approximate_bulge_segment(p1, p2, bulge)
            if coords and seg:
                seg = seg[1:]
            coords.extend(seg)

    if closed and coords and coords[0] != coords[-1]:
        coords.append(coords[0])

    return coords, closed, issues


def _polyline_coords(ent, scale_to_cm: float) -> tuple[List[tuple[float, float]], bool, List[str]]:
    issues: List[str] = []

    try:
        vertices = list(ent.vertices)
    except Exception:
        vertices = []

    if not vertices:
        return [], False, issues

    is_closed_attr = getattr(ent, "is_closed", False)
    closed = bool(is_closed_attr() if callable(is_closed_attr) else is_closed_attr)

    points: List[tuple[float, float]] = []
    bulges: List[float] = []
    for vertex in vertices:
        points.append(_xy(vertex.dxf.location, scale_to_cm))
        bulges.append(float(getattr(vertex.dxf, "bulge", 0.0) or 0.0))

    if any(not math.isclose(b, 0.0, abs_tol=1e-12) for b in bulges):
        if "POLYLINE_BULGE_APPROX" not in issues:
            issues.append("POLYLINE_BULGE_APPROX")
        coords: List[tuple[float, float]] = []
        n = len(points)
        for i, p1 in enumerate(points):
            next_i = (i + 1) % n
            if i == n - 1 and not closed:
                if not coords or coords[-1] != p1:
                    coords.append(p1)
                continue
            p2 = points[next_i]
            seg = _approximate_bulge_segment(p1, p2, bulges[i])
            if coords and seg:
                seg = seg[1:]
            coords.extend(seg)
        if closed and coords and coords[0] != coords[-1]:
            coords.append(coords[0])
        return coords, closed, issues

    if closed and points and points[0] != points[-1]:
        points.append(points[0])

    return points, closed, issues


def _approximate_circle(ent, scale_to_cm: float) -> Optional[Polygon]:
    center = _xy(ent.dxf.center, scale_to_cm)
    radius_cm = float(ent.dxf.radius) * scale_to_cm
    coords = _sample_arc_points(center, radius_cm, 0.0, 360.0, min_segments=18)
    return _safe_polygon(coords)


def _approximate_arc(ent, scale_to_cm: float) -> Optional[LineString]:
    center = _xy(ent.dxf.center, scale_to_cm)
    radius_cm = float(ent.dxf.radius) * scale_to_cm
    coords = _sample_arc_points(center, radius_cm, float(ent.dxf.start_angle), float(ent.dxf.end_angle))
    return _safe_linestring(coords)


def _flatten_entity_points(ent, scale_to_cm: float, source_step_cm: float = 2.0) -> List[tuple[float, float]]:
    flattening = getattr(ent, "flattening", None)
    if not callable(flattening):
        return []
    try:
        source_distance = max(0.05, source_step_cm / max(scale_to_cm, 1e-9))
        return [_xy(p, scale_to_cm) for p in flattening(source_distance)]
    except Exception:
        return []


def _bbox_polygon(ent, scale_to_cm: float) -> Optional[Polygon]:
    try:
        b = ent.bbox()
    except Exception:
        b = None
    if b is None:
        return None
    try:
        return box(
            float(b.extmin.x) * scale_to_cm,
            float(b.extmin.y) * scale_to_cm,
            float(b.extmax.x) * scale_to_cm,
            float(b.extmax.y) * scale_to_cm,
        )
    except Exception:
        return None


def _bbox_center_point(ent, scale_to_cm: float) -> Optional[Point]:
    try:
        b = ent.bbox()
    except Exception:
        b = None
    if b is None:
        return None
    try:
        return Point(
            round(((float(b.extmin.x) + float(b.extmax.x)) / 2.0) * scale_to_cm, 6),
            round(((float(b.extmin.y) + float(b.extmax.y)) / 2.0) * scale_to_cm, 6),
        )
    except Exception:
        return None


def _extract_hatch_geometry(ent, scale_to_cm: float) -> tuple[Optional[Union[Polygon, LineString]], List[str]]:
    issues: List[str] = []
    try:
        paths = list(ent.paths)
    except Exception:
        return None, ["HATCH_PATHS_UNAVAILABLE"]

    polygons: List[Polygon] = []
    lines: List[LineString] = []

    for path in paths:
        path_type = path.__class__.__name__.upper()

        if "POLYLINEPATH" in path_type:
            try:
                raw_vertices = list(path.vertices)
                closed = bool(getattr(path, "is_closed", True))
            except Exception:
                continue

            coords: List[tuple[float, float]] = []
            for idx, item in enumerate(raw_vertices):
                x = float(item[0])
                y = float(item[1])
                bulge = float(item[2] or 0.0) if len(item) >= 3 else 0.0
                p1 = (round(x * scale_to_cm, 6), round(y * scale_to_cm, 6))
                next_idx = (idx + 1) % len(raw_vertices)

                if idx == len(raw_vertices) - 1 and not closed:
                    if not coords or coords[-1] != p1:
                        coords.append(p1)
                    continue

                nx, ny = float(raw_vertices[next_idx][0]), float(raw_vertices[next_idx][1])
                p2 = (round(nx * scale_to_cm, 6), round(ny * scale_to_cm, 6))

                if not HAS_BULGE_TO_ARC and not math.isclose(bulge, 0.0, abs_tol=1e-12):
                    if "HATCH_BULGE_IGNORED" not in issues:
                        issues.append("HATCH_BULGE_IGNORED")

                seg = _approximate_bulge_segment(p1, p2, bulge)
                if coords and seg:
                    seg = seg[1:]
                coords.extend(seg)

            geom = _safe_polygon(coords) if closed else _safe_linestring(coords)
            if isinstance(geom, Polygon):
                polygons.append(geom)
            elif isinstance(geom, LineString):
                lines.append(geom)
        else:
            if "HATCH_EDGEPATH_FALLBACK" not in issues:
                issues.append("HATCH_EDGEPATH_FALLBACK")

    if polygons:
        polygons.sort(key=lambda p: p.area, reverse=True)
        if len(polygons) > 1:
            issues.append("HATCH_MULTIPLE_BOUNDARIES_LARGEST_USED")
        return polygons[0], issues

    if lines:
        lines.sort(key=lambda l: l.length, reverse=True)
        return lines[0], issues

    bbox_geom = _bbox_polygon(ent, scale_to_cm)
    if bbox_geom is not None:
        issues.append("HATCH_BBOX_PROXY")
        return bbox_geom, issues

    return None, issues or ["HATCH_UNSUPPORTED"]


def _extract_geometry_and_flags(
    ent,
    scale_to_cm: float,
) -> tuple[Optional[Union[Point, LineString, Polygon]], List[str], Optional[ClassificationResult]]:
    et = ent.dxftype()
    issues: List[str] = []
    classification_override: Optional[ClassificationResult] = None
    geom = None

    if et == "LINE":
        geom = _safe_linestring([_xy(ent.dxf.start, scale_to_cm), _xy(ent.dxf.end, scale_to_cm)])

    elif et == "LWPOLYLINE":
        coords, closed, lw_issues = _lwpolyline_coords(ent, scale_to_cm)
        issues.extend(lw_issues)
        geom = _safe_polygon(coords) if closed else _safe_linestring(coords)

    elif et == "POLYLINE":
        coords, closed, pl_issues = _polyline_coords(ent, scale_to_cm)
        issues.extend(pl_issues)
        geom = _safe_polygon(coords) if closed else _safe_linestring(coords)

    elif et == "CIRCLE":
        geom = _approximate_circle(ent, scale_to_cm)
        issues.append("CIRCLE_APPROX_POLYGON")

    elif et == "ARC":
        geom = _approximate_arc(ent, scale_to_cm)
        issues.append("ARC_APPROX_LINE")

    elif et == "ELLIPSE":
        points = _flatten_entity_points(ent, scale_to_cm)
        start_param = float(getattr(ent.dxf, "start_param", 0.0) or 0.0)
        end_param = float(getattr(ent.dxf, "end_param", 0.0) or 0.0)
        closed = abs((end_param - start_param) % (2 * math.pi)) >= (2 * math.pi - 1e-3)
        geom = _safe_polygon(points) if closed else _safe_linestring(points)
        if geom is not None:
            issues.append("ELLIPSE_APPROX")
        else:
            geom = _bbox_polygon(ent, scale_to_cm)
            if geom is not None:
                issues.append("ELLIPSE_BBOX_PROXY")

    elif et == "SPLINE":
        points = _flatten_entity_points(ent, scale_to_cm)
        geom = _safe_linestring(points)
        if geom is not None:
            issues.append("SPLINE_APPROX")
        else:
            geom = _bbox_polygon(ent, scale_to_cm)
            if geom is not None:
                issues.append("SPLINE_BBOX_PROXY")

    elif et == "POINT":
        geom = Point(*_xy(ent.dxf.location, scale_to_cm))

    elif et in {"TEXT", "MTEXT"}:
        insert = getattr(ent.dxf, "insert", None)
        geom = Point(*_xy(insert, scale_to_cm)) if insert is not None else _bbox_center_point(ent, scale_to_cm)
        classification_override = ClassificationResult(
            structural_type="ANNOTATION",
            confidence=1.0,
            method="rule:text",
            needs_review=False,
        )

    elif et in {"DIMENSION", "LEADER", "MULTILEADER", "ATTDEF", "ATTRIB"}:
        geom = _bbox_center_point(ent, scale_to_cm)
        classification_override = ClassificationResult(
            structural_type="ANNOTATION",
            confidence=0.98,
            method="rule:annotation_entity",
            needs_review=False,
        )

    elif et == "HATCH":
        geom, hatch_issues = _extract_hatch_geometry(ent, scale_to_cm)
        issues.extend(hatch_issues)

    if geom is None or getattr(geom, "is_empty", True):
        return None, issues, classification_override

    return geom, issues, classification_override


def inspect_file(filepath: Path, config: Optional[PipelineConfig] = None) -> dict:
    doc = _read_dxf(filepath)
    source_units, scale_to_cm, insunits_code = _resolve_units(doc, config)

    by_type: Dict[str, int] = {}
    by_layer: Dict[str, Dict[str, int]] = {}

    for ent in doc.modelspace():
        et = ent.dxftype()
        layer = getattr(ent.dxf, "layer", "0") or "0"
        by_type[et] = by_type.get(et, 0) + 1
        by_layer.setdefault(layer, {})
        by_layer[layer][et] = by_layer[layer].get(et, 0) + 1

    unsupported_by_type = {k: v for k, v in by_type.items() if k not in _SUPPORTED_DXF_TYPES}

    return {
        "file": str(filepath),
        "format": filepath.suffix.upper().lstrip("."),
        "total": sum(by_type.values()),
        "supported_total": sum(v for k, v in by_type.items() if k in _SUPPORTED_DXF_TYPES),
        "unsupported_total": sum(unsupported_by_type.values()),
        "by_type": by_type,
        "unsupported_by_type": unsupported_by_type,
        "layers": by_layer,
        "units": {
            "insunits_code": insunits_code,
            "source_units": source_units,
            "scale_to_cm": scale_to_cm,
            "normalized_units": "cm",
        },
    }


def save_entities_json(
    entities: List[RawEntity],
    output_path: Path,
    metadata: Optional[dict] = None,
) -> None:
    source_files = sorted({e.source.original_file for e in entities if e.source.original_file})
    source_units = sorted({e.source.original_units for e in entities if e.source.original_units})
    source_blocks = sorted({e.source.block_name for e in entities if e.source.block_name})

    collection = {
        "type": "FeatureCollection",
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "total": len(entities),
            "units": "cm",
            "source_files": source_files,
            "source_units": source_units,
            "source_blocks": source_blocks,
            **(metadata or {}),
        },
        "features": [e.to_geojson_feature() for e in entities],
    }
    output_path.write_text(json.dumps(collection, indent=2, ensure_ascii=False), encoding="utf-8")


def load_entities_json(
    path: Path,
    *,
    as_entities: bool = False,
) -> Union[List[dict], List[RawEntity]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    features = data.get("features", [])
    if as_entities:
        return [RawEntity.from_geojson_feature(f) for f in features]
    return features


def load_entities_json_entities(path: Path) -> List[RawEntity]:
    return load_entities_json(path, as_entities=True)  # type: ignore[return-value]


def _effective_insert_child_attrib(ent, parent_ent, attr_name: str, default_value):
    child_value = getattr(ent.dxf, attr_name, default_value)
    parent_value = getattr(parent_ent.dxf, attr_name, default_value)

    if attr_name == "layer":
        if not child_value or str(child_value).upper() == "0":
            return parent_value or default_value
        return child_value

    if attr_name == "color":
        if child_value in (0, 256, None):
            return parent_value if parent_value not in (None,) else default_value
        return child_value

    if attr_name == "linetype":
        if not child_value or str(child_value).upper() in {"BYLAYER", "BYBLOCK"}:
            return parent_value or default_value
        return child_value

    return child_value if child_value is not None else parent_value


def _make_raw_entity(
    geom,
    ent,
    source_file: str,
    source_fmt: str,
    source_units: str,
    scale_to_cm: float,
    next_id: int,
    *,
    issues: Optional[List[str]] = None,
    classification_override: Optional[ClassificationResult] = None,
    source_layer: Optional[str] = None,
    source_color: Optional[int] = None,
    source_linetype: Optional[str] = None,
    source_entity_type: Optional[str] = None,
    block_name: str = "",
    parent_insert_handle: str = "",
) -> Optional[RawEntity]:
    if geom is None or geom.is_empty:
        return None

    source = SourceMeta(
        handle=getattr(ent.dxf, "handle", "") or "",
        layer=source_layer if source_layer is not None else (getattr(ent.dxf, "layer", "0") or "0"),
        color=source_color if source_color is not None else getattr(ent.dxf, "color", 256),
        linetype=source_linetype if source_linetype is not None else (getattr(ent.dxf, "linetype", "BYLAYER") or "BYLAYER"),
        entity_type=source_entity_type if source_entity_type is not None else ent.dxftype(),
        original_file=source_file,
        original_format=source_fmt,
        original_units=source_units,
        scale_to_cm=scale_to_cm,
        block_name=block_name,
        parent_insert_handle=parent_insert_handle,
    )

    entity = RawEntity(
        id=f"ENT-{next_id:05d}",
        source=source,
        geom_props=_props_from_geom(geom),
        issues=list(issues or []),
    )
    entity.set_geometry(geom)

    if classification_override is not None:
        entity.classification = classification_override

    return entity


def _entities_from_insert(
    ent,
    cfg: PipelineConfig,
    scale_to_cm: float,
    source_file: str,
    source_fmt: str,
    source_units: str,
    next_id: int,
    *,
    depth: int = 0,
) -> tuple[List[RawEntity], int]:
    out: List[RawEntity] = []

    if cfg.expand_inserts and depth < cfg.insert_virtual_depth:
        try:
            children = list(ent.virtual_entities())
        except Exception:
            children = []

        for child in children:
            child_entities, next_id = _entities_from_dxf_object(
                child,
                cfg,
                scale_to_cm,
                source_file,
                source_fmt,
                source_units,
                next_id,
                depth=depth + 1,
                parent_insert=ent,
            )
            out.extend(child_entities)

    if out:
        return out, next_id

    geom = _bbox_polygon(ent, scale_to_cm)
    issues = ["INSERT_PROXY_FALLBACK"]
    if geom is None:
        insert = getattr(ent.dxf, "insert", None)
        if insert is not None:
            geom = Point(*_xy(insert, scale_to_cm))
            issues = ["INSERT_POINT_PROXY"]

    if geom is not None:
        raw = _make_raw_entity(
            geom=geom,
            ent=ent,
            source_file=source_file,
            source_fmt=source_fmt,
            source_units=source_units,
            scale_to_cm=scale_to_cm,
            next_id=next_id,
            issues=issues,
            source_entity_type="INSERT",
            block_name=str(getattr(ent.dxf, "name", "") or ""),
        )
        if raw is not None:
            out.append(raw)
            next_id += 1

    return out, next_id


def _entities_from_dxf_object(
    ent,
    cfg: PipelineConfig,
    scale_to_cm: float,
    source_file: str,
    source_fmt: str,
    source_units: str,
    next_id: int,
    *,
    depth: int = 0,
    parent_insert=None,
) -> tuple[List[RawEntity], int]:
    et = ent.dxftype()

    if et == "INSERT":
        return _entities_from_insert(
            ent,
            cfg,
            scale_to_cm,
            source_file,
            source_fmt,
            source_units,
            next_id,
            depth=depth,
        )

    geom, issues, classification_override = _extract_geometry_and_flags(ent, scale_to_cm)
    if geom is None:
        return [], next_id

    source_layer = None
    source_color = None
    source_linetype = None
    block_name = ""
    parent_insert_handle = ""

    if parent_insert is not None:
        source_layer = _effective_insert_child_attrib(ent, parent_insert, "layer", "0")
        source_color = int(_effective_insert_child_attrib(ent, parent_insert, "color", 256))
        source_linetype = str(_effective_insert_child_attrib(ent, parent_insert, "linetype", "BYLAYER"))
        block_name = str(getattr(parent_insert.dxf, "name", "") or "")
        parent_insert_handle = str(getattr(parent_insert.dxf, "handle", "") or "")
        issues = list(issues) + ["FROM_INSERT"]

    raw = _make_raw_entity(
        geom=geom,
        ent=ent,
        source_file=source_file,
        source_fmt=source_fmt,
        source_units=source_units,
        scale_to_cm=scale_to_cm,
        next_id=next_id,
        issues=issues,
        classification_override=classification_override,
        source_layer=source_layer,
        source_color=source_color,
        source_linetype=source_linetype,
        source_entity_type=et,
        block_name=block_name,
        parent_insert_handle=parent_insert_handle,
    )
    if raw is None:
        return [], next_id

    return [raw], next_id + 1


def run(
    input_path: Path,
    output_dir: Optional[Path] = None,
    tolerance_mode: str = "NORMAL",
) -> List[RawEntity]:
    cfg = PipelineConfig(tolerance_mode=tolerance_mode).apply_tolerance_mode()
    doc = _read_dxf(input_path)
    source_units, scale_to_cm, insunits_code = _resolve_units(doc, cfg)

    entities: List[RawEntity] = []
    skipped_by_type: Dict[str, int] = {}
    extracted_by_type: Dict[str, int] = {}
    approximated_by_type: Dict[str, int] = {}
    from_insert_count = 0

    next_id = 1
    for ent in doc.modelspace():
        try:
            extracted, next_id = _entities_from_dxf_object(
                ent,
                cfg,
                scale_to_cm,
                str(input_path),
                "DXF",
                source_units,
                next_id,
            )
        except Exception:
            extracted = []

        if not extracted:
            et = ent.dxftype()
            skipped_by_type[et] = skipped_by_type.get(et, 0) + 1
            continue

        kept_from_this_ent = 0
        for raw in extracted:
            geom = raw.geometry()
            if isinstance(geom, LineString) and geom.length < cfg.min_segment_cm:
                skipped_by_type[raw.source.entity_type] = skipped_by_type.get(raw.source.entity_type, 0) + 1
                continue

            entities.append(raw)
            kept_from_this_ent += 1
            extracted_by_type[raw.source.entity_type] = extracted_by_type.get(raw.source.entity_type, 0) + 1
            if raw.issues:
                approximated_by_type[raw.source.entity_type] = approximated_by_type.get(raw.source.entity_type, 0) + 1
            if raw.source.parent_insert_handle:
                from_insert_count += 1

        if kept_from_this_ent == 0:
            skipped_by_type[ent.dxftype()] = skipped_by_type.get(ent.dxftype(), 0) + 1

    logger.info(
        f"Extraction: {len(entities)} entities | source_units={source_units} "
        f"| scale_to_cm={scale_to_cm} | insunits={insunits_code} | from_insert={from_insert_count}"
    )
    if skipped_by_type:
        logger.info(f"Extraction skipped by type: {skipped_by_type}")
    if approximated_by_type:
        logger.info(f"Extraction approximated/proxy by type: {approximated_by_type}")

    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        save_entities_json(
            entities,
            output_dir / f"{input_path.stem}_raw_entities.geojson",
            metadata={
                "stage": "ingestion_extraction",
                "input_file": str(input_path),
                "insunits_code": insunits_code,
                "source_units": source_units,
                "scale_to_cm": scale_to_cm,
                "tolerance_mode": tolerance_mode,
                "expand_inserts": cfg.expand_inserts,
                "insert_virtual_depth": cfg.insert_virtual_depth,
                "from_insert_count": from_insert_count,
                "extracted_by_type": extracted_by_type,
                "skipped_by_type": skipped_by_type,
                "approximated_by_type": approximated_by_type,
            },
        )

    return entities


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Coffrage Core")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default="./output_coffrage")
    ap.add_argument("--inspect", action="store_true")
    args = ap.parse_args()

    input_path = Path(args.input)
    if args.inspect:
        print(json.dumps(inspect_file(input_path), indent=2, ensure_ascii=False))
    else:
        run(input_path, Path(args.output))