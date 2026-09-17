# Verification and stage materials

Read this when you reach phases 5–6 (fact-check, blind review, page alignment, print version).

## The fact-check pass

Do this once, after the script is otherwise stable, and do it against sources — not against your memory of the sources.

- **Paper-internal claims.** Re-open the paper and check every number, table/figure reference, and author-year citation in the script. Common drift: a coefficient rounded the wrong way, a sample period off by a year, "significant at 5%" where the table says 10%.
- **External claims.** For each externally-sourced fact, confirm the issuing body, document name, and date match what the script says. If a number cannot be re-traced to its source, soften the sentence ("有审计报告显示……" → drop the precise figure) or cut it. A talk survives a vague sentence; it does not survive a confidently wrong one.

The user asked for "no big factual errors; small imprecision is fine." That is the right standard: check hard for material errors (wrong policy year, wrong direction of an effect, misattributed finding), and don't litigate rounding.

Fix the script *and* flag any place where the same error lives in the slides — they are separate artifacts and drift apart silently.

## The proofread pass (language, not facts)

Fact-checking catches wrong numbers; it does not catch wrong characters. After the script stabilizes, do one separate read purely for language — or hand the script to a fresh reader for exactly this. What to look for:

- Typos and dropped characters. In Chinese scripts: a missing 的/了, homophone swaps, doubled words (a real one that shipped: "项目最初的目很朴素" — missing 的). In English: duplicated words ("the the"), agreement slips.
- Redundant hedges the speaker will trip on ("大约有上百名" — pick one).
- Any sentence you stumble over while reading silently; the speaker will stumble on it at the podium.

This pass earns its keep because the deck *quotes* the script: a typo in the script is a typo on the projector, copied verbatim onto a slide. Fix the script first, then re-sync every slide that quotes the paragraph, and regenerate the print PDF.

## The blind-audience review

The strongest cheap test of a deck: give it to a reader with zero context. Spawn a fresh subagent (or ask a colleague) whose entire knowledge of the talk is the slides PDF. Tell them only the occasion ("this is a course literature presentation") and ask them to report: what they think the talk is about, where they got lost, which pages they'd skip, what questions they'd ask at the end.

You are looking for two kinds of findings:

- **Real problems** — a logic jump the slides don't bridge, a figure nobody can parse without the paper, a section that reads as filler. Fix these.
- **Taste differences** — "I'd make it more academic." The deck was calibrated for its room in phase 0; don't recalibrate for a reviewer who wasn't in it.

This works because you, having written everything, can no longer see the talk with fresh eyes. The blind reviewer can.

**If no subagent mechanism is available** in the environment you're running in, don't skip the fresh-eyes check — degrade it gracefully: ask the user (or a colleague) to flip through the deck, or do a self-review after a real break using a fixed checklist (What is this talk about? Where does the logic jump? Which page would I cut? What question would I ask?). A degraded blind review still catches the logic jumps; what it can't catch is your own blind spots — say so when you report.

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
- **Source notes in gray, two sizes down.** `> 来源：…` lines are for fact-checking and Q&A prep, not for reading aloud — footnote-size gray keeps them findable without competing with the spoken text.
- Regenerate from the Markdown after every script edit — never hand-edit the PDF's source. One command, always in sync.

**When you hand over the print PDF, explain the two markup conventions in one sentence.** Users who didn't build the file won't guess them: "（…）括号小字 = 这部分 PPT 上有，照屏幕念；灰色小字 = 来源注记，备查不用念。" A legend the user never received is a bug, not a feature.

## Rehearsal note

Suggest (don't insist on) one full read-aloud with a timer before the talk, using the printed script and advancing the real deck. It is the only test that exercises the actual deliverable — a person, a script, the slides, and a clock — and it reliably finds the two or three sentences that can't be said aloud, which no amount of reading catches.
