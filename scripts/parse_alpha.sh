#!/usr/bin/env bash
# parse_alpha.sh — Handshake 3 thermal expansion from quasiharmonic a(T) table
# Usage: ./parse_alpha.sh [phonon_dir|a_vs_T.dat] [options]
#
# Reads cu.phonon/a_vs_T.dat (T_K, a_angstrom columns), computes
#   α = (1/a) da/dT at a target temperature, and optionally estimates
#   fixed-grip thermal strain/stress for the epilogue copper wire.
#
# Options (environment or flags):
#   --target-t T     evaluation temperature (default 300 K)
#   --delta-t DT     temperature rise for ε_th = α ΔT (default 90 K, Handshake 2)
#   --E GPa          Young's modulus for σ_th = E α ΔT (default 120)
#   --handbook A     handbook α in 1/K for comparison (default 17e-6)
#   --compare PCT    fail if |α - handbook|/handbook > PCT percent (default 15)
#   --no-write       skip writing alpha_cu_*K.dat archive (CI / fixture-safe)
#
# Emits alpha_export.yaml for archiving beside cu.phonon/ and FEM decks.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"
TARGET_T="${TARGET_T:-300}"
DELTA_T="${DELTA_T:-90}"
E_GPA="${E_GPA:-120}"
HANDBOOK="${HANDBOOK:-17e-6}"
COMPARE_PCT="${COMPARE_PCT:-15}"
NO_WRITE=0

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --target-t) TARGET_T="$2"; shift 2 ;;
    --delta-t) DELTA_T="$2"; shift 2 ;;
    --E) E_GPA="$2"; shift 2 ;;
    --handbook) HANDBOOK="$2"; shift 2 ;;
    --compare) COMPARE_PCT="$2"; shift 2 ;;
    --no-write) NO_WRITE=1; shift ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

resolve_input() {
  if [[ -z "$INPUT" ]]; then
    if [[ -f "cu.phonon/a_vs_T.dat" ]]; then
      echo "cu.phonon/a_vs_T.dat"
    elif [[ -f "$ROOT/fixtures/cu.foundation/cu.phonon/a_vs_T.dat" ]]; then
      echo "$ROOT/fixtures/cu.foundation/cu.phonon/a_vs_T.dat"
    else
      echo "FAIL: provide phonon_dir or a_vs_T.dat" >&2
      exit 1
    fi
  elif [[ -d "$INPUT" ]]; then
    [[ -f "$INPUT/a_vs_T.dat" ]] || { echo "FAIL: missing $INPUT/a_vs_T.dat" >&2; exit 1; }
    echo "$INPUT/a_vs_T.dat"
  elif [[ -f "$INPUT" ]]; then
    echo "$INPUT"
  else
    echo "FAIL: not found: $INPUT" >&2
    exit 1
  fi
}

AVST="$(resolve_input)"
PHONON_DIR="$(dirname "$AVST")"

# Parse T, a pairs (skip comments and blanks)
mapfile -t ROWS < <(awk '!/^#/ && NF >= 2 { print $1, $2 }' "$AVST")
[[ ${#ROWS[@]} -ge 2 ]] || { echo "FAIL: need at least two temperature rows in $AVST" >&2; exit 1; }

# Find bracketing indices for central difference at TARGET_T
T_LOW="" T_MID="" T_HIGH="" A_LOW="" A_MID="" A_HIGH=""
IDX_MID=-1

for i in "${!ROWS[@]}"; do
  read -r t a <<< "${ROWS[$i]}"
  if awk -v t="$t" -v tgt="$TARGET_T" 'BEGIN { exit !(t == tgt) }'; then
    IDX_MID=$i
    T_MID="$t"
    A_MID="$a"
  fi
done

# Central difference: prefer (T_{i-1}, T_{i+1}) around target, else nearest pair
if [[ "$IDX_MID" -ge 0 ]]; then
  if [[ "$IDX_MID" -gt 0 && "$IDX_MID" -lt $((${#ROWS[@]} - 1)) ]]; then
    read -r T_LOW A_LOW <<< "${ROWS[$((IDX_MID - 1))]}"
    read -r T_HIGH A_HIGH <<< "${ROWS[$((IDX_MID + 1))]}"
    A_REF="$A_MID"
  elif [[ "$IDX_MID" -eq 0 ]]; then
    read -r T_MID A_MID <<< "${ROWS[0]}"
    read -r T_HIGH A_HIGH <<< "${ROWS[1]}"
    T_LOW="$T_MID"
    A_LOW="$A_MID"
    A_REF="$A_MID"
  else
    read -r T_LOW A_LOW <<< "${ROWS[$((IDX_MID - 1))]}"
    read -r T_MID A_MID <<< "${ROWS[$IDX_MID]}"
    T_HIGH="$T_MID"
    A_HIGH="$A_MID"
    A_REF="$A_MID"
  fi
else
  # Target not in table: use two closest points for local slope
  read -r T_LOW A_LOW <<< "${ROWS[0]}"
  read -r T_HIGH A_HIGH <<< "${ROWS[1]}"
  for i in "${!ROWS[@]}"; do
    read -r t a <<< "${ROWS[$i]}"
    if awk -v t="$t" -v tgt="$TARGET_T" 'BEGIN { exit !(t <= tgt) }'; then
      T_LOW="$t"
      A_LOW="$a"
    fi
    if awk -v t="$t" -v tgt="$TARGET_T" 'BEGIN { exit !(t >= tgt) }'; then
      T_HIGH="$t"
      A_HIGH="$a"
      break
    fi
  done
  A_REF=$(awk -v tl="$T_LOW" -v th="$T_HIGH" -v al="$A_LOW" -v ah="$A_HIGH" -v tgt="$TARGET_T" \
    'BEGIN { if (th == tl) print al; else print al + (ah - al) * (tgt - tl) / (th - tl) }')
fi

DADT=$(awk -v tl="$T_LOW" -v th="$T_HIGH" -v al="$A_LOW" -v ah="$A_HIGH" \
  'BEGIN { if (th == tl) { print "FAIL"; exit 1 } else printf "%.12e", (ah - al) / (th - tl) }')
ALPHA=$(awk -v a="$A_REF" -v dadt="$DADT" 'BEGIN { printf "%.12e", dadt / a }')
ALPHA_PPM=$(awk -v a="$ALPHA" 'BEGIN { printf "%.2f", a * 1e6 }')

EPS_TH=$(awk -v a="$ALPHA" -v dt="$DELTA_T" 'BEGIN { printf "%.12e", a * dt }')
SIGMA_TH=$(awk -v e="$E_GPA" -v eps="$EPS_TH" 'BEGIN { printf "%.2f", e * 1e9 * eps / 1e6 }')

HANDBOOK_DIFF_PCT=$(awk -v a="$ALPHA" -v h="$HANDBOOK" \
  'BEGIN { if (h == 0) print "NA"; else printf "%.2f", 100 * (a - h) / h }')

DISP_OK="skipped"
if [[ -f "$PHONON_DIR/dispersion.dat" ]]; then
  GAMMA_LA=$(awk '!/^#/ && NF >= 2 && $1 == 0.000 { print $2; exit }' "$PHONON_DIR/dispersion.dat")
  if [[ -n "$GAMMA_LA" ]]; then
    if awk -v w="$GAMMA_LA" 'BEGIN { exit !(w >= 0 && w < 1.0) }'; then
      DISP_OK="yes"
    else
      DISP_OK="no"
      echo "FAIL: acoustic branch at Gamma not zero: omega=$GAMMA_LA cm-1" >&2
      exit 1
    fi
  fi
fi

echo "# parse_alpha.sh  Handshake 3 — thermal expansion from quasiharmonic a(T)"
echo "# Input: $AVST"
echo "# Target T = ${TARGET_T} K; ΔT = ${DELTA_T} K (Handshake 2); E = ${E_GPA} GPa"
echo ""
echo "alpha_1_per_K = ${ALPHA}"
echo "alpha_ppm = ${ALPHA_PPM}"
echo "a_at_target_angstrom = ${A_REF}"
echo "da_dT_angstrom_per_K = ${DADT}"
echo "epsilon_thermal = ${EPS_TH}"
echo "sigma_thermal_fixed_grip_MPa = ${SIGMA_TH}"
echo "handbook_alpha_1_per_K = ${HANDBOOK}"
echo "handbook_diff_pct = ${HANDBOOK_DIFF_PCT}"
echo "gamma_acoustic_ok = ${DISP_OK}"
echo ""

cat <<YAML
# alpha_export.yaml (archive beside cu.phonon/ and FEM *EXPANSION card)
handshake: 3  # Thermal strain → mechanical stiffness
material: Cu
source:
  a_vs_T: ${AVST}
  phonon_directory: ${PHONON_DIR}
target_temperature_K: ${TARGET_T}
results:
  alpha_1_per_K: ${ALPHA}
  alpha_ppm: ${ALPHA_PPM}
  lattice_parameter_angstrom: ${A_REF}
  delta_T_K: ${DELTA_T}
  epsilon_thermal: ${EPS_TH}
  sigma_thermal_fixed_grip_MPa: ${SIGMA_TH}
  handbook_alpha_1_per_K: ${HANDBOOK}
  handbook_diff_pct: ${HANDBOOK_DIFF_PCT}
  gamma_acoustic_ok: ${DISP_OK}
parser: parse_alpha.sh
YAML

# Write canonical archive file beside phonon data when directory is writable
OUT_ALPHA="${PHONON_DIR}/alpha_cu_${TARGET_T}K.dat"
if [[ "$NO_WRITE" -eq 0 && -w "$PHONON_DIR" ]]; then
  cat > "$OUT_ALPHA" <<EOF
# alpha_cu_${TARGET_T}K.dat — generated by parse_alpha.sh
# source: $(basename "$AVST")
alpha_1_per_K ${ALPHA}
alpha_ppm ${ALPHA_PPM}
T_K ${TARGET_T}
delta_T_K ${DELTA_T}
handbook_diff_pct ${HANDBOOK_DIFF_PCT}
EOF
  echo ""
  echo "Wrote ${OUT_ALPHA}"
fi

awk -v diff="$HANDBOOK_DIFF_PCT" -v pct="$COMPARE_PCT" 'BEGIN {
  if (diff == "NA") exit 0
  v = diff; if (v < 0) v = -v
  if (v > pct) { printf "FAIL: |alpha - handbook|/handbook = %.2f%% exceeds %s%%\n", diff, pct > "/dev/stderr"; exit 1 }
}'

echo ""
echo "PASS: alpha export complete (Handshake 3)."
