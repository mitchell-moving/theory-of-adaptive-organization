# P4d prereg amendment: syntax fix only, no outputs seen

*Thursday 26 November 2026 (EST). PREREG_P4d_2026-11-26.md (SHA-256 57825b9d…, locked 23:55:14) stands unchanged.*

The first launch failed at import with a SyntaxError in p4d_model.py line 37 (a missing ";" after `series = []`), so nothing was computed. The only change is that the ";" was inserted. Model SHA-256 is now d7b9767c3fbe95f72b269c710c6ba18fe2a9bf60f18bcec060dcbb7161861ff4; p4d_test.py is unchanged (SHA-256 67ae10aa6490ff8bd4a762627af3f27aa04179abcac56d14f4f84c3e85628048). Same seeds. This launch counts as the single run.
