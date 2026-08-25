#!/usr/bin/env bash
# Run parse scripts against fixtures/ (CI smoke test).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

echo "=== test-fixtures.sh ==="

echo "--- parse_gsf.sh ---"
./scripts/parse_gsf.sh fixtures/gsf_cu111.dat > "$TMP" 2>&1
grep -q 'gamma_sf_mJ_m2' "$TMP"

echo "--- parse_wham.sh ---"
./scripts/parse_wham.sh fixtures/wham_histogram.dat --target 380 \
  --compare fixtures/wham_histogram_long.dat > "$TMP" 2>&1
grep -q 'wham_converged_5pct=yes' "$TMP"

echo "--- parse_elastic.sh (fixtures/cu.elastic) ---"
(
  cd fixtures/cu.elastic
  "$ROOT/scripts/parse_elastic.sh"
) > "$TMP" 2>&1
grep -q 'C11_GPa' "$TMP"

echo "--- parse_cht.sh (Handshake 2) ---"
./scripts/parse_cht.sh fixtures/cht_wire.conf > "$TMP" 2>&1
grep -q 'cht_export.yaml' "$TMP"
grep -q 'fixed_point_converged = yes' "$TMP"

echo "--- parse_alpha.sh (Handshake 3) ---"
./scripts/parse_alpha.sh fixtures/cu.foundation/cu.phonon --target-t 300 --delta-t 90 --compare 15 --no-write > "$TMP" 2>&1
grep -q 'alpha_export.yaml' "$TMP"
grep -q 'gamma_acoustic_ok = yes' "$TMP"
grep -q 'PASS: alpha export complete' "$TMP"

echo "--- parse_dft_workflow.sh ---"
./scripts/parse_dft_workflow.sh fixtures/cu.foundation --check-only
./scripts/parse_dft_workflow.sh fixtures/cu.foundation > "$TMP" 2>&1
grep -q 'foundation_export.yaml' "$TMP"
grep -q 'relax_converged: yes' "$TMP"
grep -q 'gsf_archived: yes' "$TMP"
grep -q 'gamma_sf_mJ_m2: 45.0' "$TMP"
grep -q 'md_phonon_dos:' "$TMP"
grep -q 'acoustic_peak_ok: yes' "$TMP"
grep -q 'phonon_lifetime:' "$TMP"
grep -q 'LA_lifetime_ps: 15.4' "$TMP"
grep -q 'ddd_rate_extrapolation:' "$TMP"
grep -q 'rate_sensitivity_m: 0.022' "$TMP"
grep -q 'tau_flow_extrapolated_MPa: 33.20' "$TMP"
grep -q 'temperature_sweep: yes' "$TMP"
grep -q 'ln_tau_vs_T_slope: -0.002' "$TMP"
grep -q 'temperature_pedigree:' "$TMP"
grep -q 'T_w_source: default_300K' "$TMP"

echo "--- parse_lifetime.sh (MD phonon lifetime) ---"
./scripts/parse_lifetime.sh fixtures/cu.foundation/cu.phonon/phonon_lifetime.dat \
  --compare 5 --expected 15.4 > "$TMP" 2>&1
grep -q 'lifetime_export.yaml' "$TMP"
grep -q 'lifetime_primary_ps = 15.4' "$TMP"
grep -q 'PASS: phonon lifetime export complete' "$TMP"

echo "--- parse_lifetime.sh (temperature sweep, interpolated T_w) ---"
./scripts/parse_lifetime.sh fixtures/cu.foundation/cu.phonon/phonon_lifetime_vs_T.dat \
  --target-t 311.4831 --compare 5 --expected 14.94 > "$TMP" 2>&1
grep -q 'sweep_mode = yes' "$TMP"
grep -q 'interpolation = interpolated' "$TMP"
grep -q 'lifetime_primary_ps = 14.940676' "$TMP"
grep -q 'PASS: phonon lifetime export complete' "$TMP"

echo "--- parse_lifetime.sh (temperature sweep, exact node) ---"
./scripts/parse_lifetime.sh fixtures/cu.foundation/cu.phonon/phonon_lifetime_vs_T.dat \
  --target-t 380 --compare 5 --expected 12.2 > "$TMP" 2>&1
grep -q 'sweep_mode = yes' "$TMP"
grep -q 'interpolation = exact' "$TMP"
grep -q 'lifetime_primary_ps = 12.2' "$TMP"
grep -q 'ln_tau_vs_T_slope = -0.002' "$TMP"
grep -q 'PASS: phonon lifetime export complete' "$TMP"

echo "--- parse_rate.sh (Handshake 4a) ---"
./scripts/parse_rate.sh fixtures/ddd_tau_vs_rate.dat --lab-rate 1e-3 \
  --compare 2 --expected 33.21 > "$TMP" 2>&1
grep -q 'rate_export.yaml' "$TMP"
grep -q 'rate_sensitivity_m = 0.02200' "$TMP"
grep -q 'PASS: rate export complete' "$TMP"

echo "--- parse_vacf.sh (MD phonon DOS) ---"
./scripts/parse_vacf.sh fixtures/phonon_dos_md.dat --compare 5 > "$TMP" 2>&1
grep -q 'vacf_export.yaml' "$TMP"
grep -q 'acoustic_peak_ok = yes' "$TMP"
grep -q 'PASS: VACF phonon DOS export complete' "$TMP"

echo "--- parse_fe2.sh (Handshake 4b) ---"
./scripts/parse_fe2.sh fixtures/fe2_notch_comparison.dat --compare 1 --expected 10.70 > "$TMP" 2>&1
grep -q 'fe2_export.yaml' "$TMP"
grep -q 'fe2_enrichment_required = yes' "$TMP"
grep -q 'PASS: FE² export complete' "$TMP"

echo "--- parse_multiscale_workflow.sh (full chain) ---"
./scripts/parse_multiscale_workflow.sh fixtures/cu.foundation fixtures/cht_wire.conf > "$TMP" 2>&1
grep -q 'multiscale_export.yaml' "$TMP"
grep -q 'handshake_2_cht:' "$TMP"
grep -q 'T_wall_K: 311.4831' "$TMP"
grep -q 'delta_T_from_handshake_2: 11.48' "$TMP"
grep -q 'LA_lifetime_ps: 14.940676' "$TMP"
grep -q 'target_T_K: 311.4831' "$TMP"
grep -q 'interpolation: interpolated' "$TMP"
grep -q 'tau_flow_extrapolated_MPa: 33.2043' "$TMP"
grep -q 'fe2_enrichment_required: yes' "$TMP"
grep -q 'PASS: multiscale workflow complete' "$TMP"

echo ""
echo "PASS: all fixture tests succeeded."
