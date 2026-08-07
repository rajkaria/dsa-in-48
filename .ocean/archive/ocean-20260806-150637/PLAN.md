# PLAN — ocean-20260806-150637

Goal: ship **Frontend System Design in 48** (course 05) plus the **Learn track** — a hub
and 13 self-contained, beginner→advanced, cat-themed deep-dive modules for Prachi — wired
into the landing page and deployed live (GitHub Pages + Vercel prod).

Verify cmd: `bash scripts/verify.sh` (static page checks; browser pass at sweep).

## Shared design decisions (details in DECISIONS.md)

- Course 05: file `frontend-system-design.html`, accent **rose `#F472B6`**, keys `fesd48:*`.
- Learn track: `learn/` directory, hub at `learn/index.html`, modules `learn/<slug>.html`,
  keys `learn:<slug>:*` (+ `learn:theme` on the hub). Same token system/theming as courses;
  each module gets its own small accent from a fixed palette so the hub reads as a shelf.
- Module anatomy (every module): hero with "who this is for" + progress bar → numbered
  sections (beginner → advanced), each with: plain-language explainer, cat-themed worked
  example, one interactive widget (quiz / try-it runner / visualizer), "level up" advanced
  notes, section done-toggle persisted to localStorage → end matter (recap table, how it
  shows up in interviews, links to the matching in-48 course day).
- Interactive widgets are inline JS only: MCQ quiz engine with per-module score
  persistence, "run it" JS snippets (Function-sandboxed console capture) where the
  language is JS, and hand-rolled DOM/SVG visualizers elsewhere.
- The recurring explainer voice is **Professor Whiskers** (inline SVG cat) — callout boxes
  `.whiskers` used for intuition; examples use cats (cat café queues, adoption-center
  hashmaps, litter of kittens trees…). Personal touch on the hub: "built for Prachi".

## Sprints

### SP1 — Verify harness + Frontend System Design in 48 + wiring
- Files: `scripts/check_pages.py`, `scripts/verify.sh` (new), `frontend-system-design.html`
  (new), `index.html`, `dsa.html`, `system-design.html`, `behavioral.html`,
  `fullstack.html`, `README.md`, `CLAUDE.md`.
- Course content (2 days, 12 topics): D1 = the interview loop (RADIO), rendering
  strategies (CSR/SSR/SSG/ISR/streaming), component & state architecture, data fetching
  + caching, performance & Core Web Vitals, asset delivery & bundling. D2 = network
  resilience/offline/real-time, lists at scale (virtualization/infinite scroll),
  accessibility & i18n, security (XSS/CSRF/CSP), observability & errors, design systems
  at scale. Q&A reveals per topic + question bank + cheat tables + playbook + skip list.
- Wiring: course-05 card replaces placeholder (placeholder becomes 06), accent trio +
  dark override, hero counts, picker rows, series nav on all 4 course pages, README +
  CLAUDE.md tables.
- Accept: verify green; course page follows every shared convention; landing counts
  correct; all internal links resolve.

### SP2 — Learn hub + module template + `js-fundamentals`
- Files: `learn/index.html`, `learn/js-fundamentals.html` (both new).
- Hub: shelf of 13 module cards (title, blurb, level range, est. hours, per-module
  progress % read from that module's localStorage), grouped Learn-JS / DSA / Build /
  Systems / Interview; links back to the four courses; "built for Prachi" hero.
  Cards for not-yet-shipped modules render as "coming this weekend" until their file
  exists (hub ships last full link set in SP8 sweep-check).
- `js-fundamentals` (the template-bearer): values & types, coercion, scope & closures,
  `this`, prototypes → classes, modules, iterators; ~7 sections, each with quiz or
  try-it runner; cat examples throughout; recap + interview-mapping end matter.
- Accept: verify green; widgets work without console errors; progress + quiz scores
  persist per namespace; template documented as HTML comments for later modules.

### SP3 — `js-async` + `react-deep-dive`
- Event loop (with an animated task/microtask visualizer), callbacks → promises →
  async/await, error handling, concurrency patterns, timers, AbortController.
- React: mental model (props/state/render), reconciliation, every core hook in depth,
  state architecture, memoization, effects done right, suspense/RSC overview, testing.
- Accept: verify green; both pages complete module anatomy; visualizer animates.

### SP4 — `dsa-foundations` + `dsa-structures`
- Foundations: Big-O from scratch (interactive growth-curve widget), arrays, strings,
  hashmaps/sets, two pointers, sliding window, prefix sums.
- Structures: linked lists, stacks, queues/deques, heaps, intervals; each with a
  step-through visualizer or quiz; LeetCode links verified via the API.
- Accept: verify green; complexity claims correct; LC links checked against API dump.

### SP5 — `dsa-trees-graphs` + `dsa-algorithms`
- Trees/BST/tries, BFS/DFS (grid visualizer), topological sort, union-find.
- Sorting (animated compare), binary search patterns, recursion & backtracking,
  DP from first principles (memo grid widget), greedy.
- Accept: verify green; LC links verified; visualizers step correctly.

### SP6 — `node-backend` + `postgres-databases`
- Node: runtime internals, event loop server-side, streams/buffers, Express patterns,
  REST design, auth (sessions vs JWT), validation, errors, testing, deployment shape.
- Postgres: SQL from zero (interactive query-predictor quizzes), modeling & normal
  forms, joins, indexes & EXPLAIN, transactions & isolation, N+1, migrations, scaling.
- Accept: verify green; SQL examples syntactically valid; claims honest.

### SP7 — `aws-cloud` + `system-design-backend`
- AWS: the mental map (compute/storage/network/db/queue), the 12 services that matter,
  deployment architectures for a MERN app, ops (logs/metrics/alarms), cost sense, IAM.
- System design: the loop (requirements → estimate → design → deep-dive), building
  blocks (LB, cache, queue, CDN, shards, replicas), estimation drills (interactive
  calculator widget), 5 worked designs beginner→advanced (URL shortener → cat-photo
  feed), tradeoff tables.
- Accept: verify green; capacity math survives back-of-envelope check.

### SP8 — `frontend-system-design` (deep dive) + `interview-kit`
- FE deep dive: course-05 topics at tutorial depth with widgets (render-strategy
  decision tree, waterfall visualizer), component API design, state at scale, caching.
- Interview kit: story bank worksheet (persisted textareas), resume walkthrough,
  mock-loop scripts with timers, question banks per round, offer/negotiation basics,
  a 4-week study planner (interactive checklist) pointing at every module + course.
- Accept: verify green; hub cards all live (13/13); planner links all resolve.

### SP9 — Sweep + landing integration + deploy + REPORT
- Landing page gains the Learn track section (shelf teaser + link), hero counts updated;
  courses cross-link to matching learn modules ("go deeper"); README/CLAUDE.md/docs
  context updated; full browser pass (both themes, persistence, console, 375px) on all
  pages; merge worktree branch → main, push (Pages), `vercel deploy --prod`, verify live
  URLs; write `.ocean/REPORT.md`.
- Accept: verify green; live URLs 200 with new content; REPORT complete.

## Dependencies
SP2 depends on SP1 (conventions). SP3–SP8 depend on SP2 (template). SP9 last.
Module pages are independent of each other — safe to reorder SP3–SP8 if needed.
