"""Flux API complet (sans IA) via TestClient : gardes normatifs, sécurité,
four-nisseur, édition avec raison, undo, livrables."""
import time


def _wait_job(client, jid, timeout=240):
    t0 = time.time()
    while time.time() - t0 < timeout:
        j = client.get(f"/api/jobs/{jid}").json()
        if j.get("done"):
            return j
        time.sleep(0.4)
    raise AssertionError("job jamais terminé")


def test_ping_et_status(client):
    r = client.get("/api/ping")
    assert r.json()["backend"] == "connecté"
    s = client.get("/api/status").json()
    assert set(s["providers"]) == {"anthropic", "openai"}  # contrainte projet
    assert s["db"]["integrity"]


def test_fournisseur_non_autorise_refuse(client):
    r = client.put("/api/settings", json={"ia": {"fournisseur_vision": "google"}})
    assert r.status_code == 400
    r = client.post("/api/keys", json={"provider": "mistral", "api_key": "x"})
    assert r.status_code == 400
    r = client.put("/api/settings", json={"ia": {"cle_api_anthropic": "sk-test"}})
    assert r.status_code == 400  # jamais de clé en clair dans les settings


def test_suppression_exige_nom(client, project):
    r = client.delete(f"/api/projects/{project}", params={"confirm_name": "zap"})
    assert r.status_code == 403
    assert client.get(f"/api/projects/{project}").status_code == 200


def test_generate_bloque_sans_validation(client):
    pid = client.post("/api/projects", json={"name": "sans-interp", "params": {}}).json()["id"]
    r = client.post(f"/api/projects/{pid}/generate", json={"use_ai": False})
    assert r.status_code == 409


def test_validation_flux_obligatoire(client):
    import json as _json
    from conftest import INTERP
    pid = client.post("/api/projects", json={"name": "garde-validation",
                                             "params": dict(INTERP)}).json()["id"]
    iid = client.post(f"/api/projects/{pid}/interpretations/manual",
                      json={"json": INTERP}).json()["interpretation_id"]
    # statut validee sans décisions -> refus 409
    r = client.put(f"/api/projects/{pid}/interpretations/{iid}",
                   json={"json": INTERP, "validation": {"statut": "validee"}})
    assert r.status_code == 409
    # correction sans raison -> 400
    r = client.put(f"/api/projects/{pid}/interpretations/{iid}",
                   json={"json": INTERP, "validation": {"statut": "validee",
                        "corrections": [{"type": "t", "element": "MP1"}],
                        "incertitudes_traitees": [{"id": "U1", "decision": "acceptee",
                                                   "raison": "r"}]}})
    assert r.status_code == 400
    # json invalide (schéma) -> 422
    r = client.put(f"/api/projects/{pid}/interpretations/{iid}",
                   json={"json": {"batiment": {}}})
    assert r.status_code == 422


def test_generation_etapes_et_garde_fou(client, project):
    r = client.post(f"/api/projects/{project}/options/OPT-INEXISTANT/edit",
                    json={"op": "move_poteau", "element": "x", "position": [0, 0],
                          "reason": "t"})
    assert r.status_code == 404


def test_edit_justification_et_undo(client, project, option_id):
    # sans raison -> 400
    r = client.post(f"/api/projects/{project}/options/{option_id}/edit",
                    json={"op": "set_dalle_epaisseur", "element": "D1", "epaisseur": 0.24})
    assert r.status_code == 400
    # avec raison -> ok + journal d'édition + undo
    o = client.get(f"/api/projects/{project}/options/{option_id}").json()["option"]
    dalle = o["structure"]["dalles"][0]
    r = client.post(f"/api/projects/{project}/options/{option_id}/edit",
                    json={"op": "set_dalle_epaisseur", "element": dalle["id"],
                          "epaisseur": 0.24, "reason": "test épaisseur"})
    assert r.status_code == 200, r.text
    edits = client.get(f"/api/projects/{project}/options/{option_id}/edits").json()["edits"]
    assert edits and edits[0]["reason"] == "test épaisseur"
    r = client.post(f"/api/projects/{project}/options/{option_id}/undo")
    assert r.status_code == 200
    o2 = client.get(f"/api/projects/{project}/options/{option_id}").json()["option"]
    assert abs(o2["structure"]["dalles"][0]["epaisseur"] - dalle["epaisseur"]) < 1e-6


def test_deliverables_complets(client, project, option_id):
    r = client.post(f"/api/projects/{project}/deliverables",
                    json={"option_id": option_id,
                          "include": ["plans", "note", "quantitatifs", "traacabilite"],
                          "use_ai_drafting": False})
    assert r.status_code == 200, r.text
    job = _wait_job(client, r.json()["job"])
    assert not job.get("error"), job.get("error")
    created = job["result"]["created"]
    types = {c["type"] for c in created}
    assert {"plan_dxf_fondations", "plan_dxf_coffrage", "plan_dxf_ferraillage",
            "note_pdf", "quantitatifs_csv", "traacabilite_pdf"} <= types
    for c in created:
        fr = client.get(f"/api/projects/{project}/deliverables/{c['id']}/file")
        assert fr.status_code == 200 and len(fr.content) > 500, c
    # journal des livrables consultable + hash
    dels = client.get(f"/api/projects/{project}/deliverables").json()["deliverables"]
    assert all(d["sha256"] for d in dels)


def test_journaux_et_documents(client, project):
    assert client.get(f"/api/projects/{project}/ai-calls").json()["calls"] == []
    assert client.get("/api/ai-calls/export").status_code == 200
    assert client.get("/api/documents/client-consent").status_code == 200
    assert client.get("/api/documents/registre").status_code == 200
    prompts = client.get("/api/settings/prompts").json()["prompts"]
    assert len(prompts) >= 3
    assert client.get("/api/incidents").json()["incidents"] == []
