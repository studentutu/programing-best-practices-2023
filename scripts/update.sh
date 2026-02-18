#!/usr/bin/env bash
# update.sh — Refresh best-practices resources and reinstall the Kiro skill.
#
# Usage:
#   ./scripts/update.sh                  # Update all resources
#   ./scripts/update.sh --category ruby  # Update a specific category only
#   ./scripts/update.sh --limit 20       # Quick test with 20 resources
#   ./scripts/update.sh --skip-crawl     # Regenerate CSVs + reinstall only

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# ── Parse args ────────────────────────────────────────────────────────────────
CRAWL_ARGS=""
SKIP_CRAWL=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --category|-c) CRAWL_ARGS="$CRAWL_ARGS --category $2"; shift 2 ;;
    --limit|-l)    CRAWL_ARGS="$CRAWL_ARGS --limit $2";    shift 2 ;;
    --skip-crawl)  SKIP_CRAWL=true; shift ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# ── Helpers ───────────────────────────────────────────────────────────────────
step() { echo; echo "▶ $*"; }
ok()   { echo "  ✓ $*"; }
fail() { echo "  ✗ $*"; exit 1; }

# ── Check Python ──────────────────────────────────────────────────────────────
PYTHON=$(command -v python3 || command -v python || true)
[[ -z "$PYTHON" ]] && fail "Python not found. Install Python 3 first."

echo "════════════════════════════════════════════════"
echo "  Best Practices — Update & Reinstall"
echo "════════════════════════════════════════════════"

# ── Step 1: Install crawler deps ──────────────────────────────────────────────
if [[ "$SKIP_CRAWL" == false ]]; then
  step "Installing crawler dependencies..."
  "$PYTHON" -m pip install -r "$SCRIPT_DIR/crawler/requirements.txt" -q \
    && ok "Dependencies ready" \
    || fail "pip install failed"

  # ── Step 2: Crawl ─────────────────────────────────────────────────────────
  step "Crawling resources... ($( [[ -n "$CRAWL_ARGS" ]] && echo "$CRAWL_ARGS" || echo "all" ))"
  "$PYTHON" "$SCRIPT_DIR/crawler/crawl.py" --update $CRAWL_ARGS \
    && ok "Crawl complete" \
    || fail "Crawl failed"
else
  step "Skipping crawl (--skip-crawl)"
fi

# ── Step 3: Reinstall skill (regenerates CSVs + copies to .kiro/steering) ────
step "Reinstalling Kiro skill..."
"$PYTHON" "$SCRIPT_DIR/install-skill.py" "$ROOT_DIR" --mode kiro --skip-crawl --force \
  && ok "Skill reinstalled at .kiro/steering/best-practices/" \
  || fail "Skill install failed"

echo
echo "════════════════════════════════════════════════"
echo "  Done! Resources are up to date."
echo "════════════════════════════════════════════════"
