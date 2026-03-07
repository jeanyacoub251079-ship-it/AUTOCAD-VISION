#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib
import json
import sys
from collections import Counter
from pathlib import Path
from time import perf_counter
from typing import Any, Dict, Optional

from loguru import logger


def _import_module(module_name: str):
    try:
        return importlib.import_module(module_name)
    except Exception as exc:
        raise RuntimeError(f"Unable to import required module '{module_name}'") from exc


def _ensure_output_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def _persist_entities(core_mod, entities: list[Any], path: Path, stage: str, extra_metadata: Optional[dict] = None) -> Path:
    metadata = {"stage": stage}
    if extra_metadata:
        metadata.update(extra_metadata)
    core_mod.save_entities_json(entities, path, metadata=metadata)
    return path


def _entity_snapshot(entities: list[Any]) -> dict[str, Any]:
    dist = Counter()
    review_pending = 0
    trusted_wall_column = 0

    for entity in entities:
        clf = getattr(entity, "classification", None)
        if clf is None:
            continue

        structural_type = getattr(clf, "structural_type", "UNKNOWN") or "UNKNOWN"
        dist[structural_type] += 1

        if bool(getattr(clf, "needs_review", False)):
            review_pending += 1

        if structural_type in {"WALL", "COLUMN"} and not bool(getattr(clf, "needs_review", False)):
            trusted_wall_column += 1

    return {
        "total": len(entities),
        "distribution": dict(sorted(dist.items(), key=lambda kv: (-kv[1], kv[0]))),
        "review_pending": review_pending,
        "trusted_wall_column": trusted_wall_column,
    }


def _log_snapshot(stage_label: str, entities: list[Any]) -> None:
    snap = _entity_snapshot(entities)
    logger.info(
        f"{stage_label}: total={snap['total']} | review_pending={snap['review_pending']} "
        f"| trusted_wall_column={snap['trusted_wall_column']} | distribution={snap['distribution']}"
    )


def _warn_if_suspicious(stage_label: str, entities: list[Any]) -> None:
    snap = _entity_snapshot(entities)
    wall_count = int(snap["distribution"].get("WALL", 0))
    column_count = int(snap["distribution"].get("COLUMN", 0))

    if snap["total"] == 0:
        logger.warning(f"{stage_label}: no entity available")
        return

    if wall_count + column_count == 0:
        logger.warning(f"{stage_label}: no WALL/COLUMN detected after processing")

    if snap["review_pending"] == snap["total"] and snap["total"] > 0:
        logger.warning(f"{stage_label}: every entity is pending review")


def _write_pipeline_summary(
    summary_path: Path,
    *,
    input_path: Path,
    output_dir: Path,
    project_name: str,
    options: dict[str, Any],
    stage_times: dict[str, float],
    stage_files: dict[str, str],
    stage_status: dict[str, Any],
    final_snapshot: Optional[dict[str, Any]],
    outputs: dict[str, Path],
) -> Path:
    payload = {
        "input": str(input_path),
        "output_dir": str(output_dir),
        "project_name": project_name,
        "options": options,
        "stage_times_s": stage_times,
        "stage_files": stage_files,
        "stage_status": stage_status,
        "final_snapshot": final_snapshot,
        "outputs": {k: str(v) for k, v in outputs.items()},
    }
    summary_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary_path


def _read_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _read_m0_report(audit_dir: Path) -> Optional[dict]:
    return _read_json(audit_dir / "m0_report.json")


def _m0_is_usable(m0_report: Optional[dict]) -> tuple[bool, str]:
    if not m0_report:
        return False, "missing_m0_report"

    status = str(m0_report.get("status", "") or "")
    vector_counts = m0_report.get("vector_counts", {}) or {}
    walls = int(vector_counts.get("walls", 0) or 0)
    columns = int(vector_counts.get("columns", 0) or 0)

    if status == "empty_segmentation":
        return False, "empty_segmentation"

    if walls + columns <= 0:
        return False, "no_structural_entities_detected"

    return True, "ok"


def run_pipeline(
    input_path: Path,
    output_dir: Path,
    project_name: str = "PROJET",
    tolerance_mode: str = "NORMAL",
    enable_m0: bool = True,
    m0_only_structure: bool = False,
    m0_model: Path | None = None,
    m0_dpi: int = 300,
    vision_only: bool = False,
    skip_review: bool = False,
    skip_precontrol: bool = False,
    skip_zone_reasoning: bool = False,
    review_port: int = 5050,
    review_auto_open: bool = True,
    review_user: str = "operator",
    vision_path: Path | None = None,
) -> dict[str, Path]:
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if vision_only and not enable_m0:
        raise ValueError("vision_only mode requires M0 to be enabled")
    if review_port <= 0:
        raise ValueError("review_port must be > 0")
    if vision_path is not None and not vision_path.exists():
        raise FileNotFoundError(f"Vision file not found: {vision_path}")

    output_dir = _ensure_output_dir(output_dir)
    base_stem = input_path.stem
    t0 = perf_counter()

    stage_times: dict[str, float] = {}
    stage_files: dict[str, str] = {}
    stage_status: dict[str, Any] = {}

    file_sink_id = logger.add(
        output_dir / "pipeline.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level:8s} | {message}",
        level="INFO",
        encoding="utf-8",
    )

    try:
        core = _import_module("coffrage_core")

        logger.info("=" * 72)
        logger.info(f"COFFRAGE PIPELINE - {input_path.name}")
        logger.info(f"Project: {project_name}")
        logger.info(f"Tolerance: {tolerance_mode}")
        logger.info(f"M0 enabled: {'YES' if enable_m0 else 'NO'}")
        logger.info(f"Vision only: {'YES' if vision_only else 'NO'}")
        logger.info(f"Vision source: {vision_path if vision_path else 'DXF rasterized internally'}")
        logger.info(f"Output: {output_dir}")
        logger.info("=" * 72)

        cfg = core.PipelineConfig(tolerance_mode=tolerance_mode).apply_tolerance_mode()
        current_input = input_path

        if enable_m0:
            logger.info("M0 - Vision filter")
            m0 = _import_module("coffrage_m0_vision_filter")
            m0_output = output_dir / f"{base_stem}_M0_filtered.dxf"
            m0_audit_dir = output_dir / "m0_audit"

            t = perf_counter()
            m0.run(
                input_path=input_path,
                output_path=m0_output,
                only_structure=m0_only_structure,
                model_path=m0_model,
                dpi=m0_dpi,
                audit_dir=m0_audit_dir,
                vision_path=vision_path,
            )
            stage_times["M0_vision_filter"] = round(perf_counter() - t, 3)
            stage_files["m0_dxf"] = str(m0_output)

            m0_report = _read_m0_report(m0_audit_dir)
            if m0_report:
                stage_files["m0_report"] = str(m0_audit_dir / "m0_report.json")

            m0_ok, m0_reason = _m0_is_usable(m0_report)
            stage_status["m0"] = {
                "used_for_downstream": m0_ok,
                "status": m0_reason,
                "report": m0_report or {},
            }

            if m0_ok:
                logger.info("M0 accepted as downstream input")
                current_input = m0_output
            else:
                logger.warning(f"M0 bypassed for downstream processing: {m0_reason}")
                current_input = input_path
        else:
            m0_output = None
            stage_status["m0"] = {
                "used_for_downstream": False,
                "status": "disabled",
            }

        if vision_only:
            outputs: dict[str, Path] = {"m0_dxf": m0_output if m0_output is not None else input_path}
            summary_path = _write_pipeline_summary(
                output_dir / f"{base_stem}_pipeline_summary.json",
                input_path=input_path,
                output_dir=output_dir,
                project_name=project_name,
                options={
                    "tolerance_mode": tolerance_mode,
                    "enable_m0": enable_m0,
                    "m0_only_structure": m0_only_structure,
                    "m0_model": str(m0_model) if m0_model else "",
                    "m0_dpi": m0_dpi,
                    "vision_only": vision_only,
                    "skip_review": skip_review,
                    "skip_precontrol": skip_precontrol,
                    "skip_zone_reasoning": skip_zone_reasoning,
                    "review_port": review_port,
                    "review_auto_open": review_auto_open,
                    "review_user": review_user,
                    "vision_path": str(vision_path) if vision_path else "",
                },
                stage_times=stage_times,
                stage_files=stage_files,
                stage_status=stage_status,
                final_snapshot=None,
                outputs=outputs,
            )
            outputs["pipeline_summary"] = summary_path
            logger.info(f"Vision-only mode completed in {round(perf_counter() - t0, 3)}s")
            return outputs

        logger.info("M1 - Ingestion & Extraction")
        t = perf_counter()
        raw_entities = core.run(current_input, None, tolerance_mode)
        stage_times["M1_ingestion_extraction"] = round(perf_counter() - t, 3)
        raw_path = output_dir / f"{base_stem}_raw_entities.geojson"
        _persist_entities(
            core,
            raw_entities,
            raw_path,
            "M1_ingestion_extraction",
            extra_metadata={
                "input_file": str(current_input),
                "input_file_original": str(input_path),
                "m0_used_as_input": current_input == (m0_output or input_path),
            },
        )
        stage_files["raw_geojson"] = str(raw_path)
        _log_snapshot("M1 snapshot", raw_entities)

        logger.info("M2 - Reconstruction")
        recon = _import_module("coffrage_reconstruct")
        t = perf_counter()
        reconstructed = recon.run(raw_entities, cfg, None)
        stage_times["M2_reconstruction"] = round(perf_counter() - t, 3)
        reconstructed_path = output_dir / f"{base_stem}_reconstructed.geojson"
        _persist_entities(core, reconstructed, reconstructed_path, "M2_reconstruction")
        stage_files["reconstructed_geojson"] = str(reconstructed_path)
        _log_snapshot("M2 snapshot", reconstructed)

        logger.info("M3 - Classification")
        classify = _import_module("coffrage_classify")
        t = perf_counter()
        classified = classify.run(reconstructed, cfg, output_dir=None)
        stage_times["M3_classification"] = round(perf_counter() - t, 3)
        classified_path = output_dir / f"{base_stem}_classified.geojson"
        _persist_entities(core, classified, classified_path, "M3_classification")
        stage_files["classified_geojson"] = str(classified_path)
        _log_snapshot("M3 snapshot", classified)

        current_entities = classified
        current_geojson = classified_path

        if not skip_zone_reasoning:
            logger.info("M3.1 - Zone-aware reasoning")
            zone = _import_module("coffrage_zone_reasoning")
            t = perf_counter()
            current_entities = zone.run(current_entities, output_path=None, pipeline_config=cfg)
            stage_times["M3_1_zone_reasoning"] = round(perf_counter() - t, 3)
            zone_path = output_dir / f"{base_stem}_zone_reasoned.geojson"
            _persist_entities(core, current_entities, zone_path, "M3_1_zone_reasoning")
            stage_files["zone_reasoned_geojson"] = str(zone_path)
            current_geojson = zone_path
            _log_snapshot("M3.1 snapshot", current_entities)
        else:
            logger.info("M3.1 skipped (--no-zone-reasoning)")
            stage_status["zone_reasoning"] = {"status": "skipped"}

        if not skip_precontrol:
            logger.info("M3.2 - Precontrol")
            pre = _import_module("coffrage_precontrol")
            t = perf_counter()
            current_entities = pre.run(current_entities, output_path=None, pipeline_config=cfg)
            stage_times["M3_2_precontrol"] = round(perf_counter() - t, 3)
            precontrol_path = output_dir / f"{base_stem}_precontrolled.geojson"
            _persist_entities(core, current_entities, precontrol_path, "M3_2_precontrol")
            stage_files["precontrolled_geojson"] = str(precontrol_path)
            current_geojson = precontrol_path
            _log_snapshot("M3.2 snapshot", current_entities)
        else:
            logger.info("M3.2 skipped (--no-precontrol)")
            stage_status["precontrol"] = {"status": "skipped"}

        _warn_if_suspicious("Pre-output validation", current_entities)

        reviewed_path = output_dir / f"{base_stem}_reviewed.geojson"
        if not skip_review:
            logger.info("M4 - Review")
            review = _import_module("coffrage_review")
            t = perf_counter()
            review.run(
                current_geojson,
                reviewed_path,
                port=review_port,
                auto_open=review_auto_open,
                review_user=review_user,
            )
            stage_times["M4_review"] = round(perf_counter() - t, 3)

            if reviewed_path.exists():
                final_geojson = reviewed_path
                stage_files["reviewed_geojson"] = str(reviewed_path)
            else:
                logger.warning("M4 finished without reviewed output file; falling back to latest automatic GeoJSON")
                final_geojson = current_geojson
        else:
            logger.info("M4 skipped (--no-review)")
            final_geojson = current_geojson
            stage_status["review"] = {"status": "skipped"}

        stage_files["final_geojson"] = str(final_geojson)

        logger.info("M5 - DXF output")
        output_mod = _import_module("coffrage_output")
        t = perf_counter()
        outputs = output_mod.run(final_geojson, output_dir, project_name)
        stage_times["M5_output"] = round(perf_counter() - t, 3)

        final_entities = core.load_entities_json(final_geojson, as_entities=True)
        final_snapshot = _entity_snapshot(final_entities)
        _warn_if_suspicious("Final snapshot", final_entities)

        summary_path = _write_pipeline_summary(
            output_dir / f"{base_stem}_pipeline_summary.json",
            input_path=input_path,
            output_dir=output_dir,
            project_name=project_name,
            options={
                "tolerance_mode": tolerance_mode,
                "enable_m0": enable_m0,
                "m0_only_structure": m0_only_structure,
                "m0_model": str(m0_model) if m0_model else "",
                "m0_dpi": m0_dpi,
                "vision_only": vision_only,
                "skip_review": skip_review,
                "skip_precontrol": skip_precontrol,
                "skip_zone_reasoning": skip_zone_reasoning,
                "review_port": review_port,
                "review_auto_open": review_auto_open,
                "review_user": review_user,
                "vision_path": str(vision_path) if vision_path else "",
            },
            stage_times=stage_times,
            stage_files=stage_files,
            stage_status=stage_status,
            final_snapshot=final_snapshot,
            outputs=outputs,
        )
        outputs["pipeline_summary"] = summary_path

        elapsed = round(perf_counter() - t0, 3)
        logger.info(f"Pipeline completed in {elapsed}s")
        return outputs

    finally:
        logger.remove(file_sink_id)


def main() -> int:
    logger.remove()
    logger.add(
        sink=lambda message: print(message, end=""),
        format="{time:HH:mm:ss} | {level:8s} | {message}",
        level="INFO",
    )

    ap = argparse.ArgumentParser(description="Coffrage Pipeline")
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default="./output_coffrage")
    ap.add_argument("-p", "--project", default="PROJET")
    ap.add_argument("--tolerance", choices=["STRICT", "NORMAL", "LOOSE"], default="NORMAL")
    ap.add_argument("--disable-m0", action="store_true", help="Disable M0 vision filter")
    ap.add_argument("--m0-only-structure", action="store_true", help="M0 removes ARCHI_FOND entities")
    ap.add_argument("--m0-model", default="", help="Path to torch model for M0")
    ap.add_argument("--m0-dpi", type=int, default=300, help="Raster DPI for M0")
    ap.add_argument("--vision", default="", help="Optional PDF/PNG/JPG source for M0")
    ap.add_argument("--vision-only", action="store_true", help="Run only M0 and exit")
    ap.add_argument("--no-review", action="store_true")
    ap.add_argument("--no-precontrol", action="store_true")
    ap.add_argument("--no-zone-reasoning", action="store_true")
    ap.add_argument("--review-port", type=int, default=5050)
    ap.add_argument("--no-browser", action="store_true", help="Do not auto-open browser for review")
    ap.add_argument("--review-user", default="operator")
    ap.add_argument("--inspect", action="store_true")
    args = ap.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output)
    vision_path = Path(args.vision) if args.vision else None

    try:
        core = _import_module("coffrage_core")

        if args.inspect:
            print(json.dumps(core.inspect_file(input_path), indent=2, ensure_ascii=False))
            return 0

        results = run_pipeline(
            input_path=input_path,
            output_dir=output_dir,
            project_name=args.project,
            tolerance_mode=args.tolerance,
            enable_m0=not args.disable_m0,
            m0_only_structure=args.m0_only_structure,
            m0_model=Path(args.m0_model) if args.m0_model else None,
            m0_dpi=args.m0_dpi,
            vision_only=args.vision_only,
            skip_review=args.no_review,
            skip_precontrol=args.no_precontrol,
            skip_zone_reasoning=args.no_zone_reasoning,
            review_port=args.review_port,
            review_auto_open=not args.no_browser,
            review_user=args.review_user,
            vision_path=vision_path,
        )

        print({k: str(v) for k, v in results.items()})
        return 0

    except Exception as exc:
        logger.exception(f"Pipeline failed: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())