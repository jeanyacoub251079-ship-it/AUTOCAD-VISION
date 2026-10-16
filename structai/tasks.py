"""Exécutions de fond (génération, livrables) avec progression en temps réel.

Choix : threads + registre en mémoire (mono-utilisateur local — §1.5).
"""
from __future__ import annotations

import threading
import traceback
from typing import Any, Callable

from .logging_setup import get_logger
from .util import now_iso, short_hash, new_id

log = get_logger("structai.tasks")

_LOCK = threading.Lock()
_JOBS: dict[str, dict] = {}
MAX_JOBS = 50


def start(kind: str, fn: Callable[[Callable[..., None], Callable[[], bool], dict], Any],
          meta: dict | None = None) -> str:
    jid = new_id("JOB")[:24]
    job = {"id": jid, "kind": kind, "stage": "queued", "progress": 0, "log": [],
           "done": False, "error": None, "result": None, "cancel": False,
           "started": now_iso(), "meta": meta or {}}
    with _LOCK:
        _JOBS[jid] = job
        if len(_JOBS) > MAX_JOBS:
            for k in [k for k, v in list(_JOBS.items()) if v["done"]][:10]:
                _JOBS.pop(k, None)

    def run() -> None:
        def progress(stage: str, msg: str, pct: int) -> None:
            with _LOCK:
                job["stage"] = stage
                job["progress"] = int(pct)
                job["log"].append({"t": now_iso(), "stage": stage, "msg": str(msg)[:300]})
                job["log"] = job["log"][-300:]

        def cancelled() -> bool:
            return job["cancel"]

        try:
            res = fn(progress, cancelled, meta or {})
            with _LOCK:
                job["result"] = res
                if cancelled():
                    job["stage"] = "annule"
                job["done"] = True
        except Exception as exc:
            log.error("job %s KO: %s", jid, exc)
            with _LOCK:
                job["error"] = f"{exc}"
                job["log"].append({"t": now_iso(), "stage": "erreur",
                                   "msg": traceback.format_exc(limit=2)})
                job["done"] = True

    threading.Thread(target=run, daemon=True, name=f"structai-{kind}").start()
    return jid


def status(jid: str) -> dict | None:
    with _LOCK:
        j = _JOBS.get(jid)
        if j is None:
            return None
        return {k: (list(v) if k == "log" else v) for k, v in j.items()}


def cancel(jid: str) -> bool:
    with _LOCK:
        j = _JOBS.get(jid)
        if not j:
            return False
        j["cancel"] = True
        return True
