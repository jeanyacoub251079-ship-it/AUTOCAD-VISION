#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set

from loguru import logger

from coffrage_core import (
    PipelineConfig,
    RawEntity,
    load_entities_json_entities,
    save_entities_json,
)


STRUCTURAL_TYPES: Set[str] = {"WALL", "COLUMN", "SLAB", "BEAM", "TREMIE", "RESERVATION"}

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
class PrecontrolConfig:
    use_pipeline_thresholds: bool = True
    fallback_confidence_threshold: float = 0.65
    very_low_confidence_threshold: float = 0.40
    mark_unknown_for_review: bool = True
    mark_low_confidence_structural: bool = True
    mark_entities_with_critical_issues: bool = True
    mark_entities_with_coherence_errors: bool = True
    mark_entities_with_coherence_warnings: bool = False


@dataclass
class PrecontrolStats:
    total_entities: int = 0
    already_human_reviewed: int = 0
    already_pending_review: int = 0
    newly_marked_for_review: int = 0
    reasons: Dict[str, int] = field(default_factory=dict)


def _contains_critical_issue(entity: RawEntity) -> bool:
    for issue in entity.issues:
        issue_upper = (issue or "").upper()
        if any(keyword in issue_upper for keyword in CRITICAL_ISSUE_KEYWORDS):
            return True
    return False


def _confidence_threshold(
    pipeline_config: PipelineConfig,
    precontrol_config: PrecontrolConfig,
) -> float:
    if precontrol_config.use_pipeline_thresholds:
        return float(pipeline_config.confidence_auto)
    return float(precontrol_config.fallback_confidence_threshold)


def _compute_review_reasons(
    entity: RawEntity,
    pipeline_config: PipelineConfig,
    precontrol_config: PrecontrolConfig,
) -> List[str]:
    reasons: List[str] = []
    clf = entity.classification

    if clf.method == "human_review":
        return reasons

    threshold = _confidence_threshold(pipeline_config, precontrol_config)

    if precontrol_config.mark_unknown_for_review and clf.structural_type == "UNKNOWN":
        reasons.append("type_unknown")

    if precontrol_config.mark_low_confidence_structural:
        if clf.structural_type in STRUCTURAL_TYPES and float(clf.confidence) < threshold:
            if float(clf.confidence) < precontrol_config.very_low_confidence_threshold:
                reasons.append(f"very_low_confidence:{float(clf.confidence):.2f}")
            else:
                reasons.append(f"low_confidence:{float(clf.confidence):.2f}")

    if precontrol_config.mark_entities_with_critical_issues and _contains_critical_issue(entity):
        reasons.append("critical_issue")

    if precontrol_config.mark_entities_with_coherence_errors and entity.coherence.errors:
        reasons.append("coherence_error")

    if precontrol_config.mark_entities_with_coherence_warnings and entity.coherence.warnings:
        reasons.append("coherence_warning")

    return reasons


def _merge_review_reason(existing_reason: str, new_reasons: List[str]) -> str:
    parts: List[str] = []

    current = (existing_reason or "").strip()
    if current:
        parts.append(current)

    for reason in new_reasons:
        tag = f"precontrol:{reason}"
        if tag not in parts:
            parts.append(tag)

    return "; ".join(parts)


def _increment_reason_stats(stats: PrecontrolStats, reasons: List[str]) -> None:
    for reason in reasons:
        key = reason.split(":", 1)[0]
        stats.reasons[key] = stats.reasons.get(key, 0) + 1


def run(
    entities: List[RawEntity],
    context_projet: str = "",
    dry_run: bool = False,
    output_path: Optional[Path] = None,
    max_workers: int = 1,
    pipeline_config: Optional[PipelineConfig] = None,
    precontrol_config: Optional[PrecontrolConfig] = None,
) -> List[RawEntity]:
    _ = context_projet
    _ = max_workers

    cfg = pipeline_config or PipelineConfig().apply_tolerance_mode()
    pcfg = precontrol_config or PrecontrolConfig()
    stats = PrecontrolStats(total_entities=len(entities))

    for entity in entities:
        clf = entity.classification

        if clf.method == "human_review":
            stats.already_human_reviewed += 1
            continue

        reasons = _compute_review_reasons(entity, cfg, pcfg)

        if not reasons:
            if clf.needs_review:
                stats.already_pending_review += 1
            continue

        if clf.needs_review:
            stats.already_pending_review += 1
        else:
            clf.needs_review = True
            stats.newly_marked_for_review += 1

        clf.review_reason = _merge_review_reason(clf.review_reason, reasons)
        _increment_reason_stats(stats, reasons)

    logger.info(
        f"Precontrol: total={stats.total_entities} | "
        f"already_human_reviewed={stats.already_human_reviewed} | "
        f"already_pending_review={stats.already_pending_review} | "
        f"newly_marked_for_review={stats.newly_marked_for_review}"
    )

    if stats.reasons:
        details = ", ".join(
            f"{k}={v}" for k, v in sorted(stats.reasons.items(), key=lambda kv: (-kv[1], kv[0]))
        )
        logger.info(f"Precontrol reasons: {details}")

    if output_path and not dry_run:
        save_entities_json(
            entities,
            output_path,
            metadata={
                "stage": "precontrol",
                "precontrol": {
                    "total_entities": stats.total_entities,
                    "already_human_reviewed": stats.already_human_reviewed,
                    "already_pending_review": stats.already_pending_review,
                    "newly_marked_for_review": stats.newly_marked_for_review,
                    "reasons": stats.reasons,
                },
            },
        )

    return entities


def main() -> int:
    import argparse
    import sys

    ap = argparse.ArgumentParser(description="Coffrage Precontrol")
    ap.add_argument("input", help="Input GeoJSON file")
    ap.add_argument("-o", "--output", default="", help="Output GeoJSON path")
    ap.add_argument("--dry-run", action="store_true", help="Run without writing output")
    ap.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.0,
        help="Override confidence threshold (0 = use PipelineConfig.confidence_auto)",
    )
    ap.add_argument(
        "--include-coherence-warnings",
        action="store_true",
        help="Also mark entities with coherence warnings",
    )
    args = ap.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file not found: {input_path}")
        return 1

    output_path = Path(args.output) if args.output else input_path

    try:
        entities = load_entities_json_entities(input_path)
    except Exception as exc:
        logger.error(f"Unable to load entities: {exc}")
        return 1

    pipeline_cfg = PipelineConfig().apply_tolerance_mode()
    pre_cfg = PrecontrolConfig(
        mark_entities_with_coherence_warnings=args.include_coherence_warnings,
    )

    if args.confidence_threshold > 0:
        pre_cfg.use_pipeline_thresholds = False
        pre_cfg.fallback_confidence_threshold = args.confidence_threshold

    try:
        run(
            entities,
            dry_run=args.dry_run,
            output_path=None if args.dry_run else output_path,
            pipeline_config=pipeline_cfg,
            precontrol_config=pre_cfg,
        )
    except Exception as exc:
        logger.error(f"Precontrol failed: {exc}")
        return 1

    if args.dry_run:
        logger.info("Dry-run completed successfully")
    else:
        logger.info(f"Output written to {output_path}")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())