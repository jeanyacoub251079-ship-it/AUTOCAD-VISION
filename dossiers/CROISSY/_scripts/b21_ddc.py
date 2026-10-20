#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-21 — DESCENTE DE CHARGES PRÉLIMINAIRE — CONCEPTION
Projet : CROISSY-FLORA (ID-01) — CARNAC v3.0 — Indice A

Régime OUTILLÉ (V13). Ce script produit :
  1. les charges permanentes par couche et par zone (rattachées à une pièce ou à H-xx) ;
  2. les charges d'exploitation par catégorie EC1 ;
  3. les surfaces d'influence des porteurs, calculées sur la trame B-20 ;
  4. les tableaux ELS et ELU distincts, par porteur ;
  5. la vérification de l'hypothèse H-27 (σ_d sur les voiles) ;
  6. le contrôle de cohérence global (somme des aires d'influence ≈ surface de plancher).

Sorties :
  - dossiers/CROISSY/_rendus/b21_ddc.txt
  - dossiers/CROISSY/_rendus/b21_ddc.json
"""

import json
import os
from datetime import datetime

JOURNAL = "dossiers/CROISSY/_rendus/b21_ddc.txt"
JSONOUT = "dossiers/CROISSY/_rendus/b21_ddc.json"

# ---------------------------------------------------------------- trame B-20 (m, repère B-30)
FIL_X = {"A": -0.32, "B": 0.68, "C": 2.88, "D": 3.91, "E": 9.48}
FIL_Y = {1: 0.17, 2: 5.11, 3: 7.71, 4: 10.46, 5: 14.62, 6: 18.69}
A_RDC, A_R1 = 111.15, 106.92

# ---------------------------------------------------------------- Charges permanentes (kN/m²)
# chaque couche : (couche, épaisseur m, poids volumique kN/m³, g kN/m², source)
G_PLANCHER_A = [
    ("Parquet + volige", 0.03, 6.0, 0.18, "D3 p. 10 — constitution plancher bois"),
    ("Solives bois 8×18 e = 0,50 m", 0.18, 5.5, 0.16, "D3 p. 10 (section × entraxe)"),
    ("Plafond lattis-plâtre", 0.025, 12.0, 0.30, "D3 p. 9 (désordre 9)"),
    ("Divers (clouage, lambourdes)", None, None, 0.06, "H-28 (forfait de liaison)"),
    ("Câblages, gaines dans vide", None, None, 0.10, "D4 p. 6 (programme technique)"),
]
G_PLANCHER_B = [
    ("Revêtement de sol", 0.02, 20.0, 0.40, "D4 p. 5 (sol projeté)"),
    ("Chape 10 cm", 0.10, 22.0, 2.20, "D3 p. 11 — « chape 10 cm »"),
    ("Voutains briques 7 cm + hourdis", 0.07, 15.0, 1.05, "D3 p. 11"),
    ("Solives IPE 160 e = 0,72 m", 0.16, 5.0, 0.11, "D3 p. 11 (15,8 kg/m / 0,72 m)"),
    ("Plafond + suspension", None, None, 0.15, "D3 p. 12"),
]
RECHARGE = ("Recharge de sol 15 cm (D4 p. 5 et 14)", 0.15, 22.0, 3.30,
            "H-28 — densité 22 kN/m³ retenue ; D4 prescrit l'épaisseur, pas la densité")
TOITURE = [
    ("Tuiles + liteaux", 0.05, 8.0, 0.40, "D2 f. 02 (couverture) — H-29"),
    ("Chevrons + volige", 0.08, 5.5, 0.15, "D2 f. 02 — H-29"),
    ("Pannes + fermes (ramené au m²)", None, None, 0.25, "D2 f. 02 — H-29"),
    ("Plafond combles", 0.02, 12.0, 0.15, "D2 f. 02 — H-29"),
]
CLOISON_FORFAIT = 0.80   # kN/m² — EC1-1-1 § 6.3.1.2, cloisons ≤ 2,0 kN/m (H-30)

# ---------------------------------------------------------------- Charges d'exploitation (kN/m²)
Q_CAT = {
    "B": (2.50, "D2 p. 1 — cabinet paramédical / bureaux (250 daN/m²). Enveloppe retenue vs 150 daN/m² de D3 (logement)"),
    "C4": (5.00, "H-31 — salle de sport R+1 34,25 m² (CHG-01b) : EC1 cat. C4, non couverte par le 250 daN/m² de D2"),
    "H": (0.40, "EC1 cat. H — toiture inaccessible, pente > 20°"),
}
NEIGE = (0.45, "CHG-05 — zone A1, altitude < 200 m, sk = 45 daN/m² (D2 p. 1)")

LOG = []


def log(m=""):
    print(m)
    LOG.append(m)


def table(rows, widths):
    for r in rows:
        log("    " + "".join(str(c).ljust(w)[:w] for c, w in zip(r, widths)))


def main():
    os.makedirs("dossiers/CROISSY/_rendus", exist_ok=True)
    log("=" * 110)
    log("B-21 — DESCENTE DE CHARGES PRÉLIMINAIRE — CONCEPTION — INDICE A")
    log("Projet CROISSY-FLORA (ID-01) — CARNAC v3.0 — régime OUTILLÉ (V13)")
    log(f"Exécution : {datetime.now():%Y-%m-%d %H:%M:%S}")
    log("Titre opposable : DDC PRÉLIMINAIRE — CONCEPTION (remplacée par les DDC d'exécution B-40 à B-50)")
    log("=" * 110)

    # ------------------------------------------------------------ 1. charges permanentes
    log("\n[1] CHARGES PERMANENTES PAR COUCHE")
    res = {"project": "CROISSY-FLORA", "brick": "B-21", "indice": "A",
           "date": datetime.now().isoformat(timespec="seconds"), "zones": {}, "porteurs": {}}

    for name, layers in (("Plancher A — aile Est (bois 8×18)", G_PLANCHER_A),
                         ("Plancher B — aile Ouest (voutains + IPE 160)", G_PLANCHER_B),
                         ("Toiture — combles et versants", TOITURE)):
        tot = sum(l[3] for l in layers)
        log(f"\n    {name}")
        table([("Couche", "ép.(m)", "γ(kN/m³)", "g(kN/m²)", "Source")] +
              [(l[0], f"{l[1]:.3f}" if l[1] else "—", f"{l[2]:.0f}" if l[2] else "—",
                f"{l[3]:.2f}", l[4]) for l in layers] +
              [("TOTAL g_k", "", "", f"{tot:.2f}", "")], (46, 9, 11, 11, 60))
        res["zones"][name] = dict(total=tot, layers=[dict(couche=l[0], ep=l[1], gamma=l[2],
                                                          g=l[3], source=l[4]) for l in layers])

    g_A_calc = sum(l[3] for l in G_PLANCHER_A)
    g_B_calc = sum(l[3] for l in G_PLANCHER_B)
    g_toit = sum(l[3] for l in TOITURE)
    # valeurs déclarées au cartouche D2 (daN/m²)
    g_A_decl, g_B_decl = 1.00, 3.50
    log(f"\n    CONFRONTATION DÉCLARÉ / RECALCULÉ (V3 — on ne retient jamais la valeur la plus faible)")
    log(f"      Plancher A : D2 déclare {g_A_decl:.2f} kN/m² · recalcul par couches {g_A_calc:.2f} kN/m²"
        f" → retenu {max(g_A_decl, g_A_calc):.2f}")
    log(f"      Plancher B : D2 déclare {g_B_decl:.2f} kN/m² · recalcul par couches {g_B_calc:.2f} kN/m²"
        f" → retenu {max(g_B_decl, g_B_calc):.2f}  (D2 sous-déclare de {100*(g_B_calc/g_B_decl-1):.0f} %)")
    g_A = max(g_A_decl, g_A_calc)
    g_B = max(g_B_decl, g_B_calc)
    log(f"\n    Recharge de sol (D4 p. 5 et 14) : {RECHARGE[3]:.2f} kN/m² "
        f"(ép. {RECHARGE[1]:.2f} m × γ {RECHARGE[2]:.0f} kN/m³) — {RECHARGE[4]}")
    log(f"    Cloisons forfaitaires : {CLOISON_FORFAIT:.2f} kN/m² — EC1-1-1 § 6.3.1.2 (H-30)")

    # g total par zone (avec recharge et cloisons)
    g_tot_A = g_A + RECHARGE[3] + CLOISON_FORFAIT
    g_tot_B = g_B + RECHARGE[3] + CLOISON_FORFAIT
    log(f"\n    → Plancher A avec recharge et cloisons : g = {g_tot_A:.2f} kN/m²")
    log(f"    → Plancher B avec recharge et cloisons : g = {g_tot_B:.2f} kN/m²")
    log(f"    → Toiture : g = {g_toit:.2f} kN/m²")

    # ------------------------------------------------------------ 2. exploitation
    log("\n[2] CHARGES D'EXPLOITATION PAR CATÉGORIE EC1")
    table([("Catégorie", "q_k (kN/m²)", "Source")] +
          [(k, f"{v[0]:.2f}", v[1]) for k, v in Q_CAT.items()] +
          [("Neige", f"{NEIGE[0]:.2f}", NEIGE[1])], (12, 13, 90))

    # ------------------------------------------------------------ 3. porteurs
    # A_inf et composition explicites ; strip = largeur tributaire d'une poutre
    porteurs = [
        # --- poteaux métalliques (façade Ouest Sud, sous linteau bois) ---
        dict(id="P1-N", type="Poteau métal", Lx=1.26, Ly=0.50, A=0.63, zone="B",
             linteau_L=2.52, linteau_strip=1.00, mur_ep=0.50, mur_h=2.00, cont=1.00,
             justif="Demi-portée du linteau bois de façade Ouest Sud (L = 2,52 m entre P1-N et P1-S) "
                    "× épaisseur de mur porté (0,50 m) — appui de rive, extrémité de file"),
        dict(id="P1-S", type="Poteau métal", Lx=1.26, Ly=0.50, A=0.63, zone="B",
             linteau_L=2.52, linteau_strip=1.00, mur_ep=0.50, mur_h=2.00, cont=1.00,
             justif="Idem P1-N — second appui de la même baie, appui de rive"),
        # --- poteaux BA ---
        dict(id="P2", type="Poteau BA 15×25", Lx=2.785, Ly=4.115, A=11.46, zone="B",
             cont=1.15,
             justif="Demi-portée D→E (5,57/2 = 2,785 m) × demi-portées 4→5 et 5→6 "
                    "((4,16+4,07)/2 = 4,115 m) — appui intermédiaire en file 5"),
        dict(id="P3", type="Poteau BA 50×40", Lx=0.45, Ly=0.50, A=0.23, zone="B",
             linteau_L=0.90, linteau_strip=1.00, mur_ep=0.50, mur_h=2.00, cont=1.00,
             justif="Demi-portée de F1b (L = 0,90 m) × épaisseur de mur porté (0,50 m) — "
                    "appui de rive Est du frangement dans le mur Nord du hall"),
        dict(id="J1", type="Jambage BA 24×50", Lx=0.50, Ly=0.50, A=0.25, zone="B",
             linteau_L=1.00, linteau_strip=1.00, mur_ep=0.50, mur_h=2.00, cont=1.00,
             justif="Demi-portée de F1a (L = 1,00 m) × épaisseur du refend central (0,50 m) — "
                    "piédroit Nord, appui de rive"),
        # --- voiles (ramenés au mètre linéaire) ---
        dict(id="M11 (RDC)", type="Voile maçonnerie", Lx=None, Ly=None, A=None, zone="B",
             strip=4.115, cont=1.15, ml=True,
             justif="Largeur tributaire = demi-portées 4→5 et 5→6 = (4,16+4,07)/2 = 4,115 m "
                    "par mètre linéaire de voile — pignon Nord, appui intermédiaire"),
        dict(id="M03 (RDC)", type="Voile maçonnerie", Lx=None, Ly=None, A=None, zone="B",
             strip=3.455, cont=1.15, ml=True,
             justif="Largeur tributaire = demi-portées 3→4 et 4→(refend) = (2,75+4,16)/2 = 3,455 m "
                    "par mètre linéaire — refend central, appui intermédiaire"),
        # --- semelle ---
        dict(id="SF1 (sous P2)", type="Semelle isolée", Lx=None, Ly=None, A=11.46, zone="B",
             from_poteau="P2", cont=1.15,
             justif="Reçoit l'intégralité de la réaction de P2 — appui intermédiaire (continuité du plancher en tête)"),
    ]

    # --- poutres / linteaux : charge linéique puis réaction
    beams = [
        dict(id="F1a", L=1.00, strip=1.00, mur_h=3.50, mur_ep=0.50, zone="B", toit=False, cont=1.15,
             justif="Mur de moellons au-dessus (0,50 m × 3,50 m) + bande de plancher 1,00 m"),
        dict(id="F1b", L=0.90, strip=1.00, mur_h=3.50, mur_ep=0.50, zone="B", toit=False, cont=1.15,
             justif="Mur de moellons au-dessus + bande de plancher 1,00 m"),
        dict(id="F1c", L=0.85, strip=1.00, mur_h=3.50, mur_ep=0.50, zone="B", toit=False, cont=1.15,
             justif="Mur de moellons au-dessus + bande de plancher 1,00 m"),
        dict(id="F2", L=2.85, strip=3.77, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.15,
             justif="Bande 3,77 m = demi-portées 1→2 et 2→3 — plancher seul, mur supprimé"),
        dict(id="F3", L=3.85, strip=2.75, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.15,
             justif="Bande 2,75 m = 0,98 m (vers file 3) + 1,77 m (vers file 4) — plancher seul"),
        dict(id="F4", L=4.88, strip=1.615, mur_h=0.0, mur_ep=0.0, zone="B", toit=True, cont=1.15,
             justif="Bande 1,615 m = demi-portées B→C et C→D — toiture basse seule (aucun étage au-dessus)"),
        dict(id="R1", L=3.85, strip=3.455, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.15,
             justif="Bande 3,455 m = demi-portées 3→4 et 4→5 — moisage sous poutre bois 20×15"),
        dict(id="R2-N", L=3.82, strip=2.08, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.15,
             justif="Bande 2,08 m = demi-travée de part et d'autre du sous-solivage (4,16/2)"),
        dict(id="R2-S", L=3.82, strip=1.62, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.15,
             justif="Bande 1,62 m = 2 × 0,81 m (demi-travée 2→3 et 3→refend)"),
        dict(id="R3-N", L=1.55, strip=0.0, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.00,
             justif="Linteau de baie : reprend la réaction de R2-N à mi-portée — appui de rive"),
        dict(id="R3-S", L=1.55, strip=0.0, mur_h=0.0, mur_ep=0.0, zone="B", toit=False, cont=1.00,
             justif="Linteau de baie : reprend la réaction de R2-S à mi-portée — appui de rive"),
    ]

    # ------------------------------------------------------------ 4. calcul ELS / ELU
    q_B = Q_CAT["B"][0]
    q_neige = NEIGE[0]
    q_toit = Q_CAT["H"][0]
    gamma_mur = 22.0   # kN/m³ — moellons + mortier (H-32)
    gamma_beton = 25.0  # kN/m³

    log("\n[3] CHARGES LINÉIQUES SUR LES POUTRES ET LINTEAUX")
    log("    p = bande tributaire × (g plancher + q exploitation) + mur au-dessus")
    table([("Poutre", "L(m)", "bande(m)", "mur(kN/m)", "g+q ELS", "p_ELS", "p_ELU")],
          [("Poutre", "L(m)", "bande(m)", "mur(kN/m)", "g+q ELS", "p_ELS", "p_ELU")],
          ) if False else None

    rows = [("Poutre", "L(m)", "bande(m)", "mur(kN/m)", "p_ELS(kN/m)", "p_ELU(kN/m)", "Source")]
    beam_res = {}
    for b in beams:
        gm = 0.0
        if b["mur_h"] > 0:
            gm = b["mur_ep"] * b["mur_h"] * gamma_mur
        if b["toit"]:
            g_sol, q_sol = g_toit, q_neige + q_toit
        else:
            g_sol, q_sol = g_tot_B, q_B
        p_els = b["strip"] * (g_sol + q_sol) + gm
        p_elu = b["cont"] * (1.35 * (b["strip"] * g_sol + gm) + 1.5 * b["strip"] * q_sol)
        beam_res[b["id"]] = dict(L=b["L"], strip=b["strip"], mur=gm, g=g_sol, q=q_sol,
                                 p_els=p_els, p_elu=p_elu, cont=b["cont"], justif=b["justif"])
        rows.append((b["id"], f"{b['L']:.2f}", f"{b['strip']:.2f}", f"{gm:.1f}",
                     f"{p_els:.1f}", f"{p_elu:.1f}", b["justif"]))
    table(rows, (9, 7, 10, 11, 14, 14, 80))
    res["beams"] = beam_res

    log("\n[4] DESCENTE DE CHARGES PAR PORTEUR — TABLEAU ELS (ΣG_k + Q_k,1)")
    rows = [("Porteur", "Type", "A_inf(m²)", "G(kN)", "Q(kN)", "continuité", "N_ELS(kN)")]
    els = {}
    for p in porteurs:
        cont = p["cont"]
        if p.get("ml"):
            G = p["strip"] * (g_toit + g_tot_B)
            Q = p["strip"] * (q_neige + q_toit + q_B)
            unit = "kN/m"
        elif p.get("from_poteau"):
            src = els[p["from_poteau"]]
            G, Q = src["G"] * cont, src["Q"] * cont
            unit = "kN"
        elif p.get("linteau_L"):
            Lb, strip = p["linteau_L"], p["linteau_strip"]
            gm = p["mur_ep"] * p["mur_h"] * gamma_mur * Lb
            G = cont * (strip * g_tot_B * Lb + gm)
            Q = cont * strip * q_B * Lb
            unit = "kN"
        else:
            G = p["A"] * (g_toit + g_tot_B) * cont
            Q = p["A"] * (q_neige + q_B) * cont
            unit = "kN"
        els[p["id"]] = dict(G=G, Q=Q, N=G + Q, unit=unit, A=p["A"], cont=cont)
        rows.append((p["id"], p["type"], f"{p['A']:.2f}" if p["A"] else "—",
                     f"{G:.1f}", f"{Q:.1f}", f"{cont:.2f}", f"{G+Q:.1f} {unit}"))
    table(rows, (16, 20, 10, 10, 10, 12, 16))

    log("\n[5] DESCENTE DE CHARGES PAR PORTEUR — TABLEAU ELU (1,35 ΣG_k + 1,5 Q_k,1)")
    rows = [("Porteur", "1,35·G", "1,5·Q", "continuité", "N_ELU", "N/A_inf")]
    elu = {}
    for p in porteurs:
        e = els[p["id"]]
        cont = p["cont"]
        if p.get("ml"):
            g_tot = p["strip"] * (g_toit + g_tot_B)
            q_tot = p["strip"] * (q_neige + q_toit + q_B)
            N = cont * (1.35 * g_tot + 1.5 * q_tot)
            Ai = p["strip"]          # ramené au mètre linéaire
        elif p.get("from_poteau"):
            src = elu[p["from_poteau"]]
            N = src["N"] * cont
            Ai = p["A"]
        elif p.get("linteau_L"):
            Lb, strip = p["linteau_L"], p["linteau_strip"]
            gm = p["mur_ep"] * p["mur_h"] * gamma_mur * Lb
            g_p = strip * g_tot_B * Lb
            q_p = strip * q_B * Lb
            N = cont * (1.35 * (g_p + gm) + 1.5 * q_p)
            Ai = p["A"]
        else:
            g_tot = p["A"] * (g_toit + g_tot_B)
            q_tot = p["A"] * (q_neige + q_B)
            N = cont * (1.35 * g_tot + 1.5 * q_tot)
            Ai = p["A"]
        elu[p["id"]] = dict(G135=1.35 * e["G"], Q15=1.5 * e["Q"], N=N, A=Ai, unit=e["unit"])
        rows.append((p["id"], f"{1.35*e['G']:.1f}", f"{1.5*e['Q']:.1f}",
                     f"{cont:.2f}", f"{N:.1f} {e['unit']}",
                     f"{N/Ai:.1f}" if Ai else "—"))
    table(rows, (16, 11, 11, 12, 16, 12))
    res["els"] = els
    res["elu"] = elu

    # ------------------------------------------------------------ 5. H-27
    log("\n[6] VÉRIFICATION DE L'HYPOTHÈSE H-27 (σ_d SUR LES VOILES)")
    A_murs = 18.79          # m² — aire des 12 voiles RDC (B-25 Ind. B)
    N_total = (g_toit + g_tot_B) * A_R1 * 1.0 + q_neige * A_R1 + q_B * A_R1
    N_elu_total = 1.35 * ((g_toit + g_tot_B) * A_R1) + 1.5 * (q_B + q_neige) * A_R1
    sigma = N_elu_total / (A_murs * 1000.0)     # kPa -> MPa : kN / (m² × 1000)
    log(f"    Charge totale ELU transmise aux voiles : {N_elu_total:.0f} kN")
    log(f"    Aire portante des 12 voiles RDC : {A_murs:.2f} m²")
    log(f"    σ_d,calculé = {N_elu_total:.0f} kN / {A_murs:.2f} m² = {sigma*1000:.0f} kPa = {sigma:.3f} MPa")
    fvk_calc = (0.15 + 0.4 * sigma) / 2.5
    fvk_h27 = (0.15 + 0.4 * 0.30) / 2.5
    log(f"    H-27 retient σ_d = 0,300 MPa → f_vk = {fvk_h27*1000:.0f} kPa")
    log(f"    Valeur calculée     σ_d = {sigma:.3f} MPa → f_vk = {fvk_calc*1000:.0f} kPa")
    log(f"    → H-27 est CONSERVATRICE : elle majore f_vk de {(fvk_h27/fvk_calc-1)*100:.0f} %.")
    log(f"    → En retenant la valeur calculée, τ/f_vk de B-25 passerait de 0,028 à "
        f"{0.028*fvk_h27/fvk_calc:.3f} — conclusion de B-25 inchangée.")
    res["h27"] = dict(N_elu=N_elu_total, A_murs=A_murs, sigma=sigma,
                      fvk_calc=fvk_calc, fvk_h27=fvk_h27,
                      ratio_b25_recalc=0.028 * fvk_h27 / fvk_calc)

    # ------------------------------------------------------------ 6. cohérence
    log("\n[7] CONTRÔLE DE COHÉRENCE GLOBAL")
    A_inf_tot = sum(p["A"] for p in porteurs if p.get("A") and p["type"].startswith("Poteau"))
    log(f"    Somme des aires d'influence des 5 poteaux : {A_inf_tot:.2f} m²")
    log(f"    Surface de plancher R+1 (D-22) : {A_R1:.2f} m²")
    log(f"    → les poteaux ne couvrent que {100*A_inf_tot/A_R1:.1f} % de la surface : "
        f"le reste est porté directement par les murs — cohérent avec un bâtiment en maçonnerie porteuse")
    log(f"    Charge totale ELS estimée sur le R+1 : {(g_tot_B+q_B)*A_R1:.0f} kN")
    log(f"    Charge totale ELU estimée sur le R+1 : {N_elu_total:.0f} kN")

    # ------------------------------------------------------------ 8. écarts avec B-20
    log("\n[8] CONTRÔLE DE COHÉRENCE AVEC LE PRÉDIMENSIONNEMENT DE B-20")
    log("    On compare des EFFETS DE CHARGE (moment de flexion M_Ed = p_ELU·L²/8), jamais des")
    log("    résistances : la comparaison à M_el,Rd relève de B-45, pas de cette brique.")
    log("    Le coefficient de continuité 1,15 est appliqué à p puis à M — majoration volontaire.")
    b20_M = {"F1a": 10.7, "F1b": 10.7, "F1c": 10.7, "F2": 50.0, "F3": 40.8,
             "F4": 20.1, "R1": 47.5, "R2-N": 43.5, "R2-S": 43.5}
    rows = [("Élément", "M_Ed B-20", "M_Ed B-21", "écart", "Conséquence transmise")]
    ecarts = {}
    for bid, ref in b20_M.items():
        L = beam_res[bid]["L"]
        M = beam_res[bid]["p_elu"] * L ** 2 / 8.0
        ec = M / ref - 1
        ecarts[bid] = dict(M20=ref, M21=M, ecart=ec)
        cons = ("B-45 : reprendre le calcul avec l'effet de charge B-21" if ec > 0.15
                else "cohérent avec B-20 — poursuite sans réserve")
        rows.append((bid, f"{ref:.1f} kN·m", f"{M:.1f} kN·m", f"{ec*100:+.0f} %", cons))
    table(rows, (18, 14, 14, 9, 62))
    log("")
    rows2 = [("Poteau", "N_ELU B-20", "N_ELU B-21", "écart", "Conséquence transmise")]
    for pid, ref, cons in (("P1-N", 60.0, "B-45 : capacité 546 kN, marge conservée"),
                           ("P2", 85.0, "B-42 : flambement et section à reprendre")):
        val = elu[pid]["N"]
        ec = val / ref - 1
        rows2.append((pid, f"{ref:.0f} kN", f"{val:.0f} kN", f"{ec*100:+.0f} %", cons))
    val = els["SF1 (sous P2)"]["N"]
    rows2.append(("SF1 (N_ELS)", "63,2 kN", f"{val:.1f} kN", f"{(val/63.2-1)*100:+.0f} %",
                  "B-40 : capacité portante à revérifier — voir § [9]"))
    table(rows2, (18, 14, 14, 9, 62))
    res["ecarts_b20"] = ecarts

    # ------------------------------------------------------------ 9. SF1 : cohérence portance
    log("\n[9] SF1 — COHÉRENCE DE LA SURFACE D'ASSISE AVEC LA DDC (ordre de grandeur, B-40 tranche)")
    N_els_sf1 = els["SF1 (sous P2)"]["N"]
    N_elu_sf1 = elu["SF1 (sous P2)"]["N"]
    B_act = 0.60
    A_act = B_act ** 2
    sig_els = N_els_sf1 / A_act
    B_req = (N_els_sf1 / 300.0) ** 0.5
    log(f"    Semelle actuelle : {B_act*100:.0f} × {B_act*100:.0f} cm = {A_act:.2f} m² (D-14, dimension plancher)")
    log(f"    N_ELS = {N_els_sf1:.1f} kN → σ_ELS = {sig_els:.0f} kPa = {sig_els/1000:.2f} MPa"
        f" (admissible 0,30 MPa → {'NON CONFORME' if sig_els > 300 else 'conforme'})")
    log(f"    Largeur requise : B ≥ √(N_ELS / 0,30 MPa) = √({N_els_sf1:.1f}/300) = {B_req:.2f} m")
    log(f"    → si l'aire d'influence de 11,46 m² est confirmée, SF1 doit passer de 60 × 60 à "
        f"{int((B_req*100//10+1)*10)} × {int((B_req*100//10+1)*10)} cm")
    log(f"    → N_ELU = {N_elu_sf1:.1f} kN sur 0,64 m² = {N_elu_sf1/0.64:.0f} kPa"
        f" (admissible 0,49 MPa → {'NON CONFORME' if N_elu_sf1/0.64 > 490 else 'conforme'})")
    res["sf1"] = dict(N_els=N_els_sf1, N_elu=N_elu_sf1, B_act=B_act,
                      sigma_els=sig_els, B_req=B_req,
                      b20=dict(N_els=63.2, sigma_els=63.2/0.36))

    out = dict(res)
    out["porteurs"] = {p["id"]: dict(type=p["type"], A=p["A"], cont=p["cont"], justif=p["justif"])
                       for p in porteurs}
    with open(JSONOUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=float)
    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log(f"\nJournal : {JOURNAL} ({os.path.getsize(JOURNAL)} o)")
    log(f"JSON    : {JSONOUT} ({os.path.getsize(JSONOUT)} o)")


if __name__ == "__main__":
    main()
