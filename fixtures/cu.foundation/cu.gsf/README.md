# Cu {111} generalized stacking fault (illustrative fixture)

Illustrative GSF curve for `parse_gsf.sh` and `parse_dft_workflow.sh` smoke tests.
Not from a production DFT slab run — values match the Part VII / epilogue Handshake 4
literature anchor (\(\gamma_{\text{sf}} \approx 45\,\text{mJ/m}^2\) at the stable fault).

Run:

```bash
./scripts/parse_gsf.sh fixtures/cu.foundation/cu.gsf/gsf_cu111.dat
./scripts/parse_dft_workflow.sh fixtures/cu.foundation
```

Archive beside `cu.elastic/` and `cu.phonon/` in a real Part IX foundation folder.
