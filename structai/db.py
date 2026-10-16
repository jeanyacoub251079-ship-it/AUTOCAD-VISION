"""Base SQLite locale (§2.4.3) avec migrations versionnées.

Tables : projects, plans, interpretations, options, edits, deliverables,
ai_calls (traçabilité IA §5.6.1), alerts (filet de sécurité §5.4), incidents,
snapshots, access_log.

Choix pragmatique pour une V1 mono-utilisateur : sqlite3 stdlib + migrations
SQL incrémentales (l'usage d'SQLAlchemy/Alembic est prévu en V1.1 si le schéma
évolue ; voir README « écarts assumés »).
"""
from __future__ import annotations

import sqlite3
import threading
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from .config import DB_PATH, ensure_dirs

_local = threading.local()
_init_lock = threading.Lock()

SCHEMA_VERSION = 1

MIGRATIONS: dict[int, list[str]] = {
    1: [
        """
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            ref TEXT,
            comment TEXT,
            params TEXT NOT NULL DEFAULT '{}',   -- JSON (sections A..G)
            status TEXT NOT NULL DEFAULT 'nouveau',
            last_view TEXT DEFAULT 'dashboard',
            client_agreement INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS plans (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            filename TEXT NOT NULL,
            path TEXT NOT NULL,
            size INTEGER,
            sha256 TEXT,
            dxf_version TEXT,
            units TEXT,
            bbox TEXT,                          -- JSON {min:[x,y],max:[x,y]}
            layers TEXT,                        -- JSON [{nom, couleur, nb, exclure}]
            entities_count INTEGER DEFAULT 0,
            png_original TEXT,
            png_clean TEXT,
            entities_json TEXT,
            meta TEXT,
            anonymization_ok INTEGER DEFAULT 1,
            imported_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS interpretations (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            plan_id TEXT REFERENCES plans(id) ON DELETE CASCADE,
            source TEXT NOT NULL DEFAULT 'ia',   -- 'ia' | 'manuel'
            provider TEXT, model TEXT,
            json TEXT NOT NULL,
            validated INTEGER NOT NULL DEFAULT 0,
            validation TEXT,
            created_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS options (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            interpretation_id TEXT,
            method TEXT,
            seed INTEGER,
            short_desc TEXT,
            json TEXT NOT NULL,                  -- option complète (structure+résultats)
            indicators TEXT,                     -- JSON résumé pour comparateur
            conformity TEXT,                     -- JSON {ec0,ec1,ec2,ec8,an_fr}
            status TEXT NOT NULL DEFAULT 'generee',  -- generee|retenue|rejetee|figee
            rank INTEGER,
            created_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS edits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            option_id TEXT NOT NULL REFERENCES options(id) ON DELETE CASCADE,
            project_id TEXT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            element TEXT,
            before TEXT, after TEXT,
            reason TEXT NOT NULL DEFAULT '',
            option_json_after TEXT               -- instantané après édition (undo)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS deliverables (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            option_id TEXT,
            type TEXT NOT NULL,                  -- plan_dxf|note_pdf|quantitatifs|traacabilite
            path TEXT NOT NULL,
            sha256 TEXT,
            meta TEXT,
            created_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ai_calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            project_id TEXT,
            provider TEXT NOT NULL,
            model TEXT NOT NULL,
            purpose TEXT NOT NULL,               -- interpretation_plan|generation_creative|redaction_note
            tokens_in INTEGER, tokens_out INTEGER,
            cost_usd REAL,
            hash_req TEXT, hash_resp TEXT,
            size_req INTEGER,
            status TEXT NOT NULL,                -- succes|echec|retry|bloque
            latency_s REAL,
            detail TEXT
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            project_id TEXT,
            kind TEXT NOT NULL,                  -- texte_suspect|image|cartouche|nom_fichier|incoherence|plafond
            detail TEXT,
            decision TEXT DEFAULT 'en_attente'   -- ignoree|corrigee|bloquee|en_attente
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            title TEXT NOT NULL,
            detail TEXT,
            actions TEXT,
            closed INTEGER NOT NULL DEFAULT 0
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS snapshots (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
            option_id TEXT,
            kind TEXT NOT NULL,                  -- etape|figeage|avant_suppression
            label TEXT,
            path TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS access_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            kind TEXT NOT NULL,
            detail TEXT
        );
        """,
        "CREATE INDEX IF NOT EXISTS idx_plans_project ON plans(project_id);",
        "CREATE INDEX IF NOT EXISTS idx_options_project ON options(project_id);",
        "CREATE INDEX IF NOT EXISTS idx_aicalls_project ON ai_calls(project_id);",
        "CREATE INDEX IF NOT EXISTS idx_edits_option ON edits(option_id);",
    ]
}


def _connect(path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(path), check_same_thread=False, timeout=15)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA journal_mode = WAL;")
    return conn


def migrate(db: sqlite3.Connection) -> None:
    cur = db.execute("PRAGMA user_version;").fetchone()
    version = int(cur[0]) if cur else 0
    if version == 0 and db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='projects'"
    ).fetchone():
        version = 1  # base créée hors-migration
    for v in sorted(MIGRATIONS):
        if v > version:
            for stmt in MIGRATIONS[v]:
                db.execute(stmt)
            db.execute(f"PRAGMA user_version = {v};")
            version = v
    db.commit()


@contextmanager
def get_db() -> Iterator[sqlite3.Connection]:
    conn = getattr(_local, "conn", None)
    if conn is None:
        ensure_dirs()
        conn = _connect(DB_PATH)
        with _init_lock:
            migrate(conn)
        _local.conn = conn
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def db_integrity_ok() -> tuple[bool, str]:
    try:
        ensure_dirs()
        conn = _connect(DB_PATH)
        row = conn.execute("PRAGMA integrity_check;").fetchone()
        conn.close()
        ok = row and row[0] == "ok"
        return bool(ok), str(row[0] if row else "?")
    except Exception as exc:
        return False, str(exc)


def rows_to_list(rows) -> list[dict]:
    return [dict(r) for r in rows]
