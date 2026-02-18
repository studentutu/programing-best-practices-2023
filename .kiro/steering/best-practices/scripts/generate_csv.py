#!/usr/bin/env python3
"""
Generate CSV databases from content/index.json and content/ markdown files.
Reads the crawled content and produces structured CSVs for BM25 search.
"""

import csv
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.parent.parent.parent
CONTENT_DIR = REPO_ROOT / "content"
INDEX_FILE = CONTENT_DIR / "index.json"
OUTPUT_DIR = Path(__file__).parent.parent / "data"


def extract_frontmatter(filepath):
    """Extract YAML frontmatter from markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}, ""
    
    if not text.startswith("---"):
        return {}, text
    
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    
    fm_text = text[3:end].strip()
    meta = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip().strip("'\"")
    
    body = text[end + 3:].strip()
    return meta, body


def extract_summary(body, max_chars=500):
    """Extract a useful summary from markdown body."""
    # Remove markdown links, images, badges
    text = re.sub(r'!\[.*?\]\(.*?\)', '', body)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove markdown headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r'^---+$', '', text, flags=re.MULTILINE)
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    if len(text) > max_chars:
        text = text[:max_chars].rsplit(' ', 1)[0] + "..."
    return text


def extract_keywords(title, category, subcategory, body):
    """Extract searchable keywords from content."""
    keywords = set()
    
    # From title
    for word in re.findall(r'\b[a-zA-Z#+.]{2,}\b', title):
        keywords.add(word.lower())
    
    # From category/subcategory
    for word in re.findall(r'\b[a-zA-Z#+.]{2,}\b', f"{category} {subcategory}"):
        keywords.add(word.lower())
    
    # Common language aliases
    aliases = {
        "javascript": ["js", "es6", "ecmascript", "node"],
        "typescript": ["ts"],
        "python": ["py", "django", "flask"],
        "ruby": ["rb", "rails", "ror"],
        "golang": ["go"],
        "c++": ["cpp", "cplusplus"],
        "c#": ["csharp", "dotnet"],
        "objective-c": ["objc", "ios"],
        "swift": ["ios", "macos"],
        "react": ["reactjs", "jsx"],
        "vue": ["vuejs"],
        "angular": ["angularjs", "ng"],
        "postgresql": ["postgres", "pg"],
        "mysql": ["mariadb"],
        "bash": ["shell", "sh", "zsh"],
    }
    
    for lang, alts in aliases.items():
        if lang in keywords or any(a in keywords for a in alts):
            keywords.add(lang)
            keywords.update(alts)
    
    # Extract from first 2000 chars of body for topic keywords
    snippet = body[:2000].lower()
    tech_terms = [
        "style guide", "best practices", "design patterns", "clean code",
        "performance", "security", "testing", "debugging", "refactoring",
        "architecture", "microservices", "api", "database", "sql",
        "frontend", "backend", "fullstack", "devops", "ci/cd",
        "docker", "kubernetes", "aws", "cloud", "serverless",
        "rest", "graphql", "websocket", "authentication", "authorization",
        "caching", "optimization", "scalability", "monitoring", "logging",
    ]
    for term in tech_terms:
        if term in snippet:
            keywords.add(term)
    
    return ", ".join(sorted(keywords))


# Language/technology mapping for the languages CSV
LANGUAGE_MAP = {
    "JavaScript Best Practices": {"language": "JavaScript", "domain": "frontend"},
    "TypeScript Best Practices": {"language": "TypeScript", "domain": "frontend"},
    "HTML Best Practices": {"language": "HTML", "domain": "frontend"},
    "CSS Best Practices": {"language": "CSS", "domain": "frontend"},
    "SASS Best Practices": {"language": "SASS/SCSS", "domain": "frontend"},
    "Python Best Practices": {"language": "Python", "domain": "backend"},
    "Ruby Best Practices": {"language": "Ruby", "domain": "backend"},
    "Rails Best Practices": {"language": "Ruby on Rails", "domain": "backend"},
    "PHP Best Practices": {"language": "PHP", "domain": "backend"},
    "Laravel Best Practices": {"language": "Laravel", "domain": "backend"},
    "NestJS Best Practices": {"language": "NestJS", "domain": "backend"},
    "Nodejs Best Practices": {"language": "Node.js", "domain": "backend"},
    "Java Best Practices": {"language": "Java", "domain": "backend"},
    "Kotlin Best Practices": {"language": "Kotlin", "domain": "backend"},
    "Scala Best Practices": {"language": "Scala", "domain": "backend"},
    "C# Best Practices": {"language": "C#", "domain": "backend"},
    "C Best Practices": {"language": "C/C++", "domain": "systems"},
    "Rust Best Practices": {"language": "Rust", "domain": "systems"},
    "Go Golang Best Practices": {"language": "Go", "domain": "backend"},
    "Swift Best Practices": {"language": "Swift", "domain": "mobile"},
    "Objective-C Best Practices": {"language": "Objective-C", "domain": "mobile"},
    "Perl Best Practices": {"language": "Perl", "domain": "scripting"},
    "Lua Best Practices": {"language": "Lua", "domain": "scripting"},
    "Reactjs Best Practices": {"language": "React", "domain": "frontend"},
    "React Native Best Practices": {"language": "React Native", "domain": "mobile"},
    "Vue Best Practices": {"language": "Vue.js", "domain": "frontend"},
    "Angular Best Practices": {"language": "Angular", "domain": "frontend"},
    "Nextjs Best Practices": {"language": "Next.js", "domain": "frontend"},
    "Nuxt Best Practices": {"language": "Nuxt", "domain": "frontend"},
    "SQL Best Practices": {"language": "SQL", "domain": "database"},
    "PostgreSQL Best Practices": {"language": "PostgreSQL", "domain": "database"},
    "MySQL Best Practices": {"language": "MySQL", "domain": "database"},
    "Bash Script Best Practices": {"language": "Bash", "domain": "devops"},
    "System Design Best Practices": {"language": "System Design", "domain": "architecture"},
    "Frontend Performance Best Practices": {"language": "Frontend Performance", "domain": "frontend"},
    "API Security Best Practices": {"language": "API Security", "domain": "security"},
    "AWS Best Practices": {"language": "AWS", "domain": "cloud"},
    "Microservices & Cloud-Native Best Practices": {"language": "Microservices", "domain": "cloud"},
}


def generate_resources_csv(index_data):
    """Generate the main resources.csv with all crawled content."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    rows = []
    for rid, entry in index_data.items():
        filepath = REPO_ROOT / entry.get("file", "")
        if not filepath.exists():
            continue
        
        fm, body = extract_frontmatter(filepath)
        title = entry.get("title", "")
        category = entry.get("category", "")
        subcategory = entry.get("subcategory", "")
        url = entry.get("url", "")
        
        # Determine language/tech
        lang_info = LANGUAGE_MAP.get(subcategory, {})
        language = lang_info.get("language", category)
        domain = lang_info.get("domain", "general")
        
        keywords = extract_keywords(title, category, subcategory, body)
        summary = extract_summary(body)
        
        # Determine source authority
        authority = "community"
        url_lower = url.lower()
        if any(org in url_lower for org in ["google.", "airbnb", "uber", "microsoft", "mozilla", "shopify"]):
            authority = "industry-leader"
        elif "github.com" in url_lower:
            authority = "open-source"
        elif any(org in url_lower for org in ["owasp", "12factor", "refactoring.guru"]):
            authority = "standard"
        
        rows.append({
            "ID": rid,
            "Title": title,
            "Language": language,
            "Domain": domain,
            "Category": category,
            "Subcategory": subcategory,
            "Authority": authority,
            "URL": url,
            "Keywords": keywords,
            "Summary": summary,
        })
    
    outfile = OUTPUT_DIR / "resources.csv"
    fieldnames = ["ID", "Title", "Language", "Domain", "Category", "Subcategory", "Authority", "URL", "Keywords", "Summary"]
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ resources.csv: {len(rows)} entries")
    return rows


def generate_languages_csv(resources):
    """Generate languages.csv — one row per language/tech with aggregated info."""
    lang_data = {}
    for r in resources:
        lang = r["Language"]
        if lang not in lang_data:
            lang_data[lang] = {
                "Language": lang,
                "Domain": r["Domain"],
                "Resource Count": 0,
                "Top Resources": [],
                "URLs": [],
                "Keywords": set(),
            }
        lang_data[lang]["Resource Count"] += 1
        if len(lang_data[lang]["Top Resources"]) < 5:
            lang_data[lang]["Top Resources"].append(r["Title"])
            lang_data[lang]["URLs"].append(r["URL"])
        for kw in r["Keywords"].split(", "):
            lang_data[lang]["Keywords"].add(kw)
    
    rows = []
    for lang, data in sorted(lang_data.items()):
        rows.append({
            "Language": data["Language"],
            "Domain": data["Domain"],
            "Resource Count": data["Resource Count"],
            "Top Resources": " | ".join(data["Top Resources"]),
            "Top URLs": " | ".join(data["URLs"]),
            "Keywords": ", ".join(sorted(data["Keywords"])),
        })
    
    outfile = OUTPUT_DIR / "languages.csv"
    fieldnames = ["Language", "Domain", "Resource Count", "Top Resources", "Top URLs", "Keywords"]
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ languages.csv: {len(rows)} languages/technologies")


def generate_categories_csv(resources):
    """Generate categories.csv — one row per category."""
    cat_data = {}
    for r in resources:
        cat = r["Category"]
        if cat not in cat_data:
            cat_data[cat] = {
                "Category": cat,
                "Languages": set(),
                "Resource Count": 0,
                "Top Resources": [],
            }
        cat_data[cat]["Languages"].add(r["Language"])
        cat_data[cat]["Resource Count"] += 1
        if len(cat_data[cat]["Top Resources"]) < 5:
            cat_data[cat]["Top Resources"].append(r["Title"])
    
    rows = []
    for cat, data in sorted(cat_data.items()):
        rows.append({
            "Category": data["Category"],
            "Languages": ", ".join(sorted(data["Languages"])),
            "Resource Count": data["Resource Count"],
            "Top Resources": " | ".join(data["Top Resources"]),
        })
    
    outfile = OUTPUT_DIR / "categories.csv"
    fieldnames = ["Category", "Languages", "Resource Count", "Top Resources"]
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ categories.csv: {len(rows)} categories")


def main():
    if not INDEX_FILE.exists():
        print(f"Error: {INDEX_FILE} not found. Run the crawler first.")
        sys.exit(1)
    
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        index_data = json.load(f)
    
    print(f"Generating CSV databases from {len(index_data)} resources...")
    resources = generate_resources_csv(index_data)
    generate_languages_csv(resources)
    generate_categories_csv(resources)
    print(f"\nDone! CSV files written to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
