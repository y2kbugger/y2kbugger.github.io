#!/usr/bin/env python3
"""Itemize an article's git history, rename- and format-agnostic.

The blog migrated articles from reStructuredText to Markdown, so a single
article (identified by its *slug* — the file basename without extension, since
``SLUGIFY_SOURCE = 'basename'``) may live at ``content/cat/slug.rst`` in old
history and ``content/cat/slug.md`` today. Articles were also re-slugged from
underscores to hyphens (``lc3_sql`` → ``lc3-sql``) to harmonize filenames.
``git log --follow`` stitches all of those renames (the extension change and
the separator change) back into one continuous history, and slug arguments are
matched ``_``/``-`` insensitively so either spelling resolves to the article.

This tool emits, per article, every commit that touched it with the date,
subject, body, and diff statistics. That itemized history is exactly what an
analyzer (human or a fast LLM subagent) needs to judge the *last substantial
content update* — as opposed to copy-editing, reformatting, or the format
migration — and decide what ``modified:`` date, if any, an article deserves.

Usage:
    python article_history.py [--json] [PATH_OR_SLUG ...]

With no arguments every article under ``content/`` is itemized. Arguments may
be file paths (``content/food/naan.md``) or bare slugs (``naan``). ``--json``
emits machine-readable output (one object per article) for piping into an
analyzer; the default is human-readable text.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CONTENT_DIR = Path("content")
ARTICLE_SUFFIXES = {".md", ".rst"}
# Delimiters that cannot occur in git log content, used to frame each record
# and separate its fields.
FIELD_SEP = "\x1f"  # unit separator
RECORD_SEP = "\x1e"  # record separator
# A ``--numstat`` line: "<added>\t<deleted>\t<path>" (added/deleted are "-" for
# binary files). These trail each commit's formatted header.
NUMSTAT_RE = re.compile(r"^[-\d]+\t[-\d]+\t")


def run_git(args: list[str]) -> str:
    """Run a git command and return its stdout, raising on failure."""
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def discover_articles() -> list[Path]:
    """All article source files currently tracked under ``content/``."""
    return sorted(
        p
        for p in CONTENT_DIR.rglob("*")
        if p.is_file() and p.suffix in ARTICLE_SUFFIXES
    )


def normalize_slug(slug: str) -> str:
    """Canonicalize a slug for matching, ignoring ``_`` vs ``-``.

    Articles were re-slugged from underscores to hyphens (e.g.
    ``lc3_sql`` → ``lc3-sql``); ``git log --follow`` stitches the rename into
    one history, but a user may still refer to an article by either spelling.
    Treating ``_`` and ``-`` as equivalent lets both resolve to the same file.
    """
    return slug.replace("_", "-")


def resolve_targets(args: list[str]) -> list[Path]:
    """Turn CLI arguments (paths or slugs) into existing article paths."""
    if not args:
        return discover_articles()
    articles = discover_articles()
    by_slug: dict[str, list[Path]] = {}
    for path in articles:
        by_slug.setdefault(normalize_slug(path.stem), []).append(path)

    resolved: list[Path] = []
    for arg in args:
        candidate = Path(arg)
        if candidate.is_file():
            resolved.append(candidate)
        elif normalize_slug(arg) in by_slug:
            resolved.extend(by_slug[normalize_slug(arg)])
        else:
            print(f"warning: no article matches {arg!r}", file=sys.stderr)
    return resolved


def commit_history(path: Path) -> list[dict]:
    """Itemized commits that touched ``path``, following renames.

    Each entry has ``hash``, ``date`` (author date, ``YYYY-MM-DD``),
    ``subject``, ``body``, and ``stat`` (the ``--numstat`` line(s) describing
    insertions/deletions/path for this file at that commit).
    """
    fmt = RECORD_SEP + FIELD_SEP.join(["%h", "%ad", "%s", "%b"])
    raw = run_git(
        [
            "log",
            "--follow",
            "--date=short",
            "--numstat",
            f"--format={fmt}",
            "--",
            str(path),
        ]
    )

    commits: list[dict] = []
    for chunk in raw.split(RECORD_SEP):
        if not chunk.strip():
            continue
        lines = chunk.splitlines()
        # Trailing lines are the file's numstat for this commit; everything
        # before them is the formatted header (whose body may span newlines).
        stat_lines = [ln for ln in lines if NUMSTAT_RE.match(ln)]
        header_lines = lines[: len(lines) - len(stat_lines)]
        header = "\n".join(header_lines)
        fields = header.split(FIELD_SEP)
        if len(fields) < 4:
            continue
        short_hash, date, subject, body = fields[0], fields[1], fields[2], fields[3]
        added = deleted = 0
        for line in stat_lines:
            a, d, _ = line.split("\t", 2)
            if a.isdigit() and d.isdigit():
                added += int(a)
                deleted += int(d)
        commits.append(
            {
                "hash": short_hash.strip(),
                "date": date.strip(),
                "subject": subject.strip(),
                "body": body.strip(),
                "added": added,
                "deleted": deleted,
            }
        )
    return commits


def front_matter_dates(path: Path) -> dict[str, str | None]:
    """Read the current ``date``/``modified`` values from front matter."""
    dates: dict[str, str | None] = {"date": None, "modified": None}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return dates
    for line in text.splitlines():
        low = line.lower()
        if low.startswith("date:") and dates["date"] is None:
            dates["date"] = line.split(":", 1)[1].strip()
        elif low.startswith("modified:") and dates["modified"] is None:
            dates["modified"] = line.split(":", 1)[1].strip()
    return dates


def build_record(path: Path) -> dict:
    commits = commit_history(path)
    return {
        "slug": path.stem,
        "path": str(path),
        "category": path.parent.name,
        "front_matter": front_matter_dates(path),
        "commits": commits,
    }


def print_text(record: dict) -> None:
    fm = record["front_matter"]
    print(f"=== {record['slug']}  ({record['path']})")
    print(f"    category: {record['category']}")
    print(f"    date:     {fm['date']}")
    print(f"    modified: {fm['modified']}")
    print(f"    commits:  {len(record['commits'])} (newest first)")
    for c in record["commits"]:
        churn = f"+{c['added']}/-{c['deleted']}"
        print(f"      {c['date']}  {churn:>12}  {c['hash']}  {c['subject']}")
        if c["body"]:
            for bline in c["body"].splitlines():
                if bline.strip():
                    print(f"          | {bline}")
    print()


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "targets",
        nargs="*",
        metavar="PATH_OR_SLUG",
        help="article paths or bare slugs; default is every article",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit machine-readable JSON (one object per article)",
    )
    args = parser.parse_args(argv)

    targets = resolve_targets(args.targets)
    if not targets:
        print("no matching articles", file=sys.stderr)
        return 1

    records = [build_record(p) for p in targets]
    if args.json:
        json.dump(records, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        for record in records:
            print_text(record)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
