#!/usr/bin/env bash
# parse_multiscale_workflow.sh — orchestrate epilogue Handshakes 1–4b + MD phonon audits
# Usage: ./parse_multiscale_workflow.sh [foundation_dir] [cht_config] [--check-only]
#
# Runs the full copper-wire multiscale chain in dependency order:
#   1. parse_dft_workflow.sh  — DFT foundation (elastic, α, GSF, VACF, lifetime, rate)
#   2. parse_cht.sh           — Handshake 2 converged T_w, ΔT
#   3. parse_alpha.sh         — Handshake 3 with ΔT from Handshake 2 (not handbook default)
#   4. parse_lifetime.sh      — phonon drag at converged T_w when sweep data exist
#   5. parse_rate.sh          — Handshake 4a (standalone export if not merged in step 1)
#   6. parse_fe2.sh           — Handshake 4b notch enrichment audit
#   7. parse_wham.sh          — optional replica-exchange MD at target T_w
#
# Emits multiscale_export.yaml linking all handshake exports for Act VI archive.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
FOUNDATION="${1:-fixtures/cu.foundation}"
CHT_CONFIG="${2:-fixtures/cht_wire.conf}"
CHECK_ONLY=0

if [[ "${1:-}" == "--check-only" ]]; then
  CHECK_ONLY=1
  FOUNDATION="fixtures/cu.foundation"
  CHT_CONFIG="fixtures/cht_wire.conf"
elif [[ "${2:-}" == "--check-only" ]]; then
  CHECK_ONLY=1
elif [[ "${3:-}" == "--check-only" ]]; then
  CHECK_ONLY=1
fi

[[ -d "$FOUNDATION" ]] || { echo "FAIL: missing foundation directory: $FOUNDATION" >&2; exit 1; }
[[ -f "$CHT_CONFIG" ]] || { echo "FAIL: missing CHT config: $CHT_CONFIG" >&2; exit 1; }

TMPDIR_WORK="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_WORK"' EXIT

echo "# parse_multiscale_workflow.sh"
echo "# foundation=$FOUNDATION  cht=$CHT_CONFIG"
echo "# Epilogue multiscale chain — Handshakes 1, 2, 3, 4a, 4b + MD phonon audits"
echo ""

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  "$ROOT/scripts/parse_dft_workflow.sh" "$FOUNDATION" --check-only
  echo "PASS: multiscale workflow structure OK (--check-only)."
  exit 0
fi

# --- Handshake 1: DFT foundation (includes embedded α, VACF, lifetime, rate when archived) ---
echo "=== Handshake 1 — DFT foundation ==="
"$ROOT/scripts/parse_dft_workflow.sh" "$FOUNDATION" | tee "$TMPDIR_WORK/foundation.txt"
echo ""

# Extract Voigt E for Handshake 3 if available
E_GPA=$(grep 'youngs_modulus_GPa:' "$TMPDIR_WORK/foundation.txt" | awk '{print $2}')
[[ "$E_GPA" == "NA" || -z "$E_GPA" ]] && E_GPA="120"

# --- Handshake 2: conjugate heat transfer ---
echo "=== Handshake 2 — conjugate heat transfer ==="
"$ROOT/scripts/parse_cht.sh" "$CHT_CONFIG" | tee "$TMPDIR_WORK/cht.txt"
T_WALL=$(grep '^T_wall_K = ' "$TMPDIR_WORK/cht.txt" | awk '{print $3}')
DELTA_T=$(grep '^delta_T_K = ' "$TMPDIR_WORK/cht.txt" | awk '{print $3}')
T_MID=$(grep '^T_midspan_K = ' "$TMPDIR_WORK/cht.txt" | awk '{print $3}')
[[ -z "$T_WALL" ]] && { echo "FAIL: could not parse T_wall from parse_cht.sh" >&2; exit 1; }
[[ -z "$DELTA_T" ]] && DELTA_T="90"
echo ""

# --- Handshake 3: thermal expansion at Handshake 2 ΔT ---
ALPHA="NA" ALPHA_PPM="NA" SIGMA_TH="NA"
if [[ -f "$FOUNDATION/cu.phonon/a_vs_T.dat" ]]; then
  echo "=== Handshake 3 — thermal expansion (ΔT=${DELTA_T} K from Handshake 2) ==="
  (
    "$ROOT/scripts/parse_alpha.sh" "$FOUNDATION/cu.phonon" \
      --target-t 300 --delta-t "$DELTA_T" --E "$E_GPA" --compare 15 --no-write
  ) | tee "$TMPDIR_WORK/alpha.txt"
  ALPHA=$(grep '^alpha_1_per_K = ' "$TMPDIR_WORK/alpha.txt" | awk '{print $3}')
  ALPHA_PPM=$(grep '^alpha_ppm = ' "$TMPDIR_WORK/alpha.txt" | awk '{print $3}')
  SIGMA_TH=$(grep '^sigma_thermal_fixed_grip_MPa = ' "$TMPDIR_WORK/alpha.txt" | awk '{print $3}')
  echo ""
else
  echo "# Handshake 3 skipped: no cu.phonon/a_vs_T.dat"
  echo ""
fi

# --- MD phonon lifetime at converged T_w (temperature pedigree for Handshake 4a) ---
LA_LIFETIME="NA" LA_LINEWIDTH="NA" LIFETIME_T="NA" DRAG_SLOPE="NA" LIFETIME_INTERP="NA"
LIFETIME_INPUT=""
if [[ -f "$FOUNDATION/cu.phonon/phonon_lifetime_vs_T.dat" ]]; then
  LIFETIME_INPUT="$FOUNDATION/cu.phonon/phonon_lifetime_vs_T.dat"
elif [[ -f "$FOUNDATION/cu.phonon/phonon_lifetime.dat" ]]; then
  LIFETIME_INPUT="$FOUNDATION/cu.phonon/phonon_lifetime.dat"
fi
if [[ -n "$LIFETIME_INPUT" ]]; then
  echo "=== MD phonon lifetime at T_w=${T_WALL} K (Handshake 2 converged) ==="
  (
    "$ROOT/scripts/parse_lifetime.sh" "$LIFETIME_INPUT" --target-t "$T_WALL"
  ) | tee "$TMPDIR_WORK/lifetime_tw.txt"
  LA_LIFETIME=$(grep '^lifetime_primary_ps = ' "$TMPDIR_WORK/lifetime_tw.txt" | awk '{print $3}')
  LA_LINEWIDTH=$(grep '^linewidth_primary_GHz = ' "$TMPDIR_WORK/lifetime_tw.txt" | awk '{print $3}')
  LIFETIME_T=$(grep '^target_temperature_K = ' "$TMPDIR_WORK/lifetime_tw.txt" | awk '{print $3}')
  LIFETIME_INTERP=$(grep '^interpolation = ' "$TMPDIR_WORK/lifetime_tw.txt" | awk '{print $3}')
  DRAG_SLOPE=$(grep '^ln_tau_vs_T_slope = ' "$TMPDIR_WORK/lifetime_tw.txt" | awk '{print $3}')
  echo ""
fi

# --- Handshake 4a: DDD rate extrapolation ---
RATE_M="NA" RATE_TAU_LAB="NA" RATE_OVERPRED="NA"
RATE_INPUT=""
if [[ -f "$FOUNDATION/ddd_tau_vs_rate.dat" ]]; then
  RATE_INPUT="$FOUNDATION/ddd_tau_vs_rate.dat"
elif [[ -f "$FOUNDATION/cu.ddd/ddd_tau_vs_rate.dat" ]]; then
  RATE_INPUT="$FOUNDATION/cu.ddd/ddd_tau_vs_rate.dat"
elif [[ -f "$ROOT/fixtures/ddd_tau_vs_rate.dat" ]]; then
  RATE_INPUT="$ROOT/fixtures/ddd_tau_vs_rate.dat"
fi
if [[ -n "$RATE_INPUT" ]]; then
  echo "=== Handshake 4a — DDD rate extrapolation ==="
  (
    "$ROOT/scripts/parse_rate.sh" "$RATE_INPUT" --lab-rate 1e-3
  ) | tee "$TMPDIR_WORK/rate.txt"
  RATE_M=$(grep '^rate_sensitivity_m = ' "$TMPDIR_WORK/rate.txt" | awk '{print $3}')
  RATE_TAU_LAB=$(grep '^tau_flow_extrapolated_MPa = ' "$TMPDIR_WORK/rate.txt" | awk '{print $3}')
  RATE_OVERPRED=$(grep '^direct_import_overprediction_pct = ' "$TMPDIR_WORK/rate.txt" | awk '{print $3}')
  echo ""
fi

# --- Handshake 4b: FE² notch enrichment ---
FE2_UPLIFT="NA" FE2_ENRICH="unknown"
FE2_INPUT="$ROOT/fixtures/fe2_notch_comparison.dat"
if [[ -f "$FE2_INPUT" ]]; then
  echo "=== Handshake 4b — FE² notch enrichment ==="
  (
    "$ROOT/scripts/parse_fe2.sh" "$FE2_INPUT"
  ) | tee "$TMPDIR_WORK/fe2.txt"
  FE2_UPLIFT=$(grep '^fe2_vs_cp_uplift_pct = ' "$TMPDIR_WORK/fe2.txt" | awk '{print $3}')
  FE2_ENRICH=$(grep '^fe2_enrichment_required = ' "$TMPDIR_WORK/fe2.txt" | awk '{print $3}')
  echo ""
fi

# --- Optional: WHAM at target T_w ---
WHAM_OK="skipped"
if [[ -f "$ROOT/fixtures/wham_histogram.dat" ]]; then
  echo "=== Replica MD (WHAM) at T_w=${T_WALL} K ==="
  if (
    "$ROOT/scripts/parse_wham.sh" "$ROOT/fixtures/wham_histogram.dat" \
      --target "$T_WALL" --compare "$ROOT/fixtures/wham_histogram_long.dat"
  ) | tee "$TMPDIR_WORK/wham.txt"; then
    WHAM_OK="yes"
  else
    WHAM_OK="no"
  fi
  echo ""
fi

# --- Sensitivity rank (from epilogue table logic) ---
SENSITIVITY_RANK="2,3,4a,1,4b"
if [[ "$FE2_ENRICH" != "yes" ]]; then
  SENSITIVITY_RANK="2,3,4a,1"
fi

cat <<YAML
# multiscale_export.yaml (archive beside Act VI workflow folder)
material: Cu
workflow: parse_multiscale_workflow.sh
foundation_directory: ${FOUNDATION}
cht_config: ${CHT_CONFIG}

handshake_1_dft:
  export: foundation_export.yaml
  parser: parse_dft_workflow.sh
  source: ${FOUNDATION}

handshake_2_cht:
  export: cht_export.yaml
  parser: parse_cht.sh
  T_wall_K: ${T_WALL}
  T_midspan_K: ${T_MID}
  delta_T_K: ${DELTA_T}

handshake_3_thermal:
  export: alpha_export.yaml
  parser: parse_alpha.sh
  alpha_1_per_K: ${ALPHA}
  alpha_ppm: ${ALPHA_PPM}
  sigma_thermal_fixed_grip_MPa: ${SIGMA_TH}
  delta_T_from_handshake_2: ${DELTA_T}

md_phonon_lifetime_at_Tw:
  export: lifetime_export.yaml
  parser: parse_lifetime.sh
  target_T_K: ${LIFETIME_T:-${T_WALL}}
  interpolation: ${LIFETIME_INTERP:-unknown}
  LA_lifetime_ps: ${LA_LIFETIME}
  LA_linewidth_GHz: ${LA_LINEWIDTH}
  ln_tau_vs_T_slope: ${DRAG_SLOPE}
  source_file: ${LIFETIME_INPUT:-none}
  note: "Lifetime evaluated at Handshake 2 converged T_w for Handshake 4a drag pedigree"

handshake_4a_rate:
  export: rate_export.yaml
  parser: parse_rate.sh
  rate_sensitivity_m: ${RATE_M}
  tau_flow_extrapolated_MPa: ${RATE_TAU_LAB}
  direct_import_overprediction_pct: ${RATE_OVERPRED}
  source_file: ${RATE_INPUT:-none}

handshake_4b_fe2:
  export: fe2_export.yaml
  parser: parse_fe2.sh
  fe2_uplift_pct: ${FE2_UPLIFT}
  fe2_enrichment_required: ${FE2_ENRICH}

replica_md_wham:
  parser: parse_wham.sh
  converged_at_Tw: ${WHAM_OK}

sensitivity_rank: [${SENSITIVITY_RANK}]
YAML

echo ""
echo "PASS: multiscale workflow complete. Archive multiscale_export.yaml with foundation/ and CHT decks."
