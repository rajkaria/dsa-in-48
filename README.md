# in 48 — weekend crash syllabi for working engineers

**Two-day interview-prep courses for full-stack JavaScript engineers.** Each course is one
self-contained HTML file: no build, no dependencies to install, no CS degree assumed. Open
it, work through it, walk into the interview.

**Start here:** [dsa-in-48.vercel.app](https://dsa-in-48.vercel.app/) — the series landing page, which
routes you to whichever course you need (and to every future one).

| course | what it covers | read it |
|---|---|---|
| **DSA in 48** | 13 data-structure & algorithm topics, 48 link-verified LeetCode problems, interview playbook, pattern matcher | [/dsa](https://dsa-in-48.vercel.app/dsa) · [GitHub Pages](https://rajkaria.github.io/dsa-in-48/dsa.html) |
| **System Design in 48** | 12 system-design topics, 32 whiteboard drills, the 6-step interview framework, 3 classic designs (URL shortener · feed · chat) | [/system-design](https://dsa-in-48.vercel.app/system-design) · [GitHub Pages](https://rajkaria.github.io/dsa-in-48/system-design.html) |
| **Behavioral in 48** | 13 behavioral & leadership topics for senior loops at US product companies — story bank, STAR+, hiring-manager round, 40-question senior bank, negotiation | [/behavioral](https://dsa-in-48.vercel.app/behavioral) · [GitHub Pages](https://rajkaria.github.io/dsa-in-48/behavioral.html) |
| **Full-Stack in 48** | 12 tech-screen topics across JavaScript, React, Node.js, PostgreSQL & AWS — 150+ rapid-fire questions with answers, cheat tables, the night-before refresher | [/fullstack](https://dsa-in-48.vercel.app/fullstack) · [GitHub Pages](https://rajkaria.github.io/dsa-in-48/fullstack.html) |
| **Frontend System Design in 48** | 12 topics for the senior frontend design round — RADIO walkthrough, rendering strategies, state & data architecture, CWV, resilience, a11y, security — 140+ Q&As with answers | [/frontend-system-design](https://dsa-in-48.vercel.app/frontend-system-design) · [GitHub Pages](https://rajkaria.github.io/dsa-in-48/frontend-system-design.html) |

**Not cramming?** The **[Learn track](https://dsa-in-48.vercel.app/learn)** is the other speed:
sixteen self-paced, beginner-to-advanced modules (JS ×2, TypeScript, DSA ×4, React, Node,
PostgreSQL, AWS, testing, system design ×2, the web platform, and an interview kit with
persisted worksheets) — plain language,
code that runs on the page, quizzes, visualizers, and per-module progress, with a
nine-question three-tier reasoning gym closing every module (369 quiz questions across
the track). Each module is
one self-contained HTML file under [`learn/`](./learn/), same rules as the courses.

---

## Who this is for

You've shipped production systems for years. You already *use* every structure and *operate*
every component in these courses — you've just never had to *name them under pressure*.
Both syllabi attach interview vocabulary and patterns to instincts you already have:

| you ship this daily | DSA calls it | you deploy this daily | system design calls it |
|---|---|---|---|
| the call stack in DevTools | Stack | nginx in front of PM2 workers | Load Balancer |
| `{}` and `new Map()` | Hash Map | Redis holding sessions | Cache |
| the DOM · component tree | Tree | a MongoDB replica set | Replication |
| `node_modules` dependencies | Graph | BullMQ email jobs | Message Queue |
| `useMemo` · a Redis cache | Dynamic Programming | socket.io + Redis adapter | Pub/Sub |

## The format

Both courses share the same structure — a timed two-day schedule (~8.5h/day) where every
topic is a block of:

1. a plain-English **idea** with the MERN mapping ("you already know this"),
2. one **snippet or diagram** worth internalizing,
3. **trigger phrases** — "when the problem says X, reach for Y",
4. a short **drill set** with checkboxes (progress + theme persist in `localStorage`;
   nothing is sent anywhere).

After the last topic, every course has a **reasoning gym**: twelve scored multiple-choice
questions in three tiers (warm-up → apply → stretch) built to train inference — trace the
state, locate the layer, catch the false claim, estimate the cost — with a first-attempt
score that persists locally.

Plus reference sections: an interview playbook, a 10-second pattern/component index,
complexity & latency cheat tables, and an honest "safe to skip" list. Both pages tell you
which subset to do if you only have one day.

## Running locally

Single self-contained files — just open them:

```bash
open index.html
```

`index.html` is the landing page; `dsa.html`, `system-design.html`, `behavioral.html`,
`fullstack.html`, and `frontend-system-design.html` are the courses; `learn/` holds the
Learn track (hub + 16 modules). Serve over HTTP (not `file://`) for localStorage progress
to behave, and run `bash scripts/verify.sh` for the static checks (tag balance, anchors,
unique drill keys, external-request allowlist).

Or serve the folder:

```bash
python3 -m http.server 8000
```

Fonts and syntax highlighting load from CDNs (with subresource integrity); pages degrade
gracefully to system fonts when offline.

## Deploys

- **Vercel** — config in `vercel.json`, clean URLs so `/dsa` and `/system-design` work
  without the `.html`.
- **GitHub Pages** — serves the same files from `main` at
  [rajkaria.github.io/dsa-in-48](https://rajkaria.github.io/dsa-in-48/).

## Contributing

Corrections, better analogies, and swapped-in problems/drills are welcome — open an issue
or a PR. House rules:

- **Keep each course one file.** No build step, no framework, no dependencies.
- **Keep it honest.** Complexity claims must be correct; every LeetCode link must point at
  a real, currently-live problem; every capacity number should survive a back-of-envelope
  check.

## License

[MIT](LICENSE) — use it, fork it, teach from it.

LeetCode problem names and numbers are referenced for study purposes; the problems
themselves belong to LeetCode.
