---
feature: learn-track
globs:
  - learn/**
  - frontend-system-design.html
  - scripts/**
  - .ocean/templates/**
updated: 2026-08-07
---

# The Learn track + Frontend System Design in 48 — the Aug 2026 expansion

## Current state — what's working, deployed, broken

- **2026-08-08 — Reasoning Gym layer — DEPLOYED TO PROD** (branch
  `claude/course-practice-questions-quizzes-493f8a` → merged to main `f96bc01`; Vercel
  `dpl_8o4aErdRhozJs8h47wtFNEN5vZoW` aliased to dsa-in-48.vercel.app, GitHub Pages
  workflow green — gym markers verified live on both hosts, hub totals confirmed via
  curl): every Learn module gained a final `#gym` lesson — 9 scored MCQs in
  three tiers (warm-up / apply / stretch: inference-only questions, FALSE-claim hunts,
  estimation, cross-section chains; qids `<prefix>-gym-1..9` on the existing
  `learn:<slug>:quiz` key) — and every course page gained a 12-question `#gym` section
  before its playbook (`.mcq` engine ported from `learn-tail.html`, first attempt persisted
  to `<ns>:gym`, score in `#gym-score`, "// practice" side-group). New Learn totals:
  **237 sections / ~153h / 369 quizzes** (hub cards, hub hero, landing counts all
  recounted; landing hero now shows 60 course-gym questions and ~87h). Docs (CLAUDE.md,
  README, this file) updated. verify.sh green across all 23 pages.
- **DEPLOYED TO PROD 2026-08-08** (depth-expansion run `ocean-20260807-130307`, 10/10
  sprints; report in `.ocean/REPORT.md`, previous run archived under `.ocean/archive/`).
  Vercel: merged to main (`dddfa54`), deployed `dpl_FaYkGBCgziZhLCGKC3CM75m61WF7`,
  aliased to dsa-in-48.vercel.app — landing, hub, and all 16 modules verified live with
  correct titles. GitHub Pages: Actions workflow deploy green (~20s), hub + modules
  verified live. Browser sweep: 23 pages, zero console errors, zero horizontal overflow
  at 375px, widget/persistence checks green in both themes.

## Current state — what's shipped

- **Course 05 — Frontend System Design in 48** (`frontend-system-design.html`): 12 topics
  (RADIO loop, rendering, components, state, data, CWV / assets, real-time, lists, a11y,
  security, observability), **141 reveal Q&As** (93 in topics + 48 bank), 36 drills
  (18/18), walkthrough script, question matcher, cheat tables, skip list. Rose accent
  `#F472B6`, keys `fesd48:*`.
- **The Learn track** (`learn/`): hub + 16 self-paced modules, all live. Every module is
  now expanded to 14–16 sections with band dividers (`// beginner` / `// intermediate` /
  `// advanced`) plus a closing reasoning gym. Totals: **237 sections / ~153h / 369
  quizzes**. Built for Prachi
  (cat-themed examples, Professor Whiskers callouts) but general-audience safe. Shelves:
  - *Learn JavaScript*: `js-fundamentals` (amber), `js-async` (sky — event-loop stepper),
    `typescript` (purple `#C084FC` — predict-the-compiler-error gauntlet) **(new)**
  - *Learn DSA*: `dsa-foundations` (yellow — growth explorer, 41 verified LC links),
    `dsa-structures` (lime — pointer-surgery stepper, MinHeap, 34 LC), `dsa-trees-graphs`
    (emerald — BFS grid flood, trie, Kahn's, union-find, 29 LC), `dsa-algorithms` (cyan —
    sorting race, answer-space binary search, DP call-counter, 37 LC)
  - *Build the stack*: `react-deep-dive` (blue — cascade sim, hook slots), `node-backend`
    (green — 20-line Express, tamperable HMAC-JWT), `postgres-databases` (indigo — in-page
    SQL + join engines, lost-update race, N+1 demo), `aws-cloud` (orange — staged
    architectures), `testing` (red `#F87171` — 20-line test framework on the page) **(new)**
  - *Think in systems*: `system-design-backend` (teal — envelope calculator, 8 worked
    designs), `frontend-system-design` (rose — rendering decision tree, annotated RADIO),
    `web-platform` (slate `#94A3B8` — freshness-decider runner) **(new)**
  - *Ace the interview*: `interview-kit` (violet — 18 persisted worksheets, 4-week planner)
- **Wiring**: landing page has the course-05 card + a Learn-track section/topbar/footer/
  picker rows; all five course pages cross-link the track (series nav + footer); README +
  CLAUDE.md updated.
- **Verify harness**: `scripts/verify.sh` → `scripts/check_pages.py` (stdlib Python) —
  tag balance, unique data-keys, anchor resolution incl. cross-file, external-request
  allowlist (fonts + hljs only, `<a href>` navigation exempt), hljs integrity, namespace
  hygiene, and (new) `data-qid` uniqueness. All 23 pages green.

### Aug 2026 depth expansion (ocean-20260807-130307)

- Expansion was **in-place**: existing section ids and quiz qids were never renamed, so
  reader progress in localStorage is preserved. New sections were appended or interleaved
  around the originals.
- Three new modules added (`typescript`, `testing`, `web-platform`); every existing
  module deepened to 13–15 sections with beginner/intermediate/advanced band dividers.
- Hub cards recounted (sections, quizzes, runners, durations, `data-total`/pcount).
- Deploy state will be updated after sprint 10 — the live hosts still serve the
  pre-expansion track until then.

## Conventions the modules follow (beyond CLAUDE.md)

- Templates in `.ocean/templates/`: `make_head.py <slug> <title> <desc> <FAV> <acc>
  <acc_deep> <acc_darkdeep> <acc_rgb>` (FAV = plain ASCII initials — it lands inside a
  URL-encoded SVG). Tail: `learn-tail.html` with `__SLUG__` swap.
- Module anatomy: hero (crumb → level chips → honest hero-meta counts) → `.lesson`
  sections (explainer → Whiskers callout → runner/viz/quiz → levelup → done-row) →
  recap table → "in the interview" cross-links → footer.
- Widgets: `.mcq` (first attempt recorded), `.runner` (Function-sandboxed, console
  captured, async wrapper), page-specific `.viz` scripts inline before the tail,
  `.ws` textareas (interview-kit only) saving to `learn:interview-kit:ws:<key>`.
- Hero-meta numbers must match reality (quiz counts, runner counts) — the verify script
  doesn't check these; count by hand when editing.
- **Gym anatomy (every module):** `<section class="lesson" id="gym">` as the last lesson —
  intro para → 9 `.mcq`s tagged `// warm-up|apply|stretch N of 3 — <skill>` → a
  "LEVEL UP — how to read your score" remediation list → done-row. Questions must force an
  inference (no recall); each tier-3 set includes a FALSE-claim hunt and an
  estimation/trade-off; `.mcq-why` names the misconception behind each distractor. The
  build spec used to generate them is `.ocean/templates/`-adjacent knowledge only — the
  authoritative description is this bullet + CLAUDE.md.
- LeetCode links verified against the API dump (all 62 across the DSA modules checked,
  incl. `paid_only` false).

## Known quirks / gotchas hit during the build

- The Claude-browser preview pane throttles timers to 1/s and returns zero-size geometry
  when hidden — timer-based demos "hang" and layout checks lie. Verify runners by
  stubbing timers; do visual passes with the pane actually visible.
- Inline `<script>` blocks must NOT HTML-escape `<`/`>` (entities aren't decoded in
  script contexts) — code panels (`<pre><code>`) MUST escape them. The favicon text sits
  URL-encoded inside the data-URI (`%3EXX%3C`).
- The runner note "— async work finished —" only prints when the wrapper resolves >150ms
  after click.

## Next steps — specific, actionable

- **GitHub Pages: RESOLVED 2026-08-07.** The legacy Jekyll builder kept failing even
  with `.nojekyll`, so Pages now deploys via `.github/workflows/pages.yml`
  (`build_type: workflow`, actions/deploy-pages) — 20s deploys, real logs under the
  Actions tab. All 20 pages verified 200 and byte-identical to the repo on BOTH hosts;
  full live link-crawl clean (LeetCode 403s are bot-blocking, not breakage — links are
  API-verified per CLAUDE.md).
- Optional polish, none blocking: per-module og-images; an aggregate progress bar on the
  hub; a `.soon` placeholder card pattern for any future module 14; hero-meta count
  checks added to `scripts/check_pages.py`.
- Vercel git auto-deploy is STILL not connected (pushes need manual
  `vercel deploy --prod` from the repo root) — granting the Vercel GitHub app access
  remains Raj's call. GitHub Pages, by contrast, now auto-deploys on every push to main.
