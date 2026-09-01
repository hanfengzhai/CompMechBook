#!/usr/bin/env bash
# parse_gsf.sh — extract GSF energies from metadynamics or DFT sweep data
# Usage: ./parse_gsf.sh [input.dat] [--fault-area Å²]
#
# Input format: whitespace-separated columns
#   s  F_eV  [optional: gamma_mJ_m2]
# where s is normalized shear displacement (0 = perfect, 1 = stable fault)
#
# Output: tabulated γ_sf, γ_USF, and OpenDiS-ready yaml snippet

set -euo pipefail

INPUT="${1:-gsf_metadynamics_cu111.dat}"
FAULT_AREA="${2:-}"
EV_TO_MJM2=1602.18  # (eV/Å²) → (mJ/m²) when divided by area in Å²

if [[ ! -f "$INPUT" ]]; then
  echo "Usage: $0 <gsf_data.dat> [--fault-area Å²]" >&2
  echo "  Expected columns: s  F_eV  [gamma_mJ_m2]" >&2
  exit 1
fi

# Parse optional --fault-area flag
if [[ "${2:-}" == "--fault-area" && -n "${3:-}" ]]; then
  FAULT_AREA="$3"
fi

# Default fault area for Cu {111}: a0²√3/2 with a0 ≈ 3.615 Å
if [[ -z "$FAULT_AREA" ]]; then
  FAULT_AREA=$(awk 'BEGIN { a0=3.615; printf "%.4f", a0*a0*sqrt(3)/2 }')
  echo "# Using default Cu {111} fault area: ${FAULT_AREA} Å²" >&2
fi

TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT

# Skip comment lines; require at least two columns
grep -v '^#' "$INPUT" | grep -v '^[[:space:]]*$' > "$TMP"
N=$(wc -l < "$TMP")
if [[ "$N" -lt 3 ]]; then
  echo "FAIL: need at least 3 data points in $INPUT" >&2
  exit 1
fi

# Compute gamma if not provided in third column
awk -v area="$FAULT_AREA" -v conv="$EV_TO_MJM2" '
  NF >= 2 {
    s = $1; F = $2
    g = (NF >= 3) ? $3 : (F / area) * conv
    print s, F, g
  }
' "$TMP" > "${TMP}.gamma"

# Find stable fault minimum (s near 1.0) and USF maximum (s near 0.5)
read -r S_SF GAMMA_SF <<< "$(awk '
  $1 >= 0.8 && $1 <= 1.2 { if (min == "" || $3 < min) { min=$3; s=$1 } }
  END { if (min != "") print s, min; else print "NA NA" }
' "${TMP}.gamma")"

read -r S_USF GAMMA_USF <<< "$(awk '
  $1 >= 0.3 && $1 <= 0.7 { if (max == "" || $3 > max) { max=$3; s=$1 } }
  END { if (max != "") print s, max; else print "NA NA" }
' "${TMP}.gamma")"

# Reference at s=0
read -r S0 GAMMA0 <<< "$(awk '
  { d = ($1)^2; if (best == "" || d < best) { best=d; s=$1; g=$3 } }
  END { print s, g }
' "${TMP}.gamma")"

echo "# parse_gsf.sh  input=$INPUT  fault_area=${FAULT_AREA} Å²"
echo "# points: $N"
echo ""
echo "gamma_sf_mJ_m2   = ${GAMMA_SF}"
echo "gamma_usf_mJ_m2  = ${GAMMA_USF}"
echo "s_stable_fault   = ${S_SF}"
echo "s_unstable_fault = ${S_USF}"
echo "gamma_ref_mJ_m2  = ${GAMMA0}"
echo ""

if [[ "$GAMMA_SF" == "NA" || "$GAMMA_USF" == "NA" ]]; then
  echo "WARN: could not locate stable fault minimum or USF maximum — check s range" >&2
fi

# Partial separation estimate: d = mu * bp^2 / (2*pi*gamma*(1-nu))  [Hirth & Lothe]
read -r D_NM <<< "$(awk -v gsf="$GAMMA_SF" '
  BEGIN {
    if (gsf == "NA" || gsf <= 0) { print "NA"; exit }
    mu = 48e9; nu = 0.34; bp = 1.47e-10; gsf_SI = gsf * 1e-3
    d = mu * bp * bp / (2 * 3.14159265 * gsf_SI * (1 - nu))
    printf "%.2f", d * 1e9
  }
')"
echo "partial_separation_nm = ${D_NM}"
echo ""

cat <<YAML
# gsf_export.yaml (paste into OpenDiS / DAMASK handoff folder)
material: Cu
surface: "{111}"
source_file: ${INPUT}
fault_area_A2: ${FAULT_AREA}
gamma_sf_mJ_m2: ${GAMMA_SF}
gamma_usf_mJ_m2: ${GAMMA_USF}
partial_separation_nm: ${D_NM}
s_stable: ${S_SF}
s_unstable: ${S_USF}
YAML
