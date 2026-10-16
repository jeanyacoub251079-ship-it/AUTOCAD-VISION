"""Sécurité locale (§5.8) : secrets dans le trousseau système, mot de passe
d'application, sessions avec expiration, registre d'accès.

Conformité à l'exigence : les clés API sont stockées via `keyring`
(trousseau système) — jamais dans le code, jamais en clair dans les logs.
En environnement sans trousseau (CI, conteneur), un repli fichier 0600 avec
avertissement explicite est utilisé (mode dégradé assumé pour usage perso).
"""
from __future__ import annotations

import hashlib
import hmac
import logging
import os
import secrets
import time
from typing import Optional

from .config import DATA_DIR, load_settings

log = logging.getLogger("structai.security")

try:
    import keyring as _keyring
    HAS_KEYRING_BACKEND = None  # déterminé au premier usage
except Exception:  # pragma: no cover
    _keyring = None
    HAS_KEYRING_BACKEND = False

SERVICE = "StructAI"
_SECRETS_FILE = DATA_DIR / ".secrets.json"

# ---------------------------------------------------------------------------
# Stockage des clés API
# ---------------------------------------------------------------------------

_store_cache: dict[str, str] = {}


def _keyring_available() -> bool:
    global HAS_KEYRING_BACKEND
    if HAS_KEYRING_BACKEND is None:
        try:
            _store_cache["__probe__"] = "x"
            ok = _keyring_get("__probe__") == "x"
            _keyring_delete("__probe__")
            HAS_KEYRING_BACKEND = ok
        except Exception:
            HAS_KEYRING_BACKEND = False
    return HAS_KEYRING_BACKEND


def _keyring_get(name: str) -> Optional[str]:
    try:
        return _keyring.get_password(SERVICE, name)
    except Exception:
        return None


def _keyring_set(name: str, value: str) -> None:
    _keyring.set_password(SERVICE, name, value)


def _keyring_delete(name: str) -> None:
    try:
        _keyring.delete_password(SERVICE, name)
    except Exception:
        pass


def _file_get(name: str) -> Optional[str]:
    if name in _store_cache:
        return _store_cache[name]
    from .util import read_json
    data = read_json(_SECRETS_FILE, default={}) or {}
    _store_cache.update(data)
    return data.get(name)


def _file_set(name: str, value: str) -> None:
    from .util import read_json
    data = read_json(_SECRETS_FILE, default={}) or {}
    data[name] = value
    _store_cache[name] = value
    _SECRETS_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = _SECRETS_FILE.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        import json as _json
        _json.dump(data, f)
    os.replace(tmp, _SECRETS_FILE)
    os.chmod(_SECRETS_FILE, 0o600)


def store_key(provider: str, api_key: str) -> str:
    """Retourne le mode de stockage effectif ('keyring' | 'fichier-local')."""
    name = f"api_key:{provider}"
    if _keyring_available():
        _keyring_set(name, api_key)
        return "keyring"
    log.warning("Trousseau système indisponible — stockage fichier local 0600 (mode dégradé).")
    _file_set(name, api_key)
    return "fichier-local"


def get_key(provider: str) -> Optional[str]:
    name = f"api_key:{provider}"
    if _keyring_available():
        val = _keyring_get(name)
        if val:
            return val
    return _file_get(name)


def delete_key(provider: str) -> None:
    name = f"api_key:{provider}"
    _keyring_delete(name)
    _store_cache.pop(name, None)
    from .util import read_json
    data = read_json(_SECRETS_FILE, default={}) or {}
    if name in data:
        data.pop(name, None)
        from .util import write_json
        write_json(_SECRETS_FILE, data)


def has_key(provider: str) -> bool:
    return bool(get_key(provider))


# ---------------------------------------------------------------------------
# Mot de passe local + sessions (§5.8.4)
# ---------------------------------------------------------------------------

def set_app_password(plain: str) -> None:
    from .config import update_settings
    salt = secrets.token_hex(16)
    digest = hashlib.sha256(f"{salt}${plain}".encode("utf-8")).hexdigest()
    update_settings({"securite": {"mot_de_passe_salt": salt, "mot_de_passe_hash": digest}})


def clear_app_password() -> None:
    from .config import update_settings
    update_settings({"securite": {"mot_de_passe_hash": "", "mot_de_passe_salt": ""}})


def password_required() -> bool:
    s = load_settings().get("securite", {})
    return bool(s.get("mot_de_passe_hash"))


def check_password(plain: str) -> bool:
    s = load_settings().get("securite", {})
    salt, stored = s.get("mot_de_passe_salt", ""), s.get("mot_de_passe_hash", "")
    if not stored:
        return True
    digest = hashlib.sha256(f"{salt}${plain}".encode("utf-8")).hexdigest()
    return hmac.compare_digest(digest, stored)


class SessionStore:
    """Tokens en mémoire ; expiration après inactivité (§5.8.4)."""

    def __init__(self) -> None:
        self._tokens: dict[str, float] = {}

    def _ttl(self) -> float:
        mins = float(load_settings().get("securite", {}).get("session_expiration_min", 30) or 30)
        return mins * 60.0

    def issue(self) -> str:
        tok = secrets.token_urlsafe(32)
        self._tokens[tok] = time.time()
        return tok

    def validate(self, tok: Optional[str]) -> bool:
        if not tok:
            return False
        last = self._tokens.get(tok)
        if last is None:
            return False
        if time.time() - last > self._ttl():
            self._tokens.pop(tok, None)
            return False
        self._tokens[tok] = time.time()  # glissant
        return True

    def revoke(self, tok: Optional[str]) -> None:
        if tok:
            self._tokens.pop(tok, None)

    def purge_expired(self) -> None:
        ttl = self._ttl()
        now = time.time()
        for t, last in list(self._tokens.items()):
            if now - last > ttl:
                self._tokens.pop(t, None)


sessions = SessionStore()


def verify_session_signature_placeholder() -> None:  # pragma: no cover
    """Point d'extension éventuel (clé de signature de cookie)."""


# ---------------------------------------------------------------------------
# Registre d'accès local optionnel (§5.6.3)
# ---------------------------------------------------------------------------

def log_local_access(kind: str, detail: str = "") -> None:
    if not load_settings().get("securite", {}).get("journal_acces_local", True):
        return
    try:
        from .db import get_db
        with get_db() as db:
            db.execute(
                "INSERT INTO access_log (datetime, kind, detail) VALUES (datetime('now'), ?, ?)",
                (kind, detail[:500]),
            )
    except Exception as exc:  # ne jamais casser un flux pour un log
        log.debug("journal accès ignoré: %s", exc)
