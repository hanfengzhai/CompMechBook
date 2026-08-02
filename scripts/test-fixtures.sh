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

echo ""
echo "PASS: all fixture tests succeeded."
