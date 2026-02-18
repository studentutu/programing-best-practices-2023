#!/usr/bin/env python3
"""
Best Practices Search Core - BM25 search engine for programming best practices.
"""

import csv
import re
from pathlib import Path
from math import log
from collections import defaultdict

# ============ CONFIGURATION ============
DATA_DIR = Path(__file__).parent.parent / "data"
CONTENT_DIR = Path(__file__).parent.parent.parent.parent.parent / "content"
MAX_RESULTS = 5

CSV_CONFIG = {
    "resource": {
        "file": "resources.csv",
        "search_cols": ["Title", "Language", "Keywords", "Summary", "Category", "Subcategory"],
        "output_cols": ["Title", "Language", "Domain", "Authority", "URL", "Keywords", "Summary"],
    },
    "language": {
        "file": "languages.csv",
        "search_cols": ["Language", "Domain", "Keywords", "Top Resources"],
        "output_cols": ["Language", "Domain", "Resource Count", "Top Resources", "Top URLs", "Keywords"],
    },
    "category": {
        "file": "categories.csv",
        "search_cols": ["Category", "Languages", "Top Resources"],
        "output_cols": ["Category", "Languages", "Resource Count", "Top Resources"],
    },
}


# ============ BM25 IMPLEMENTATION ============

class BM25:
    """Okapi BM25 ranking function for text search."""
    
    def __init__(self, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.doc_len = []
        self.avgdl = 0
        self.doc_freqs = []
        self.idf = {}
        self.doc_count = 0
        self.tokenized_docs = []
    
    def tokenize(self, text):
        text = str(text).lower()
        tokens = re.findall(r'[a-z0-9#+.]+', text)
        return tokens
    
    def fit(self, documents):
        self.doc_count = len(documents)
        self.tokenized_docs = [self.tokenize(doc) for doc in documents]
        self.doc_len = [len(doc) for doc in self.tokenized_docs]
        self.avgdl = sum(self.doc_len) / self.doc_count if self.doc_count else 1
        
        df = defaultdict(int)
        for doc in self.tokenized_docs:
            unique_terms = set(doc)
            for term in unique_terms:
                df[term] += 1
        
        self.idf = {}
        for term, freq in df.items():
            self.idf[term] = log((self.doc_count - freq + 0.5) / (freq + 0.5) + 1)
    
    def score(self, query):
        query_tokens = self.tokenize(query)
        scores = []
        for i, doc in enumerate(self.tokenized_docs):
            score = 0
            doc_len = self.doc_len[i]
            term_freqs = defaultdict(int)
            for term in doc:
                term_freqs[term] += 1
            
            for token in query_tokens:
                if token not in self.idf:
                    continue
                tf = term_freqs.get(token, 0)
                idf = self.idf[token]
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                score += idf * numerator / denominator
            
            scores.append(score)
        return scores


# ============ SEARCH FUNCTIONS ============

def _load_csv(filepath):
    """Load CSV file and return list of dicts."""
    with open(filepath, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _search_csv(filepath, search_cols, output_cols, query, max_results):
    """Search a CSV file using BM25."""
    rows = _load_csv(filepath)
    if not rows:
        return []
    
    documents = []
    for row in rows:
        doc_text = " ".join(str(row.get(col, "")) for col in search_cols)
        documents.append(doc_text)
    
    bm25 = BM25()
    bm25.fit(documents)
    scores = bm25.score(query)
    
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            result = {col: rows[idx].get(col, "") for col in output_cols if col in rows[idx]}
            result["_score"] = round(score, 3)
            results.append(result)
    
    return results


def search(query, domain=None, max_results=MAX_RESULTS):
    """Search best practices by domain or auto-detect."""
    if domain and domain in CSV_CONFIG:
        config = CSV_CONFIG[domain]
    else:
        domain = "resource"
        config = CSV_CONFIG["resource"]
    
    filepath = DATA_DIR / config["file"]
    if not filepath.exists():
        return {"error": f"Data file not found: {filepath}. Run generate_csv.py first.", "query": query}
    
    results = _search_csv(filepath, config["search_cols"], config["output_cols"], query, max_results)
    
    return {
        "domain": domain,
        "query": query,
        "file": config["file"],
        "count": len(results),
        "results": results,
    }


def search_content(query, language=None, max_results=MAX_RESULTS):
    """Search within crawled content files for deeper answers."""
    import json
    
    index_file = CONTENT_DIR / "index.json"
    if not index_file.exists():
        return {"error": "content/index.json not found. Run the crawler first.", "query": query}
    
    with open(index_file, "r", encoding="utf-8") as f:
        index_data = json.load(f)
    
    # Filter by language if specified
    entries = []
    for rid, entry in index_data.items():
        if language:
            sub = entry.get("subcategory", "").lower()
            cat = entry.get("category", "").lower()
            title = entry.get("title", "").lower()
            lang_lower = language.lower()
            if lang_lower not in sub and lang_lower not in cat and lang_lower not in title:
                continue
        entries.append((rid, entry))
    
    if not entries:
        return {"error": f"No content found for language: {language}", "query": query}
    
    # Build documents from content files
    documents = []
    valid_entries = []
    for rid, entry in entries:
        filepath = Path(__file__).parent.parent.parent.parent / entry.get("file", "")
        if not filepath.exists():
            continue
        try:
            text = filepath.read_text(encoding="utf-8", errors="replace")
            # Remove frontmatter
            if text.startswith("---"):
                end = text.find("---", 3)
                if end != -1:
                    text = text[end + 3:]
            documents.append(text[:3000])  # First 3000 chars for search
            valid_entries.append((rid, entry))
        except Exception:
            continue
    
    if not documents:
        return {"error": "No readable content files found.", "query": query}
    
    bm25 = BM25()
    bm25.fit(documents)
    scores = bm25.score(query)
    
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    results = []
    for idx, score in ranked[:max_results]:
        if score > 0:
            rid, entry = valid_entries[idx]
            results.append({
                "Title": entry.get("title", ""),
                "Category": entry.get("category", ""),
                "URL": entry.get("url", ""),
                "File": entry.get("file", ""),
                "Relevance": round(score, 3),
            })
    
    return {
        "domain": "content",
        "query": query,
        "language": language,
        "count": len(results),
        "results": results,
    }
