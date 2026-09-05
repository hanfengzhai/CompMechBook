#!/usr/bin/env bash
# parse_wham.sh — histogram reweighting for replica-exchange MD (WHAM-style)
# Usage: ./parse_wham.sh [histogram.dat] --target T_K [--compare long.dat]
#
# Input format (whitespace-separated, # comments allowed):
#   T_K  E_eV  count
#
# Reweights pooled replica-exchange histograms to --target T_K using log-sum-exp
# stabilized Boltzmann factors. With --compare, checks ≤ 5% stability in mean
# energy between two run lengths (Part VIII.3 Lab act pass criterion).
#
# For production free-energy surfaces, use LAMMPS fix wham or the WHAM tool;
# this script certifies the handoff checklist before exporting cross-slip rates.

set -euo pipefail

INPUT=""
TARGET_T=""
COMPARE=""

usage() {
  cat <<EOF
Usage: $0 [histogram.dat] --target T_K [--compare FILE]

Input columns: T_K  E_eV  count
EOF
  exit "${1:-0}"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET_T="${2:?}"; shift 2 ;;
    --compare) COMPARE="${2:?}"; shift 2 ;;
    -h|--help) usage 0 ;;
    -) INPUT="-"; shift ;;
    *)
      if [[ -z "$INPUT" ]]; then INPUT="$1"; else echo "Unknown arg: $1" >&2; usage 1; fi
      shift
      ;;
  esac
done

[[ -n "$TARGET_T" ]] || { echo "FAIL: --target T_K is required" >&2; exit 1; }
INPUT="${INPUT:-wham_histogram.dat}"

read_hist() {
  local file="$1"
  if [[ "$file" == "-" ]]; then
    grep -v '^#' | grep -v '^[[:space:]]*$'
  else
    [[ -f "$file" ]] || { echo "FAIL: missing $file" >&2; exit 1; }
    grep -v '^#' "$file" | grep -v '^[[:space:]]*$'
  fi
}

run_reweight() {
  local label="$1"
  local histfile="$2"
  python3 - "$label" "$TARGET_T" "$histfile" <<'PY'
import math, sys

label, target_T, histfile = sys.argv[1:4]
kB = 8.617333262e-5
beta0 = 1.0 / (kB * float(target_T))

rows = []
temps = set()
for line in open(histfile):
    p = line.split()
    if len(p) < 3:
        continue
    T, E, n = float(p[0]), float(p[1]), float(p[2])
    if n <= 0:
        continue
    rows.append((T, E, n))
    temps.add(T)

if len(temps) < 2:
    sys.exit("FAIL: need histograms from at least 2 replica temperatures")

# log weight for each row: log(n) - (beta0 - beta_T) * E
logw = []
for T, E, n in rows:
    betaT = 1.0 / (kB * T)
    lw = math.log(n) - (beta0 - betaT) * E
    logw.append(lw)

m = max(logw)
w = [math.exp(lw - m) for lw in logw]
Z = sum(w)
if Z <= 0:
    sys.exit("FAIL: normalization Z <= 0")

meanE = sum(wi * rows[i][1] for i, wi in enumerate(w)) / Z
neff = 1.0 / sum((wi / Z) ** 2 for wi in w)

print(f"label={label}")
print(f"target_T_K={float(target_T):.2f}")
print(f"reweighted_mean_E_eV={meanE:.6f}")
print(f"effective_sample_size={neff:.1f}")
print(f"n_replica_temperatures={len(temps)}")
print(f"n_histogram_rows={len(rows)}")
PY
}

TMP1=$(mktemp)
trap 'rm -f "$TMP1" "${TMP2:-}"' EXIT
read_hist "$INPUT" > "$TMP1"
[[ $(wc -l < "$TMP1") -ge 4 ]] || { echo "FAIL: need at least 4 histogram rows" >&2; exit 1; }

echo "# parse_wham.sh  input=$INPUT  target=${TARGET_T} K"
echo "# Histogram reweighting for parallel tempering (Part VIII.3 Lab act)"
echo ""

RESULT1=$(run_reweight "primary" "$TMP1")
echo "$RESULT1"
echo ""

MEAN1=$(echo "$RESULT1" | awk -F= '/reweighted_mean_E_eV/ {print $2}')
WHAM_OK="unknown"

if [[ -n "$COMPARE" ]]; then
  TMP2=$(mktemp)
  read_hist "$COMPARE" > "$TMP2"
  RESULT2=$(run_reweight "compare" "$TMP2")
  echo "$RESULT2"
  echo ""
  MEAN2=$(echo "$RESULT2" | awk -F= '/reweighted_mean_E_eV/ {print $2}')
  PCT=$(python3 - "$MEAN1" "$MEAN2" <<'PY'
import sys
a, b = map(float, sys.argv[1:3])
if abs(a) < 1e-15:
    print("NA")
else:
    print(f"{abs((b - a) / a * 100):.2f}")
PY
)
  PASS="no"
  python3 - "$PCT" <<'PY' && PASS="yes"
import sys
if sys.argv[1] != "NA" and float(sys.argv[1]) <= 5.0:
    raise SystemExit(0)
raise SystemExit(1)
PY
  WHAM_OK="$PASS"
  echo "convergence_pct_change=${PCT}"
  echo "wham_converged_5pct=${PASS}"
  echo ""
  if [[ "$PASS" == "yes" ]]; then
    echo "PASS: reweighted mean energy stable within 5% between runs."
  else
    echo "WARN: extend replica-exchange wall time or tighten replica spacing (target ≤ 5%)." >&2
  fi
fi

cat <<YAML

# wham_export.yaml (archive beside cross_slip_380K.yaml)
temperature_K: ${TARGET_T}
source_script: parse_wham.sh
input_histogram: ${INPUT}
reweighted_mean_E_eV: ${MEAN1}
wham_converged: ${WHAM_OK}
YAML
