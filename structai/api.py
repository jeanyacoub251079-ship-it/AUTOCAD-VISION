"""Routes FastAPI locales (§2.4.2).

Tout est servi sur localhost ; l'app n'écoute jamais le réseau (bind 127.0.1
recommandé — le sandbox de démo autorise 0.0.0.0 pour la prévisualisation).
Les routes /api/* sont protégées par la session locale si un mot de passe est
défini (§5.8.4). /api/ping reste ouvert (test de démarrage Lot 0).
"""
from __future__ import annotations

import json
import shutil
import time
from pathlib import Path
from typing import Any, Optional

from fastapi import (Body, Depends, File, Header, HTTPException, Request,
                     UploadFile, status)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from . import __version__, tasks
from .calc.engine import analyze_option
from .config import (ALLOWED_PROVIDERS, DB_PATH, MAX_DXF_SIZE, PROJECTS_DIR,
                     WEB_DIST, load_settings, project_dir, update_settings)
from .db import db_integrity_ok, get_db
from .logging_setup import get_logger
from .parsing import dxf as dxfparse
from .projects import (add_incident, ai_calls, close_incident, create_project,
                       delete_project, duplicate_project, get_project,
                       list_alerts, list_incidents, list_projects, list_snapshots, log_alert,
                       purge_old_snapshots, resolve_alert, restore_snapshot,
                       snapshot, update_project)
from .security import (check_password, clear_app_password, delete_key,
                       get_key, has_key, log_local_access, password_required,
                       sessions, set_app_password, store_key)
from .util import (human_size, jsonable, new_id, now_iso, read_json, safe_filename,
                   sha256_bytes, sha256_file, sha256_text, write_json, atomic_write_bytes)
from .visu import render_option_iso_svg, render_option_png

log = get_logger("structai.api")
from fastapi import APIRouter

app = None  # créée par create_app()

OPEN_PATHS = {"/api/ping", "/api/session/login", "/api/session/status"}


def create_app():
    from fastapi import FastAPI
    application = FastAPI(title="StructAI", version=__version__,
                          docs_url="/api/docs", openapi_url="/api/openapi.json")
    application.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_credentials=True,
        allow_methods=["*"], allow_headers=["*"])

    @application.middleware("http")
    async def auth_middleware(request: Request, call_next):
        path = request.url.path
        if (path.startswith("/api") and path not in OPEN_PATHS
                and password_required()):
            tok = request.headers.get("X-StructAI-Token") or request.cookies.get("structai_session")
            if not sessions.validate(tok):
                return JSONResponse({"detail": "session expirée ou absente"}, status_code=401)
        return await call_next(request)

    _register_routes(application)
    return application


# ===========================================================================
def _register_routes(app):

    # ---------------------------------------------------------------- session
    @app.post("/api/session/login")
    def login(body: dict = Body(...)):
        pwd = str(body.get("password", ""))
        if not password_required():
            return {"ok": True, "token": None, "note": "pas de mot de passe configuré"}
        if not check_password(pwd):
            time.sleep(0.6)  # dissuasion brute-force minimale
            raise HTTPException(401, "Mot de passe incorrect.")
        tok = sessions.issue()
        log_local_access("connexion", "session ouverte")
        return {"ok": True, "token": tok}

    @app.post("/api/session/logout")
    def logout(request: Request):
        sessions.revoke(request.headers.get("X-StructAI-Token")
                        or request.cookies.get("structai_session"))
        return {"ok": True}

    @app.get("/api/session/status")
    def session_status():
        return {"required": password_required()}

    # ------------------------------------------------------------------ divers
    @app.get("/api/ping")
    def ping():
        return {"ok": True, "app": "StructAI", "version": __version__,
                "time": now_iso(), "backend": "connecté"}

    @app.get("/api/status")
    def status_all():
        from .ai.providers import provider_status
        from .ai.orchestrator import budget_status, list_prompts
        s = load_settings()
        provs = provider_status()
        ok, msg = db_integrity_ok()
        ia = s.get("ia", {})
        return jsonable({
            "version": __version__,
            "db": {"path": str(DB_PATH), "integrity": ok, "note": msg if not ok else "ok"},
            "providers": provs,
            "ia_disponible": any(p["cle_presente"] for p in provs.values()),
            "mode_paranoiaque": bool(ia.get("mode_paranoiaque")),
            "budget": budget_status(),
            "prompts": [p.get("fichier") for p in list_prompts()],
            "data_dir": str(DB_PATH.parent),
        })

    # ---------------------------------------------------------------- settings
    @app.get("/api/settings")
    def settings_get():
        s = jsonable(load_settings())
        s.pop("securite", {k: "***" for k in s.get("securite", {}) if "hash" in k or "salt" in k})
        s["securite"] = {"mot_de_passe_actif": bool(password_required()),
                         "session_expiration_min": load_settings()["securite"].get("session_expiration_min", 30),
                         "journal_acces_local": load_settings()["securite"].get("journal_acces_local", True)}
        return s

    @app.put("/api/settings")
    def settings_put(body: dict = Body(...)):
        patch = dict(body or {})
        sec = patch.get("securite") or {}
        if "mot_de_passe_nouveau" in sec:
            pwd = sec.pop("mot_de_passe_nouveau")
            if pwd:
                set_app_password(str(pwd))
            else:
                clear_app_password()
        patch["securite"] = sec
        # interdiction d'écrire des clés API en clair dans les settings
        for prov in list(patch.get("ia", {}).keys()):
            if "key" in prov.lower() or "cle" in prov.lower():
                raise HTTPException(400, "Les clés API se gèrent via /api/keys (trousseau).")
        ia = patch.get("ia") or {}
        for f in ("fournisseur_vision", "fournisseur_raisonnement", "fournisseur_texte"):
            if ia.get(f) and ia[f] not in ALLOWED_PROVIDERS:
                raise HTTPException(400, f"Fournisseur « {ia[f]} » non autorisé — seuls "
                                         "Anthropic (Claude Opus) et OpenAI (ChatGPT) sont activés.")
        merged = update_settings(patch)
        return jsonable(merged)

    @app.get("/api/settings/prompts")
    def prompts_list():
        from .ai.orchestrator import list_prompts
        return {"prompts": list_prompts()}

    @app.get("/api/settings/prompts/{name}")
    def prompt_get(name: str):
        from .ai.orchestrator import load_prompt
        try:
            return jsonable(load_prompt(name))
        except FileNotFoundError:
            raise HTTPException(404, "prompt introuvable")

    @app.post("/api/keys")
    def key_set(body: dict = Body(...)):
        prov = str(body.get("provider", ""))
        key = str(body.get("api_key", ""))
        if prov not in ALLOWED_PROVIDERS:
            raise HTTPException(400, "Fournisseur non autorisé : seuls "
                                     "« anthropic » et « openai » sont acceptés (contrainte du projet).")
        if not key.strip():
            raise HTTPException(400, "clé vide")
        mode = store_key(prov, key.strip())
        log_local_access("cle_api", f"clé enregistrée pour {prov} ({mode})")
        return {"ok": True, "stockee_dans": mode,
                "avertissement": (None if mode == "keyring" else
                                  "Trousseau système indisponible : stockage fichier local 0600.")}

    @app.delete("/api/keys/{provider}")
    def key_del(provider: str):
        if provider not in ALLOWED_PROVIDERS:
            raise HTTPException(400, "fournisseur inconnu")
        delete_key(provider)
        return {"ok": True}

    @app.get("/api/documents/client-consent")
    def doc_client():
        out = load_settings_dir_exports() / f"accord_client_modele_{int(time.time())}.pdf"
        from .export.pdf_docs import document_client
        document_client(out)
        return FileResponse(out, media_type="application/pdf", filename="accord_client_modele.pdf")

    @app.get("/api/documents/registre")
    def doc_registre():
        out = load_settings_dir_exports() / f"registre_traitements_{int(time.time())}.pdf"
        from .export.pdf_docs import registre_traitements
        registre_traitements(out)
        return FileResponse(out, media_type="application/pdf", filename="registre_traitements.pdf")

    def load_settings_dir_exports() -> Path:
        from .config import EXPORT_DIR
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)
        return EXPORT_DIR

    # --------------------------------------------------------------- incidents
    @app.get("/api/incidents")
    def incidents_list():
        return {"incidents": list_incidents()}

    @app.post("/api/incidents")
    def incidents_add(body: dict = Body(...)):
        return add_incident(str(body.get("title", "incident"))[:200],
                            str(body.get("detail", ""))[:2000],
                            str(body.get("actions", ""))[:2000])

    @app.post("/api/incidents/{iid}/close")
    def incidents_close(iid: int):
        close_incident(iid)
        return {"ok": True}

    # ---------------------------------------------------------------- projets
    @app.get("/api/projects")
    def projects_list():
        return {"projects": list_projects()}

    @app.post("/api/projects")
    def projects_create(body: dict = Body(...)):
        try:
            return get_project(create_project(str(body.get("name", "")),
                                               body.get("params") or {},
                                               str(body.get("ref", "")),
                                               str(body.get("comment", "")))["id"])
        except ValueError as exc:
            raise HTTPException(400, str(exc))

    @app.get("/api/projects/{pid}")
    def project_get(pid: str):
        p = get_project(pid)
        if p is None:
            raise HTTPException(404, "projet introuvable")
        # compléments de tableau de bord
        with get_db() as db:
            n_plans = db.execute("SELECT COUNT(*) FROM plans WHERE project_id=?", (pid,)).fetchone()[0]
            latest_plan = db.execute("SELECT * FROM plans WHERE project_id=? "
                                     "ORDER BY imported_at DESC LIMIT 1", (pid,)).fetchone()
            n_interp = db.execute("SELECT COUNT(*) FROM interpretations WHERE project_id=?", (pid,)).fetchone()[0]
            interp_ok = db.execute("SELECT COUNT(*) FROM interpretations WHERE project_id=? AND validated=1",
                                   (pid,)).fetchone()[0]
            n_opts = db.execute("SELECT COUNT(*) FROM options WHERE project_id=?", (pid,)).fetchone()[0]
            retenu = db.execute("SELECT id FROM options WHERE project_id=? AND status IN ('retenue','figee') "
                                "ORDER BY created_at DESC LIMIT 1", (pid,)).fetchone()
            n_deliv = db.execute("SELECT COUNT(*) FROM deliverables WHERE project_id=?", (pid,)).fetchone()[0]
        steps = {
            "import": n_plans > 0,
            "parsing": bool(latest_plan and latest_plan["entities_count"]),
            "interpretation": n_interp > 0,
            "interpretation_validee": interp_ok > 0,
            "generation": n_opts > 0,
            "option_retenue": retenu is not None,
            "livrables": n_deliv > 0,
        }
        p["steps"] = steps
        p["plan_latest"] = jsonable(dict(latest_plan) if latest_plan else None)
        return p

    @app.put("/api/projects/{pid}")
    def project_put(pid: str, body: dict = Body(...)):
        try:
            return update_project(pid, body)
        except KeyError:
            raise HTTPException(404, "projet introuvable")
        except ValueError as exc:
            raise HTTPException(400, str(exc))

    @app.post("/api/projects/{pid}/duplicate")
    def project_dup(pid: str):
        return duplicate_project(pid)

    @app.delete("/api/projects/{pid}")
    def project_del(pid: str, confirm_name: str = ""):
        try:
            delete_project(pid, confirm_name)
            return {"ok": True, "supprime": pid}
        except PermissionError as exc:
            raise HTTPException(403, str(exc))

    @app.get("/api/projects/{pid}/snapshots")
    def snaps(pid: str):
        return {"snapshots": list_snapshots(pid)}

    @app.post("/api/projects/{pid}/snapshots")
    def snap_make(pid: str, body: dict = Body(default={})):
        return snapshot(pid, kind=body.get("kind", "etape"), label=body.get("label", ""))

    @app.post("/api/projects/{pid}/snapshots/{sid}/restore")
    def snap_restore(pid: str, sid: str):
        if not restore_snapshot(pid, sid):
            raise HTTPException(404, "snapshot introuvable")
        return {"ok": True}

    @app.get("/api/projects/{pid}/file")
    def project_file(pid: str, path: str):
        root = (PROJECTS_DIR / pid).resolve()
        target = (root / path).resolve()
        if not str(target).startswith(str(root)):
            raise HTTPException(403, "chemin hors projet")
        if target.suffix.lower() not in (".png", ".pdf", ".dxf", ".csv", ".xlsx", ".json"):
            raise HTTPException(403, "type de fichier non servi")
        if not target.exists():
            raise HTTPException(404, "fichier introuvable")
        return FileResponse(target)

    # -------------------------------------------------------------- plans
    @app.get("/api/projects/{pid}/plans")
    def plans_list(pid: str):
        with get_db() as db:
            rows = db.execute("SELECT * FROM plans WHERE project_id=? ORDER BY imported_at DESC",
                              (pid,)).fetchall()
        return {"plans": jsonable([dict(r) for r in rows])}

    @app.post("/api/projects/{pid}/plans")
    async def plan_upload(pid: str, file: UploadFile = File(...)):
        if get_project(pid) is None:
            raise HTTPException(404, "projet introuvable")
        d = project_dir(pid)
        tmp = d / "plans" / f"tmp_{int(time.time())}_{safe_filename(file.filename or 'plan.dxf')}"
        data = await file.read()
        if len(data) > MAX_DXF_SIZE:
            raise HTTPException(413, f"Fichier trop volumineux (max {human_size(MAX_DXF_SIZE)}).")
        tmp.write_bytes(data)
        try:
            info = dxfparse.validate_and_copy(tmp, d / "plans", MAX_DXF_SIZE)
        except dxfparse.DXFImportError as exc:
            tmp.unlink(missing_ok=True)
            raise HTTPException(422, str(exc))
        tmp.unlink(missing_ok=True)
        fname_alert = dxfparse.check_filename_suspicious(info["filename"])
        plan_id = new_id("PLN")
        stored = d / "plans" / f"{plan_id}_{safe_filename(info['filename'])}"
        if info["path"] != str(stored):
            shutil.move(info["path"], stored)
        with get_db() as db:
            db.execute(
                """INSERT INTO plans (id, project_id, filename, path, size, sha256, dxf_version,
                   anonymization_ok, imported_at)
                   VALUES (?,?,?,?,?,?,?,?,datetime('now'))""",
                (plan_id, pid, info["filename"], str(stored), info["size"], info["sha256"],
                 info["dxf_version"], 0 if fname_alert else 1,))
        if fname_alert:
            log_alert(pid, "nom_fichier", f"import {info['filename']} : {fname_alert}")
        return {"plan": {"id": plan_id, **info, "path": str(stored),
                         "filename_alert": fname_alert}}

    @app.post("/api/projects/{pid}/plans/{plan_id}/parse")
    def plan_parse(pid: str, plan_id: str, body: dict = Body(default={})):
        with get_db() as db:
            row = db.execute("SELECT * FROM plans WHERE id=? AND project_id=?",
                             (plan_id, pid)).fetchone()
        if row is None:
            raise HTTPException(404, "plan introuvable")
        d = project_dir(pid)
        path = Path(row["path"])
        if not path.exists():
            raise HTTPException(410, "fichier source introuvable — réimporter")
        try:
            parsed = dxfparse.parse_dxf(path, units_override=body.get("units"))
        except dxfparse.DXFImportError as exc:
            raise HTTPException(422, str(exc))
        parsed["fichier"]["date_import"] = row["imported_at"]
        parsed["fichier"]["hash_sha256"] = row["sha256"]
        dxfparse.save_parsed(parsed, d / "rendus")
        png_o = dxfparse.render_png(parsed, d / "rendus" / f"{plan_id}_original.png", clean=False,
                                     excluded_layers=set(body.get("exclude_layers", [])))
        png_c = dxfparse.render_png(parsed, d / "rendus" / f"{plan_id}_clean.png", clean=True,
                                     excluded_layers=set(body.get("exclude_layers", [])))
        alerts = parsed["anonymisation"]["alertes"]
        if alerts:
            for a in alerts:
                log_alert(pid, a["type"], a["message"])
        layers_meta = [{"nom": c["nom"], "couleur": c["couleur"], "nb": c["nombre_entites"],
                        "exclure": c["nom"] in body.get("exclude_layers", [])}
                       for c in parsed["calques"]]
        with get_db() as db:
            db.execute("""UPDATE plans SET units=?, bbox=?, layers=?, entities_count=?,
                          png_original=?, png_clean=?, entities_json=?, meta=?,
                          anonymization_ok = CASE WHEN ?> 0 THEN 0 ELSE anonymization_ok END
                          WHERE id=?""",
                       (parsed["unites"], json.dumps(parsed["emprise"]),
                        json.dumps(layers_meta, ensure_ascii=False),
                        parsed["nombre_total_entites"],
                        str(png_o.relative_to(d)), str(png_c.relative_to(d)),
                        "rendus/parsed.json",
                        json.dumps({"version_dxf": parsed["fichier"]["version_dxf"],
                                    "images": parsed["images"], "unit_to_m": parsed["unit_to_m"]}),
                        len(alerts), plan_id))
        warn = []
        if parsed["nombre_total_entites"] > 500_000:
            warn.append("Plus de 500 000 entités : performances dégradées, envisager un filtrage de calques.")
        if "heuristique" in parsed["unites_note"] or parsed["unites_note"] == "défaut — à confirmer":
            warn.append(f"Unités déduites ({parsed['unites']}, {parsed['unites_note']}) — à confirmer.")
        return jsonable({
            "ok": True, "units": parsed["unites"], "unites_note": parsed["unites_note"],
            "bbox": parsed["emprise"], "entities": parsed["nombre_total_entites"],
            "layers": layers_meta, "alerts": alerts, "warnings": warn,
            "png_original": f"rendus/{png_o.name}", "png_clean": f"rendus/{png_c.name}",
            "plan_id": plan_id,
        })

    @app.post("/api/projects/{pid}/plans/{plan_id}/render")
    def plan_render(pid: str, plan_id: str, body: dict = Body(default={})):
        d = project_dir(pid)
        parsed = dxfparse.load_parsed(d / "rendus")
        if not parsed:
            raise HTTPException(409, "parser le plan d'abord")
        suffix = int(time.time())
        png = d / "rendus" / f"{plan_id}_regen_{suffix}.png"
        dxfparse.render_png(parsed, png, clean=bool(body.get("clean")),
                            excluded_layers=set(body.get("exclude_layers", [])))
        with get_db() as db:
            db.execute(f"UPDATE plans SET {body.get('target', 'png_clean')}=? WHERE id=?",
                       (f"rendus/{png.name}", plan_id))
        return {"ok": True, "png": f"rendus/{png.name}"}

    @app.post("/api/projects/{pid}/plans/{plan_id}/confirm-anonymization")
    def plan_confirm(pid: str, plan_id: str, body: dict = Body(...)):
        decision = str(body.get("decision", "ignoree"))  # ignoree | corrigee
        with get_db() as db:
            db.execute("UPDATE plans SET anonymization_ok=1 WHERE id=? AND project_id=?",
                       (plan_id, pid))
        for a in list_alerts(pid):
            if a["decision"] == "en_attente" and a["kind"] in ("texte_suspect", "image", "cartouche",
                                                                "nom_fichier"):
                resolve_alert(a["id"], decision)
        return {"ok": True}

    @app.get("/api/projects/{pid}/plans/{plan_id}/preview-payload")
    def plan_preview(pid: str, plan_id: str):
        """Aperçu de ce qui sera envoyé à l'IA (§5.4.3)."""
        d = project_dir(pid)
        with get_db() as db:
            row = db.execute("SELECT * FROM plans WHERE id=? AND project_id=?",
                             (plan_id, pid)).fetchone()
        if row is None:
            raise HTTPException(404, "plan introuvable")
        parsed = dxfparse.load_parsed(d / "rendus") or {}
        texts = dxfparse.extract_plain_texts_for_review(parsed)
        from .ai.orchestrator import estimate_call
        from .ai.providers import list_models
        s = load_settings()["ia"]
        prov = s.get("fournisseur_vision", "anthropic")
        mdl = s.get("modele_vision", "")
        img = (d / row["png_clean"]) if row["png_clean"] else None
        img_bytes = img.read_bytes() if img and img.exists() else b""
        est = estimate_call(prov, mdl, img_bytes, "")

        return jsonable({
            "image": row["png_clean"],
            "textes_detectes": texts[:80],
            "nb_textes": len(texts),
            "provider": prov, "model": mdl, "estimation": est,
            "avertissement": "Une image du plan NETTOYÉ sera envoyée. Aucune donnée "
                             "identifiante ne doit y figurer.",
            "hash_image": sha256_file(Path(row["path"]))[:16] if row["path"] else "",
        })

    # -------------------------------------------------------- interprétation
    @app.get("/api/projects/{pid}/interpretations")
    def interp_list(pid: str):
        with get_db() as db:
            rows = db.execute("SELECT id, plan_id, source, provider, model, validated, created_at "
                              "FROM interpretations WHERE project_id=? ORDER BY created_at DESC",
                              (pid,)).fetchall()
        return {"interpretations": jsonable([dict(r) for r in rows])}

    @app.get("/api/projects/{pid}/interpretations/{iid}")
    def interp_get(pid: str, iid: str):
        with get_db() as db:
            row = db.execute("SELECT * FROM interpretations WHERE id=? AND project_id=?",
                             (iid, pid)).fetchone()
        if row is None:
            raise HTTPException(404, "interprétation introuvable")
        d = dict(row)
        d["json"] = json.loads(d.get("json") or "{}")
        d["validation"] = json.loads(d.get("validation") or "null")
        return jsonable(d)

    @app.post("/api/projects/{pid}/interpretations/run")
    def interp_run(pid: str, body: dict = Body(...)):
        """Phase 5 — appel IA de vision (job de fond)."""
        if get_project(pid) is None:
            raise HTTPException(404, "projet introuvable")
        plan_id = body.get("plan_id")
        with get_db() as db:
            row = db.execute("SELECT * FROM plans WHERE id=? AND project_id=?",
                             (plan_id, pid)).fetchone() if plan_id else None
        if row is None:
            raise HTTPException(409, "aucun plan sélectionné/parsé")
        if not row["png_clean"]:
            raise HTTPException(409, "lancer d'abord le parsing (image nettoyée requise)")
        if not body.get("confirmed"):
            raise HTTPException(400, "confirmation explicite de l'envoi requise (§5.9.1)")

        def job(progress, cancelled, meta):
            from .ai.orchestrator import interpret_plan_call
            d = project_dir(pid)
            progress("send", "Envoi de l'image du plan nettoyé…", 15)
            if cancelled():
                return {"cancelled": True}
            res = interpret_plan_call(pid, d / row["png_clean"],
                                      body.get("provider"), body.get("model"),
                                      user_confirmed=True)
            progress("analyse", "Analyse du modèle de vision…", 60)
            if not res["ok"]:
                err = res.get("error") or res.get("erreur") or "échec inconnu"
                if res.get("code") in ("config", "paranoid", "budget"):
                    raise RuntimeError(err)
                raise RuntimeError(err + " — basculez de fournisseur ou utilisez "
                                   "la saisie manuelle (mode dégradé).")
            data = res["data"]
            data.setdefault("murs_non_porteurs", [])
            data.setdefault("zones_humides", [])
            data.setdefault("escaliers", [])
            data.setdefault("hypotheses", [])
            data.setdefault("incertitudes", [])
            iid = new_id("ITP")
            write_json(d / "interpretations" / f"{iid}.json", {"json": data, "meta": {
                k: res[k] for k in ("provider", "model", "tokens_in", "tokens_out",
                                     "cost_usd", "hash_req", "hash_resp", "latency_s")}})
            with get_db() as db:
                db.execute(
                    """INSERT INTO interpretations (id, project_id, plan_id, source, provider,
                       model, json, validated, created_at)
                       VALUES (?,?,?,'ia',?,?,?,0,datetime('now'))""",
                    (iid, pid, plan_id, res["provider"], res["model"],
                     json.dumps(data, ensure_ascii=False)))
            progress("done", "Interprétation reçue — à valider/corriger.", 100)
            return {"interpretation_id": iid, "cost_usd": res["cost_usd"],
                    "tokens": [res["tokens_in"], res["tokens_out"]],
                    "raw_text": res["raw_text"][:4000]}

        jid = tasks.start("interpretation", job, {"pid": pid, "plan_id": plan_id})
        return {"job": jid}

    @app.post("/api/projects/{pid}/interpretations/manual")
    def interp_manual(pid: str, body: dict = Body(...)):
        """Mode dégradé — saisie manuelle (§2.7)."""
        data = body.get("json") or {}
        iid = new_id("ITP")
        _validate_interp(data)
        with get_db() as db:
            db.execute("""INSERT INTO interpretations (id, project_id, plan_id, source, json,
                          validated, created_at) VALUES (?,?,?, 'manuel', ?,0,datetime('now'))""",
                       (iid, pid, body.get("plan_id"), json.dumps(data, ensure_ascii=False)))
        return {"interpretation_id": iid}

    @app.put("/api/projects/{pid}/interpretations/{iid}")
    def interp_put(pid: str, iid: str, body: dict = Body(...)):
        data = body.get("json")
        validation = body.get("validation")
        force = bool(body.get("force"))
        if data is None:
            raise HTTPException(400, "json requis")
        errors = _validate_interp(data)
        validated = 0
        if validation and validation.get("statut") == "validee":
            for corr in validation.get("corrections", []):
                if not corr.get("raison"):
                    raise HTTPException(400, "chaque correction doit avoir une raison (§4.4).")
            pending = [u for u in (data.get("incertitudes") or [])
                       if not _uncertainty_decided(validation, u.get("id"))]
            if pending and not force:
                raise HTTPException(409, json.dumps({
                    "message": "Incertitudes non traitées — corriger, accepter, ou forcer "
                               "(validation possible mais déconseillée).",
                    "pending": pending}, ensure_ascii=False))
            validated = 1
        with get_db() as db:
            cur = db.execute("SELECT id FROM interpretations WHERE id=? AND project_id=?",
                             (iid, pid)).fetchone()
            if cur is None:
                raise HTTPException(404, "interprétation introuvable")
            db.execute("UPDATE interpretations SET json=?, validation=?, validated=? WHERE id=?",
                       (json.dumps(data, ensure_ascii=False),
                        json.dumps(validation, ensure_ascii=False) if validation else None,
                        validated, iid))
        write_json(project_dir(pid) / "interpretations" / f"{iid}.json",
                   {"json": data, "validation": validation})
        if validated:
            snapshot(pid, kind="etape", label=f"interprétation validée ({iid})")
        return {"ok": True, "validated": bool(validated), "schema_warnings": errors}

    def _validate_interp(data: dict) -> list[str]:
        from jsonschema import Draft7Validator
        from .ai.schemas import INTERPRETATION_SCHEMA
        v = Draft7Validator(INTERPRETATION_SCHEMA)
        errs = sorted(v.iter_errors(data), key=lambda e: list(e.path))
        msgs = [f"{'/'.join(map(str, e.path)) or '<racine>'}: {e.message}" for e in errs[:20]]
        if msgs:
            raise HTTPException(422, "schéma JSON invalide : " + " | ".join(msgs[:6]))
        return msgs

    def _uncertainty_decided(validation: dict, uid) -> bool:
        for t in validation.get("incertitudes_traitees", []):
            if t.get("id") == uid and (t.get("decision") or "").strip():
                return True
        return False

    # ------------------------------------------------------------- génération
    def proj_params_for_calc(pid: str) -> tuple[dict, dict, dict]:
        proj = get_project(pid)
        if proj is None:
            raise HTTPException(404, "projet introuvable")
        with get_db() as db:
            it = db.execute("SELECT * FROM interpretations WHERE project_id=? AND validated=1 "
                            "ORDER BY created_at DESC LIMIT 1", (pid,)).fetchone()
        if it is None:
            raise HTTPException(409, "valider d'abord une interprétation "
                                     "(IA ou saisie manuelle) — étape requise.")
        interp = json.loads(it["json"])
        s = load_settings()
        gen = s.get("generation", {})
        p = dict(proj.get("params") or {})
        p["id"] = pid
        p.setdefault("q_comportement", s["projet_defauts"]["q_comportement"])
        p.setdefault("categorie_importance", s["projet_defauts"]["categorie_importance"])
        p.setdefault("classe_exposition", s["projet_defauts"]["classe_exposition"])
        p.setdefault("duree_utilisation", s["projet_defauts"]["duree_utilisation"])
        p.setdefault("zone_sismique", 2)
        p.setdefault("zone_neige", "A2")
        p.setdefault("zone_vent", 2)
        p.setdefault("altitude", 50)
        p.setdefault("usage", "habitation")
        p.setdefault("niveaux", interp.get("batiment", {}).get("niveaux", 1))
        p.setdefault("hauteur_etage", interp.get("batiment", {}).get("hauteur_etage", 2.8))
        p.setdefault("materiaux", ["beton_arme"])
        p.setdefault("seed", int(time.time()) % 1_000_000)
        p.setdefault("nb_options", s["projet_defauts"]["nb_options"])
        p.setdefault("critere_classement", s["projet_defauts"]["critereme_classement"])
        p.setdefault("systeme_sismique", "portique")
        p.setdefault("classe_sol", "A")
        p.setdefault("qsol_kpa", s.get("normes", {}).get("qsol_kpa", 250.0))
        return p, gen, interp

    @app.get("/api/projects/{pid}/generation/config")
    def gen_config(pid: str):
        p, gen, interp = proj_params_for_calc(pid)
        from .ai.orchestrator import estimate_call
        s = load_settings()["ia"]
        est = estimate_call(s.get("fournisseur_raisonnement", "anthropic"),
                            s.get("modele_raisonnement", ""), b"",
                            json.dumps(interp, ensure_ascii=False))
        return jsonable({"params": p, "generation": gen, "interpretation_ready": True,
                         "estimation_ia": est})

    @app.post("/api/projects/{pid}/generate")
    def generate(pid: str, body: dict = Body(default={})):
        p, gen, interp = proj_params_for_calc(pid)
        if body.get("nb_options"):
            p["nb_options"] = max(3, min(5, int(body["nb_options"])))
        if body.get("criterere_classement") or body.get("critere_classement"):
            p["critere_classement"] = body.get("critere_classement") or body.get("criterere_classement")
        if body.get("seed") is not None:
            p["seed"] = int(body["seed"])
        use_ai = bool(body.get("use_ai", False))
        ai_variants: list[dict] = []
        from .security import has_key
        any_key = any(has_key(pr) for pr in ALLOWED_PROVIDERS)

        def job(progress, cancelled, meta):
            nonlocal ai_variants
            from .gen.generator import generate_options
            if use_ai and any_key and not cancelled():
                progress("ia", "Appel du modèle de raisonnement (pistes créatives)…", 8)
                try:
                    from .ai.orchestrator import creative_variants_call
                    res = creative_variants_call(pid, interp, {
                        "zones": {"seisme": p.get("zone_sismique"), "neige": p.get("zone_neige"),
                                   "vent": p.get("zone_vent")},
                        "materiaux": p.get("materiaux"), "q": p.get("q_comportement"),
                        "niveaux": p.get("niveaux"),
                        "contrainte": "variantes constructibles uniquement, portées 3—7.5 m"},
                        body.get("provider"), body.get("model"))
                    if res["ok"] and isinstance(res["data"], dict):
                        ai_variants = list(res["data"].get("variantes", []))[:3]
                        progress("ia", f"{len(ai_variants)} piste(s) IA retenues pour validation "
                                 f"par calcul (coût {res.get('cost_usd', 0):.4f} USD).", 10)
                    else:
                        progress("ia", f"IA créative indisponible ({res.get('error')}) — "
                                 "mode dégradé : algorithmes locaux seuls.", 10)
                except Exception as exc:
                    progress("ia", f"IA créative KO ({exc}) — mode dégradé local.", 10)
            elif use_ai and not any_key:
                progress("ia", "Aucune clé API : génération 100 % locale (mode dégradé).", 10)

            def cb(stage, msg, pct):
                progress(stage, msg, pct)

            out = generate_options(interp, p, gen, ai_variants=ai_variants or None,
                                   progress=cb, cancel=cancelled, parsed=_load_parsed(pid))
            d = project_dir(pid)
            opts_saved = []
            with get_db() as db:
                db.execute("DELETE FROM options WHERE project_id=? AND status='generee'", (pid,))
                for o in out["options"]:
                    oid = new_id("OPT")
                    o["id_saved"] = oid
                    o["projet_id"] = pid
                    write_json(d / "options" / f"{oid}.json", o)
                    full = dict(o)
                    resultats = full.pop("resultats_calcul", None)
                    db.execute(
                        """INSERT INTO options (id, project_id, interpretation_id, method, seed,
                           short_desc, json, indicators, conformity, status, rank, created_at)
                           VALUES (?,?,?,?,?,?,?,?,?, 'generee', ?, datetime('now'))""",
                        (oid, pid, None, full["methode"], full["seed"], full["description_courte"],
                         json.dumps(jsonable(full), ensure_ascii=False),
                         json.dumps(jsonable(o.get("indicateurs")), ensure_ascii=False),
                         json.dumps(jsonable(o.get("conformite")), ensure_ascii=False),
                         o.get("rank")))
                    if resultats is not None:
                        write_json(d / "calculs" / f"{oid}_resultats.json", resultats)
                    opts_saved.append(oid)
            write_json(d / "options" / "index.json", out["index"])
            snapshot(pid, kind="etape", label=f"génération {len(opts_saved)} options")
            return {"nb_presentees": len(out["options"]), "index": out["index"],
                    "diagnostic": out.get("diagnostic", ""), "option_ids": opts_saved}

        jid = tasks.start("generation", job, {"pid": pid})
        return {"job": jid}

    def _load_parsed(pid: str) -> dict | None:
        return read_json(project_dir(pid) / "rendus" / "parsed.json")

    # ---------------------------------------------------------------- options
    @app.get("/api/projects/{pid}/options")
    def options_list(pid: str):
        with get_db() as db:
            rows = db.execute(
                """SELECT id, method, seed, short_desc, indicators, conformity, status, rank,
                          created_at,
                          (SELECT COUNT(*) FROM edits e WHERE e.option_id=options.id) AS n_edits
                   FROM options WHERE project_id=? ORDER BY rank, created_at DESC""",
                (pid,)).fetchall()
        out = []
        for r in rows:
            d = dict(r)
            for k in ("indicators", "conformity"):
                d[k] = json.loads(d.get(k) or "null")
            d.pop("json", None)
            out.append(d)
        return {"options": jsonable(out)}

    def _load_option_row(pid: str, oid: str) -> dict:
        with get_db() as db:
            row = db.execute("SELECT * FROM options WHERE id=? AND project_id=?",
                             (oid, pid)).fetchone()
        if row is None:
            raise HTTPException(404, "option introuvable")
        d = dict(row)
        d["json"] = json.loads(d["json"])
        full = d["json"]
        calc_path = project_dir(pid) / "calculs" / f"{oid}_resultats.json"
        if calc_path.exists():
            full["resultats_calcul"] = read_json(calc_path, {})
        return {"row": d, "option": full}

    @app.get("/api/projects/{pid}/options/{oid}")
    def option_get(pid: str, oid: str):
        ctx = _load_option_row(pid, oid)
        full = ctx["option"]
        full["id"] = oid
        if not full.get("resultats_calcul"):
            full["resultats_calcul"] = full.get("json", {})
        # données de rendu SVG pour le frontend
        svg3d = render_option_iso_svg(full)
        return jsonable({"option": full, "status": ctx["row"]["status"], "rank": ctx["row"]["rank"],
                        "iso_svg": svg3d})

    @app.get("/api/projects/{pid}/options/{oid}/render")
    def option_render(pid: str, oid: str):
        ctx = _load_option_row(pid, oid)
        out = project_dir(pid) / "rendus" / f"{oid}_vue.png"
        render_option_png(ctx["option"], out, title=f"Option {oid}")
        return {"png": f"rendus/{out.name}"}

    @app.post("/api/projects/{pid}/options/{oid}/select")
    def option_select(pid: str, oid: str, body: dict = Body(default={})):
        with get_db() as db:
            row = db.execute("SELECT id FROM options WHERE id=? AND project_id=?",
                             (oid, pid)).fetchone()
            if row is None:
                raise HTTPException(404, "option introuvable")
            db.execute("UPDATE options SET status='rejetee' WHERE project_id=? AND status='retenue'",
                       (pid,))
            db.execute("UPDATE options SET status='retenue' WHERE id=?", (oid,))
        _append_history(pid, oid, "selection", {"raison": body.get("raison", "")})
        snapshot(pid, kind="etape", label=f"option retenue {oid}")
        return {"ok": True}

    def _append_history(pid: str, oid: str, typ: str, payload: dict):
        d = project_dir(pid) / "options" / f"{oid}.history.json"
        hist = read_json(d, default=[]) or []
        hist.append({"date": now_iso(), "type": typ, **payload})
        write_json(d, hist[-500:])

    @app.post("/api/projects/{pid}/options/{oid}/reject")
    def option_reject(pid: str, oid: str):
        with get_db() as db:
            db.execute("UPDATE options SET status='rejetee' WHERE id=? AND project_id=?",
                       (oid, pid))
        return {"ok": True}

    @app.post("/api/projects/{pid}/options/{oid}/freeze")
    def option_freeze(pid: str, oid: str):
        ctx = _load_option_row(pid, oid)
        snap = snapshot(pid, kind="figeage", label=f"version figée {oid}", option_id=oid)
        with get_db() as db:
            db.execute("UPDATE options SET status='figee' WHERE id=? AND project_id=?",
                       (oid, pid))
        write_json(project_dir(pid) / "options" / f"{oid}_figee.json", ctx["option"])
        _append_history(pid, oid, "figeage", {"snapshot_id": snap["id"] if snap else None})
        return {"ok": True, "snapshot_id": snap["id"] if snap else None}

    def _apply_edit(option: dict, op: str, body: dict) -> Optional[str]:
        """Applique une opération de l'éditeur structurel sur option['structure'].
        Retourne un message d'erreur ou None."""
        st = option.setdefault("structure", {})
        try:
            if op == "move_poteau":
                pos = [float(v) for v in body.get("position", [])]
                if len(pos) != 2:
                    return "position [x, y] requise"
                for c in st.get("poteaux", []):
                    if c["id"] == body.get("element"):
                        c["position"] = pos
                        return None
                return "poteau introuvable"
            if op == "add_poteau":
                pos = [float(v) for v in body.get("position", [])]
                if len(pos) != 2:
                    return "position [x, y] requise"
                sec = body.get("section", [0.30, 0.30])
                nid = f"PA{len(st.get('poteaux', [])) + 1:02d}"
                st.setdefault("poteaux", []).append({
                    "id": nid, "position": pos, "section": [float(sec[0]), float(sec[1])],
                    "niveaux": body.get("niveaux", [1, int(option.get("params", {}).get("niveaux", 1))]),
                    "ajoute_manuellement": True})
                return None
            if op in ("set_poteau_section", "set_poutre_section", "set_voile_epaisseur"):
                target = {"set_poteau_section": "poteaux", "set_poutre_section": "poutres",
                          "set_voile_epaisseur": "voiles"}[op]
                for el in st.get(target, []):
                    if el["id"] == body.get("element"):
                        if op == "set_voile_epaisseur":
                            el["epaisseur"] = float(body.get("epaisseur", el.get("epaisseur", 0.2)))
                        else:
                            sec = body.get("section")
                            if not (isinstance(sec, (list, tuple)) and len(sec) >= 2):
                                return "section [b, h] requise"
                            el["section"] = [float(sec[0]), float(sec[1])]
                        return None
                return "élément introuvable"
            if op == "delete_element":
                found = False
                for key in ("poteaux", "poutres", "voiles", "fondations", "dalles"):
                    keep = []
                    for el in st.get(key, []):
                        if el.get("id") == body.get("element"):
                            found = True
                        else:
                            keep.append(el)
                    st[key] = keep
                if not found:
                    return "élément introuvable"
                return None
            if op == "add_poutre":
                d = body.get("debut"); f = body.get("fin")
                if not (isinstance(d, (list, tuple)) and isinstance(f, (list, tuple))):
                    return "debut/fin [x, y] requis"
                sec = body.get("section", [0.25, 0.50])
                nid = f"BA{len(st.get('poutres', [])) + 1:02d}"
                st.setdefault("poutres", []).append({
                    "id": nid, "debut": [float(d[0]), float(d[1])],
                    "fin": [float(f[0]), float(f[1])],
                    "section": [float(sec[0]), float(sec[1])],
                    "niveau": int(body.get("niveau", 1)), "ajoutee_manuellement": True})
                return None
            if op == "set_dalle_epaisseur":
                for el in st.get("dalles", []):
                    if el["id"] == body.get("element"):
                        el["epaisseur"] = float(body.get("epaisseur", 0.2))
                        return None
                return "dalle introuvable"
            if op == "set_fondation":
                for el in st.get("fondations", []):
                    if el.get("poteau") == body.get("element") or el.get("id") == body.get("element"):
                        dims = body.get("dimensions")
                        if isinstance(dims, (list, tuple)) and len(dims) >= 2:
                            el["dimensions"] = [float(dims[0]), float(dims[1]),
                                                float(dims[2]) if len(dims) > 2 else el.get("dimensions", [1, 1, 0.5])[2]]
                        if body.get("type"):
                            el["type"] = str(body["type"])
                        return None
                return "fondation introuvable"
            if op == "set_altitude_radier" and False:  # placeholder inutilisé
                return None
        except (TypeError, ValueError, KeyError, IndexError) as exc:
            return f"paramètres d'édition invalides : {exc}"
        return f"opération inconnue : {op}"

    # ------------------------------------------------------------------ édition
    @app.post("/api/projects/{pid}/options/{oid}/edit")
    def option_edit(pid: str, oid: str, body: dict = Body(...)):
        op = str(body.get("op", ""))
        reason = str(body.get("reason", "")).strip()
        if not reason:
            raise HTTPException(400, "chaque modification doit être justifiée (raison) — §4.7.")
        ctx = _load_option_row(pid, oid)
        option = ctx["option"]
        before = json.loads(json.dumps(option.get("structure", {})))
        err = _apply_edit(option, op, body)
        if err:
            raise HTTPException(422, err)
        p, gen, interp = proj_params_for_calc(pid)
        try:
            an = analyze_option(option, p, gen)
            option["resultats_calcul"] = an["resultats"]
            option["indicateurs"] = an["indicateurs"]
            option["conformite"] = an["conformite"]
            option["synthese"] = an["synthese"]
        except Exception as exc:
            raise HTTPException(422, f"recalcul impossible : {exc} — version précédente conservée.")
        with get_db() as db:
            db.execute("""UPDATE options SET json=?, indicators=?, conformity=? WHERE id=?""",
                       (json.dumps(jsonable(_trim(option)), ensure_ascii=False),
                        json.dumps(jsonable(option["indicateurs"])),
                        json.dumps(jsonable(option["conformite"])), oid))
            db.execute("""INSERT INTO edits (option_id, project_id, date, type, element,
                          before, after, reason, option_json_after)
                          VALUES (?, ?, datetime('now'), ?, ?, ?, ?, ?, ?)""",
                       (oid, pid, op, str(body.get("element", "")),
                        json.dumps(jsonable(before), ensure_ascii=False),
                        json.dumps(jsonable(option["structure"]), ensure_ascii=False),
                        reason,
                        json.dumps(jsonable(_trim(option)), ensure_ascii=False)))
        write_json(project_dir(pid) / "calculs" / f"{oid}_resultats.json", an["resultats"])
        write_json(project_dir(pid) / "options" / f"{oid}.json", option)
        _append_history(pid, oid, "edit", {"op": op, "reason": reason})
        return jsonable({"ok": True, "indicateurs": option["indicateurs"],
                         "conformite": option["conformite"],
                         "synthese": option["synthese"],
                         "avertissements": option["resultats_calcul"].get("avertissements", []),
                         "structure": option["structure"]})

    def _trim(option: dict) -> dict:
        o = dict(option)
        o.pop("resultats_calcul", None)
        return o

    @app.get("/api/projects/{pid}/options/{oid}/edits")
    def edits_list(pid: str, oid: str):
        with get_db() as db:
            rows = db.execute("SELECT id, date, type, element, before, after, reason "
                              "FROM edits WHERE option_id=? AND project_id=? ORDER BY id DESC",
                              (oid, pid)).fetchall()
        return {"edits": jsonable([dict(r) for r in rows])}

    @app.post("/api/projects/{pid}/options/{oid}/undo")
    def edit_undo(pid: str, oid: str):
        with get_db() as db:
            row = db.execute("SELECT * FROM edits WHERE option_id=? AND project_id=? "
                             "ORDER BY id DESC LIMIT 1", (oid, pid)).fetchone()
        if row is None:
            raise HTTPException(404, "aucune édition à annuler")
        before = json.loads(row["before"])
        ctx = _load_option_row(pid, oid)
        option = ctx["option"]
        option["structure"] = before
        p, gen, _ = proj_params_for_calc(pid)
        an = analyze_option(option, p, gen)
        option["resultats_calcul"] = an["resultats"]
        option["indicateurs"] = an["indicateurs"]
        option["conformite"] = an["conformite"]
        with get_db() as db:
            db.execute("DELETE FROM edits WHERE id=?", (row["id"],))
            db.execute("UPDATE options SET json=?, indicators=?, conformity=? WHERE id=?",
                       (json.dumps(jsonable(_trim(option)), ensure_ascii=False),
                        json.dumps(jsonable(an["indicateurs"])),
                        json.dumps(jsonable(an["conformite"])), oid))
        write_json(project_dir(pid) / "options" / f"{oid}.json", option)
        write_json(project_dir(pid) / "calculs" / f"{oid}_resultats.json", an["resultats"])
        _append_history(pid, oid, "undo", {"edit_id": row["id"]})
        return jsonable({"ok": True, "indicateurs": an["indicateurs"],
                         "conformite": an["conformite"], "structure": option["structure"]})

    @app.post("/api/projects/{pid}/options/{oid}/recalc")
    def option_recalc(pid: str, oid: str):
        ctx = _load_option_row(pid, oid)
        option = ctx["option"]
        p, gen, _ = proj_params_for_calc(pid)
        an = analyze_option(option, p, gen)
        option["resultats_calcul"] = an["resultats"]
        option["indicateurs"] = an["indicateurs"]
        option["conformite"] = an["conformite"]
        with get_db() as db:
            db.execute("UPDATE options SET json=?, indicators=?, conformity=? WHERE id=?",
                       (json.dumps(jsonable(_trim(option)), ensure_ascii=False),
                        json.dumps(jsonable(an["indicateurs"])),
                        json.dumps(jsonable(an["conformite"])), oid))
        write_json(project_dir(pid) / "calculs" / f"{oid}_resultats.json", an["resultats"])
        return jsonable({"ok": True, "indicateurs": an["indicateurs"],
                         "conformite": an["conformite"], "synthese": an["synthese"]})

    # ------------------------------------------------------------- livrables
    @app.get("/api/projects/{pid}/deliverables")
    def deliv_list(pid: str):
        with get_db() as db:
            rows = db.execute("SELECT * FROM deliverables WHERE project_id=? "
                              "ORDER BY created_at DESC", (pid,)).fetchall()
        return {"deliverables": jsonable([dict(r) for r in rows])}

    @app.post("/api/projects/{pid}/deliverables")
    def deliv_generate(pid: str, body: dict = Body(...)):
        oid = body.get("option_id")
        if not oid:
            raise HTTPException(400, "option_id requis")
        ctx = _load_option_row(pid, oid)
        include = body.get("include", ["plans", "note", "quantitatifs", "traacabilite"])
        use_ai = bool(body.get("use_ai_drafting", False))

        def job(progress, cancelled, meta):
            return _build_deliverables(pid, oid, ctx["option"], include, use_ai,
                                       body.get("provider"), body.get("model"),
                                       progress, cancelled)

        jid = tasks.start("deliverables", job, {"pid": pid, "option_id": oid})
        return {"job": jid}

    def _build_deliverables(pid, oid, option, include, use_ai, provider, model, progress, cancelled):
        d = project_dir(pid)
        stamp = time.strftime("%Y%m%dT%H%M%S")
        out_dir = d / "livrables" / f"{stamp}_{oid}"
        out_dir.mkdir(parents=True, exist_ok=True)
        p, gen, interp = proj_params_for_calc(pid)
        option = dict(option)
        option["id"] = oid
        emprise = (option.get("meta") or {}).get("emprise") or {"x0": 0, "y0": 0, "x1": 12.5, "y1": 9.0}
        created: list[dict] = []
        infos = {"projet": f"{p.get('name', pid)}", "date": now_iso()[:16].replace("T", " "),
                 "option": oid}

        def register(typ: str, path: Path):
            h = sha256_file(path)
            with get_db() as db:
                did = new_id("DEL")
                db.execute("""INSERT INTO deliverables (id, project_id, option_id, type, path,
                              sha256, created_at) VALUES (?,?,?,?,?,?,datetime('now'))""",
                           (did, pid, oid, typ, str(path.relative_to(d)), h))
            created.append({"id": did, "type": typ, "path": str(path.relative_to(d)),
                            "sha256": h, "size": path.stat().st_size if path.exists() else 0})

        prog = 10
        if "plans" in include:
            from .export.dxf_plans import plan_coffrage, plan_ferraillage, plan_fondations
            progress("dxf", "Plan de fondations…", prog); prog += 8
            plan_fondations(option, emprise, out_dir / f"{oid}_fondations.dxf", infos)
            register("plan_dxf_fondations", out_dir / f"{oid}_fondations.dxf")
            if cancelled():
                return {"cancelled": True, "created": created}
            progress("dxf", "Plan de coffrage…", prog); prog += 8
            plan_coffrage(option, emprise, out_dir / f"{oid}_coffrage.dxf", infos)
            register("plan_dxf_coffrage", out_dir / f"{oid}_coffrage.dxf")
            progress("dxf", "Plan de ferraillage (synthèse)…", prog); prog += 8
            plan_ferraillage(option, emprise, out_dir / f"{oid}_ferraillage.dxf", infos)
            register("plan_dxf_ferraillage", out_dir / f"{oid}_ferraillage.dxf")
        png = out_dir / f"{oid}_vue.png"
        render_option_png(option, png, title=f"{infos['projet']} — {oid}")
        png3 = out_dir / f"{oid}_iso.png"
        render_option_iso(option, png3)
        if "quantitatifs" in include:
            from .export.quantities import export_csv, export_xlsx, quantities_rows
            progress("qty", "Quantitatifs…", prog); prog += 8
            rows = quantities_rows(option, p)
            export_csv(rows, out_dir / f"{oid}_quantitatifs.csv")
            register("quantitatifs_csv", out_dir / f"{oid}_quantitatifs.csv")
            try:
                export_xlsx(rows, out_dir / f"{oid}_quantitatifs.xlsx")
                register("quantitatifs_xlsx", out_dir / f"{oid}_quantitatifs.xlsx")
            except Exception:
                pass
        redaction = None
        if use_ai:
            progress("ia", "Rédaction assistée des sections explicatives…", prog); prog += 10
            try:
                from .ai.orchestrator import drafting_call
                donnees = {
                    "projet": {"nom": p.get("name"), "typologie": p.get("type_batiment"),
                               "niveaux": p.get("niveaux"), "usage": p.get("usage"),
                               "zones": {"seisme": p.get("zone_sismique"), "neige": p.get("zone_neige"),
                                          "vent": p.get("zone_vent")},
                               "note": "aucune donnée identifiante — anonymisé en amont"},
                    "option": {"id": oid, "description": option.get("description_courte"),
                               "indicateurs": option.get("indicateurs"),
                               "conformite": option.get("conformite"),
                               "synthese": (option.get("resultats_calcul") or {}).get("synthese"),
                               "avertissements": (option.get("resultats_calcul") or {}).get("avertissements")},
                }
                res = drafting_call(pid, donnees, provider, model)
                if res["ok"]:
                    redaction = res["data"]
                else:
                    progress("ia", f"rédaction IA indisponible ({res.get('error')}) — "
                             "note générée sans IA.", prog)
            except Exception as exc:
                progress("ia", f"rédaction IA KO ({exc}) — mode dégradé sans IA.", prog)
        if "note" in include:
            from .export.pdf_docs import note_de_calcul
            progress("pdf", "Note de calcul PDF…", prog); prog += 12
            note_de_calcul(out_dir / f"{oid}_note_calcul.pdf", {
                "name": p.get("name"), "params": p}, option, redaction, png, png3)
            register("note_pdf", out_dir / f"{oid}_note_calcul.pdf")
        if "traacabilite" in include or "traçabilité" in include:
            from .export.pdf_docs import rapport_tracabilite
            progress("pdf", "Rapport de traçabilité…", prog); prog += 8
            with get_db() as db:
                plans = [dict(r) for r in db.execute(
                    "SELECT * FROM plans WHERE project_id=?", (pid,)).fetchall()]
                ints = [dict(r) for r in db.execute(
                    "SELECT id, plan_id, source, provider, model, validated, created_at "
                    "FROM interpretations WHERE project_id=?", (pid,)).fetchall()]
                edits = [dict(r) for r in db.execute(
                    "SELECT date, type, element, reason FROM edits WHERE project_id=? ORDER BY id",
                    (pid,)).fetchall()]
                aic = ai_calls(pid)
                dels = [dict(r) for r in db.execute(
                    "SELECT * FROM deliverables WHERE project_id=?", (pid,)).fetchall()]
                optidx = read_json(d / "options" / "index.json", default={})
            rapport_tracabilite(out_dir / f"{oid}_tracabilite.pdf",
                                {"id": pid, "name": p.get("name"),
                                 "params": {k: v for k, v in p.items() if not k.startswith("_")}},
                                plans, ints, optidx, edits, aic, dels)
            register("traacabilite_pdf", out_dir / f"{oid}_tracabilite.pdf")
        snapshot(pid, kind="etape", label=f"livrables {oid}")
        progress("done", f"{len(created)} fichier(s) produits.", 100)
        return {"created": created, "ai_drafting_used": bool(redaction)}

    @app.get("/api/projects/{pid}/deliverables/{did}/file")
    def deliv_file(pid: str, did: str):
        with get_db() as db:
            row = db.execute("SELECT * FROM deliverables WHERE id=? AND project_id=?",
                             (did, pid)).fetchone()
        if row is None:
            raise HTTPException(404, "livrable introuvable")
        target = (project_dir(pid) / row["path"]).resolve()
        if not target.exists():
            raise HTTPException(410, "fichier supprimé")
        return FileResponse(target, filename=target.name)

    @app.post("/api/projects/{pid}/deliverables/export")
    def deliv_export(pid: str, body: dict = Body(...)):
        dest = Path(str(body.get("dest_dir", ""))).expanduser()
        if not str(dest) or not dest.is_dir():
            raise HTTPException(400, "répertoire de destination inaccessible — "
                                     "choisir un dossier existant.")
        copied = []
        for did in body.get("ids", []):
            with get_db() as db:
                row = db.execute("SELECT * FROM deliverables WHERE id=? AND project_id=?",
                                 (did, pid)).fetchone()
            if row is None:
                continue
            src = project_dir(pid) / row["path"]
            if src.exists():
                out = dest / src.name
                shutil.copy2(src, out)
                copied.append(str(out))
        log_local_access("export_livrables", f"{len(copied)} fichiers → {dest}")
        return {"ok": True, "copied": copied}

    # -------------------------------------------------------------------- jobs
    @app.get("/api/jobs/{jid}")
    def job_status(jid: str):
        st = tasks.status(jid)
        if st is None:
            raise HTTPException(404, "job inconnu")
        return jsonable(st)

    @app.post("/api/jobs/{jid}/cancel")
    def job_cancel(jid: str):
        return {"ok": tasks.cancel(jid)}

    # ------------------------------------------------------------------ journaux
    @app.get("/api/projects/{pid}/ai-calls")
    def proj_ai_calls(pid: str):
        from .ai.orchestrator import budget_status
        return {"calls": ai_calls(pid), "budget": budget_status(pid)}

    @app.get("/api/projects/{pid}/alerts")
    def proj_alerts(pid: str):
        return {"alerts": list_alerts(pid)}

    @app.post("/api/projects/{pid}/alerts/{aid}")
    def proj_alert_resolve(pid: str, aid: int, body: dict = Body(...)):
        resolve_alert(aid, str(body.get("decision", "ignoree")))
        return {"ok": True}

    @app.get("/api/ai-calls/export")
    def ai_export(fmt: str = "csv"):
        import csv as _csv
        from io import StringIO
        rows = ai_calls(None, 5000)
        buf = StringIO()
        fields = ["datetime", "project_id", "provider", "model", "purpose", "tokens_in",
                  "tokens_out", "cost_usd", "hash_req", "hash_resp", "status", "latency_s"]
        w = _csv.DictWriter(buf, fieldnames=fields, extrasaction="ignore", delimiter=";")
        w.writeheader()
        for r in rows:
            w.writerow(r)
        out = Path(__file__).resolve().parent.parent / "data" / "exports" / f"journal_ia_{int(time.time())}.{fmt}"
        out.parent.mkdir(parents=True, exist_ok=True)
        if fmt == "json":
            out.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        else:
            out.write_text(buf.getvalue(), encoding="utf-8")
        return FileResponse(out, filename=out.name)

    @app.post("/api/maintenance/purge")
    def purge_run():
        s = load_settings()
        n = purge_old_snapshots(int(s["retention"]["snapshots_jours"]))
        return {"snapshots_supprimes": n}

    @app.get("/api/local-access-log")
    def access_log(limit: int = 200):
        with get_db() as db:
            rows = db.execute("SELECT * FROM access_log ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
        return {"log": jsonable([dict(r) for r in rows])}


def render_option_iso(option: dict, out_path: Path) -> Path:
    """Mini isométrie PNG pour le PDF (Figure 2)."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    st = option.get("structure", {})
    h = 2.8
    fig = plt.figure(figsize=(8, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_axis_off()
    for lvl in sorted({int(b.get("niveau", 1)) for b in st.get("poutres", [])} or {1}):
        z = lvl * h
        for b in st.get("poutres", []):
            if int(b.get("niveau", 1)) != lvl:
                continue
            ax.plot([b["debut"][0], b["fin"][0]], [b["debut"][1], b["fin"][1]], [z, z],
                    color="#2471a3", linewidth=1.2)
        for c in st.get("poteaux", []):
            lv = c.get("niveaux", [0, 0])
            if not (min(lv) <= lvl - 1 <= max(lv)):
                continue
            x, y = c["position"]
            ax.plot([x, x], [y, y], [(lvl - 1) * h, lvl * h], color="#b03a2e", linewidth=2)
    ax.view_init(elev=22, azim=-60)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out_path), dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return out_path


# ---------------------------------------------------------------------------
# Frontend (React build) monté en dernier, avec fallback SPA
# ---------------------------------------------------------------------------

def mount_frontend(app):
    if WEB_DIST.exists() and (WEB_DIST / "index.html").exists():
        app.mount("/assets", StaticFiles(directory=str(WEB_DIST / "assets")), name="assets")

        @app.get("/", response_class=HTMLResponse, include_in_schema=False)
        @app.get("/ui/{full_path:path}", response_class=HTMLResponse, include_in_schema=False)
        def spa(full_path: str = ""):
            candidate = WEB_DIST / full_path
            if full_path and candidate.is_file():
                return FileResponse(candidate)
            return HTMLResponse((WEB_DIST / "index.html").read_text(encoding="utf-8"))
    else:
        @app.get("/", response_class=HTMLResponse, include_in_schema=False)
        def spa_missing():
            return HTMLResponse(
                "<h1>StructAI</h1><p>Backend opérationnel — interface React non "
                "construite. Lancer <code>cd web && npm install && npm run build</code> "
                "puis recharger.</p><p><a href='/api/ping'>/api/ping</a> · "
                "<a href='/api/status'>/api/status</a></p>")
