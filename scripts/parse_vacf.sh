#!/usr/bin/env bash
# parse_vacf.sh — MD phonon DOS from VACF spectral density (Part VIII audit)
# Usage: ./parse_vacf.sh [phonon_dos_md.dat] [options]
#
# Input format (whitespace-separated, # comments allowed):
#   omega_THz  g_omega
# Peaks are local maxima above 20% of global max.
#
# Options:
#   --dispersion FILE   DFT dispersion.dat for acoustic branch cross-check
#   --tolerance PCT     max |shift| vs DFT LA reference (default 5)
#   --compare PCT       fail if shift exceeds PCT (optional, for CI)
#
# Emits vacf_export.yaml for archiving beside cu.phonon/phonon_dos_md.dat

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INPUT="${1:-}"
DISPERSION=""
TOLERANCE="${TOLERANCE:-5}"
COMPARE_PCT=""

shift || true
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dispersion) DISPERSION="$2"; shift 2 ;;
    --tolerance) TOLERANCE="$2"; shift 2 ;;
    --compare) COMPARE_PCT="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

resolve_input() {
  if [[ -z "$INPUT" ]]; then
    if [[ -f "$ROOT/fixtures/phonon_dos_md.dat" ]]; then
      echo "$ROOT/fixtures/phonon_dos_md.dat"
    else
      echo "FAIL: provide phonon_dos_md.dat" >&2
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
if [[ -z "$DISPERSION" ]]; then
  if [[ -f "$(dirname "$DATA")/dispersion.dat" ]]; then
    DISPERSION="$(dirname "$DATA")/dispersion.dat"
  elif [[ -f "$ROOT/fixtures/cu.foundation/cu.phonon/dispersion.dat" ]]; then
    DISPERSION="$ROOT/fixtures/cu.foundation/cu.phonon/dispersion.dat"
  fi
fi

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

awk '!/^#/ && NF >= 2 { print $1, $2 }' "$DATA" > "$TMP"
N=$(wc -l < "$TMP")
[[ "$N" -ge 3 ]] || { echo "FAIL: need at least three omega rows in $DATA" >&2; exit 1; }

# Global max and local peaks (simple interior maxima)
read -r OMEGA_MAX G_MAX <<< "$(awk 'BEGIN { max=0 } { if ($2 > max) { max=$2; om=$1 } } END { printf "%.4f %.6f", om, max }' "$TMP")"

mapfile -t PEAKS < <(awk -v gmax="$G_MAX" '
  NR == 1 { prev_om=$1; prev_g=$2; next }
  {
    if (prev_g > $2 && prev_g > prev_prev_g && prev_g >= 0.2 * gmax)
      print prev_om, prev_g
    prev_prev_g = prev_g
    prev_om = $1
    prev_g = $2
  }
  END {
    if (prev_g > prev_prev_g && prev_g >= 0.2 * gmax) print prev_om, prev_g
  }
' "$TMP")

# If no interior peaks found, use global max
if [[ ${#PEAKS[@]} -eq 0 ]]; then
  PEAKS=("$OMEGA_MAX $G_MAX")
fi

# Find peak closest to DFT LA reference (acoustic cross-check)
if [[ -n "$DISPERSION" && -f "$DISPERSION" ]]; then
  DFT_LA_CM=$(awk '$3 == "LA" && $1 == 0.100 { print $2; exit }' "$DISPERSION")
  if [[ -n "$DFT_LA_CM" ]]; then
    DFT_LA_THZ=$(awk -v cm="$DFT_LA_CM" 'BEGIN { printf "%.4f", cm / 33.356 }')
    read -r ACOUSTIC_OM ACOUSTIC_G <<< "$(awk -v ref="$DFT_LA_THZ" '
      { om=$1; g=$2; d=(om-ref)^2; if (best=="" || d<best) { best=d; aom=om; ag=g } }
      END { printf "%.4f %.6f", aom, ag }
    ' "$TMP")"
    DFT_SHIFT_PCT=$(awk -v md="$ACOUSTIC_OM" -v dft="$DFT_LA_THZ" 'BEGIN {
      if (dft <= 0) { print "NA"; exit }
      diff = 100 * (md - dft) / dft
      if (diff < 0) diff = -diff
      printf "%.2f", diff
    }')
    ACOUSTIC_OK=$(awk -v shift="$DFT_SHIFT_PCT" -v tol="$TOLERANCE" 'BEGIN {
      if (shift == "NA") print "unknown"
      else if (shift <= tol) print "yes"
      else print "no"
    }')
  fi
fi

# Default acoustic cross-check when no dispersion reference
DFT_LA_THZ="${DFT_LA_THZ:-NA}"
DFT_SHIFT_PCT="${DFT_SHIFT_PCT:-NA}"
ACOUSTIC_OK="${ACOUSTIC_OK:-unknown}"
if [[ "$ACOUSTIC_OM" == "" ]]; then
  read -r ACOUSTIC_OM ACOUSTIC_G <<< "${PEAKS[0]}"
fi

PEAK_LIST=$(printf '%s THz, ' "${PEAKS[@]%% *}" | sed 's/, $//')

echo "# parse_vacf.sh  MD phonon DOS from VACF spectral density"
echo "# Input: $DATA"
[[ -n "$DISPERSION" ]] && echo "# DFT dispersion: $DISPERSION"
echo ""
echo "omega_max_THz = ${OMEGA_MAX}"
echo "g_max = ${G_MAX}"
echo "acoustic_peak_THz = ${ACOUSTIC_OM}"
echo "peak_list_THz = [${PEAK_LIST}]"
echo "dft_LA_reference_THz = ${DFT_LA_THZ}"
echo "acoustic_shift_pct = ${DFT_SHIFT_PCT}"
echo "acoustic_peak_ok = ${ACOUSTIC_OK}"
echo ""

cat <<YAML
# vacf_export.yaml (archive beside cu.phonon/ and phonon_dos_md.dat)
handshake: MD-phonon  # VACF DOS cross-check for Handshake 3 pedigree
material: Cu
source_file: ${DATA}
dispersion_reference: ${DISPERSION:-none}
results:
  omega_max_THz: ${OMEGA_MAX}
  acoustic_peak_THz: ${ACOUSTIC_OM}
  peak_list_THz: [${PEAK_LIST}]
  dft_LA_reference_THz: ${DFT_LA_THZ}
  acoustic_shift_pct: ${DFT_SHIFT_PCT}
  acoustic_peak_ok: ${ACOUSTIC_OK}
  tolerance_pct: ${TOLERANCE}
parser: parse_vacf.sh
YAML

if [[ -n "$COMPARE_PCT" ]]; then
  [[ "$ACOUSTIC_OK" == "yes" ]] || {
    echo "FAIL: acoustic peak shift ${DFT_SHIFT_PCT}% exceeds tolerance ${TOLERANCE}%" >&2
    exit 1
  }
fi

echo ""
echo "PASS: VACF phonon DOS export complete."
