#!/usr/bin/env bash
# parse_rate.sh — Handshake 4a: DDD strain-rate sweep → lab-rate flow stress extrapolation
# Usage: ./parse_rate.sh [ddd_rate_sweep.dat] [options]
#
# Input format (whitespace-separated, # comments allowed):
#   strain_rate_s-1  tau_flow_MPa  [gamma]
# Rows at fixed plastic strain (default gamma = 0.01) at multiple DDD-accessible rates.
#
# Options:
#   --lab-rate R     target lab strain rate in s^-1 (default 1e-3)
#   --gamma G        plastic strain at which tau_flow is extracted (default 0.01)
#   --schmid S       Schmid factor for macro yield (default 0.408, fcc {111}<110>)
#   --compare PCT    fail if |tau_extrap - expected|/expected > PCT percent (optional)
#   --expected TAU   expected extrapolated tau in MPa for --compare
#
# Emits rate_export.yaml for archiving beside opendis.restart and hardening.yaml.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"
LAB_RATE="${LAB_RATE:-1e-3}"
REF_RATE="${REF_RATE:-1e3}"
GAMMA="${GAMMA:-0.01}"
SCHMID="${SCHMID:-0.408}"
COMPARE_PCT=""
EXPECTED_TAU=""

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --lab-rate) LAB_RATE="$2"; shift 2 ;;
    --ref-rate) REF_RATE="$2"; shift 2 ;;
    --gamma) GAMMA="$2"; shift 2 ;;
    --schmid) SCHMID="$2"; shift 2 ;;
    --compare) COMPARE_PCT="$2"; shift 2 ;;
    --expected) EXPECTED_TAU="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

resolve_input() {
  if [[ -z "$INPUT" ]]; then
    if [[ -f "$ROOT/fixtures/ddd_tau_vs_rate.dat" ]]; then
      echo "$ROOT/fixtures/ddd_tau_vs_rate.dat"
    else
      echo "FAIL: provide ddd_rate_sweep.dat" >&2
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

# Filter rows matching target gamma (or all if gamma column absent)
awk -v g="$GAMMA" '
  /^#/ || /^[[:space:]]*$/ { next }
  NF >= 2 {
    row_g = (NF >= 3) ? $3 : 0.01
    if (row_g == g || (NF < 3 && g == 0.01)) print $1, $2
  }
' "$DATA" > "$TMP"

N=$(wc -l < "$TMP")
[[ "$N" -ge 2 ]] || { echo "FAIL: need at least two strain-rate rows at gamma=$GAMMA in $DATA" >&2; exit 1; }

# Anchor tau_ref at REF_RATE (default 1e3 s^-1, matching epilogue DDD reference)
read -r TAU_REF EPS_REF <<< "$(awk -v ref="$REF_RATE" '
  { ed=$1; tau=$2; d=(log(ed)-log(ref))^2
    if (best=="" || d<best) { best=d; tau_ref=tau; eps_ref=ed }
  }
  END { if (tau_ref=="") { print "NA NA"; exit 1 } else printf "%.6f %.6e", tau_ref, eps_ref }
' "$TMP")"

if [[ "$TAU_REF" == "NA" ]]; then
  echo "FAIL: could not locate reference rate row near ${REF_RATE} s^-1" >&2
  exit 1
fi

# Fit m from log-log slope relative to anchor: ln(tau/tau_ref) = m * ln(ed/eps_ref)
read -r M <<< "$(awk -v eref="$EPS_REF" -v tref="$TAU_REF" '
  {
    ed = $1; tau = $2
    if (ed <= 0 || tau <= 0 || ed == eref) next
    lx = log(ed / eref)
    ly = log(tau / tref)
    n++; sx += lx; sy += ly; sxx += lx*lx; sxy += lx*ly
  }
  END {
    if (n < 1) { print "NA"; exit 1 }
    if (n == 1) { printf "%.6f", sy / sx; exit }
    denom = n * sxx - sx * sx
    if (denom == 0) { print "NA"; exit 1 }
    printf "%.6f", (n * sxy - sx * sy) / denom
  }
' "$TMP")"

if [[ "$M" == "NA" ]]; then
  echo "FAIL: could not fit power-law rate sensitivity" >&2
  exit 1
fi

# Extrapolate to lab rate
TAU_LAB=$(awk -v tref="$TAU_REF" -v m="$M" -v ed="$LAB_RATE" -v eref="$EPS_REF" \
  'BEGIN { printf "%.4f", tref * (ed / eref)^m }')

# Flow stress at REF_RATE (for direct-import comparison)
TAU_DDD_REF="$TAU_REF"

OVERPRED_PCT=$(awk -v direct="$TAU_DDD_REF" -v extrap="$TAU_LAB" \
  'BEGIN { if (extrap <= 0) print "NA"; else printf "%.1f", 100 * (direct - extrap) / extrap }')

SIGMA_LAB=$(awk -v tau="$TAU_LAB" -v s="$SCHMID" 'BEGIN { printf "%.1f", tau / s }')
SIGMA_DIRECT=$(awk -v tau="$TAU_DDD_REF" -v s="$SCHMID" 'BEGIN { printf "%.1f", tau / s }')

# Collect rates used
RATES=$(awk '{ printf "%s%s", (NR>1?", ":""), $1 }' "$TMP")

echo "# parse_rate.sh  Handshake 4a — DDD rate extrapolation to lab frame"
echo "# Input: $DATA"
echo "# gamma = $GAMMA; lab_rate = ${LAB_RATE} s^-1; Schmid = $SCHMID"
echo ""
echo "ddd_strain_rates_s-1 = [${RATES}]"
echo "rate_sensitivity_m = ${M}"
echo "tau_ref_MPa_at_eps_ref = ${TAU_REF}"
echo "eps_ref_s-1 = ${EPS_REF}"
echo "tau_flow_DDD_at_1e3_s-1_MPa = ${TAU_DDD_REF}"
echo "tau_flow_extrapolated_MPa = ${TAU_LAB}"
echo "sigma_y_extrapolated_MPa = ${SIGMA_LAB}"
echo "sigma_y_direct_DDD_import_MPa = ${SIGMA_DIRECT}"
echo "direct_import_overprediction_pct = ${OVERPRED_PCT}"
echo ""

cat <<YAML
# rate_export.yaml (archive beside opendis.restart and hardening.yaml)
handshake: 4a  # DDD strain rate → quasi-static load cell
material: Cu
source_file: ${DATA}
plastic_strain: ${GAMMA}
ddd_strain_rates_s-1: [${RATES}]
lab_target_strain_rate_s-1: ${LAB_RATE}
rate_sensitivity_m: ${M}
tau_flow_extrapolated_MPa: ${TAU_LAB}
tau_flow_DDD_at_1e3_s-1_MPa: ${TAU_DDD_REF}
sigma_y_extrapolated_MPa: ${SIGMA_LAB}
sigma_y_direct_import_MPa: ${SIGMA_DIRECT}
direct_import_overprediction_pct: ${OVERPRED_PCT}
schmid_factor: ${SCHMID}
extrapolation_method: power_law
temperature_K: 300
parser: parse_rate.sh
YAML

if [[ -n "$COMPARE_PCT" && -n "$EXPECTED_TAU" ]]; then
  awk -v got="$TAU_LAB" -v expected="$EXPECTED_TAU" -v pct="$COMPARE_PCT" 'BEGIN {
    if (expected == 0) exit 0
    diff = 100 * (got - expected) / expected
    if (diff < 0) diff = -diff
    if (diff > pct) {
      printf "FAIL: |tau_extrap - expected|/expected = %.2f%% exceeds %s%%\n", diff, pct > "/dev/stderr"
      exit 1
    }
  }'
fi

echo ""
echo "PASS: rate export complete (Handshake 4a)."
