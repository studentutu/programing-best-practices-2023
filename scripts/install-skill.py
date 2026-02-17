#!/usr/bin/env python3
"""
Install best-practices skill to a target project.

Full pipeline: install deps → crawl content → generate CSVs → copy skill.

Supports:
  - Claude Code skill:  copies to <target>/skills/best-practices/
  - Kiro steering:      copies to <target>/.kiro/steering/best-practices/

Usage:
  python3 scripts/install-skill.py <target_path> --mode claude
  python3 scripts/install-skill.py <target_path> --mode kiro
  python3 scripts/install-skill.py <target_path> --mode both
  python3 scripts/install-skill.py <target_path> --mode both --skip-crawl
  python3 scripts/install-skill.py <target_path> --mode both --crawl-limit 20
"""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
SKILL_SRC = REPO_ROOT / "skills" / "best-practices"
CRAWLER_DIR = REPO_ROOT / "scripts" / "crawler"
CONTENT_DIR = REPO_ROOT / "content"
INDEX_FILE = CONTENT_DIR / "index.json"

DEST_MAP = {
    "claude": "skills/best-practices",
    "kiro": ".kiro/steering/best-practices",
}


# ============ STEP 1: DEPENDENCIES ============

def install_crawler_deps():
    """Install crawler dependencies via pip."""
    req_file = CRAWLER_DIR / "requirements.txt"
    if not req_file.exists():
        print("  ⚠ requirements.txt not found, skipping dependency install")
        return True

    print("  Installing crawler dependencies...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(req_file), "-q"],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"  ✗ pip install failed:\n{result.stderr}")
        return False

    print("  ✓ Dependencies installed")
    return True


# ============ STEP 2: CRAWL ============

def crawl_content(limit=None, category=None, update=False):
    """Run the crawler to fetch content from README.md links."""
    crawl_script = CRAWLER_DIR / "crawl.py"
    if not crawl_script.exists():
        print(f"  ✗ Crawler not found at {crawl_script}")
        return False

    cmd = [sys.executable, str(crawl_script)]
    if limit:
        cmd += ["--limit", str(limit)]
    if category:
        cmd += ["--category", category]
    if update:
        cmd += ["--update"]

    desc = []
    if limit:
        desc.append(f"limit={limit}")
    if category:
        desc.append(f"category={category}")
    if update:
        desc.append("update")
    desc_str = f" ({', '.join(desc)})" if desc else ""

    print(f"  Crawling content{desc_str}...")
    result = subprocess.run(cmd, cwd=str(REPO_ROOT))

    if result.returncode != 0:
        print("  ✗ Crawl failed")
        return False

    if INDEX_FILE.exists():
        import json
        with open(INDEX_FILE, "r") as f:
            count = len(json.load(f))
        print(f"  ✓ Crawled content: {count} resources in content/index.json")
    else:
        print("  ✗ content/index.json not created")
        return False

    return True


# ============ STEP 3: GENERATE CSVs ============

def generate_csvs():
    """Run generate_csv.py to build searchable CSV databases."""
    gen_script = SKILL_SRC / "scripts" / "generate_csv.py"
    if not gen_script.exists():
        print(f"  ✗ generate_csv.py not found at {gen_script}")
        return False

    print("  Generating CSV databases...")
    result = subprocess.run(
        [sys.executable, str(gen_script)],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"  ✗ CSV generation failed:\n{result.stderr}")
        return False

    for line in result.stdout.strip().split("\n"):
        print(f"  {line}")

    return True


# ============ STEP 4: COPY SKILL ============

def rewrite_skill_md(src_text, script_path_prefix):
    """Rewrite SKILL.md to use correct paths for the target location."""
    text = src_text
    text = text.replace(
        "python3 skills/best-practices/scripts/",
        f"python3 {script_path_prefix}/scripts/"
    )
    text = text.replace(
        "python3 .kiro/steering/best-practices/scripts/",
        f"python3 {script_path_prefix}/scripts/"
    )
    return text


def rewrite_core_py(src_text, depth_to_root):
    """Rewrite core.py CONTENT_DIR to correct depth for target location."""
    parents = ".parent" * depth_to_root
    old_pattern = 'CONTENT_DIR = Path(__file__).parent.parent.parent.parent / "content"'
    new_line = f'CONTENT_DIR = Path(__file__){parents} / "content"'
    return src_text.replace(old_pattern, new_line)


def rewrite_generate_csv(src_text, depth_to_root):
    """Rewrite generate_csv.py REPO_ROOT to correct depth for target location."""
    parents = ".parent" * depth_to_root
    old_pattern = 'REPO_ROOT = Path(__file__).parent.parent.parent.parent'
    new_line = f'REPO_ROOT = Path(__file__){parents}'
    return src_text.replace(old_pattern, new_line)


def copy_skill(target_path, mode):
    """Copy skill to target project with correct path rewrites."""
    dest_rel = DEST_MAP[mode]
    dest = target_path / dest_rel
    script_path_prefix = dest_rel

    depth_map = {
        "claude": 4,   # skills/best-practices/scripts/file.py
        "kiro": 5,     # .kiro/steering/best-practices/scripts/file.py
    }
    depth = depth_map[mode]

    if dest.exists():
        print(f"  ⚠ Removing existing {dest_rel}/")
        shutil.rmtree(dest)

    # Copy data/
    data_src = SKILL_SRC / "data"
    data_dest = dest / "data"
    if data_src.exists() and list(data_src.glob("*.csv")):
        shutil.copytree(data_src, data_dest)
        csv_count = len(list(data_dest.glob("*.csv")))
        print(f"  ✓ Copied data/ ({csv_count} CSV files)")
    else:
        data_dest.mkdir(parents=True, exist_ok=True)
        print(f"  ⚠ No CSV data found — run generate_csv.py after crawling")

    # Copy and rewrite scripts/
    scripts_src = SKILL_SRC / "scripts"
    scripts_dest = dest / "scripts"
    scripts_dest.mkdir(parents=True, exist_ok=True)

    for py_file in scripts_src.glob("*.py"):
        src_text = py_file.read_text(encoding="utf-8")
        if py_file.name == "core.py":
            src_text = rewrite_core_py(src_text, depth)
        elif py_file.name == "generate_csv.py":
            src_text = rewrite_generate_csv(src_text, depth)
        (scripts_dest / py_file.name).write_text(src_text, encoding="utf-8")

    print(f"  ✓ Copied scripts/ (paths adjusted for {mode})")

    # Copy and rewrite SKILL.md
    skill_src = SKILL_SRC / "SKILL.md"
    if skill_src.exists():
        src_text = skill_src.read_text(encoding="utf-8")
        rewritten = rewrite_skill_md(src_text, script_path_prefix)

        if mode == "claude":
            if rewritten.startswith("---"):
                end = rewritten.find("---", 3)
                if end != -1:
                    rewritten = rewritten[end + 3:].lstrip("\n")

        (dest / "SKILL.md").write_text(rewritten, encoding="utf-8")
        print(f"  ✓ Created SKILL.md ({mode} format)")

    return dest


# ============ MAIN ============

def print_post_install(target_path, mode, dest):
    """Print post-install instructions."""
    rel = dest.relative_to(target_path)
    print(f"\n{'─' * 60}")
    print(f"  Installed to: {rel}/")
    print(f"{'─' * 60}")

    if mode == "claude":
        print(f"""
  Claude Code will auto-detect skills/best-practices/SKILL.md

  To search:
    python3 {rel}/scripts/search.py "python style guide" --recommend
""")
    elif mode == "kiro":
        print(f"""
  Kiro will auto-include .kiro/steering/best-practices/SKILL.md
  (inclusion: auto is set in frontmatter)

  To search:
    python3 {rel}/scripts/search.py "python style guide" --recommend
""")


def main():
    parser = argparse.ArgumentParser(
        description="Install best-practices skill to a target project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Full install (crawl all + generate + copy)
  python3 scripts/install-skill.py ~/Projects/my-app --mode claude

  # Quick test (crawl 20 resources only)
  python3 scripts/install-skill.py ~/Projects/my-app --mode kiro --crawl-limit 20

  # Skip crawl (use existing content/)
  python3 scripts/install-skill.py ~/Projects/my-app --mode both --skip-crawl

  # Crawl specific category only
  python3 scripts/install-skill.py ~/Projects/my-app --mode both --crawl-category python

  # Update existing crawled content
  python3 scripts/install-skill.py ~/Projects/my-app --mode both --crawl-update
        """
    )
    parser.add_argument("target", help="Target project path")
    parser.add_argument(
        "--mode", "-m",
        choices=["claude", "kiro", "both"],
        default="both",
        help="Install mode: claude, kiro, or both (default: both)"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite existing installation without prompting"
    )
    # Crawl options
    parser.add_argument(
        "--skip-crawl",
        action="store_true",
        help="Skip crawling, use existing content/ data"
    )
    parser.add_argument(
        "--crawl-limit",
        type=int, default=None,
        help="Limit number of resources to crawl (e.g., 20 for quick test)"
    )
    parser.add_argument(
        "--crawl-category",
        type=str, default=None,
        help="Crawl only a specific category (e.g., python, javascript)"
    )
    parser.add_argument(
        "--crawl-update",
        action="store_true",
        help="Update existing crawled content instead of skipping"
    )

    args = parser.parse_args()
    target = Path(args.target).expanduser().resolve()

    if not target.exists():
        print(f"Error: Target path does not exist: {target}")
        sys.exit(1)
    if not target.is_dir():
        print(f"Error: Target path is not a directory: {target}")
        sys.exit(1)
    if not SKILL_SRC.exists():
        print(f"Error: Skill source not found at {SKILL_SRC}")
        sys.exit(1)

    modes = ["claude", "kiro"] if args.mode == "both" else [args.mode]

    print("=" * 60)
    print("  Best Practices Skill Installer")
    print("=" * 60)
    print(f"  Target:  {target}")
    print(f"  Mode:    {args.mode}")
    print()

    # --- Step 1: Dependencies ---
    has_content = INDEX_FILE.exists()
    need_crawl = not args.skip_crawl and (not has_content or args.crawl_update or args.crawl_limit or args.crawl_category)

    if need_crawl:
        print("[1/4] Installing dependencies...")
        if not install_crawler_deps():
            print("\n  Failed to install dependencies. You can install manually:")
            print(f"  pip install -r {CRAWLER_DIR / 'requirements.txt'}")
            sys.exit(1)
    else:
        print("[1/4] Dependencies — skipped (not crawling)")

    # --- Step 2: Crawl ---
    if need_crawl:
        print("\n[2/4] Crawling content...")
        if not crawl_content(
            limit=args.crawl_limit,
            category=args.crawl_category,
            update=args.crawl_update
        ):
            print("\n  Crawl failed. You can retry manually:")
            print(f"  python3 {CRAWLER_DIR / 'crawl.py'}")
            sys.exit(1)
    elif has_content:
        import json
        with open(INDEX_FILE, "r") as f:
            count = len(json.load(f))
        print(f"[2/4] Crawling — skipped (using existing {count} resources)")
    else:
        print("[2/4] Crawling — skipped (no content/ found, CSVs will be empty)")

    # --- Step 3: Generate CSVs ---
    if INDEX_FILE.exists():
        print("\n[3/4] Generating CSV databases...")
        if not generate_csvs():
            print("\n  CSV generation failed. You can retry manually:")
            print(f"  python3 {SKILL_SRC / 'scripts' / 'generate_csv.py'}")
            sys.exit(1)
    else:
        print("\n[3/4] CSV generation — skipped (no content/index.json)")

    # --- Step 4: Copy skill ---
    print(f"\n[4/4] Installing skill...")
    for mode in modes:
        dest_rel = DEST_MAP[mode]
        dest = target / dest_rel

        if dest.exists() and not args.force:
            response = input(f"  {dest_rel}/ already exists. Overwrite? [y/N] ")
            if response.lower() != "y":
                print(f"  Skipped {mode} installation.")
                continue

        print(f"\n  [{mode.upper()}]")
        dest_path = copy_skill(target, mode)
        print_post_install(target, mode, dest_path)

    print("=" * 60)
    print("  Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()
