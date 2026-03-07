#!/usr/bin/env python3
from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Optional, Set, Tuple

from loguru import logger
from shapely.geometry import LineString, Polygon

from coffrage_core import (
    ClassificationResult,
    PipelineConfig,
    RawEntity,
    save_entities_json,
)


STRUCTURAL_TYPES: Set[str] = {"WALL", "COLUMN", "SLAB", "BEAM", "TREMIE", "RESERVATION"}
PRIMARY_STRUCTURAL_TYPES: Set[str] = {"WALL", "COLUMN"}

_EXACT_LAYER_HINTS: dict[str, tuple[str, float, str]] = {
    "BA_MURS": ("WALL", 0.98, "layer:exact:BA_MURS"),
    "BA_POTEAUX": ("COLUMN", 0.98, "layer:exact:BA_POTEAUX"),
    "BA_DALLES": ("SLAB", 0.95, "layer:exact:BA_DALLES"),
    "BA_POUTRES": ("BEAM", 0.95, "layer:exact:BA_POUTRES"),
    "BA_TREMIES": ("TREMIE", 0.92, "layer:exact:BA_TREMIES"),
    "BA_RESERVATIONS": ("RESERVATION", 0.92, "layer:exact:BA_RESERVATIONS"),
    "ARCHI_FOND": ("FURNITURE", 0.99, "layer:exact:ARCHI_FOND"),
    "0_ARCHIVE": ("FURNITURE", 0.99, "layer:exact:0_ARCHIVE"),
    "S-GN-TEXT": ("ANNOTATION", 0.99, "layer:exact:S-GN-TEXT"),
    "S-BA-VOIL": ("WALL", 0.97, "layer:exact:S-BA-VOIL"),
    "S-BA-POTE": ("COLUMN", 0.97, "layer:exact:S-BA-POTE"),
    "S-BA-DALL": ("SLAB", 0.95, "layer:exact:S-BA-DALL"),
    "S-BA-POUT": ("BEAM", 0.95, "layer:exact:S-BA-POUT"),
    "__RECONSTRUCTED__": ("UNKNOWN", 0.40, "layer:exact:RECONSTRUCTED"),
}

_KEYWORDS_BY_TYPE: dict[str, tuple[str, ...]] = {
    "ANNOTATION": ("TEXT", "MTEXT", "COTA", "COTE", "DIM", "NOTE", "ANNOT"),
    "WALL": ("VOILE", "VOIL", "MUR", "WALL", "REFEND", "PORTEUR", "NOYAU", "CORE"),
    "COLUMN": ("POTEAU", "POT", "COLUMN", "COL", "PILIER", "PIL"),
    "SLAB": ("DALLE", "DALL", "SLAB", "PLANCHER", "PLANCH"),
    "BEAM": ("POUTRE", "POUT", "BEAM"),
    "TREMIE": ("TREMIE", "TRÉMIE", "OPENING", "OUVERTURE"),
    "RESERVATION": ("RESERV", "RESA", "RESE"),
    "FURNITURE": ("FURN", "MEUBL", "MOBIL", "ARCHI", "MENUIS", "DOOR", "WINDOW", "SANIT", "EQUIP"),
}

_LAYER_PRIORITY = ("ANNOTATION", "WALL", "COLUMN", "SLAB", "BEAM", "TREMIE", "RESERVATION", "FURNITURE")


def _clamp_confidence(value: float) -> float:
    return round(max(0.0, min(1.0, float(value))), 2)


def _make_result(
    cfg: PipelineConfig,
    structural_type: str,
    sub_type: str,
    confidence: float,
    method: str,
    *,
    needs_review: Optional[bool] = None,
    review_reason: str = "",
    scores: Optional[dict[str, float]] = None,
) -> ClassificationResult:
    conf = _clamp_confidence(confidence)
    if needs_review is None:
        needs_review = structural_type == "UNKNOWN" or conf < cfg.confidence_auto
    return ClassificationResult(
        structural_type=structural_type,
        sub_type=sub_type,
        confidence=conf,
        method=method,
        needs_review=needs_review,
        review_reason=review_reason,
        scores=scores or {},
    )


def _tokenize_layer(layer: str) -> tuple[list[str], str]:
    upper = (layer or "").upper().strip()
    tokens = [t for t in re.split(r"[^A-Z0-9]+", upper) if t]
    compact = "".join(tokens)
    return tokens, compact


def _has_keyword(tokens: Iterable[str], compact: str, keywords: Iterable[str]) -> bool:
    token_set = set(tokens)
    return any(keyword in token_set or keyword in compact for keyword in keywords)


def _layer_hint(layer: str) -> Optional[tuple[str, float, str]]:
    upper = (layer or "").upper().strip()
    if not upper:
        return None

    if upper in _EXACT_LAYER_HINTS:
        return _EXACT_LAYER_HINTS[upper]

    tokens, compact = _tokenize_layer(upper)
    for structural_type in _LAYER_PRIORITY:
        keywords = _KEYWORDS_BY_TYPE[structural_type]
        if _has_keyword(tokens, compact, keywords):
            if structural_type == "ANNOTATION":
                return ("ANNOTATION", 0.97, "layer:keyword:annotation")
            if structural_type == "FURNITURE":
                return ("FURNITURE", 0.92, "layer:keyword:furniture")
            return (structural_type, 0.72, f"layer:keyword:{structural_type.lower()}")

    return None


def _entity_type_hint(entity_type: str) -> Optional[tuple[str, float, str]]:
    et = (entity_type or "").upper().strip()
    if not et:
        return None
    if et in {"TEXT", "MTEXT", "DIMENSION", "LEADER", "MULTILEADER", "ATTDEF", "ATTRIB"}:
        return ("ANNOTATION", 0.99, "entity_type:annotation")
    return None


def _locked_existing_classification(existing: ClassificationResult) -> bool:
    if existing.method == "human_review":
        return True
    if existing.structural_type == "ANNOTATION" and existing.confidence >= 0.95:
        return True
    if existing.structural_type == "FURNITURE" and existing.confidence >= 0.95:
        return True
    return False


def _existing_candidate(existing: ClassificationResult, cfg: PipelineConfig) -> Optional[ClassificationResult]:
    if not existing.structural_type or existing.structural_type == "UNKNOWN":
        return None
    if existing.confidence <= 0.0:
        return None
    return _make_result(
        cfg,
        structural_type=existing.structural_type,
        sub_type=existing.sub_type,
        confidence=existing.confidence,
        method=existing.method or "previous",
        needs_review=existing.needs_review,
        review_reason=existing.review_reason,
        scores=dict(existing.scores),
    )


def _polygon_scores(entity: RawEntity) -> tuple[float, float, float, float]:
    thickness = float(entity.geom_props.thickness_cm or 0.0)
    length = float(entity.geom_props.length_cm or 0.0)
    area = float(entity.geom_props.area_m2 or 0.0)
    aspect = length / max(thickness, 0.1) if length > 0 else 0.0
    return thickness, length, area, aspect


def _support_bonus(entity: RawEntity) -> float:
    bonus = 0.0

    if entity.geom_props.was_reconstructed:
        bonus += 0.04

    support_count = 0
    for issue in entity.issues:
        if issue.startswith("RECON_SOURCE_LINE_COUNT="):
            try:
                support_count = int(issue.split("=", 1)[1])
            except Exception:
                support_count = 0
            break

    if support_count >= 4:
        bonus += 0.05
    elif support_count >= 2:
        bonus += 0.03

    if entity.source.block_name:
        bonus += 0.02

    return bonus


def _polygon_candidates(
    entity: RawEntity,
    cfg: PipelineConfig,
    hint: Optional[tuple[str, float, str]],
) -> list[ClassificationResult]:
    thickness, length, area, aspect = _polygon_scores(entity)
    hint_type = hint[0] if hint else None
    hint_conf = hint[1] if hint else 0.0
    support_bonus = _support_bonus(entity)

    scores = {
        "thickness_cm": round(thickness, 2),
        "length_cm": round(length, 2),
        "area_m2": round(area, 4),
        "aspect_ratio": round(aspect, 2),
        "support_bonus": round(support_bonus, 2),
    }

    candidates: list[ClassificationResult] = []

    # Mur / voile / noyau allongé
    if 10.0 <= thickness <= 60.0 and length >= 60.0 and area >= 0.12 and aspect >= 2.0:
        conf = 0.80 + support_bonus
        subtype = "VOILE_BA"
        if thickness >= 25.0 and area >= 1.0:
            subtype = "NOYAU_OU_VOILE_LARGE"

        review_reason = ""
        if hint_type == "WALL":
            conf += 0.08
        elif hint_type in {"COLUMN", "FURNITURE"}:
            conf -= 0.16
            review_reason = "Geometry/layer mismatch"

        candidates.append(
            _make_result(
                cfg,
                structural_type="WALL",
                sub_type=subtype,
                confidence=conf,
                method="rule:poly_wall",
                needs_review=(conf < cfg.confidence_auto or bool(review_reason)),
                review_reason=review_reason,
                scores=scores,
            )
        )

    # Poteau / massif compact
    min_dim = min(thickness, length) if thickness > 0 and length > 0 else 0.0
    max_dim = max(thickness, length)
    if (
        12.0 <= min_dim <= 100.0
        and 12.0 <= max_dim <= 160.0
        and 0.01 <= area <= 2.50
        and aspect <= 2.4
    ):
        conf = 0.78 + support_bonus
        review_reason = ""
        if hint_type == "COLUMN":
            conf += 0.10
        elif hint_type in {"WALL", "FURNITURE"}:
            conf -= 0.12
            review_reason = "Geometry/layer mismatch"

        candidates.append(
            _make_result(
                cfg,
                structural_type="COLUMN",
                sub_type="POTEAU_OU_MASSIF",
                confidence=conf,
                method="rule:poly_column",
                needs_review=(conf < cfg.confidence_auto or bool(review_reason)),
                review_reason=review_reason,
                scores=scores,
            )
        )

    # Trémie / réservation : seulement si calque ou géométrie très suggestifs.
    if hint_type in {"TREMIE", "RESERVATION"} and area >= 0.05:
        stype = hint_type
        conf = max(0.80, hint_conf) + support_bonus * 0.5
        candidates.append(
            _make_result(
                cfg,
                structural_type=stype,
                sub_type=stype,
                confidence=conf,
                method=f"rule:poly_{stype.lower()}",
                needs_review=(conf < cfg.confidence_auto),
                review_reason="" if conf >= cfg.confidence_auto else "Opening/reservation inference",
                scores=scores,
            )
        )

    # Dalle : très conservatif.
    if hint_type == "SLAB" and hint_conf >= 0.90 and area >= 1.50 and thickness >= 8.0:
        conf = max(0.80, hint_conf)
        candidates.append(
            _make_result(
                cfg,
                structural_type="SLAB",
                sub_type="DALLE",
                confidence=conf,
                method="rule:poly_slab",
                needs_review=(conf < cfg.confidence_auto),
                review_reason="Layer-supported slab inference" if conf < 0.90 else "",
                scores=scores,
            )
        )

    return candidates


def _line_candidates(
    entity: RawEntity,
    cfg: PipelineConfig,
    hint: Optional[tuple[str, float, str]],
) -> list[ClassificationResult]:
    length = float(entity.geom_props.length_cm or 0.0)
    hint_type = hint[0] if hint else None
    hint_conf = hint[1] if hint else 0.0
    exact_hint = hint_conf >= 0.95

    candidates: list[ClassificationResult] = []

    if hint_type == "WALL" and length >= 40.0:
        conf = 0.86 if exact_hint else 0.68
        candidates.append(
            _make_result(
                cfg,
                structural_type="WALL",
                sub_type="WALL_EDGE",
                confidence=conf,
                method="rule:line_wall",
                needs_review=(not exact_hint or conf < cfg.confidence_auto),
                review_reason="" if exact_hint else "Line-based wall inference",
                scores={"length_cm": round(length, 2)},
            )
        )

    if hint_type == "BEAM" and length >= 80.0:
        conf = 0.82 if exact_hint else 0.72
        candidates.append(
            _make_result(
                cfg,
                structural_type="BEAM",
                sub_type="POUTRE",
                confidence=conf,
                method="rule:line_beam",
                needs_review=True,
                review_reason="Beam inference requires support review",
                scores={"length_cm": round(length, 2)},
            )
        )

    if hint_type in {"TREMIE", "RESERVATION"} and length >= 20.0:
        conf = 0.70 if exact_hint else 0.58
        candidates.append(
            _make_result(
                cfg,
                structural_type=hint_type,
                sub_type=hint_type,
                confidence=conf,
                method=f"rule:line_{hint_type.lower()}",
                needs_review=True,
                review_reason="Opening/reservation line requires review",
                scores={"length_cm": round(length, 2)},
            )
        )

    return candidates


def _fallback_from_hint(
    cfg: PipelineConfig,
    hint: tuple[str, float, str],
    geom,
) -> ClassificationResult:
    hint_type, hint_conf, hint_method = hint

    if hint_type == "ANNOTATION":
        return _make_result(
            cfg,
            structural_type="ANNOTATION",
            sub_type="",
            confidence=hint_conf,
            method=hint_method,
            needs_review=False,
        )

    if hint_type == "FURNITURE":
        return _make_result(
            cfg,
            structural_type="FURNITURE",
            sub_type="ARCHIVE",
            confidence=hint_conf,
            method=hint_method,
            needs_review=False,
        )

    adjusted_conf = hint_conf
    review_reason = "Layer-based inference"

    if hint_type in {"COLUMN", "TREMIE", "RESERVATION"} and isinstance(geom, LineString):
        adjusted_conf = min(adjusted_conf, 0.60)
    elif hint_type == "SLAB" and not isinstance(geom, Polygon):
        adjusted_conf = min(adjusted_conf, 0.50)
    elif hint_type == "WALL" and isinstance(geom, LineString) and hint_conf < 0.95:
        adjusted_conf = min(adjusted_conf, 0.66)

    return _make_result(
        cfg,
        structural_type=hint_type,
        sub_type="",
        confidence=adjusted_conf,
        method=hint_method,
        needs_review=(adjusted_conf < cfg.confidence_auto),
        review_reason="" if adjusted_conf >= cfg.confidence_auto else review_reason,
        scores={"layer_hint_confidence": round(hint_conf, 2)},
    )


def _candidate_rank(candidate: ClassificationResult) -> float:
    rank = float(candidate.confidence)

    if candidate.method.startswith("rule:poly"):
        rank += 0.05
    elif candidate.method.startswith("rule:line"):
        rank += 0.02
    elif candidate.method.startswith("layer:exact"):
        rank += 0.01

    if candidate.structural_type in PRIMARY_STRUCTURAL_TYPES:
        rank += 0.015

    if candidate.needs_review:
        rank -= 0.03

    return rank


def _classify_one(entity: RawEntity, cfg: PipelineConfig) -> ClassificationResult:
    existing = entity.classification or ClassificationResult()

    if _locked_existing_classification(existing):
        return existing

    geom = entity.geometry()
    if geom is None or geom.is_empty:
        return _make_result(
            cfg,
            structural_type="UNKNOWN",
            sub_type="",
            confidence=0.10,
            method="rule:no_geometry",
            needs_review=True,
            review_reason="Empty or invalid geometry",
        )

    entity_type_hint = _entity_type_hint(entity.source.entity_type)
    if entity_type_hint and entity_type_hint[0] == "ANNOTATION":
        return _fallback_from_hint(cfg, entity_type_hint, geom)

    layer_hint = _layer_hint(entity.source.layer)
    if layer_hint and layer_hint[0] in {"ANNOTATION", "FURNITURE"}:
        return _fallback_from_hint(cfg, layer_hint, geom)

    candidates: list[ClassificationResult] = []

    previous = _existing_candidate(existing, cfg)
    if previous is not None:
        candidates.append(previous)

    if isinstance(geom, Polygon):
        candidates.extend(_polygon_candidates(entity, cfg, layer_hint))
    elif isinstance(geom, LineString):
        candidates.extend(_line_candidates(entity, cfg, layer_hint))

    if layer_hint is not None:
        candidates.append(_fallback_from_hint(cfg, layer_hint, geom))

    if entity_type_hint is not None and entity_type_hint[0] != "ANNOTATION":
        candidates.append(_fallback_from_hint(cfg, entity_type_hint, geom))

    if candidates:
        return max(candidates, key=_candidate_rank)

    return _make_result(
        cfg,
        structural_type="UNKNOWN",
        sub_type="",
        confidence=0.20,
        method="rule:unknown",
        needs_review=True,
        review_reason="Ambiguous entity",
    )


def _archive_redundant_lines(entities: List[RawEntity], cfg: PipelineConfig) -> int:
    strong_polygons: list[tuple[Polygon, str]] = []

    for entity in entities:
        geom = entity.geometry()
        if not isinstance(geom, Polygon):
            continue
        if entity.classification.structural_type not in {"WALL", "COLUMN"}:
            continue
        if entity.classification.confidence < max(cfg.confidence_auto, 0.78):
            continue
        strong_polygons.append((geom, entity.classification.structural_type))

    if not strong_polygons:
        return 0

    archived = 0
    cover_tolerance = max(2.0, cfg.snap_distance_cm * 1.5)

    for entity in entities:
        geom = entity.geometry()
        if not isinstance(geom, LineString):
            continue
        if entity.classification.method == "human_review":
            continue
        if entity.classification.structural_type in {"ANNOTATION", "FURNITURE", "BEAM"}:
            continue

        hint = _layer_hint(entity.source.layer)
        hint_type = hint[0] if hint else None

        for poly, poly_type in strong_polygons:
            try:
                if not poly.buffer(cover_tolerance).covers(geom):
                    continue
            except Exception:
                continue

            if poly_type == "WALL":
                if hint_type not in {None, "WALL", "FURNITURE"} and entity.classification.structural_type not in {"WALL", "UNKNOWN"}:
                    continue
            if poly_type == "COLUMN":
                if hint_type not in {None, "COLUMN", "FURNITURE"} and entity.classification.structural_type not in {"COLUMN", "UNKNOWN"}:
                    continue

            entity.classification = _make_result(
                cfg,
                structural_type="FURNITURE",
                sub_type=f"ARCHIVED_{poly_type}_EDGE",
                confidence=0.98,
                method="rule:redundant_line",
                needs_review=False,
                review_reason="Redundant with reconstructed structural polygon",
            )
            archived += 1
            break

    return archived


def _bbox_distance(
    a: tuple[float, float, float, float],
    b: tuple[float, float, float, float],
) -> float:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    dx = max(ax0 - bx1, bx0 - ax1, 0.0)
    dy = max(ay0 - by1, by0 - ay1, 0.0)
    return math.hypot(dx, dy)


def _build_topology(entities: List[RawEntity], cfg: PipelineConfig) -> None:
    for entity in entities:
        entity.topology.adjacent_ids = []

    candidates: list[tuple[RawEntity, tuple[float, float], tuple[float, float, float, float]]] = []
    for entity in entities:
        if entity.classification.structural_type in {"ANNOTATION", "FURNITURE"}:
            continue
        if entity.geom_props.centroid_x is None or entity.geom_props.centroid_y is None:
            continue
        geom = entity.geometry()
        if geom is None or geom.is_empty:
            continue
        try:
            bounds = tuple(float(v) for v in geom.bounds)
        except Exception:
            continue
        candidates.append(
            (
                entity,
                (float(entity.geom_props.centroid_x), float(entity.geom_props.centroid_y)),
                bounds,
            )
        )

    if not candidates:
        return

    centroid_threshold = max(150.0, cfg.snap_distance_cm * 10.0)
    bbox_gap_threshold = max(20.0, cfg.snap_distance_cm * 5.0)
    cell_size = centroid_threshold

    grid: DefaultDict[tuple[int, int], list[int]] = defaultdict(list)
    for idx, (_, (cx, cy), _) in enumerate(candidates):
        key = (int(cx // cell_size), int(cy // cell_size))
        grid[key].append(idx)

    adjacency: dict[str, set[str]] = {item[0].id: set() for item in candidates}

    for idx, (entity, (cx, cy), bounds) in enumerate(candidates):
        base_cell = (int(cx // cell_size), int(cy // cell_size))
        candidate_indices: set[int] = set()

        for ix in range(base_cell[0] - 1, base_cell[0] + 2):
            for iy in range(base_cell[1] - 1, base_cell[1] + 2):
                candidate_indices.update(grid.get((ix, iy), []))

        for other_idx in candidate_indices:
            if other_idx <= idx:
                continue

            other_entity, (ocx, ocy), other_bounds = candidates[other_idx]
            bbox_gap = _bbox_distance(bounds, other_bounds)
            centroid_gap = math.hypot(cx - ocx, cy - ocy)

            if bbox_gap <= bbox_gap_threshold or centroid_gap <= centroid_threshold:
                adjacency[entity.id].add(other_entity.id)
                adjacency[other_entity.id].add(entity.id)

    for entity in entities:
        entity.topology.adjacent_ids = sorted(adjacency.get(entity.id, set()))


def run(
    entities: List[RawEntity],
    config: Optional[PipelineConfig] = None,
    memory_path: Optional[Path] = None,
    cabinet_key: str = "default",
    output_dir: Optional[Path] = None,
) -> List[RawEntity]:
    _ = memory_path
    _ = cabinet_key

    cfg = config or PipelineConfig().apply_tolerance_mode()

    if not entities:
        logger.warning("Classification skipped: no entities provided")
        return entities

    for entity in entities:
        entity.classification = _classify_one(entity, cfg)

    archived_redundant = _archive_redundant_lines(entities, cfg)
    _build_topology(entities, cfg)

    dist = Counter(entity.classification.structural_type for entity in entities)
    review_pending = sum(1 for entity in entities if entity.classification.needs_review)

    logger.info(f"Classification distribution: {dict(dist)}")
    logger.info(
        f"Classification review queue: {review_pending}"
        + (f" | redundant lines archived={archived_redundant}" if archived_redundant else "")
    )

    if output_dir:
        output_dir.mkdir(parents=True, exist_ok=True)
        save_entities_json(
            entities,
            output_dir / "classified_entities.geojson",
            metadata={
                "stage": "classification",
                "distribution": dict(dist),
                "review_pending": review_pending,
                "redundant_lines_archived": archived_redundant,
            },
        )

    return entities


if __name__ == "__main__":
    import argparse

    import coffrage_core as core
    import coffrage_reconstruct as recon

    ap = argparse.ArgumentParser(description="Coffrage Classify")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default="./output_coffrage")
    args = ap.parse_args()

    out = Path(args.output)
    cfg = core.PipelineConfig().apply_tolerance_mode()
    raw = core.run(Path(args.input), out)
    reconstructed = recon.run(raw, cfg, out)
    run(reconstructed, cfg, output_dir=out)