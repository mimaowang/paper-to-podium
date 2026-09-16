# Verification and stage materials

Read this when you reach phases 5–6 (fact-check, blind review, page alignment, print version).

## The fact-check pass

Do this once, after the script is otherwise stable, and do it against sources — not against your memory of the sources.

- **Paper-internal claims.** Re-open the paper and check every number, table/figure reference, and author-year citation in the script. Common drift: a coefficient rounded the wrong way, a sample period off by a year, "significant at 5%" where the table says 10%.
- **External claims.** For each externally-sourced fact, confirm the issuing body, document name, and date match what the script says. If a number cannot be re-traced to its source, soften the sentence ("有审计报告显示……" → drop the precise figure) or cut it. A talk survives a vague sentence; it does not survive a confidently wrong one.

The user asked for "no big factual errors; small imprecision is fine." That is the right standard: check hard for material errors (wrong policy year, wrong direction of an effect, misattributed finding), and don't litigate rounding.

Fix the script *and* flag any place where the same error lives in the slides — they are separate artifacts and drift apart silently.

## The blind-audience review

The strongest cheap test of a deck: give it to a reader with zero context. Spawn a fresh subagent (or ask a colleague) whose entire knowledge of the talk is the slides PDF. Tell them only the occasion ("this is a course literature presentation") and ask them to report: what they think the talk is about, where they got lost, which pages they'd skip, what questions they'd ask at the end.

You are looking for two kinds of findings:

- **Real problems** — a logic jump the slides don't bridge, a figure nobody can parse without the paper, a section that reads as filler. Fix these.
- **Taste differences** — "I'd make it more academic." The deck was calibrated for its room in phase 0; don't recalibrate for a reviewer who wasn't in it.

This works because you, having written everything, can no longer see the talk with fresh eyes. The blind reviewer can.

## Page-turn markers: aligning the script to the deck

The speaker holds the script and drives the slides; the script must tell them when to advance. Once the deck's page numbering is final, annotate the script:

- One marker per slide transition, in a consistent format: `【翻页 → 第 5 页】` (or `[TURN → p.5]` for English). Just the target page number — the speaker glances for half a second mid-sentence; extra words ("…现在我们看第三部分") are noise at the podium.
- A two-page jump gets its own marker (`【翻两页 → 第 3 页】`), because skipping a page by accident and noticing mid-sentence is exactly the kind of moment these markers exist to prevent.
- Typeset the marker *attached to the paragraph that follows it* (the text for the new page), with blank space before it. The speaker's eye should land: marker → the words they say next. Space between marker and its paragraph sends the eye to the wrong place.

Markers go between paragraphs, never mid-paragraph. If one script block spans two slides, split the block at the transition point.

Because page numbers shift as the deck evolves, do this alignment once, late, after the deck is frozen — and verify by counting: the number of markers should equal the number of slide transitions the speaker actually performs (title page usually has no marker; a skipped framework/agenda page explains a "翻两页").

## The print-ready script

For a printed script to read from at the podium, generate a PDF from the script Markdown with `scripts/script_to_print_pdf.py` (XeLaTeX; handles CJK). Its conventions, each learned from real use:

- **Body text 11–12pt with ~1.3 line spacing.** Smaller strains the eyes under stage lighting; larger balloons the page count and the speaker loses the page-position memory that comes from a stable layout.
- **Headings small.** Block headings ("第 11–12 页 · 发现一：成交价格上升 | 约 2 分钟") are wayfinding, not content — normal size, bold. Large headings waste the speaker's glance on navigation.
- **Slide-verbatim paragraphs wrapped in full-width parentheses, one size smaller.** Paragraphs that appear word-for-word on a slide (the figure pages' side text) will be read off the *screen*, so the paper copy is only a backup. Mark them with （…） and set them one size smaller than body. Do this with parentheses plus size, not a color — the script will be printed black-and-white, and a "dark blue" annotation is a gray smudge on a department printer. Mark these paragraphs in the Markdown with a `:::verbatim` fence (or pass their opening words via `--dup-keys-file`); the script does the rest.
- **Turn cues in gray bold**, spaced as described above.
- Regenerate from the Markdown after every script edit — never hand-edit the PDF's source. One command, always in sync.

## Rehearsal note

Suggest (don't insist on) one full read-aloud with a timer before the talk, using the printed script and advancing the real deck. It is the only test that exercises the actual deliverable — a person, a script, the slides, and a clock — and it reliably finds the two or three sentences that can't be said aloud, which no amount of reading catches.
