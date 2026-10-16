"""Fixtures pytest — data dir isolée par session, client TestClient."""
import os
import sys
import tempfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

_tmp = tempfile.mkdtemp(prefix="structai_test_")
os.environ["STRUCTAI_DATA"] = _tmp
os.environ["STRUCTAI_NO_BROWSER"] = "1"


@pytest.fixture(scope="session")
def data_dir() -> Path:
    return Path(_tmp)


@pytest.fixture(scope="session")
def client():
    from fastapi.testclient import TestClient
    from structai.api import create_app
    app = create_app()
    with TestClient(app) as c:
        yield c


INTERP = {
    "meta": {"source": "test"},
    "batiment": {"niveaux": 3, "hauteur_etage": 2.8,
                 "emprise": {"largeur": 12.0, "profondeur": 9.0, "forme": "rectangle"}},
    "murs_porteurs": [
        {"id": "MP1", "debut": [0, 0], "fin": [12, 0], "epaisseur": 0.2,
         "niveaux": [1, 2, 3], "confiance": 0.9},
        {"id": "MP2", "debut": [0, 9], "fin": [12, 9], "epaisseur": 0.2,
         "niveaux": [1, 2, 3], "confiance": 0.9},
        {"id": "MP3", "debut": [0, 0], "fin": [0, 9], "epaisseur": 0.2,
         "niveaux": [1, 2, 3], "confiance": 0.8},
        {"id": "MP4", "debut": [12, 0], "fin": [12, 9], "epaisseur": 0.2,
         "niveaux": [1, 2, 3], "confiance": 0.8}],
    "ouvertures": [{"id": "O1", "type": "porte", "largeur": 0.9, "mur": "MP3"}],
    "incertitudes": [{"id": "U1", "description": "test", "impact": "faible"}],
}

PROJ_PARAMS = {
    "type_batiment": "R+2", "niveaux": 3, "hauteur_etage": 2.8, "usage": "habitation",
    "zone_sismique": 3, "zone_neige": "C1", "zone_vent": 3, "altitude": 150,
    "materiaux": ["beton_arme"], "seed": 42, "nb_options": 4,
    "critere_classement": "masse_acier",
}


@pytest.fixture(scope="session")
def project(client):
    r = client.post("/api/projects", json={"name": "Projet test", "ref": "T-1",
                                           "params": PROJ_PARAMS})
    assert r.status_code == 200, r.text
    pid = r.json()["id"]
    # interprétation manuelle validée
    r = client.post(f"/api/projects/{pid}/interpretations/manual",
                    json={"json": INTERP})
    assert r.status_code == 200, r.text
    iid = r.json()["interpretation_id"]
    r = client.put(f"/api/projects/{pid}/interpretations/{iid}",
                   json={"json": INTERP, "validation": {
                       "statut": "validee", "corrections": [],
                       "incertitudes_traitees": [{"id": "U1", "decision": "acceptee",
                                                  "raison": "test"}]}})
    assert r.status_code == 200, r.text
    return pid


@pytest.fixture(scope="session")
def option_id(client, project):
    import time
    r = client.post(f"/api/projects/{project}/generate",
                     json={"use_ai": False, "seed": 42})
    assert r.status_code == 200, r.text
    jid = r.json()["job"]
    t0 = time.time()
    while time.time() - t0 < 300:
        j = client.get(f"/api/jobs/{jid}").json()
        if j.get("done"):
            break
        time.sleep(0.5)
    assert j.get("done") and not j.get("error"), str(j.get("error"))[:300]
    assert j["result"]["nb_presentees"] >= 3
    opts = client.get(f"/api/projects/{project}/options").json()["options"]
    return client.get(f"/api/projects/{project}/options").json()["options"][0]["id"]
