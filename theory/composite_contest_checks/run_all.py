"""Run lemmas, search, decisions, classical-direction control, and optional Crossref."""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _write(name: str, text: str) -> None:
    (HERE / name).write_text(text, encoding="utf-8", newline="\n")


def main(argv: list[str]) -> int:
    sys.path.insert(0, str(HERE))
    from lemmas import run_lemmas
    from search import run_search
    from decide import classical_control, run_grid

    lemma_txt = run_lemmas()
    _write("lemmas.out", lemma_txt)
    if "ALL LEMMAS PASS" not in lemma_txt:
        print(lemma_txt)
        return 1
    search = run_search()
    # JSON-ish stable text, not a raw dict (arrays of correlators stay out of the byte file
    # except through the losses the decision uses).
    env_txt = "\n".join(f"{M} {L:.16e}" for M, L in search["envelope"]) + "\n"
    _write("envelope.txt", env_txt)
    grid_txt, _rows = run_grid(search)
    _write("decisions.out", grid_txt)
    ctrl = classical_control()
    _write("control.out", ctrl)
    if "--with-crossref" in argv:
        from crossref_check import run as run_crossref

        _write("crossref.out", run_crossref())
    files = ["lemmas.out", "envelope.txt", "decisions.out", "control.out"]
    if (HERE / "crossref.out").exists():
        files.append("crossref.out")
    lines = []
    for name in files:
        digest = hashlib.sha256((HERE / name).read_bytes()).hexdigest()
        lines.append(f"{digest}  {name}")
    _write("SHA256SUMS", "\n".join(lines) + "\n")
    print(lemma_txt, end="")
    print(grid_txt, end="")
    print(ctrl, end="")
    print("WROTE", ", ".join(files))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
