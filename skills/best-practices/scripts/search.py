#!/usr/bin/env python3
"""
Best Practices Search - BM25 search engine for programming best practices.

Usage:
  python search.py "<query>"                          # Search all resources
  python search.py "<query>" --domain resource        # Search resources
  python search.py "<query>" --domain language         # Search by language
  python search.py "<query>" --domain category         # Search by category
  python search.py "<query>" --content                 # Deep search in content files
  python search.py "<query>" --content --lang python   # Deep search filtered by language
  python search.py "<query>" --recommend               # Get full recommendation for a language/topic
"""

import argparse
import sys
import io
from core import CSV_CONFIG, MAX_RESULTS, search, search_content

# Force UTF-8
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
if sys.stderr.encoding and sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def format_output(result):
    """Format results for AI consumption."""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    output.append(f"## Best Practices Search Results")
    output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    if result.get("language"):
        output.append(f"**Language Filter:** {result['language']}")
    output.append(f"**Found:** {result['count']} results\n")

    for i, row in enumerate(result['results'], 1):
        output.append(f"### Result {i}")
        for key, value in row.items():
            if key.startswith("_"):
                continue
            value_str = str(value)
            if len(value_str) > 400:
                value_str = value_str[:400] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


def format_recommendation(query, resource_results, content_results):
    """Format a comprehensive recommendation."""
    output = []
    output.append(f"{'=' * 70}")
    output.append(f"  BEST PRACTICES RECOMMENDATION: {query.upper()}")
    output.append(f"{'=' * 70}")
    output.append("")
    
    # Top resources
    if resource_results.get("results"):
        output.append("  📚 TOP RESOURCES:")
        for i, r in enumerate(resource_results["results"][:5], 1):
            authority_badge = ""
            auth = r.get("Authority", "")
            if auth == "industry-leader":
                authority_badge = " ⭐"
            elif auth == "standard":
                authority_badge = " 🏆"
            output.append(f"    {i}. {r.get('Title', 'N/A')}{authority_badge}")
            output.append(f"       URL: {r.get('URL', 'N/A')}")
            output.append(f"       Domain: {r.get('Domain', 'N/A')} | Authority: {auth}")
            if r.get("Summary"):
                summary = r["Summary"][:200]
                output.append(f"       Summary: {summary}...")
            output.append("")
    
    # Deep content matches
    if content_results.get("results"):
        output.append("  📖 DEEP CONTENT (crawled articles):")
        for i, r in enumerate(content_results["results"][:3], 1):
            output.append(f"    {i}. {r.get('Title', 'N/A')}")
            output.append(f"       File: {r.get('File', 'N/A')}")
            output.append(f"       URL: {r.get('URL', 'N/A')}")
            output.append("")
    
    if not resource_results.get("results") and not content_results.get("results"):
        output.append("  No results found. Try different keywords.")
    
    output.append(f"{'=' * 70}")
    return "\n".join(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Best Practices Search")
    parser.add_argument("query", help="Search query (e.g., 'python style guide', 'react performance')")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain: resource, language, category")
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 5)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--content", "-c", action="store_true", help="Deep search within crawled content files")
    parser.add_argument("--lang", "-l", type=str, default=None, help="Filter content search by language")
    parser.add_argument("--recommend", "-r", action="store_true", help="Get full recommendation (resources + content)")

    args = parser.parse_args()

    if args.recommend:
        # Full recommendation: search resources + content
        resource_results = search(args.query, "resource", args.max_results)
        content_results = search_content(args.query, args.lang, 3)
        print(format_recommendation(args.query, resource_results, content_results))
    elif args.content:
        result = search_content(args.query, args.lang, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
    else:
        result = search(args.query, args.domain, args.max_results)
        if args.json:
            import json
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print(format_output(result))
