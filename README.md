# paper-to-podium

**Turn an academic paper into a talk you can actually deliver.** You give it a paper and a time budget; it gives you back three things: a spoken script timed to the minute, slides distilled from that script, and a print-ready podium script with page-turn cues. Built for journal clubs, course presentations, conference talks, and group meetings — for your own paper or someone else's.

[English](#paper-to-podium) | [中文](#paper-to-podium-1)

## The one idea behind it

**The script is the talk. The slides are an excerpt of the script — never the other way around.**

Agents (and people) instinctively start with slides, which produces dense bullet pages that get read aloud while the audience reads ahead. paper-to-podium reverses the dependency: write what you will *say* first, sized to your minutes and your speaking pace, then extract the few sentences and figures worth putting on screen. The result is a talk, not a document with a person attached.

## Quick start

1. Install — copy the skill into your agent's user skills directory:
   ```bash
   cp -r paper-to-podium ~/.claude/skills/    # Claude Code
   cp -r paper-to-podium ~/.agents/skills/    # Kimi Code
   ```
2. Use — just ask naturally, e.g.:
   > "I need to present this paper in class next week, 30 minutes including Q&A. Help me prepare the talk script and slides."

   The skill triggers on requests like this (also 文献汇报 / 课堂展示 / 组会汇报 / 讲稿). It will ask about occasion, audience, and your speaking pace, then run the full pipeline below.

## What you get

- **A talk script written to a time budget** — minutes × speaking rate = target length (25 min of measured Chinese ≈ 5,000 characters; 12 min of conference English ≈ 1,400 words), re-checked after every edit with a bundled tool. Plain spoken language, with explicit guardrails against the "AI flavor" failure mode (rhetorical-question openers, manufactured suspense) — including real before/after examples.
- **Slides designed for the back row** — one idea per page, big type, and a *key-points page → figure page* split: the figure fills one page while the speaker reads secondary text off the screen beside it, so nothing needs memorizing.
- **A fact-check and a blind review** — every spoken number re-traced to the paper or a named source, then a fresh agent with zero context reviews the deck as a new audience member would.
- **A print-ready podium script** — page-turn cues aligned to the final deck (`[TURN → p.5]`), and slide-verbatim paragraphs wrapped in parentheses at a smaller size (readable on black-and-white prints; you read those off the screen anyway).

## How it works

```
read the paper ──▶ research the background (sources on file)
      │                    │
      ▼                    ▼
write the script ◀── length budget = minutes × speaking rate
      │
      ▼
distill the slides ──▶ visual QA: render every page, look at it, fix
      │
      ▼
fact-check + blind-audience review
      │
      ▼
page-turn cues + print-ready script  ──▶  you, presenting
```

Each phase has a dedicated reference file with the reasoning and the failure modes — read the SKILL.md for the map. If you already have a script, jump in at the slides phase; the phases are ordered by dependency, not ceremony.

## Bundled tools

| Tool | What it does |
|---|---|
| `scripts/estimate_talk_length.py` | Script → minutes at standard speaking rates (Chinese & English). Run after every substantial edit. |
| `scripts/script_to_print_pdf.py` | Script Markdown → print-ready PDF via XeLaTeX: turn cues, small headings, slide-verbatim paragraphs in parentheses at a smaller size. |
| `scripts/render_pdf_pages.sh` | Render every PDF page to PNGs for the visual QA loop. |
| `assets/beamer-skeleton.tex` | 16:9 Beamer starting deck on the Metropolis theme (~7k stars, ships with TeX Live/MiKTeX), with a tested CJK block and both page patterns. |

## Repository layout

```
paper-to-podium/
├── SKILL.md                      # the workflow; what the agent reads when triggered
├── references/
│   ├── script-writing.md         # timing math, spoken style, structure, AI-flavor pitfalls
│   ├── slide-craft.md            # extraction vs compression, typography, figure pages, visual QA
│   └── qa-and-rehearsal.md       # fact-check, blind review, page cues, print version
├── scripts/                      # the three tools above
├── assets/beamer-skeleton.tex
└── evals/evals.json              # realistic test prompts
```

## Requirements

- Python 3 (standard library only) for the tools.
- XeLaTeX with `ctex` (any full TeX Live / MiKTeX install) for slides and the print script.
- `pdftoppm` (poppler; ships with MiKTeX) for page rendering.

## Origin

Distilled from a real end-to-end project: a 30-minute Chinese course presentation of an economics paper — script, 23-page Beamer deck, institutional template, fact-check, blind review, print-ready annotated script — that went through ~15 rounds of user feedback. The references preserve what the feedback taught, including the failures (the phrases the speaker refused to say, the layouts that looked fine in LaTeX and bad on screen).

## License

MIT — see [LICENSE](LICENSE). The skeleton uses the Metropolis theme (© Matthias Vogelgesang, LPPL, loaded as a system package); institutional themes you fetch from GitHub carry their own licenses.

---

# paper-to-podium

**把一篇学术论文变成一场你站上台真能讲的汇报。** 你给它一篇论文和一个时长，它还你三样东西：按分钟算准的口语讲稿、从讲稿里提炼出来的 slides、以及一份带翻页提示的打印版上台讲稿。适用于文献汇报、课堂展示、组会、会议报告——讲自己的论文或别人的都行。

[English](#paper-to-podium) | [中文](#paper-to-podium-1)

## 它背后的一个核心理念

**讲稿是汇报本身，slides 是讲稿的节选——顺序绝不能反。**

Agent（和人）的本能是先做 PPT，结果是密密麻麻的要点页：汇报人照着念，观众提前读完。paper-to-podium 把依赖关系倒过来：先写你要"说"的话，按你的语速和时长定量；再从中挑出值得放上屏幕的那几句和几张图。最终得到的是一场汇报，而不是一份配了人的文档。

## 快速上手

1. 安装——把 skill 复制进你的 agent 的用户 skill 目录：
   ```bash
   cp -r paper-to-podium ~/.claude/skills/    # Claude Code
   cp -r paper-to-podium ~/.agents/skills/    # Kimi Code
   ```
2. 使用——自然语言直接提需求即可，比如：
   > "下周课上要汇报这篇论文，30 分钟含提问，帮我准备讲稿和 slides。"

   此类请求（包括"文献汇报 / 课堂展示 / 组会汇报 / 讲稿"等说法）会触发本 skill。它会先问清场合、听众和你的语速，然后走完下面的完整流程。

## 你会得到什么

- **一份按时长预算写出的讲稿**——分钟数 × 语速 = 目标字数（偏慢中文 25 分钟 ≈ 5000 字；会议英语 12 分钟 ≈ 1400 词），每次大改用自带工具重新核算。语言朴实口语化，并针对"AI 味"（反问开场、制造悬念、刻意金句）设有明确护栏，附真实的修改前后对照。
- **为后排观众设计的 slides**——每页一个意思、字号够大，并有"要点页 → 附图页"拆页模式：图独占一页，汇报人照着图旁的小字段落直接念，全程零背诵。
- **事实核查 + 盲评**——每个要说出口的数字回溯到论文原表或具名来源；再派一个零上下文的新 agent 扮演第一次听讲的观众审片。
- **一份打印版上台讲稿**——翻页提示与最终 slides 页码一一对应（`【翻页 → 第 5 页】`）；与 PPT 逐字重复的段落用括号括起、字号小一号（黑白打印清晰可读——那部分你本来就照屏幕念）。

## 工作流程

```
读论文 ──────▶ 检索制度背景（来源留档）
   │                │
   ▼                ▼
写讲稿 ◀── 字数预算 = 分钟 × 语速
   │
   ▼
提炼 slides ──▶ 视觉检查：每页渲染成图，亲眼看，再修
   │
   ▼
事实核查 + 盲评
   │
   ▼
翻页标记 + 打印版讲稿 ──▶ 你，上台
```

每个阶段都有专门的 reference 文件解释原理和失败模式，地图在 SKILL.md 里。已有讲稿就从 slides 阶段进——各阶段按依赖排序，不是形式主义。

## 自带工具

| 工具 | 作用 |
|---|---|
| `scripts/estimate_talk_length.py` | 讲稿字数 → 分钟数（中英文语速档位）。每次大改后跑一遍。 |
| `scripts/script_to_print_pdf.py` | 讲稿 md → 打印版 PDF（XeLaTeX）：翻页提示、小标题、重复段落加括号并小一号。 |
| `scripts/render_pdf_pages.sh` | 把 slides 每页渲染成 PNG，供逐页视觉检查。 |
| `assets/beamer-skeleton.tex` | 16:9 Beamer 骨架，基于 Metropolis 主题（约 7k stars，TeX Live/MiKTeX 自带），内置实测可用的中文配置和两种页面模式。 |

## 目录结构

```
paper-to-podium/
├── SKILL.md                      # 工作流本体；触发时 agent 读它
├── references/
│   ├── script-writing.md         # 时长换算、口语风格、结构、AI 味病例
│   ├── slide-craft.md            # 提炼与压缩之别、排版、附图页、视觉检查
│   └── qa-and-rehearsal.md       # 事实核查、盲评、翻页标记、打印版
├── scripts/                      # 上表三个工具
├── assets/beamer-skeleton.tex
└── evals/evals.json              # 真实感测试用例
```

## 环境要求

- Python 3（仅用标准库）。
- XeLaTeX 及 `ctex`（任一完整版 TeX Live / MiKTeX），用于 slides 和打印版讲稿。
- `pdftoppm`（poppler；MiKTeX 自带），用于页面渲染。

## 来源

提炼自一个真实的完整项目：一场 30 分钟的中文课程论文汇报——讲稿、23 页 Beamer slides、学校模板、事实核查、盲评、打印版标注讲稿——历经约 15 轮用户反馈。references 里保存的是这些反馈教会我们的东西，包括失败的部分（汇报人拒绝念出口的句子、LaTeX 里好看投影上难看的版式）。

## 许可证

MIT，见 [LICENSE](LICENSE)。骨架基于 Metropolis 主题（© Matthias Vogelgesang，LPPL，以系统宏包方式调用）；你从 GitHub 自取的院校模板遵循其各自的许可证。
