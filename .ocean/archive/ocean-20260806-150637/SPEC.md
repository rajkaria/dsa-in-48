# SPEC — The in-48 "massive sprint": Frontend System Design course + full Learn track

Verbatim intent from Raj (2026-08-06), for Prachi (resume: React, JavaScript, Node.js,
PostgreSQL, AWS — working full-stack engineer prepping for interviews; she likes cats):

1. **New course:** a Frontend System Design course page, similar in shape to the
   existing four courses (one self-contained HTML page, same conventions).
2. **Massive sprint — in-depth learning modules for ALL topics**: DSA, system design,
   full-stack, frontend, everything. Total depth, beginner → advanced. Interactive
   examples, simple examples, easy-to-learn language. Personalized for Prachi —
   cat-themed examples woven in so it's easier/funner to learn.
3. **Separate modules for each topic** so she can pick up whatever she wants, whenever
   she wants — each module self-contained, independently usable.
4. **Anything else needed for interview prep** in the future — build it proactively.
5. **Make it live on the website** alongside the existing courses (landing page wiring,
   GitHub Pages push + Vercel prod deploy). Explicitly authorized by Raj in the request.

## Constraints (from CLAUDE.md — binding)

- One file per page. No build step, no framework, no npm deps. Everything inline.
- Only two external requests per page: Google Fonts + highlight.js CDN (integrity hash).
  Pages degrade gracefully offline.
- Keep it honest: complexity claims correct, LeetCode links verified via the API,
  capacity numbers survive back-of-envelope.
- Design tokens in `:root`, `--tint` mixing, per-course accent, namespaced localStorage,
  anti-FOUC theme bootstrap, drill-checkbox label pattern, reference sections at the end.

## Deliverables

### A. Course 05 — Frontend System Design in 48 (`frontend-system-design.html`)
Crash-course format like the other four: 2 days, topics with chips → "you already know
this" analogy → idea bullets → code/diagram panel → spot-it-in-the-wild → drills.
Covers: rendering strategies (CSR/SSR/SSG/ISR), component architecture & state,
data fetching/caching, performance & Core Web Vitals, asset delivery/bundling, network
resilience/offline, accessibility & i18n at scale, observability/errors, security
(XSS/CSRF/CSP), infinite scroll/virtualization/real-time UI patterns, design-system
thinking, the interview walkthrough loop (RADIO-style). New accent + `fesd48:*` keys.

### B. The Learn track — deep-dive modules (separate pages under `learn/`)
A hub (`learn/index.html`) + self-contained modules, each beginner → advanced with
interactive inline widgets (quizzes, click-to-run/visualizers built in inline JS),
cat-themed worked examples, plain language. Module list (each its own HTML page):

1. `js-fundamentals` — values, types, coercion, scope, closures, this, prototypes, classes
2. `js-async` — event loop, callbacks, promises, async/await, streams of events
3. `dsa-foundations` — Big-O, arrays, strings, hashmaps, two pointers, sliding window
4. `dsa-structures` — linked lists, stacks, queues, heaps, intervals
5. `dsa-trees-graphs` — trees, BSTs, tries, graphs, BFS/DFS, topo sort
6. `dsa-algorithms` — sorting, binary search, recursion, backtracking, DP, greedy
7. `react-deep-dive` — rendering model, hooks in depth, state patterns, performance, RSC
8. `node-backend` — Node internals, Express/API design, auth, testing, errors
9. `postgres-databases` — SQL from zero, modeling, indexes, transactions, N+1, scaling
10. `aws-cloud` — core services, deployment architectures, ops, cost sense
11. `system-design-backend` — from URL shortener to feeds; building blocks, estimation
12. `frontend-system-design` (deep dive) — the course-05 topics at tutorial depth
13. `interview-kit` — resume walkthrough, mock-loop scripts, question banks, negotiation,
    study planner (the "anything else for future prep" item)

Namespace: `learn:<slug>:*` localStorage keys; shared visual language with the series
but its own progress model (per-section done buttons + quiz scores).

### C. Wiring + deploy
- Landing page: Learn track section + course-05 card, hero counts, picker table rows,
  accent trios (light+dark), footer.
- Series nav on every course page gains course 05; README + CLAUDE.md tables updated.
- Deploy: merge to `main`, push (GitHub Pages), `vercel deploy --prod` (Raj
  pre-authorized making it live in the request).

## Quality bar
Every page passes `scripts/verify.sh` (static checks: tag balance, unique data-keys,
anchor resolution, external-request allowlist, namespace hygiene) plus a browser pass
(both themes, persistence, clean console, no horizontal scroll at 375px).
