"""Recheck the DOIs named in theory/composite-contest-2026-11-24/PREREG.md section 11."""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request

DOIS = [
    "10.1088/1367-2630/15/5/053040",
    "10.1088/1367-2630/13/6/063001",
    "10.1103/PhysRevA.84.012311",
    "10.1007/s10701-011-9616-6",
    "10.1007/s10701-014-9777-1",
    "10.1103/PhysRevLett.102.020505",
    "10.1103/PhysRevA.87.052106",
    "10.1007/s10701-010-9488-1",
    "10.1038/s41586-021-04160-4",
    "10.1103/PhysRevA.75.032304",
    "10.1103/PhysRevLett.104.080402",
    "10.1007/BF00417500",
    "10.1007/BF02058098",
    "10.1016/j.shpsb.2003.12.001",
    "10.1103/PhysRevA.77.022104",
]


def fetch(doi: str) -> str:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    req = urllib.request.Request(url, headers={"User-Agent": "gtao-composite-contest/0.1"})
    with urllib.request.urlopen(req, timeout=40) as resp:
        msg = json.load(resp)["message"]
    title = (msg.get("title") or [""])[0].replace("\n", " ")
    authors = " ".join(a.get("family", "") for a in msg.get("author", [])[:4])
    year = msg.get("issued", {}).get("date-parts", [[None]])[0][0]
    cont = (msg.get("container-title") or [""])[0]
    return f"OK {doi} | {year} | {authors} | {cont} | {title}"


def run() -> str:
    lines = []
    fails = 0
    for i, doi in enumerate(DOIS):
        if i:
            time.sleep(0.4)
        try:
            lines.append(fetch(doi))
        except Exception as exc:  # network or parse
            fails += 1
            lines.append(f"FAIL {doi} | {type(exc).__name__}")
    lines.append(f"FAILS {fails}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(run(), end="")
