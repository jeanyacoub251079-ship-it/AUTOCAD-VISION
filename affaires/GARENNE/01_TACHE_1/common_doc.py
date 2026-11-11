"""Moteur de production documentaire A4 ISO (DOCX + PDF) — Affaire GARENNE.

Un modele de contenu unique est rendu a l'identique en .docx (python-docx)
et en .pdf (reportlab), afin de garantir la coherence stricte des deux
livrables exiges par le cahier des charges.

Blocs de contenu disponibles :
  ("h1", texte) ("h2", texte) ("h3", texte)
  ("p", texte)  -> gras inline **...**
  ("note", texte) -> encadre gris
  ("bullets", [textes])
  ("table", dict(cols=[...], header=[...], rows=[[...]], widths=[mm...],
                 caption=..., font=8, align=[...]))
  ("figure", chemin, legende, largeur_mm)
  ("pagebreak",)
"""
from __future__ import annotations

import os
import re

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Mm, Pt, RGBColor

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, Image, KeepTogether,
                                PageTemplate, Paragraph, Spacer, Table,
                                TableStyle)

# --------------------------------------------------------------------------
# Charte
# --------------------------------------------------------------------------
BLEU = "1F3864"
BLEU_CLAIR = "D9E2F3"
GRIS = "F2F2F2"
GRIS_FONCE = "595959"
ROUGE = "C00000"
ORANGE = "BF8F00"

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
F_REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")
F_BOL = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
F_MONO = os.path.join(FONT_DIR, "DejaVuSansMono.ttf")

_pdf_ready = False


def _register_fonts():
    global _pdf_ready
    if _pdf_ready:
        return
    pdfmetrics.registerFont(TTFont("DV", F_REG))
    pdfmetrics.registerFont(TTFont("DVB", F_BOL))
    pdfmetrics.registerFont(TTFont("DVM", F_MONO))
    pdfmetrics.registerFontFamily("DV", normal="DV", bold="DVB",
                                  italic="DV", boldItalic="DVB")
    _pdf_ready = True


# --------------------------------------------------------------------------
# Utilitaires texte
# --------------------------------------------------------------------------
def _split_bold(text: str):
    """Retourne [(morceau, gras)] a partir d'un texte a **gras**."""
    parts = []
    for i, chunk in enumerate(re.split(r"\*\*", text)):
        if chunk:
            parts.append((chunk, i % 2 == 1))
    return parts or [(text, False)]


def plain(text: str) -> str:
    """Remplace les balises <sub>/<sup> par une notation lineaire lisible.

    Les deux moteurs de rendu (python-docx et reportlab) ne gerent pas les
    exposants typographiques : `<sub>ELU</sub>` deviendrait sinon `ELU`, colle
    au caractere precedent et illisible. On le convertit donc en `_ELU`, et
    `<sup>x</sup>` en `^x`, notation usuelle des notes de calcul.
    """
    text = re.sub(r"<sub>(.*?)</sub>", r"_\1", text)
    return re.sub(r"<sup>(.*?)</sup>", r"^\1", text)


def _pdf_rich(text: str) -> str:
    out = []
    for chunk, bold in _split_bold(plain(text)):
        esc = (chunk.replace("&", "&amp;").replace("<", "&lt;")
               .replace(">", "&gt;"))
        out.append(f"<b>{esc}</b>" if bold else esc)
    return "".join(out)


# --------------------------------------------------------------------------
# Rendu DOCX
# --------------------------------------------------------------------------
class DocxWriter:
    def __init__(self, meta: dict):
        self.meta = meta
        self.doc = Document()
        self._setup()

    def _setup(self):
        d = self.doc
        s = d.sections[0]
        s.page_width, s.page_height = Mm(210), Mm(297)
        s.left_margin = s.right_margin = Mm(20)
        s.top_margin = Mm(22)
        s.bottom_margin = Mm(18)
        s.header_distance = Mm(10)
        s.footer_distance = Mm(8)

        st = d.styles["Normal"]
        st.font.name = "Arial"
        st.font.size = Pt(9.5)
        st.paragraph_format.space_after = Pt(4)
        st.paragraph_format.line_spacing = 1.05
        rpr = st.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts")
            rpr.append(rf)
        rf.set(qn("w:eastAsia"), "Arial")

        for i, (sz, col) in enumerate([(15, BLEU), (12, BLEU), (10.5, "000000")], 1):
            h = d.styles[f"Heading {i}"]
            h.font.name = "Arial"
            h.font.size = Pt(sz)
            h.font.bold = True
            h.font.color.rgb = RGBColor.from_string(col)
            h.paragraph_format.space_before = Pt(10 if i == 1 else 8)
            h.paragraph_format.space_after = Pt(4)
            h.paragraph_format.keep_with_next = True

        self._header_footer()

    def _header_footer(self):
        s = self.doc.sections[0]
        s.different_first_page_header_footer = True

        hp = s.header.paragraphs[0]
        hp.text = ""
        r = hp.add_run(self.meta["entete_gauche"])
        r.font.size = Pt(7.5)
        r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)
        hp.add_run("\t\t")
        r2 = hp.add_run(self.meta["entete_droit"])
        r2.font.size = Pt(7.5)
        r2.font.bold = True
        r2.font.color.rgb = RGBColor.from_string(BLEU)
        self._bottom_border(hp)

        fp = s.footer.paragraphs[0]
        fp.text = ""
        r = fp.add_run(self.meta["pied_gauche"])
        r.font.size = Pt(7)
        r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)
        fp.add_run("\t\t")
        r = fp.add_run("Page ")
        r.font.size = Pt(7)
        self._field(fp, "PAGE")
        r = fp.add_run(" / ")
        r.font.size = Pt(7)
        self._field(fp, "NUMPAGES")

        # premiere page : bandeau seulement
        ffp = s.first_page_footer.paragraphs[0]
        ffp.text = ""
        r = ffp.add_run(self.meta["pied_gauche"])
        r.font.size = Pt(7)
        r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)

    @staticmethod
    def _field(par, code):
        run = par.add_run()
        f1 = OxmlElement("w:fldChar")
        f1.set(qn("w:fldCharType"), "begin")
        it = OxmlElement("w:instrText")
        it.set(qn("xml:space"), "preserve")
        it.text = code
        f2 = OxmlElement("w:fldChar")
        f2.set(qn("w:fldCharType"), "end")
        run._r.append(f1)
        run._r.append(it)
        run._r.append(f2)
        run.font.size = Pt(7)

    @staticmethod
    def _bottom_border(par):
        pPr = par._p.get_or_add_pPr()
        pbdr = OxmlElement("w:pBdr")
        bot = OxmlElement("w:bottom")
        bot.set(qn("w:val"), "single")
        bot.set(qn("w:sz"), "6")
        bot.set(qn("w:color"), BLEU)
        bot.set(qn("w:space"), "2")
        pbdr.append(bot)
        pPr.append(pbdr)

    @staticmethod
    def _shade(cell, hexcolor):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), hexcolor)
        tcPr.append(shd)

    def add(self, block):
        kind = block[0]
        if kind == "h1":
            self.doc.add_heading(block[1], level=1)
        elif kind == "h2":
            self.doc.add_heading(block[1], level=2)
        elif kind == "h3":
            self.doc.add_heading(block[1], level=3)
        elif kind == "p":
            p = self.doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for chunk, bold in _split_bold(block[1]):
                r = p.add_run(plain(chunk))
                r.bold = bold
        elif kind == "note":
            t = self.doc.add_table(rows=1, cols=1)
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            cell = t.cell(0, 0)
            self._shade(cell, GRIS)
            cell.paragraphs[0].text = ""
            for chunk, bold in _split_bold(block[1]):
                r = cell.paragraphs[0].add_run(plain(chunk))
                r.bold = bold
                r.font.size = Pt(8.5)
            self._set_borders(t, color="BFBFBF")
            self.doc.add_paragraph().paragraph_format.space_after = Pt(2)
        elif kind == "bullets":
            for item in block[1]:
                p = self.doc.add_paragraph(style="List Bullet")
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                for chunk, bold in _split_bold(item):
                    r = p.add_run(plain(chunk))
                    r.bold = bold
                p.paragraph_format.space_after = Pt(2)
        elif kind == "table":
            self._table(block[1])
        elif kind == "figure":
            path, legend, wmm = block[1], block[2], block[3]
            p = self.doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(path, width=Mm(wmm))
            cap = self.doc.add_paragraph()
            cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = cap.add_run(plain(legend))
            r.italic = True
            r.font.size = Pt(8)
            r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)
        elif kind == "pagebreak":
            self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    @staticmethod
    def _set_borders(table, color="808080", sz="4"):
        tbl = table._tbl
        tblPr = tbl.tblPr
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), sz)
            el.set(qn("w:color"), color)
            borders.append(el)
        tblPr.append(borders)

    def _table(self, spec):
        header = spec.get("header")
        rows = spec["rows"]
        widths = spec.get("widths")
        fsize = spec.get("font", 7.5)
        ncols = len(header) if header else len(rows[0])
        t = self.doc.add_table(rows=0, cols=ncols)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.autofit = False

        if header:
            cells = t.add_row().cells
            for i, txt in enumerate(header):
                cells[i].text = ""
                par = cells[i].paragraphs[0]
                r = par.add_run(plain(str(txt)))
                r.bold = True
                r.font.size = Pt(fsize)
                r.font.color.rgb = RGBColor.from_string("FFFFFF")
                par.paragraph_format.space_after = Pt(1)
                self._shade(cells[i], BLEU)

        for ri, row in enumerate(rows):
            cells = t.add_row().cells
            for i, txt in enumerate(row):
                cells[i].text = ""
                par = cells[i].paragraphs[0]
                par.paragraph_format.space_after = Pt(0)
                for chunk, bold in _split_bold(str(txt)):
                    r = par.add_run(plain(chunk))
                    r.bold = bold
                    r.font.size = Pt(fsize)
                if ri % 2 == 1:
                    self._shade(cells[i], GRIS)

        if widths:
            for row in t.rows:
                for i, w in enumerate(widths):
                    row.cells[i].width = Mm(w)
        self._set_borders(t, color="A6A6A6", sz="4")
        if spec.get("caption"):
            cap = self.doc.add_paragraph()
            r = cap.add_run(plain(spec["caption"]))
            r.italic = True
            r.font.size = Pt(7.5)
            r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)
            cap.paragraph_format.space_before = Pt(2)
        else:
            self.doc.add_paragraph().paragraph_format.space_after = Pt(2)

    def cover(self, title_lines, subtitle, info_rows, ref_bloc):
        d = self.doc
        p = d.add_paragraph()
        p.paragraph_format.space_before = Pt(30)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("BUREAU D'ÉTUDES TECHNIQUES — STRUCTURE")
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)

        p = d.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(title_lines[0])
        r.font.size = Pt(24)
        r.font.bold = True
        r.font.color.rgb = RGBColor.from_string(BLEU)

        for line in title_lines[1:]:
            p = d.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(line)
            r.font.size = Pt(15)
            r.font.bold = True
            r.font.color.rgb = RGBColor.from_string(BLEU)
            p.paragraph_format.space_after = Pt(2)

        p = d.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        r = p.add_run(subtitle)
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)

        d.add_paragraph()

        t = d.add_table(rows=0, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for k, v in info_rows:
            cells = t.add_row().cells
            cells[0].text = ""
            cells[1].text = ""
            r = cells[0].paragraphs[0].add_run(plain(k))
            r.bold = True
            r.font.size = Pt(9)
            for chunk, bold in _split_bold(v):
                rr = cells[1].paragraphs[0].add_run(chunk)
                rr.font.size = Pt(9)
                rr.bold = bold
            cells[0].width = Mm(52)
            cells[1].width = Mm(110)
            cells[0].paragraphs[0].paragraph_format.space_after = Pt(2)
            cells[1].paragraphs[0].paragraph_format.space_after = Pt(2)
        self._set_borders(t, color="BFBFBF")

        d.add_paragraph()
        p = d.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(10)
        for chunk, bold in _split_bold(ref_bloc):
            r = p.add_run(plain(chunk))
            r.bold = bold
            r.font.size = Pt(8)
            r.font.color.rgb = RGBColor.from_string(GRIS_FONCE)
        d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

    def save(self, path):
        self.doc.save(path)


# --------------------------------------------------------------------------
# Rendu PDF
# --------------------------------------------------------------------------
def _pdf_styles():
    ss = getSampleStyleSheet()
    st = {
        "body": ParagraphStyle("body", parent=ss["BodyText"], fontName="DV",
                               fontSize=8.6, leading=11.6, alignment=TA_JUSTIFY,
                               spaceAfter=3.5),
        "h1": ParagraphStyle("h1", fontName="DVB", fontSize=13.5, leading=16,
                             textColor=colors.HexColor("#" + BLEU),
                             spaceBefore=10, spaceAfter=5, keepWithNext=1),
        "h2": ParagraphStyle("h2", fontName="DVB", fontSize=10.8, leading=13,
                             textColor=colors.HexColor("#" + BLEU),
                             spaceBefore=8, spaceAfter=3.5, keepWithNext=1),
        "h3": ParagraphStyle("h3", fontName="DVB", fontSize=9.4, leading=11.5,
                             spaceBefore=6, spaceAfter=2.5, keepWithNext=1),
        "cell": ParagraphStyle("cell", fontName="DV", fontSize=7.0, leading=8.5),
        "cellh": ParagraphStyle("cellh", fontName="DVB", fontSize=7.0,
                                leading=8.5, textColor=colors.white),
        "note": ParagraphStyle("note", fontName="DV", fontSize=8.0, leading=10.4,
                               alignment=TA_JUSTIFY),
        "bullet": ParagraphStyle("bullet", parent=ss["BodyText"], fontName="DV",
                                 fontSize=8.6, leading=11.4, alignment=TA_JUSTIFY,
                                 leftIndent=10, bulletIndent=2, spaceAfter=2.5),
        "cap": ParagraphStyle("cap", fontName="DV", fontSize=7.2, leading=9,
                              textColor=colors.HexColor("#" + GRIS_FONCE),
                              alignment=TA_CENTER, spaceBefore=2, spaceAfter=6),
    }
    return st


class PdfWriter:
    def __init__(self, meta, filename):
        _register_fonts()
        self.meta = meta
        self.filename = filename
        self.st = _pdf_styles()
        self.story = []
        self.blocks = []
        self.cover_args = None
        self._replaying = False
        self.doc = BaseDocTemplate(
            filename, pagesize=A4,
            leftMargin=20 * mm, rightMargin=20 * mm,
            topMargin=22 * mm, bottomMargin=18 * mm,
            title=meta["titre_pdf"], author=meta["entete_gauche"],
            subject=meta["sujet_pdf"], creator="BET Structure — Affaire GARENNE")
        frame = Frame(self.doc.leftMargin, self.doc.bottomMargin,
                      self.doc.width, self.doc.height, id="normal",
                      leftPadding=0, rightPadding=0, topPadding=0,
                      bottomPadding=0)
        self.doc.addPageTemplates([
            PageTemplate(id="all", frames=[frame], onPage=self._decor),
        ])

    def _decor(self, canv, doc):
        canv.saveState()
        w, h = A4
        # bandeau
        canv.setFont("DVB", 6.8)
        canv.setFillColor(colors.HexColor("#" + GRIS_FONCE))
        canv.drawString(20 * mm, h - 14 * mm, self.meta["entete_gauche"])
        canv.setFont("DVB", 6.8)
        canv.setFillColor(colors.HexColor("#" + BLEU))
        canv.drawRightString(w - 20 * mm, h - 14 * mm, self.meta["entete_droit"])
        canv.setStrokeColor(colors.HexColor("#" + BLEU))
        canv.setLineWidth(0.7)
        canv.line(20 * mm, h - 15.2 * mm, w - 20 * mm, h - 15.2 * mm)
        # pied
        canv.setFont("DV", 6.5)
        canv.setFillColor(colors.HexColor("#" + GRIS_FONCE))
        canv.drawString(20 * mm, 10 * mm, self.meta["pied_gauche"])
        canv.drawRightString(w - 20 * mm, 10 * mm,
                             f"Page {doc.page} / {self.meta.get('npages', '?')}")
        canv.setStrokeColor(colors.HexColor("#BFBFBF"))
        canv.setLineWidth(0.4)
        canv.line(20 * mm, 13 * mm, w - 20 * mm, 13 * mm)
        canv.restoreState()

    def add(self, block):
        st = self.st
        kind = block[0]
        if kind in ("h1", "h2", "h3"):
            self.story.append(Paragraph(_pdf_rich(block[1]), st[kind]))
        elif kind == "p":
            self.story.append(Paragraph(_pdf_rich(block[1]), st["body"]))
        elif kind == "note":
            inner = Paragraph(_pdf_rich(block[1]), st["note"])
            t = Table([[inner]], colWidths=[self.doc.width])
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#" + GRIS)),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]))
            self.story.append(t)
            self.story.append(Spacer(1, 4))
        elif kind == "bullets":
            for item in block[1]:
                self.story.append(Paragraph(_pdf_rich(item), st["bullet"],
                                            bulletText="\u2022"))
        elif kind == "table":
            self._table(block[1])
        elif kind == "figure":
            path, legend, wmm = block[1], block[2], block[3]
            from PIL import Image as PILImage
            iw, ih = PILImage.open(path).size
            wpx = wmm * mm
            hpx = wpx * ih / iw
            img = Image(path, width=wpx, height=hpx)
            img.hAlign = "CENTER"
            self.story.append(KeepTogether([img,
                                            Paragraph(_pdf_rich(legend), st["cap"])]))
        elif kind == "pagebreak":
            from reportlab.platypus import PageBreak
            self.story.append(PageBreak())
        if kind != "pagebreak" and not self._replaying:
            self.blocks.append(block)

    def _table(self, spec):
        header = spec.get("header")
        rows = spec["rows"]
        widths = spec.get("widths")
        ncols = len(header) if header else len(rows[0])
        avail = self.doc.width / mm
        if widths:
            cw = [w / sum(widths) * avail * mm for w in widths]
        else:
            cw = [avail / ncols * mm] * ncols

        data = []
        if header:
            data.append([Paragraph(_pdf_rich(str(t)), self.st["cellh"])
                         for t in header])
        for row in rows:
            data.append([Paragraph(_pdf_rich(str(t)), self.st["cell"])
                         for t in row])

        cmds = [
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#A6A6A6")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 3),
            ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ("TOPPADDING", (0, 0), (-1, -1), 2.2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
        ]
        if header:
            cmds += [("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#" + BLEU)),
                     ("REPEATROWS", (0, 0), (-1, 0))]
        for ri in range(len(data)):
            if header and ri == 0:
                continue
            idx = ri - 1 if header else ri
            if idx % 2 == 1:
                cmds.append(("BACKGROUND", (0, ri), (-1, ri),
                             colors.HexColor("#" + GRIS)))
        t = Table(data, colWidths=cw, repeatRows=1 if header else 0)
        t.setStyle(TableStyle(cmds))
        # La legende est solidaire du tableau : on evite qu'elle se retrouve
        # seule en tete de page suivante quand le tableau se termine en bas
        # de page.
        cap = None
        if spec.get("caption"):
            cap = Paragraph(_pdf_rich(spec["caption"]), self.st["cap"])
        if cap is not None:
            keep = [t, cap]
            # si le tableau est court, on garde le tout ensemble
            if len(data) <= 14:
                self.story.append(KeepTogether(keep))
            else:
                self.story.append(t)
                self.story.append(cap)
        else:
            self.story.append(t)
            self.story.append(Spacer(1, 5))

    def cover(self, title_lines, subtitle, info_rows, ref_bloc):
        self.cover_args = (title_lines, subtitle, info_rows, ref_bloc)
        from reportlab.platypus import Spacer
        self.story.append(Spacer(1, 22 * mm))
        self.story.append(Paragraph(
            "BUREAU D'ÉTUDES TECHNIQUES — STRUCTURE",
            ParagraphStyle("k", fontName="DVB", fontSize=8.5,
                           textColor=colors.HexColor("#" + GRIS_FONCE),
                           alignment=TA_CENTER)))
        self.story.append(Spacer(1, 6 * mm))
        self.story.append(Paragraph(
            _pdf_rich(title_lines[0]),
            ParagraphStyle("t0", fontName="DVB", fontSize=23, leading=26,
                           textColor=colors.HexColor("#" + BLEU),
                           alignment=TA_CENTER)))
        for line in title_lines[1:]:
            self.story.append(Paragraph(
                _pdf_rich(line),
                ParagraphStyle("t1", fontName="DVB", fontSize=13.5, leading=17,
                               textColor=colors.HexColor("#" + BLEU),
                               alignment=TA_CENTER)))
        self.story.append(Spacer(1, 5 * mm))
        self.story.append(Paragraph(
            _pdf_rich(subtitle),
            ParagraphStyle("sub", fontName="DV", fontSize=10,
                           leading=13, alignment=TA_CENTER,
                           textColor=colors.HexColor("#" + GRIS_FONCE))))
        self.story.append(Spacer(1, 14 * mm))

        data = [[Paragraph(f"<b>{k}</b>", self.st["cell"]),
                 Paragraph(_pdf_rich(v), self.st["cell"])] for k, v in info_rows]
        t = Table(data, colWidths=[52 * mm, 110 * mm])
        t.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#BFBFBF")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ]))
        t.hAlign = "CENTER"
        self.story.append(t)
        self.story.append(Spacer(1, 8 * mm))
        self.story.append(Paragraph(
            _pdf_rich(ref_bloc),
            ParagraphStyle("ref", fontName="DV", fontSize=7.2, leading=9.5,
                           alignment=TA_JUSTIFY,
                           textColor=colors.HexColor("#" + GRIS_FONCE))))
        from reportlab.platypus import PageBreak
        self.story.append(PageBreak())

    def _rebuild(self, target):
        self.doc = BaseDocTemplate(
            target, pagesize=A4,
            leftMargin=20 * mm, rightMargin=20 * mm,
            topMargin=22 * mm, bottomMargin=18 * mm,
            title=self.meta["titre_pdf"], author=self.meta["entete_gauche"],
            subject=self.meta["sujet_pdf"],
            creator="BET Structure — Affaire GARENNE")
        frame = Frame(self.doc.leftMargin, self.doc.bottomMargin,
                      self.doc.width, self.doc.height, id="normal",
                      leftPadding=0, rightPadding=0, topPadding=0,
                      bottomPadding=0)
        self.doc.addPageTemplates([
            PageTemplate(id="all", frames=[frame], onPage=self._decor),
        ])
        self.doc.build(list(self.story))

    def save(self):
        """Rendu en deux passes : la premiere mesure le nombre de pages,
        la seconde l'inscrit reellement dans le pied de page."""
        import io as _io
        import pymupdf

        def _newdoc(target):
            doc = BaseDocTemplate(
                target, pagesize=A4,
                leftMargin=20 * mm, rightMargin=20 * mm,
                topMargin=22 * mm, bottomMargin=18 * mm,
                title=self.meta["titre_pdf"], author=self.meta["entete_gauche"],
                subject=self.meta["sujet_pdf"],
                creator="BET Structure — Affaire GARENNE")
            frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width,
                          doc.height, id="normal", leftPadding=0,
                          rightPadding=0, topPadding=0, bottomPadding=0)
            doc.addPageTemplates([PageTemplate(id="all", frames=[frame],
                                               onPage=self._decor)])
            return doc

        def _emit(target):
            # reconstruit des flowables neufs a chaque passe
            self._replaying = True
            self.doc = _newdoc(target)
            self.story = []
            if self.cover_args:
                self.cover(*self.cover_args)
            for b in self.blocks:
                self.add(b)
            self._replaying = False
            self.doc.build(list(self.story))

        buf = _io.BytesIO()
        _emit(buf)
        with pymupdf.open(stream=buf.getvalue(), filetype="pdf") as d:
            self.meta["npages"] = len(d)
        _emit(self.filename)
        return self.filename


# --------------------------------------------------------------------------
# API unifiee
# --------------------------------------------------------------------------
def _renumber(blocks):
    """Renumerote sequentiellement les tableaux et figures selon leur ordre
    d'apparition, pour garantir une numerotation continue et sans trou."""
    t = f = 0
    out = []
    for b in blocks:
        if b[0] == "table" and b[1].get("caption"):
            t += 1
            cap = re.sub(r"^Tableau\s+\d+", f"Tableau {t}", b[1]["caption"])
            spec = dict(b[1]); spec["caption"] = cap
            out.append(("table", spec))
            continue
        if b[0] == "figure":
            f += 1
            leg = re.sub(r"^Figure\s+\d+", f"Figure {f}", b[2])
            out.append(("figure", b[1], leg, b[3]))
            continue
        if b[0] in ("p", "note"):
            txt = re.sub(r"Tableau\s+(\d+)", lambda m: f"Tableau {m.group(1)}", b[1])
            out.append((b[0], txt))
            continue
        out.append(b)
    return out


def build(meta: dict, blocks, outdir: str, basename: str):
    """Produit basename.docx et basename.pdf a partir des memes blocs."""
    blocks = _renumber(blocks)
    os.makedirs(outdir, exist_ok=True)
    docx_path = os.path.join(outdir, basename + ".docx")
    pdf_path = os.path.join(outdir, basename + ".pdf")

    w = DocxWriter(meta)
    if meta.get("cover"):
        w.cover(*meta["cover"])
    for b in blocks:
        w.add(b)
    w.save(docx_path)

    p = PdfWriter(meta, pdf_path)
    if meta.get("cover"):
        p.cover(*meta["cover"])
    for b in blocks:
        p.add(b)
    p.save()

    return docx_path, pdf_path


def count_pages(pdf_path):
    import pymupdf
    with pymupdf.open(pdf_path) as d:
        return len(d)
