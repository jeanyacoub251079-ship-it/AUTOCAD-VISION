"""Journalisation locale (Lot 0 — §6.2).

Aucun secret ne doit transiter par les logs : le filtre ci-dessous masque
les valeurs associées aux clés API si un appelant les logge par erreur.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

from .config import LOGS_DIR, ensure_dirs

try:
    from loguru import logger as _loguru
    HAS_LOGURU = True
except Exception:  # pragma: no cover
    _loguru = None
    HAS_LOGURU = False

_SENSITIVE_KEYS = ("api_key", "apikey", "sk-", "token", "password", "mot_de_passe")


def _mask(text: str) -> str:
    out = text
    for needle in _SENSITIVE_KEYS:
        if needle in out:
            out = out.replace(needle, "***")
    return out


class _MaskingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:  # noqa: D102
        try:
            record.msg = _mask(str(record.msg))
        except Exception:
            pass
        return True


def setup_logging() -> None:
    ensure_dirs()
    fmt = "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s"
    handlers: list[logging.Handler] = []
    file_handler = logging.FileHandler(LOGS_DIR / "structai.log", encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(fmt))
    file_handler.addFilter(_MaskingFilter())
    handlers.append(file_handler)
    stream = logging.StreamHandler(sys.stderr)
    stream.setFormatter(logging.Formatter(fmt))
    stream.addFilter(_MaskingFilter())
    handlers.append(stream)

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    for h in list(root.handlers):
        root.removeHandler(h)
    for h in handlers:
        root.addHandler(h)

    if HAS_LOGURU:
        _loguru.remove()
        _loguru.add(
            str(LOGS_DIR / "structai-{time:YYYYMMDD}.log"),
            level="INFO",
            rotation="20 MB",
            retention="30 days",
            enqueue=True,
            filter=lambda r: not r["message"].__contains__("sk-"),
        )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
