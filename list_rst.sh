#!/usr/bin/env bash
# List remaining reStructuredText articles still awaiting conversion to Markdown.
# Prints each .rst file under content/ with its article date and modified date
# (pulled from the RST metadata, not the filesystem), sorted by path.
set -euo pipefail

cd "$(dirname "$0")"

shopt -s globstar nullglob
files=(content/**/*.rst)

if [ "${#files[@]}" -eq 0 ]; then
    echo "No .rst files remain — migration to Markdown is complete."
    exit 0
fi

for f in "${files[@]}"; do
    date=$(grep -m1 -iE '^:date:' "$f" | sed 's/^:date:[[:space:]]*//I' || true)
    modified=$(grep -m1 -iE '^:modified:' "$f" | sed 's/^:modified:[[:space:]]*//I' || true)
    printf '%-55s date=%-21s modified=%s\n' "$f" "${date:--}" "${modified:--}"
done | sort
