# in-48 — Project Instructions

**Weekend crash syllabi for working full-stack JS engineers.** Each course is one
self-contained HTML page that turns "I've shipped this for years" into "I can name it
under interview pressure."

## Current state

| course | file | live |
|---|---|---|
| DSA in 48 | [`index.html`](./index.html) | [/](https://dsa-in-48.vercel.app/) · [Pages](https://rajkaria.github.io/dsa-in-48/) |
| System Design in 48 | [`system-design.html`](./system-design.html) | [/system-design](https://dsa-in-48.vercel.app/system-design) · [Pages](https://rajkaria.github.io/dsa-in-48/system-design.html) |

Repo: https://github.com/rajkaria/dsa-in-48 (public, MIT). The GitHub repo and Vercel
project are still named `dsa-in-48` from before the second course — the folder is `in-48`.
Renaming them is optional and would change the Pages URL + the links baked into both
pages' footers and the README.

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
- **Accent per course:** DSA = yellow `#FFD60A`, System Design = teal `#2DD4BF`. A new
  course gets a new accent and swaps `--mark`/`--mark-deep`/`--mark-soft`.
- **localStorage is namespaced per course** (`dsa48:*`, `sd48:*`) so progress and theme
  never collide. Keys: `<ns>:progress`, `<ns>:collapsed`, `<ns>:theme`. An anti-FOUC
  bootstrap in `<head>` sets `data-theme` before first paint.
- **Structure of every topic:** chips (day/time) → "you already know this" analogy mapped
  to the MERN stack → `// the idea` bullets → one code/diagram panel → `// spot it in the
  wild` trigger phrases → drills with persisted checkboxes.
- **Drill checkboxes:** the `<label class="prob-main">` wraps only the input + name; the
  external link sits *outside* it so clicking a link never toggles a box. Each input needs
  a unique `data-key` and a `data-day` of `1` or `2`.
- Every page ends with reference sections: interview playbook, a 10-second pattern/
  component index, cheat tables, and an honest "safe to skip" list. Both days tell the
  reader what to cut if they only have one day.

## Adding a third course

Copy the head + trailing `<script>` from an existing page (they're identical apart from
the storage namespace and accent), write the body, then update: the "in this series" nav
in *both* existing pages, the README course table, and the footers.

## Deploying

```bash
git push origin main          # GitHub Pages updates automatically
vercel deploy --prod          # Vercel does NOT auto-deploy — see below
```

⚠️ **Vercel git auto-deploy is not connected.** `vercel git connect` fails because the
Vercel GitHub app has no access to this repo. Until Raj grants it (Vercel dashboard →
`dsa-in-48` → Settings → Git), every push needs a manual `vercel deploy --prod`.

## Verifying a change

There is no test suite; the check is visual + behavioural in a browser:

1. Serve the folder (`python3 -m http.server 8000`) — the pages must be served over HTTP,
   not `file://`, for localStorage to behave.
2. Confirm **both themes** render: hero, topic cards, code panels, drill rows, tables.
3. Toggle a checkbox → reload → state restored. Toggle theme → reload → persists.
4. Check the console is clean and the page doesn't scroll horizontally at 375px.
