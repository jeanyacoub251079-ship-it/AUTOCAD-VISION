#!/usr/bin/env python3
"""
CROISSY-FLORA — Inventaire scripté du DXF indice C (D5).
CARNAC v2.6 — verrou V13 : tout livrable reposant sur une géométrie de fichier
est produit par un script exécuté, conservé et journalisé.

Entrée  : google_drive/208_FLORA_Plans_DCE_IndC.dxf
Sortie  : _rendus/dxf_inventaire.txt (journal d'exécution)

Ce script ne produit AUCUN livrable : il établit la preuve de contenu
(nombre d'entités, calques, unités, emprises, textes des cartouches).
"""
import sys, hashlib, collections
import ezdxf
from ezdxf import bbox

DXF = "google_drive/208_FLORA_Plans_DCE_IndC.dxf"
OUT = "dossiers/CROISSY/_rendus/dxf_inventaire.txt"

lines = []
def out(s=""):
    lines.append(str(s))
    print(s)

# --- empreinte du fichier : V13 exige la traçabilité de l'entrée
h = hashlib.sha256(open(DXF, "rb").read()).hexdigest()
out("=" * 78)
out("INVENTAIRE DXF — CROISSY-FLORA")
out("=" * 78)
out(f"Fichier        : {DXF}")
out(f"Taille         : {len(open(DXF,'rb').read()):,} octets")
out(f"SHA-256        : {h}")
out(f"ezdxf          : {ezdxf.__version__}")
out("")

doc = ezdxf.readfile(DXF)
out(f"Version DXF    : {doc.dxfversion}  ({doc.acad_release})")
out(f"Encodage       : {doc.encoding}")

hdr = doc.header
def hget(name, default="—"):
    try:
        v = hdr.get(name)
        return default if v is None else v
    except Exception:
        return default

out("")
out("--- VARIABLES D'EN-TÊTE (unités et emprises) ---")
for k in ("$INSUNITS", "$MEASUREMENT", "$EXTMIN", "$EXTMAX", "$LIMMIN", "$LIMMAX",
          "$LTSCALE", "$DIMSCALE", "$INSBASE", "$ACADVER"):
    out(f"  {k:<14} : {hget(k)}")

UNIT = {0: "sans unité", 1: "pouces", 2: "pieds", 4: "mm", 5: "cm", 6: "m", 7: "km"}
out(f"  -> $INSUNITS = {UNIT.get(hget('$INSUNITS', 0), 'inconnu')}  [GEO-06]")

out("")
out("--- CALQUES ---")
layers = [ly.dxf.name for ly in doc.layers]
out(f"Nombre de calques : {len(layers)}")
for n in sorted(layers)[:60]:
    out(f"  · {n}")
if len(layers) > 60:
    out(f"  ... et {len(layers)-60} autres")

out("")
out("--- BLOCS ---")
blocks = [b.name for b in doc.blocks if not b.name.startswith("*")]
out(f"Nombre de blocs nommés : {len(blocks)}")
for n in sorted(blocks)[:40]:
    out(f"  · {n}")
if len(blocks) > 40:
    out(f"  ... et {len(blocks)-40} autres")

# --- espaces de travail
out("")
out("--- ESPACES ---")
msp = doc.modelspace()
out(f"Modelspace : {len(msp)} entités")
for lay in doc.layouts:
    if lay.name == "Model":
        continue
    out(f"Paper space « {lay.name} » : {len(lay)} entités")

# --- comptage par type et par calque
def count(space, label):
    out("")
    out(f"--- TYPES D'ENTITÉS — {label} ---")
    c = collections.Counter(e.dxftype() for e in space)
    for t, n in c.most_common():
        out(f"  {t:<16} {n:>7}")
    return c

count(msp, "MODELSPACE")

out("")
out("--- ENTITÉS PAR CALQUE (modelspace) ---")
c = collections.Counter(e.dxf.layer for e in msp)
for lay, n in c.most_common(40):
    out(f"  {lay:<32} {n:>6}")

# --- emprise calculée
out("")
out("--- EMPRISE GÉOMÉTRIQUE CALCULÉE ---")
try:
    ext = bbox.extents(msp, fast=True)
    out(f"  X : {ext.extmin.x:,.2f}  ->  {ext.extmax.x:,.2f}   (Δ = {ext.extmax.x-ext.extmin.x:,.2f})")
    out(f"  Y : {ext.extmin.y:,.2f}  ->  {ext.extmax.y:,.2f}   (Δ = {ext.extmax.y-ext.extmin.y:,.2f})")
    out(f"  Z : {ext.extmin.z:,.2f}  ->  {ext.extmax.z:,.2f}")
    out(f"  Diagonale : {ext.size.magnitude:,.2f}")
except Exception as e:
    out(f"  ÉCHEC : {e}")

# --- textes : cartouches, titres, cotes
out("")
out("--- TEXTES (MTEXT + TEXT) — 200 premiers ---")
txts = []
for e in msp:
    t = e.dxftype()
    if t == "TEXT":
        txts.append((e.dxf.layer, e.dxf.insert.x, e.dxf.insert.y, e.dxf.text))
    elif t == "MTEXT":
        txts.append((e.dxf.layer, e.dxf.insert.x, e.dxf.insert.y, e.plain_text()))
out(f"Total textes : {len(txts)}")
for lay, x, y, s in txts[:200]:
    s1 = " ".join(s.split())[:90]
    out(f"  [{lay:<22}] ({x:>10,.0f},{y:>10,.0f})  {s1}")

# --- cotes : valeurs
out("")
out("--- COTES (DIMENSION) — valeurs distinctes ---")
dims = [e for e in msp if e.dxftype() == "DIMENSION"]
out(f"Nombre de cotes : {len(dims)}")
vals = []
for d in dims:
    try:
        vals.append(round(d.get_measurement(), 2))
    except Exception:
        pass
if vals:
    out(f"  min = {min(vals)}   max = {max(vals)}")
    vc = collections.Counter(vals)
    out(f"  valeurs les plus fréquentes : {vc.most_common(15)}")

# --- écriture du journal
import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"\n[journal écrit : {OUT}]")
