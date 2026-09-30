#!/usr/bin/env bash
# parse_elastic.sh — extract C11, C44, C12 from six Quantum ESPRESSO strain runs
# Usage: ./parse_elastic.sh [delta]   (default delta = 0.005)
# Expects cu_C11_eps_{p,m}.out, cu_C44_shear_{p,m}.out, cu_C12_tet_{p,m}.out

set -euo pipefail
DELTA="${1:-0.005}"
KBAR_TO_GPA=0.1

stress_component() {
  local file="$1" idx="$2"   # idx: 1=xx, 2=yy, 3=zz, 4=yz, 5=xz, 6=xy
  grep -A 3 "total   stress" "$file" | tail -3 | awk -v i="$idx" '
    NR==1 { s1=$i }
    NR==2 { s2=$i }
    NR==3 { s3=$i }
    END { print (s1+s2+s3)/3 }'
}

parse_run() {
  local file="$1"
  grep -q "convergence has been achieved" "$file" || { echo "FAIL: $file" >&2; exit 1; }
}

for f in cu_C11_eps_p.out cu_C11_eps_m.out cu_C44_shear_p.out cu_C44_shear_m.out \
         cu_C12_tet_p.out cu_C12_tet_m.out; do
  [[ -f "$f" ]] || { echo "Missing $f" >&2; exit 1; }
  parse_run "$f"
done

s11_p=$(stress_component cu_C11_eps_p.out 1)
s11_m=$(stress_component cu_C11_eps_m.out 1)
sxy_p=$(stress_component cu_C44_shear_p.out 6)
sxy_m=$(stress_component cu_C44_shear_m.out 6)
st11_p=$(stress_component cu_C12_tet_p.out 1)
st11_m=$(stress_component cu_C12_tet_m.out 1)

C11=$(awk -v sp="$s11_p" -v sm="$s11_m" -v d="$DELTA" -v k="$KBAR_TO_GPA" \
  'BEGIN { printf "%.2f", k * (sp - sm) / (2*d) }')
C44=$(awk -v sp="$sxy_p" -v sm="$sxy_m" -v d="$DELTA" -v k="$KBAR_TO_GPA" \
  'BEGIN { printf "%.2f", k * (sp - sm) / (2*d) }')
C12=$(awk -v c11="$C11" -v sp="$st11_p" -v sm="$st11_m" -v d="$DELTA" -v k="$KBAR_TO_GPA" \
  'BEGIN { printf "%.2f", c11 - k * (sp - sm) / (2*d) }')

echo "# parse_elastic.sh  delta=$DELTA"
echo "C11_GPa = $C11"
echo "C12_GPa = $C12"
echo "C44_GPa = $C44"
echo "B_GPa   = $(awk -v c11="$C11" -v c12="$C12" 'BEGIN { printf "%.2f", (c11 + 2*c12)/3 }')"
echo "G_GPa   = $(awk -v c11="$C11" -v c12="$C12" -v c44="$C44" 'BEGIN { printf "%.2f", (c11 - c12 + 3*c44)/5 }')"
