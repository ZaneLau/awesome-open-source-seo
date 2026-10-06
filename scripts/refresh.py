#!/usr/bin/env python3
"""Refresh star counts, activity badges and archived flags in README.md / README.zh.md.

Pure stdlib. Reads GitHub repo metadata via the REST API (GITHUB_TOKEN env, optional),
rewrites the ``(1.5k★, MIT)`` counts, keeps the Active badge honest (commit in the
last 12 months) and appends a warning to archived repos.

Usage:
    python3 scripts/refresh.py            # update both READMEs in place
    python3 scripts/refresh.py --check    # report only, no writes (CI guard)
"""
import json
import os
import re
import sys
import time
import urllib.request

FILES = ["README.md", "README.zh.md"]
ACTIVE_BADGE = "![Active][Active Icon]"
ARCHIVE_FLAG = "⚠️ archived"
STALE_DAYS = 365

ENTRY_RE = re.compile(
    r"^(?P<pre>- \[[^\]]+\]\(https://github\.com/(?P<repo>[^/)]+/[^/)]+)\))"
    r"(?P<badges>(?: !\[[^\]]*\]\[[^\]]+\])*)"
    r"(?P<rest> — .*)$"
)
LINK_RE = re.compile(r"https://github\.com/([^/\s\")]+)/([^/\s\")]+)")
STARS_RE = re.compile(r"\((\d[\d.]*k?)★")
STAR_IN_RE = re.compile(r"(\d[\d.]*k?)★")


def api(url, token, payload=None):
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, headers={
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "awesome-open-source-seo-refresh",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r), r.status
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 502):
                time.sleep(4 * (attempt + 1))
                continue
            return None, e.code
        except Exception:
            time.sleep(3)
    return None, 0


def fmt_stars(n):
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def collect_repos(files):
    repos = {}
    for path in files:
        with open(path, encoding="utf-8") as f:
            for line in f:
                for owner, name in LINK_RE.findall(line):
                    if name.lower() in (".git", "topics"):
                        continue
                    repos.setdefault(f"{owner}/{name}".lower(), f"{owner}/{name}")
    return repos


def fetch_meta(repos, token):
    """Batch via GraphQL — one request per 40 repos instead of one per repo."""
    meta, gone = {}, []
    items = sorted(repos.items())
    for start in range(0, len(items), 40):
        chunk = items[start:start + 40]
        parts, payload_vars = [], {}
        for i, (key, full) in enumerate(chunk):
            owner, name = full.split("/")
            parts.append(
                f'r{i}: repository(owner: $o{i}, name: $n{i}) '
                f'{{ nameWithOwner stargazerCount pushedAt isArchived }}'
            )
            payload_vars[f"o{i}"], payload_vars[f"n{i}"] = owner, name
        query = "query(" + " ".join(f"${k}: String!" for k in payload_vars) + "){" + "".join(parts) + "}"
        data, status = api("https://api.github.com/graphql", token, {"query": query, "variables": payload_vars})
        if status != 200 or not data or "data" not in data:
            print(f"  ! GraphQL chunk failed (HTTP {status}) — repos skipped this run")
            continue
        for i, (key, full) in enumerate(chunk):
            node = (data.get("data") or {}).get(f"r{i}")
            if node is None:
                gone.append(full)
            else:
                meta[key] = {
                    "stargazers_count": node["stargazerCount"],
                    "pushed_at": node["pushedAt"],
                    "archived": node["isArchived"],
                }
        print(f"  … {min(start + 40, len(items))}/{len(items)} repos fetched")
    return meta, gone


def process(path, meta, write):
    out, changed = [], 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = ENTRY_RE.match(line)
            new = line
            if m:
                key = m.group("repo").lower()
                d = meta.get(key)
                if d:
                    rest = m.group("rest")
                    # 1. star count
                    if STARS_RE.search(rest):
                        n = fmt_stars(d.get("stargazers_count", 0))
                        rest = STAR_IN_RE.sub(n + "★", rest, count=1)
                    # 2. activity badge
                    badges = m.group("badges").replace(ACTIVE_BADGE, "").rstrip()
                    fresh = (time.time() - time.mktime(time.strptime(
                        d.get("pushed_at", "1970-01-01")[:10], "%Y-%m-%d"))) / 86400 < STALE_DAYS
                    if fresh:
                        badges = (badges + " " + ACTIVE_BADGE).replace("  ", " ")
                    # 3. archived flag
                    if d.get("archived") and ARCHIVE_FLAG not in rest:
                        rest = rest.rstrip() + " " + ARCHIVE_FLAG
                    newline = "\n" if line.endswith("\n") else ""
                    new = m.group("pre") + badges + rest + newline
            if new != line:
                changed += 1
            out.append(new)
    if write and changed:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(out)
    return changed


def main():
    args = sys.argv[1:]
    token = os.environ.get("GITHUB_TOKEN", "")
    files = [a for a in args if a.endswith(".md")] or FILES
    check = "--check" in args

    repos = collect_repos(files)
    print(f"Found {len(repos)} unique GitHub repos across {len(files)} files")
    meta, gone = fetch_meta(repos, token)
    if gone:
        print("404 (candidates for removal):")
        for g in gone:
            print(f"  - {g}")
    if not meta:
        print("No repo metadata fetched — aborting")
        sys.exit(1)

    total = 0
    for path in files:
        changed = process(path, meta, write=not check)
        total += changed
        print(f"{path}: {changed} line(s) {'would change' if check else 'updated'}")
    print(f"Done — {total} line(s) total, {len(gone)} repo(s) gone")
    sys.exit(1 if (check and total) else 0)


if __name__ == "__main__":
    main()
