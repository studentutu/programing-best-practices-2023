#!/usr/bin/env bash
# =============================================================================
# setup-kb.sh — Integrate Programming Best Practices into your project
# =============================================================================
#
# Usage (run from your project root):
#   curl -sSL https://raw.githubusercontent.com/dereknguyen269/programing-best-practices/main/scripts/setup-kb.sh | bash
#
#   Or locally:
#   chmod +x scripts/setup-kb.sh && ./scripts/setup-kb.sh
#
# =============================================================================

set -e

REPO_URL="https://github.com/dereknguyen269/programing-best-practices"
INSTALL_SCRIPT_URL="https://raw.githubusercontent.com/dereknguyen269/programing-best-practices/main/scripts/install-skill.py"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# ── Helpers ───────────────────────────────────────────────────────────────────
ok()   { echo -e "${GREEN}  ✓ $*${NC}"; }
warn() { echo -e "${YELLOW}  ⚠ $*${NC}"; }
fail() { echo -e "${RED}  ✗ $*${NC}"; exit 1; }
step() { echo -e "\n${CYAN}▶ $*${NC}"; }

PYTHON=$(command -v python3 || command -v python || true)

echo -e "${BLUE}"
echo "════════════════════════════════════════════════"
echo "  Programming Best Practices — Project Setup"
echo "════════════════════════════════════════════════"
echo -e "${NC}"

# ── Detect project root ───────────────────────────────────────────────────────
PROJECT_ROOT="$(pwd)"
if [ ! -d "$PROJECT_ROOT/.git" ]; then
  warn "No .git found — running from: $PROJECT_ROOT"
fi

# ── Choose integration method ─────────────────────────────────────────────────
echo "How would you like to integrate the knowledge base?"
echo ""
echo "  1) Kiro steering  — auto-included in every Kiro session (recommended)"
echo "  2) Claude Code skill — auto-invoked when writing/reviewing code"
echo "  3) Both           — install for Kiro + Claude Code"
echo "  4) Git submodule  — add the full repo as a submodule"
echo ""
read -rp "Choose an option (1-4): " choice

case $choice in
  1) MODE="kiro" ;;
  2) MODE="claude" ;;
  3) MODE="both" ;;
  4) MODE="submodule" ;;
  *) fail "Invalid option." ;;
esac

# ── Submodule path ────────────────────────────────────────────────────────────
if [ "$MODE" = "submodule" ]; then
  step "Adding Git submodule..."
  [ ! -d ".git" ] && fail "Git submodule requires a git repository."
  mkdir -p .kb
  git submodule add "$REPO_URL" .kb/best-practices
  ok "Submodule added at .kb/best-practices"
  echo ""
  echo "  To update later:"
  echo "    git submodule update --remote .kb/best-practices"
  echo ""
  echo -e "${GREEN}════════════════════════════════════════════════"
  echo "  Done!"
  echo -e "════════════════════════════════════════════════${NC}"
  exit 0
fi

# ── Skill install path ────────────────────────────────────────────────────────
[ -z "$PYTHON" ] && fail "Python not found. Install Python 3 first."

# Crawl options
echo ""
echo "How much content to crawl?"
echo ""
echo "  1) Full  — all 150+ resources (~10-15 min)"
echo "  2) Quick — 20 resources for a fast test (~2 min)"
echo "  3) Skip  — use existing content/ if already crawled"
echo ""
read -rp "Choose an option (1-3): " crawl_choice

case $crawl_choice in
  1) CRAWL_OPT="" ;;
  2) CRAWL_OPT="--crawl-limit 20" ;;
  3) CRAWL_OPT="--skip-crawl" ;;
  *) fail "Invalid option." ;;
esac

# ── Download install-skill.py if running via curl (not inside the repo) ───────
INSTALL_SCRIPT="$(dirname "$0")/install-skill.py"

if [ ! -f "$INSTALL_SCRIPT" ]; then
  step "Downloading install-skill.py..."
  TMP_DIR=$(mktemp -d)
  curl -sSL "$INSTALL_SCRIPT_URL" -o "$TMP_DIR/install-skill.py" \
    && ok "Downloaded install-skill.py" \
    || fail "Failed to download install-skill.py"
  INSTALL_SCRIPT="$TMP_DIR/install-skill.py"
fi

# ── Run installer ─────────────────────────────────────────────────────────────
step "Installing best-practices skill (mode: $MODE)..."
"$PYTHON" "$INSTALL_SCRIPT" "$PROJECT_ROOT" --mode "$MODE" --force $CRAWL_OPT \
  && ok "Skill installed" \
  || fail "Installation failed"

# ── Post-install summary ──────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}════════════════════════════════════════════════"
echo "  Done!"
echo -e "════════════════════════════════════════════════${NC}"
echo ""

if [ "$MODE" = "kiro" ] || [ "$MODE" = "both" ]; then
  echo "  Kiro: .kiro/steering/best-practices/ (auto-included)"
fi
if [ "$MODE" = "claude" ] || [ "$MODE" = "both" ]; then
  echo "  Claude Code: skills/best-practices/ (auto-invoked)"
fi

echo ""
echo "  To update resources later:"
echo "    ./scripts/update.sh"
echo ""
echo "  Docs: $REPO_URL"
echo ""
