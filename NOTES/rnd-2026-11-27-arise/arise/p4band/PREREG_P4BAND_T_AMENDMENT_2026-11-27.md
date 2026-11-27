# P4-BAND-T amendment (before any analysis was seen)

*Friday 27 November 2026 (EST). Amends PREREG_P4BAND_T_2026-11-27.md (SHA-256 e2b3e3e7ae129cd37937aa35b8e2e49a576da3cc28fbcb1b47da4105766cea88). Append-only; the prereg is not changed.*

- The locked supply_test.py (f01b2e1f…) ran all 120 simulations and saved them to supply_runs.json (SHA-256 42897836471b644db2fe62494a03cf594e797899a5078b65f0252bd849a05484) before it crashed on a leftover no-op loop (NameError: `mu` undefined, line 22; supply_test.out SHA-256 af689db1aa42cf277e61cf4004ffc33cc0be53d6eeb68f9e96560045112d5cf8). No edge, shift or test was printed, so no result was seen.
- Fix: supply_analysis.py (SHA-256 4d44f2785348d18e88e4deeeda6d8fc6767082467be2488ad70a2ff64022f96e) is supply_test.py with exactly two changes (diff in this note's WORKLOG line): the no-op loop is removed, and the runs are loaded from supply_runs.json instead of recomputed. The edge rule, bootstrap, thresholds and predictions are unchanged. The simulations are deterministic per seed, so recomputing would give the same numbers.
