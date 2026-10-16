"""Orchestrateur IA (§2.4.5, §5.9) — Anthropic Claude Opus / OpenAI uniquement.

Responsabilités :
- prompts versionnés YAML ;
- estimation de coût AVANT appel ; plafonds par projet et par jour ;
- vérification configuration « zero retention / no training » ;
- mode paranoïaque (confirmation explicite requise ailleurs) ;
- retry (SDK côté) + bascule fournisseur alternatif + mode dégradé ;
- validation jsonschema de la réponse ;
- journalisation `ai_calls` (hash req/resp, tokens, coût — JAMAIS le contenu).
"""
from __future__ import annotations

import datetime as _dt
import json
from pathlib import Path
from typing import Any, Optional

import yaml
from jsonschema import Draft7Validator

from ..config import ALLOWED_PROVIDERS, PROMPTS_DIR, load_settings
from ..logging_setup import get_logger
from ..util import sha256_bytes, sha256_text
from . import providers
from .providers import ProviderError, NoKeyError
from .schemas import INTERPRETATION_SCHEMA

log = get_logger("structai.ai.orchestrator")


def list_prompts() -> list[dict]:
    out = []
    for p in sorted(PROMPTS_DIR.glob("*.yaml")):
        try:
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            out.append({"fichier": p.name, "name": data.get("name"),
                        "version": data.get("version"), "date": data.get("date"),
                        "usage": data.get("usage")})
        except Exception as exc:
            out.append({"fichier": p.name, "erreur": str(exc)})
    return out


def load_prompt(name: str) -> dict:
    files = sorted(PROMPTS_DIR.glob(f"{name}*.yaml"))
    if not files:
        raise FileNotFoundError(f"prompt introuvable : {name}")
    chosen = files[-1]  # version la plus récente (nommage vN)
    return yaml.safe_load(chosen.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Budgets / plafonds (§1.4, §2.4.5)
# ---------------------------------------------------------------------------

def budget_status(project_id: Optional[str] = None) -> dict:
    from ..db import get_db
    s = load_settings()["ia"]
    today = _dt.date.today().isoformat()
    with get_db() as db:
        q_day = db.execute("SELECT COALESCE(SUM(cost_usd),0) c, COUNT(*) n FROM ai_calls "
                           "WHERE substr(datetime,1,10)=?", (today,)).fetchone()
        if project_id:
            q_prj = db.execute("SELECT COALESCE(SUM(cost_usd),0) c, COUNT(*) n FROM ai_calls "
                               "WHERE project_id=?", (project_id,)).fetchone()
        else:
            q_prj = (0, 0)
    return {
        "jour_usd": round(q_day["c"] if hasattr(q_day, "keys") else q_day[0], 4),
        "jour_calls": int(q_day[1] if hasattr(q_day, "keys") else q_day[1]),
        "projet_usd": round(q_prj[0] if hasattr(q_prj, "keys") else q_prj[0], 4),
        "projet_calls": int(q_prj[1] if hasattr(q_prj, "keys") else q_prj[1]),
        "plafond_jour_usd": float(s.get("plafond_usd_jour", 10.0)),
        "plafond_projet_usd": float(s.get("plafond_usd_projet", 5.0)),
    }


def _budget_check(est_cost: float, project_id: Optional[str]) -> Optional[str]:
    if est_cost <= 0:
        return None
    b = budget_status(project_id)
    if b["jour_usd"] + est_cost > b["plafond_jour_usd"]:
        return (f"Plafond journal dépassé ({b['jour_usd']:.3f} + {est_cost:.3f} > "
                f"{b['plafond_jour_usd']:.3f} USD). Réessayez demain ou augmentez le plafond.")
    if project_id and b["projet_usd"] + est_cost > b["plafond_projet_usd"]:
        return (f"Plafond projet dépassé ({b['projet_usd']:.3f} + {est_cost:.3f} > "
                f"{b['plafond_projet_usd']:.3f} USD).")
    return None


# ---------------------------------------------------------------------------
# Journal
# ---------------------------------------------------------------------------

def _journal(project_id: Optional[str], provider: str, model: str, purpose: str,
              tokens_in: int, tokens_out: int, cost: float, hreq: str, hresp: str,
              status: str, latency: float, size_req: int, detail: str = "") -> None:
    try:
        from ..db import get_db
        with get_db() as db:
            db.execute(
                """INSERT INTO ai_calls (datetime, project_id, provider, model, purpose,
                        tokens_in, tokens_out, cost_usd, hash_req, hash_resp, size_req,
                        status, latency_s, detail)
                   VALUES (datetime('now'),?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (project_id, provider, model, purpose, tokens_in, tokens_out, cost,
                 hreq, hresp, size_req, status, latency, detail[:500]),
            )
    except Exception as exc:
        log.warning("journal ai_calls KO: %s", exc)


# ---------------------------------------------------------------------------
# Exécution
# ---------------------------------------------------------------------------

def _config_ok_for_call(settings: dict, provider: str) -> Optional[str]:
    ia = settings.get("ia", {})
    if ia.get("exiger_zero_retention", True):
        if not ia.get("zero_data_retention", {}).get(provider, False):
            return (f"L'option « zero data retention » n'est pas déclarée active pour "
                    f"{provider}. Réactivation requise dans Paramètres → IA.")
        if not ia.get("no_training", {}).get(provider, False):
            return (f"L'option « no training » n'est pas déclarée active pour {provider}.")
    return None


def estimate_call(provider: str, model: str, image_bytes: bytes, prompt_text: str) -> dict:
    """Estimation grossière : 1 token ≈ 4 car; image PNG ≈ (largeur/750)·1100 tokens."""
    s = load_settings()["ia"]
    approx_in = int(len(prompt_text) / 4) + (len(image_bytes) // 1500 if image_bytes else 0) + 900
    approx_out = 1600
    cost = providers.estimate_cost(s, provider, model, approx_in, approx_out)
    return {"tokens_in_est": approx_in, "tokens_out_est": approx_out,
            "cout_estime_usd": cost, "model": model, "provider": provider,
            "note": "estimation indicative ; le coût réel est journalisé après appel"}


def call_ai(purpose: str, project_id: Optional[str], *, provider: Optional[str] = None,
            model: Optional[str] = None, image_path: Optional[Path] = None,
            prompt_vars: Optional[dict] = None, schema: Optional[dict] = None,
            prompt_name: str = "interpret_plan", expect_json: bool = True,
            user_confirmed: bool = True) -> dict:
    """Point d'entrée unique de tout appel IA. Retourne un dict d'exécution."""
    settings = load_settings()
    ia = settings.get("ia", {})
    if ia.get("mode_paranoiaque") and not user_confirmed:
        _journal(project_id, "-", "-", purpose, 0, 0, 0, "", "", "bloque", 0, 0,
                 "mode paranoïaque : confirmation explicite requise")
        return {"ok": False, "error": "Mode paranoïaque actif : confirmation explicite requise "
                "pour tout envoi.", "code": "paranoid"}

    prompt = load_prompt(prompt_name)
    text_prompt = prompt["prompt"]
    system = prompt.get("systeme", "")
    for k, v in (prompt_vars or {}).items():
        text_prompt = text_prompt.replace("{" + k + "}", v if isinstance(v, str) else json.dumps(v, ensure_ascii=False, indent=1))
    prompt_full = text_prompt
    if system:
        prompt_full = system + "\n\n---\n\n" + text_prompt

    providers_order: list[tuple[str, str]] = []
    prov_map = {"interpretation": ("fournisseur_vision", "modele_vision"),
                "generation": ("fournisseur_raisonnement", "modele_raisonnement"),
                "redaction": ("fournisseur_texte", "modele_texte")}
    keyp, keym = prov_map.get(purpose.split("_")[0], ("fournisseur_raisonnement", "modele_raisonnement"))
    start_provider = provider or ia.get(keyp, "anthropic")
    start_model = model or ia.get(keym, "")
    providers_order.append((start_provider, start_model))
    if ia.get("fallback_fournisseur", True):
        for alt in ALLOWED_PROVIDERS:
            if alt != start_provider:
                providers_order.append((alt, (ia.get(keym) if alt == start_provider
                                             else providers.list_models(
                                                 "vision" if purpose.startswith("interpret")
                                                 else "text").get(alt, [""])[0]) or ""))
    img_bytes = image_path.read_bytes() if image_path else b""

    err_msg = None
    for provider_i, (prov, mdl) in enumerate(providers_order):
        if prov not in ALLOWED_PROVIDERS:
            err_msg = f"Fournisseur « {prov} » non autorisé (Claude Opus / ChatGPT exclusivement)."
            continue
        cfg_err = _config_ok_for_call(settings, prov)
        if cfg_err:
            return {"ok": False, "error": cfg_err, "code": "config"}
        est = estimate_call(prov, mdl, img_bytes, prompt_full)
        blocked = _budget_check(est["cout_estime_usd"], project_id)
        if blocked:
            _journal(project_id, prov, mdl, purpose, 0, 0, 0,
                     sha256_text(prompt_full)[:16] if not img_bytes else sha256_bytes(img_bytes)[:16],
                     "", "bloque", 0, len(prompt_full), "plafond")
            return {"ok": False, "error": blocked, "code": "budget"}
        hreq = sha256_text(prompt_full) if not img_bytes else sha256_bytes(img_bytes + prompt_full.encode())
        try:
            if img_bytes:
                resp = providers.generate_vision(prov, mdl, img_bytes, prompt_full,
                                                  timeout=int(ia.get("timeout_s", 60)))
            else:
                resp = providers.generate_text(prov, mdl, prompt_full,
                                                timeout=int(ia.get("timeout_s", 60)) + 30,
                                                system="", json_mode=expect_json)
        except NoKeyError as exc:
            err_msg = str(exc)
            _journal(project_id, prov, mdl, purpose, 0, 0, 0, hreq[:16], "", "echec", 0,
                     len(prompt_full), "cle absente")
            continue
        except ProviderError as exc:
            err_msg = str(exc)
            _journal(project_id, prov, mdl, purpose, 0, 0, 0, hreq[:16], "", "echec", 0,
                     len(prompt_full), str(exc)[:200])
            continue
        cost = providers.estimate_cost(ia, resp.provider, resp.model, resp.tokens_in, resp.tokens_out)
        payload_json = None
        status = "succes"
        errors: list[str] = []
        if expect_json:
            payload_json = resp.json
            if payload_json is None:
                errors.append("JSON illisible dans la réponse")
                status = "retry"
            elif schema:
                v = Draft7Validator(schema)
                errs = sorted(v.iter_errors(payload_json), key=lambda e: e.path)
                if errs:
                    errors = [f"{'/'.join(map(str, e.path)) or '<racine>'}: {e.message}"
                              for e in errs[:12]]
                    status = "retry"
        hresp = sha256_text(resp.text)
        _journal(project_id, resp.provider, resp.model, purpose, resp.tokens_in,
                 resp.tokens_out, cost, hreq[:16], hresp[:16], status, resp.latency_s,
                 len(prompt_full) + len(img_bytes), "; ".join(errors)[:400])
        if status == "retry" and provider_i + 1 < len(providers_order):
            log.info("Réponse invalide de %s/%s — bascule fournisseur %s.",
                     resp.provider, resp.model, providers_order[provider_i + 1][0])
            continue
        return {"ok": status == "succes", "data": payload_json if expect_json else resp.text,
                "raw_text": resp.text, "provider": resp.provider, "model": resp.model,
                "tokens_in": resp.tokens_in, "tokens_out": resp.tokens_out,
                "cost_usd": cost, "latency_s": resp.latency_s,
                "schema_errors": errors, "estimation": est,
                "hash_req": hreq, "hash_resp": hresp,
                "erreur": ("; ".join(errors) if errors else None)}
    return {"ok": False, "error": err_msg or "Tous les fournisseurs sont indisponibles — "
            "mode dégradé : utilisez la saisie manuelle.", "code": "unavailable"}


def interpret_plan_call(project_id: str, image_path: Path, provider: Optional[str],
                        model: Optional[str], user_confirmed: bool) -> dict:
    return call_ai("interpretation_plan", project_id, provider=provider, model=model,
                   image_path=image_path, prompt_name="interpret_plan",
                   schema=INTERPRETATION_SCHEMA, user_confirmed=user_confirmed)


def creative_variants_call(project_id: str, interpretation: dict, contraintes: dict,
                           provider: Optional[str], model: Optional[str]) -> dict:
    return call_ai("generation_creative", project_id, provider=provider, model=model,
                   prompt_name="creative_generation",
                   prompt_vars={"interpretation_json": json.dumps(interpretation, ensure_ascii=False),
                                "contraintes": json.dumps(contraintes, ensure_ascii=False)},
                   schema={"type": "object", "required": ["variantes"],
                           "properties": {"variantes": {"type": "array",
                                                        "items": {"type": "object",
                                                                  "required": ["titre", "portee"]}}}},
                   user_confirmed=True)


def drafting_call(project_id: str, donnees: dict, provider: Optional[str],
                   model: Optional[str]) -> dict:
    return call_ai("redaction_note", project_id, provider=provider, model=model,
                   prompt_name="note_redaction",
                   prompt_vars={"donnees_json": json.dumps(donnees, ensure_ascii=False)},
                   schema={"type": "object",
                           "required": ["presentation_projet", "justification_choix",
                                        "synthese_conclusion"]},
                   user_confirmed=True)
