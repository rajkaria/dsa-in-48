# Plan — Learn track depth expansion (ocean-20260807-130307)

Spec: `.ocean/SPEC.md` (binding — per-module NEW section ids, new-module head args,
wiring list, verification gates all live there). Verify cmd: `bash scripts/verify.sh`.

Working style, every module sprint:
1. Write new sections in scratchpad files, then splice into the module (interleaving
   into beginner/intermediate/advanced band order per spec).
2. Add the three `.band` dividers, new quizzes (unique qids in the module's pattern),
   runners/viz per spec, update the module's own hero-meta + duration by hand.
3. DSA sprints: verify every new LeetCode link against the API dump in-sprint.
4. `bash scripts/verify.sh` green → single commit `ocean(spN): <title>` → sprint-done
   → checkpoint.

Counts ledger (target sections): js-fund 15 · js-async 14 · typescript 13 ·
dsa-found 14 · dsa-struct 13 · dsa-tg 13 · dsa-algo 13 · react 15 · node 15 ·
postgres 15 · aws 14 · testing 13 · sd-backend 14 · fesd 14 · web-platform 13 ·
interview-kit 13 → 221 sections, ~145h. Wiring sprint recounts from the actual files,
not this ledger.

## Sprints

### Sprint 1 — js-fundamentals + js-async expansions
Files: `learn/js-fundamentals.html`, `learn/js-async.html`.
Adds: jsf +8 (scope errors classes generators symbols regex memory copying),
asy +7 (combinators rejections iterasync streams workers scheduling patterns) + a
scheduling-timeline stepper or event-loop-stepper extension.
Accept: both modules 15/14 sections, bands visible, every new section has quiz,
runners for runnable topics, hero-meta recounted, verify green.

### Sprint 2 — dsa-foundations + dsa-structures expansions
Adds: dsf +7 (bits math prefix2d hashing windowplus matrix recursion),
dss +7 (monotonic lrucache twoheaps rollinghash listsplus balance deque).
Accept: 14/13 sections, new LC links API-verified, bands, quizzes, verify green.

### Sprint 3 — dsa-trees-graphs + dsa-algorithms expansions
Adds: dtg +7 (lca rangetrees shortestpaths mst bfsplus topodp gridtricks) + Dijkstra
frontier viz; dal +7 (exchange intervals backtracking dpfamilies bsanswer quickselect
strings).
Accept: 13/13 sections, LC links API-verified, verify green.

### Sprint 4 — react-deep-dive + node-backend expansions
Adds: react +8 (keys context refs forms boundaries concurrent rsc statemgmt),
node +8 (phases backpressure buffers clustering authplus websockets security
observability).
Accept: 15/15 sections, verify green.

### Sprint 5 — postgres-databases + aws-cloud expansions
Adds: pg +8 (isolation mvcc explain indexplus windows ctes jsonb migrations) with
SQL-engine extensions where feasible; aws +8 (iamplus vpc compute s3 datastores
messaging edge iac).
Accept: 15/14 sections, verify green.

### Sprint 6 — system-design-backend + frontend-system-design expansions
Adds: sdb +7 (consistency consensus ratelimiter idempotency search multiregion
workedplus w/ 3 new worked designs); fesd +7 (offline caching designsystem i18n
flags rum collab).
Accept: 14/14 sections, verify green.

### Sprint 7 — interview-kit expansion + NEW typescript module
Adds: kit +6 (starbank sdrubric takehome negotiation offersheet mockscripts — two new
persisted worksheets in `learn:interview-kit:ws:*`); build `learn/typescript.html`
(13 sections per spec, head via make_head.py args in spec, predict-the-error MCQs).
Accept: kit 13 sections; typescript module complete standalone (hub card comes in
sprint 9); verify green.

### Sprint 8 — NEW testing + NEW web-platform modules
Build `learn/testing.html` (13 sections, hand-rolled in-page `expect` runners) and
`learn/web-platform.html` (13 sections, request-lifecycle stepper viz).
Accept: both modules complete standalone, verify green.

### Sprint 9 — hub + landing + docs wiring, full recount
Per spec Wiring list: 3 new hub cards, all 16 cards recounted (sections + durations
from the actual files), hub hero totals, root index.html Learn section, README,
CLAUDE.md, docs/context/learn-track.md rewrite.
Accept: no stale count anywhere (grep for "13 modules", "~50h", old per-card counts),
verify green (incl. cross-file anchors to new modules).

### Sprint 10 — full sweep, browser pass, REPORT, deploy
verify.sh, HTTP-served browser pass per spec gates (both themes, persistence reloads,
375px, console, new widgets exercised), re-read SPEC section-by-section for coverage,
write `.ocean/REPORT.md`, merge worktree → main, `git push origin main`,
`vercel deploy --prod`, verify live URLs both hosts.
Accept: run complete, REPORT written, prod verified.

## Dependencies
Sprints 1–8 independent of each other (all touch disjoint files). Sprint 9 needs 1–8.
Sprint 10 needs 9.
