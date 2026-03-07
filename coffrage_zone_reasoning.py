#!/usr/bin/env python3
from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import DefaultDict, Dict, List, Optional, Set, Tuple

from loguru import logger
from shapely.geometry import Polygon

from coffrage_core import PipelineConfig, RawEntity, save_entities_json


STRUCTURAL_TYPES: Set[str] = {"WALL", "COLUMN", "SLAB", "BEAM", "TREMIE", "RESERVATION"}
PRIMARY_STRUCTURAL_TYPES: Set[str] = {"WALL", "COLUMN"}
PROMOTABLE_TYPES: Set[str] = {"WALL", "COLUMN"}
CRITICAL_ISSUE_KEYWORDS: tuple[str, ...] = (
    "INVALID",
    "ERROR",
    "FAILED",
    "MISMATCH",
    "UNSUPPORTED",
    "EMPTY",
    "CORRUPT",
)


@dataclass
class ZoneReasoningConfig:
    min_structural_neighbors_for_support: int = 2
    min_reliable_neighbors_for_support: int = 2
    min_reliable_neighbors_for_promotion: int = 3
    dominant_ratio_for_promotion: float = 0.70
    support_confidence_floor: float = 0.78
    support_confidence_ceiling: float = 0.92
    isolation_review_threshold: float = 0.72
    enable_unknown_promotion: bool = True
    enable_isolation_review: bool = True
    adjacency_centroid_threshold_cm: float = 180.0
    adjacency_bbox_gap_threshold_cm: float = 25.0


@dataclass
class ZoneReasoningStats:
    total_entities: int = 0
    eligible_entities: int = 0
    adjacency_enriched_entities: int = 0
    confidence_updates: int = 0
    unknown_promotions: int = 0
    isolated_marked_for_review: int = 0
    review_cleared_by_support: int = 0


@dataclass
class NeighborSummary:
    total_neighbors: int
    structural_neighbors: int
    reliable_structural_neighbors: int
    by_type: Dict[str, int]
    reliable_by_type: Dict[str, int]
    dominant_reliable_type: Optional[str]
    dominant_reliable_ratio: float


def _add_unique(values: List[str], value: str) -> None:
    if value and value not in values:
        values.append(value)


def _append_review_reason(existing: str, reason: str) -> str:
    reason = (reason or "").strip()
    if not reason:
        return existing
    parts = [p.strip() for p in (existing or "").split(";") if p.strip()]
    if reason not in parts:
        parts.append(reason)
    return "; ".join(parts)


def _has_blocking_issue(entity: RawEntity) -> bool:
    if entity.coherence.errors:
        return True
    for issue in entity.issues:
        text = (issue or "").upper()
        if any(keyword in text for keyword in CRITICAL_ISSUE_KEYWORDS):
            return True
    return False


def _geometry_supports_wall(entity: RawEntity) -> bool:
    geom = entity.geometry()
    if not isinstance(geom, Polygon):
        return False

    thickness = float(entity.geom_props.thickness_cm or 0.0)
    length = float(entity.geom_props.length_cm or 0.0)
    area_m2 = float(entity.geom_props.area_m2 or 0.0)
    aspect = length / max(thickness, 0.1) if length > 0 else 0.0

    return (
        10.0 <= thickness <= 60.0
        and length >= 50.0
        and area_m2 >= 0.10
        and aspect >= 1.8
    )


def _geometry_supports_column(entity: RawEntity) -> bool:
    geom = entity.geometry()
    if not isinstance(geom, Polygon):
        return False

    thickness = float(entity.geom_props.thickness_cm or 0.0)
    length = float(entity.geom_props.length_cm or 0.0)
    area_m2 = float(entity.geom_props.area_m2 or 0.0)

    if thickness <= 0 or length <= 0:
        return False

    min_dim = min(thickness, length)
    max_dim = max(thickness, length)
    aspect = max_dim / max(min_dim, 0.1)

    return (
        12.0 <= min_dim <= 100.0
        and 12.0 <= max_dim <= 160.0
        and 0.01 <= area_m2 <= 2.5
        and aspect <= 2.5
    )


def _geometry_supports_type(entity: RawEntity, structural_type: str) -> bool:
    if structural_type == "WALL":
        return _geometry_supports_wall(entity)
    if structural_type == "COLUMN":
        return _geometry_supports_column(entity)
    return False


def _bbox_distance(
    a: Tuple[float, float, float, float],
    b: Tuple[float, float, float, float],
) -> float:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    dx = max(ax0 - bx1, bx0 - ax1, 0.0)
    dy = max(ay0 - by1, by0 - ay1, 0.0)
    return math.hypot(dx, dy)


def _build_local_adjacency(
    entities: List[RawEntity],
    pipeline_cfg: PipelineConfig,
    zone_cfg: ZoneReasoningConfig,
) -> Dict[str, List[str]]:
    items: list[tuple[RawEntity, tuple[float, float], tuple[float, float, float, float]]] = []

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

        items.append(
            (
                entity,
                (float(entity.geom_props.centroid_x), float(entity.geom_props.centroid_y)),
                bounds,
            )
        )

    if not items:
        return {}

    centroid_threshold = max(zone_cfg.adjacency_centroid_threshold_cm, pipeline_cfg.snap_distance_cm * 10.0)
    bbox_gap_threshold = max(zone_cfg.adjacency_bbox_gap_threshold_cm, pipeline_cfg.snap_distance_cm * 4.0)
    cell_size = centroid_threshold

    grid: DefaultDict[tuple[int, int], list[int]] = defaultdict(list)
    for idx, (_, (cx, cy), _) in enumerate(items):
        key = (int(cx // cell_size), int(cy // cell_size))
        grid[key].append(idx)

    adjacency: Dict[str, Set[str]] = {item[0].id: set() for item in items}

    for idx, (entity, (cx, cy), bounds) in enumerate(items):
        base_cell = (int(cx // cell_size), int(cy // cell_size))
        candidate_indices: Set[int] = set()

        for ix in range(base_cell[0] - 1, base_cell[0] + 2):
            for iy in range(base_cell[1] - 1, base_cell[1] + 2):
                candidate_indices.update(grid.get((ix, iy), []))

        for other_idx in candidate_indices:
            if other_idx <= idx:
                continue

            other_entity, (ocx, ocy), other_bounds = items[other_idx]
            bbox_gap = _bbox_distance(bounds, other_bounds)
            centroid_gap = math.hypot(cx - ocx, cy - ocy)

            if bbox_gap <= bbox_gap_threshold or centroid_gap <= centroid_threshold:
                adjacency[entity.id].add(other_entity.id)
                adjacency[other_entity.id].add(entity.id)

    return {entity_id: sorted(ids) for entity_id, ids in adjacency.items()}


def _merge_adjacency_into_entities(entities: List[RawEntity], local_adjacency: Dict[str, List[str]]) -> int:
    changed = 0
    for entity in entities:
        existing = set(entity.topology.adjacent_ids or [])
        merged = sorted(existing.union(local_adjacency.get(entity.id, [])))
        if merged != (entity.topology.adjacent_ids or []):
            entity.topology.adjacent_ids = merged
            changed += 1
    return changed


def _is_reliable_structural(entity: RawEntity, pipeline_cfg: PipelineConfig) -> bool:
    clf = entity.classification
    if clf.structural_type not in STRUCTURAL_TYPES:
        return False
    if clf.method == "human_review":
        return True
    if clf.needs_review:
        return False
    return float(clf.confidence) >= float(pipeline_cfg.confidence_auto)


def _neighbor_summary(
    entity: RawEntity,
    entities_by_id: Dict[str, RawEntity],
    pipeline_cfg: PipelineConfig,
) -> NeighborSummary:
    total_neighbors = 0
    structural_neighbors = 0
    reliable_structural_neighbors = 0
    by_type: Counter[str] = Counter()
    reliable_by_type: Counter[str] = Counter()

    for neighbor_id in entity.topology.adjacent_ids or []:
        neighbor = entities_by_id.get(neighbor_id)
        if neighbor is None:
            continue

        total_neighbors += 1
        n_type = neighbor.classification.structural_type

        if n_type in STRUCTURAL_TYPES:
            structural_neighbors += 1
            by_type[n_type] += 1
            if _is_reliable_structural(neighbor, pipeline_cfg):
                reliable_structural_neighbors += 1
                reliable_by_type[n_type] += 1

    dominant_type: Optional[str] = None
    dominant_ratio = 0.0
    if reliable_by_type:
        dominant_type, dominant_count = max(reliable_by_type.items(), key=lambda kv: kv[1])
        dominant_ratio = dominant_count / max(reliable_structural_neighbors, 1)

    return NeighborSummary(
        total_neighbors=total_neighbors,
        structural_neighbors=structural_neighbors,
        reliable_structural_neighbors=reliable_structural_neighbors,
        by_type=dict(by_type),
        reliable_by_type=dict(reliable_by_type),
        dominant_reliable_type=dominant_type,
        dominant_reliable_ratio=dominant_ratio,
    )


def _can_clear_review(entity: RawEntity) -> bool:
    if _has_blocking_issue(entity):
        return False

    reason = (entity.classification.review_reason or "").lower()
    blocking_markers = (
        "critical_issue",
        "coherence_error",
        "coherence_warning",
        "blocking_issue",
        "zone:isolation",
    )
    return not any(marker in reason for marker in blocking_markers)


def _support_existing_structural(
    entity: RawEntity,
    summary: NeighborSummary,
    pipeline_cfg: PipelineConfig,
    zone_cfg: ZoneReasoningConfig,
    stats: ZoneReasoningStats,
) -> None:
    clf = entity.classification
    entity_type = clf.structural_type

    if entity_type not in STRUCTURAL_TYPES or clf.method == "human_review":
        return

    same_type_reliable = int(summary.reliable_by_type.get(entity_type, 0))
    enough_support = (
        summary.structural_neighbors >= zone_cfg.min_structural_neighbors_for_support
        and summary.reliable_structural_neighbors >= zone_cfg.min_reliable_neighbors_for_support
        and (same_type_reliable >= 1 or summary.dominant_reliable_type == entity_type)
    )

    if enough_support:
        boost = 0.02 * min(summary.reliable_structural_neighbors, 5)
        new_conf = min(
            zone_cfg.support_confidence_ceiling,
            max(float(clf.confidence), zone_cfg.support_confidence_floor + boost),
        )

        if new_conf > float(clf.confidence):
            clf.confidence = round(new_conf, 2)
            if clf.method != "human_review":
                clf.method = "zone:context_support"
            stats.confidence_updates += 1

        _add_unique(entity.coherence.passed, "zone_supported")
        entity.topology.zone_label = "SUPPORTED_STRUCTURAL"

        if clf.needs_review and new_conf >= pipeline_cfg.confidence_auto and _can_clear_review(entity):
            clf.needs_review = False
            clf.review_reason = ""
            stats.review_cleared_by_support += 1

        return

    if (
        zone_cfg.enable_isolation_review
        and summary.structural_neighbors == 0
        and float(clf.confidence) < zone_cfg.isolation_review_threshold
    ):
        if not clf.needs_review:
            stats.isolated_marked_for_review += 1
        clf.needs_review = True
        clf.review_reason = _append_review_reason(clf.review_reason, "zone:isolation")
        if clf.method != "human_review":
            clf.method = "zone:isolation_review"
        clf.confidence = round(min(float(clf.confidence), zone_cfg.isolation_review_threshold), 2)
        _add_unique(entity.coherence.warnings, "zone_isolated")
        entity.topology.zone_label = "ISOLATED_STRUCTURAL"


def _promote_unknown_if_supported(
    entity: RawEntity,
    summary: NeighborSummary,
    pipeline_cfg: PipelineConfig,
    zone_cfg: ZoneReasoningConfig,
    stats: ZoneReasoningStats,
) -> None:
    clf = entity.classification

    if clf.method == "human_review":
        return
    if clf.structural_type != "UNKNOWN":
        return
    if not zone_cfg.enable_unknown_promotion:
        return
    if summary.reliable_structural_neighbors < zone_cfg.min_reliable_neighbors_for_promotion:
        return

    dominant_type = summary.dominant_reliable_type
    if dominant_type not in PROMOTABLE_TYPES:
        return
    if summary.dominant_reliable_ratio < zone_cfg.dominant_ratio_for_promotion:
        return
    if not _geometry_supports_type(entity, dominant_type):
        return

    clf.structural_type = dominant_type
    clf.sub_type = "ZONE_PROMOTED"
    clf.confidence = round(
        min(
            zone_cfg.support_confidence_ceiling,
            max(zone_cfg.support_confidence_floor, float(pipeline_cfg.confidence_auto) + 0.02),
        ),
        2,
    )
    clf.method = "zone:promote_unknown"
    clf.needs_review = _has_blocking_issue(entity)
    clf.review_reason = "" if not clf.needs_review else _append_review_reason(clf.review_reason, "zone:blocking_issue")

    _add_unique(entity.coherence.passed, "zone_promoted")
    entity.topology.zone_label = f"PROMOTED_{dominant_type}"
    stats.unknown_promotions += 1
    stats.confidence_updates += 1


def run(
    entities: List[RawEntity],
    context_projet: str = "",
    output_path: Optional[Path] = None,
    max_workers: int = 1,
    config: Optional[ZoneReasoningConfig] = None,
    pipeline_config: Optional[PipelineConfig] = None,
) -> List[RawEntity]:
    _ = context_projet
    _ = max_workers

    if not entities:
        logger.info("Zone reasoning: no entities to process")
        return entities

    zone_cfg = config or ZoneReasoningConfig()
    pipe_cfg = pipeline_config or PipelineConfig().apply_tolerance_mode()
    stats = ZoneReasoningStats(total_entities=len(entities))

    local_adjacency = _build_local_adjacency(entities, pipe_cfg, zone_cfg)
    stats.adjacency_enriched_entities = _merge_adjacency_into_entities(entities, local_adjacency)

    entities_by_id = {entity.id: entity for entity in entities}

    for entity in entities:
        clf = entity.classification
        if clf.structural_type in {"ANNOTATION", "FURNITURE"}:
            continue

        stats.eligible_entities += 1
        summary = _neighbor_summary(entity, entities_by_id, pipe_cfg)

        _promote_unknown_if_supported(entity, summary, pipe_cfg, zone_cfg, stats)
        _support_existing_structural(entity, summary, pipe_cfg, zone_cfg, stats)

    dist = Counter(entity.classification.structural_type for entity in entities)
    logger.info(
        "Zone reasoning: "
        f"eligible={stats.eligible_entities} | "
        f"adjacency_enriched={stats.adjacency_enriched_entities} | "
        f"confidence_updates={stats.confidence_updates} | "
        f"unknown_promotions={stats.unknown_promotions} | "
        f"isolated_marked={stats.isolated_marked_for_review} | "
        f"review_cleared={stats.review_cleared_by_support}"
    )
    logger.info(f"Zone reasoning distribution: {dict(dist)}")

    if output_path:
        save_entities_json(
            entities,
            output_path,
            metadata={
                "stage": "zone_reasoning",
                "zone_reasoning": {
                    "total_entities": stats.total_entities,
                    "eligible_entities": stats.eligible_entities,
                    "adjacency_enriched_entities": stats.adjacency_enriched_entities,
                    "confidence_updates": stats.confidence_updates,
                    "unknown_promotions": stats.unknown_promotions,
                    "isolated_marked_for_review": stats.isolated_marked_for_review,
                    "review_cleared_by_support": stats.review_cleared_by_support,
                },
            },
        )

    return entities


if __name__ == "__main__":
    print("Use via coffrage_pipeline.py")