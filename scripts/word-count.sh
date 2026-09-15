#!/usr/bin/env bash
# Report word counts for the main book and each Writings subtree.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

count_words() {
  find "$1" -name '*.md' -print0 | xargs -0 wc -w 2>/dev/null | tail -1 | awk '{print $1}'
}

main_count="$(count_words "$ROOT/src")"
echo "CompMechBook src/: $main_count words"

for dir in "$ROOT"/writings/*/chapters; do
  [[ -d "$dir" ]] || continue
  name="$(basename "$(dirname "$dir")")"
  part_count="$(count_words "$dir")"
  echo "  writings/$name: $part_count words"
done
