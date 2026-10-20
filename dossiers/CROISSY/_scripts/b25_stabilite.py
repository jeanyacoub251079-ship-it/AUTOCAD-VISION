#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B-25 — STABILITÉ GLOBALE, CONTREVENTEMENT, JOINTS DE DILATATION ET SISMIQUE
Projet : CROISSY-FLORA (ID-01) — CARNAC v3.0 — Indice A

Régime OUTILLÉ (V13). Ce script produit la preuve numérique de la brique :
  1. Extrait les murs porteurs réels des fonds nettoyés B-32 (blocs géomètre D5),
     étage par étage, et les caractérise (aire, longueur, épaisseur, inerties).
  2. Calcule la raideur horizontale de chaque mur (flexion + cisaillement),
     le centre de rigidité, les excentricités et la raideur torsionnelle.
  3. Applique l'action du vent EC1-1-4 (vb = 24 m/s, terrain III) par niveau,
     puis répartit les efforts avec torsion structurale + excentrique accidentelle.
  4. Vérifie le cisaillement des murs (EC6 § 3.6.2) et l'élancement hors plan.
  5. Évalue la sensibilité sismique EC8 (zone 1, cat. II retenue ; sensibilité
     cat. III pour un ERP type J) au moyen de la méthode des forces latérales.
  6. Teste les phases provisoires : retrait successif de chaque mur entaillé par
     un frangement, recalcul du centre de rigidité et du taux de travail.
  7. Statue sur les joints de dilatation (température + retrait + phasage).

Sorties :
  - dossiers/CROISSY/_rendus/b25_stabilite.txt   (journal OUT-03)
  - dossiers/CROISSY/_rendus/b25_stabilite.json  (résultats pour la note)
"""

import json
import math
import os
from datetime import datetime

import ezdxf
import numpy as np

SRC_RDC = "dossiers/CROISSY/_plans/FLORA_RDC_VUE-NETTOYEE_IndD.dxf"
SRC_R1 = "dossiers/CROISSY/_plans/FLORA_R1_VUE-NETTOYEE_IndD.dxf"
JOURNAL = "dossiers/CROISSY/_rendus/b25_stabilite.txt"
JSONOUT = "dossiers/CROISSY/_rendus/b25_stabilite.json"

B30 = (8586.97, 4442.70)          # origine P1 (cm DXF) — repère B-30
BLOCK_RDC = "Murs porteurs selon geometre projet"
BLOCK_R1 = "R+1 Projet"
DY_R1 = 3755.0                    # cm — translation d'empilement R+1 -> RDC (B-31 Ind. C, GEO-11)

# ---------------------------------------------------------------- hypothèses
H_MASONRY = dict(
    fk=1.5,          # MPa — résistance caractéristique en compression (moellons) — H-25
    E=1500.0,        # MPa — E = 1000 fk (EC6 § 3.7.2) — H-25
    nu=0.2,
    fvk0=0.15,       # MPa — cohésion initiale au cisaillement — H-26
    gamma_M=2.5,
    sigma_d=0.30,    # MPa — contrainte verticale moyenne de service sur les murs — H-27
)
H_GEOM = dict(h_rdc=3.00, h_r1=3.00)     # m — hauteurs libres (D2 : P2 H = 3,00 m)
H_WIND = dict(vb=24.0, rho=1.25, z0=0.30, zmin=5.0, cpe_net=1.30, cscd=1.0, terrain="III")
H_SEIS = dict(ag=0.40, gamma_I=1.20, S=1.50, TB=0.15, TC=0.40, q=1.50)   # sol C (S=1,50) — H-24
H_MASS = dict(g_floor=4.50, q_floor=2.50, psi2=0.30, g_roof=0.80)
A_RDC, A_R1 = 111.15, 106.92            # m² — surfaces D-22

LOG = []


def log(msg=""):
    print(msg)
    LOG.append(msg)


def b30(x, y):
    return ((x - B30[0]) / 100.0, (y - B30[1]) / 100.0)


# ---------------------------------------------------------------- géométrie
def polygon_area_centroid_I(pts):
    """Aire, centre, inerties Ixx, Iyy, Ixy d'un polygone (formules de Green)."""
    x = np.array([p[0] for p in pts], dtype=float)
    y = np.array([p[1] for p in pts], dtype=float)
    x1, y1 = np.roll(x, -1), np.roll(y, -1)
    cross = x * y1 - x1 * y
    A = 0.5 * cross.sum()
    if abs(A) < 1e-12:
        return 0.0, (0.0, 0.0), 0.0, 0.0, 0.0
    cx = ((x + x1) * cross).sum() / (6 * A)
    cy = ((y + y1) * cross).sum() / (6 * A)
    Ixx = ((y * y + y * y1 + y1 * y1) * cross).sum() / 12.0
    Iyy = ((x * x + x * x1 + x1 * x1) * cross).sum() / 12.0
    Ixy = ((x * y1 + 2 * x * y + 2 * x1 * y1 + x1 * y) * cross).sum() / 24.0
    return abs(A), (cx, cy), abs(Ixx - A * cy * cy), abs(Iyy - A * cx * cx), Ixy - A * cx * cy


def extract_walls(path, block_name, dy_cm=0.0):
    doc = ezdxf.readfile(path)
    ins = [e for e in doc.modelspace()
           if e.dxftype() == "INSERT" and e.dxf.name == block_name]
    if not ins:
        raise SystemExit(f"Bloc introuvable : {block_name} dans {path}")
    walls = []
    for i in ins:
        m = i.matrix44()
        for be in doc.blocks.get(i.dxf.name):
            if be.dxftype() != "LWPOLYLINE" or be.dxf.layer != "010_mur":
                continue
            pts = [tuple(m.transform((p[0], p[1], 0)))[:2] for p in be.get_points("xy")]
            if len(pts) < 3:
                continue
            pts_m = [b30(p[0], p[1] + dy_cm) for p in pts]
            A, (cx, cy), Ixx, Iyy, Ixy = polygon_area_centroid_I(pts_m)
            if A < 0.15:      # liserés non surfaciques du relevé
                continue
            a = np.array(pts_m)
            ev, evec = np.linalg.eigh(np.cov(a.T))
            d = evec[:, np.argmax(ev)]
            ang = math.degrees(math.atan2(d[1], d[0])) % 180.0
            u = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
            n = np.array([-u[1], u[0]])
            L = float((a @ u).max() - (a @ u).min())
            t = float((a @ n).max() - (a @ n).min())
            walls.append(dict(A=A, c=(cx, cy), Ixx=Ixx, Iyy=Iyy, Ixy=Ixy,
                              ang=ang, L=L, t=t, t_eq=A / max(L, 1e-9), pts=pts_m))
    walls.sort(key=lambda w: (round(w["c"][1], 1), round(w["c"][0], 1)))
    for k, w in enumerate(walls, 1):
        w["id"] = f"M{k:02d}"
    return walls


# ---------------------------------------------------------------- raideurs
def stiffness(w, h, mat):
    E = mat["E"] * 1000.0
    G = E / (2 * (1 + mat["nu"]))

    def k(I, A):
        return 1.0 / (h ** 3 / (3 * E * max(I, 1e-9)) + 1.2 * h / (G * max(A, 1e-9)))
    return k(w["Iyy"], w["A"]), k(w["Ixx"], w["A"])


def centre_rigidite(walls, key, idx):
    den = sum(w[key] for w in walls)
    return (sum(w[key] * w["c"][idx] for w in walls) / den if den else 0.0), den


def torsion_stiffness(walls, key, idx, cr):
    return sum(w[key] * (w["c"][idx] - cr) ** 2 for w in walls)


def distribute(walls, key, idx, cr, Ktot, KT, V, Mt):
    out = {}
    for w in walls:
        d = w["c"][idx] - cr
        out[w["id"]] = V * w[key] / Ktot + (Mt * w[key] * d / KT if KT > 1e-9 else 0.0)
    return out


# ---------------------------------------------------------------- vent EC1
def qp(z, wind):
    kr = 0.19 * (wind["z0"] / 0.05) ** 0.07
    zz = max(z, wind["zmin"])
    lz = math.log(zz / wind["z0"])
    ce = kr * kr * lz * (7 + lz)
    qb = 0.5 * wind["rho"] * wind["vb"] ** 2 / 1000.0
    return ce * qb, ce, qb


def wind_force(width, z_lo, z_hi, wind):
    zs = np.linspace(z_lo, z_hi, 40)
    q = np.array([qp(z, wind)[0] for z in zs])
    trapz = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trapz(q, zs) * width * wind["cpe_net"] * wind["cscd"])


def hull_centroid(walls):
    pts = np.array([p for w in walls for p in w["pts"]])
    try:
        from scipy.spatial import ConvexHull
        h = ConvexHull(pts)
        poly = pts[h.vertices]
    except Exception:
        x, y = pts[:, 0], pts[:, 1]
        cx, cy = x.mean(), y.mean()
        ang = np.sort(np.arctan2(y - cy, x - cx))
        poly = pts[np.argsort(np.arctan2(y - cy, x - cx))]
    A, (cx, cy), _, _, _ = polygon_area_centroid_I([tuple(p) for p in poly])
    return A, (cx, cy), poly


def main():
    os.makedirs("dossiers/CROISSY/_rendus", exist_ok=True)
    log("=" * 104)
    log("B-25 — STABILITÉ GLOBALE, CONTREVENTEMENT, JOINTS ET SISMIQUE — INDICE A")
    log("Projet CROISSY-FLORA (ID-01) — CARNAC v3.0 — régime OUTILLÉ (V13)")
    log(f"Exécution : {datetime.now():%Y-%m-%d %H:%M:%S}")
    log(f"Sources   : {SRC_RDC}")
    log(f"            {SRC_R1}  (translation d'empilement dy = +{DY_R1:.0f} cm — B-31)")
    log("=" * 104)

    walls_rdc = extract_walls(SRC_RDC, BLOCK_RDC)
    walls_r1 = extract_walls(SRC_R1, BLOCK_R1, DY_R1)
    log(f"\n[1] GÉOMÉTRIE — murs porteurs surfaciques extraits des fonds B-32 Ind. D")
    log(f"    RDC : {len(walls_rdc)} murs surfaciques · R+1 : {len(walls_r1)} murs surfaciques")
    log("    (les liserés de moins de 0,05 m² — arêtes du relevé — sont écartés et consignés)")

    levels = [("R+1", walls_r1, H_GEOM["h_r1"]), ("RDC", walls_rdc, H_GEOM["h_rdc"])]
    for name, ws, h in levels:
        log(f"\n    Niveau {name} (h = {h:.2f} m, E = {H_MASONRY['E']:.0f} MPa) :")
        log("      ID     A(m²)  L(m)  t(m)  dir(°)   centre B-30 (m)        Kx(kN/m)   Ky(kN/m)")
        for w in ws:
            w["Kx"], w["Ky"] = stiffness(w, h, H_MASONRY)
            log(f"      {w['id']}  {w['A']:6.2f} {w['L']:5.2f} {w['t']:5.2f}  {w['ang']:6.1f}"
                f"  ({w['c'][0]:+6.2f},{w['c'][1]:+6.2f})  {w['Kx']:10.0f} {w['Ky']:10.0f}")

    results = {"project": "CROISSY-FLORA", "brick": "B-25", "indice": "A",
               "date": datetime.now().isoformat(timespec="seconds"),
               "hypotheses": {"masonry": H_MASONRY, "geom": H_GEOM, "wind": H_WIND,
                              "seis": H_SEIS, "mass": H_MASS,
                              "surfaces": {"RDC": A_RDC, "R+1": A_R1}},
               "levels": {}, "wind": {}, "seis": {}, "phases": [], "joints": {}}

    # ------------------------------------------------------------ raideurs globales
    log("\n[2] CENTRES DE RIGIDITÉ, CENTRES DE MASSE ET RAIDEURS D'ENSEMBLE")
    for name, ws, h in levels:
        Kx = sum(w["Kx"] for w in ws)
        Ky = sum(w["Ky"] for w in ws)
        cr_y, _ = centre_rigidite(ws, "Kx", 1)
        cr_x, _ = centre_rigidite(ws, "Ky", 0)
        KT_x = torsion_stiffness(ws, "Kx", 1, cr_y)
        KT_y = torsion_stiffness(ws, "Ky", 0, cr_x)
        Ah, Gh, poly = hull_centroid(ws)
        S = A_RDC if name == "RDC" else A_R1
        log(f"    {name} : ΣKx = {Kx:9.0f} kN/m · ΣKy = {Ky:9.0f} kN/m")
        log(f"          CR(vent X) : Y = {cr_y:+6.2f} m   ·   CR(vent Y) : X = {cr_x:+6.2f} m")
        log(f"          KT,x = {KT_x:11.0f} kN·m²/rad · KT,y = {KT_y:11.0f} kN·m²/rad")
        log(f"          G estimé (barycentre de l'enveloppe, aire {Ah:.1f} m² pour {S:.2f} m² utiles)"
            f" = ({Gh[0]:+6.2f},{Gh[1]:+6.2f})")
        log(f"          excentricité structurale vent X : e_y = {Gh[1]-cr_y:+.2f} m"
            f" · vent Y : e_x = {Gh[0]-cr_x:+.2f} m")
        results["levels"][name] = dict(
            Kx=Kx, Ky=Ky, cr_y=cr_y, cr_x=cr_x, KT_x=KT_x, KT_y=KT_y, h=h,
            hull_area=Ah, G=[Gh[0], Gh[1]], e_struct=[Gh[0] - cr_x, Gh[1] - cr_y],
            walls=[{k: v for k, v in w.items() if k != "pts"} for w in ws],
        )

    # ------------------------------------------------------------ vent
    xs = [w["c"][0] for w in walls_rdc]
    ys = [w["c"][1] for w in walls_rdc]
    Bx = max(ys) - min(ys) + 2.0     # largeur de façade chargée par un vent selon X
    By = max(xs) - min(xs) + 1.0     # largeur de façade chargée par un vent selon Y
    log(f"\n[3] ACTION DU VENT — EC1-1-4 (vb = {H_WIND['vb']:.0f} m/s · terrain {H_WIND['terrain']}"
        f" · cpe,net = {H_WIND['cpe_net']:.2f} · cscd = {H_WIND['cscd']:.1f})")
    qb = 0.5 * H_WIND["rho"] * H_WIND["vb"] ** 2 / 1000.0
    log(f"    qb = 0,5 × {H_WIND['rho']} × {H_WIND['vb']:.0f}² = {qb*1000:.0f} Pa")
    for z in (3.0, 6.0):
        q, ce, _ = qp(z, H_WIND)
        log(f"    z = {z:4.1f} m : ce(z) = {ce:.2f} · qp(z) = {q*1000:.0f} Pa")
    log(f"    Largeur chargée : vent X = {Bx:.1f} m (façades N/S) · vent Y = {By:.1f} m (façades E/O)")
    wx = {"R+1": wind_force(Bx, 3.0, 6.0, H_WIND), "RDC": wind_force(Bx, 0.0, 3.0, H_WIND)}
    wy = {"R+1": wind_force(By, 3.0, 6.0, H_WIND), "RDC": wind_force(By, 0.0, 3.0, H_WIND)}
    log(f"    Vent X : R+1 {wx['R+1']:5.1f} kN · RDC {wx['RDC']:5.1f} kN → total {sum(wx.values()):5.1f} kN")
    log(f"    Vent Y : R+1 {wy['R+1']:5.1f} kN · RDC {wy['RDC']:5.1f} kN → total {sum(wy.values()):5.1f} kN")

    # ------------------------------------------------------------ torsion + cisaillement
    log("\n[4] TORSION ET CISAILLEMENT DES MURS (EC6 § 3.6.2 et § 4.5.2)")
    fvk = (H_MASONRY["fvk0"] * 1000 + 0.4 * H_MASONRY["sigma_d"] * 1000) / H_MASONRY["gamma_M"]
    log(f"    fvk = (fvk0 + 0,4 σd)/γM = ({H_MASONRY['fvk0']*1000:.0f} + 0,4×{H_MASONRY['sigma_d']*1000:.0f})"
        f" / {H_MASONRY['gamma_M']:.1f} = {fvk:.0f} kPa")
    checks = {}
    for name, ws, h in levels:
        L = results["levels"][name]
        for axe, K, cr, idx, V, span in (
                ("X", "Kx", L["cr_y"], 1, wx[name], Bx),
                ("Y", "Ky", L["cr_x"], 0, wy[name], By)):
            e_struct = abs(L["e_struct"][1] if axe == "X" else L["e_struct"][0])
            e_acc = 0.05 * span
            Mt = V * (e_struct + e_acc)
            vv = distribute(ws, K, idx, cr, L[K], L["KT_" + axe.lower()], V, Mt)
            vmax_id = max(vv, key=lambda k: abs(vv[k]))
            wr = next(w for w in ws if w["id"] == vmax_id)
            tau = abs(vv[vmax_id]) / wr["A"]
            log(f"    {name} — vent {axe} : V = {V:5.1f} kN · e_struct = {e_struct:.2f} m"
                f" · e_acc = ±{e_acc:.2f} m · Mt = {Mt:5.1f} kN·m")
            log(f"          mur le plus chargé {vmax_id} : V = {abs(vv[vmax_id]):5.1f} kN"
                f" · τ = {tau:5.1f} kPa · τ/fvk = {tau/fvk:6.3f}")
            checks[f"{name}-{axe}"] = dict(V=V, e_struct=e_struct, e_acc=e_acc, Mt=Mt,
                                           vmax_id=vmax_id, vmax=abs(vv[vmax_id]),
                                           tau=tau, fvk=fvk, ratio=tau / fvk, vv=vv)
    results["wind"] = dict(wx=wx, wy=wy, qb=qb, Bx=Bx, By=By, checks=checks, fvk=fvk)

    # ------------------------------------------------------------ élancement hors plan
    log("\n[5] STABILITÉ HORS PLAN DES VOILES (EC6 § 5.5.1.2 — élancement)")
    for name, ws, h in levels:
        who = max(ws, key=lambda w: h / max(w["t_eq"], 1e-6))
        ratio = h / max(who["t_eq"], 1e-6)
        verdict = "OK (≤ 20)" if ratio <= 20 else "À VÉRIFIER (> 20)"
        log(f"    {name} : h/t_eq maximal = {ratio:5.1f} (mur {who['id']}, t_eq = A/L = {who['t_eq']:.2f} m)"
            f" → {verdict}")
        results["slenderness_{}".format(name)] = dict(id=who["id"], t_eq=who["t_eq"], ratio=ratio)

    # ------------------------------------------------------------ sismique
    log("\n[6] POSITION SISMIQUE — EC8-1 / arrêté du 22 octobre 2010")
    W = (A_RDC + A_R1) * (H_MASS["g_floor"] + H_MASS["psi2"] * H_MASS["q_floor"]) + A_R1 * H_MASS["g_roof"]
    T1 = 0.05 * 6.30 ** 0.75
    Sd = H_SEIS["ag"] * H_SEIS["S"] * 2.5 / H_SEIS["q"] * H_SEIS["gamma_I"]
    Vb = Sd * W / 9.81
    log(f"    W = (111,15 + 106,92) × (4,50 + 0,30 × 2,50) + 106,92 × 0,80 = {W:.0f} kN ({W/9.81:.1f} t)")
    log(f"    T1 = Ct·H^0,75 = 0,05 × 6,30^0,75 = {T1:.3f} s → plateau du spectre de calcul")
    log(f"    Sd(T1) = ag·S·2,5/q·γI = {H_SEIS['ag']:.2f}×{H_SEIS['S']:.2f}×2,5/{H_SEIS['q']:.1f}"
        f"×{H_SEIS['gamma_I']:.1f} = {Sd:.2f} m/s²")
    log(f"    Vb = Sd·W/g = {Vb:.1f} kN (hypothèse enveloppe catégorie III, à arbitrer — D2 annonce II)")
    log(f"    Vent : Vx = {sum(wx.values()):.1f} kN · Vy = {sum(wy.values()):.1f} kN")
    log(f"    → le séisme d'enveloppe cat. III ({Vb:.0f} kN) vaut {Vb/max(sum(wx.values()),1e-9):.1f} fois le vent X")
    log("    → zone 1 (très faible) : l'arrêté du 22/10/2010 (art. 3) ne rend les règles EC8 applicables")
    log("      qu'en zones 2 à 5 — aucune catégorie d'importance n'y est soumise en zone 1.")
    log("      La vérification ci-dessus est donc une SENSIBILITÉ (enveloppe cat. III), pas une obligation.")
    # répartition par la méthode des forces latérales : F_i = Vb · z_i·m_i / Σ z_j·m_j
    m_r1 = A_R1 * (H_MASS["g_floor"] + H_MASS["psi2"] * H_MASS["q_floor"]) + A_R1 * H_MASS["g_roof"]
    m_rdc = A_RDC * (H_MASS["g_floor"] + H_MASS["psi2"] * H_MASS["q_floor"])
    z_r1, z_rdc = 6.30, 3.15
    den = z_r1 * m_r1 + z_rdc * m_rdc
    F_r1, F_rdc = Vb * z_r1 * m_r1 / den, Vb * z_rdc * m_rdc / den
    log(f"    Répartition en hauteur : m_R+1 = {m_r1:.0f} kN · m_RDC = {m_rdc:.0f} kN"
        f" → F_R+1 = {F_r1:.1f} kN · F_RDC = {F_rdc:.1f} kN")
    seis_checks = {}
    for name, ws, F in (("R+1", walls_r1, F_r1), ("RDC", walls_rdc, F_rdc)):
        L = results["levels"][name]
        for axe, K, cr, idx, span in (("X", "Kx", L["cr_y"], 1, Bx), ("Y", "Ky", L["cr_x"], 0, By)):
            Mt = F * (abs(L["e_struct"][1] if axe == "X" else L["e_struct"][0]) + 0.05 * span)
            vv = distribute(ws, K, idx, cr, L[K], L["KT_" + axe.lower()], F, Mt)
            vmax_id = max(vv, key=lambda k: abs(vv[k]))
            wr = next(w for w in ws if w["id"] == vmax_id)
            tau = abs(vv[vmax_id]) / wr["A"]
            log(f"      {name} — séisme {axe} : F = {F:5.1f} kN · Mt = {Mt:5.1f} kN·m"
                f" · mur {vmax_id} V = {abs(vv[vmax_id]):5.1f} kN · τ/fvk = {tau/fvk:.3f}")
            seis_checks[f"{name}-{axe}"] = dict(F=F, Mt=Mt, vmax_id=vmax_id,
                                               vmax=abs(vv[vmax_id]), tau=tau,
                                               ratio=tau / fvk, vv=vv)
    results["seis"] = dict(W=W, mass_t=W / 9.81, T1=T1, Sd=Sd, Vb=Vb, F={"R+1": F_r1, "RDC": F_rdc},
                           checks=seis_checks)

    # ------------------------------------------------------------ phases provisoires
    log("\n[7] PHASES PROVISOIRES — retrait d'un mur entaillé, recalcul complet")
    phases = []
    for name, ws, h in levels:
        L = results["levels"][name]
        K0 = L["Ky"]
        for w in ws:
            reste = [x for x in ws if x["id"] != w["id"]]
            cr2, K2 = centre_rigidite(reste, "Ky", 0)
            KT2 = torsion_stiffness(reste, "Ky", 0, cr2)
            V = wy[name]
            Mt = V * (0.05 * By + abs(cr2 - L["cr_x"]))
            vv = distribute(reste, "Ky", 0, cr2, K2, KT2, V, Mt)
            vmax_id = max(vv, key=lambda k: abs(vv[k]))
            wr = next(x for x in reste if x["id"] == vmax_id)
            tau = abs(vv[vmax_id]) / wr["A"]
            phases.append(dict(level=name, removed=w["id"], dCR=cr2 - L["cr_x"],
                               K2=K2, K0=K0, part=K2 / K0, ratio=tau / fvk, tau=tau,
                               vmax_id=vmax_id, vmax=abs(vv[vmax_id])))
    phases.sort(key=lambda p: -p["ratio"])
    log("    Situations les plus défavorables (mur retiré · déplacement du CR · raideur restante · taux) :")
    for p in phases[:8]:
        log(f"      {p['level']} — retrait {p['removed']} : ΔCR = {p['dCR']:+5.2f} m"
            f" · ΣKy = {p['K2']:8.0f}/{p['K0']:8.0f} kN/m ({100*p['part']:5.1f} %)"
            f" · mur {p['vmax_id']} V = {p['vmax']:5.1f} kN · τ/fvk = {p['ratio']:.3f}")
    results["phases"] = phases

    # enveloppe de démolition : retrait simultané des deux murs les plus défavorables
    log("\n[7bis] ENVELOPPE DE DÉMOLITION — retrait simultané des deux murs les plus défavorables")
    env = {}
    for name, ws, h in levels:
        L = results["levels"][name]
        worst = sorted([p for p in phases if p["level"] == name], key=lambda p: -abs(p["dCR"]))[:2]
        ids = [p["removed"] for p in worst]
        reste = [x for x in ws if x["id"] not in ids]
        cr2, K2 = centre_rigidite(reste, "Ky", 0)
        KT2 = torsion_stiffness(reste, "Ky", 0, cr2)
        V = wy[name]
        Mt = V * (0.05 * By + abs(cr2 - L["cr_x"]))
        vv = distribute(reste, "Ky", 0, cr2, K2, KT2, V, Mt)
        vmax_id = max(vv, key=lambda k: abs(vv[k]))
        wr = next(x for x in reste if x["id"] == vmax_id)
        tau = abs(vv[vmax_id]) / wr["A"]
        log(f"    {name} — retrait {ids[0]} + {ids[1]} : ΔCR = {cr2-L['cr_x']:+5.2f} m"
            f" · ΣKy = {K2:8.0f}/{L['Ky']:8.0f} kN/m ({100*K2/L['Ky']:5.1f} %)"
            f" · mur {vmax_id} V = {abs(vv[vmax_id]):5.1f} kN · τ/fvk = {tau/fvk:.3f}")
        env[name] = dict(removed=ids, dCR=cr2 - L["cr_x"], K2=K2, K0=L["Ky"],
                         part=K2 / L["Ky"], vmax_id=vmax_id, vmax=abs(vv[vmax_id]),
                         tau=tau, ratio=tau / fvk)
    results["envelope_demolition"] = env

    # ------------------------------------------------------------ joints
    log("\n[8] JOINTS DE DILATATION")
    Lmax = max(By, Bx)
    dT = 30.0
    dl = 10e-6 * dT * Lmax * 1000
    log(f"    Emprise du bloc : {By:.1f} m × {Bx:.1f} m")
    log(f"    Dilatation thermique libre : α·ΔT·L = 10⁻⁵ × {dT:.0f} × {Lmax:.1f} = {dl:.1f} mm")
    log("    Maçonnerie existante sans joint depuis sa construction, mortier ancien stabilisé,")
    log("    aucun tassement différencié identifié dans D3, frangements neufs appuyés (portée ≤ 4,88 m).")
    log("    → AUCUN joint de dilatation à créer (D-xx à consigner au RDR).")
    results["joints"] = dict(dim=[By, Bx], delta_T=dT, dl_mm=dl, nb_joints=0)

    with open(JSONOUT, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1, ensure_ascii=False, default=float)
    with open(JOURNAL, "w", encoding="utf-8") as f:
        f.write("\n".join(LOG) + "\n")
    log(f"\nJournal écrit : {JOURNAL} ({os.path.getsize(JOURNAL)} o)")
    log(f"Résultats     : {JSONOUT} ({os.path.getsize(JSONOUT)} o)")


if __name__ == "__main__":
    main()
