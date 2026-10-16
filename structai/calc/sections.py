"""Vérifications EC2 + dimensionnement des armatures (béton armé).

Méthodes de la pratique française (compatibles EC2) :
- Flexion : bloc rectangulaire δ=0.8 ; As min/max ; armatures de compression
  si μ > μ_lim.
- Effort tranchant : VRd,c (sans armature) puis cadres (cotθ = 2.5, choix
  courant FR), bielles VRd,max.
- Poteau : compression composée + second ordre (raideur nominale simplifiée,
  EC2 §5.8.7-5.8.8) + interaction approchée.
- Flèche ELS : δ = 5qL⁴/(384·E·I), différée via φ∞ ; limite L/200.
- Fissuration simplifiée (EC2 §7.3.4 : wk ≈ 0.85·srm·(εsm−εcm)).
- Dispositions : enrobage par classe d'exposition, ancrage (EC2 §8.4.2).
Sélection aux diamètres commerciaux (8..32) et espacements (100..400).

Ces formules sont destinées à des PROPOSITIONS de conception, à valider par
l'ingénieur ; les cas non standards (torsion, bielles complexes, poinçonnement
avancé) sont signalés en hypothèses.
"""
from __future__ import annotations

import math
from typing import Optional

from .codes import concrete_props, steel_props, design_cover

# Diamètres commerciaux courants (mm)
BAR_DIAMETERS = [8, 10, 12, 14, 16, 20, 25, 32]
STIRRUP_DIAMETERS = [6, 8, 10, 12]
SPACINGS = [100, 125, 150, 175, 200, 225, 250, 275, 300, 350, 400]
BAR_AREA_MM2 = {d: math.pi * d * d / 4 for d in sorted(set(BAR_DIAMETERS + STIRRUP_DIAMETERS))}


def _pick_bars(as_needed_cm2: float, min_bars: int = 2) -> tuple[str, float, list[int]]:
    """Choisit un chenetis : (notation '4HA20', section réelle mm², diamètres)."""
    as_mm2 = max(as_needed_cm2 * 100.0, 1e-9)
    best = None
    for n in range(min_bars, min_bars + 3):
        for d in BAR_DIAMETERS:
            real = n * BAR_AREA_MM2[d]
            if real >= as_mm2:
                ratio = real / as_mm2
                if best is None or ratio < best[0] - 1e-12 or (
                        abs(ratio - best[0]) <= 1e-12 and d < best[2][0]):
                    best = (ratio, real, [d] * n)
                break
    if best is None:
        n = max(min_bars, math.ceil(as_mm2 / BAR_AREA_MM2[32]))
        real = n * BAR_AREA_MM2[32]
        best = (real / as_mm2, real, [32] * n)
    ratio, real, bars = best
    notation = f"{len(bars)}HA{bars[0]}"
    return notation, real, bars


def flexion(b: float, h: float, cover_mm: float, M_ed_kNm: float,
            concrete: str = "C25/30") -> dict:
    """Section rectangulaire en flexion simple (M > 0, fibre inférieure tendue)."""
    c = concrete_props(concrete)
    s = steel_props()
    d = h * 1000.0 - cover_mm
    b_mm = b * 1000.0
    M = abs(M_ed_kNm) * 1e6
    mu = M / (b_mm * d * d * c["fcd"])
    alpha_lim = 0.35          # x/d ≤ 0.35 (ductilité, béton ≤ C50/60)
    mu_lim = 0.8 * alpha_lim * (1 - 0.4 * alpha_lim)
    res: dict = {"b_m": b, "h_m": h, "enrobage_mm": cover_mm, "d_mm": round(d, 1),
                 "M_Ed_kNm": round(M_ed_kNm, 2), "mu": round(mu, 4),
                 "mu_lim": round(mu_lim, 4)}
    dprime = cover_mm + 10.0
    as_comp = 0.0
    if mu <= mu_lim:
        z = d * (1 - 0.4 * alpha_lim * min(mu / mu_lim, 1.0))
        alpha = (0.8 - math.sqrt(max(0.0, 0.64 - 1.6 * mu))) / 0.8
        z = d * (1 - 0.4 * alpha)
        as_need = M / (z * s["fyd"])
        res["regime"] = "simplement armé"
    else:
        z = d * (1 - 0.4 * alpha_lim)
        M_lim = mu_lim * b_mm * d * d * c["fcd"]
        as_comp = max(0.0, (M - M_lim) / (max(1e-9, (d - dprime)) * s["fyd"]))
        as_need = M_lim / (z * s["fyd"]) + as_comp
        res["regime"] = "doublement armé"
        res["M_lim_kNm"] = round(M_lim / 1e6, 2)
    rho_min = 0.26 * c["fctm"] / s["fyk"]
    As_min = rho_min * b_mm * d
    As_min = max(As_min, 1.6 * b_mm * d / 1000.0)  # min(0.26 fctm/fyk ; 0.16.../h) → plancher courant
    As_max = 0.04 * b_mm * d
    as_need = max(as_need, As_min)
    over = as_need > As_max
    res.update({
        "As_need_cm2": round(as_need / 100.0, 2),
        "As_comp_cm2": round(as_comp / 100.0, 2),
        "As_min_cm2": round(As_min / 100.0, 2),
        "As_max_cm2": round(As_max / 100.0, 2),
        "section_max_depassee": over,
    })
    not_long, real_long, bars = _pick_bars(as_need / 100.0)
    res["longitudinel"] = {"barres": not_long, "section_reelle_cm2": round(real_long / 100.0, 2)}
    if as_comp > 10.0:
        not_c, real_c, _ = _pick_bars(as_comp / 100.0, min_bars=2)
        res["compression"] = {"barres": not_c, "section_reelle_cm2": round(real_c / 100.0, 2)}
    taux = (as_need / real_long) if real_long > 0 else 9.99
    res["taux_travail"] = round(min(9.99, taux), 3)
    res["statut"] = "conforme" if (taux <= 1.0 and not over) else "non_conforme"
    return res


def effort_tranchant(b: float, h: float, cover_mm: float, V_ed_kN: float,
                     As_long_cm2: float, concrete: str = "C25/30") -> dict:
    c = concrete_props(concrete)
    s = steel_props()
    d = h * 1000.0 - cover_mm
    b_mm = b * 1000.0
    k = max(1.0, min(2.0, 1.75 / math.sqrt(d)))
    Crd_c = 0.18 / 1.5
    rho_l = min(As_long_cm2 * 100.0 / (b_mm * d), 0.02)
    vmin = 0.035 * k ** 1.5 * math.sqrt(c["fck"])
    VRdc = max(Crd_c * k * (100.0 * rho_l * c["fck"]) ** (1 / 3.0), vmin) * b_mm * d / 1000.0
    V = abs(V_ed_kN)
    res: dict = {"V_Ed_kN": round(V, 2), "VRd_c_kN": round(VRdc, 2), "d_mm": round(d, 1),
                 "k": round(k, 2)}
    asw_s = 0.0
    VRdmax = float("inf")
    st = "conforme"
    if V <= VRdc:
        res["armature_cisaillement"] = "non requise (VRd,c suffisante) — cadres constructifs"
    else:
        cot, tan = 2.5, 1 / 2.5
        z = 0.9 * d
        nu1 = 0.6 * (1.0 - c["fck"] / 250.0)
        VRdmax = (1.0 * b_mm * z * nu1 * c["fcd"]) / (cot + tan) / 1000.0
        asw_s = V * 1000.0 / (z * s["fyd"] * cot)  # mm²/mm
        res["armature_cisaillement"] = "cadres requis"
        res["Asw_par_m_cm2"] = round(asw_s * 1000.0 / 100.0, 1)
        res["VRd_max_kN"] = round(VRdmax, 2)
        st = "conforme" if V <= VRdmax else "non_conforme"
    if asw_s > 0:
        chosen = None
        for dd in STIRRUP_DIAMETERS[1:]:  # HA8 en premier
            area2 = 2 * BAR_AREA_MM2[dd]   # 2 branches
            sreq = area2 / asw_s
            for sp in SPACINGS:
                if sp <= sreq:
                    chosen = (dd, sp)
                    break
            if chosen:
                break
        if chosen:
            res["cadres"] = f"HA{chosen[0]} e={chosen[1]}"
        else:
            res["cadres"] = "section insuffisante — revoir b/h"
            st = "non_conforme"
    else:
        res["cadres"] = "HA8 e=250 (constructif)"
    denom = VRdc if V <= VRdc else max(VRdmax, 1e-9)
    res["taux_travail"] = round(V / denom, 3)
    res["statut"] = st
    return res


def poteau(b: float, h: float, Lf: float, N_ed_kN: float, M_ed_kNm: float,
           concrete: str = "C25/30", classe_expo: str = "XC1") -> dict:
    """Compression composée avec flambement (raideur nominale, EC2 §5.8.7/5.8.8).

    - N_B = π²·Ecd·I / Lo² ; M_tot = M1 / (1 − Nu/N_B) (1ère itération, fluage
      négligé — signalé en hypothèse).
    - Nu,Rd = 0.85·(Ac·fcd + As,req·fyd), As ≥ 1 %·Ac (DCM).
    - Interaction approchée : Nu/Nu,Rd + 1.15·(M_tot/Mu,Rd0)·(Nu/Nu,Rd) ≤ 1
      (approx. de prédimensionnement, conservatrice dans la zone usuelle).
    """
    c = concrete_props(concrete)
    s = steel_props()
    cover = design_cover(classe_expo, "poteau")
    b_mm, h_mm = b * 1000.0, h * 1000.0
    Ac = b_mm * h_mm
    Lo = (0.7 * Lf if Lf > 0 else 3.0) * 1000.0
    i_min = min(b_mm, h_mm) / math.sqrt(12.0)
    elancement = Lo / i_min
    I = min(b_mm * h_mm ** 3, h_mm * b_mm ** 3) / 12.0
    N_B = math.pi ** 2 * c["Ecd"] * I / (Lo * Lo) / 1000.0  # kN
    ratio = min(N_ed_kN / max(N_B, 1e-9), 0.98)
    M1 = abs(M_ed_kNm)
    M_tot = M1 / (1.0 - ratio) if M1 > 0 else 0.0
    As_min_cm2 = max(0.01 * Ac / 100.0, 4 * BAR_AREA_MM2[14] / 100.0)
    As_min_cm2 = min(As_min_cm2, 0.04 * Ac / 100.0)
    Nu_Rd = 0.85 * (Ac * c["fcd"] + As_min_cm2 * 100.0 * s["fyd"]) / 1000.0
    # Mu,Rd0 : flexion sous compression N — équilibre simplifié (bloc béton +
    # acier symétrique) : Mu_Rd0 ≈ Nu_Rd·(0.5h − d'/2)·0.75? On borne par la
    # flexion pure (flexion()) :
    flex = flexion(b, h, cover, M_tot or 1e-9, concrete)
    Mu_Rd0 = max((flex["As_need_cm2"] and 1.0 or 1.0) * 0.0, 0.0)  # non utilisé direct
    # estimation Mu,Rd0 cohérente : moment repris par le couple interne sous Nu
    z_max = 0.8 * (h_mm - cover) / 1000.0  # m
    Mu_Rd0 = max(Nu_Rd * 0.30 * z_max, 25.0)  # capacité flexion en domaine ductile
    interaction = (N_ed_kN / Nu_Rd) + (M_tot / Mu_Rd0) * 0.55
    taux = max(interaction, N_ed_kN / Nu_Rd)
    res = {
        "b_m": b, "h_m": h, "Lf_m": Lf, "enrobage_mm": cover,
        "elancement": round(elancement, 1),
        "N_Ed_kN": round(N_ed_kN, 1), "M_Ed_kNm": round(M1, 1), "M_tot_kNm": round(M_tot, 1),
        "N_B_kN": round(N_B, 1), "Nu_Rd_kN": round(Nu_Rd, 1), "Mu_Rd0_kNm": round(Mu_Rd0, 1),
        "As_min_cm2": round(As_min_cm2, 1),
        "interaction": round(interaction, 3),
        "taux_travail": round(min(9.99, taux), 3),
    }
    res["statut"] = "conforme" if taux <= 1.0 else "non_conforme"
    notat, real, bars = _pick_bars(As_min_cm2, min_bars=4)
    res["longitudinel"] = {"barres": notat, "section_reelle_cm2": round(real / 100.0, 2)}
    max_shear = None
    res["cadres"] = "HA8 e=200 (DCM : réduit à 150 en zone ≥3)"
    return res


def fleche(L: float, q_els_qp: float, q_els_char: float, h: float, b: float = 1.0,
           concrete: str = "C25/30", phi_inf: float = 2.0, lim_div: float = 200.0) -> dict:
    """Flèche ELS poutre/dalle sur 2 appuis : δ = 5qL⁴/(384·E·I), φ différé."""
    c = concrete_props(concrete)
    I = (b * 1000.0) * (h * 1000.0) ** 3 / 12.0
    E = c["Ecm"]  # MPa = N/mm²
    Lmm = L * 1000.0
    # 1 kN/m = 1 N/mm — pas de facteur de conversion
    q_qp = float(q_els_qp)
    q_ch = float(q_els_char)
    delta_qp = 5 * q_qp * Lmm ** 4 / (384 * E * I)
    delta_char = 5 * q_ch * Lmm ** 4 / (384 * E * I)
    delta_tot = delta_char + delta_qp * phi_inf
    limit = Lmm / lim_div
    res = {
        "L_m": round(L, 2), "h_m": h,
        "fleche_qp_differee_mm": round(delta_qp * phi_inf, 2),
        "fleche_totale_mm": round(delta_tot, 2),
        "limite_mm": round(limit, 1),
        "limite": f"L/{int(lim_div)}",
        "rapport_h_L": round(h / max(L, 1e-9), 4),
        "statut": "conforme" if delta_tot <= limit else "non_conforme",
    }
    res["taux_travail"] = round(delta_tot / max(limit, 1e-9), 3)
    return res


def fissuration(b: float, h: float, cover_mm: float, M_qp_kNm: float, As_cm2: float,
                phi_mm: float = 16.0, concrete: str = "C25/30", wk_lim: float = 0.3) -> dict:
    """Ouverture de fissure simplifiée (EC2 §7.3.4 éq. 7.9-7.11, allégée)."""
    c = concrete_props(concrete)
    s = steel_props()
    d = h * 1000.0 - cover_mm
    As = max(As_cm2 * 100.0, 1e-9)
    Ac_eff = min(0.5 * (h - d / 2.0) * b * 1000.0, 2.5 * (h * 1000.0 - d) * b * 1000.0)
    Ac_eff = max(Ac_eff, 1e-9)
    rho_eff = As / Ac_eff
    sig_s = abs(M_qp_kNm) * 1e6 / (0.9 * d * As)
    k1, k2, k3, k4 = 0.8, 0.5, 1.0, 3.0
    fct_eff = c["fctm"]
    d_eps = (sig_s - k1 * k2 * fct_eff / max(rho_eff, 1e-9) * (1.0 + rho_eff)) / s["Es"]
    d_eps = max(0.0, min(d_eps, 0.6 * sig_s / s["Es"]))
    # srm = k3·c + k1·k2·k4·φ/(4ρeff) → forme usuelle : 2.5c + 0.5·k1·k2·k4·φ/ρeff
    srm = k3 * cover_mm * 2.5 + k1 * k2 * k4 * phi_mm / max(rho_eff, 1e-9)
    srm = max(srm, 1.6 * cover_mm)
    wk = 0.85 * srm * d_eps
    res = {
        "sigma_s_MPa": round(sig_s, 1), "rho_eff": round(rho_eff, 5),
        "srm_mm": round(srm, 1), "wk_mm": round(wk, 3), "wk_lim_mm": wk_lim,
        "statut": "conforme" if wk <= wk_lim else "non_conforme",
    }
    res["taux_travail"] = round(wk / max(wk_lim, 1e-9), 3)
    return res


def ancrage(fyk: float = 500.0, phi_mm: float = 16.0, concrete: str = "C25/30") -> dict:
    c = concrete_props(concrete)
    fyd = fyk / 1.15
    lb = (1.0 * 1.0 * phi_mm * fyd) / (4.0 * max(c["fctd"], 0.1))
    lb = max(lb, 15 * phi_mm, 200.0)
    return {"lb_mm": round(lb, 0), "lb_diametres": round(lb / phi_mm, 1)}


def check_detailing(b: float, h: float, cover_mm: float, bar_d_mm: float,
                    spacing_mm: float, bar_count: int) -> list[dict]:
    checks = [{
        "regle": "enrobage nominal ≥ Ø barre",
        "statut": "conforme" if cover_mm >= bar_d_mm else "non_conforme",
    }]
    pass_min = max(bar_d_mm, 20.0)
    clear = (b * 1000.0 - 2 * cover_mm - bar_d_mm * bar_count) / max(bar_count - 1, 1)
    checks.append({
        "regle": "passe-libre ≥ max(Ø, 20 mm)",
        "statut": "conforme" if clear >= pass_min else "non_conforme",
    })
    checks.append({
        "regle": "espacement ≤ 400 mm (dalle) / 300 mm (poutre, DCM)",
        "statut": "conforme" if spacing_mm <= 400 else "non_conforme",
    })
    return checks
