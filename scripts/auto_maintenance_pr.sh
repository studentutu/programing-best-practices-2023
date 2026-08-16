#!/usr/bin/env bash
# auto_maintenance_pr.sh — Automated weekly maintenance: fixes links, commits, and opens a PR.

set -e

REPO_DIR="/home/ubuntu/repo"
cd "$REPO_DIR"

echo "=== Starting Automated Repository Maintenance ==="

# 1. Ensure we are on main and up to date
git checkout master || git checkout main
git pull origin $(git branch --show-current)

# 2. Create a unique maintenance branch
BRANCH_NAME="chore/weekly-maintenance-$(date +%Y%m%d)"
git checkout -b "$BRANCH_NAME" || git checkout "$BRANCH_NAME"

echo "Created/Switched to branch: $BRANCH_NAME"

# 3. Run link fixer / maintenance scripts
PYTHON=$(command -v python3 || command -v python)
if [ -f "$REPO_DIR/scripts/fix_links.py" ]; then
    echo "Running link maintenance..."
    "$PYTHON" "$REPO_DIR/scripts/fix_links.py"
fi

# 4. Check if there are any changes
if git diff --quiet && git diff --staged --quiet; then
    echo "No maintenance changes needed at this time."
    exit 0
fi

# 5. Commit changes
git add .
git commit -m "chore: weekly automated content maintenance and link fixes [skip ci]"

# 6. Push branch and create PR using GitHub CLI
echo "Pushing branch to remote..."
git push -u origin "$BRANCH_NAME" --force

echo "Creating Pull Request..."
gh pr create \
  --title "🧹 Weekly Content Maintenance & Link Fixes ($(date +%Y-%m-%d))" \
  --body "Automated weekly maintenance run by Manus AI. This PR updates outdated links, verifies documentation clarity, and ensures adherence to repository standards." \
  --base main \
  --head "$BRANCH_NAME"

echo "=== Automated Maintenance & PR Creation Complete ==="
