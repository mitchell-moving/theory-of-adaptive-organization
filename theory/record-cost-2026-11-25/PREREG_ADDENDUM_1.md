# Addendum 1 to the record-cost preregistration

*Wednesday 25 November 2026 (America/New_York). Written after `PREREG.md` was locked (its sha256 is in `PREREG.sha256`, and `PREREG.md` is not edited). Nothing here changes Definition D or the rules R1–R3. No new computation was made between the lock and this addendum; the scripts were rerun only to reproduce the session's outputs, which match.*

## A. Wording

In `PREREG.md`, "law" (as in "finite law" and "joint law") means a probability distribution, the sense of "finite-law" at `CORE.md:52`. It is not the theory's word. New text in this folder and in `theory/RECORD_COST_CHAIN_2026-11-25.md` says "distribution".

## B. A further reason from A6 (does not change D)

On a classical memory, where A6 is unambiguous, the per-record sum already differs from A6's mutual information. Let \(X_0, X_1\) be fair independent bits and let the memory hold \(M=X_0\oplus X_1\). Then \(I(X_0X_1;M)=1\) bit, while \(I(X_0;M)=I(X_1;M)=0\), so the per-record sum is 0. For independent records the per-record sum is never larger than the total on a classical memory, and it can be strictly smaller. So the per-record reading is not an extension of A6 to general probabilistic theories; it disagrees with A6 on A6's own domain. Its supremum over encodings agrees with the capacity \(\log N\) wherever information causality holds, which is why the two readings coincide as capacities there and differ as costs of a given design.

## C. A qualification of "D equals the capacity price"

`PREREG.md` says that on the encodings used, D equals the capacity price \(\log_2 N\), citing the composition route's round 2. That identification was checked there for the gbit memory (one bit) and is stated for the other memories on the strength of their encodings reaching capacity. It is not re-proved here. The table in `PREREG.md` uses the capacity prices as computed by `scripts/composition/t6_pricing_additivity.py` and `scripts/composition/t5_bipartite_drift.py`.
