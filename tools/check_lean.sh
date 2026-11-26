#!/usr/bin/env bash
# Build the Lean 4 formalization of the GTAO core (T19).
# Run from the repo root:  tools/check_lean.sh
# Repo rule: run it only in the dedicated checkout /tmp/gtao-lean, never in an
# ordinary clone (the Mathlib cache it unpacks is several GB).
# tools/test_lean.py enforces that.
# Exit 0 = lake build succeeded, no forbidden token occurs in project
#          sources (GTAO.lean, GTAO/*.lean), and the axiom audit
#          (formal/lean/scripts/AxiomAudit.lean) finds that every GTAO
#          declaration depends only on propext, Classical.choice and
#          Quot.sound (so no sorryAx).
# Exit 2 = Lean / lake is not installed.
# Exit 1 = build failed or a forbidden token was found.
#
# The scan is restricted to project sources.  It does not walk `.lake/`
# or `lake-packages/`: after `lake exe cache get`, those trees contain
# thousands of Mathlib files with `sorry` / `axiom` in tests and comments.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEAN_DIR="$ROOT/formal/lean"

if [[ -f "${HOME}/.elan/env" ]]; then
  # shellcheck disable=SC1091
  source "${HOME}/.elan/env"
fi
if [[ -d "${HOME}/.elan/bin" ]]; then
  export PATH="${HOME}/.elan/bin:${PATH}"
fi

if ! command -v lake >/dev/null 2>&1; then
  echo "check_lean.sh: lake/elan not found. Install Lean 4 via elan, then rerun." >&2
  exit 2
fi

# Project sources only.  Prefer an explicit path list so a warm cache
# cannot be grepped even if exclude flags are ignored.
shopt -s nullglob
SOURCES=("$LEAN_DIR/GTAO.lean")
SOURCES+=("$LEAN_DIR/GTAO"/*.lean)
shopt -u nullglob
if [[ ${#SOURCES[@]} -eq 0 || ! -f "$LEAN_DIR/GTAO.lean" ]]; then
  echo "check_lean.sh: no project Lean sources under $LEAN_DIR" >&2
  exit 1
fi

# Whole-token match: sorry, admit, axiom, native_decide, unsafe, implemented_by.
TOKEN_RE='(^|[^A-Za-z_])(sorry|admit|axiom|native_decide|unsafe|implemented_by)([^A-Za-z_]|$)'

scan_sources() {
  if command -v rg >/dev/null 2>&1; then
    # Still exclude the cache dirs if a caller points rg at LEAN_DIR later.
    rg -n --glob '*.lean' -g '!.lake/**' -g '!lake-packages/**' -e "$TOKEN_RE" "${SOURCES[@]}" || true
  else
    grep -n --include='*.lean' -E "$TOKEN_RE" "${SOURCES[@]}" \
      --exclude-dir=.lake --exclude-dir=lake-packages || true
  fi
}

HITS="$(scan_sources)"
if [[ -n "${HITS}" ]]; then
  echo "check_lean.sh: forbidden token (sorry/admit/axiom/native_decide/unsafe/implemented_by) in project sources:" >&2
  echo "${HITS}" >&2
  exit 1
fi

cd "$LEAN_DIR"
echo "check_lean.sh: lake exe cache get"
nice -n 19 lake exe cache get
echo "check_lean.sh: lake build"
nice -n 19 lake build
echo "check_lean.sh: AxiomAudit"
nice -n 19 lake env lean scripts/AxiomAudit.lean
echo "check_lean.sh: OK"
