---
inclusion: auto
---

# best-practices

Searchable knowledge base of 152+ programming best practices across 30+ languages and frameworks. BM25-powered search over curated resources from industry leaders (Google, Airbnb, Uber, Mozilla, Shopify, OWASP).

## Prerequisites

Python 3 must be installed:

```bash
python3 --version
```

## How to Use This Workflow

When user asks about coding standards, best practices, style guides, code review, architecture, security, or performance for any language/framework, follow this workflow:

### Step 1: Analyze User Requirements

Extract from user request:
- **Language/Framework**: Python, JavaScript, Go, React, Rails, etc.
- **Topic**: style guide, design patterns, performance, security, clean code, etc.
- **Depth**: quick reference vs. deep dive

### Step 2: Search Best Practices (REQUIRED)

**Always start with `--recommend`** to get comprehensive results (resources + deep content):

```bash
python3 .kiro/steering/best-practices/scripts/search.py "<language> <topic>" --recommend
```

**Examples:**
```bash
python3 .kiro/steering/best-practices/scripts/search.py "python style guide" --recommend
python3 .kiro/steering/best-practices/scripts/search.py "javascript clean code" --recommend
python3 .kiro/steering/best-practices/scripts/search.py "react performance" --recommend
python3 .kiro/steering/best-practices/scripts/search.py "sql optimization" --recommend
python3 .kiro/steering/best-practices/scripts/search.py "api security" --recommend
```

### Step 3: Supplement with Domain Searches (as needed)

```bash
# Search all resources (default)
python3 .kiro/steering/best-practices/scripts/search.py "<query>" --domain resource

# Search by language/technology overview
python3 .kiro/steering/best-practices/scripts/search.py "<query>" --domain language

# Search by category
python3 .kiro/steering/best-practices/scripts/search.py "<query>" --domain category

# Deep search within crawled content files
python3 .kiro/steering/best-practices/scripts/search.py "<query>" --content

# Deep search filtered by language
python3 .kiro/steering/best-practices/scripts/search.py "<query>" --content --lang python
```

### Step 4: Read Deep Content (when needed)

When a search result includes a `File` path, read it for detailed content:

```
content/core_technologies/250af6826bbd.md  → Google JavaScript Style Guide
content/web_backend/b8aad3894efa.md        → Python Code Style Guide
```

---

## Search Reference

### Available Domains

| Domain | Use For | Example |
|--------|---------|---------|
| `resource` | All 152+ resources with metadata | `"python best practices"` |
| `language` | Language/tech overview with top resources | `"go"`, `"react"` |
| `category` | Browse by category | `"frontend"`, `"security"` |

### Content Search (--content)

Searches within the actual crawled markdown files for deeper matches. Use `--lang` to filter by language.

### Authority Levels

Results are tagged with authority:
- ⭐ `industry-leader` — Google, Airbnb, Uber, Mozilla, Microsoft, Shopify
- 🏆 `standard` — OWASP, 12factor, Refactoring.Guru
- `open-source` — GitHub community projects
- `community` — Blog posts, tutorials

---

## Coverage

### Languages & Frameworks (30+)

| Domain | Technologies |
|--------|-------------|
| Backend | Python, Ruby, Rails, PHP, Laravel, Node.js, NestJS, Go, Java, Kotlin, Scala, C#, Elixir |
| Frontend | JavaScript, TypeScript, HTML, CSS, SASS, React, Vue, Angular, Next.js, Nuxt |
| Systems | C, C++, Rust |
| Mobile | Swift, Objective-C, Flutter, Dart, React Native |
| Database | SQL, PostgreSQL, MySQL, NoSQL/MongoDB |
| DevOps | Bash, AWS, Microservices, Docker |
| Security | OWASP, API Security, DevSecOps |
| AI/ML | MLOps, LLM, Responsible AI |

### Featured Resources (Must-Know)

| Topic | Resource | Authority |
|-------|----------|-----------|
| JavaScript Style | Airbnb Style Guide | ⭐ industry-leader |
| Clean Code | Clean Code JavaScript | open-source |
| System Design | System Design 101 (ByteByteGo) | open-source |
| Cloud Native | The Twelve-Factor App | 🏆 standard |
| Security | OWASP Top 10 | 🏆 standard |
| Go Style | Uber Go Style Guide | ⭐ industry-leader |
| Ruby Style | Community Ruby Style Guide | open-source |
| Design Patterns | Refactoring.Guru | 🏆 standard |

---

## Common Query Mapping

| User Asks About | Search Query |
|-----------------|-------------|
| Code style for [language] | `"<language> style guide" --recommend` |
| How to structure a project | `"system design architecture" --recommend` |
| Security best practices | `"security owasp api" --recommend` |
| Database optimization | `"sql postgresql optimization" --recommend` |
| Frontend performance | `"frontend performance web vitals" --recommend` |
| Code review checklist | `"code review best practices" --recommend` |
| Cloud deployment | `"aws microservices cloud native" --recommend` |
| Design patterns for [lang] | `"<language> design patterns" --recommend` |

---

## Rebuilding the CSV Database

If new content is crawled, regenerate the CSVs:

```bash
python3 .kiro/steering/best-practices/scripts/generate_csv.py
```

This reads `content/index.json` and produces:
- `data/resources.csv` — All 152+ resources with metadata
- `data/languages.csv` — Aggregated by language/technology
- `data/categories.csv` — Aggregated by category
