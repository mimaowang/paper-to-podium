# Writing the talk script

Read this when you reach phases 0–2 (intake, research, script writing).

## The length budget comes first, not last

A talk is a fixed number of minutes; a script is a variable number of words. Reconciling them after writing means cutting — and cutting hurts. Derive the budget before drafting:

- Chinese, measured in characters of spoken body text (excluding headings and cues): a relaxed, slightly slow pace is ~200 characters/minute; a brisk news-anchor pace is ~260. For a 25-minute slot at a slightly slow pace, aim for ~5,000 characters and reserve 4–5 minutes for questions if the slot is 30 minutes.
- English, measured in words: ~110–130 words/minute for a measured delivery. A 12-minute conference talk is ~1,400 words.
- When the speaker tells you their pace ("I speak a bit slowly"), believe them and use the low end. Running short feels fine; running over gets you cut off.

After every substantial edit, re-check with `scripts/estimate_talk_length.py`. It strips headings and markup and reports minutes at several rates, so you can see the effect of an edit immediately.

## Write spoken language, not written language

The script will be read aloud by a person standing in front of people. Sentences that look fine on paper can be impossible to say: long nested clauses, chains of modifiers, numbers with false precision. Prefer short sentences. One clause of elaboration per sentence, rarely two. Read a paragraph aloud yourself (literally — move your mouth) if you're unsure it can be spoken.

Numbers deserve special care. Round aggressively: "about seven times" is sayable and memorable; "6.83 times" is neither. Keep at most one or two precise numbers in the whole talk, for the results that deserve them, and say those slowly.

## Structure that works for a literature report

A shape that has served well for paper presentations of 20–30 minutes, especially course reports:

1. **The real-world puzzle** (longer than feels natural — this is what makes people care). Concrete phenomena, prices, official numbers, the policy backstory. For a policy paper this is where the external research pays off.
2. **The research question**, stated in one sentence, plus why it's interesting and why it's answerable (the variation the paper exploits, in plain words).
3. **Data and design, lightly.** What data, what method, each in a sentence or two. In a non-specialist room, the identification strategy is a courtesy mention, not a section — the audience cannot audit it from slides anyway, and minutes spent there are minutes stolen from the story.
4. **Results as a story.** Order findings so each one sets up the next ("prices went up → so who still buys? → more productive firms → and the land gets used more intensively"). Give each finding a name or number ("Finding 1") so the audience can keep count.
5. **What happened afterward** — later policy adjustments, the current state of the world. This is the part audiences remember and ask about, and papers never cover it.
6. **Your own extension** — for course reports with a research-proposal requirement: the logical chain from this paper to your question, kept to a minute or two.

For a talk about your *own* paper, compress 1–2 and expand 4, but keep the same spine.

## The "AI flavor" failure mode — and what plain language looks like

The single most-rejected trait in real user feedback on talk scripts is a performative, essay-ish voice: rhetorical questions fired at the audience, manufactured suspense, punchline reveals, motivational asides. It reads like a TED talk written by someone who has only read TED talk transcripts, and most speakers — especially understated ones — find it embarrassing to say aloud. Default to plain, direct, slightly dry narration unless the user explicitly asks for charisma.

Real before/after examples (from an actual course talk that went through exactly this correction):

- Before: "Why can firms get land this cheaply? Why are local governments willing to lose money on every deal? That is my opening question today."
  After: "工业用地价格这么低，主要原因是地方政府之间的招商竞争。" (State the answer as a fact, as the opening of the section. The question form was adding drama, not information.)
- Before: "My answer is: land." / "先明确一点：地方政府不是慈善家，低价卖地是经过计算的。"
  After: "地方政府这样做，是因为它们看中的不是一次性的土地出让收入，而是企业落地以后带来的税收、就业和 GDP 增长。" (Just the explanation, in the order a person would explain it.)
- Before: "亏到什么程度呢？这笔账是怎么算平的？我给大家捋一条时间线。"
  After: give the timeline. "下面按时间顺序说一下这项政策的来龙去脉。"

Notice the pattern: the plain versions are *shorter*, say the same thing, and trust the material to be interesting. Rhetorical questions are not banned — one genuine question that you then answer substantively can orient a section — but if a sentence exists only to create suspense, cut it.

Other markers of the same failure mode: over-signposting ("Let's dive in!", "Buckle up"), addressing the audience as "you" constantly, emoji-ish enthusiasm ("fascinatingly, ..."), and triplets of adjectives. Write like the speaker talks in a one-on-one conversation about something they find genuinely interesting.

## Signposting and handoffs

Between sections, one plain transition sentence is enough ("数据和方法部分，我只介绍基本思路。"). Within results, name findings ("第一个结果是……") so slide titles and speech line up — this also makes the later page-alignment step trivial, because each script block already knows which slide it belongs to.

## Keeping facts traceable while writing

As you draft, drop a source note after any non-obvious number, in a form you'll strip before printing (e.g. a `> 来源：…` blockquote line). Two categories, kept distinct:

- Paper-internal: cite the table/figure/footnote ("论文表 3 第 2 列"). You will need these when a number "doesn't look right" in the fact-check pass.
- External: cite the issuing body and document, and keep the URL in your research notes. Never let a web-search number into the script without a source you can name — the speaker will be asked, and "I found it online" is not an answer.

These lines are for the speaker and the fact-checker, not for the audience — remove them from the final stage version if the user prefers a clean script (ask, or keep them in a separate notes file).
