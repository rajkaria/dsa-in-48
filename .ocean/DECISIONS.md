# Decision Journal

Every autonomous decision gets an entry. Two-way doors get one line; one-way
doors get the full block.

<!-- Template for one-way doors:
## D<N>: <title>
- **Sprint:** <n>  **Date:** <YYYY-MM-DD>
- **Options:** <a> / <b> / <c>
- **Chose:** <x>
- **Why:** <reasoning — user workflow first, implementation convenience last>
- **Cost to reverse:** <low/medium/high — what it would take>
-->

## D1: Learn track lives at `learn/<slug>.html` with hub `learn/index.html`
- **Sprint:** planning  **Date:** 2026-08-06
- **Options:** (a) flat root files `learn-js.html`… / (b) `learn/` directory
- **Chose:** (b)
- **Why:** 14 new pages would drown the root; `/learn/js-fundamentals` URLs read
  better; GitHub Pages and Vercel both serve directories fine.
- **Cost to reverse:** low today, high after deploy (published URLs) — hence decided now.

## D2: localStorage namespaces — `fesd48:*` (course 05), `learn:<slug>:*` per module, `learn:theme` (hub)
- **Sprint:** planning  **Date:** 2026-08-06
- **Options:** per-page NS (existing rule) / one shared `learn:*` bucket
- **Chose:** per-module `learn:<slug>:*` so progress never collides and the hub can
  read each module's progress by prefix.
- **Why:** matches the existing per-page rule; keys ship in published pages, renames
  orphan user progress. Verify-script NS allowlist updated to match.
- **Cost to reverse:** high after first real use (orphaned progress).

Two-way doors (one-liners):
- **D3:** course 05 accent = rose `#F472B6` (deep `#E11D48`) — distinct from
  yellow/teal/violet/orange in both themes.
- **D4:** course 05 filename `frontend-system-design.html` — self-describing, matches
  `system-design.html` sibling naming.
- **D5:** Learn modules keep the same two allowed external requests as courses
  (Google Fonts + highlight.js w/ integrity) — they are code-heavy tutorials.
- **D6:** interactivity is inline JS only — MCQ quiz engine, Function-sandboxed
  "run it" snippets with console capture, hand-rolled DOM/SVG visualizers. No libs.
- **D7:** recurring mascot "Professor Whiskers" (inline SVG cat) narrates intuition
  callouts; worked examples cat-themed; personal "built for Prachi" note on the Learn
  hub only — course pages stay general.
- **D8:** verify harness lives in-repo (`scripts/check_pages.py` + `verify.sh`,
  stdlib-only). `<a href>` navigation exempt from the external-request allowlist (the
  rule is about resource fetches); localStorage NS check is literal-keys-only.
- **D9:** deploy IS in scope — Raj's request ("make it live on the website") explicitly
  pre-authorizes push-to-main + Vercel prod deploy in SP9; failures logged to REPORT
  with GitHub Pages (auto on push) as fallback.
- **D10:** landing keeps a placeholder "course 06" card after 05 goes real; the Learn
  track gets its own landing section in SP9.
