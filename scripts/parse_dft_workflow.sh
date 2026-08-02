#!/usr/bin/env bash
# parse_dft_workflow.sh — audit Part IX foundation folder (Act VI) for epilogue Handshake 1
# Usage: ./parse_dft_workflow.sh [foundation_dir] [--check-only]
#
# Expects a study folder (e.g. cu.foundation/) with:
#   README.md          metadata (functional, pseudo, QE version)
#   cu.relax.out       optional — vc-relax log with converged forces
#   cu.elastic/        optional — six strain pw.x outputs for parse_elastic.sh
#   cu.phonon/         optional — phonon dispersion archive
#   cu.gsf/            optional — stacking-fault slab calculations
#
# Emits foundation_export.yaml for epilogue multiscale handshakes.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIR="${1:-cu.foundation}"
CHECK_ONLY=0

if [[ "${2:-}" == "--check-only" || "${1:-}" == "--check-only" ]]; then
  CHECK_ONLY=1
  [[ "${1:-}" == "--check-only" ]] && DIR="cu.foundation"
fi

[[ -d "$DIR" ]] || { echo "FAIL: missing foundation directory: $DIR" >&2; exit 1; }

MISSING=()
OPTIONAL_MISSING=()

[[ -f "$DIR/README.md" ]] || MISSING+=("README.md")

for opt in cu.relax.out cu.phonon cu.gsf; do
  [[ -e "$DIR/$opt" ]] || OPTIONAL_MISSING+=("$opt")
done

ELASTIC_OK=0
if [[ -d "$DIR/cu.elastic" ]]; then
  ELASTIC_OK=1
  for f in cu_C11_eps_p.out cu_C11_eps_m.out cu_C44_shear_p.out cu_C44_shear_m.out \
           cu_C12_tet_p.out cu_C12_tet_m.out; do
    [[ -f "$DIR/cu.elastic/$f" ]] || { ELASTIC_OK=0; MISSING+=("cu.elastic/$f"); }
  done
else
  OPTIONAL_MISSING+=("cu.elastic/")
fi

if [[ ${#MISSING[@]} -gt 0 ]]; then
  echo "FAIL: required items missing in $DIR:" >&2
  printf '  - %s\n' "${MISSING[@]}" >&2
  exit 1
fi

echo "# parse_dft_workflow.sh  foundation=$DIR"
echo "# Part IX Act VI audit — epilogue Handshake 1"
echo ""

if [[ ${#OPTIONAL_MISSING[@]} -gt 0 ]]; then
  echo "# optional (not yet archived):"
  printf '#   - %s\n' "${OPTIONAL_MISSING[@]}"
  echo ""
fi

C11="NA" C12="NA" C44="NA" B="NA" G="NA" E="NA" NU="NA"

if [[ "$ELASTIC_OK" -eq 1 ]]; then
  echo "# Running parse_elastic.sh on cu.elastic/"
  (
    cd "$DIR/cu.elastic"
    "$ROOT/scripts/parse_elastic.sh"
  ) | tee /tmp/parse_elastic_out.txt
  C11=$(grep 'C11_GPa' /tmp/parse_elastic_out.txt | awk '{print $3}')
  C12=$(grep 'C12_GPa' /tmp/parse_elastic_out.txt | awk '{print $3}')
  C44=$(grep 'C44_GPa' /tmp/parse_elastic_out.txt | awk '{print $3}')
  B=$(grep 'B_GPa' /tmp/parse_elastic_out.txt | awk '{print $3}')
  G=$(grep 'G_GPa' /tmp/parse_elastic_out.txt | awk '{print $3}')
  E=$(awk -v b="$B" -v g="$G" 'BEGIN {
    if (b == "NA" || g == "NA") print "NA"; else printf "%.1f", 9*b*g/(3*b+g)
  }')
  NU=$(awk -v b="$B" -v g="$G" 'BEGIN {
    if (b == "NA" || g == "NA") print "NA"; else printf "%.3f", (3*b-2*g)/(2*(3*b+g))
  }')
  echo ""
fi

RELAX_OK="no"
if [[ -f "$DIR/cu.relax.out" ]]; then
  grep -q "convergence has been achieved" "$DIR/cu.relax.out" && RELAX_OK="yes"
fi

ALPHA="NA" ALPHA_PPM="NA" SIGMA_TH="NA"
PHONON_OK=0
if [[ -f "$DIR/cu.phonon/a_vs_T.dat" ]]; then
  PHONON_OK=1
  echo "# Running parse_alpha.sh on cu.phonon/"
  (
    "$ROOT/scripts/parse_alpha.sh" "$DIR/cu.phonon" --target-t 300 --delta-t 90 --E "${E:-120}" --compare 15
  ) | tee /tmp/parse_alpha_out.txt
  ALPHA=$(grep '^alpha_1_per_K = ' /tmp/parse_alpha_out.txt | awk '{print $3}')
  ALPHA_PPM=$(grep '^alpha_ppm = ' /tmp/parse_alpha_out.txt | awk '{print $3}')
  SIGMA_TH=$(grep '^sigma_thermal_fixed_grip_MPa = ' /tmp/parse_alpha_out.txt | awk '{print $3}')
  echo ""
fi

echo "foundation_audit:"
echo "  directory: $DIR"
echo "  readme_present: yes"
echo "  relax_converged: $RELAX_OK"
echo "  elastic_complete: $([ "$ELASTIC_OK" -eq 1 ] && echo yes || echo no)"
echo "  phonon_archived: $([ -d "$DIR/cu.phonon" ] && echo yes || echo no)"
echo "  gsf_archived: $([ -d "$DIR/cu.gsf" ] && echo yes || echo no)"
echo ""

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  echo "PASS: foundation folder structure OK (--check-only)."
  exit 0
fi

cat <<YAML
# foundation_export.yaml (archive beside epilogue handshake table)
material: Cu
source_directory: ${DIR}
handshake: 1  # DFT → continuum elastic constants
functional: see README.md
elastic_constants_GPa:
  C11: ${C11}
  C12: ${C12}
  C44: ${C44}
  bulk_modulus: ${B}
  shear_modulus: ${G}
voigt_isotropic:
  youngs_modulus_GPa: ${E}
  poissons_ratio: ${NU}
thermal_expansion:
  alpha_1_per_K: ${ALPHA}
  alpha_ppm: ${ALPHA_PPM}
  sigma_thermal_fixed_grip_MPa: ${SIGMA_TH}
  handshake: 3
  parser_alpha: parse_alpha.sh
relaxation_converged: ${RELAX_OK}
phonon_quasiharmonic: $([ "$PHONON_OK" -eq 1 ] && echo yes || echo no)
parser_elastic: parse_elastic.sh
parser_workflow: parse_dft_workflow.sh
YAML

echo ""
echo "PASS: foundation audit complete. Archive foundation_export.yaml with cu.elastic/ and README.md."
