#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from loguru import logger
from shapely.geometry import LineString, MultiPolygon, Polygon
from shapely.ops import polygonize_full, unary_union

from coffrage_core import (
    GeomProps,
    PipelineConfig,
    RawEntity,
    SourceMeta,
    compute_mrr,
    save_entities_json,
)


ARCHIVE_SOURCE_LAYERS = {"ARCHI_FOND", "0_ARCHIVE", "S-GN-TEXT"}
ANNOTATION_SOURCE_TYPES = {"TEXT", "MTEXT", "DIMENSION", "LEADER", "MULTILEADER", "ATTDEF", "ATTRIB"}


@dataclass
class ReconstructionConfig:
    min_reconstructed_area_m2: float = 0.015
    min_reconstructed_thickness_cm: float = 8.0
    dedupe_overlap_ratio: float = 0.92
    max_aspect_ratio: float = 60.0
    min_boundary_support_lines: int = 2


@dataclass
class ReconstructionStats:
    input_entities: int = 0
    candidate_lines: int = 0
    skipped_lines_archived: int = 0
    skipped_lines_too_short: int = 0
    skipped_lines_invalid: int = 0
    from_insert_source_lines: int = 0
    snapped_vertices: int = 0
    unique_lines_after_snap: int = 0
    polygon_candidates: int = 0
    polygons_reconstructed: int = 0
    polygons_rejected_small: int = 0
    polygons_rejected_thin: int = 0
    polygons_rejected_duplicate: int = 0
    polygons_rejected_weak_support: int = 0
    dangles: int = 0
    cuts: int = 0
    invalid_ring_lines: int = 0


class _UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1


def _round_point(x: float, y: float, ndigits: int = 6) -> Tuple[float, float]:
    return round(float(x), ndigits), round(float(y), ndigits)


def _largest_polygon(geom) -> Optional[Polygon]:
    if geom is None or geom.is_empty:
        return None
    if isinstance(geom, Polygon):
        return geom
    if isinstance(geom, MultiPolygon):
        polys = [g for g in geom.geoms if isinstance(g, Polygon) and not g.is_empty]
        if polys:
            return max(polys, key=lambda p: p.area)
    return None


def _normalize_polygon(poly: Polygon) -> Optional[Polygon]:
    if poly.is_empty:
        return None
    if not poly.is_valid:
        repaired = poly.buffer(0)
        poly = _largest_polygon(repaired) or poly
    if poly.is_empty or not poly.is_valid or poly.area <= 0:
        return None
    return poly


def _is_annotation_like_source(entity: RawEntity) -> bool:
    source_type = (entity.source.entity_type or "").upper().strip()
    source_layer = (entity.source.layer or "").upper().strip()

    if source_type in ANNOTATION_SOURCE_TYPES:
        return True
    if source_layer in ARCHIVE_SOURCE_LAYERS:
        return True
    if any(token in source_layer for token in ("TEXT", "MTEXT", "DIM", "COTA", "NOTE", "ANNOT")):
        return True
    return False


def _is_candidate_line(entity: RawEntity, config: PipelineConfig, stats: ReconstructionStats) -> bool:
    geom = entity.geometry()
    if not isinstance(geom, LineString):
        return False

    if geom.is_empty:
        stats.skipped_lines_invalid += 1
        return False

    if geom.length < config.min_segment_cm:
        stats.skipped_lines_too_short += 1
        return False

    if _is_annotation_like_source(entity):
        stats.skipped_lines_archived += 1
        return False

    return True


def _collect_candidate_lines(
    entities: List[RawEntity],
    config: PipelineConfig,
    stats: ReconstructionStats,
) -> List[Tuple[RawEntity, LineString]]:
    out: List[Tuple[RawEntity, LineString]] = []

    for entity in entities:
        if _is_candidate_line(entity, config, stats):
            geom = entity.geometry()
            if isinstance(geom, LineString):
                out.append((entity, geom))
                if entity.source.parent_insert_handle:
                    stats.from_insert_source_lines += 1

    return out


def _collect_existing_polygons(entities: List[RawEntity]) -> List[Polygon]:
    out: List[Polygon] = []
    for entity in entities:
        geom = entity.geometry()
        if isinstance(geom, Polygon) and not geom.is_empty and geom.area > 0:
            norm = _normalize_polygon(geom)
            if norm is not None:
                out.append(norm)
    return out


def _cluster_vertices(
    line_records: List[Tuple[RawEntity, LineString]],
    tolerance_cm: float,
) -> tuple[List[Tuple[RawEntity, LineString]], int]:
    if not line_records or tolerance_cm <= 0:
        return line_records, 0

    points: List[Tuple[float, float]] = []
    line_indices: List[List[int]] = []

    for _, line in line_records:
        coords = list(line.coords)
        idxs: List[int] = []
        for x, y, *_ in coords:
            idxs.append(len(points))
            points.append(_round_point(x, y))
        line_indices.append(idxs)

    if not points:
        return line_records, 0

    uf = _UnionFind(len(points))
    cell_size = max(tolerance_cm, 1e-6)
    grid: Dict[Tuple[int, int], List[int]] = {}

    for idx, (x, y) in enumerate(points):
        cell = (int(x // cell_size), int(y // cell_size))

        for gx in range(cell[0] - 1, cell[0] + 2):
            for gy in range(cell[1] - 1, cell[1] + 2):
                for other_idx in grid.get((gx, gy), []):
                    ox, oy = points[other_idx]
                    dx = x - ox
                    dy = y - oy
                    if (dx * dx + dy * dy) ** 0.5 <= tolerance_cm:
                        uf.union(idx, other_idx)

        grid.setdefault(cell, []).append(idx)

    groups: Dict[int, List[Tuple[float, float]]] = {}
    for idx, pt in enumerate(points):
        root = uf.find(idx)
        groups.setdefault(root, []).append(pt)

    centers: Dict[int, Tuple[float, float]] = {}
    snapped_vertices = 0
    for root, pts in groups.items():
        if len(pts) > 1:
            snapped_vertices += len(pts)
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        centers[root] = _round_point(cx, cy)

    snapped_records: List[Tuple[RawEntity, LineString]] = []
    for (entity, _), idxs in zip(line_records, line_indices):
        coords: List[Tuple[float, float]] = []
        for pt_idx in idxs:
            snapped = centers[uf.find(pt_idx)]
            if not coords or coords[-1] != snapped:
                coords.append(snapped)

        if len(coords) < 2:
            continue

        snapped_line = LineString(coords)
        if not snapped_line.is_empty and snapped_line.length > 0:
            snapped_records.append((entity, snapped_line))

    return snapped_records, snapped_vertices


def _dedupe_lines(
    line_records: List[Tuple[RawEntity, LineString]],
    min_length_cm: float,
) -> List[Tuple[RawEntity, LineString]]:
    unique: Dict[tuple[Tuple[float, float], ...], Tuple[RawEntity, LineString]] = {}

    for entity, line in line_records:
        if line.is_empty or line.length < min_length_cm:
            continue

        coords = tuple(_round_point(x, y) for x, y, *_ in line.coords)
        if len(coords) < 2:
            continue

        reverse_coords = tuple(reversed(coords))
        key = min(coords, reverse_coords)

        if key not in unique:
            unique[key] = (entity, line)

    return list(unique.values())


def _polygon_metrics(poly: Polygon) -> tuple[float, float, float, float]:
    thickness_cm, length_cm, _ = compute_mrr(poly)
    thickness = float(thickness_cm or 0.0)
    length = float(length_cm or 0.0)
    area_m2 = float(poly.area / 10000.0)
    aspect = length / max(thickness, 0.1) if length > 0 else 0.0
    return thickness, length, area_m2, aspect


def _is_duplicate_polygon(
    poly: Polygon,
    existing_polygons: List[Polygon],
    overlap_ratio: float,
    buffer_cm: float,
) -> bool:
    if poly.area <= 0:
        return True

    for existing in existing_polygons:
        try:
            buffered = existing.buffer(buffer_cm)
            if buffered.covers(poly):
                return True

            inter_area = buffered.intersection(poly).area
            if inter_area / max(poly.area, 1e-9) >= overlap_ratio:
                return True
        except Exception:
            continue

    return False


def _supporting_line_records(
    poly: Polygon,
    line_records: List[Tuple[RawEntity, LineString]],
    tolerance_cm: float,
) -> List[Tuple[RawEntity, LineString]]:
    try:
        boundary_zone = poly.boundary.buffer(max(tolerance_cm, 0.5))
    except Exception:
        return []

    bx0, by0, bx1, by1 = boundary_zone.bounds
    supports: List[Tuple[RawEntity, LineString]] = []

    for entity, line in line_records:
        lx0, ly0, lx1, ly1 = line.bounds
        if lx1 < bx0 or lx0 > bx1 or ly1 < by0 or ly0 > by1:
            continue
        try:
            if boundary_zone.intersects(line):
                supports.append((entity, line))
        except Exception:
            continue

    return supports


def _dominant_value(values: List[str]) -> str:
    if not values:
        return ""
    counts = Counter(v for v in values if v)
    if not counts:
        return ""
    return counts.most_common(1)[0][0]


def _make_reconstructed_polygon(
    poly: Polygon,
    seed_id: int,
    support_records: List[Tuple[RawEntity, LineString]],
    reconstruction_method: str,
    snap_distance_cm: float,
) -> RawEntity:
    thickness_cm, length_cm, orientation_deg = compute_mrr(poly)

    geom_props = GeomProps(
        thickness_cm=thickness_cm,
        length_cm=length_cm,
        area_m2=round(poly.area / 10000.0, 4),
        orientation_deg=orientation_deg,
        is_closed=True,
        was_reconstructed=True,
        reconstruction_method=reconstruction_method,
        centroid_x=round(poly.centroid.x, 2),
        centroid_y=round(poly.centroid.y, 2),
    )

    source = SourceMeta(
        layer="__RECONSTRUCTED__",
        color=256,
        linetype="BYLAYER",
        entity_type="RECONSTRUCTED_POLYGON",
    )

    if support_records:
        first = support_records[0][0].source
        source.original_file = first.original_file
        source.original_format = first.original_format
        source.original_units = first.original_units
        source.scale_to_cm = first.scale_to_cm
        source.block_name = _dominant_value([rec[0].source.block_name for rec in support_records])

    source_layers = sorted({rec[0].source.layer for rec in support_records if rec[0].source.layer})
    support_count = len(support_records)

    entity = RawEntity(
        id=f"REC-{seed_id:05d}",
        source=source,
        geom_props=geom_props,
        issues=[
            "RECONSTRUCTED=true",
            f"RECON_METHOD={reconstruction_method}",
            f"RECON_SOURCE_LINE_COUNT={support_count}",
            f"RECON_SNAP_DISTANCE_CM={round(snap_distance_cm, 3)}",
            f"RECON_SOURCE_LAYERS={','.join(source_layers[:8])}" if source_layers else "RECON_SOURCE_LAYERS=",
        ],
    )
    entity.set_geometry(poly)
    return entity


def run(
    entities: List[RawEntity],
    config: PipelineConfig,
    output_dir: Path | None = None,
    reconstruction_config: Optional[ReconstructionConfig] = None,
) -> List[RawEntity]:
    rcfg = reconstruction_config or ReconstructionConfig()
    stats = ReconstructionStats(input_entities=len(entities))

    candidate_records = _collect_candidate_lines(entities, config, stats)
    stats.candidate_lines = len(candidate_records)

    if not candidate_records:
        logger.info("Reconstruction: no eligible lines, skipping")
        if output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            save_entities_json(
                entities,
                output_dir / "reconstructed_entities.geojson",
                metadata={
                    "stage": "reconstruction",
                    "reconstruction_stats": stats.__dict__,
                },
            )
        return entities

    snapped_records, snapped_vertices = _cluster_vertices(candidate_records, config.snap_distance_cm)
    stats.snapped_vertices = snapped_vertices

    unique_records = _dedupe_lines(snapped_records, config.min_segment_cm)
    stats.unique_lines_after_snap = len(unique_records)

    if not unique_records:
        logger.warning("Reconstruction: all snapped lines collapsed or were filtered out")
        if output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            save_entities_json(
                entities,
                output_dir / "reconstructed_entities.geojson",
                metadata={
                    "stage": "reconstruction",
                    "reconstruction_stats": stats.__dict__,
                },
            )
        return entities

    existing_polygons = _collect_existing_polygons(entities)
    network = unary_union([line for _, line in unique_records])

    polygons_geom, dangles_geom, cuts_geom, invalid_geom = polygonize_full(network)

    polygon_candidates = [p for p in getattr(polygons_geom, "geoms", []) if isinstance(p, Polygon)]
    stats.polygon_candidates = len(polygon_candidates)
    stats.dangles = len(getattr(dangles_geom, "geoms", []))
    stats.cuts = len(getattr(cuts_geom, "geoms", []))
    stats.invalid_ring_lines = len(getattr(invalid_geom, "geoms", []))

    reconstructed: List[RawEntity] = []
    reconstruction_method = "polygonize_snap_insertaware"
    duplicate_buffer_cm = max(config.snap_distance_cm * 1.5, 1.0)

    for idx, candidate in enumerate(polygon_candidates, start=1):
        poly = _normalize_polygon(candidate)
        if poly is None:
            stats.polygons_rejected_small += 1
            continue

        thickness_cm, length_cm, area_m2, aspect_ratio = _polygon_metrics(poly)

        if area_m2 < rcfg.min_reconstructed_area_m2:
            stats.polygons_rejected_small += 1
            continue

        if thickness_cm > 0:
            if thickness_cm < rcfg.min_reconstructed_thickness_cm and area_m2 < 0.25:
                stats.polygons_rejected_thin += 1
                continue
            if aspect_ratio > rcfg.max_aspect_ratio and area_m2 < 0.10:
                stats.polygons_rejected_thin += 1
                continue

        if _is_duplicate_polygon(
            poly,
            existing_polygons,
            overlap_ratio=rcfg.dedupe_overlap_ratio,
            buffer_cm=duplicate_buffer_cm,
        ):
            stats.polygons_rejected_duplicate += 1
            continue

        support_records = _supporting_line_records(poly, unique_records, config.snap_distance_cm)
        if len(support_records) < rcfg.min_boundary_support_lines:
            stats.polygons_rejected_weak_support += 1
            continue

        reconstructed_entity = _make_reconstructed_polygon(
            poly=poly,
            seed_id=idx,
            support_records=support_records,
            reconstruction_method=reconstruction_method,
            snap_distance_cm=config.snap_distance_cm,
        )
        reconstructed.append(reconstructed_entity)

    stats.polygons_reconstructed = len(reconstructed)
    out = entities + reconstructed

    logger.info(
        "Reconstruction: "
        f"candidate_lines={stats.candidate_lines} | "
        f"from_insert={stats.from_insert_source_lines} | "
        f"skipped_archived={stats.skipped_lines_archived} | "
        f"skipped_short={stats.skipped_lines_too_short} | "
        f"snapped_vertices={stats.snapped_vertices} | "
        f"unique_lines={stats.unique_lines_after_snap} | "
        f"polygon_candidates={stats.polygon_candidates} | "
        f"reconstructed={stats.polygons_reconstructed} | "
        f"rejected_small={stats.polygons_rejected_small} | "
        f"rejected_thin={stats.polygons_rejected_thin} | "
        f"rejected_duplicate={stats.polygons_rejected_duplicate} | "
        f"rejected_weak_support={stats.polygons_rejected_weak_support} | "
        f"dangles={stats.dangles} | cuts={stats.cuts} | invalid_rings={stats.invalid_ring_lines}"
    )

    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        save_entities_json(
            out,
            output_dir / "reconstructed_entities.geojson",
            metadata={
                "stage": "reconstruction",
                "reconstruction_stats": stats.__dict__,
                "snap_distance_cm": config.snap_distance_cm,
                "min_segment_cm": config.min_segment_cm,
            },
        )

    return out


if __name__ == "__main__":
    import argparse
    import coffrage_core as core

    ap = argparse.ArgumentParser(description="Coffrage Reconstruct")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default="./output_coffrage")
    args = ap.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)

    cfg = core.PipelineConfig().apply_tolerance_mode()
    raw = core.run(input_path, output_dir)
    run(raw, cfg, output_dir)