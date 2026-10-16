"""Moteur FE + générateur : reproductibilité, conformité, non-nullité des
sollicitations ELS. (Écart < 2 % vs calcul main couvert par test_calc_sections.)"""
import copy

import pytest

from conftest import INTERP, PROJ_PARAMS


def _gen(seed):
    from structai.gen.generator import generate_options
    proj = dict(PROJ_PARAMS, seed=seed, id="T")
    gen = {"max_options_calculees": 6, "portee_min_m": 3.2, "portee_max_m": 6.5,
           "epaisseurs_dalle_m": [0.18, 0.20, 0.22]}
    return generate_options(copy.deepcopy(INTERP), proj, gen)


@pytest.mark.slow
def test_seed_reproductible():
    a = _gen(42)
    b = _gen(42)
    assert a["index"]["seed"] == b["index"]["seed"] == 42
    ia = [(o["description_courte"], o["rank"], o["indicateurs"]["taux_travail_max"])
          for o in a["options"]]
    ib = [(o["description_courte"], o["rank"], o["indicateurs"]["taux_travail_max"])
          for o in b["options"]]
    assert ia == ib


@pytest.mark.slow
def test_au_moins_3_options_conformes():
    out = _gen(7)
    assert out["index"]["nombre_options_presentees"] >= 3, out.get("diagnostic")
    for o in out["options"]:
        assert all(v in ("conforme", "non_requis") for v in o["conformite"].values()), o["conformite"]


@pytest.mark.slow
def test_indicateurs_non_nuls():
    out = _gen(42)
    assert out["options"], out.get("diagnostic")
    o = out["options"][0]
    ind = o["indicateurs"]
    assert ind["volume_beton_m3"] > 1.0
    assert ind["masse_acier_kg"] > 10.0
    assert 0 < ind["taux_travail_max"] <= 1.0
    verifs = o["resultats_calcul"]["verifications"]
    fleches = [v for v in verifs if v["verification"] == "fleche"]
    assert fleches and any(v["valeur_mm"] > 0 for v in fleches), "flèches doivent être non nulles"
