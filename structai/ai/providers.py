"""Clients IA unifiés — FOURNEAUX EXCLUSIFS (contrainte utilisateur) :

- Anthropic — Claude Opus (vision, raisonnement, texte)
- OpenAI — ChatGPT / GPT      (vision, raisonnement, texte)

Aucun autre fournisseur n'est implémenté ni appelé (pas de Mistral, pas de
Google, pas d'exécution locale), conformément à la directive :
« en utilisant exclusivement les ressources de Claude Opus (Anthropic) ou
de ChatGPT (OpenAI) ». Les modèles restent paramétrables dans ces deux
fournisseurs uniquement.

Timeout 60 s, retry ×2 avec backoff exponentiel (§5.9.2).
"""
from __future__ import annotations

import base64
import json
import time
from dataclasses import dataclass, field
from typing import Any, Optional

from ..config import ALLOWED_PROVIDERS, PROVIDER_MODELS
from ..logging_setup import get_logger
from ..security import get_key

log = get_logger("structai.ai")


class ProviderError(Exception):
    pass


class NoKeyError(ProviderError):
    pass


@dataclass
class AIResponse:
    text: str = ""
    json: Optional[Any] = None
    tokens_in: int = 0
    tokens_out: int = 0
    provider: str = ""
    model: str = ""
    latency_s: float = 0.0
    raw: dict = field(default_factory=dict)


def list_models(purpose: str) -> dict[str, list[str]]:
    out = {}
    for prov in ALLOWED_PROVIDERS:
        out[prov] = list(PROVIDER_MODELS.get(prov, {}).get(purpose, []))
    return out


def provider_status() -> dict[str, dict]:
    st = {}
    for prov in ALLOWED_PROVIDERS:
        key = get_key(prov)
        st[prov] = {
            "label": PROVIDER_MODELS.get(prov, {}).get("label", prov),
            "cle_presente": bool(key),
            "note": ("clé dans le trousseau système" if key
                     else "clé absente — fonctions IA indisponibles (mode dégradé)"),
        }
    return st


def extract_json(text: str) -> Any:
    """Extrait le premier objet JSON d'une réponse (tolère ```json fenced)."""
    if not text:
        raise ProviderError("réponse vide")
    t = text.strip()
    if "```" in t:
        parts = t.split("```")
        for p in parts[1:]:
            p = p.strip()
            if p.startswith("json"):
                p = p[4:]
            p = p.strip()
            if p.startswith("{") or p.startswith("["):
                t = p
                break
    i = min([x for x in (t.find("{"), t.find("[")) if x >= 0] or [-1])
    if i < 0:
        raise ProviderError("aucun JSON détecté dans la réponse")
    t = t[i:]
    # détection de fin par comptage des accolades
    depth = 0
    end = None
    in_str = False
    esc = False
    for j, ch in enumerate(t):
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{[":
            depth += 1
        elif ch in "}]":
            depth -= 1
            if depth == 0:
                end = j + 1
                break
    if end is None:
        raise ProviderError("JSON tronqué dans la réponse")
    return json.loads(t[:end])


def _b64_image(image_bytes: bytes, path_hint: str = "") -> str:
    return base64.b64encode(image_bytes).decode("ascii")


def generate_vision(provider: str, model: str, image_bytes: bytes, prompt: str,
                    timeout: int = 60) -> AIResponse:
    if provider not in ALLOWED_PROVIDERS:
        raise ProviderError(f"Fournisseur « {provider} » non autorisé (seuls Anthropic "
                            "Claude Opus et OpenAI ChatGPT sont activés).")
    key = get_key(provider)
    if not key:
        raise NoKeyError(f"Clé API {provider} absente du trousseau.")
    t0 = time.time()
    b64 = _b64_image(image_bytes)
    try:
        if provider == "anthropic":
            from anthropic import Anthropic
            client = Anthropic(api_key=key, timeout=timeout, max_retries=2)
            resp = client.messages.create(
                model=model, max_tokens=8000,
                system="Tu es un ingénieur structure. Réponds UNIQUEMENT avec l'objet JSON demandé.",
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64",
                                                     "media_type": "image/png", "data": b64}},
                        {"type": "text", "text": prompt},
                    ],
                }],
            )
            text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
            tin, tout = resp.usage.input_tokens, resp.usage.output_tokens
        else:
            from openai import OpenAI
            client = OpenAI(api_key=key, timeout=timeout, max_retries=2)
            resp = client.chat.completions.create(
                model=model,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system",
                     "content": "Tu es un ingénieur structure. Réponds UNIQUEMENT avec l'objet JSON demandé."},
                    {"role": "user", "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url",
                         "image_url": {"url": f"data:image/png;base64,{b64}", "detail": "high"}},
                    ]},
                ],
                max_completion_tokens=8000,
            )
            choice = resp.choices[0]
            text = choice.message.content or ""
            tin = getattr(resp.usage, "prompt_tokens", 0) or 0
            tout = getattr(resp.usage, "completion_tokens", 0) or 0
    except (NoKeyError, ProviderError):
        raise
    except Exception as exc:
        raise ProviderError(f"{provider}/{model}: {exc}") from exc
    out = AIResponse(text=text, tokens_in=int(tin), tokens_out=int(tout),
                     provider=provider, model=model, latency_s=round(time.time() - t0, 2))
    try:
        out.json = extract_json(text)
    except Exception as exc:
        out.raw["json_parse_error"] = str(exc)
    return out


def generate_reasoning(provider: str, model: str, prompt: str, timeout: int = 90,
                       json_mode: bool = True) -> AIResponse:
    return generate_text(provider, model, prompt, timeout, json_mode=json_mode)


def generate_text(provider: str, model: str, prompt: str, timeout: int = 90,
                  system: str = "", json_mode: bool = True) -> AIResponse:
    if provider not in ALLOWED_PROVIDERS:
        raise ProviderError(f"Fournisseur « {provider} » non autorisé.")
    key = get_key(provider)
    if not key:
        raise NoKeyError(f"Clé API {provider} absente du trousseau.")
    t0 = time.time()
    sys_txt = system or ("Tu réponds en français, en JSON strict si demandé."
                         if json_mode else "Tu réponds en français.")
    try:
        if provider == "anthropic":
            from anthropic import Anthropic
            client = Anthropic(api_key=key, timeout=timeout, max_retries=2)
            resp = client.messages.create(model=model, max_tokens=6000, system=sys_txt,
                                          messages=[{"role": "user", "content": prompt}])
            text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
            tin, tout = resp.usage.input_tokens, resp.usage.output_tokens
        else:
            from openai import OpenAI
            client = OpenAI(api_key=key, timeout=timeout, max_retries=2)
            kwargs: dict[str, Any] = {
                "model": model,
                "messages": [{"role": "system", "content": sys_txt},
                             {"role": "user", "content": prompt}],
                "max_completion_tokens": 6000,
            }
            if json_mode:
                kwargs["response_format"] = {"type": "json_object"}
            resp = client.chat.completions.create(**kwargs)
            text = resp.choices[0].message.content or ""
            tin = getattr(resp.usage, "prompt_tokens", 0) or 0
            tout = getattr(resp.usage, "completion_tokens", 0) or 0
    except (NoKeyError, ProviderError):
        raise
    except Exception as exc:
        raise ProviderError(f"{provider}/{model}: {exc}") from exc
    out = AIResponse(text=text, tokens_in=int(tin), tokens_out=int(tout),
                     provider=provider, model=model, latency_s=round(time.time() - t0, 2))
    if json_mode:
        try:
            out.json = extract_json(text)
        except Exception as exc:
            out.raw["json_parse_error"] = str(exc)
    return out


def estimate_cost(settings: dict, provider: str, model: str, tokens_in: int,
                  tokens_out: int) -> float:
    pricing = settings.get("pricing_usd_per_mtok", {}) or {}
    p = pricing.get(model) or {}
    usd = (tokens_in / 1e6) * float(p.get("in", 0)) + (tokens_out / 1e6) * float(p.get("out", 0))
    return round(usd, 5)
