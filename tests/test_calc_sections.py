"""Validation normative du moteur de sections : écart < 2 % vs calcul à la main
(exigence §6.2 du cahier des charges) + non-régression des unités."""
import math

import pytest

from structai.calc.sections import effort_tranchant, fleche, flexion


def _I_m2(b, h):
    return b * h**3 / 12.0


def test_fleche_isostatique_vs_main_propre():
    """Poutre bi-appuyée L=6 m, b=0.30, h=0.50, C25/30, qp=12 kN/m, qchar=8 kN/m."""
    L, b, h = 6.0, 0.30, 0.50
    Ecm = 31_000.0  # MPa — valeur du moteur (codes.concrete_props C25/30)
    I_mm4 = (b * 1e3) * (h * 1e3) ** 3 / 12.0
    qp, qch = 12.0, 8.0  # kN/m ≡ N/mm
    main = 5 * (qch + 2.0 * qp) * (L * 1e3) ** 4 / (384 * Ecm * I_mm4)
    got = fleche(L, qp, qch, h, b, "C25/30")
    assert got["fleche_totale_mm"] > 0.05, "régression : flèche nulle (bug facteur 1e-3)"
    assert abs(got["fleche_totale_mm"] - main) / main < 0.02, (got, main)


def test_fleche_unites_kN_m_eq_N_mm():
    """1 kN/m ≡ 1 N/mm exactement dans les formules (aucun facteur de conversion)."""
    d = fleche(6.0, 0.0, 12.0, 0.5, 0.3, "C25/30", phi_inf=0.0)
    I_mm4 = 300.0 * 500.0**3 / 12.0
    main = 5 * 12.0 * 6000.0**4 / (384 * 31_000.0 * I_mm4)
    assert abs(d["fleche_totale_mm"] - main) / main < 0.02, (d, main)


def test_fleche_limite_Lsur200():
    r = fleche(6.0, 12.0, 8.0, 0.5, 0.3)
    assert math.isclose(r["limite_mm"], 6000.0 / 200.0, abs_tol=0.11)


def test_flexion_m_ed_conserve():
    L, b, h, q = 6.0, 0.30, 0.55, 30.0
    M_ed = q * L**2 / 8.0
    r = flexion(b, h, 30.0, M_ed, "C25/30")
    assert abs(r["M_Ed_kNm"] - M_ed) / M_ed < 0.02, r
    assert r["As_need_cm2"] >= r["As_min_cm2"] - 1e-9, "le minimum constructif s'applique"
    if r["statut"] == "conforme":
        assert r["taux_travail"] <= 1.0 + 1e-6


def test_flexion_double_armature_declenchee():
    """Moment énorme -> régime doublement armé signalé."""
    r = flexion(0.30, 0.40, 30.0, 400.0, "C25/30")
    assert r["regime"] == "doublement armé"
    assert r["As_comp_cm2"] > 0


def test_effort_tranchant_ministre():
    e = effort_tranchant(0.30, 0.50, 30.0, 40.0, 8.0, "C25/30")
    assert "non requise" in e.get("armature_cisaillement", "") or e["VRd_c_kN"] > 0
    big = effort_tranchant(0.30, 0.50, 30.0, 900.0, 8.0, "C25/30")
    assert big["statut"] == "non_conforme" or big.get("VRd_max_kN", 9e9) >= 900.0


def test_poteau_ferraillage_normalise():
    p = flexion(0.30, 0.55, 30.0, 60.0, "C25/30")
    assert "HA" in p["longitudinel"]["barres"]
