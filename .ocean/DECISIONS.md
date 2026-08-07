# Decisions — ocean-20260807-130307

- 2026-08-07 (planning, one-way door): **Expand in place, never rename existing section ids/qids** — options were in-place expansion, full rewrite, companion advanced pages. Chosen for progress-key preservation (learn:<slug>:done / :quiz reference ids) and to keep ~1.1MB of verified content. Cost to reverse: high (a later rewrite would break reader progress anyway).
- 2026-08-07 (planning): New-module accents — typescript purple #C084FC, testing red #F87171, web-platform slate #94A3B8; all distinct from the 13 existing accents (grep-verified against learn hub --acc list). Two-way door.
- 2026-08-07 (planning): Shelf placement — typescript→js, testing→build, web-platform→systems; 5 shelves stay. Two-way door.
- 2026-08-07 (planning): Duration labels = sections × ~40min rounded to 0.5h; honesty rule per CLAUDE.md. Two-way door.
- 2026-08-07 (planning): Prod deploy in sprint 10 is pre-authorized — Raj explicitly chose "Approve — run it" over "Approve, but deploy manually" in-session.
- 2026-08-07 (sp1): js-async — spec's planned `combinators` section already exists as `parallel` (combinators+loop trap), and debounce/throttle live in `cancel`. Swapped new sections to: rejections, building (promisify/deferred/event-interop), scheduling, iterasync, streams, workers, patterns (pool/dedupe/polling implementations). Still +7 → 14 sections. Two-way door.
- 2026-08-07 (sp2): added data-qid uniqueness to check_pages.py after catching a real duplicate (dsf-hash-1 reused by the new hashing section — renamed dsf-hashing-1). Harness now guards all remaining quiz-heavy sprints.
- 2026-08-07 (sp6): workedplus design #3 — spec said chat/proximity/ticketing but chat already exists in the worked section (design 4); swapped in a leaderboard design (sorted sets/skip lists — ties dss balance + heaps sections). Two-way door.
