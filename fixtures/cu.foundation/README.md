# Part IX foundation folder (illustrative audit fixture)
# Run: ./scripts/parse_dft_workflow.sh fixtures/cu.foundation
# Run: ./scripts/parse_cht.sh fixtures/cht_wire.conf  →  archive cht_export.yaml beside this folder

functional: PBE
pseudopotential: Cu.pbe-d-v1.0.uspp.F.UPF
qe_version: fixture
date: 2026-08-02
relaxed_a_angstrom: 3.630
ecutwfc_ry: 60
k_mesh: 12 12 12
notes: Illustrative metadata for parse_dft_workflow.sh --check
gsf_fixture: cu.gsf/gsf_cu111.dat (parse_gsf.sh → Handshake 4)

# T_w column (temperature pedigree — rows 8–9 skill checkpoints)
# Converged wall temperature from Handshake 2 (Joule heating + CHT). Populate from
# parse_cht.sh on fixtures/cht_wire.conf before evaluating alpha(T_w) or tau_ph(T_w).
# Omit until cht_export.yaml exists — phonon tables at 300 K alone leave Act VI partially audited.
T_w_K: null  # set from cht_export.yaml T_wall_K (fixture converges ≈ 379 K)
T_w_source: null  # e.g. parse_cht.sh fixtures/cht_wire.conf
T_w_column_required_for: [alpha_export.yaml, mobility_cu_screw_*K.yaml, phonon_lifetime_at_Tw]
