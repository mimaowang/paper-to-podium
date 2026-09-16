#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estimate how long a talk script runs when spoken aloud.

Counts CJK characters and Latin words in the *spoken body* of a Markdown
script (headings, page-turn cues, blockquote source notes, and markup are
stripped) and reports minutes at standard speaking rates.

Usage:
    python estimate_talk_length.py script.md
    python estimate_talk_length.py script.md --rate zh-slow
    python estimate_talk_length.py script.md --target 25

Rates (characters/minute for CJK, words/minute for Latin):
    zh-slow    200   measured, slightly slow Chinese delivery (default for zh)
    zh-normal  240
    en-slow    110   conference-measured English delivery
    en-normal  130   (default for en)

Why this exists: a talk is minutes; a script is words. Checking the
conversion after every substantial edit is far cheaper than cutting a
finished talk down to time.
"""
import argparse
import re
import sys

RATES = {"zh-slow": 200, "zh-normal": 240, "en-slow": 110, "en-normal": 130}

def spoken_text(md: str) -> str:
    out = []
    for raw in md.split("\n"):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#"):                     # headings are wayfinding, not spoken
            continue
        if line.startswith(">"):                     # blockquote = source note, not spoken
            continue
        if line.startswith("【翻") or line.startswith("[TURN"):  # page-turn cues
            continue
        if line.startswith(":::verbatim") or line == ":::":
            continue
        line = re.sub(r"\*\*(.+?)\*\*", r"\1", line)  # unwrap bold/italic
        line = re.sub(r"\*(.+?)\*", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        out.append(line)
    return "\n".join(out)

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("script")
    ap.add_argument("--rate", choices=RATES, help="single rate to report (default: show all relevant)")
    ap.add_argument("--target", type=float, help="target minutes; prints over/under vs each rate")
    args = ap.parse_args()

    text = spoken_text(open(args.script, encoding="utf-8").read())
    cjk = len(re.findall(r"[一-鿿]", text))
    words = len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))

    print(f"spoken body: {cjk} CJK characters, {words} Latin words")
    if args.rate:
        rates = {args.rate: RATES[args.rate]}
    elif cjk >= words:
        rates = {k: v for k, v in RATES.items() if k.startswith("zh")}
    else:
        rates = {k: v for k, v in RATES.items() if k.startswith("en")}
    for name, per_min in rates.items():
        n = cjk if name.startswith("zh") else words
        minutes = n / per_min
        line = f"  {name:10s} ({per_min}/min): {minutes:5.1f} min"
        if args.target:
            diff = minutes - args.target
            line += f"   -> {'OVER' if diff > 0 else 'under'} by {abs(diff):.1f} min vs target {args.target}"
        print(line)
    if cjk and words:
        print("note: mixed-language script; estimate is approximate (numbers/English inside Chinese text add a little time)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
