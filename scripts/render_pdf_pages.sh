#!/usr/bin/env bash
# Render every page of a PDF to a PNG for visual inspection.
#
# The visual QA loop (see references/slide-craft.md): compile, render,
# then LOOK at every page. 70 dpi is enough for layout checks
# (crowding, overflow, alignment); use 150 to read small text.
#
# Usage:
#   ./render_pdf_pages.sh slides.pdf            # all pages at 70 dpi
#   ./render_pdf_pages.sh slides.pdf 150        # all pages at 150 dpi
#   ./render_pdf_pages.sh slides.pdf 150 3 5    # pages 3-5 only
#
# Output: <pdf-stem>-page-<N>.png in a directory named <pdf-stem>_pages/
# next to the PDF. Requires pdftoppm (poppler), which ships with MiKTeX
# and is available via package managers elsewhere.
set -euo pipefail

PDF="${1:?usage: render_pdf_pages.sh file.pdf [dpi] [first] [last]}"
DPI="${2:-70}"
FIRST="${3:-}"
LAST="${4:-}"

DIR="$(dirname "$PDF")"
STEM="$(basename "$PDF" .pdf)"
OUT="$DIR/${STEM}_pages"
mkdir -p "$OUT"

ARGS=(-png -r "$DPI")
if [ -n "$FIRST" ] && [ -n "$LAST" ]; then
  ARGS+=(-f "$FIRST" -l "$LAST")
fi

pdftoppm "${ARGS[@]}" "$PDF" "$OUT/$STEM-page"
echo "rendered to: $OUT"
ls "$OUT"
