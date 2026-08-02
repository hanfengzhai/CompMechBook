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
./scripts/parse_alpha.sh fixtures/cu.foundation/cu.phonon --target-t 300 --delta-t 90 --compare 15 > "$TMP" 2>&1
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

echo ""
echo "PASS: all fixture tests succeeded."
