# LOCK_ERRATA: hash locks that do not verify as the tree stands

*Tuesday 24 November 2026 (America/New_York). Checked by [`tools/verify_locks.py`](../tools/verify_locks.py), which runs inside `tools/check_consistency.py`. No locked file is edited by this page or by that script, and git history is not rewritten.*

A lock is a `*.sha256`, `SHA256SUMS*` or `LOCK*.txt` file made before a result was computed. On `main` at `c341c5e` there are 222 lock lines: **163 verify**, **17 do not match** and **42 name files that are not in the repository**. This page accounts for the 17 and the 42. A plain `sha256sum -c` shows the 17 as mismatches, which looks like editing after the lock. For 13 of them the cause is one commit that changed only box paths. The other 4 and the 42 are described plainly below.

## 1. Scrub only: 13 files, proved

The public-readiness scrub `d513528` (18 November 2026, "tree only") replaced box paths in these files: `<local>` stands for `/workspace` and `<repo>` for `/workspace/theory-of-adaptive-organization`. Reversing exactly that substitution in memory gives back the locked sha256 for all 13 (`python3 tools/verify_locks.py` does this on every run). The original bytes also sit in git history at the commit in the last column.

| file | lock file | locked sha256 (first 16) | current sha256 (first 16) | locked bytes in history |
|---|---|---|---|---|
| `prereg/WIKIDATA-BAND/PREREG.md` | `prereg/WIKIDATA-BAND/LOCK.txt` | `068528225b72d5ad` | `64627432b4b12d0d` | `7cffd93` |
| `prereg/vigil-ona/ona_analyze.py` | `prereg/vigil-ona/LOCK.txt` | `3328161ccbe0b7e7` | `b5cb4b6ca1754035` | `52a624a` |
| `tests/C3b/PREREG_ADDENDUM_A2.md` | `tests/C3b/PREREG.sha256` | `42deb7bca4bf04af` | `6064d4ee311c5cf8` | `54ae2ce` |
| `tests/C3b/PREREG_ADDENDUM_A3.md` | `tests/C3b/PREREG.sha256` | `5a3384e52ba4561c` | `c8a18dc13fd0e890` | `bf8a4a3` |
| `tests/DECISIVE/banks/PREREG.md` | `tests/DECISIVE/banks/PREREG.sha256` | `b7ea310e30d4afe4` | `af9294797fa321dd` | `54ae2ce` |
| `tests/F1/code/analyze.py` | `tests/F1/PREREG.sha256` | `55ac2d8d01609076` | `0ba5193988c35e3b` | `54ae2ce` |
| `tests/F1/code/analyze_E.py` | `tests/F1/PREREG.sha256` | `4a77b3c80a4bd8f2` | `971bd3ea01e78fbf` | `54ae2ce` |
| `tests/F1/code/build_dataset.py` | `tests/F1/PREREG.sha256` | `89f8e84e137aa961` | `96912e652825b6d6` | `54ae2ce` |
| `tests/F1/code/covid.py` | `tests/F1/PREREG.sha256` | `3b494ee3017b179a` | `736409743dc82011` | `54ae2ce` |
| `tests/F1/code/extract.py` | `tests/F1/PREREG.sha256` | `b0a40771db2ee2b7` | `1ba5d70aeefc9684` | `54ae2ce` |
| `tests/F1/code/measures.py` | `tests/F1/PREREG.sha256` | `296a2e25e181bdca` | `0843c9bbf0880dfd` | `54ae2ce` |
| `tests/F1/code/power.py` | `tests/F1/PREREG.sha256` | `5684cd5d1e0bb66d` | `df68b55bc22a7d57` | `54ae2ce` |
| `tests/F1/code/sim_dataset.py` | `tests/F1/PREREG.sha256` | `a7c462befcb4c82e` | `5358e7b264bff655` | `54ae2ce` |

## 2. Changed after the lock: 2 files, declared

| file | locked version | later version | declaration |
|---|---|---|---|
| `night2/GITHUB/code/pull.py` | commit `86aa1cc`, blob `44563ed7`, lock hash `a6c218e0…` | commit `d9152f2`, blob `ee4f718e` (current) | The commit message reads "post-lock I/O fix (declared): pull.py waits for rate-limit reset instead of giving up; analysis code unchanged", and the file marks the lines "POST-LOCK I/O FIX (declared)". The diff changes `tries` from 4 to 40 and the rate-limit wait. |
| `theory/layers_checks/stores.py` | commit `e50e92f`, blob `c7c1e06b`, lock hash `df6b7039…` (listed in `tests/EVO1/PREREG_EVO.sha256`) | commit `a1a98aa`, blob `71a113e0` (current) | PR #116, "v2.8-htindex". The function `mse_given_b` gained a numerical guard (21 lines added, 6 removed); the commit text calls it a "store-optimizer fix + regression test". The change is not marked as post-lock in the file or in the commit message. Which EVO1 results ran on which version is not recorded here. |

`verify_locks.py` confirms, when git history is present, that the committed version at the locked commit hashes to the lock.

## 3. No committed version matches: 2 files, unverifiable

| file | lock hash | committed versions | finding |
|---|---|---|---|
| `tests/DECISIVE/glucose/code/analyze.py` | `8822a118…` | one, `54ae2ce` (blob `1c9a5051`) | Neither it nor its reverse substitution hashes to the lock. The locked bytes were not committed. |
| `tests/F1/code/outcome.py` | `35640274…` | two, `54ae2ce` (blob `7f4876fe`) and `d513528` (blob `3126c5e0`) | Neither version, with or without the reverse substitution, hashes to the lock. The locked bytes were not committed. |

For these two the lock cannot be checked from this repository, so nothing here says whether the file was edited after the lock. A result that depends on either file keeps the label it already has, with this limit added.

## 4. Raw data never committed: 42 lock lines

These lock hashes of external data files (downloads, API pulls). The data are not in the repository, so the hashes cannot be checked here.

| lock file | lines |
|---|---|
| `prereg/vigil-ona/SHA256SUMS_raw.txt` | 30 |
| `night2/GITHUB/data/SHA256SUMS` | 5 |
| `prereg/WIKIDATA-BAND/data/SHA256SUMS` | 2 |
| `theory/measured/ecoli/LOCK.txt` | 2 |
| `prereg/SENSE-CELL/data/SHA256SUMS` | 1 |
| `tests/F1/raw/companyfacts.sha256` | 1 |
| `tests/F1/raw/submissions.sha256` | 1 |

## What the counts mean

- 13 of 17 mismatches are explained exactly. 2 more are declared edits with the locked version in history. 2 cannot be checked. 42 lock lines point at data that is not here.
- The locks are real: they were committed before the results they protect, and the original blobs are in the public history except for the two in section 3.
- `tools/verify_locks.py` pins these counts (163 or more OK, 13, 2, 2, 42 and the seven lock files above). It also pins the **current git blob** of the three files that no lock covers and whose lock does not verify: `theory/layers_checks/stores.py` (`71a113e0`), `tests/F1/code/outcome.py` (`3126c5e0`) and `tests/DECISIVE/glucose/code/analyze.py` (`1c9a5051`). A later edit to any of the three fails. The later git blob of each post-lock file is always checked, including when this clone has no lock-time history: `night2/GITHUB/code/pull.py` is pinned at `ee4f718e`, and `theory/layers_checks/stores.py` at `71a113e0`. The 13 scrub-only files are protected by the reverse-substitution proof. A new lock that does not verify, a pinned file that starts to verify, a change in the 42, or an edit to a pinned file fails `tools/check_consistency.py` until this page and the script are updated together.

## Which locks the script reads

It reads only lock lines of the form `<64 hex>  <path>` in `*.sha256`, `SHA256SUMS*` and `LOCK*.txt` files: 222 lines. It does **not** read two other kinds, so "every lock" here means every such line, not every lock in the repository:
- six lock files whose lines are a bare hash with no path: `core/bridge_2026-11-21/PREDICTIONS.sha256`, `core/bridge_2026-11-21/PREREG.sha256`, `core/sim1_2026-11-21/PREDICTIONS.sha256`, `core/sim1_2026-11-21/PREREG.sha256`, `core/sim1_2026-11-21/RUN_SIM1.sha256` and `core/sim1_2026-11-21/SIM1_LIB.sha256` (a reviewer checked that each hash matches one tracked file);
- prose locks written as `sha256: …` inside a text file, for example `core/sim1_2026-11-21/LOCK.txt`.

## Not done, on purpose

No locked file was restored, re-hashed or edited, and no lock file was rewritten. Restoring the box paths would change the public tree; re-hashing would replace a lock with a new one. A reviewer who wants the original bytes can take them from the commits above.
