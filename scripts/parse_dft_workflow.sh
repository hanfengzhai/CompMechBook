#!/usr/bin/env bash
# parse_dft_workflow.sh — audit Part IX foundation folder (Act VI) for epilogue Handshake 1
# Usage: ./parse_dft_workflow.sh [foundation_dir] [--check-only]
#
# Expects a study folder (e.g. cu.foundation/) with:
#   README.md          metadata (functional, pseudo, QE version)
#   cu.relax.out       optional — vc-relax log with converged forces
#   cu.elastic/        optional — six strain pw.x outputs for parse_elastic.sh
#   cu.phonon/         optional — phonon dispersion archive
#                      optional — phonon_dos_md.dat (VACF cross-check via parse_vacf.sh)
#                      optional — phonon_lifetime.dat (LA linewidth via parse_lifetime.sh)
#   cu.gsf/            optional — stacking-fault slab calculations
#   ddd_tau_vs_rate.dat optional — OpenDiS rate sweep (Handshake 4a via parse_rate.sh)
#   cu.ddd/ddd_tau_vs_rate.dat  optional — same, nested layout
#
# Emits foundation_export.yaml for epilogue multiscale handshakes.
# When DDD rate data is archived, Handshake 4a fields merge into the same yaml.

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

LIFETIME_OK=0
LA_LIFETIME="NA" LA_LINEWIDTH="NA" LA_LIFETIME_SRC="none"
LIFETIME_INPUT=""
LIFETIME_SWEEP=0
LIFETIME_T_LIST="NA" LIFETIME_DRAG_SLOPE="NA"
if [[ -f "$DIR/cu.phonon/phonon_lifetime_vs_T.dat" ]]; then
  LIFETIME_INPUT="$DIR/cu.phonon/phonon_lifetime_vs_T.dat"
  LIFETIME_SWEEP=1
elif [[ -f "$DIR/cu.phonon/phonon_lifetime.dat" ]]; then
  LIFETIME_INPUT="$DIR/cu.phonon/phonon_lifetime.dat"
elif [[ -f "$DIR/phonon_lifetime.dat" ]]; then
  LIFETIME_INPUT="$DIR/phonon_lifetime.dat"
fi
if [[ -n "$LIFETIME_INPUT" ]]; then
  LIFETIME_OK=1
  echo "# Running parse_lifetime.sh on $(basename "$LIFETIME_INPUT")"
  (
    "$ROOT/scripts/parse_lifetime.sh" "$LIFETIME_INPUT" --target-t 300
  ) | tee /tmp/parse_lifetime_out.txt
  LA_LIFETIME=$(grep '^lifetime_primary_ps = ' /tmp/parse_lifetime_out.txt | awk '{print $3}')
  LA_LINEWIDTH=$(grep '^linewidth_primary_GHz = ' /tmp/parse_lifetime_out.txt | awk '{print $3}')
  LA_LIFETIME_SRC=$(grep '^source_primary = ' /tmp/parse_lifetime_out.txt | awk '{print $3}')
  if grep -q '^sweep_mode = yes' /tmp/parse_lifetime_out.txt; then
    LIFETIME_SWEEP=1
    LIFETIME_T_LIST=$(grep '^temperature_list_K = ' /tmp/parse_lifetime_out.txt | sed 's/temperature_list_K = //')
    LIFETIME_DRAG_SLOPE=$(grep '^ln_tau_vs_T_slope = ' /tmp/parse_lifetime_out.txt | awk '{print $3}')
  fi
  echo ""
fi

VACF_OK=0
ACOUSTIC_PEAK="NA" ACOUSTIC_SHIFT="NA" ACOUSTIC_OK="unknown"
VACF_INPUT=""
if [[ -f "$DIR/cu.phonon/phonon_dos_md.dat" ]]; then
  VACF_INPUT="$DIR/cu.phonon/phonon_dos_md.dat"
elif [[ -f "$DIR/phonon_dos_md.dat" ]]; then
  VACF_INPUT="$DIR/phonon_dos_md.dat"
fi
if [[ -n "$VACF_INPUT" ]]; then
  VACF_OK=1
  echo "# Running parse_vacf.sh on phonon_dos_md.dat"
  DISP_ARG=()
  [[ -f "$DIR/cu.phonon/dispersion.dat" ]] && DISP_ARG=(--dispersion "$DIR/cu.phonon/dispersion.dat")
  (
    "$ROOT/scripts/parse_vacf.sh" "$VACF_INPUT" "${DISP_ARG[@]}"
  ) | tee /tmp/parse_vacf_out.txt
  ACOUSTIC_PEAK=$(grep '^acoustic_peak_THz = ' /tmp/parse_vacf_out.txt | awk '{print $3}')
  ACOUSTIC_SHIFT=$(grep '^acoustic_shift_pct = ' /tmp/parse_vacf_out.txt | awk '{print $3}')
  ACOUSTIC_OK=$(grep '^acoustic_peak_ok = ' /tmp/parse_vacf_out.txt | awk '{print $3}')
  echo ""
fi

GAMMA_SF="NA" GAMMA_USF="NA" PARTIAL_SEP="NA"
GSF_OK=0
GSF_INPUT=""
if [[ -f "$DIR/cu.gsf/gsf_cu111.dat" ]]; then
  GSF_INPUT="$DIR/cu.gsf/gsf_cu111.dat"
elif [[ -f "$DIR/cu.gsf/gsf.dat" ]]; then
  GSF_INPUT="$DIR/cu.gsf/gsf.dat"
fi
if [[ -n "$GSF_INPUT" ]]; then
  GSF_OK=1
  echo "# Running parse_gsf.sh on cu.gsf/"
  (
    "$ROOT/scripts/parse_gsf.sh" "$GSF_INPUT"
  ) | tee /tmp/parse_gsf_out.txt
  GAMMA_SF=$(grep '^gamma_sf_mJ_m2   = ' /tmp/parse_gsf_out.txt | awk '{print $3}')
  GAMMA_USF=$(grep '^gamma_usf_mJ_m2  = ' /tmp/parse_gsf_out.txt | awk '{print $3}')
  PARTIAL_SEP=$(grep '^partial_separation_nm = ' /tmp/parse_gsf_out.txt | awk '{print $3}')
  echo ""
fi

RATE_OK=0
RATE_M="NA" RATE_TAU_LAB="NA" RATE_TAU_REF="NA" RATE_OVERPRED="NA" RATE_SIGMA_LAB="NA"
RATE_INPUT=""
if [[ -f "$DIR/ddd_tau_vs_rate.dat" ]]; then
  RATE_INPUT="$DIR/ddd_tau_vs_rate.dat"
elif [[ -f "$DIR/cu.ddd/ddd_tau_vs_rate.dat" ]]; then
  RATE_INPUT="$DIR/cu.ddd/ddd_tau_vs_rate.dat"
fi
if [[ -n "$RATE_INPUT" ]]; then
  RATE_OK=1
  echo "# Running parse_rate.sh on ddd_tau_vs_rate.dat (Handshake 4a)"
  (
    "$ROOT/scripts/parse_rate.sh" "$RATE_INPUT" --lab-rate 1e-3
  ) | tee /tmp/parse_rate_out.txt
  RATE_M=$(grep '^rate_sensitivity_m = ' /tmp/parse_rate_out.txt | awk '{print $3}')
  RATE_TAU_LAB=$(grep '^tau_flow_extrapolated_MPa = ' /tmp/parse_rate_out.txt | awk '{print $3}')
  RATE_TAU_REF=$(grep '^tau_flow_DDD_at_1e3_s-1_MPa = ' /tmp/parse_rate_out.txt | awk '{print $3}')
  RATE_OVERPRED=$(grep '^direct_import_overprediction_pct = ' /tmp/parse_rate_out.txt | awk '{print $3}')
  RATE_SIGMA_LAB=$(grep '^sigma_y_extrapolated_MPa = ' /tmp/parse_rate_out.txt | awk '{print $3}')
  echo ""
fi

echo "foundation_audit:"
echo "  directory: $DIR"
echo "  readme_present: yes"
echo "  relax_converged: $RELAX_OK"
echo "  elastic_complete: $([ "$ELASTIC_OK" -eq 1 ] && echo yes || echo no)"
echo "  phonon_archived: $([ -d "$DIR/cu.phonon" ] && echo yes || echo no)"
echo "  vacf_dos_archived: $([ "$VACF_OK" -eq 1 ] && echo yes || echo no)"
echo "  phonon_lifetime_archived: $([ "$LIFETIME_OK" -eq 1 ] && echo yes || echo no)"
echo "  ddd_rate_archived: $([ "$RATE_OK" -eq 1 ] && echo yes || echo no)"
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
stacking_fault:
  gamma_sf_mJ_m2: ${GAMMA_SF}
  gamma_usf_mJ_m2: ${GAMMA_USF}
  partial_separation_nm: ${PARTIAL_SEP}
  handshake: 4
  parser_gsf: parse_gsf.sh
  source_file: ${GSF_INPUT:-none}
relaxation_converged: ${RELAX_OK}
phonon_quasiharmonic: $([ "$PHONON_OK" -eq 1 ] && echo yes || echo no)
md_phonon_dos:
  acoustic_peak_THz: ${ACOUSTIC_PEAK}
  acoustic_shift_pct: ${ACOUSTIC_SHIFT}
  acoustic_peak_ok: ${ACOUSTIC_OK}
  handshake: MD-phonon
  parser_vacf: parse_vacf.sh
  source_file: ${VACF_INPUT:-none}
phonon_lifetime:
  LA_lifetime_ps: ${LA_LIFETIME}
  LA_linewidth_GHz: ${LA_LINEWIDTH}
  source: ${LA_LIFETIME_SRC}
  temperature_sweep: $([ "$LIFETIME_SWEEP" -eq 1 ] && echo yes || echo no)
  temperature_list_K: ${LIFETIME_T_LIST}
  ln_tau_vs_T_slope: ${LIFETIME_DRAG_SLOPE}
  handshake: MD-phonon-lifetime
  parser_lifetime: parse_lifetime.sh
  source_file: ${LIFETIME_INPUT:-none}
ddd_rate_extrapolation:
  archived: $([ "$RATE_OK" -eq 1 ] && echo yes || echo no)
  rate_sensitivity_m: ${RATE_M}
  tau_flow_extrapolated_MPa: ${RATE_TAU_LAB}
  tau_flow_DDD_at_1e3_s-1_MPa: ${RATE_TAU_REF}
  sigma_y_extrapolated_MPa: ${RATE_SIGMA_LAB}
  direct_import_overprediction_pct: ${RATE_OVERPRED}
  handshake: 4a
  parser_rate: parse_rate.sh
  source_file: ${RATE_INPUT:-none}
gsf_archived: $([ "$GSF_OK" -eq 1 ] && echo yes || echo no)
parser_elastic: parse_elastic.sh
parser_workflow: parse_dft_workflow.sh
YAML

echo ""
echo "PASS: foundation audit complete. Archive foundation_export.yaml with cu.elastic/ and README.md."
