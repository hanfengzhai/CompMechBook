#!/usr/bin/env bash
# parse_lifetime.sh — phonon lifetime audit from DFT ph.x or MD VACF width (Part VIII–IX)
# Usage: ./parse_lifetime.sh [phonon_lifetime.dat] [options]
#
# Input format (whitespace-separated, # comments allowed):
#   mode  omega_THz  linewidth_GHz  lifetime_ps  [source]
# At least one row required; LA row used for acoustic drag cross-check.
#
# Temperature sweep format (auto-detected when first data column is numeric T_K):
#   T_K  mode  omega_THz  linewidth_GHz  lifetime_ps  [source]
#
# Options:
#   --mode LABEL     mode label for primary export (default LA)
#   --target-t T     report lifetime at this temperature in sweep mode (default 300)
#   --compare PCT    fail if |lifetime - expected|/expected > PCT percent
#   --expected TAU   expected lifetime in ps for --compare
#
# Emits lifetime_export.yaml for archiving beside cu.phonon/phonon_lifetime.dat

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"
MODE="${MODE:-LA}"
TARGET_T="${TARGET_T:-300}"
COMPARE_PCT=""
EXPECTED_TAU=""

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode) MODE="$2"; shift 2 ;;
    --target-t) TARGET_T="$2"; shift 2 ;;
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

# Detect temperature-sweep format: first data column is numeric T_K, second is mode label
SWEEP=0
FIRST_ROW=$(awk '!/^#/ && NF >= 4 { print; exit }' "$DATA")
if [[ -n "$FIRST_ROW" ]]; then
  COL1=$(echo "$FIRST_ROW" | awk '{print $1}')
  COL2=$(echo "$FIRST_ROW" | awk '{print $2}')
  if [[ "$COL1" =~ ^[0-9]+(\.[0-9]+)?$ && ! "$COL2" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    SWEEP=1
  fi
fi

if [[ "$SWEEP" -eq 1 ]]; then
  awk -v m="$MODE" '!/^#/ && NF >= 5 && $2 == m { print $1, $3, $4, $5, (NF>=6 ? $6 : "unknown") }' "$DATA" > "$TMP"
  N=$(wc -l < "$TMP")
  [[ "$N" -ge 1 ]] || { echo "FAIL: need at least one sweep row for mode=$MODE in $DATA" >&2; exit 1; }

  T_LIST=$(awk '{ printf "%s%s", (NR>1?", ":""), $1 }' "$TMP")
  read -r LA_T LA_OM LA_GHZ LA_PS LA_SRC <<< "$(awk -v t="$TARGET_T" '
    { tk=$1; d=(tk-t)^2
      if (best=="" || d<best) { best=d; t_ref=tk; om=$2; ghz=$3; ps=$4; src=$5 }
    }
    END { if (t_ref=="") exit 1; else printf "%.0f %.6f %.6f %.6f %s", t_ref, om, ghz, ps, src }
  ' "$TMP")"

  # Linear fit d(ln tau)/dT for drag temperature pedigree (Handshake 4a coupling)
  read -r DRAG_SLOPE <<< "$(awk '
    { t=$1; tau=$4; if (tau <= 0) next; lt = log(tau); n++; sx += t; sy += lt; sxx += t*t; sxy += t*lt }
    END {
      if (n < 2) { print "NA"; exit }
      denom = n * sxx - sx * sx
      if (denom == 0) { print "NA"; exit }
      printf "%.6f", (n * sxy - sx * sy) / denom
    }
  ' "$TMP")"

  echo "# parse_lifetime.sh  phonon lifetime temperature sweep (Part VIII–IX)"
  echo "# Input: $DATA"
  echo "# primary mode: $MODE; target_T = ${TARGET_T} K"
  echo ""
  echo "sweep_mode = yes"
  echo "temperature_list_K = [${T_LIST}]"
  echo "mode_primary = ${MODE}"
  echo "target_temperature_K = ${LA_T}"
  echo "omega_primary_THz = ${LA_OM}"
  echo "linewidth_primary_GHz = ${LA_GHZ}"
  echo "lifetime_primary_ps = ${LA_PS}"
  echo "source_primary = ${LA_SRC}"
  echo "ln_tau_vs_T_slope = ${DRAG_SLOPE}"
  echo ""

  cat <<YAML
# lifetime_export.yaml (archive beside cu.phonon/ and phonon_lifetime_vs_T.dat)
handshake: MD-phonon-lifetime  # phonon drag cross-check for Handshake 4a mobility
material: Cu
source_file: ${DATA}
sweep: yes
primary_mode: ${MODE}
target_temperature_K: ${LA_T}
temperature_list_K: [${T_LIST}]
results:
  omega_THz: ${LA_OM}
  linewidth_GHz: ${LA_GHZ}
  lifetime_ps: ${LA_PS}
  source: ${LA_SRC}
  ln_tau_vs_T_slope: ${DRAG_SLOPE}
downstream:
  consumer: "Part VII mobility phonon drag; Handshake 4a rate at elevated T"
parser: parse_lifetime.sh
YAML

  COMPARE_TAU="$LA_PS"
else
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
  echo "sweep_mode = no"
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
sweep: no
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

  COMPARE_TAU="$LA_PS"
fi

if [[ -n "$COMPARE_PCT" && -n "$EXPECTED_TAU" ]]; then
  awk -v got="$COMPARE_TAU" -v expected="$EXPECTED_TAU" -v pct="$COMPARE_PCT" 'BEGIN {
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
