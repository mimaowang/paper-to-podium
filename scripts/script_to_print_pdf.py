#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert a page-marker-annotated talk script (Markdown) into a print-ready
PDF for the podium, via XeLaTeX.

Conventions (see references/qa-and-rehearsal.md for the reasoning):
  * body 12pt with ~1.3 line spacing  — readable under stage lighting
  * '## ' block headings small+bold   — wayfinding, not content
  * page-turn cues in gray bold, attached to the paragraph that FOLLOWS them
  * paragraphs that appear verbatim on the slides are wrapped in full-width
    parentheses and set one size smaller: the speaker reads those off the
    screen, so the paper copy is only a backup. Parentheses plus a size
    difference (unlike a color) survive black-and-white printing.

Markdown conventions understood:
  # Title                 document title (replaced by --title)
  ## Heading              block heading
  【翻页 → 第 5 页】        page-turn cue (customize with --cue-regex;
  [TURN -> p.5]           both defaults recognized)
  :::verbatim ... :::     paragraph(s) shown word-for-word on a slide
  > note                  source note (rendered small; drop with --drop-notes)
  **bold**, *italic*      inline markup

Usage:
    python script_to_print_pdf.py talk.md --title "My Talk Script" --compile
    python script_to_print_pdf.py talk.md --title "..." --dup-keys-file dups.txt
    python script_to_print_pdf.py talk.md --lang en --title "..." --compile

--dup-keys-file: a UTF-8 text file with one paragraph-opening string per
line; paragraphs starting with any of these strings are also treated as
slide-verbatim. Useful when fences would clutter a shared Markdown file.

Requires: xelatex with ctex (any TeX Live / MiKTeX full install) when
--compile is given. Chinese font defaults to Microsoft YaHei with a
Noto/Source Han fallback chain — override with --cjk-font.
"""
import argparse
import os
import re
import subprocess
import sys

def esc(s: str) -> str:
    for a, b in [("\\", r"\textbackslash{}"), ("%", r"\%"), ("&", r"\&"),
                 ("#", r"\#"), ("_", r"\_"), ("$", r"\$"),
                 ("^", r"\textasciicircum{}"), ("~", r"\textasciitilde{}")]:
        s = s.replace(a, b)
    return s

def inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"\*(.+?)\*", r"\\textit{\1}", s)
    return s

CUE_DEFAULTS = [r"^【翻", r"^\[TURN"]

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script")
    ap.add_argument("--title", required=True, help="document title printed at the top")
    ap.add_argument("--out", help="output .tex path (default: <script>_print.tex alongside input)")
    ap.add_argument("--cue-regex", action="append", default=[],
                    help="extra regex for page-turn cue lines (anchored at line start); repeatable")
    ap.add_argument("--dup-keys-file", help="file with paragraph-opening strings, one per line")
    ap.add_argument("--drop-notes", action="store_true", help="omit '> ' blockquote source notes entirely")
    ap.add_argument("--lang", choices=["zh", "en"], default="zh",
                    help="zh: ctexart + CJK fonts; en: article + Times-like fonts")
    ap.add_argument("--cjk-font", default="Microsoft YaHei")
    ap.add_argument("--body-size", default="12pt", choices=["10pt", "11pt", "12pt"])
    ap.add_argument("--compile", action="store_true", help="run xelatex twice after writing the .tex")
    args = ap.parse_args()

    cue_res = [re.compile(p) for p in (CUE_DEFAULTS + args.cue_regex)]
    dup_keys = []
    if args.dup_keys_file:
        dup_keys = [ln.strip() for ln in open(args.dup_keys_file, encoding="utf-8")
                    if ln.strip() and not ln.startswith("#")]

    body, verbatim = [], False
    for raw in open(args.script, encoding="utf-8").read().split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("# "):
            continue
        if line.strip() == "---":
            continue
        if line.strip() == ":::verbatim":
            verbatim = True
            continue
        if line.strip() == ":::":
            verbatim = False
            continue
        if line.startswith("## "):
            body.append(r"\blkhead{%s}" % inline(line[3:].strip()))
            continue
        if any(r.search(line) for r in cue_res):
            body.append(r"\flip{%s}" % inline(line.strip()))
            continue
        if line.startswith(">"):
            if not args.drop_notes:
                body.append(r"\srcline{%s}" % inline(line.lstrip("> ").strip()))
            continue
        dup = verbatim or any(line.startswith(k) for k in dup_keys)
        body.append((r"\pptdup{%s}" if dup else r"\para{%s}") % inline(line.strip()))

    if args.lang == "zh":
        preamble = (r"""\documentclass[__SIZE__,a4paper]{ctexart}
\usepackage[margin=2.2cm]{geometry}
\setmainfont{Times New Roman}
\setCJKmainfont[BoldFont={__FONT__ Bold}]{__FONT__}
\setCJKsansfont[BoldFont={__FONT__ Bold}]{__FONT__}"""
            .replace("__SIZE__", args.body_size)
            .replace("__FONT__", args.cjk_font))
    else:
        preamble = (r"""\documentclass[__SIZE__,a4paper]{article}
\usepackage[margin=2.2cm]{geometry}
\usepackage{newtxtext}"""
            .replace("__SIZE__", args.body_size))

    tex = preamble + r"""
\usepackage{xcolor}
\usepackage{setspace}
\definecolor{flipgray}{RGB}{90,90,90}
\setstretch{1.32}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
% block heading: wayfinding only — small, bold
\newcommand{\blkhead}[1]{\vspace{10pt}{\normalsize\bfseries #1}\par\vspace{2pt}}
% page-turn cue: gray bold, spaced above, attached to what follows
\newcommand{\flip}[1]{\vspace{16pt}{\normalsize\bfseries\color{flipgray} #1}\par\vspace{0pt}}
% ordinary spoken paragraph
\newcommand{\para}[1]{#1\par}
% slide-verbatim paragraph: wrapped in full-width parentheses, one size smaller
% (read off the screen; B/W-print safe — no color needed)
\newcommand{\pptdup}[1]{{\small （#1）}\par}
% source note line: two sizes smaller — on file for Q&A, not read aloud
\newcommand{\srcline}[1]{{\footnotesize\color{flipgray} #1}\par}
\title{\vspace{-1.5cm}{\Large\bfseries __TITLE__}\vspace{-0.5em}}
\date{}
\begin{document}
\maketitle
\vspace{-1.5em}

__BODY__

\end{document}
""".replace("__TITLE__", inline(args.title)).replace("__BODY__", "\n".join(body))

    out = args.out or re.sub(r"\.[^.]+$", "", args.script) + "_print.tex"
    open(out, "w", encoding="utf-8", newline="\n").write(tex)
    print("tex written:", out)

    if args.compile:
        cwd = os.path.dirname(os.path.abspath(out))
        job = os.path.splitext(os.path.basename(out))[0]
        for i in range(2):
            r = subprocess.run(["xelatex", "-interaction=nonstopmode", job + ".tex"],
                               cwd=cwd, capture_output=True, text=True)
            if r.returncode != 0:
                tail = "\n".join((r.stdout + r.stderr).splitlines()[-25:])
                print("xelatex FAILED (pass %d):\n%s" % (i + 1, tail), file=sys.stderr)
                return 1
        print("pdf written:", os.path.join(cwd, job + ".pdf"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
