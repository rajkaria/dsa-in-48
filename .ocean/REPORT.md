# Ocean run report — ocean-20260807-130307

**Goal:** Expand all 13 Learn modules to 12–15 sections (beginner→advanced), add 3 new
modules (typescript, testing, web-platform), rewire every count, verify, deploy.

**Result: shipped.** The Learn track grew from 13 modules / ~80 sections / ~50h to
**16 modules / 221 sections / ~145h**, every module a beginner→intermediate→advanced
ladder with band dividers, every new section carrying a first-attempt-scored quiz.
Existing section ids and quiz qids were never renamed — reader progress survives.

## What shipped (sprint → commit)

| # | Sprint | Commit |
|---|--------|--------|
| 1 | js-fundamentals 7→15 + js-async 7→14 | `18329c9` |
| 2 | dsa-foundations 7→14 + dsa-structures 6→13 | `3641378` |
| 3 | dsa-trees-graphs 6→13 + dsa-algorithms 6→13 | `8eebf71` |
| 4 | react-deep-dive 7→15 + node-backend 7→15 | `f38600e` |
| 5 | postgres-databases 7→15 + aws-cloud 6→14 | `9368bfb` |
| 6 | system-design-backend 7→14 + frontend-system-design 7→14 | `d0e972a` |
| 7 | interview-kit 7→13 + NEW typescript (13) | `1ff647d` |
| 8 | NEW testing (13) + NEW web-platform (13) | `c550ece` |
| 9 | hub + landing + docs wiring, full recount | `0284c42` |
| 10 | browser sweep, title fixes, report, merge + deploy | (this commit) |

## Decisions worth human review (full journal: `.ocean/DECISIONS.md`)

- **One-way door — expand in place, never rename ids/qids.** Chosen over rewrite or
  companion pages to preserve `learn:<slug>:done` / `learn:<slug>:quiz` progress keys.
- **Spec deviations, both logged:** js-async's planned `combinators` section already
  existed as `parallel` (swapped in rejections/building/scheduling/iterasync/streams/
  workers/patterns instead); system-design-backend's planned chat worked-design already
  existed (swapped in a leaderboard design).
- **New accents:** typescript `#C084FC`, testing `#F87171`, web-platform `#94A3B8` —
  grep-verified distinct from all 13 existing accents.
- **Durations:** sections × ~40 min, rounded to 0.5h — hub cards, module heroes, hub
  hero (~145h), landing page, and README all recounted by hand and cross-checked.
- **Harness upgrade (sp2):** `scripts/check_pages.py` now enforces `data-qid`
  uniqueness after catching a real duplicate.

## Verification

- `bash scripts/verify.sh` green — 23 pages clean (tag balance, unique keys/qids,
  anchors, external-request allowlist, namespace hygiene).
- Hub `data-total` per card cross-checked against each module's actual `done-btn`
  count and its own `sec-count` label: 16/16 exact matches.
- Browser sweep (local server, Chromium): all 23 pages load with **zero console
  errors** and **zero horizontal overflow at 375px**. Hub verified visually in both
  themes; js-fundamentals verified dark, typescript verified light.
- Interactions verified live: runner panel executes, quiz stores first-attempt score
  (`learn:<slug>:quiz`), mark-section-done persists across reload (`learn:<slug>:done`),
  hub progress bars read those keys (3/15 → 20% bar), shared `learn:theme` persists.
- Stale-count grep: zero "13 modules" / "~50h" references anywhere.

## Known limitations

- Timer-based demos (event-loop stepper, scheduling demos) are throttled by the
  browser in hidden/background tabs — cosmetic only, standard browser behavior.
- typescript module has one runnable panel by design (no in-browser tsc); its depth
  rides on predict-the-error MCQs.
- Hub section totals remain hardcoded per card (house convention) — a future module
  edit must update its card, `sec-count`, and duration label by hand; verify.sh does
  not count sections.

## How to run / verify

```bash
bash scripts/verify.sh          # static gate, must print "OK — 23 pages clean"
python3 -m http.server 8000     # then open /learn/ — localStorage needs HTTP
```

Live: https://dsa-in-48.vercel.app/learn · https://rajkaria.github.io/dsa-in-48/learn/
