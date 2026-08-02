#!/usr/bin/env bash
# parse_lifetime.sh — phonon lifetime audit from DFT ph.x or MD VACF width (Part VIII–IX)
# Usage: ./parse_lifetime.sh [phonon_lifetime.dat] [options]
#
# Input format (whitespace-separated, # comments allowed):
#   mode  omega_THz  linewidth_GHz  lifetime_ps  [source]
# At least one row required; LA row used for acoustic drag cross-check.
#
# Options:
#   --mode LABEL     mode label for primary export (default LA)
#   --compare PCT    fail if |lifetime - expected|/expected > PCT percent
#   --expected TAU   expected lifetime in ps for --compare
#
# Emits lifetime_export.yaml for archiving beside cu.phonon/phonon_lifetime.dat

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"
MODE="${MODE:-LA}"
COMPARE_PCT=""
EXPECTED_TAU=""

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode) MODE="$2"; shift 2 ;;
    --compare) COMPARE_PCT="$2"; shift 2 ;;
    --expected) EXPECTED_TAU="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

resolve_input() {
  if [[ -z "$INPUT" ]]; then
    if [[ -f "$ROOT/fixtures/cu.foundation/cu.phonon/phonon_lifetime.dat" ]]; then
      echo "$ROOT/fixtures/cu.foundation/cu.phonon/phonon_lifetime.dat"
    else
      echo "FAIL: provide phonon_lifetime.dat" >&2
      exit 1
    fi
  elif [[ -f "$INPUT" ]]; then
    echo "$INPUT"
  else
    echo "FAIL: not found: $INPUT" >&2
    exit 1
  fi
}

DATA="$(resolve_input)"
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

awk '!/^#/ && NF >= 4 { print $1, $2, $3, $4, (NF>=5 ? $5 : "unknown") }' "$DATA" > "$TMP"
N=$(wc -l < "$TMP")
[[ "$N" -ge 1 ]] || { echo "FAIL: need at least one mode row in $DATA" >&2; exit 1; }

read -r LA_OM LA_GHZ LA_PS LA_SRC <<< "$(awk -v m="$MODE" '$1 == m { print $2, $3, $4, $5; exit }' "$TMP")"
if [[ -z "$LA_OM" ]]; then
  read -r LA_OM LA_GHZ LA_PS LA_SRC <<< "$(awk 'NR==1 { print $2, $3, $4, $5 }' "$TMP")"
  MODE=$(awk 'NR==1 { print $1 }' "$TMP")
fi

MODE_LIST=$(awk '{ printf "%s%s", (NR>1?", ":""), $1 }' "$TMP")

echo "# parse_lifetime.sh  phonon lifetime audit (Part VIII–IX)"
echo "# Input: $DATA"
echo "# primary mode: $MODE"
echo ""
echo "mode_primary = ${MODE}"
echo "omega_primary_THz = ${LA_OM}"
echo "linewidth_primary_GHz = ${LA_GHZ}"
echo "lifetime_primary_ps = ${LA_PS}"
echo "source_primary = ${LA_SRC}"
echo "mode_list = [${MODE_LIST}]"
echo ""

cat <<YAML
# lifetime_export.yaml (archive beside cu.phonon/ and phonon_lifetime.dat)
handshake: MD-phonon-lifetime  # phonon drag cross-check for Handshake 4a mobility
material: Cu
source_file: ${DATA}
primary_mode: ${MODE}
results:
  omega_THz: ${LA_OM}
  linewidth_GHz: ${LA_GHZ}
  lifetime_ps: ${LA_PS}
  source: ${LA_SRC}
  mode_list: [${MODE_LIST}]
downstream:
  consumer: "Part VII mobility phonon drag; Part VIII kappa reduction"
parser: parse_lifetime.sh
YAML

if [[ -n "$COMPARE_PCT" && -n "$EXPECTED_TAU" ]]; then
  awk -v got="$LA_PS" -v expected="$EXPECTED_TAU" -v pct="$COMPARE_PCT" 'BEGIN {
    if (expected == 0) exit 0
    diff = 100 * (got - expected) / expected
    if (diff < 0) diff = -diff
    if (diff > pct) {
      printf "FAIL: |lifetime - expected|/expected = %.2f%% exceeds %s%%\n", diff, pct > "/dev/stderr"
      exit 1
    }
  }'
fi

echo ""
echo "PASS: phonon lifetime export complete."
