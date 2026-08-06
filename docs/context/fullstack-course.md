---
feature: fullstack-course
globs:
  - fullstack.html
  - index.html
updated: 2026-08-06
---

# Full-Stack in 48 — course 04 (the tech-screen refresher)

## Current state — what's working, deployed, broken

- **Shipped to prod 2026-08-06.** `fullstack.html` live at
  https://dsa-in-48.vercel.app/fullstack (Vercel deploy `48c9ec1`, aliased) and on
  GitHub Pages via the `main` push. Nothing known broken.
- Scope: 12 topics (JS core, async, modern JS/TS, React rendering, hooks, React at
  scale · Node internals, Express/API, PostgreSQL core, indexes/N+1, AWS map, AWS ops),
  **153 reveal-answer Q&As** (97 in topics + 56 in the `#qbank` bank), 36 drills
  (18/day), cheat tables (`#cheats`: status codes, hooks, AWS map), playbook, question
  matcher, safe-to-skip.
- Verified: both themes, checkbox + theme persistence (`fs48:*`), clean console, no
  horizontal scroll at 375px, all internal links/anchors across all five pages resolve,
  tag balance clean.

## Recent changes — files touched and why

- `fullstack.html` — **new.** Head/CSS/trailing script cloned from `behavioral.html`
  (sed accent+namespace swap), body written fresh.
- `index.html` — real course-04 card (`.course.fs`), placeholder moved to course 05,
  accent trio + dark overrides, 2 fs xlate items, hero counts (4/50/152/~68h), 2 new
  picker rows, footer link, meta descriptions.
- `dsa.html` / `system-design.html` / `behavioral.html` — series nav +1 link;
  behavioral footer "pairs with" +fullstack; behavioral badge on hub now "live".
- `README.md`, `CLAUDE.md` — course tables, accent list, `fs48:*` namespace, heading
  "Adding a new course".

## Key decisions — choices and trade-offs

- **Accent orange `#FB923C`** (deep `#EA580C` light / `#FDBA74` dark), namespace
  `fs48:*`, favicon "FS".
- **Q&A format reuses the existing `.quiz` `<details>` component** — no new UI; the
  question bank *is* the "training data / night-before refresher" the request asked for.
- **One page-specific CSS divergence** (commented in-file): `.spot li{flex-wrap:wrap}` +
  `.spot .then{white-space:normal}` — this course's "reach for" labels are longer than
  other pages'; nowrap clipped them at card edges (`overflow:hidden`) on both mobile
  and desktop.
- Honesty fixes worth keeping: PG `TRUNCATE` does **not** reset identity by default
  (`RESTART IDENTITY` is opt-in); setTimeout-vs-setImmediate ordering stated as
  nondeterministic outside I/O.
- Browser-pane caveat found while verifying: screenshots only paint near scroll 0 when
  the pane is hidden — verify deep sections via JS DOM checks or
  `document.body.style.transform` translate trick (+ force `.reveal.on`).

## Next steps — specific, actionable

1. Confirm GitHub Pages picked up the push:
   https://rajkaria.github.io/dsa-in-48/fullstack.html (should be live already).
2. Optional: Vercel git auto-deploy is still not connected (dashboard → dsa-in-48 →
   Settings → Git) — until then every push needs `vercel deploy --prod`.
3. Optional content pass: add a TypeScript-utility-types and testing (Jest/RTL) topic
   or bank group if screens demand it; keep the 40-min re-read promise honest.
