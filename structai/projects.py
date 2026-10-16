"""Gestion de projet locale (§1.6-1, §3.3, §5.10) : CRUD, snapshots, purge.

- Un projet = une ligne SQLite + un répertoire structuré sous
  data/projects/<ID>/ (plans, rendus, interpretations, options, calculs,
  livrables, snapshots).
- Snapshot = archive ZIP horodatée du dossier projet à chaque étape majeure.
- Suppression définitive exige la saisie du nom technique du projet (§5.7.5).
"""
from __future__ import annotations

import json
import shutil
import zipfile
from pathlib import Path
from typing import Any, Optional

from .config import project_dir
from .db import get_db
from .logging_setup import get_logger
from .util import jsonable, new_id, now_iso, read_json, write_json

log = get_logger("structai.projects")


def list_projects(limit: int = 50) -> list[dict]:
    with get_db() as db:
        rows = db.execute(
            "SELECT id, name, ref, status, updated_at, last_view, "
            "(SELECT COUNT(*) FROM plans WHERE project_id=projects.id) AS n_plans, "
            "(SELECT COUNT(*) FROM options WHERE project_id=projects.id) AS n_options "
            "FROM projects ORDER BY updated_at DESC LIMIT ?", (limit,)).fetchall()
    return jsonable([dict(r) for r in rows])


def create_project(name: str, params: dict, ref: str = "", comment: str = "") -> dict:
    if not name or not name.strip():
        raise ValueError("Le nom du projet est obligatoire.")
    pid = new_id("PRJ")
    ts = now_iso()
    with get_db() as db:
        db.execute(
            "INSERT INTO projects (id, name, ref, comment, params, status, created_at, updated_at) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (pid, name.strip(), (ref or "").strip(), (comment or "").strip(),
             json.dumps(params or {}, ensure_ascii=False), "nouveau", ts, ts))
    project_dir(pid)
    write_json(project_dir(pid) / "projet.json", {"id": pid, "name": name, "params": params})
    snapshot(pid, kind="etape", label="création")
    return get_project(pid)


def get_project(pid: str) -> Optional[dict]:
    with get_db() as db:
        row = db.execute("SELECT * FROM projects WHERE id=?", (pid,)).fetchone()
    if not row:
        return None
    d = dict(row)
    d["params"] = json.loads(d.get("params") or "{}")
    return jsonable(d)


def update_project(pid: str, patch: dict) -> dict:
    cur = get_project(pid)
    if cur is None:
        raise KeyError("projet introuvable")
    params = dict(cur.get("params") or {})
    name = patch.get("name", cur["name"])
    if "params" in patch and patch["params"] is not None:
        params.update(patch["params"])
    with get_db() as db:
        db.execute(
            "UPDATE projects SET name=?, ref=?, comment=?, params=?, status=?, "
            "last_view=?, client_agreement=?, updated_at=? WHERE id=?",
            (name, patch.get("ref", cur.get("ref") or ""),
             patch.get("comment", cur.get("comment") or ""),
             json.dumps(params, ensure_ascii=False),
             patch.get("status", cur.get("status") or "nouveau"),
             patch.get("last_view", cur.get("last_view") or "dashboard"),
             int(patch.get("client_agreement", cur.get("client_agreement") or 0)),
             now_iso(), pid))
    write_json(project_dir(pid) / "projet.json", {"id": pid, "name": name, "params": params})
    return get_project(pid)


def duplicate_project(pid: str) -> dict:
    cur = get_project(pid)
    if cur is None:
        raise KeyError("projet introuvable")
    new = create_project(f"{cur['name']} (copie)", cur.get("params") or {},
                         ref=(cur.get("ref") or "") + "-copie",
                         comment="dupliqué depuis " + pid)
    src = project_dir(pid)
    dst = project_dir(new["id"])
    for sub in ("plans", "rendus", "interpretations", "options", "calculs", "livrables"):
        s = src / sub
        if s.exists():
            shutil.copytree(s, dst / sub, dirs_exist_ok=True)
    with get_db() as db:
        for tbl in ("plans", "interpretations", "options"):
            rows = db.execute(f"SELECT * FROM {tbl} WHERE project_id=?", (pid,)).fetchall()
            for r in rows:
                d = dict(r)
                d.pop("id", None)
                old_id = r["id"] if "id" in r.keys() else None
                cols = [k for k in d.keys() if k not in ("validated",)]
                ph = ",".join("?" for _ in cols)
                ins = db.execute(
                    f"INSERT INTO {tbl} ({','.join(cols)}) VALUES ({ph})",
                    tuple(new_id(_prefix_of(tbl)) if k == "id" else
                          (new["id"] if k == "project_id" else
                           (new_id(_prefix_of(tbl)) if k == old_id and old_id else d[k]))
                          for k in cols))
    return new


def _prefix_of(tbl: str) -> str:
    return {"plans": "PLN", "interpretations": "ITP", "options": "OPT",
            "deliverables": "DEL", "snapshots": "SNAP"}.get(tbl, "ID")


# ---------------------------------------------------------------------------
# Snapshots & rétention (§2.3-9, §5.10)
# ---------------------------------------------------------------------------

def snapshot(pid: str, kind: str = "etape", label: str = "", option_id: str = "") -> Optional[dict]:
    d = project_dir(pid)
    if not d.exists():
        return None
    sid = new_id("SNAP")
    zpath = d / "snapshots" / f"{sid}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for sub in ("projet.json", "plans", "rendus", "interpretations", "options",
                    "calculs", "livrables"):
            p = d / sub
            if p.is_file():
                z.write(p, sub)
            elif p.is_dir():
                for f in p.rglob("*"):
                    if f.is_file() and ".snapshots" not in f.parts:
                        z.write(f, f.relative_to(d))
    with get_db() as db:
        db.execute("INSERT INTO snapshots (id, project_id, option_id, kind, label, path, created_at) "
                   "VALUES (?,?,?,?,?,?,?)",
                   (sid, pid, option_id or None, kind, label, str(zpath), now_iso()))
    return {"id": sid, "path": str(zpath), "kind": kind, "label": label, "created_at": now_iso()}


def list_snapshots(pid: str) -> list[dict]:
    with get_db() as db:
        rows = db.execute("SELECT * FROM snapshots WHERE project_id=? ORDER BY created_at DESC",
                          (pid,)).fetchall()
    return jsonable([dict(r) for r in rows])


def restore_snapshot(pid: str, sid: str) -> bool:
    with get_db() as db:
        row = db.execute("SELECT path FROM snapshots WHERE id=? AND project_id=?",
                         (sid, pid)).fetchone()
    if not row:
        return False
    z = Path(row["path"])
    if not z.exists():
        return False
    d = project_dir(pid)
    with zipfile.ZipFile(z) as zf:
        zf.extractall(d)
    return True


def purge_old_snapshots(jours: int) -> int:
    """Job de maintenance au lancement (§5.10.2)."""
    removed = 0
    with get_db() as db:
        rows = db.execute(
            "SELECT id, project_id, path FROM snapshots WHERE "
            "created_at < datetime('now', ?) AND kind != 'figeage'",
            (f"-{int(jours)} days",)).fetchall()
        for r in rows:
            try:
                Path(r["path"]).unlink(missing_ok=True)
                db.execute("DELETE FROM snapshots WHERE id=?", (r["id"],))
                removed += 1
            except Exception as exc:
                log.warning("purge snapshot %s KO: %s", r["id"], exc)
    # temp files
    root = Path(__file__).resolve().parent.parent / "data"
    for tmp in root.rglob(".tmp-*"):
        try:
            tmp.unlink()
        except Exception:
            pass
    return removed


def delete_project(pid: str, confirm_name: str) -> bool:
    cur = get_project(pid)
    if cur is None:
        raise KeyError("projet introuvable")
    if (confirm_name or "").strip() != cur["name"].strip():
        raise PermissionError("Le nom technique saisi ne correspond pas — suppression annulée.")
    with get_db() as db:
        db.execute("DELETE FROM ai_calls WHERE project_id=?", (pid,))
        db.execute("DELETE FROM alerts WHERE project_id=?", (pid,))
        db.execute("DELETE FROM snapshots WHERE project_id=?", (pid,))
        db.execute("DELETE FROM deliverables WHERE project_id=?", (pid,))
        db.execute("DELETE FROM edits WHERE project_id=?", (pid,))
        db.execute("DELETE FROM options WHERE project_id=?", (pid,))
        db.execute("DELETE FROM interpretations WHERE project_id=?", (pid,))
        db.execute("DELETE FROM plans WHERE project_id=?", (pid,))
        db.execute("DELETE FROM projects WHERE id=?", (pid,))
    d = project_dir(pid)
    if d.exists():
        shutil.rmtree(d, ignore_errors=True)
    return True


# ---------------------------------------------------------------------------
# Journal / alertes / incidents
# ---------------------------------------------------------------------------

def log_alert(project_id: Optional[str], kind: str, detail: str, decision: str = "en_attente") -> None:
    with get_db() as db:
        db.execute("INSERT INTO alerts (datetime, project_id, kind, detail, decision) "
                   "VALUES (datetime('now'),?,?,?,?)", (project_id, kind, detail[:1000], decision))


def resolve_alert(alert_id: int, decision: str) -> None:
    with get_db() as db:
        db.execute("UPDATE alerts SET decision=? WHERE id=?", (decision, alert_id))


def list_alerts(project_id: Optional[str] = None) -> list[dict]:
    with get_db() as db:
        if project_id:
            rows = db.execute("SELECT * FROM alerts WHERE project_id=? ORDER BY id DESC",
                              (project_id,)).fetchall()
        else:
            rows = db.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 500").fetchall()
    return jsonable([dict(r) for r in rows])


def add_incident(title: str, detail: str, actions: str = "") -> dict:
    with get_db() as db:
        cur = db.execute("INSERT INTO incidents (datetime, title, detail, actions) "
                         "VALUES (datetime('now'),?,?,?)", (title, detail, actions))
        iid = cur.lastrowid
    return {"id": iid}


def list_incidents() -> list[dict]:
    with get_db() as db:
        rows = db.execute("SELECT * FROM incidents ORDER BY id DESC LIMIT 200").fetchall()
    return jsonable([dict(r) for r in rows])


def close_incident(iid: int) -> None:
    with get_db() as db:
        db.execute("UPDATE incidents SET closed=1 WHERE id=?", (iid,))


def ai_calls(project_id: Optional[str] = None, limit: int = 400) -> list[dict]:
    with get_db() as db:
        if project_id:
            rows = db.execute("SELECT * FROM ai_calls WHERE project_id=? ORDER BY id DESC LIMIT ?",
                              (project_id, limit)).fetchall()
        else:
            rows = db.execute("SELECT * FROM ai_calls ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    return jsonable([dict(r) for r in rows])
