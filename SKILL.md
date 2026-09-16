---
name: paper-to-podium
description: Build a complete spoken presentation from an academic paper — the talk script AND the slides, taken all the way to a rehearsed, fact-checked, print-ready state. Use whenever the user needs to present a paper (their own or someone else's) at a journal club, class/seminar presentation, conference, group meeting, or defense rehearsal — especially when they mention a time budget, a talk script / speaker notes, or slides based on a paper. Also triggers for requests phrased in Chinese such as 文献汇报、课堂展示、组会汇报、讲稿、slides/PPT 制作. Do not use for posters, for slides with no spoken component, or for writing the paper itself.
---

# Paper to Podium

Turn an academic paper into a talk that a real person can stand up and deliver: a spoken script timed to the minute, slides distilled from that script, and the small finishing touches (page-turn cues, a print-ready script) that make the difference between reading notes off a screen and actually presenting.

This skill encodes one strong opinion, validated over many iterations of real talks:

**The script is the talk. The slides are an excerpt of the script — never the other way around.**

If you start with slides, you end up with dense bullet pages that the speaker reads aloud while the audience reads ahead. If you start with the script, the slides become what they should be: the few sentences and figures the audience should look at while the speaker talks. Every phase below follows from this.

## The workflow at a glance

0. **Intake** — pin down occasion, audience, duration, and extra requirements before writing a word.
1. **Read & research** — read the paper end to end; research the institutional and real-world background the paper assumes but doesn't spell out.
2. **Write the script** — to a length budget derived from the time limit, in plain spoken language.
3. **Distill the slides** — extract the load-bearing sentences and figures from the script; design for the back row.
4. **Visual QA loop** — render every page to an image and look at it; fix what looks off. Repeat.
5. **Verify** — a fact-check pass against paper and sources, then a blind review by a fresh "audience" that has only seen the slides.
6. **Stage materials** — align the script to slide pages with turn cues; produce a print-friendly script with slide-verbatim paragraphs marked.

The phases are ordered by dependency, not by ceremony. If the user already has a script, jump in at phase 3. If they only want a deck review, run phases 4–5. The skill's job is to keep the script-first dependency straight, not to force every step.

Detailed guidance lives in three references — read them when you reach the relevant phase, not upfront:

- `references/script-writing.md` — phases 0–2: timing math, spoken style, structure, the "AI flavor" failure mode with real before/after examples.
- `references/slide-craft.md` — phases 3–4: extraction vs. compression, typography, the key-points-page → figure-page split, figure sourcing, template hunting, the visual QA loop.
- `references/qa-and-rehearsal.md` — phases 5–6: fact-checking with traceable sources, blind-audience review, page-turn markers, the print-ready script.

Bundled scripts (use them instead of reinventing):

- `scripts/estimate_talk_length.py <file.md> [--rate zh-slow|zh-normal|en-slow|en-normal]` — reports how many minutes the script runs at a given speaking rate. Run it after every substantial script edit; a talk that is 20% over budget is a talk that gets cut off.
- `scripts/script_to_print_pdf.py <file.md> --title "..." [--compile]` — converts the page-marker-annotated script (Markdown) into a print-ready PDF via XeLaTeX: small headings, comfortable body text, page-turn cues in gray, and paragraphs that appear verbatim on the slides wrapped in full-width parentheses and set one size smaller — the speaker reads those off the screen, so the paper copy is only a backup, and parentheses plus a size difference (unlike a color) survive black-and-white printing.
- `scripts/render_pdf_pages.sh <file.pdf> [dpi]` — renders every PDF page to a PNG for the visual QA loop.

`assets/beamer-skeleton.tex` is a 16:9 Beamer starting point built on Metropolis (the most-starred general Beamer theme, shipped with TeX Live/MiKTeX), with a tested CJK block, the typography defaults this workflow converged on, and an example of each page pattern. Use it when the user has no institutional template; when they do, prefer theirs.

## Phase 0 — Intake

Four answers change everything downstream; get them from the user or infer them from context before writing:

- **Occasion and rigor level.** A course literature report is storytelling plus institutional background — the identification strategy gets one sentence, not a section. A seminar for specialists is the opposite. Most failed talks are calibrated for the wrong room.
- **Duration, and the speaker's pace.** Ask, or assume a slightly slow pace — it is far more common to run over than under. The length budget in phase 2 depends on this.
- **Required extras.** Course presentations often carry specific assignments: connect to the home country's real-world situation, close with your own research idea, compare two papers. These are graded components, not optional garnish — schedule minutes for them.
- **Language.** Script and slides should be in the language the talk will be given in, from the first draft. Translating a finished script wastes a full iteration.

## Phase 1 — Read & research

Read the whole paper, including appendix figures that look presentation-worthy. Then research what the paper takes for granted: for a policy paper, the policy's backstory, implementation timeline, sibling policies, and what happened afterward. Audiences reliably ask about exactly this material, and it is what turns a paper summary into a talk.

One discipline matters here: **every number that will be said aloud must be traceable.** Keep a running source list that separates two kinds of claims — paper-internal claims (cite the table/figure/footnote: "Table 3, column 2") and external facts (cite the document or outlet). You will need this list twice later: for the fact-check pass, and when the audience asks "where does that number come from?"

## Phases 2–6

Read the three reference files as you reach each phase. Two habits cut across all of them:

**Look at the output, don't trust the source.** LaTeX that compiles is not slides that read well. After every meaningful change, render the PDF pages to images (`scripts/render_pdf_pages.sh`) and view them. Crowded pages, misaligned timelines, oversized numbers, figures colliding with theme decorations — you only catch these by looking. Treat "I looked at every page" as the definition of done for the deck.

**Iterate in small, reversible steps.** Real users review drafts and give feedback like "the background section runs long, the mechanism part runs short — shift a little, not a lot." Make the smallest edit that addresses the note, re-render, show. Don't restructure on each round; the overall shape was agreed early and churn destroys trust.

## What "done" looks like

- A script whose spoken length, at the speaker's actual pace, lands inside the time budget with margin for questions.
- Slides where every page passes a visual check: readable from the back, one idea per page, no orphaned two-word pages, no walls of text, and the paper's 2–4 argument-carrying figures are on figure pages (see `references/slide-craft.md` on identifying them).
- A fact-check that found no material errors, with sources on file for the numbers.
- A blind reviewer (fresh context, saw only the slides) who could follow the talk's logic without the paper.
- A print-ready script with page-turn cues matching the final deck's page numbers, and slide-verbatim paragraphs visibly marked.
