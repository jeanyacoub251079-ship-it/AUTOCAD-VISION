"""Utilitaires transverses : hachages, identifiants, dates, écritures atomiques."""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def now_compact() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def canonical_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def short_hash(hexa: str, n: int = 8) -> str:
    return hexa[:n] if hexa else ""


def new_id(prefix: str) -> str:
    """Identifiant technique lisible et triable : PRJ-20261016T095200Z-A3F1."""
    rnd = os.urandom(2).hex().upper()
    return f"{prefix}-{now_compact()}-{rnd}"


_ID_RE = re.compile(r"^[A-Z]{3,4}-\d{8}T\d{6}Z-[0-9A-F]{4}$")


def is_valid_id(value: str) -> bool:
    return bool(_ID_RE.match(value or ""))


def slugify(text: str, max_len: int = 48) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip("-")
    return text[:max_len] or "projet"


def atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=".tmp-")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def write_json(path: Path, obj: Any) -> None:
    atomic_write_bytes(path, json.dumps(obj, ensure_ascii=False, indent=2).encode("utf-8"))


def read_json(path: Path, default: Any = None) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def human_size(n: float) -> str:
    for unit in ("o", "Ko", "Mo", "Go"):
        if abs(n) < 1024 or unit == "Go":
            return f"{n:.1f} {unit}" if unit != "o" else f"{int(n)} o"
        n /= 1024.0
    return f"{n:.1f} Go"


def safe_filename(name: str) -> str:
    """Nom de fichier assaini (aucune donnée identifiante ne doit transiter)."""
    return slugify(name, 80)


def jsonable(obj: Any) -> Any:
    """Rend un objet 100 % sérialisable JSON (numpy, sets, tuples…)."""
    import json as _json
    import math
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [jsonable(v) for v in obj]
    if isinstance(obj, set):
        return sorted(jsonable(v) for v in obj)
    if isinstance(obj, bool) or obj is None or isinstance(obj, str):
        return obj
    try:
        import numpy as _np
        if isinstance(obj, (_np.floating, _np.integer)):
            obj = obj.item()
    except Exception:
        pass
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return round(obj, 6)
    if isinstance(obj, int):
        return obj
    try:
        _json.dumps(obj)
        return obj
    except Exception:
        return str(obj)
