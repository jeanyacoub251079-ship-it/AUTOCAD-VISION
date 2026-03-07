#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import ezdxf
from loguru import logger
from shapely.geometry import GeometryCollection, LineString, MultiLineString, MultiPolygon, Point, Polygon
from shapely.geometry.base import BaseGeometry

from coffrage_core import PipelineConfig, RawEntity, load_entities_json_entities


ARCHIVE_LAYER = "ARCHI_FOND"

LAYER_MAP_STRUCTURAL = {
    "WALL": "BA_MURS",
    "COLUMN": "BA_POTEAUX",
    "SLAB": "BA_DALLES",
    "BEAM": "BA_POUTRES",
    "TREMIE": "BA_TREMIES",
    "RESERVATION": "BA_RESERVATIONS",
}

LAYER_COLORS = {
    "BA_MURS": 1,
    "BA_POTEAUX": 4,
    "BA_DALLES": 2,
    "BA_POUTRES": 3,
    "BA_TREMIES": 6,
    "BA_RESERVATIONS": 5,
    ARCHIVE_LAYER: 8,
}

STRUCTURAL_LAYERS = set(LAYER_MAP_STRUCTURAL.values())
STRUCTURAL_TYPES = set(LAYER_MAP_STRUCTURAL.keys())


@dataclass
class OutputStats:
    loaded_entities: int = 0
    review_pending: int = 0
    trusted_structural_entities: int = 0
    invalid_geometries: int = 0
    exported_full_primitives: int = 0
    exported_structure_primitives: int = 0


def _sanitize_project_name(project_name: str) -> str:
    name = (project_name or "PROJET").strip()
    name = re.sub(r"[^\w\-]+", "_", name, flags=re.UNICODE)
    return name or "PROJET"


def _load_feature_collection(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Output input file not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("type") != "FeatureCollection":
        raise ValueError(f"Invalid GeoJSON FeatureCollection: {path}")
    return data


def _setup_layers(doc: ezdxf.document.Drawing) -> None:
    for name, color in LAYER_COLORS.items():
        if name in doc.layers:
            doc.layers.get(name).color = color
        else:
            layer = doc.layers.add(name)
            layer.color = color


def _set_doc_units_cm(doc: ezdxf.document.Drawing) -> None:
    try:
        doc.header["$INSUNITS"] = 5
    except Exception:
        pass


def _safe_geometry(entity: RawEntity) -> Optional[BaseGeometry]:
    try:
        geom = entity.geometry()
    except Exception:
        return None
    if geom is None or geom.is_empty:
        return None
    return geom


def _drop_duplicate_last(coords: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    if len(coords) >= 2 and coords[0] == coords[-1]:
        return coords[:-1]
    return coords


def _iter_export_primitives(geom: BaseGeometry) -> Iterable[BaseGeometry]:
    if geom.is_empty:
        return

    if isinstance(geom, (Polygon, LineString, Point)):
        yield geom
        return

    if isinstance(geom, MultiPolygon):
        for part in geom.geoms:
            if not part.is_empty:
                yield part
        return

    if isinstance(geom, MultiLineString):
        for part in geom.geoms:
            if not part.is_empty:
                yield part
        return

    if isinstance(geom, GeometryCollection):
        for part in geom.geoms:
            yield from _iter_export_primitives(part)
        return


def _export_polygon(msp, poly: Polygon, layer: str) -> int:
    exported = 0

    exterior = [(float(x), float(y)) for x, y in poly.exterior.coords]
    exterior = _drop_duplicate_last(exterior)
    if len(exterior) >= 3:
        msp.add_lwpolyline(exterior, close=True, dxfattribs={"layer": layer})
        exported += 1

    for interior in poly.interiors:
        ring = [(float(x), float(y)) for x, y in interior.coords]
        ring = _drop_duplicate_last(ring)
        if len(ring) >= 3:
            msp.add_lwpolyline(ring, close=True, dxfattribs={"layer": layer})
            exported += 1

    return exported


def _export_linestring(msp, line: LineString, layer: str) -> int:
    pts = [(float(x), float(y)) for x, y in line.coords]
    if len(pts) < 2:
        return 0
    if len(pts) == 2:
        msp.add_line(pts[0], pts[1], dxfattribs={"layer": layer})
    else:
        msp.add_lwpolyline(pts, dxfattribs={"layer": layer})
    return 1


def _export_point(msp, point: Point, layer: str) -> int:
    msp.add_point((float(point.x), float(point.y)), dxfattribs={"layer": layer})
    return 1


def _export_geometry(msp, geom: BaseGeometry, layer: str) -> int:
    exported = 0
    for primitive in _iter_export_primitives(geom):
        if isinstance(primitive, Polygon):
            exported += _export_polygon(msp, primitive, layer)
        elif isinstance(primitive, LineString):
            exported += _export_linestring(msp, primitive, layer)
        elif isinstance(primitive, Point):
            exported += _export_point(msp, primitive, layer)
    return exported


def _effective_pipeline_config(metadata_in: dict) -> PipelineConfig:
    tolerance_mode = str(metadata_in.get("tolerance_mode", "NORMAL") or "NORMAL")
    return PipelineConfig(tolerance_mode=tolerance_mode).apply_tolerance_mode()


def _is_trusted_structural(entity: RawEntity, cfg: PipelineConfig) -> bool:
    clf = entity.classification

    if clf.structural_type not in STRUCTURAL_TYPES:
        return False

    if clf.method == "human_review":
        return True

    if clf.needs_review:
        return False

    return float(clf.confidence) >= float(cfg.confidence_auto)


def _resolve_export_route(entity: RawEntity, cfg: PipelineConfig) -> tuple[str, str, bool]:
    clf = entity.classification
    structural_type = clf.structural_type or "UNKNOWN"

    if _is_trusted_structural(entity, cfg):
        return LAYER_MAP_STRUCTURAL[structural_type], "trusted_structural", True

    if structural_type in STRUCTURAL_TYPES:
        return ARCHIVE_LAYER, "untrusted_structural", False

    if structural_type in {"ANNOTATION", "FURNITURE", "UNKNOWN"}:
        return ARCHIVE_LAYER, "non_structural", False

    return ARCHIVE_LAYER, "fallback_archive", False


def _source_summary(entities: List[RawEntity]) -> tuple[List[str], List[str], List[str]]:
    source_files = sorted({e.source.original_file for e in entities if e.source.original_file})
    source_units = sorted({e.source.original_units for e in entities if e.source.original_units})
    source_blocks = sorted({e.source.block_name for e in entities if e.source.block_name})
    return source_files, source_units, source_blocks


def _count_methods(entities: List[RawEntity]) -> Dict[str, int]:
    counter = Counter()
    for entity in entities:
        counter[entity.classification.method or ""] += 1
    return dict(sorted(counter.items(), key=lambda kv: (-kv[1], kv[0])))


def _count_issues(entities: List[RawEntity], limit: int = 20) -> Dict[str, int]:
    counter = Counter()
    for entity in entities:
        for issue in entity.issues:
            counter[issue] += 1
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]
    return dict(items)


def _write_qa_report(
    output_path: Path,
    *,
    project_name: str,
    input_geojson: Path,
    entities: List[RawEntity],
    stats: OutputStats,
    class_distribution: Dict[str, int],
    layer_distribution: Dict[str, int],
    route_distribution: Dict[str, int],
    source_files: List[str],
    source_units: List[str],
    source_blocks: List[str],
) -> None:
    human_reviewed = sum(1 for e in entities if e.classification.method == "human_review")
    low_confidence = sum(1 for e in entities if float(e.classification.confidence) < PipelineConfig().confidence_auto)

    lines = [
        "# Rapport QA - Coffrage",
        "",
        f"- Projet : {project_name}",
        f"- Date : {datetime.now().isoformat()}",
        f"- GeoJSON source : {input_geojson}",
        f"- Entités chargées : {stats.loaded_entities}",
        f"- Entités en revue : {stats.review_pending}",
        f"- Entités revues humainement : {human_reviewed}",
        f"- Entités structurelles fiables : {stats.trusted_structural_entities}",
        f"- Entités basse confiance : {low_confidence}",
        f"- Géométries invalides/ignorées : {stats.invalid_geometries}",
        f"- Primitives exportées DXF complet : {stats.exported_full_primitives}",
        f"- Primitives exportées DXF structure_only : {stats.exported_structure_primitives}",
        "",
        "## Fichiers source",
    ]

    lines.extend([f"- {path}" for path in source_files] if source_files else ["- Non renseigné"])

    lines.extend(["", "## Unités source"])
    lines.extend([f"- {unit}" for unit in source_units] if source_units else ["- Non renseigné"])

    lines.extend(["", "## Blocs source"])
    lines.extend([f"- {name}" for name in source_blocks[:25]] if source_blocks else ["- Aucun"])

    lines.extend(["", "## Distribution des types classifiés"])
    for key, value in sorted(class_distribution.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Distribution des couches exportées"])
    for key, value in sorted(layer_distribution.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Motifs de routage export"])
    for key, value in sorted(route_distribution.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Méthodes de classification"])
    for key, value in _count_methods(entities).items():
        lines.append(f"- {key}: {value}")

    lines.extend(["", "## Issues les plus fréquentes"])
    issue_distribution = _count_issues(entities)
    if issue_distribution:
        for key, value in issue_distribution.items():
            lines.append(f"- {key}: {value}")
    else:
        lines.append("- Aucune")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def run(geojson_path: Path, output_dir: Path, project_name: str = "PROJET") -> Dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_project_name = _sanitize_project_name(project_name)

    payload = _load_feature_collection(geojson_path)
    metadata_in = dict(payload.get("metadata") or {})
    entities = load_entities_json_entities(geojson_path)

    if not entities:
        logger.warning(f"Output: no entities found in {geojson_path}")

    cfg = _effective_pipeline_config(metadata_in)

    doc_full = ezdxf.new("R2018")
    doc_structure = ezdxf.new("R2018")
    _set_doc_units_cm(doc_full)
    _set_doc_units_cm(doc_structure)
    _setup_layers(doc_full)
    _setup_layers(doc_structure)

    msp_full = doc_full.modelspace()
    msp_structure = doc_structure.modelspace()

    stats = OutputStats(loaded_entities=len(entities))
    class_distribution = Counter()
    layer_distribution = Counter()
    route_distribution = Counter()

    for entity in entities:
        clf = entity.classification
        class_distribution[clf.structural_type or "UNKNOWN"] += 1
        if clf.needs_review:
            stats.review_pending += 1

        geom = _safe_geometry(entity)
        if geom is None:
            stats.invalid_geometries += 1
            continue

        layer, route_reason, is_structure = _resolve_export_route(entity, cfg)
        layer_distribution[layer] += 1
        route_distribution[route_reason] += 1

        exported_full = _export_geometry(msp_full, geom, layer)
        stats.exported_full_primitives += exported_full

        if is_structure:
            stats.trusted_structural_entities += 1
            exported_structure = _export_geometry(msp_structure, geom, layer)
            stats.exported_structure_primitives += exported_structure

    out_dxf = output_dir / f"{safe_project_name}_coffrage.dxf"
    out_dxf_structure = output_dir / f"{safe_project_name}_coffrage_structure_only.dxf"
    doc_full.saveas(str(out_dxf))
    doc_structure.saveas(str(out_dxf_structure))

    out_qa = output_dir / f"{safe_project_name}_rapport_qa.md"
    source_files, source_units, source_blocks = _source_summary(entities)
    _write_qa_report(
        out_qa,
        project_name=safe_project_name,
        input_geojson=geojson_path,
        entities=entities,
        stats=stats,
        class_distribution=dict(class_distribution),
        layer_distribution=dict(layer_distribution),
        route_distribution=dict(route_distribution),
        source_files=source_files,
        source_units=source_units,
        source_blocks=source_blocks,
    )

    out_geo = output_dir / f"{safe_project_name}_modele_final.geojson"
    metadata_out = {
        **metadata_in,
        "timestamp_output": datetime.now().isoformat(),
        "project_name": safe_project_name,
        "export_units": "cm",
        "input_geojson": str(geojson_path),
        "output_dxf": str(out_dxf),
        "output_dxf_structure_only": str(out_dxf_structure),
        "qa_report": str(out_qa),
        "review_pending": stats.review_pending,
        "trusted_structural_entities": stats.trusted_structural_entities,
        "invalid_geometries": stats.invalid_geometries,
        "exported_full_primitives": stats.exported_full_primitives,
        "exported_structure_primitives": stats.exported_structure_primitives,
        "export_layer_distribution": dict(layer_distribution),
        "export_route_distribution": dict(route_distribution),
        "source_files": source_files,
        "source_units": source_units,
        "source_blocks": source_blocks,
    }

    out_geo.write_text(
        json.dumps(
            {
                "type": "FeatureCollection",
                "metadata": metadata_out,
                "features": payload.get("features", []),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    logger.info(
        f"Output generated: {out_dxf} | structure_only={out_dxf_structure} "
        f"| trusted_structural={stats.trusted_structural_entities} | review_pending={stats.review_pending}"
    )

    return {
        "dxf": out_dxf,
        "dxf_structure_only": out_dxf_structure,
        "qa": out_qa,
        "geojson": out_geo,
    }


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Coffrage Output")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default="./output_coffrage")
    ap.add_argument("-p", "--project", default="PROJET")
    args = ap.parse_args()

    result = run(Path(args.input), Path(args.output), args.project)
    print({k: str(v) for k, v in result.items()})