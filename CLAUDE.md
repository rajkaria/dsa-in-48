# in-48 — Project Instructions

**Weekend crash syllabi for working full-stack JS engineers.** Each course is one
self-contained HTML page that turns "I've shipped this for years" into "I can name it
under interview pressure."

## Current state

| page | file | live |
|---|---|---|
| Series landing page | [`index.html`](./index.html) | [/](https://dsa-in-48.vercel.app/) · [Pages](https://rajkaria.github.io/dsa-in-48/) |
| DSA in 48 | [`dsa.html`](./dsa.html) | [/dsa](https://dsa-in-48.vercel.app/dsa) · [Pages](https://rajkaria.github.io/dsa-in-48/dsa.html) |
| System Design in 48 | [`system-design.html`](./system-design.html) | [/system-design](https://dsa-in-48.vercel.app/system-design) · [Pages](https://rajkaria.github.io/dsa-in-48/system-design.html) |
| Behavioral in 48 | [`behavioral.html`](./behavioral.html) | [/behavioral](https://dsa-in-48.vercel.app/behavioral) · [Pages](https://rajkaria.github.io/dsa-in-48/behavioral.html) |
| Full-Stack in 48 | [`fullstack.html`](./fullstack.html) | [/fullstack](https://dsa-in-48.vercel.app/fullstack) · [Pages](https://rajkaria.github.io/dsa-in-48/fullstack.html) |
| Frontend System Design in 48 | [`frontend-system-design.html`](./frontend-system-design.html) | [/frontend-system-design](https://dsa-in-48.vercel.app/frontend-system-design) · [Pages](https://rajkaria.github.io/dsa-in-48/frontend-system-design.html) |
| The Learn track (hub + 13 modules) | [`learn/`](./learn/) | [/learn](https://dsa-in-48.vercel.app/learn) · [Pages](https://rajkaria.github.io/dsa-in-48/learn/) |

**The Learn track** (`learn/index.html` + 13 modules, added Aug 2026) is the self-paced
deep-dive companion to the courses: beginner→advanced tutorials with inline-JS interactive
widgets (MCQ quizzes with first-attempt scoring, sandboxed "run it" panels, hand-rolled
visualizers, persisted worksheets). Module scaffolding lives in `.ocean/templates/`
(`learn-head-base.html` + `make_head.py` + `learn-tail.html`) — new modules are built by
instantiating the head (accent/meta/fav placeholders), writing the body, and appending the
tail with the `__SLUG__` swap. localStorage: `learn:<slug>:done` (array of section ids),
`learn:<slug>:quiz` (map qid→0/1), `learn:interview-kit:ws:*` (worksheets), and a single
`learn:theme` shared across the whole track (deliberate exception to per-page themes).
The hub reads every module's progress via those keys; its cards hardcode section totals.

`index.html` used to be the DSA course; it became the landing page in Aug 2026 and the
course moved to `dsa.html`. Old bookmarks to `/` now land on the hub, one click from the
course.

Repo: https://github.com/rajkaria/dsa-in-48 (public, MIT). The GitHub repo and Vercel
project are still named `dsa-in-48` from before the second course — the folder is `in-48`.
Renaming them is optional and would change the Pages URL + the links baked into both
pages' footers and the README.

## Context docs

| doc | covers |
|---|---|
| [`docs/context/fullstack-course.md`](./docs/context/fullstack-course.md) | Full-Stack in 48 (`fullstack.html`) + its landing-page wiring — state, decisions, next steps |

## Hard rules

- **One file per course. No build step, no framework, no npm dependencies.** Everything —
  CSS, JS, SVG icons — is inline. If a change needs a bundler, the change is wrong.
- **Only two external requests:** Google Fonts and the highlight.js CDN (with an
  `integrity` hash). Pages must degrade gracefully to system fonts and unhighlighted code
  when offline. Don't add a third.
- **Keep it honest.** Complexity claims must be correct, LeetCode links must point at
  real live problems, and capacity numbers must survive a back-of-envelope check.
- **Verify LeetCode links against the API**, never HTTP status — problem pages return 403
  to curl regardless of whether they exist:
  `curl -s https://leetcode.com/api/problems/all/` then match
  `stat.frontend_question_id` → `stat.question__title_slug`.

## Shared conventions across courses

- **Design tokens** live in `:root`; every translucent overlay is mixed from a single
  `--tint` RGB triple, so light/dark flips with one variable. Text on the accent marker
  uses `--on-mark` (always dark) and text on `--ink` fills uses `--on-ink`.
- **Accent per course:** DSA = yellow `#FFD60A`, System Design = teal `#2DD4BF`,
  Behavioral = violet `#A78BFA`, Full-Stack = orange `#FB923C`, Frontend System Design =
  rose `#F472B6`. A new course gets a new accent and swaps
  `--mark`/`--mark-deep`/`--mark-soft`.
- **localStorage is namespaced per course** (`dsa48:*`, `sd48:*`, `bh48:*`, `fs48:*`,
  `fesd48:*`, and `in48:theme` for the landing page) so progress and theme never collide. Keys: `<ns>:progress`,
  `<ns>:collapsed`, `<ns>:theme`. An anti-FOUC bootstrap in `<head>` sets `data-theme`
  before first paint. Theme is deliberately *not* shared across pages.
- **The landing page is accent-neutral.** It keeps yellow as the page `--mark` and gives
  each course card its own `--acc`/`--acc-deep`/`--acc-soft` trio (`.course.dsa`,
  `.course.sd`), overridden once for dark. It loads no highlight.js — Google Fonts is its
  only external request.
- **Structure of every topic:** chips (day/time) → "you already know this" analogy mapped
  to the MERN stack → `// the idea` bullets → one code/diagram panel → `// spot it in the
  wild` trigger phrases → drills with persisted checkboxes.
- **Drill checkboxes:** the `<label class="prob-main">` wraps only the input + name; the
  external link sits *outside* it so clicking a link never toggles a box. Each input needs
  a unique `data-key` and a `data-day` of `1` or `2`.
- Every page ends with reference sections: interview playbook, a 10-second pattern/
  component index, cheat tables, and an honest "safe to skip" list. Both days tell the
  reader what to cut if they only have one day.

## Adding a new course

Copy the head + trailing `<script>` from an existing course page (they're identical apart
from the storage namespace and accent), write the body, then update:

1. **`index.html`** — replace the `.course.next` placeholder card with a real `<article
   class="course …">` (course number, badge, tagline, stats, both day chip columns, start
   button + deep links), add a new `.course.<slug>` accent trio in the CSS *and* its dark
   override, add rows to the "which one first?" table, and bump the hero `hero-meta`
   counts (courses / topics / drills / hours).
2. The **"in this series" nav** in *every* other course page (each lists the other courses
   plus "All courses" → `./index.html`).
3. The **README** course table and the **footers**.

## Deploying

```bash
git push origin main          # GitHub Pages updates automatically
vercel deploy --prod          # Vercel does NOT auto-deploy — see below
```

⚠️ **Vercel git auto-deploy is not connected.** `vercel git connect` fails because the
Vercel GitHub app has no access to this repo. Until Raj grants it (Vercel dashboard →
`dsa-in-48` → Settings → Git), every push needs a manual `vercel deploy --prod`.

## Verifying a change

First gate: `bash scripts/verify.sh` — static checks over every page (tag balance, unique
`data-key`s, internal + cross-file anchor resolution, external-request allowlist, hljs
integrity attribute, localStorage namespace hygiene). Green is required before any commit.
Then the browser check:

1. Serve the folder (`python3 -m http.server 8000`) — the pages must be served over HTTP,
   not `file://`, for localStorage to behave.
2. Confirm **both themes** render: hero, topic cards, code panels, drill rows, tables.
3. Toggle a checkbox → reload → state restored. Toggle theme → reload → persists.
4. Check the console is clean and the page doesn't scroll horizontally at 375px.
