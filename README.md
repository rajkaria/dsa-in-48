# DSA in 48

**A two-day data structures & algorithms crash syllabus for working full-stack JavaScript engineers.**

One HTML file. No build, no dependencies to install, no CS degree assumed. Open it, work through it, walk into the interview.

📄 **[Read it here →](https://rajkaria.github.io/dsa-in-48/)**

---

## Who this is for

You've shipped production systems for years. You already *use* every structure in this
course — you've just never had to *name it under pressure*. This syllabus attaches
interview vocabulary and patterns to instincts you already have.

Every concept is mapped to something you've already deployed:

| you ship this daily | it's called |
|---|---|
| the call stack in DevTools | Stack |
| the event loop's task queue | Queue |
| `{}` and `new Map()` | Hash Map |
| the DOM · your component tree | Tree |
| the Express middleware chain | Linked List |
| `node_modules` dependencies | Graph |
| a MongoDB index (B-tree) | Binary Search |
| `useMemo` · a Redis cache | Dynamic Programming |

## What's inside

- **13 timed topics** across two ~8.5-hour days, each with a plain-English idea, a
  JavaScript snippet worth memorizing, trigger phrases that reveal the pattern, and a
  short problem set.
- **48 curated LeetCode problems**, every one linked and difficulty-tagged, ordered
  easy-first so each easy installs the template and each medium makes it stick.
- **The interview playbook** — the seven-step script to run in the room, plus the
  JavaScript-specific gotchas (`.sort()` lies, there's no built-in heap) that are free
  points when you name them.
- **A pattern matcher** — the 10-second index from "the problem says X" to "start with Y",
  plus complexity cheat tables for every structure and algorithm.
- **A "safe to skip" list**, so you spend the 48 hours on what actually gets asked.

**Day 1 — foundations:** Big O · arrays & two pointers · sliding window · hash maps & sets ·
stacks & queues · linked lists · recursion

**Day 2 — branches:** binary search · trees (BFS & DFS) · heaps · graphs · backtracking ·
dynamic programming

## How to use it

1. Open the page and follow the schedule. The clock is the point — depth comes from
   repetition later, not from this weekend.
2. **Retype every snippet.** Reading code is not learning code. Run it, then rewrite it
   from memory.
3. **The 25-minute rule.** Stuck past 25 minutes? Read the solution, close it, re-code it
   blind. This weekend you're studying patterns, not grinding.
4. **Check off problems as you go.** Progress and theme are saved in your browser
   (`localStorage`) — nothing is sent anywhere.

Only have one day? The page tells you which five topics cover ~70% of what gets asked.

## Running it locally

It's a single self-contained file — just open it:

```bash
open index.html
```

Or serve it, if you prefer a real origin:

```bash
python3 -m http.server 8000
```

Fonts and syntax highlighting load from CDNs (with subresource integrity); the page
degrades gracefully to system fonts and unhighlighted code when offline.

## Contributing

Corrections, better analogies, and swapped-in problems are welcome — open an issue or a
PR. Two house rules:

- **Keep it one file.** No build step, no framework, no dependencies.
- **Keep it honest.** Every claim about complexity should be correct, and every problem
  link should point at a real, currently-live LeetCode problem.

## License

[MIT](LICENSE) — use it, fork it, teach from it.

LeetCode problem names and numbers are referenced for study purposes; the problems
themselves belong to LeetCode.
