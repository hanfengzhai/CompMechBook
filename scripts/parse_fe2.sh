#!/usr/bin/env bash
# parse_fe2.sh — Handshake 4b: FE² notch comparison audit
# Usage: ./parse_fe2.sh [fe2_notch_comparison.dat] [options]
#
# Input format (whitespace-separated, # comments allowed):
#   model  peak_sigma_eq_MPa  plastic_zone_um  cpu_relative
# Expects rows for scalar_j2, crystal_plasticity, and fe2 models.
#
# Options:
#   --enrich-threshold PCT   FE² vs CP uplift above which enrichment required (default 10)
#   --offline-threshold PCT    FE² vs CP uplift below which offline calibration suffices (default 5)
#   --compare PCT              fail if fe2_vs_cp_uplift differs from --expected by PCT
#   --expected UPLIFT          expected uplift percent for --compare
#
# Emits fe2_export.yaml for archiving beside fe2_notch.log and fe2_zones.txt

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"
ENRICH_THRESH="${ENRICH_THRESH:-10}"
OFFLINE_THRESH="${OFFLINE_THRESH:-5}"
COMPARE_PCT=""
EXPECTED_UPLIFT=""

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --enrich-threshold) ENRICH_THRESH="$2"; shift 2 ;;
    --offline-threshold) OFFLINE_THRESH="$2"; shift 2 ;;
    --compare) COMPARE_PCT="$2"; shift 2 ;;
    --expected) EXPECTED_UPLIFT="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

resolve_input() {
  if [[ -z "$INPUT" ]]; then
    if [[ -f "$ROOT/fixtures/fe2_notch_comparison.dat" ]]; then
      echo "$ROOT/fixtures/fe2_notch_comparison.dat"
    else
      echo "FAIL: provide fe2_notch_comparison.dat" >&2
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

awk '!/^#/ && NF >= 4 { print $1, $2, $3, $4 }' "$DATA" > "$TMP"
[[ -s "$TMP" ]] || { echo "FAIL: no data rows in $DATA" >&2; exit 1; }

get_row() {
  local key="$1"
  awk -v k="$key" '$1 == k { print $2, $3, $4; exit }' "$TMP"
}

read -r SIG_SCALAR PZ_SCALAR CPU_SCALAR <<< "$(get_row scalar_j2_4a)"
read -r SIG_CP PZ_CP CPU_CP <<< "$(get_row crystal_plasticity)"
read -r SIG_FE2 PZ_FE2 CPU_FE2 <<< "$(get_row fe2_48_active)"

[[ -n "$SIG_SCALAR" && -n "$SIG_CP" && -n "$SIG_FE2" ]] || {
  echo "FAIL: need scalar_j2_4a, crystal_plasticity, fe2_48_active rows" >&2
  exit 1
}

FE2_VS_CP=$(awk -v fe2="$SIG_FE2" -v cp="$SIG_CP" 'BEGIN { printf "%.2f", 100 * (fe2 - cp) / cp }')
FE2_VS_SCALAR=$(awk -v fe2="$SIG_FE2" -v sc="$SIG_SCALAR" 'BEGIN { printf "%.2f", 100 * (fe2 - sc) / sc }')
CP_VS_SCALAR=$(awk -v cp="$SIG_CP" -v sc="$SIG_SCALAR" 'BEGIN { printf "%.2f", 100 * (cp - sc) / sc }')

FE2_ENRICH=$(awk -v u="$FE2_VS_CP" -v t="$ENRICH_THRESH" 'BEGIN { print (u > t) ? "yes" : "no" }')
OFFLINE_OK=$(awk -v u="$FE2_VS_CP" -v t="$OFFLINE_THRESH" 'BEGIN { print (u <= t) ? "yes" : "no" }')

echo "# parse_fe2.sh  Handshake 4b — FE² notch-root stress audit"
echo "# Input: $DATA"
echo ""
echo "peak_sigma_scalar_MPa = ${SIG_SCALAR}"
echo "peak_sigma_crystal_plasticity_MPa = ${SIG_CP}"
echo "peak_sigma_fe2_MPa = ${SIG_FE2}"
echo "plastic_zone_fe2_um = ${PZ_FE2}"
echo "cpu_relative_fe2 = ${CPU_FE2}"
echo "fe2_vs_cp_uplift_pct = ${FE2_VS_CP}"
echo "fe2_vs_scalar_uplift_pct = ${FE2_VS_SCALAR}"
echo "cp_vs_scalar_uplift_pct = ${CP_VS_SCALAR}"
echo "fe2_enrichment_required = ${FE2_ENRICH}"
echo "offline_calibration_sufficient = ${OFFLINE_OK}"
echo ""

cat <<YAML
# fe2_export.yaml (archive beside fe2_notch.log and fe2_zones.txt)
handshake: 4b  # FE² at notch when homogenization under-predicts localization
material: Cu
source_file: ${DATA}
models:
  scalar_j2_4a:
    peak_sigma_eq_MPa: ${SIG_SCALAR}
    plastic_zone_um: ${PZ_SCALAR}
    cpu_relative: ${CPU_SCALAR}
  crystal_plasticity:
    peak_sigma_eq_MPa: ${SIG_CP}
    plastic_zone_um: ${PZ_CP}
    cpu_relative: ${CPU_CP}
  fe2_48_active:
    peak_sigma_eq_MPa: ${SIG_FE2}
    plastic_zone_um: ${PZ_FE2}
    cpu_relative: ${CPU_FE2}
results:
  fe2_vs_cp_uplift_pct: ${FE2_VS_CP}
  fe2_vs_scalar_uplift_pct: ${FE2_VS_SCALAR}
  cp_vs_scalar_uplift_pct: ${CP_VS_SCALAR}
  fe2_enrichment_required: ${FE2_ENRICH}
  offline_calibration_sufficient: ${OFFLINE_OK}
  enrich_threshold_pct: ${ENRICH_THRESH}
  offline_threshold_pct: ${OFFLINE_THRESH}
parser: parse_fe2.sh
YAML

if [[ -n "$COMPARE_PCT" && -n "$EXPECTED_UPLIFT" ]]; then
  awk -v got="$FE2_VS_CP" -v expected="$EXPECTED_UPLIFT" -v pct="$COMPARE_PCT" 'BEGIN {
    diff = got - expected
    if (diff < 0) diff = -diff
    if (diff > pct) {
      printf "FAIL: |fe2_vs_cp_uplift - expected| = %.2f exceeds %s\n", diff, pct > "/dev/stderr"
      exit 1
    }
  }'
fi

echo ""
echo "PASS: FE² export complete (Handshake 4b)."
