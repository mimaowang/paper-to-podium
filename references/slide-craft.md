# Slide craft

Read this when you reach phases 3–4 (distilling slides from the script, visual QA).

## Extraction, not compression

The deck is built by *choosing* from the script, not by *shrinking* it. For each slide, ask: if the audience remembers one sentence from these two minutes, which is it? That sentence — plus the number or figure it needs — goes on the slide. Everything else stays in the speaker's mouth.

Two failure modes sit on either side, and both are real:

- **Too much text.** The audience reads ahead and stops listening; the speaker, seeing a wall of text, starts reading it aloud. If a content page needs more than ~6 short bullet lines, it is two pages.
- **Too little text.** The speaker loses their on-screen prompter. Remember the speaker glances at the screen to recall what comes next — slides should carry enough substance to cue the next sentence. A page with three words on it forces memorization. Aim for pages the speaker *could* talk from without the script in a pinch.

Page count is free. Never crowd a page to save a page.

## Typography for the back row

Defaults this workflow converged on after several rounds of "make it bigger / now slightly smaller":

- Beamer 16:9 (`aspectratio=169`), base font 11–12pt. Body text below 10pt is invisible past row three.
- Slide titles one notch larger than body, bold — not huge. Oversized titles eat the page.
- Numbers and Latin text in a serif (Times New Roman) when the body is a sans CJK font — mixed scripts look noticeably more professional, and audiences do notice.
- One highlight color from the theme (e.g. the institution's red) for the key numbers; define a `\hl` command and use it sparingly — if everything is highlighted, nothing is.
- Define a `\srcnote` command (tiny, gray) for source lines at page bottoms: "数据来源：……" or "Figure 3 of the paper". Tiny gray sources signal rigor without costing attention.

For CJK decks, `\usepackage{ctex}` with a hei-style font (Microsoft YaHei / Source Han Sans) reads far better from a distance than song-style fonts.

## The key-points page → figure page split

The most valuable layout pattern in this skill, discovered when dense "text left, figure right" pages kept failing on both duties:

Split such a page into **two pages**:

1. **Key-points page** — the distilled, load-bearing sentences, well typeset, full width. This is the page that carries the argument.
2. **Figure page** — the figure large on one side (as large as possible without touching the theme's header/footer decorations), and beside it, in smaller text, the *secondary* script paragraphs: context, caveats, the "nice to say while they look at the picture" material that didn't make the key-points cut.

Why this works so well: while the audience studies the figure, the speaker reads the secondary text *straight off the slide* — those minutes require zero memorization, and the talk's total information goes up without crowding anything. Mark these verbatim-on-slide paragraphs in the script (see `qa-and-rehearsal.md` on the print version) so the speaker knows: on this page, the script and the screen are the same — just read the screen.

## Figures

**Which figures to take: the skill is to *identify* the paper's 2–4 most important visual results, not to find *a* figure.** A deck built from this workflow typically ends up with too few figures if you only grab what's convenient. Before writing any slide, go through the paper's figures and tables once and rank them by how much of the argument each one carries:

1. **First priority: the paper's visual core** — the figures a referee would ask about: event-study / dynamic-effect plots, maps of the key variation, density or distribution shifts, mechanism diagrams, reduced-form discontinuities. In empirical economics papers there are usually two to four of these, and they are the slides' figure pages.
2. **Worth taking if time allows**: descriptive maps or trend charts that make the setting concrete (these often live in the *appendix* — check it; appendix figures are frequently more presentation-friendly than main-text coefficient plots).
3. **Never**: regression tables as screenshots. If a table result matters, restate it as one sentence with its number. A dense table on screen is a wall of text with extra steps.

Minor figures and tables that don't carry the argument stay out — the goal is coverage of what matters, not completeness.

Then extract at high resolution and crop tightly:

- **Paper figures**: render the PDF page at 300dpi and crop. Example (poppler): `pdftoppm -png -r 300 -f 7 -l 7 paper.pdf fig` renders page 7, then crop with `pdftoppm`'s `-x -y -W -H` flags (crop-box coordinates in pixels at the given dpi) or any image tool. Screenshotting at screen resolution produces blurry axis labels — don't.
- **External figures**: official statistical charts, reputable outlets. No watermarks, no blurry screenshots, no decorative stock photos, and no screenshots of policy documents (a page of red-header PDF is the visual equivalent of a wall of text). If the user requests a specific image — a particular film still, a particular photo — find exactly that one, not a substitute.
- Every figure needs a one-line caption saying what it is and where it's from (`\srcnote`).

## Templates

If the user has an institutional template, use it. Otherwise:

1. **Default to the bundled skeleton** (`assets/beamer-skeleton.tex`). It uses **Metropolis** (github.com/matze/mtheme, ~7k stars — the most-starred general Beamer theme, and the reference for "minimal and professional"), which ships with every full TeX Live / MiKTeX as `beamertheme-metropolis`, so there is nothing to install. If the user wants something else, GitHub themes for their institution ("Beamer <university>", prefer more stars and recent fixes) are the next stop.
2. **For CJK decks, uncomment the skeleton's CJK block** — it is tested and known-good. Two traps it exists to prevent, both discovered the hard way on MiKTeX: ctex's default fontset demands fonts that fail to load, and `newtxtext` loaded before ctex poisons CJK font lookup. Both failure modes produce a PDF that **compiles with exit code 0 but shows empty boxes instead of Chinese**.
3. **Compile the pristine skeleton first and LOOK at the glyphs.** Because of the above, "xelatex exited cleanly" proves nothing — render page 1 and confirm the characters are actually there before writing any content. Missing-glyph checks are part of the visual QA loop below, not an afterthought.
4. Customize the identity fields (name, institute, date) and remove title-page elements meant for other occasions (e.g. "开题报告" banners on thesis templates).
5. Keep a cleaned copy somewhere permanent — after one talk, the user owns a proven template, and the next talk starts from it.

## The visual QA loop

After every meaningful edit: compile (XeLaTeX for CJK decks), render pages to PNGs (`scripts/render_pdf_pages.sh`), and *look at every page*. What to check for:

- text overflowing the frame or running into the theme's header/footer bars;
- **missing glyphs** — empty boxes (tofu) where characters should be, especially CJK; xelatex exits 0 while dropping glyphs, so this is a *looking* check, not a log check;
- figures touching decorative elements, or scaled so small their axis text is unreadable;
- alignment within a page (e.g. three dates in a timeline that don't line up — a real piece of user feedback; misalignment "looks uncomfortable" even when users can't name why);
- orphaned pages with two words on them, and crowded pages that should split;
- font-size hierarchy: titles, body, and secondary text should each be consistent across pages.

Fix what you see, re-render, look again. When reporting to the user, mention what you checked — "I looked at all 23 pages" is a meaningful claim; "it compiles" is not.
