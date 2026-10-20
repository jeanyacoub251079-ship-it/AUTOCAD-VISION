#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""md2html.py — conversion Markdown -> HTML pour import Google Docs.

Pas de dépendance externe (pandoc et le module `markdown` sont absents du
sandbox). Gère ce dont nos livrables se servent réellement :

  titres # / ## / ###        tableaux | … |
  gras **, italique *, code `  listes - et 1.
  citations >                règles ---
  images ![..](..) -> texte   liens [..](..) -> texte + URL

Les images locales ne sont PAS embarquées : Google Docs les perdrait de
toute façon. On écrit le chemin en clair, ce qui reste traçable.
"""
import html
import os
import re
import sys


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", t)
    t = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"<i>[image : \2]</i>", t)
    return t


def cells(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_sep(line):
    return bool(re.fullmatch(r"\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?", line.strip()))


def convert(md):
    lines = md.splitlines()
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        st = ln.strip()

        if not st:
            i += 1
            continue

        if re.fullmatch(r"-{3,}|\*{3,}", st):
            out.append("<hr>")
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", st)
        if m:
            lvl = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (lvl, inline(m.group(2)), lvl))
            i += 1
            continue

        # tableau
        if st.startswith("|") and i + 1 < len(lines) and is_sep(lines[i + 1]):
            head = cells(st)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(cells(lines[i].strip()))
                i += 1
            t = ["<table border=1 cellspacing=0 cellpadding=4>", "<tr>"]
            for c in head:
                t.append("<th>%s</th>" % inline(c))
            t.append("</tr>")
            for r in body:
                t.append("<tr>")
                for c in r:
                    t.append("<td>%s</td>" % inline(c))
                t.append("</tr>")
            t.append("</table>")
            out.append("".join(t))
            continue

        # citation
        if st.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append('<blockquote><p>%s</p></blockquote>'
                       % "<br>".join(inline(b) for b in buf if b))
            continue

        # listes
        mo = re.match(r"^(\d+)[.)]\s+(.*)$", st)
        if mo:
            items = []
            while i < len(lines):
                mm = re.match(r"^(\d+)[.)]\s+(.*)$", lines[i].strip())
                if not mm:
                    break
                items.append(mm.group(2))
                i += 1
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        if re.match(r"^[-*+]\s+", st):
            items = []
            while i < len(lines) and re.match(r"^[-*+]\s+", lines[i].strip()):
                items.append(re.sub(r"^[-*+]\s+", "", lines[i].strip()))
                i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(x) for x in items))
            continue

        # paragraphe (lignes consécutives hors structure)
        buf = [st]
        i += 1
        while i < len(lines):
            s2 = lines[i].strip()
            if (not s2 or s2.startswith("#") or s2.startswith("|")
                    or s2.startswith(">") or re.match(r"^[-*+]\s+", s2)
                    or re.match(r"^\d+[.)]\s+", s2)
                    or re.fullmatch(r"-{3,}", s2)):
                break
            buf.append(s2)
            i += 1
        out.append("<p>%s</p>" % "<br>".join(inline(b) for b in buf))
    return "\n".join(out)


CSS = ("body{font-family:Georgia,serif;font-size:10.5pt;line-height:1.42;}"
       "h1{font-size:19pt;}h2{font-size:14pt;}h3{font-size:12pt;}"
       "table{border-collapse:collapse;font-size:8.6pt;width:100%;}"
       "th{background:#e8e8e8;text-align:left;}td,th{border:1px solid #888;}"
       "code{font-family:'Courier New',monospace;font-size:9pt;background:#f2f2f2;}"
       "blockquote{border-left:3px solid #bbb;margin-left:0;padding-left:12px;"
       "color:#333;font-style:italic;}")


def main(src, dst):
    md = open(src, encoding="utf-8").read()
    body = convert(md)
    titre = os.path.basename(src).replace(".md", "")
    doc = ('<html><head><meta charset="utf-8"><style>%s</style></head>'
           "<body>%s</body></html>" % (CSS, body))
    open(dst, "w", encoding="utf-8").write(doc)
    return len(body)


if __name__ == "__main__":
    print(main(sys.argv[1], sys.argv[2]))
