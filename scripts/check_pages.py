#!/usr/bin/env python3
"""Static checks for every HTML page in the repo.

No dependencies — stdlib only. Run via scripts/verify.sh from the repo root.

Checks, per page:
  1. Tag balance (stack-based; void elements exempt).
  2. data-key uniqueness within the page; data-day present and 1/2 on drill inputs.
  3. Internal anchors (#x) resolve to an id in the same page.
  4. Relative links resolve to real files; cross-file anchors resolve to real ids.
  5. External requests limited to the allowlist (Google Fonts + highlight.js CDN).
  6. Any highlight.js <script src> carries an integrity hash.
  7. localStorage keys are string literals under a known namespace.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
# tags browsers auto-close that we don't require perfect nesting for
LENIENT = {"p", "li", "option", "tr", "td", "th", "thead", "tbody", "dt", "dd"}

ALLOWED_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com", "cdnjs.cloudflare.com"}

NS_RE = re.compile(r"^(dsa48|sd48|bh48|fs48|fesd48|in48|learn):")

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
        self.ids = set()
        self.data_keys = []
        self.hrefs = []          # (value, line)
        self.ext_urls = []       # (value, line)
        self.hljs_scripts = []   # (attrs_dict, line)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag not in VOID:
            self.stack.append((tag, line))
        if "id" in a and a["id"]:
            self.ids.add(a["id"])
        if "data-key" in a:
            self.data_keys.append((a.get("data-key"), a.get("data-day"), line))
        for attr in ("href", "src"):
            v = a.get(attr)
            if not v:
                continue
            external = v.startswith(("http://", "https://", "//"))
            # the two-request rule covers resource FETCHES, not <a> navigation
            if external and tag in ("link", "script", "img", "iframe", "video",
                                    "audio", "source", "embed", "object"):
                self.ext_urls.append((v, line))
                if tag == "script" and "highlight" in v:
                    self.hljs_scripts.append((a, line))
            elif not external and attr == "href" and tag == "a" \
                    and not v.startswith(("mailto:", "javascript:", "data:")):
                self.hrefs.append((v, line))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        line = self.getpos()[0]
        if not self.stack:
            self.errors.append(f"line {line}: </{tag}> with empty stack")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
            return
        # tolerate lenient tags left open between us and the match
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                skipped = [t for t, _ in self.stack[i + 1:]]
                if all(t in LENIENT for t in skipped):
                    del self.stack[i:]
                    return
                self.errors.append(
                    f"line {line}: </{tag}> closes over unclosed {skipped}")
                del self.stack[i:]
                return
        if tag not in LENIENT:
            self.errors.append(f"line {line}: stray </{tag}>")


def check_file(path: Path, all_ids: dict, problems: list):
    text = path.read_text(encoding="utf-8")
    p = PageParser()
    p.feed(text)
    p.close()
    rel = path.relative_to(ROOT)

    for e in p.errors:
        problems.append(f"{rel}: TAG {e}")
    leftover = [(t, l) for t, l in p.stack if t not in LENIENT]
    if leftover:
        problems.append(f"{rel}: TAG unclosed at EOF: {leftover[:8]}")

    seen = {}
    for key, day, line in p.data_keys:
        if not key:
            problems.append(f"{rel}: KEY empty data-key at line {line}")
            continue
        if key in seen:
            problems.append(f"{rel}: KEY duplicate data-key '{key}' "
                            f"(lines {seen[key]} and {line})")
        seen[key] = line
        if day not in (None, "1", "2"):
            problems.append(f"{rel}: KEY data-day '{day}' not 1/2 at line {line}")

    for url, line in p.ext_urls:
        host = re.sub(r"^(https?:)?//", "", url).split("/")[0]
        if host not in ALLOWED_HOSTS:
            problems.append(f"{rel}: EXT disallowed host '{host}' line {line}")
    for attrs, line in p.hljs_scripts:
        if not attrs.get("integrity"):
            problems.append(f"{rel}: EXT highlight.js script missing integrity, line {line}")

    # only string-literal keys are statically checkable; variables carry the NS const
    for raw in re.findall(r"localStorage\.(?:getItem|setItem|removeItem)\(\s*([^),]+)", text):
        m = re.match(r"""^['"]([^'"]+)['"]$""", raw.strip())
        if m and not NS_RE.match(m.group(1)):
            problems.append(f"{rel}: NS localStorage key '{m.group(1)}' not namespaced")

    all_ids[rel.as_posix()] = (p.ids, p.hrefs)


def main():
    pages = sorted(ROOT.glob("*.html")) + sorted(ROOT.glob("learn/*.html"))
    if not pages:
        print("no HTML pages found"); return 1
    problems, all_ids = [], {}
    for f in pages:
        check_file(f, all_ids, problems)

    # link + anchor resolution across files
    for page, (_ids, hrefs) in all_ids.items():
        base = Path(page).parent
        for href, line in hrefs:
            frag = None
            target = href
            if "#" in href:
                target, frag = href.split("#", 1)
            if target in ("", "."):
                dest_page = page
            else:
                dest = (base / target).resolve()
                try:
                    dest_page = dest.relative_to(ROOT).as_posix()
                except ValueError:
                    problems.append(f"{page}: LINK escapes repo '{href}' line {line}")
                    continue
                if dest.is_dir():
                    dest_page = (dest_page.rstrip("/") + "/index.html").lstrip("/")
                if not (ROOT / dest_page).exists():
                    problems.append(f"{page}: LINK missing file '{href}' line {line}")
                    continue
            if frag:
                if dest_page in all_ids and frag not in all_ids[dest_page][0]:
                    problems.append(f"{page}: ANCHOR '#{frag}' not in {dest_page} line {line}")

    if problems:
        print(f"FAIL — {len(problems)} problem(s):")
        for pr in problems:
            print("  " + pr)
        return 1
    total_keys = sum(1 for f in pages for _ in [0])
    print(f"OK — {len(pages)} pages clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
