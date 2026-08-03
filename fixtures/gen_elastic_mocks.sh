#!/usr/bin/env bash
# Generate minimal Quantum ESPRESSO mock outputs for parse_elastic.sh fixture tests.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/fixtures/cu.elastic"
mkdir -p "$OUT"

write_mock() {
  local name="$1" s11="$2" s22="$3" s33="$4" s23="$5" s13="$6" s12="$7"
  cat > "$OUT/${name}.out" <<EOF
     Program PWSCF v.7.2 starts on ...

     convergence has been achieved

          total   stress (kbar)                   xxx                   yyy                   zzz
  ${s11}  ${s22}  ${s33}  ${s23}  ${s13}  ${s12}
  ${s11}  ${s22}  ${s33}  ${s23}  ${s13}  ${s12}
  ${s11}  ${s22}  ${s33}  ${s23}  ${s13}  ${s12}
EOF
}

# Target: C11≈168, C12≈122, C44≈75 GPa at delta=0.005
write_mock cu_C11_eps_p   8.40  0.00  0.00  0.00  0.00  0.00
write_mock cu_C11_eps_m  -8.40  0.00  0.00  0.00  0.00  0.00
write_mock cu_C44_shear_p 0.00 0.00 0.00 0.00 0.00  3.75
write_mock cu_C44_shear_m 0.00 0.00 0.00 0.00 0.00 -3.75
write_mock cu_C12_tet_p   2.30  0.00  0.00  0.00  0.00  0.00
write_mock cu_C12_tet_m  -2.30  0.00  0.00  0.00  0.00  0.00

echo "Wrote mock QE outputs to $OUT"
