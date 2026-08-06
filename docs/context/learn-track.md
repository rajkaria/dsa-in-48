---
feature: learn-track
globs:
  - learn/**
  - frontend-system-design.html
  - scripts/**
  - .ocean/templates/**
updated: 2026-08-06
---

# The Learn track + Frontend System Design in 48 — the Aug 2026 expansion

## Current state — what's working, deployed, broken

- **DEPLOYED TO PROD 2026-08-06.** Vercel: merged to main (`0c4f4a7`), deployed
  (`dpl_EcXu1ky6Zo6TALRyqkxWpKVivVBf`, aliased to dsa-in-48.vercel.app) — all URLs
  verified 200 with correct titles. GitHub Pages: first build **errored** (Jekyll choked
  on JSX `{{ }}` inside code panels) — fixed with a root `.nojekyll` (`c4c9afb`);
  rebuild was in flight at save time. Ocean run `ocean-20260806-150637` complete
  (9/9 sprints); full report in `.ocean/REPORT.md`.

## Current state — what's shipped

- **Course 05 — Frontend System Design in 48** (`frontend-system-design.html`): 12 topics
  (RADIO loop, rendering, components, state, data, CWV / assets, real-time, lists, a11y,
  security, observability), **141 reveal Q&As** (93 in topics + 48 bank), 36 drills
  (18/18), walkthrough script, question matcher, cheat tables, skip list. Rose accent
  `#F472B6`, keys `fesd48:*`.
- **The Learn track** (`learn/`): hub + 13 self-paced modules, all live. Built for Prachi
  (cat-themed examples, Professor Whiskers callouts) but general-audience safe. Shelves:
  - *Learn JavaScript*: `js-fundamentals` (amber), `js-async` (sky — event-loop stepper)
  - *Learn DSA*: `dsa-foundations` (yellow — growth explorer, 18 verified LC links),
    `dsa-structures` (lime — pointer-surgery stepper, MinHeap, 14 LC), `dsa-trees-graphs`
    (emerald — BFS grid flood, trie, Kahn's, union-find, 14 LC), `dsa-algorithms` (cyan —
    sorting race, answer-space binary search, DP call-counter, 16 LC)
  - *Build the stack*: `react-deep-dive` (blue — cascade sim, hook slots), `node-backend`
    (green — 20-line Express, tamperable HMAC-JWT), `postgres-databases` (indigo — in-page
    SQL + join engines, lost-update race, N+1 demo), `aws-cloud` (orange — staged
    architectures)
  - *Think in systems*: `system-design-backend` (teal — envelope calculator, 5 worked
    designs), `frontend-system-design` (rose — rendering decision tree, annotated RADIO)
  - *Ace the interview*: `interview-kit` (violet — 12 persisted worksheets, 4-week planner)
- **Wiring**: landing page has the course-05 card + a Learn-track section/topbar/footer/
  picker rows; all five course pages cross-link the track (series nav + footer); README +
  CLAUDE.md updated.
- **Verify harness**: `scripts/verify.sh` → `scripts/check_pages.py` (stdlib Python) —
  tag balance, unique data-keys, anchor resolution incl. cross-file, external-request
  allowlist (fonts + hljs only, `<a href>` navigation exempt), hljs integrity, namespace
  hygiene. All 20 pages green.

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

- **Confirm GitHub Pages went green** after the `.nojekyll` fix:
  `curl -s -o /dev/null -w '%{http_code}' https://rajkaria.github.io/dsa-in-48/learn/`
  (expect 200; if errored again: `gh api repos/rajkaria/dsa-in-48/pages/builds/latest`).
- Optional polish, none blocking: per-module og-images; an aggregate progress bar on the
  hub; a `.soon` placeholder card pattern for any future module 14; hero-meta count
  checks added to `scripts/check_pages.py`.
- Vercel git auto-deploy is STILL not connected (pushes need manual
  `vercel deploy --prod` from the repo root) — granting the Vercel GitHub app access
  remains Raj's call.
