"""Génération PDF (ReportLab) — notes de calcul, traçabilité, documents
conformité (§4.9, §4.11, §5.12, Lot 6/7).

Les sections techniques (charges → vérifications → armatures) sont 100 %
déterministes et issues du JSON de calcul. Les sections explicatives peuvent
être rédigées par LLM (Anthropic/OpenAI) — elles sont alors marquées
« rédigé avec assistance IA » (§2.6).
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (Image, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

from ..logging_setup import get_logger
from ..util import now_iso

log = get_logger("structai.export.pdf")

COUPE = colors.HexColor("#0e4f6e")


def _styles():
    ss = getSampleStyleSheet()
    ss.add(ParagraphStyle("H2c", parent=ss["Heading2"], textColor=COUPE,
                          fontSize=12.5, spaceBefore=12))
    ss.add(ParagraphStyle("H3c", parent=ss["Heading3"], textColor=COUPE,
                          fontSize=10.5, spaceBefore=8))
    ss.add(ParagraphStyle("small", parent=ss["Normal"], fontSize=8, leading=10))
    ss.add(ParagraphStyle("warn", parent=ss["Normal"], fontSize=8.5,
                          textColor=colors.HexColor("#8a5a00"), backColor=colors.HexColor("#fff6e0"),
                          borderColor=colors.HexColor("#e0b25a"), borderWidth=0.6,
                          borderPadding=4, spaceBefore=6, spaceAfter=6))
    return ss


def _table(data, widths=None, font=8):
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), COUPE),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), font),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#eef4f8")]),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#9db8c8")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return t


def note_de_calcul(out_path: Path, projet: dict, option: dict,
                   redaction_ia: Optional[dict], png_plan: Optional[Path],
                   png_3d: Optional[Path]) -> Path:
    ss = _styles()
    story = []
    P = ss["BodyText"]
    st = option.get("structure", {})
    res = option.get("resultats_calcul", {}) or {}

    # ---- page de garde ----
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph("NOTE DE CALCUL — STRUCTURE BÉTON ARMÉ", ss["Title"]))
    story.append(Paragraph(f"<b>Projet :</b> {projet.get('name', '')}", P))
    story.append(Paragraph(f"<b>Option retenue :</b> {option.get('id', '')} — "
                           f"{option.get('description_courte', '')}", P))
    story.append(Paragraph(f"<b>Date :</b> {now_iso()[:10]} &nbsp;&nbsp; "
                           f"<b>Visionneuse :</b> StructAI v0.1 — moteur local Eurocodes + AN FR", P))
    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph(
        "DOCUMENT DE TRAVAIL — n'est pas un livrable signé. Cette note présente des "
        "propositions de conception générées et calculées automatiquement ; toute valeur "
        "doit être vérifiée et validée par un ingénieur habilité avant usage réel.", ss["warn"]))
    story.append(PageBreak())

    # ---- sommaire ----
    story.append(Paragraph("Sommaire", ss["Heading1"]))
    for i, s in enumerate([
            "Présentation du projet", "Hypothèses de calcul", "Charges", "Combinaisons",
            "Modélisation", "Vérifications EC2/EC8", "Dimensionnement des armatures",
            "Synthèse", "Annexes — résultats détaillés"], start=1):
        story.append(Paragraph(f"{i}. {s}", P))
    story.append(PageBreak())

    # ---- 1. présentation ----
    story.append(Paragraph("1. Présentation du projet", ss["H2c"]))
    if redaction_ia and redaction_ia.get("presentation_projet"):
        story.append(Paragraph(redaction_ia["presentation_projet"], P))
        story.append(Paragraph("<i>Section rédigée avec assistance IA (Claude Opus / "
                               "ChatGPT) à partir des données structurées ci-dessous.</i>",
                               ss["small"]))
    par = projet.get("params", {}) or {}
    story.append(_table([
        ["Paramètre", "Valeur"],
        ["Typologie", str(par.get("type_batiment", "maison_individuelle"))],
        ["Niveaux", f"R+{par.get('niveaux', 1) - 1}"],
        ["Hauteur d'étage", f"{par.get('hauteur_etage', 2.8)} m"],
        ["Usage principal", str(par.get("usage", "habitation"))],
        ["Zone sismique", str(par.get("zone_sismique", "-"))],
        ["Zone de neige", str(par.get("zone_neige", "-"))],
        ["Zone de vent", str(par.get("zone_vent", "-"))],
        ["Altitude", f"{par.get('altitude', '-')} m"],
        ["Matériaux", ", ".join(par.get("materiaux", ["beton_arme"]))],
    ]))

    # ---- 2. hypothèses ----
    hypo = res.get("hypotheses", {})
    story.append(Paragraph("2. Hypothèses de calcul", ss["H2c"]))
    mat = (hypo.get("materiaux") or {})
    beton = mat.get("beton", {})
    acier = mat.get("acier", {})
    story.append(_table([
        ["Grandeur", "Valeur", "Origine"],
        ["Classe béton", beton.get("classe", "C25/30"), "EC2 §3.1.6"],
        ["fck / fcd (MPa)", f"{beton.get('fck', 25)} / {beton.get('fcd', 14.17)}",
         "fcd = αcc·fck/1,5 ; αcc=0,85 (AN FR)"],
        ["Acier", f"{acier.get('classe', 'B500B')} fyk={acier.get('fyk', 500)} "
                  f"fyd={acier.get('fyd', 435)} MPa", "EC2 §3.2.5"],
        ["Durée d'utilisation", f"{hypo.get('duree_utilisation', 50)} ans", "EC0"],
        ["Classe d'exposition", str(hypo.get("classe_exposition", "XC1")), "EC2 §4.2"],
        ["Catégorie d'importance", str(hypo.get("categorie_importance", "II")), "EC0 Table A/B"],
    ]))
    story.append(Paragraph("Modélisation : " + ", ".join(
        f"{k} = {v}" for k, v in (hypo.get("modeles") or {}).items()), ss["small"]))
    story.append(Paragraph(hypo.get("note", ""), ss["warn"]))

    # ---- 3. charges ----
    ch = res.get("charges", {})
    story.append(Paragraph("3. Charges (EC1 + AN FR)", ss["H2c"]))
    perm = ch.get("permanentes", {})
    expl = ch.get("exploitation", {})
    neige = ch.get("neige", {})
    vent = ch.get("vent", {})
    seis = ch.get("seisme", {})
    story.append(_table([
        ["Action", "Valeur", "Note"],
        ["Poids propre", perm.get("poids_propre", "auto"), f"γc={perm.get('beton_gamma', 25)} kN/m³"],
        ["Revêtements", f"{perm.get('revetements', 1.5)} kPa", "EC1-1-1 AN"],
        ["Cloisons", f"{perm.get('cloisons', 0.8)} kPa", "EC1-1-1 AN.2.3"],
        ["Exploitation", f"{expl.get('psi0') and ', '.join(f'{k}={v}' for k, v in expl.items() if isinstance(v,(int,float)))}", expl.get("libelle", "")],
        ["Neige", f"sk={neige.get('sk', 0)} kPa (zone {neige.get('zone')}) μ={neige.get('mu', 0.8)}",
         neige.get("note", "")],
        ["Vent", f"vb0={vent.get('vb0_ms', 24)} m/s → qb={vent.get('qb_kpa', 0.36)} kPa", vent.get("note", "")],
        ["Séisme", f"zone {seis.get('zone')} : ag={seis.get('ag_ms2', 0)} m/s², "
                   f"sol {seis.get('classe_sol')}, q={seis.get('q')}, T1≈{seis.get('T1_estime_s')} s",
         "arrêté 2010 + EC8"],
    ]))
    if png_plan:
        story.append(Spacer(1, 4))
        story.append(Image(str(png_plan), width=16 * cm, height=10 * cm, kind="proportional"))
        story.append(Paragraph("Figure 1 — Structure de l'option retenue (rendu local).", ss["small"]))

    # ---- 4. combinaisons ----
    story.append(Paragraph("4. Combinaisons (EC0 + AN FR)", ss["H2c"]))
    rows = [["Combinaison", "Type", "Expression", "Valeur réf. (kPa)"]]
    for c in res.get("combinaisons", []):
        rows.append([c["id"], c["type"], c["expression"], str(c.get("valeur", ""))])
    story.append(_table(rows))

    # ---- 5. modélisation ----
    story.append(Paragraph("5. Modélisation", ss["H2c"]))
    mo = res.get("modele", {})
    story.append(_table([
        ["Élément", "Valeur"],
        ["Méthode d'analyse", str(mo.get("methode"))],
        ["Nombre de barres", str(mo.get("n_members"))],
        ["Nombre de nœuds", str(mo.get("n_nodes"))],
        ["Poteaux / poutres / voiles", f"{len(st.get('poteaux', []))} / "
         f"{len(st.get('poutres', []))} / {len(st.get('voiles', []))}"],
    ]))
    story.append(Paragraph(
        "Liaisons : nœuds rigides (cadre 3D) ; encastrement en base (hypothèse semelles "
        "noyées) ; planchers considérés comme diaphragmes infinis dans leur plan.", P))
    if png_3d:
        story.append(Image(str(png_3d), width=16 * cm, height=9 * cm, kind="proportional"))
        story.append(Paragraph("Figure 2 — Vue 3D de la structure (contrôle visuel).", ss["small"]))

    # ---- 6. vérifications ----
    story.append(Paragraph("6. Vérifications — sollicitations / résistances / taux", ss["H2c"]))
    ver = res.get("verifications", [])
    story.append(_table([["Élément", "Type", "Vérification", "Combinaison", "Sollic.", "Résist.",
                          "Taux", "Statut"]] +
        [[v.get("element", ""), v.get("type", ""), v.get("verification", ""),
          v.get("combinaison", ""),
          f"{v.get('sollicitation_kN') or v.get('sollicitation_kNm') or v.get('valeur_mm') or v.get('sollicitation_kPa') or ''}",
          f"{v.get('resistance_kN') or v.get('limite_mm') or v.get('resistance_kPa') or v.get('resistance_kNm') or ''}",
          f"{v.get('taux_travail', '')}",
          v.get("statut", "")] for v in ver], font=7))

    # ---- 7. armatures ----
    story.append(Paragraph("7. Dimensionnement des armatures", ss["H2c"]))
    arm = res.get("dimensionnement_armatures", {})
    rows = [["Élément", "Longitudinal", "Cadres / répartition", "Enrobage (mm)"]]
    for eid, a in arm.items():
        rows.append([eid, str(a.get("barres", a.get("section_longitudinale_cm2_m", ""))),
                     str(a.get("cadres", "—")), str(a.get("enrobage_mm", "—"))])
    story.append(_table(rows, font=7))

    # ---- 8. synthèse ----
    syn = res.get("synthese", {})
    conf = option.get("conformite", {})
    story.append(Paragraph("8. Synthèse", ss["H2c"]))
    if redaction_ia and redaction_ia.get("justification_choix"):
        story.append(Paragraph(redaction_ia["justification_choix"], P))
        story.append(Paragraph("<i>Rédigé avec assistance IA à partir des données ci-dessous.</i>",
                               ss["small"]))
    story.append(_table([
        ["Indicateur", "Valeur"],
        ["Taux de travail maximal", f"{syn.get('taux_travail_max')} "
         f"({syn.get('element_critique')} — {syn.get('verification_critique')})"],
        ["Marge", f"{syn.get('marge_pct')} %"],
        ["Conformité EC0 / EC1 / EC2 / EC8 / AN FR",
         f"{conf.get('ec0')} / {conf.get('ec1')} / {conf.get('ec2')} / "
         f"{conf.get('ec8')} / {conf.get('an_fr')}"],
        ["Quantitatifs", f"Béton {option.get('indicateurs', {}).get('volume_beton_m3', '—')} m³ — "
         f"Acier {option.get('indicateurs', {}).get('masse_acier_kg', '—')} kg — "
         f"Coffrage {option.get('indicateurs', {}).get('surface_coffrage_m2', '—')} m²"],
    ]))
    for w in res.get("avertissements", []) or []:
        story.append(Paragraph(f"⚠ {w}", ss["warn"]))
    if redaction_ia and redaction_ia.get("synthese_conclusion"):
        story.append(Paragraph(redaction_ia["synthese_conclusion"], P))
        story.append(Paragraph("<i>Rédigé avec assistance IA.</i>", ss["small"]))

    # ---- 9. annexes ----
    story.append(Paragraph("9. Annexes — hypothèses détaillées", ss["H2c"]))
    story.append(_table([["Clé", "Valeur"]] + [
        [k, str(v)] for k, v in (hypo.get("modeles") or {}).items()], font=7))
    story.append(Paragraph(
        "Généré par StructAI (application personnelle — cahier des charges StructAI). "
        "Chaîne de traçabilité complète disponible dans le rapport de traçabilité du projet.",
        ss["small"]))
    doc = SimpleDocTemplate(str(out_path), pagesize=A4, title=f"Note de calcul {option.get('id')}",
                            author="StructAI", leftMargin=1.7 * cm, rightMargin=1.7 * cm,
                            topMargin=1.6 * cm, bottomMargin=1.6 * cm)
    doc.build(story)
    return out_path


def rapport_tracabilite(out_path: Path, projet: dict, plans: list[dict],
                        interpretations: list[dict], options_index: dict,
                        edits_rows: list[dict], ai_calls_rows: list[dict],
                        deliverables_rows: list[dict]) -> Path:
    ss = _styles()
    P = ss["BodyText"]
    story = [Paragraph("RAPPORT DE TRAÇABILITÉ", ss["Title"]),
             Paragraph(f"Projet : <b>{projet.get('name', '')}</b> — "
                       f"id {projet.get('id', '')}", P),
             Paragraph(f"Généré le {now_iso()} — StructAI", ss["small"]),
             Spacer(1, 8)]
    story.append(Paragraph("1. Paramètres d'entrée", ss["H2c"]))
    story.append(_table([["Clé", "Valeur"]] + [[str(k), str(v)] for k, v in
                     (projet.get("params") or {}).items() if k != "id"], font=7))
    story.append(Paragraph("2. Plans sources", ss["H2c"]))
    story.append(_table([["Fichier", "Taille (o)", "Hash SHA-256", "Import"]] +
        [[pl.get("filename", ""), str(pl.get("size", "")), str(pl.get("sha256", ""))[:24] + "…",
          str(pl.get("imported_at", ""))] for pl in plans], font=7))
    story.append(Paragraph("3. Interprétations", ss["H2c"]))
    story.append(_table([["Id", "Source", "Modèle", "Validée", "Date"]] +
        [[it.get("id", ""), it.get("source", ""), f"{it.get('provider', '')}/{it.get('model', '')}",
          "oui" if it.get("validated") else "non", str(it.get("created_at", ""))]
         for it in interpretations], font=7))
    story.append(Paragraph("4. Génération", ss["H2c"]))
    story.append(_table([["Clé", "Valeur"]] + [[str(k), str(v)] for k, v in options_index.items()], font=7))
    story.append(Paragraph("5. Éditions manuelles", ss["H2c"]))
    story.append(_table([["Date", "Type", "Élément", "Raison"]] +
        [[e.get("date", ""), e.get("type", ""), e.get("element", ""), e.get("reason", "")]
         for e in edits_rows[:120]], font=7))
    story.append(Paragraph("6. Appels IA", ss["H2c"]))
    story.append(_table([["Date", "Fournisseur", "Modèle", "Finalité", "Tok in/out",
                          "Coût USD", "Hash req", "Statut"]] +
        [[a.get("datetime", "")[:19], a.get("provider", ""), a.get("model", ""), a.get("purpose", ""),
          f"{a.get('tokens_in', 0)}/{a.get('tokens_out', 0)}", f"{a.get('cost_usd', 0):.4f}",
          str(a.get("hash_req", ""))[:12] + "…", a.get("status", "")] for a in ai_calls_rows], font=7))
    story.append(Paragraph("7. Livrables produits", ss["H2c"]))
    story.append(_table([["Type", "Fichier", "Hash", "Date"]] +
        [[d.get("type", ""), Path(d.get("path", "")).name, str(d.get("sha256", ""))[:16] + "…",
          str(d.get("created_at", ""))] for d in deliverables_rows], font=7))
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "Le contenu envoyé aux fournisseurs IA n'est jamais stocké en clair : seuls les "
        "hash SHA-256 (tronqués) figurent au journal, permettant de prouver qu'un envoi a "
        "eu lieu sans en conserver la matière.", ss["small"]))
    doc = SimpleDocTemplate(str(out_path), pagesize=A4, title="Traçabilité StructAI",
                            leftMargin=1.5 * cm, rightMargin=1.5 * cm,
                            topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    doc.build(story)
    return out_path


def document_client(out_path: Path, projet_name: str = "") -> Path:
    """Modèle de document d'information/accord client (§5.7.2)."""
    ss = _styles()
    P = ss["BodyText"]
    texte = f"""
    <b>INFORMATION ET ACCORD — TRAITEMENT TECHNIQUE DE DONNÉES ANONYMISÉES</b><br/><br/>
    Dans le cadre de la conception structurelle du projet référencé
    <b>{projet_name or '« … »'}</b>, le concepteur utilise un outil d'assistance à la
    conception (StructAI, application locale personnelle).<br/><br/>
    Le concepteur s'engage à ce que :
    <br/>— les plans et données transmis aux services d'IA en ligne soient préalablement
    anonymisés (aucun nom, adresse, référence cadastrale, logo ou cartouche) ;
    <br/>— seules des données techniques abstraites (géométrie nettoyée, résultats de
    calcul résumés) transitent vers les fournisseurs d'IA retenus ;
    <br/>— les fournisseurs retenus (<b>Anthropic</b> — modèles Claude Opus — et
    <b>OpenAI</b> — modèles ChatGPT/GPT) soient contractualisés avec un accord de
    traitement des données (DPA) prévoyant la non-rétention et la non-utilisation pour
    l'entraînement ;
    <br/>— aucune donnée à caractère personnel ne soit transmise.<br/><br/>
    Le client reconnaît avoir été informé de ce traitement technique et l'accepte pour
    les besoins de la conception. Les documents produits (plans, notes, quantitatifs)
    demeurent des <b>propositions</b> vérifiées et validées par un ingénieur avant tout
    usage.<br/><br/>
    Fait à ______________, le ____ / ____ / ______<br/><br/>
    Signature du client : <br/><br/> Signature du concepteur :
    """
    story = [Paragraph("StructAI — modèle de document client", ss["Title"]),
             Spacer(1, 10), Paragraph(texte.replace("\n", "<br/>").replace("<br/><br/><br/>", "<br/><br/>"), P)]
    doc = SimpleDocTemplate(str(out_path), pagesize=A4, title="Accord anonymisation",
                            leftMargin=2 * cm, rightMargin=2 * cm)
    doc.build(story)
    return out_path


def registre_traitements(out_path: Path) -> Path:
    ss = _styles()
    P = ss["BodyText"]
    story = [Paragraph("Registre simplifié des traitements — StructAI (usage personnel)",
                       ss["Title"]), Spacer(1, 8)]
    story.append(_table([
        ["Traitement", "Finalité", "Données", "Destinataires", "Base légale / notes"],
        ["Import & parsing DXF", "Conception structurelle", "Plans anonymisés",
         "Aucun (local)", "Aucune donnée personnelle"],
        ["Interprétation IA", "Conception structurelle", "Image PNG nettoyée du plan",
         "Fournisseur IA (Anthropic ou OpenAI)", "Anonymisation amont par l'utilisateur"],
        ["Génération d'options", "Conception structurelle", "JSON abstrait",
         "Fournisseur IA (Anthropic ou OpenAI)", "Pas de plan brut, pas de méta"],
        ["Rédaction de notes", "Production de livrables", "Résumés de calcul",
         "Fournisseur IA (Anthropic ou OpenAI)", "Données techniques uniquement"],
        ["Journal d'appels", "Traçabilité", "Hash + tokens + coût", "Local uniquement",
         "Contenu jamais stocké en clair"],
    ], font=7))
    story.append(Paragraph(
        "RGPD : l'application ne traite pas de données personnelles (données techniques "
        "anonymisées en amont). Les engagements détaillés figurent au §5 du cahier des "
        "charges ; ce registre est fourni à titre de documentation interne.", ss["small"]))
    doc = SimpleDocTemplate(str(out_path), pagesize=A4, title="Registre StructAI")
    doc.build(story)
    return out_path
