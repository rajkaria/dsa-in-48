# Learn track depth expansion — 13 modules → truly in-depth, +3 new modules

Approved by Raj in-session 2026-08-07 (AskUserQuestion: "Full rebuild — all 13" +
new modules TypeScript, Testing, Web Platform & HTTP; then "Approve — run it", which
explicitly pre-authorizes the prod deploy at the end).

## Why

The hub's "in-depth" modules advertise ~3–4.5h each (6–7 sections). Raj's verdict:
in-depth must mean genuinely beginner→advanced, "every little thing". Target: every
module 12–15 sections (~8–10h), plus three new modules, honest re-counted labels
everywhere. Track grows ~80 → ~221 sections, ~50h → ~145h.

## Approach (decided, do not relitigate)

- **Expand in place.** Existing section ids and quiz qids are NEVER renamed or removed —
  reader progress in `learn:<slug>:done` / `learn:<slug>:quiz` must survive. New sections
  get NEW ids (listed below). Interleaving new sections between existing ones is allowed
  and encouraged where pedagogy demands (e.g. `scope` before `closures`).
- **Ladder bands.** Each module's sections are grouped under three visible band dividers
  in the house comment style: `// beginner`, `// intermediate`, `// advanced` — a small
  `.band` element (eyebrow-styled, non-interactive, not a section, no done-row). Add the
  band CSS once per module head (or inline `<style>` addition consistent across modules).
  Hero level chips stay; hero-meta re-counted.
- **Section anatomy unchanged** (context doc `docs/context/learn-track.md`): explainer →
  Whiskers callout → widget (quiz always; runner/viz where runnable) → level-up →
  done-row. Cat-themed examples, general-audience safe.
- **Every new section has a quiz** (`.mcq`, first-attempt scoring, unique qid following
  the module's existing qid pattern). Runnable topics get `.runner` panels. Each expanded
  module gains ≥1 new hand-rolled visualizer where the table below names one.
- **Hard rules stand**: one self-contained file per module, no build step, only the two
  external requests (fonts + hljs), inline `<script>` never HTML-escapes `<`/`>`, code
  panels always escape, verify.sh green before every commit.
- **Durations**: label = sections × ~40 min, rounded to nearest 0.5h (12 → ~8h,
  13 → ~8.5h, 14 → ~9.5h, 15 → ~10h). Hub cards, module heroes, hub hero, landing page,
  README all re-counted BY HAND (verify.sh does not check counts).

## Per-module expansion maps

Existing ids listed for orientation; NEW ids are binding (content/titles are the
worker's call, coverage listed is the minimum).

### Learn JavaScript shelf

**js-fundamentals** (15 total; existing: values coercion closures this prototypes modules iteration)
NEW: `scope` (scope chains, hoisting, TDZ, var/let/const — place before closures) ·
`errors` (throw/try/catch, custom Error subclasses, cause, stack hygiene) ·
`classes` (class semantics on top of prototypes, private fields, static, accessors) ·
`generators` (generators + iterator protocol deep, delegation, lazy pipelines) ·
`symbols` (symbols, well-known symbols, Symbol.iterator/asyncIterator/toPrimitive) ·
`regex` (literals, flags, groups, lookarounds, replace callbacks, common interview regexes) ·
`memory` (GC mental model, reference vs value, leaks: closures/timers/detached DOM, WeakMap/WeakRef) ·
`copying` (shallow vs deep, spread traps, structuredClone, immutability patterns).

**js-async** (14 total; existing: why loop promises await ordering parallel cancel)
NEW: `combinators` (all/allSettled/any/race patterns + failure semantics) ·
`rejections` (error propagation in chains vs await, unhandledrejection, retry patterns) ·
`iterasync` (async iterators, for await…of, async generators) ·
`streams` (Web Streams: readable/writable/transform, backpressure intuition) ·
`workers` (Web Workers, structured clone, message passing, when threads help) ·
`scheduling` (queueMicrotask, rAF, setTimeout clamping, Node phases vs browser) ·
`patterns` (concurrency pools, debounce/throttle, once, queue serialization).
New viz: extend the event-loop stepper or add a scheduling-timeline stepper.

**typescript** — NEW MODULE, 13 sections. Slug `typescript`, shelf `#js`.
Head: `python3 .ocean/templates/make_head.py typescript "TypeScript, from Zero" "<desc>" "TS" "#C084FC" "#9333EA" "#A855F7" "192,132,252"` + tail `__SLUG__`→`typescript`.
Sections: `mental` (structural typing, types vs values, erasure) · `basics` (primitives,
arrays, tuples, objects, readonly) · `narrowing` (unions, literal types, typeof/in/
instanceof guards, discriminated unions, never) · `functions` (signatures, optional/
default/rest, overloads, void vs undefined) · `generics` (functions, constraints,
defaults, inference) · `utility` (Partial/Pick/Omit/Record/ReturnType, mapped +
conditional types, keyof, infer) · `classes` (interfaces vs types, implements,
abstract, declaration merging) · `declarations` (modules, ambient types, .d.ts,
@types) · `tsconfig` (strict family, noUncheckedIndexedAccess, module/target) ·
`react` (typing props/children/hooks/events/refs) · `node` (typing Express handlers,
env, zod-at-the-boundary pattern) · `migration` (any vs unknown, assertions, escape
hatches, JS→TS strategy) · `practice` (predict-the-compiler-error gauntlet).
No tsc in-browser — widgets are predict-the-error/predict-the-type MCQs; runners only
for plain-JS-behavior demos. hljs already highlights `typescript`.

### Learn DSA shelf — every new LeetCode link verified against the API dump
(`curl -s https://leetcode.com/api/problems/all/`, match frontend_question_id →
question__title_slug, reject paid_only) — never HTTP status.

**dsa-foundations** (14; existing: bigo arrays hashmaps twopointers window prefix practice)
NEW: `bits` (operators, masks, XOR tricks, counting bits) · `math` (gcd, primes/sieve,
modular arithmetic, overflow) · `prefix2d` (difference arrays, 2D prefix sums) ·
`hashing` (hash function intuition, collisions, rolling-hash preview, when O(1) lies) ·
`windowplus` (variable windows with counts/maps, at-most-K trick, min-window) ·
`matrix` (traversals, spirals, rotation, in-place tricks) · `recursion` (recurrence →
complexity, master-theorem intuition, recursion→iteration).

**dsa-structures** (13; existing: lists stacks queues heaps intervals practice)
NEW: `monotonic` (monotonic stack/queue, next-greater, sliding-window max) ·
`lrucache` (LRU design map+DLL, LFU sketch) · `twoheaps` (median, scheduling patterns) ·
`rollinghash` (Rabin-Karp, substring equality) · `listsplus` (copy-random-pointer,
cycle proof, in-place reversal families) · `balance` (BST balance intuition, treaps/
AVL/red-black at concept level, when interviews expect them) · `deque` (deque patterns).

**dsa-trees-graphs** (13; existing: trees bst tries graphs topo unionfind)
NEW: `lca` (LCA patterns, path-through-node problems) · `rangetrees` (Fenwick + segment
tree intuition, when to name them) · `shortestpaths` (Dijkstra, Bellman-Ford, when BFS
suffices) · `mst` (Kruskal/Prim + union-find reuse) · `bfsplus` (multi-source, 0-1 BFS,
bidirectional intuition) · `topodp` (DP on DAGs, longest path, course-schedule variants) ·
`gridtricks` (islands family, boundary flood, state-in-cell encodings).
New viz: Dijkstra frontier stepper on the existing grid, or reuse BFS flood w/ weights.

**dsa-algorithms** (13; existing: sorting binsearch recursion dp greedy choosing)
NEW: `exchange` (greedy exchange arguments — proving/breaking greedy) · `intervals`
(merge/insert/meeting-rooms family as one pattern) · `backtracking` (permutations/
subsets/combination-sum, pruning, complexity honesty) · `dpfamilies` (knapsack 0/1 +
unbounded, LIS n log n, edit distance, grid DP, bitmask DP, tree DP — one worked
example each) · `bsanswer` (binary search on answer space, Koko/ship-capacity family) ·
`quickselect` (partition, kth element, average vs worst case) · `strings` (KMP failure
function intuition, Z-idea, when to say "rolling hash").

### Build the stack shelf

**react-deep-dive** (15; existing: model rendering state effects hooks performance modern)
NEW: `keys` (reconciliation deep, key pitfalls, identity vs index) · `context`
(propagation model, splitting contexts, perf traps) · `refs` (refs/forwardRef/
imperative escape hatches, measuring DOM) · `forms` (controlled vs uncontrolled, form
actions, validation patterns) · `boundaries` (error boundaries, Suspense mental model) ·
`concurrent` (transitions, useDeferredValue, tearing, why concurrent exists) · `rsc`
(server components, hydration, islands, "use client" boundaries) · `statemgmt` (lifting
vs colocation, reducers, external stores + useSyncExternalStore, custom-hook design).

**node-backend** (15; existing: runtime streams express rest auth robust ship)
NEW: `phases` (libuv, event-loop phases, micro vs macro in Node, blocking the loop) ·
`backpressure` (highWaterMark, pipe/pipeline, async iteration of streams) · `buffers`
(Buffer, encodings, binary safety) · `clustering` (cluster vs worker_threads vs PM2,
when each) · `authplus` (session vs JWT tradeoffs deep, refresh rotation, OAuth 2 /
OIDC flows walked) · `websockets` (ws lifecycle, heartbeats, scaling fan-out) ·
`security` (helmet-style headers, rate limiting, input validation, OWASP top hits in
Express terms) · `observability` (structured logs, metrics, traces, health checks).

**postgres-databases** (15; existing: sql modeling joins indexes transactions nplus1 scale)
NEW: `isolation` (all four levels, every anomaly named + demoed like the lost-update
race) · `mvcc` (row versions, vacuum, bloat, why long transactions hurt) · `explain`
(reading plans: seq/index/bitmap scans, join strategies, when the planner ignores your
index) · `indexplus` (GIN/GiST/BRIN, partial, covering, expression indexes) · `windows`
(window functions family, frames, top-N-per-group) · `ctes` (CTEs, recursive queries,
materialization) · `jsonb` (operators, GIN on jsonb, when to normalize instead) ·
`migrations` (zero-downtime patterns, lock traps, connection pooling, backfill strategy).
New viz/runner: extend the in-page SQL engine where feasible; plan-reading can be
static annotated panels.

**aws-cloud** (14; existing: map services architectures iam ops cost)
NEW: `iamplus` (policy evaluation, roles vs users, STS/assume-role, least privilege) ·
`vpc` (subnets, route tables, SG vs NACL, NAT, private egress) · `compute` (EC2 vs
ECS vs EKS vs Lambda vs App Runner decision tree) · `s3` (consistency, storage
classes, presigned URLs, static hosting, encryption) · `datastores` (RDS/Aurora vs
DynamoDB, single-table intro, ElastiCache) · `messaging` (SQS vs SNS vs EventBridge,
DLQs, fan-out, idempotent consumers) · `edge` (CloudFront, cache keys, invalidation,
signed URLs) · `iac` (why IaC, CDK/Terraform concept level, drift).

**testing** — NEW MODULE, 13 sections. Slug `testing`, shelf `#build`.
Head: `make_head.py testing "Testing JavaScript, Properly" "<desc>" "TQ" "#F87171" "#DC2626" "#EF4444" "248,113,113"` + tail swap.
Sections: `why` (pyramid vs trophy, what tests buy, what to test) · `anatomy` (AAA,
describe/it, matchers — ship a tiny hand-rolled `expect` so runners execute real
assertions in-page) · `jest` (config, setup, snapshots honestly appraised) · `mocking`
(module mocks, spies, fake timers, DI vs mocking) · `async` (testing promises, fake
timers + async, flushing microtasks) · `rtl` (React Testing Library queries, roles,
user-event, what not to assert) · `hooks` (testing hooks/context/providers,
renderHook) · `api` (supertest-style integration, test servers) · `db` (test doubles
vs test DBs, transactions-as-fixtures, seeding) · `e2e` (Playwright model: locators,
auto-wait, trace; when e2e earns its cost) · `coverage` (line vs branch, what 100%
misses, mutation intuition) · `tdd` (red-green-refactor walked on a real kata) ·
`ci` (flakes: causes + quarantine, parallelism, CI pipeline shape).
Runners: hand-rolled `expect` + fake-timer demos run in-page. Jest/RTL/Playwright
API panels are static code panels (be honest that they need a terminal).

### Think in systems shelf

**system-design-backend** (14; existing: loop estimate traffic caching datascale queues worked)
NEW: `consistency` (linearizable vs eventual, read-your-writes, CAP → PACELC in plain
words) · `consensus` (quorums, leader election, why odd numbers, split brain) ·
`ratelimiter` (token bucket vs sliding window, distributed limiter design) ·
`idempotency` (idempotency keys, dedupe, exactly-once revisited end-to-end) ·
`search` (inverted index, relevance basics, search-vs-DB boundary) · `multiregion`
(active-passive vs active-active, data residency, failover drills) · `workedplus`
(three MORE worked designs end-to-end: chat/WhatsApp, proximity/Yelp, ticketing/
Ticketmaster — same envelope→verdict format as existing five).

**frontend-system-design** (14; existing: radio rendering components state data perf resilience)
NEW: `offline` (service workers, cache strategies, PWA, background sync) · `caching`
(the full layer cake: HTTP cache → SW → memory → state, invalidation story) ·
`designsystem` (tokens, theming, component API design at scale, versioning) · `i18n`
(locales, pluralization, RTL, lazy locale loading) · `flags` (feature flags,
experiments, kill switches, progressive rollout) · `rum` (RUM vs synthetic, CWV
budgets in CI, error tracking) · `collab` (presence, OT vs CRDT intuition, cursors —
when to buy not build).

**web-platform** — NEW MODULE, 13 sections. Slug `web-platform`, shelf `#systems`.
Head: `make_head.py web-platform "How the Web Actually Works" "<desc>" "WP" "#94A3B8" "#475569" "#64748B" "148,163,184"` + tail swap.
Sections: `browser` (parse→style→layout→paint→composite, what triggers each) · `http`
(HTTP/1.1 → 2 → 3: head-of-line, multiplexing, QUIC — in plain words) · `tls`
(handshake intuition, certs, why HTTPS everywhere) · `dns` (resolution path, records,
TTLs, DNS as deploy lever) · `caching` (Cache-Control grammar, ETag/304, immutable +
hashed assets pattern, CDN interplay) · `storage` (cookie attributes deep, local/
session/IndexedDB, quotas) · `cors` (same-origin, preflight, credentials — the whole
dance, debugging playbook) · `security` (XSS types + CSP, CSRF + SameSite,
clickjacking, sanitization) · `auth` (sessions vs tokens on the web, OAuth 2 + OIDC
flows drawn out, PKCE) · `realtime` (polling vs SSE vs WebSockets, reconnect/backoff
design) · `urls` (URL anatomy, encoding pitfalls, query vs path vs fragment) ·
`forms` (native form behavior, multipart, file upload paths) · `practice` (cross-page
quiz gauntlet).
Viz: a request-lifecycle stepper (DNS→TCP→TLS→HTTP→render) — hand-rolled, no network.

### Ace the interview shelf

**interview-kit** (13; existing: stories pitch mockloop questions offer planner rituals)
NEW: `starbank` (STAR story-bank builder — persisted `.ws` worksheet grid) · `sdrubric`
(what system-design interviewers actually grade, self-score sheet) · `takehome`
(strategy, scoping, README-first, common sinks) · `negotiation` (levels, comp
components, scripts, counter etiquette) · `offersheet` (offer-evaluation worksheet —
persisted) · `mockscripts` (three self-run mock scripts with timers and rubrics).
Worksheets keep the `learn:interview-kit:ws:*` namespace.

## Wiring (dedicated sprint, after all modules)

1. `learn/index.html` hub: 3 new cards (typescript → js shelf, testing → build shelf,
   web-platform → systems shelf) following existing card markup; ALL 16 cards get
   re-counted section totals + durations; hub hero re-counted (16 modules, ~145h, real
   totals); progress JS reads the new slugs automatically via card data — verify.
2. Root `index.html`: Learn-track section copy ("thirteen" → sixteen, ~50h → real
   total, shelf lists + deep links), "which one first?" Learn row if counts named.
3. Every module's footer/cross-links that name module counts; `learn-tail.html`
   template if it hardcodes anything track-wide.
4. `README.md`, `CLAUDE.md` (Learn-track paragraph: 13 → 16, key list), and
   `docs/context/learn-track.md` (rewrite state sections to post-expansion reality).
5. Meta descriptions of the three new modules; og where the pattern exists.

## Verification gates (every sprint)

- `bash scripts/verify.sh` green before every commit (tag balance, unique data-keys,
  anchors incl. cross-file, external allowlist, hljs integrity, namespace hygiene).
- New LeetCode links API-verified within the sprint that adds them.
- Hero-meta counts hand-recounted for every touched module.
- Final sprint: serve over HTTP, both themes, checkbox+quiz+theme persistence reload
  test, console clean, no horizontal scroll at 375px, spot-check each new visualizer
  and 2–3 runners per new module in the real browser pane (remember: preview pane
  throttles timers when hidden — keep it visible for timer demos).

## Deploy (final sprint, pre-authorized)

`git push origin main` (Pages auto-deploys via Actions) + `vercel deploy --prod` from
the repo root (Vercel git auto-deploy is NOT connected). Verify live URLs 200 on both
hosts + spot-crawl new pages. Worktree: merge to main first per repo flow.

## Non-goals

- No renaming of existing section ids/qids, no localStorage migrations.
- No fourth external request, no build step, no frameworks.
- No og-image generation beyond existing patterns; no module 17+.
