#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Sequence, Tuple

import ezdxf
import numpy as np
from loguru import logger

try:
    import cv2
    HAS_CV2 = True
except Exception:
    cv2 = None
    HAS_CV2 = False

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    HAS_TORCH = True
except Exception:
    torch = None
    nn = None
    F = None
    HAS_TORCH = False

try:
    import segmentation_models_pytorch as smp
    HAS_SMP = True
except Exception:
    smp = None
    HAS_SMP = False

try:
    import onnxruntime as ort
    HAS_ONNX = True
except Exception:
    ort = None
    HAS_ONNX = False

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except Exception:
    fitz = None
    HAS_FITZ = False

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.config import Configuration
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend


MAX_RASTER_SIDE_PX = 6000
MIN_RASTER_SIDE_PX = 512
MODEL_TILE_SIZE = 1024
MODEL_TILE_OVERLAP = 128
MAX_INSERT_DEPTH_FOR_BOUNDS = 3
MAX_BOUNDS_EXPANSION_ITERS = 5
INK_WHITE_THRESHOLD = 248
INK_BORDER_MARGIN_PX = 4

ANNOTATION_ENTITY_TYPES = {
    "TEXT",
    "MTEXT",
    "DIMENSION",
    "LEADER",
    "MULTILEADER",
    "ATTDEF",
    "ATTRIB",
}
DIRECT_ARCHIVE_ENTITY_TYPES = ANNOTATION_ENTITY_TYPES | {"HATCH"}
RENDER_NOISE_ENTITY_TYPES = DIRECT_ARCHIVE_ENTITY_TYPES | {"POINT"}

DXF_UNIT_TO_CM: dict[int, tuple[str, float]] = {
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

ENTITY_BOX_RATIO_REJECT = 25.0
GLOBAL_DIAG_RATIO_REJECT = 20.0
GLOBAL_DIAG_P90_FACTOR = 6.0


if HAS_TORCH:
    class _TinyFallbackNet(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
            self.conv2 = nn.Conv2d(16, 3, 3, padding=1)

        def forward(self, x):
            x = torch.relu(self.conv1(x))
            return self.conv2(x)
else:
    _TinyFallbackNet = None  # type: ignore[assignment]


@dataclass(frozen=True)
class BoundsInfo:
    bounds: Tuple[float, float, float, float]
    robust: bool
    total_boxes: int
    kept_boxes: int


@dataclass(frozen=True)
class UnitsInfo:
    source_units: str
    scale_to_cm: float
    insunits_code: int


@dataclass(frozen=True)
class RasterSourceInfo:
    origin: str
    vision_path: str
    cropped: bool
    padded: bool


@dataclass(frozen=True)
class SamplePoint:
    x: float
    y: float
    weight: float
    role: str
    group_id: int


@dataclass(frozen=True)
class PatchStats:
    exact_class: int
    dominant_class: Optional[int]
    dark_ratio: float
    structure_ratio: float
    wall_ratio: float
    column_ratio: float


def _odd(value: int) -> int:
    return value if value % 2 == 1 else value + 1


def _safe_bbox_from_points(points: Sequence[Tuple[float, float]]) -> Optional[Tuple[float, float, float, float]]:
    if not points:
        return None
    xs = [p[0] for p in points if math.isfinite(p[0])]
    ys = [p[1] for p in points if math.isfinite(p[1])]
    if not xs or not ys:
        return None
    return min(xs), min(ys), max(xs), max(ys)


def _bbox_diag(box: Tuple[float, float, float, float]) -> float:
    min_x, min_y, max_x, max_y = box
    return math.hypot(max_x - min_x, max_y - min_y)


def _bbox_aspect(box: Tuple[float, float, float, float]) -> float:
    min_x, min_y, max_x, max_y = box
    w = max(max_x - min_x, 1e-9)
    h = max(max_y - min_y, 1e-9)
    return max(w / h, h / w)


def _union_bounds(boxes: Sequence[Tuple[float, float, float, float]]) -> Tuple[float, float, float, float]:
    min_x = min(b[0] for b in boxes)
    min_y = min(b[1] for b in boxes)
    max_x = max(b[2] for b in boxes)
    max_y = max(b[3] for b in boxes)
    return min_x, min_y, max_x, max_y


def _pad_bounds(bounds: Tuple[float, float, float, float], ratio: float = 0.08, min_pad: float = 10.0) -> Tuple[float, float, float, float]:
    min_x, min_y, max_x, max_y = bounds
    w = max(max_x - min_x, 1.0)
    h = max(max_y - min_y, 1.0)
    pad_x = max(w * ratio, min_pad)
    pad_y = max(h * ratio, min_pad)
    return min_x - pad_x, min_y - pad_y, max_x + pad_x, max_y + pad_y


def _expand_bounds(
    bounds: Tuple[float, float, float, float],
    *,
    left: bool,
    right: bool,
    bottom: bool,
    top: bool,
    expand_ratio: float = 0.22,
    min_expand: float = 10.0,
) -> Tuple[float, float, float, float]:
    min_x, min_y, max_x, max_y = bounds
    w = max(max_x - min_x, 1.0)
    h = max(max_y - min_y, 1.0)
    dx = max(w * expand_ratio, min_expand)
    dy = max(h * expand_ratio, min_expand)

    if left:
        min_x -= dx
    if right:
        max_x += dx
    if bottom:
        min_y -= dy
    if top:
        max_y += dy

    return min_x, min_y, max_x, max_y


def _entity_bbox_native(ent) -> Optional[Tuple[float, float, float, float]]:
    try:
        bbox = ent.bbox()
    except Exception:
        bbox = None
    if bbox is None:
        return None
    try:
        min_x = float(bbox.extmin.x)
        min_y = float(bbox.extmin.y)
        max_x = float(bbox.extmax.x)
        max_y = float(bbox.extmax.y)
    except Exception:
        return None
    if not all(math.isfinite(v) for v in (min_x, min_y, max_x, max_y)):
        return None
    if max_x < min_x or max_y < min_y:
        return None
    return min_x, min_y, max_x, max_y


def _append_point(points: list[Tuple[float, float]], x: float, y: float) -> None:
    if math.isfinite(x) and math.isfinite(y):
        points.append((float(x), float(y)))


def _entity_points_for_bounds(ent, *, depth: int = 0, max_depth: int = MAX_INSERT_DEPTH_FOR_BOUNDS) -> list[Tuple[float, float]]:
    et = ent.dxftype()
    points: list[Tuple[float, float]] = []

    try:
        if et == "LINE":
            _append_point(points, float(ent.dxf.start.x), float(ent.dxf.start.y))
            _append_point(points, float(ent.dxf.end.x), float(ent.dxf.end.y))
            return points

        if et == "LWPOLYLINE":
            for p in ent.get_points("xy"):
                _append_point(points, float(p[0]), float(p[1]))
            return points

        if et == "POLYLINE":
            try:
                for v in ent.vertices:
                    _append_point(points, float(v.dxf.location.x), float(v.dxf.location.y))
            except Exception:
                pass
            return points

        if et == "CIRCLE":
            c = ent.dxf.center
            r = float(ent.dxf.radius)
            for dx, dy in ((-r, 0.0), (r, 0.0), (0.0, -r), (0.0, r)):
                _append_point(points, float(c.x) + dx, float(c.y) + dy)
            return points

        if et == "ARC":
            c = ent.dxf.center
            r = float(ent.dxf.radius)
            start = math.radians(float(ent.dxf.start_angle))
            end = math.radians(float(ent.dxf.end_angle))
            for ang in (start, end):
                _append_point(points, float(c.x) + r * math.cos(ang), float(c.y) + r * math.sin(ang))
            return points

        if et == "ELLIPSE":
            c = ent.dxf.center
            major = ent.dxf.major_axis
            ratio = float(ent.dxf.ratio or 1.0)
            mx, my = float(major.x), float(major.y)
            nx, ny = -my * ratio, mx * ratio
            for dx, dy in ((mx, my), (-mx, -my), (nx, ny), (-nx, -ny)):
                _append_point(points, float(c.x) + dx, float(c.y) + dy)
            return points

        if et == "SPLINE":
            for attr_name in ("fit_points", "control_points"):
                pts = getattr(ent, attr_name, None)
                if pts:
                    for p in pts:
                        _append_point(points, float(p.x), float(p.y))
                    if points:
                        return points

        if et == "POINT":
            _append_point(points, float(ent.dxf.location.x), float(ent.dxf.location.y))
            return points

        if et in {"TEXT", "MTEXT", "ATTDEF", "ATTRIB"}:
            insert = getattr(ent.dxf, "insert", None)
            if insert is not None:
                _append_point(points, float(insert.x), float(insert.y))
            return points

        if et == "INSERT":
            insert = getattr(ent.dxf, "insert", None)
            if insert is not None:
                _append_point(points, float(insert.x), float(insert.y))
            if depth < max_depth:
                try:
                    for child in ent.virtual_entities():
                        points.extend(_entity_points_for_bounds(child, depth=depth + 1, max_depth=max_depth))
                except Exception:
                    pass
            return points

        if et == "HATCH":
            try:
                for path in ent.paths:
                    if hasattr(path, "vertices"):
                        for item in path.vertices:
                            _append_point(points, float(item[0]), float(item[1]))
            except Exception:
                pass
            return points

    except Exception:
        return points

    return points


def _merge_entity_bbox_candidates(
    candidates: Sequence[Tuple[float, float, float, float]],
) -> Optional[Tuple[float, float, float, float]]:
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]

    ordered = sorted(candidates, key=_bbox_diag)
    smallest = ordered[0]
    largest = ordered[-1]

    small_diag = max(_bbox_diag(smallest), 1e-9)
    large_diag = _bbox_diag(largest)

    if large_diag / small_diag >= ENTITY_BOX_RATIO_REJECT:
        return smallest

    return _union_bounds(ordered)


def _collect_entity_extent_box(ent) -> Optional[Tuple[float, float, float, float]]:
    candidates: list[Tuple[float, float, float, float]] = []

    native_bbox = _entity_bbox_native(ent)
    if native_bbox is not None:
        candidates.append(native_bbox)

    pts = _entity_points_for_bounds(ent, depth=0, max_depth=MAX_INSERT_DEPTH_FOR_BOUNDS)
    pts_bbox = _safe_bbox_from_points(pts)
    if pts_bbox is not None:
        candidates.append(pts_bbox)

    return _merge_entity_bbox_candidates(candidates)


def _looks_like_annotation_layer(layer_name: str) -> bool:
    u = (layer_name or "").upper()
    return any(token in u for token in ("TEXT", "MTEXT", "DIM", "COTA", "NOTE", "ANNOT"))


def _strip_render_noise(render_doc: ezdxf.document.Drawing) -> int:
    msp = render_doc.modelspace()
    removed = 0

    for ent in list(msp):
        et = ent.dxftype()
        layer = getattr(ent.dxf, "layer", "") or ""

        if et in RENDER_NOISE_ENTITY_TYPES or _looks_like_annotation_layer(layer):
            try:
                msp.delete_entity(ent)
                removed += 1
            except Exception:
                pass

    return removed


def _collect_visible_boxes_for_extent(doc: ezdxf.document.Drawing) -> list[Tuple[float, float, float, float]]:
    entity_boxes: list[Tuple[float, float, float, float]] = []

    for ent in doc.modelspace():
        et = ent.dxftype()
        layer = getattr(ent.dxf, "layer", "") or ""

        if et in RENDER_NOISE_ENTITY_TYPES or _looks_like_annotation_layer(layer):
            continue

        box = _collect_entity_extent_box(ent)
        if box is not None:
            entity_boxes.append(box)

    return entity_boxes


def _select_global_bounds(boxes: Sequence[Tuple[float, float, float, float]]) -> BoundsInfo:
    if not boxes:
        return BoundsInfo(bounds=(0.0, 0.0, 100.0, 100.0), robust=False, total_boxes=0, kept_boxes=0)

    all_bounds = _union_bounds(boxes)
    all_diag = _bbox_diag(all_bounds)
    all_aspect = _bbox_aspect(all_bounds)

    if len(boxes) < 20:
        return BoundsInfo(bounds=_pad_bounds(all_bounds), robust=False, total_boxes=len(boxes), kept_boxes=len(boxes))

    diags = np.array([_bbox_diag(b) for b in boxes], dtype=np.float64)
    median_diag = max(float(np.median(diags)), 1e-6)
    p90_diag = max(float(np.percentile(diags, 90)), median_diag)
    max_allowed_diag = max(50.0, median_diag * GLOBAL_DIAG_RATIO_REJECT, p90_diag * GLOBAL_DIAG_P90_FACTOR)

    filtered_boxes = [box for box, diag in zip(boxes, diags) if float(diag) <= max_allowed_diag]

    if len(filtered_boxes) < max(10, int(0.70 * len(boxes))):
        return BoundsInfo(bounds=_pad_bounds(all_bounds), robust=False, total_boxes=len(boxes), kept_boxes=len(boxes))

    filtered_bounds = _union_bounds(filtered_boxes)
    filtered_diag = _bbox_diag(filtered_bounds)
    filtered_aspect = _bbox_aspect(filtered_bounds)

    should_use_filtered = (
        all_diag > filtered_diag * 3.0
        or all_aspect > filtered_aspect * 4.0
    )

    if should_use_filtered:
        return BoundsInfo(
            bounds=_pad_bounds(filtered_bounds),
            robust=True,
            total_boxes=len(boxes),
            kept_boxes=len(filtered_boxes),
        )

    return BoundsInfo(bounds=_pad_bounds(all_bounds), robust=False, total_boxes=len(boxes), kept_boxes=len(boxes))


def _infer_unitless_scale_from_bounds(bounds_info: BoundsInfo) -> Tuple[str, float]:
    min_x, min_y, max_x, max_y = bounds_info.bounds
    width = abs(max_x - min_x)
    height = abs(max_y - min_y)
    max_dim = max(width, height)

    if max_dim <= 120.0:
        return "inferred_m", 100.0
    if max_dim >= 8000.0:
        return "inferred_mm", 0.1
    return "inferred_cm", 1.0


def _resolve_units(doc: ezdxf.document.Drawing) -> UnitsInfo:
    insunits_code = int(doc.header.get("$INSUNITS", 0) or 0)

    if insunits_code in DXF_UNIT_TO_CM and insunits_code != 0:
        unit_name, factor = DXF_UNIT_TO_CM[insunits_code]
        return UnitsInfo(source_units=unit_name, scale_to_cm=factor, insunits_code=insunits_code)

    boxes = _collect_visible_boxes_for_extent(doc)
    bounds_info = _select_global_bounds(boxes)
    inferred_name, inferred_scale = _infer_unitless_scale_from_bounds(bounds_info)
    return UnitsInfo(source_units=inferred_name, scale_to_cm=inferred_scale, insunits_code=insunits_code)


def _bbox_doc(doc: ezdxf.document.Drawing) -> BoundsInfo:
    return _select_global_bounds(_collect_visible_boxes_for_extent(doc))


def _compute_raster_shape(
    bounds: Tuple[float, float, float, float],
    dpi: int,
    scale_to_cm: float,
) -> Tuple[int, int]:
    min_x, min_y, max_x, max_y = bounds
    width_cm = max((max_x - min_x) * scale_to_cm, 1.0)
    height_cm = max((max_y - min_y) * scale_to_cm, 1.0)

    px_per_cm = max(dpi / 100.0, 0.5)
    width_px = width_cm * px_per_cm
    height_px = height_cm * px_per_cm

    max_side = max(width_px, height_px)
    if max_side < MIN_RASTER_SIDE_PX:
        factor = MIN_RASTER_SIDE_PX / max_side
        width_px *= factor
        height_px *= factor

    max_side = max(width_px, height_px)
    if max_side > MAX_RASTER_SIDE_PX:
        factor = MAX_RASTER_SIDE_PX / max_side
        width_px *= factor
        height_px *= factor

    return max(256, int(round(width_px))), max(256, int(round(height_px)))


def _render_gray_from_dxf(
    doc: ezdxf.document.Drawing,
    bounds: Tuple[float, float, float, float],
    units_info: UnitsInfo,
    dpi: int,
) -> np.ndarray:
    min_x, min_y, max_x, max_y = bounds
    width_px, height_px = _compute_raster_shape(bounds, dpi, units_info.scale_to_cm)

    fig = plt.figure(figsize=(width_px / dpi, height_px / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])

    ctx = RenderContext(doc)
    cfg = Configuration(
        background_policy="custom",
        custom_bg_color="#FFFFFF",
        custom_fg_color="#000000",
    )
    backend = MatplotlibBackend(ax)
    Frontend(ctx, backend, config=cfg).draw_layout(doc.modelspace(), finalize=True)

    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    ax.set_aspect("auto")
    ax.axis("off")

    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    plt.close(fig)

    if HAS_CV2:
        return cv2.cvtColor(rgba, cv2.COLOR_RGBA2GRAY)
    return (0.299 * rgba[:, :, 0] + 0.587 * rgba[:, :, 1] + 0.114 * rgba[:, :, 2]).astype(np.uint8)


def _ink_bbox(gray: np.ndarray, white_threshold: int = INK_WHITE_THRESHOLD) -> Optional[Tuple[int, int, int, int]]:
    ys, xs = np.where(gray < white_threshold)
    if len(xs) == 0 or len(ys) == 0:
        return None
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())


def _ink_touches_border(
    ink_bbox: Tuple[int, int, int, int],
    gray_shape: Tuple[int, int],
    margin_px: int = INK_BORDER_MARGIN_PX,
) -> tuple[bool, bool, bool, bool]:
    x0, y0, x1, y1 = ink_bbox
    h, w = gray_shape
    left = x0 <= margin_px
    right = x1 >= (w - 1 - margin_px)
    top = y0 <= margin_px
    bottom = y1 >= (h - 1 - margin_px)
    return left, right, bottom, top


def _crop_to_content(gray: np.ndarray, pad_px: int = 8) -> tuple[np.ndarray, bool]:
    ink = _ink_bbox(gray)
    if ink is None:
        return gray, False

    x0, y0, x1, y1 = ink
    h, w = gray.shape
    x0 = max(0, x0 - pad_px)
    y0 = max(0, y0 - pad_px)
    x1 = min(w - 1, x1 + pad_px)
    y1 = min(h - 1, y1 + pad_px)

    cropped = gray[y0:y1 + 1, x0:x1 + 1]
    if cropped.size == 0:
        return gray, False
    return cropped, True


def _resize_gray(gray: np.ndarray, target_w: int, target_h: int) -> np.ndarray:
    if HAS_CV2:
        return cv2.resize(gray, (target_w, target_h), interpolation=cv2.INTER_AREA)

    ys = np.linspace(0, gray.shape[0] - 1, target_h).astype(np.int32)
    xs = np.linspace(0, gray.shape[1] - 1, target_w).astype(np.int32)
    return gray[np.ix_(ys, xs)]


def _pad_image_to_aspect(gray: np.ndarray, target_aspect: float) -> tuple[np.ndarray, bool]:
    h, w = gray.shape
    image_aspect = w / max(h, 1)

    if target_aspect <= 0:
        return gray, False

    if abs(image_aspect - target_aspect) <= 0.02:
        return gray, False

    if image_aspect < target_aspect:
        target_w = int(round(h * target_aspect))
        pad_total = max(target_w - w, 0)
        pad_left = pad_total // 2
        pad_right = pad_total - pad_left
        padded = np.pad(gray, ((0, 0), (pad_left, pad_right)), mode="constant", constant_values=255)
        return padded, True

    target_h = int(round(w / target_aspect))
    pad_total = max(target_h - h, 0)
    pad_top = pad_total // 2
    pad_bottom = pad_total - pad_top
    padded = np.pad(gray, ((pad_top, pad_bottom), (0, 0)), mode="constant", constant_values=255)
    return padded, True


def _load_external_raster(
    vision_path: Path,
    dpi: int,
    dxf_bounds: Tuple[float, float, float, float],
    units_info: UnitsInfo,
) -> tuple[np.ndarray, RasterSourceInfo]:
    suffix = vision_path.suffix.lower()
    gray: np.ndarray

    if suffix == ".pdf":
        if not HAS_FITZ:
            raise RuntimeError("PyMuPDF (fitz) is required to use a PDF as vision source")
        pdf = fitz.open(str(vision_path))
        if pdf.page_count == 0:
            raise RuntimeError(f"Empty PDF: {vision_path}")
        page = pdf.load_page(0)
        zoom = dpi / 72.0
        matrix = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
        pdf.close()

        if arr.ndim == 3 and arr.shape[2] >= 3:
            if HAS_CV2:
                gray = cv2.cvtColor(arr[:, :, :3], cv2.COLOR_RGB2GRAY)
            else:
                gray = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(np.uint8)
        else:
            gray = arr.astype(np.uint8)

        origin = "pdf"

    elif suffix in {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp"}:
        if HAS_CV2:
            gray = cv2.imread(str(vision_path), cv2.IMREAD_GRAYSCALE)
            if gray is None:
                raise RuntimeError(f"Unable to read image: {vision_path}")
        else:
            img = plt.imread(str(vision_path))
            if img.ndim == 2:
                gray = (img * 255).astype(np.uint8) if img.dtype != np.uint8 else img
            else:
                rgb = img[:, :, :3]
                if rgb.dtype != np.uint8:
                    rgb = (rgb * 255).astype(np.uint8)
                gray = (0.299 * rgb[:, :, 0] + 0.587 * rgb[:, :, 1] + 0.114 * rgb[:, :, 2]).astype(np.uint8)

        origin = "image"
    else:
        raise ValueError(f"Unsupported vision source: {vision_path.suffix}")

    cropped_gray, cropped = _crop_to_content(gray)
    min_x, min_y, max_x, max_y = dxf_bounds
    target_aspect = (max_x - min_x) / max(max_y - min_y, 1e-9)
    padded_gray, padded = _pad_image_to_aspect(cropped_gray, target_aspect)

    target_w, target_h = _compute_raster_shape(dxf_bounds, dpi, units_info.scale_to_cm)
    final_gray = _resize_gray(padded_gray, target_w, target_h)

    return final_gray, RasterSourceInfo(
        origin=origin,
        vision_path=str(vision_path),
        cropped=cropped,
        padded=padded,
    )


def _rasterize_from_dxf(
    render_doc: ezdxf.document.Drawing,
    units_info: UnitsInfo,
    dpi: int = 200,
) -> Tuple[np.ndarray, BoundsInfo]:
    logger.info("M0: rasterisation DXF -> image")
    bounds_info = _bbox_doc(render_doc)
    bounds = bounds_info.bounds

    gray = _render_gray_from_dxf(render_doc, bounds, units_info, dpi)
    expanded = False

    for _ in range(MAX_BOUNDS_EXPANSION_ITERS):
        ink_bbox = _ink_bbox(gray)
        if ink_bbox is None:
            break

        left, right, bottom, top = _ink_touches_border(ink_bbox, gray.shape)
        if not any((left, right, bottom, top)):
            break

        bounds = _expand_bounds(
            bounds,
            left=left,
            right=right,
            bottom=bottom,
            top=top,
            expand_ratio=0.22,
            min_expand=10.0,
        )
        gray = _render_gray_from_dxf(render_doc, bounds, units_info, dpi)
        expanded = True

    final_bounds = BoundsInfo(
        bounds=bounds,
        robust=(bounds_info.robust or expanded),
        total_boxes=bounds_info.total_boxes,
        kept_boxes=bounds_info.kept_boxes,
    )

    logger.info(
        f"M0: raster size={gray.shape[1]}x{gray.shape[0]} px"
        + (" | auto-expanded to fit drawing extent" if expanded else " | using drawing extent")
    )
    return gray, final_bounds


def _compatible_with_fallback_state_dict(state_dict: dict) -> bool:
    if _TinyFallbackNet is None:
        return False
    required = {"conv1.weight", "conv1.bias", "conv2.weight", "conv2.bias"}
    return required.issubset(set(state_dict.keys()))


def _load_model_config(model_path: Path) -> dict:
    config_path = model_path.with_name("model_config.json")
    default_config = {
        "encoder_name": "resnet34",
        "input_size": [MODEL_TILE_SIZE, MODEL_TILE_SIZE],
        "in_channels": 3,
        "classes": 3,
        "class_names": ["background", "wall", "column"],
        "normalization": {"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}
    }
    if config_path.exists():
        try:
            user_config = json.loads(config_path.read_text(encoding="utf-8"))
            default_config.update(user_config)
            logger.info(f"M0: loaded model config from {config_path.name}")
        except Exception as exc:
            logger.warning(f"M0: failed to load model config {config_path}: {exc}")
    return default_config


def _load_model(model_path: Optional[Path]) -> tuple[Any, dict]:
    if model_path is None:
        return None, {}
    if not model_path.exists():
        raise FileNotFoundError(f"M0: model file not found: {model_path}")

    config = _load_model_config(model_path)
    suffix = model_path.suffix.lower()

    if suffix == ".onnx":
        if not HAS_ONNX:
            raise RuntimeError("M0: onnxruntime is required to load .onnx models. Install it with: pip install onnxruntime")
        try:
            session = ort.InferenceSession(str(model_path))
            logger.info(f"M0: ONNX model loaded ({model_path.name})")
            return session, config
        except Exception as exc:
            raise RuntimeError(f"M0: failed to load ONNX model: {exc}")

    if not HAS_TORCH:
        raise RuntimeError("M0: torch is required to load a .pth/.pt model. Install it with: pip install torch")

    # Try loading as TorchScript first
    try:
        model = torch.jit.load(str(model_path), map_location="cpu")
        model.eval()
        logger.info(f"M0: torchscript model loaded ({model_path.name})")
        return model, config
    except Exception:
        pass

    # Try loading as state dict with SMP
    if HAS_SMP:
        try:
            model = smp.Unet(
                encoder_name=config["encoder_name"],
                encoder_weights=None,
                in_channels=config["in_channels"],
                classes=config["classes"],
            )
            state_dict = torch.load(model_path, map_location="cpu", weights_only=True)
            model.load_state_dict(state_dict)
            model.eval()
            logger.info(f"M0: SMP model loaded with state_dict ({model_path.name})")
            return model, config
        except Exception as exc:
            logger.debug(f"M0: SMP load failed, trying generic torch load: {exc}")

    # Fallback to generic torch load
    try:
        payload = torch.load(str(model_path), map_location="cpu")
        if isinstance(payload, nn.Module):
            payload.eval()
            logger.info(f"M0: torch module loaded ({model_path.name})")
            return payload, config
        if isinstance(payload, dict) and isinstance(payload.get("model"), nn.Module):
            model = payload["model"]
            model.eval()
            logger.info(f"M0: embedded torch module loaded ({model_path.name})")
            return model, config

        state_dict = payload.get("state_dict") if isinstance(payload, dict) and "state_dict" in payload else payload
        if isinstance(state_dict, dict) and _compatible_with_fallback_state_dict(state_dict):
            model = _TinyFallbackNet()
            model.load_state_dict(state_dict, strict=True)
            model.eval()
            logger.warning(f"M0: loaded legacy fallback checkpoint ({model_path.name})")
            return model, config
    except Exception as exc:
        raise RuntimeError(f"M0: failed to load torch model {model_path}: {exc}")

    raise RuntimeError(f"M0: unsupported model format for {model_path.name}")


def _extract_logits(output):
    if not HAS_TORCH:
        raise RuntimeError("Torch unavailable")

    if torch.is_tensor(output):
        return output

    if isinstance(output, dict):
        for key in ("out", "logits", "mask", "pred"):
            value = output.get(key)
            if torch.is_tensor(value):
                return value
        for value in output.values():
            if torch.is_tensor(value):
                return value

    if isinstance(output, (tuple, list)):
        for item in output:
            if torch.is_tensor(item):
                return item

    raise RuntimeError("M0: unsupported model output format")


def _run_model_once(model, tile: np.ndarray, config: dict):
    # tile is (H, W) or (H, W, C)
    norm = config.get("normalization", {})
    mean = np.array(norm.get("mean", [0.485, 0.456, 0.406]), dtype=np.float32)
    std = np.array(norm.get("std", [0.229, 0.224, 0.225]), dtype=np.float32)

    in_channels = config.get("in_channels", 3)

    if in_channels == 3:
        if tile.ndim == 2:
            tile_norm = np.stack([tile]*3, axis=-1)
        else:
            tile_norm = tile
        tile_norm = (tile_norm - mean) / std
    else:
        tile_norm = (tile - mean[0]) / std[0]
        if tile_norm.ndim == 2:
            tile_norm = tile_norm[:, :, np.newaxis]

    if HAS_ONNX and isinstance(model, ort.InferenceSession):
        inp = tile_norm.transpose(2, 0, 1)[np.newaxis, ...]
        input_name = model.get_inputs()[0].name
        output = model.run(None, {input_name: inp})
        logits = output[0] if isinstance(output, (list, tuple)) else output
        return logits

    if HAS_TORCH and isinstance(model, nn.Module):
        inp = torch.from_numpy(tile_norm.transpose(2, 0, 1)).unsqueeze(0).float()
        with torch.no_grad():
            output = model(inp)
            logits = _extract_logits(output)
            if logits.shape[-2:] != tile.shape[:2]:
                logits = F.interpolate(logits, size=tile.shape[:2], mode="bilinear", align_corners=False)
            return logits.cpu().numpy()

    raise RuntimeError("M0: unsupported model type for inference")


def _tile_positions(size: int, tile_size: int, overlap: int) -> list[Tuple[int, int]]:
    if size <= tile_size:
        return [(0, size)]

    stride = max(1, tile_size - overlap)
    positions: list[Tuple[int, int]] = []
    start = 0
    while start < size:
        end = min(start + tile_size, size)
        start = max(0, end - tile_size)
        positions.append((start, end))
        if end >= size:
            break
        start += stride
    return positions


def _segment_with_model(gray: np.ndarray, model, config: dict) -> np.ndarray:
    arr = gray.astype(np.float32) / 255.0
    h, w = arr.shape

    tile_size = config.get("input_size", [MODEL_TILE_SIZE, MODEL_TILE_SIZE])[0]
    ys = _tile_positions(h, tile_size, MODEL_TILE_OVERLAP)
    xs = _tile_positions(w, tile_size, MODEL_TILE_OVERLAP)

    sum_logits: Optional[np.ndarray] = None
    visits = np.zeros((h, w), dtype=np.float32)

    for y0, y1 in ys:
        for x0, x1 in xs:
            tile = arr[y0:y1, x0:x1]
            tile_h, tile_w = tile.shape

            if tile_h < tile_size or tile_w < tile_size:
                padded = np.ones((tile_size, tile_size), dtype=np.float32)
                padded[:tile_h, :tile_w] = tile
                tile = padded

            logits = _run_model_once(model, tile, config)
            # logits is (1, C, H, W) or (C, H, W)
            if logits.ndim == 4:
                logits = logits[0]

            tile_logits = logits[:, :tile_h, :tile_w].astype(np.float32)

            if sum_logits is None:
                sum_logits = np.zeros((logits.shape[0], h, w), dtype=np.float32)

            sum_logits[:, y0:y1, x0:x1] += tile_logits
            visits[y0:y1, x0:x1] += 1.0

    if sum_logits is None:
        raise RuntimeError("M0: empty model inference")

    avg_logits = sum_logits / np.maximum(visits[None, :, :], 1.0)
    return np.argmax(avg_logits, axis=0).astype(np.uint8)


def _segment_morph(
    gray: np.ndarray,
    bounds: Tuple[float, float, float, float],
    units_info: UnitsInfo,
) -> np.ndarray:
    if not HAS_CV2:
        raise RuntimeError("M0: OpenCV is required when no torch model is available")

    h, w = gray.shape
    min_x, min_y, max_x, max_y = bounds

    width_cm = max((max_x - min_x) * units_info.scale_to_cm, 1e-6)
    height_cm = max((max_y - min_y) * units_info.scale_to_cm, 1e-6)
    px_per_cm_x = (w - 1) / width_cm
    px_per_cm_y = (h - 1) / height_cm
    px_per_cm = max(min(px_per_cm_x, px_per_cm_y), 0.05)

    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    small_area_px = max(12, int(round((px_per_cm * 2.0) ** 2)))
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bw, connectivity=8)
    clean = np.zeros_like(bw)
    for label in range(1, num_labels):
        area_px = int(stats[label, cv2.CC_STAT_AREA])
        if area_px >= small_area_px:
            clean[labels == label] = 255

    wall_bridge_px = _odd(max(5, min(31, int(round(px_per_cm * 18.0)))))
    col_bridge_px = _odd(max(3, min(21, int(round(px_per_cm * 12.0)))))

    wall_kernel = np.ones((wall_bridge_px, wall_bridge_px), np.uint8)
    col_kernel = np.ones((col_bridge_px, col_bridge_px), np.uint8)

    wall_closed = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, wall_kernel)
    col_closed = cv2.morphologyEx(clean, cv2.MORPH_CLOSE, col_kernel)

    mask = np.zeros_like(gray, dtype=np.uint8)
    max_component_area_px = h * w * 0.80

    col_contours, _ = cv2.findContours(col_closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in col_contours:
        area_px = float(cv2.contourArea(contour))
        if area_px < small_area_px or area_px > max_component_area_px:
            continue

        x, y, ww, hh = cv2.boundingRect(contour)
        width_obj_cm = ww / max(px_per_cm_x, 1e-6)
        height_obj_cm = hh / max(px_per_cm_y, 1e-6)
        min_dim_cm = min(width_obj_cm, height_obj_cm)
        max_dim_cm = max(width_obj_cm, height_obj_cm)
        aspect = max_dim_cm / max(min_dim_cm, 0.1)
        fill_ratio = area_px / max(ww * hh, 1)

        is_column = (
            5.0 <= min_dim_cm <= 200.0
            and 5.0 <= max_dim_cm <= 250.0
            and aspect <= 3.0
            and fill_ratio >= 0.10
        )
        if is_column:
            cv2.drawContours(mask, [contour], -1, 2, -1)

    wall_contours, _ = cv2.findContours(wall_closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in wall_contours:
        area_px = float(cv2.contourArea(contour))
        if area_px < small_area_px or area_px > max_component_area_px:
            continue

        x, y, ww, hh = cv2.boundingRect(contour)
        width_obj_cm = ww / max(px_per_cm_x, 1e-6)
        height_obj_cm = hh / max(px_per_cm_y, 1e-6)
        min_dim_cm = min(width_obj_cm, height_obj_cm)
        max_dim_cm = max(width_obj_cm, height_obj_cm)
        aspect = max_dim_cm / max(min_dim_cm, 0.1)
        fill_ratio = area_px / max(ww * hh, 1)

        is_wall = (
            3.0 <= min_dim_cm <= 150.0
            and max_dim_cm >= 30.0
            and aspect >= 1.5
            and fill_ratio >= 0.04
        )
        if is_wall:
            temp = np.zeros_like(mask)
            cv2.drawContours(temp, [contour], -1, 1, -1)
            mask = np.where(mask == 2, mask, temp).astype(np.uint8)

    return mask




def _build_visual_support_map(
    gray: np.ndarray,
    bounds: Tuple[float, float, float, float],
    units_info: UnitsInfo,
) -> np.ndarray:
    if not HAS_CV2:
        return (gray < INK_WHITE_THRESHOLD).astype(np.uint8) * 255

    h, w = gray.shape
    min_x, min_y, max_x, max_y = bounds
    width_cm = max((max_x - min_x) * units_info.scale_to_cm, 1e-6)
    height_cm = max((max_y - min_y) * units_info.scale_to_cm, 1e-6)
    px_per_cm_x = (w - 1) / width_cm
    px_per_cm_y = (h - 1) / height_cm
    px_per_cm = max(min(px_per_cm_x, px_per_cm_y), 0.05)

    _, bw = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    bridge_px = _odd(max(3, min(21, int(round(px_per_cm * 8.0)))))
    support_kernel = np.ones((bridge_px, bridge_px), np.uint8)
    support = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, support_kernel)

    dilate_px = max(1, min(5, int(round(px_per_cm * 1.0))))
    support = cv2.dilate(support, np.ones((dilate_px, dilate_px), np.uint8), iterations=1)
    return support


def _add_target_layers(doc: ezdxf.document.Drawing) -> None:
    for layer_name, color in (("BA_MURS", 1), ("BA_POTEAUX", 4), ("ARCHI_FOND", 8)):
        if layer_name in doc.layers:
            doc.layers.get(layer_name).color = color
        else:
            lyr = doc.layers.add(layer_name)
            lyr.color = color


def _apply_entity_style(ent, layer_name: str) -> None:
    ent.dxf.layer = layer_name
    if hasattr(ent.dxf, "color"):
        ent.dxf.color = 256  # BYLAYER
    if hasattr(ent.dxf, "linetype"):
        ent.dxf.linetype = "BYLAYER"
    if hasattr(ent.dxf, "lineweight"):
        ent.dxf.lineweight = -1  # BYLAYER


def _sample_entity_points(ent, units_info: UnitsInfo) -> list[SamplePoint]:
    et = ent.dxftype()
    offset_dist = 8.0 / max(units_info.scale_to_cm, 1e-9)

    try:
        if et == "LINE":
            s = ent.dxf.start
            t = ent.dxf.end
            dx, dy = float(t.x - s.x), float(t.y - s.y)
            length = math.hypot(dx, dy)
            if length < 1e-6:
                return []

            nx, ny = -dy / length * offset_dist, dx / length * offset_dist
            base_pts = _line_sample_points([(float(s.x), float(s.y)), (float(t.x), float(t.y))], 5)

            samples: list[SamplePoint] = []
            for group_id, (x, y) in enumerate(base_pts):
                samples.append(SamplePoint(x=x, y=y, weight=3.0, role="center", group_id=group_id))
                samples.append(SamplePoint(x=x + nx, y=y + ny, weight=1.0, role="left", group_id=group_id))
                samples.append(SamplePoint(x=x - nx, y=y - ny, weight=1.0, role="right", group_id=group_id))
            return samples

        if et in {"LWPOLYLINE", "POLYLINE"}:
            pts = _entity_points_for_bounds(ent)
            if len(pts) < 2:
                return []
            sampled = _line_sample_points(pts, 12)
            return [
                SamplePoint(x=x, y=y, weight=1.0, role="body", group_id=i)
                for i, (x, y) in enumerate(sampled)
            ]

        bbox_pts = _bbox_samples_from_points(_entity_points_for_bounds(ent))
        return [
            SamplePoint(x=x, y=y, weight=float(weight), role="body", group_id=i)
            for i, (x, y, weight) in enumerate(bbox_pts)
        ]

    except Exception:
        return []


def _is_closed_entity(ent) -> bool:
    et = ent.dxftype()

    if et in {"CIRCLE", "INSERT"}:
        return True

    if hasattr(ent, "closed"):
        try:
            return bool(ent.closed)
        except Exception:
            return False

    if hasattr(ent, "is_closed"):
        try:
            attr = ent.is_closed
            return bool(attr() if callable(attr) else attr)
        except Exception:
            return False

    return False


def _dominant_structure_class(local_mask: np.ndarray) -> Optional[int]:
    if local_mask.size == 0:
        return None
    counts_local = np.bincount(local_mask.flatten(), minlength=3)
    local_size = float(local_mask.size)

    if counts_local[1] > counts_local[2] and counts_local[1] >= (local_size * 0.30):
        return 1
    if counts_local[2] >= (local_size * 0.30):
        return 2
    return None


def _analyze_patch(
    mask: np.ndarray,
    support_map: np.ndarray,
    px: int,
    py: int,
    neighborhood: int,
) -> PatchStats:
    h, w = mask.shape
    exact_class = int(mask[py, px])

    y0, y1 = max(0, py - neighborhood), min(h, py + neighborhood + 1)
    x0, x1 = max(0, px - neighborhood), min(w, px + neighborhood + 1)

    local_mask = mask[y0:y1, x0:x1]
    local_support = support_map[y0:y1, x0:x1]

    dominant = _dominant_structure_class(local_mask)
    local_size = float(max(local_mask.size, 1))

    structure_ratio = float(np.count_nonzero(local_mask > 0)) / local_size
    wall_ratio = float(np.count_nonzero(local_mask == 1)) / local_size
    column_ratio = float(np.count_nonzero(local_mask == 2)) / local_size
    dark_ratio = float(np.count_nonzero(local_support > 0)) / float(max(local_support.size, 1))

    return PatchStats(
        exact_class=exact_class,
        dominant_class=dominant,
        dark_ratio=dark_ratio,
        structure_ratio=structure_ratio,
        wall_ratio=wall_ratio,
        column_ratio=column_ratio,
    )


def _group_is_visually_supported(role_stats: Dict[str, PatchStats]) -> bool:
    center = role_stats.get("center")
    left = role_stats.get("left")
    right = role_stats.get("right")
    body = role_stats.get("body")

    if body is not None:
        return body.dark_ratio >= 0.12 or body.structure_ratio >= 0.10 or body.exact_class != 0

    center_ok = center is not None and (center.dark_ratio >= 0.10 or center.structure_ratio >= 0.10 or center.exact_class != 0)
    left_ok = left is not None and (left.dark_ratio >= 0.12 or left.structure_ratio >= 0.10 or left.exact_class != 0)
    right_ok = right is not None and (right.dark_ratio >= 0.12 or right.structure_ratio >= 0.10 or right.exact_class != 0)

    if center_ok and (left_ok or right_ok):
        return True
    if left_ok and right_ok:
        return True
    return False


def _choose_class_fused(
    *,
    weighted_votes: dict[int, float],
    total_weight: float,
    avg_dark_ratio: float,
    supported_group_ratio: float,
    entity_type: str,
    is_closed: bool,
) -> int:
    if total_weight <= 0:
        return 0

    wall_ratio = weighted_votes.get(1, 0.0) / total_weight
    col_ratio = weighted_votes.get(2, 0.0) / total_weight
    structure_ratio = wall_ratio + col_ratio

    if structure_ratio < 0.10 and supported_group_ratio < 0.15 and avg_dark_ratio < 0.05:
        return 0

    if is_closed or entity_type in {"CIRCLE", "INSERT"}:
        if col_ratio >= 0.35 and (supported_group_ratio >= 0.40 or avg_dark_ratio >= 0.14):
            return 2
        if wall_ratio >= 0.55 and (supported_group_ratio >= 0.50 or avg_dark_ratio >= 0.18):
            return 1
        return 0

    if entity_type == "LINE":
        if col_ratio >= 0.50 and supported_group_ratio >= 0.40:
            return 2
        if wall_ratio >= 0.45 and supported_group_ratio >= 0.45 and avg_dark_ratio >= 0.08:
            return 1
        return 0

    if col_ratio >= 0.45 and (supported_group_ratio >= 0.35 or avg_dark_ratio >= 0.12):
        return 2
    if wall_ratio >= 0.40 and (supported_group_ratio >= 0.40 or avg_dark_ratio >= 0.12):
        return 1
    return 0


def _is_candidate_entity_type(entity_type: str) -> bool:
    et = (entity_type or "").upper().strip()
    if not et:
        return False
    if et in DIRECT_ARCHIVE_ENTITY_TYPES:
        return False
    return et in {
        "LINE",
        "LWPOLYLINE",
        "POLYLINE",
        "CIRCLE",
        "ARC",
        "ELLIPSE",
        "SPLINE",
        "INSERT",
    }


def _map_vectors(
    doc: ezdxf.document.Drawing,
    mask: np.ndarray,
    support_map: np.ndarray,
    bounds: Tuple[float, float, float, float],
    units_info: UnitsInfo,
    only_structure: bool,
) -> dict:
    min_x, min_y, max_x, max_y = bounds
    h, w = mask.shape
    msp = doc.modelspace()
    _add_target_layers(doc)

    width_cm = max((max_x - min_x) * units_info.scale_to_cm, 1e-6)
    height_cm = max((max_y - min_y) * units_info.scale_to_cm, 1e-6)
    px_per_cm_x = (w - 1) / width_cm
    px_per_cm_y = (h - 1) / height_cm
    neighborhood = max(3, int(round(min(px_per_cm_x, px_per_cm_y) * 2.0)))

    counts = {
        "walls": 0,
        "columns": 0,
        "background": 0,
        "purged": 0,
        "direct_archived": 0,
        "total": 0,
    }

    def to_px(x: float, y: float) -> Tuple[int, int]:
        px = int(round((x - min_x) / max((max_x - min_x), 1e-6) * (w - 1)))
        py = h - 1 - int(round((y - min_y) / max((max_y - min_y), 1e-6) * (h - 1)))
        return px, py

    for ent in list(msp):
        counts["total"] += 1
        et = ent.dxftype()

        if not _is_candidate_entity_type(et):
            _apply_entity_style(ent, "ARCHI_FOND")
            counts["background"] += 1
            counts["direct_archived"] += 1
            continue

        if et == "LINE":
            line_len = math.hypot(float(ent.dxf.end.x - ent.dxf.start.x), float(ent.dxf.end.y - ent.dxf.start.y))
            if (line_len * units_info.scale_to_cm) < 2.5:
                _apply_entity_style(ent, "ARCHI_FOND")
                counts["background"] += 1
                continue

        samples = _sample_entity_points(ent, units_info)
        if not samples:
            _apply_entity_style(ent, "ARCHI_FOND")
            counts["background"] += 1
            continue

        weighted_votes = {0: 0.0, 1: 0.0, 2: 0.0}
        total_weight = 0.0
        dark_weight_sum = 0.0
        group_roles: Dict[int, Dict[str, PatchStats]] = {}

        for sample in samples:
            px, py = to_px(sample.x, sample.y)
            if not (0 <= px < w and 0 <= py < h):
                continue

            total_weight += sample.weight
            patch = _analyze_patch(mask, support_map, px, py, neighborhood)
            dark_weight_sum += patch.dark_ratio * sample.weight
            group_roles.setdefault(sample.group_id, {})[sample.role] = patch

            if patch.exact_class != 0:
                weighted_votes[patch.exact_class] += sample.weight
            elif patch.dominant_class is not None:
                weighted_votes[patch.dominant_class] += sample.weight * 0.5

        if total_weight <= 0:
            _apply_entity_style(ent, "ARCHI_FOND")
            counts["background"] += 1
            continue

        supported_groups = sum(1 for role_stats in group_roles.values() if _group_is_visually_supported(role_stats))
        total_groups = max(len(group_roles), 1)
        supported_group_ratio = supported_groups / total_groups
        avg_dark_ratio = dark_weight_sum / total_weight

        cls = _choose_class_fused(
            weighted_votes=weighted_votes,
            total_weight=total_weight,
            avg_dark_ratio=avg_dark_ratio,
            supported_group_ratio=supported_group_ratio,
            entity_type=et,
            is_closed=_is_closed_entity(ent),
        )

        if cls == 1:
            _apply_entity_style(ent, "BA_MURS")
            counts["walls"] += 1
        elif cls == 2:
            _apply_entity_style(ent, "BA_POTEAUX")
            counts["columns"] += 1
        else:
            _apply_entity_style(ent, "ARCHI_FOND")
            counts["background"] += 1

    if only_structure and (counts["walls"] + counts["columns"] > 0):
        for ent in list(msp):
            if (getattr(ent.dxf, "layer", "") or "") == "ARCHI_FOND":
                try:
                    msp.delete_entity(ent)
                    counts["purged"] += 1
                except Exception:
                    pass
    elif only_structure:
        logger.warning("M0: only_structure requested but no structural entity was detected; purge skipped")

    return counts


def _save_audit(
    gray: np.ndarray,
    mask: np.ndarray,
    support_map: np.ndarray,
    bounds_info: BoundsInfo,
    units_info: UnitsInfo,
    counts: dict,
    audit_dir: Optional[Path],
    model_path: Optional[Path],
    render_noise_removed: int,
    raster_source: RasterSourceInfo,
) -> None:
    if audit_dir is None:
        return

    audit_dir.mkdir(parents=True, exist_ok=True)

    plt.imsave(audit_dir / "m0_raster.png", gray, cmap="gray", vmin=0, vmax=255)

    color = np.zeros((mask.shape[0], mask.shape[1], 3), dtype=np.uint8)
    color[mask == 1] = (220, 60, 60)
    color[mask == 2] = (60, 200, 220)
    plt.imsave(audit_dir / "m0_mask.png", color)
    plt.imsave(audit_dir / "m0_support.png", support_map, cmap="gray", vmin=0, vmax=255)

    # m0_overlay.png
    if gray.ndim == 2:
        gray_rgb = np.stack([gray]*3, axis=-1)
    else:
        gray_rgb = gray
    overlay = cv2.addWeighted(gray_rgb, 0.7, color, 0.3, 0) if HAS_CV2 else (gray_rgb * 0.7 + color * 0.3).astype(np.uint8)
    plt.imsave(audit_dir / "m0_overlay.png", overlay)

    report = {
        "units_detected": units_info.source_units,
        "units_source": "insunits" if units_info.insunits_code != 0 else "inferred_from_extents",
        "extents": {
            "xmin": bounds_info.bounds[0],
            "ymin": bounds_info.bounds[1],
            "xmax": bounds_info.bounds[2],
            "ymax": bounds_info.bounds[3]
        },
        "raster_size": [int(gray.shape[1]), int(gray.shape[0])],
        "vision_source": raster_source.origin,
        "vision_file": str(raster_source.vision_path),
        "segmentation_mode": "model" if model_path else "fallback",
        "model_path": str(model_path) if model_path else "",
        "model_format": model_path.suffix.lstrip(".") if model_path else "none",
        "image_cropped": raster_source.cropped,
        "image_padded": raster_source.padded,
        "pixels_wall": int(np.sum(mask == 1)),
        "pixels_column": int(np.sum(mask == 2)),
        "total_dxf_entities": counts.get("total", 0),
        "entities_BA_MURS": counts.get("walls", 0),
        "entities_BA_POTEAUX": counts.get("columns", 0),
        "entities_ARCHI_FOND": counts.get("background", 0),
        "status": "empty_segmentation" if int(np.sum(mask > 0)) == 0 else ("fallback_used" if not model_path else "ok")
    }
    (audit_dir / "m0_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


def run(
    input_path: Path,
    output_path: Path,
    only_structure: bool = False,
    model_path: Optional[Path] = None,
    dpi: int = 300,
    audit_dir: Optional[Path] = None,
    vision_path: Optional[Path] = None,
) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"M0: input file not found: {input_path}")
    if input_path.suffix.lower() != ".dxf":
        raise ValueError("M0 currently supports DXF input")
    if dpi <= 0:
        raise ValueError("M0: dpi must be > 0")
    if vision_path is not None and not vision_path.exists():
        raise FileNotFoundError(f"M0: vision source not found: {vision_path}")

    logger.info(f"M0: vision filtering on {input_path.name}")
    output_doc = ezdxf.readfile(str(input_path))
    render_doc = ezdxf.readfile(str(input_path))

    render_noise_removed = _strip_render_noise(render_doc)
    logger.info(f"M0: render noise removed={render_noise_removed}")

    units_info = _resolve_units(render_doc)
    logger.info(
        f"M0: source_units={units_info.source_units} | scale_to_cm={units_info.scale_to_cm} | insunits={units_info.insunits_code}"
    )

    bounds_info = _bbox_doc(render_doc)

    if vision_path is not None:
        gray, raster_source = _load_external_raster(vision_path, dpi, bounds_info.bounds, units_info)
        logger.info(f"M0: external vision source used ({raster_source.origin})")
    else:
        gray, bounds_info = _rasterize_from_dxf(render_doc, units_info, dpi=dpi)
        raster_source = RasterSourceInfo(origin="dxf", vision_path="", cropped=False, padded=False)

    model, model_config = _load_model(model_path)
    if model is not None:
        mask = _segment_with_model(gray, model, model_config)
    else:
        mask = _segment_morph(gray, bounds_info.bounds, units_info)
    support_map = _build_visual_support_map(gray, bounds_info.bounds, units_info)

    mask_wall_px = int(np.sum(mask == 1))
    mask_col_px = int(np.sum(mask == 2))
    logger.info(f"M0: mask pixels | walls={mask_wall_px} | columns={mask_col_px}")

    if mask_wall_px + mask_col_px == 0:
        logger.warning("M0: segmentation returned an empty structural mask")

    counts = _map_vectors(output_doc, mask, support_map, bounds_info.bounds, units_info, only_structure=only_structure)
    _save_audit(
        gray,
        mask,
        support_map,
        bounds_info,
        units_info,
        counts,
        audit_dir,
        model_path,
        render_noise_removed,
        raster_source,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_doc.saveas(str(output_path))

    logger.info(
        f"M0 output: {output_path} | total={counts['total']} | walls={counts['walls']} "
        f"| cols={counts['columns']} | bg={counts['background']} | direct_archived={counts['direct_archived']} "
        f"| purged={counts['purged']}"
    )
    return output_path


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Coffrage M0 Vision Filter")
    ap.add_argument("input", help="Input DXF")
    ap.add_argument("-o", "--output", default="./output_coffrage/m0_filtered.dxf")
    ap.add_argument("--only-structure", action="store_true")
    ap.add_argument("--model", default="", help="Path to torch model (.pt/.pth) (optional)")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--audit-dir", default="", help="Audit output folder")
    ap.add_argument("--vision", default="", help="Optional PDF/PNG/JPG vision source")
    args = ap.parse_args()

    run(
        Path(args.input),
        Path(args.output),
        only_structure=args.only_structure,
        model_path=Path(args.model) if args.model else None,
        dpi=args.dpi,
        audit_dir=Path(args.audit_dir) if args.audit_dir else None,
        vision_path=Path(args.vision) if args.vision else None,
    )