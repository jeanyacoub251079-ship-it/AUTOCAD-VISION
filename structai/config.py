"""Configuration : chemins, paramètres par défaut, settings persistés.

Les clés API ne vivent JAMAIS ici (trousseau système via structai.security).
Le fichier settings.json ne contient que des préférences non sensibles.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .util import read_json, write_json

APP_TITLE = "StructAI — Conception structurelle assistée par IA"

# ---------------------------------------------------------------------------
# Répertoires
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = Path(os.environ.get("STRUCTAI_DATA", str(REPO_ROOT / "data")))
PROJECTS_DIR = DATA_DIR / "projects"
LOGS_DIR = DATA_DIR / "logs"
EXPORT_DIR = DATA_DIR / "exports"
DB_PATH = DATA_DIR / "structai.sqlite3"
SETTINGS_PATH = DATA_DIR / "settings.json"
PROMPTS_DIR = Path(__file__).resolve().parent / "ai" / "prompts"

WEB_DIST = REPO_ROOT / "web" / "dist"

# Limites (cahier des charges §3.4 / §1.4)
MAX_DXF_SIZE = 100 * 1024 * 1024  # 100 Mo
SUPPORTED_DXF_VERSIONS = {"AC1009", "AC1012", "AC1014", "AC1015", "AC1018", "AC1021", "AC1024", "AC1027", "AC1032", "AC1035", "AC1036"}
ENTITY_WARN_THRESHOLD = 500_000

# ---------------------------------------------------------------------------
# Fournisseurs IA — CONTRAINTE UTILISATEUR : exclusivement Anthropic Claude
# Opus et OpenAI (ChatGPT/GPT). Aucun autre fournisseur n'est proposé.
# ---------------------------------------------------------------------------
ALLOWED_PROVIDERS = ("anthropic", "openai")

PROVIDER_MODELS: dict[str, dict[str, list[str]]] = {
    "anthropic": {
        "vision": ["claude-opus-4-1", "claude-opus-4-20250514", "claude-opus-4-5"],
        "reasoning": ["claude-opus-4-1", "claude-opus-4-5"],
        "text": ["claude-opus-4-1", "claude-opus-4-5"],
        "label": "Anthropic — Claude Opus",
    },
    "openai": {
        "vision": ["gpt-4o", "gpt-4.1", "gpt-5"],
        "reasoning": ["gpt-5", "o3", "gpt-4.1"],
        "text": ["gpt-4o", "gpt-5"],
        "label": "OpenAI — ChatGPT / GPT",
    },
}

# Tarifs indicatifs USD / million de tokens (à vérifier/ajuster dans les
# paramètres ; utilisés uniquement pour ESTIMER le coût des appels).
DEFAULT_PRICING_USD_PER_MTOK: dict[str, dict[str, float]] = {
    "claude-opus-4-1": {"in": 15.0, "out": 75.0},
    "claude-opus-4-5": {"in": 15.0, "out": 75.0},
    "claude-opus-4-20250514": {"in": 15.0, "out": 75.0},
    "gpt-4o": {"in": 2.5, "out": 10.0},
    "gpt-4.1": {"in": 2.0, "out": 8.0},
    "gpt-5": {"in": 1.25, "out": 10.0},
    "o3": {"in": 2.0, "out": 8.0},
}

# ---------------------------------------------------------------------------
# Paramètres applicatifs par défaut (modifiables via l'écran Paramètres)
# ---------------------------------------------------------------------------
DEFAULT_SETTINGS: dict[str, Any] = {
    "ui": {"langue": "fr"},
    "ia": {
        "fournisseur_vision": "anthropic",
        "modele_vision": "claude-opus-4-1",
        "fournisseur_raisonnement": "anthropic",
        "modele_raisonnement": "claude-opus-4-1",
        "fournisseur_texte": "openai",
        "modele_texte": "gpt-4o",
        "plafond_usd_projet": 5.0,
        "plafond_usd_jour": 10.0,
        "mode_paranoiaque": False,   # bloque tout envoi IA sans confirmation explicite
        "timeout_s": 60,
        "max_retries": 2,
        "exiger_zero_retention": True,   # vérifie les options contractuelles déclarées
        "zero_data_retention": {"anthropic": True, "openai": True},
        "no_training": {"anthropic": True, "openai": True},
        "pricing_usd_per_mtok": dict(DEFAULT_PRICING_USD_PER_MTOK),
        "fallback_fournisseur": True,
    },
    "securite": {
        "mot_de_passe_hash": "",       # sha256(salt$mdp) — vide = pas de verrou local
        "mot_de_passe_salt": "",
        "session_expiration_min": 30,
        "journal_acces_local": True,
    },
    "projet_defauts": {
        "nb_options": 5,
        "critereme_classement": "simplicite_mise_en_oeuvre",
        "hauteur_etage": 2.80,
        "materiau": "beton_arme",
        "classe_exposition": "XC1",
        "duree_utilisation": 50,
        "categorie_importance": "II",
        "q_comportement": 3.0,
    },
    "generation": {
        "max_options_calculees": 40,     # budget calcul complet par projet
        "portee_min_m": 3.2,
        "portee_max_m": 6.5,
        "epaisseurs_dalle_m": [0.16, 0.18, 0.20, 0.22, 0.25],
        "activer_ia_creative_par_defaut": False,
    },
    "retention": {
        "snapshots_jours": 90,
        "journaux_compression_mois": 12,
        "journaux_conservation_annees": 3,
    },
    "normes": {
        "ec0": True, "ec1": True, "ec2": True, "ec8": True, "ec6": False, "ec7": False, "ec3": False,
        "qsol_kpa": 250.0,
        "note": "Valeurs par défaut indicatives — à vérifier contre les annexes nationales en vigueur (NF EN 199x-x/NA).",
    },
}


def ensure_dirs() -> None:
    for d in (DATA_DIR, PROJECTS_DIR, LOGS_DIR, EXPORT_DIR):
        d.mkdir(parents=True, exist_ok=True)


def load_settings() -> dict[str, Any]:
    stored = read_json(SETTINGS_PATH, default={}) or {}
    return _deep_merge(DEFAULT_SETTINGS, stored)


def save_settings(settings: dict[str, Any]) -> None:
    write_json(SETTINGS_PATH, settings)


def update_settings(patch: dict[str, Any]) -> dict[str, Any]:
    settings = load_settings()
    merged = _deep_merge(settings, patch)
    save_settings(merged)
    return merged


def reset_settings() -> dict[str, Any]:
    save_settings({})
    return load_settings()


def _deep_merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def project_dir(project_id: str) -> Path:
    p = PROJECTS_DIR / project_id
    (p / "plans").mkdir(parents=True, exist_ok=True)
    (p / "rendus").mkdir(parents=True, exist_ok=True)
    (p / "interpretations").mkdir(parents=True, exist_ok=True)
    (p / "options").mkdir(parents=True, exist_ok=True)
    (p / "calculs").mkdir(parents=True, exist_ok=True)
    (p / "livrables").mkdir(parents=True, exist_ok=True)
    (p / "snapshots").mkdir(parents=True, exist_ok=True)
    return p
