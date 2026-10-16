"""Livrables : DXF ouvrables/relu par ezdxf, totaux quantitatifs vérifiables,
PDF valides (génération locale, sans IA)."""
import csv
import io
from pathlib import Path

import ezdxf
import pytest

from conftest import INTERP, PROJ_PARAMS


@pytest.fixture(scope="module")
def gen_option():
    from structai.gen.generator import generate_options
    out = generate_options(dict(INTERP), dict(PROJ_PARAMS, id="TX", seed=11),
                           {"max_options_calculees": 3, "portee_min_m": 3.2,
                            "portee_max_m": 6.5, "epaisseurs_dalle_m": [0.20]})
    assert out["options"], out.get("diagnostic")
    o = out["options"][0]
    o.setdefault("meta", {})["emprise"] = {"x0": 0, "y0": 0, "x1": 12.0, "y1": 9.0}
    return o


def test_dxf_plans_rechargeables(gen_option, tmp_path):
    from structai.export.dxf_plans import plan_coffrage, plan_ferraillage, plan_fondations
    em = gen_option["meta"]["emprise"]
    infos = {"projet": "test", "date": "2026-01-01", "option": "OPT-TEST", "plan": "x"}
    for name, fn in [("fondations", plan_fondations), ("coffrage", plan_coffrage),
                     ("ferraillage", plan_ferraillage)]:
        out = tmp_path / f"{name}.dxf"
        fn(gen_option, em, out, dict(infos, plan=name))
        doc = ezdxf.readfile(str(out))
        msp = doc.modelspace()
        assert doc.dxfversion >= "AC1021"
        assert len(list(msp)) > 10, name
        layers = {e.dxf.layer for e in msp}
        assert layers <= {l.dxf.name for l in doc.layers}


def test_quantites_totaux_coherents(gen_option):
    from structai.export.quantities import quantities_rows
    rows = quantities_rows(gen_option, PROJ_PARAMS)
    lignes = [r for r in rows if not str(r.get("Detail", "")).startswith("TOTAL")]
    totaux = [r for r in rows if str(r.get("Detail", "")).startswith("TOTAL")]
    sums = {}
    for r in lignes:
        sums[r["Categorie"]] = sums.get(r["Categorie"], 0.0) + float(r["Quantite"])
    assert len(totaux) >= 3
    for t in totaux:
        assert abs(t["Quantite"] - sums.get(t["Categorie"], -1)) < 0.05, t
    cat = {c: sums.get(c, 0) for c in ("Béton", "Acier", "Coffrage")}
    assert cat["Béton"] > 10 and cat["Acier"] > 100 and cat["Coffrage"] > 10, cat


def test_export_csv_encodage(gen_option, tmp_path):
    from structai.export.quantities import export_csv, quantities_rows
    out = tmp_path / "q.csv"
    export_csv(quantities_rows(gen_option, PROJ_PARAMS), out)
    txt = out.read_text(encoding="utf-8-sig")
    assert ";" in txt and "TOTAL" in txt


def test_note_calcul_pdf(gen_option, tmp_path):
    from structai.export.pdf_docs import note_de_calcul
    out = tmp_path / "note.pdf"
    note_de_calcul(out, {"name": "Projet test", "params": PROJ_PARAMS}, gen_option,
                   None, None, None)
    data = out.read_bytes()
    assert data.startswith(b"%PDF")
    assert len(data) > 8000
    assert data.rstrip().endswith(b"%%EOF")
    import re
    m = re.search(rb"/Count (\d+)", data)
    assert m and int(m.group(1)) >= 6, "note de calcul : ≥ 6 pages (11 sections)"


def test_rapport_tracabilite_pdf(tmp_path):
    from structai.export.pdf_docs import rapport_tracabilite
    out = tmp_path / "trac.pdf"
    rapport_tracabilite(out, {"id": "P1", "name": "test", "params": {}},
                       [{"filename": "a.dxf", "sha256": "ab" * 32, "dxf_version": "AC1027",
                         "imported_at": "2026-01-01", "entities_count": 10,
                         "anonymization_ok": 1}],
                       [{"id": "I1", "source": "manuel", "validated": 1,
                         "created_at": "2026-01-01"}],
                       {"seed": 1, "options_presentees": []}, [],
                       [{"datetime": "2026-01-01", "provider": "anthropic", "model": "m",
                         "purpose": "p", "tokens_in": 1, "tokens_out": 1, "cost_usd": 0.1,
                         "hash_req": "h1", "hash_resp": "h2", "status": "succes",
                         "latency_s": 1.0}], [])
    data = out.read_bytes()
    assert data.startswith(b"%PDF") and len(data) > 3000


def test_registre_traitements(tmp_path):
    from structai.export.pdf_docs import registre_traitements
    out = registre_traitements(tmp_path / "reg.pdf")
    assert Path(out).exists() and out.read_bytes().startswith(b"%PDF")


