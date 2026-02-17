# Project Overview

## Quick Summary
- **Name**: Programming Best Practices Knowledge Base
- **Description**: Curated collection of coding standards, style guides, and best practices across 30+ programming languages and frameworks
- **Domain**: Developer Education / Knowledge Management
- **Status**: 🚧 Work in Progress — continuously updated

## Technology Stack

### Core
- **Content Format**: Markdown (README.md as primary knowledge base)
- **Crawler**: Python 3 (requests, beautifulsoup4, markdownify, aiohttp)
- **Shell Scripts**: Bash (setup, quick-start automation)

### Dependencies (Crawler)
- requests >= 2.28.0
- beautifulsoup4 >= 4.11.0
- markdownify >= 0.11.0
- tqdm >= 4.64.0
- PyYAML >= 6.0
- aiohttp >= 3.8.0
- aiofiles >= 23.0.0

### Infrastructure
- **Hosting**: GitHub repository
- **License**: CC0 1.0 Universal (Public Domain)
- **CI**: GitHub-based (FUNDING.yml)

## Architecture

### Pattern
Static knowledge base with optional Python crawler for offline content access and AI summary generation.

### Directory Structure
```
programing-best-practices/
├── README.md                    # Main knowledge base (1000+ lines, 30+ languages)
├── CLAUDE.md / AGENTS.md        # AI editor configurations
├── .agent/ .kiro/ .cursorrules  # Multi-editor AI support
├── scripts/
│   ├── crawler/                 # Python crawler tools
│   │   ├── crawl.py             # Main crawler
│   │   ├── search.py            # Local search tool
│   │   ├── generate_summaries.py # AI summary generator
│   │   └── requirements.txt
│   ├── quick-start.sh           # Interactive setup script
│   └── setup-kb.sh              # Integration setup for other projects
├── templates/                   # AI editor config templates
├── docs/                        # Documentation and guides
├── content/                     # (Generated) Crawled content
└── summaries/                   # (Generated) AI-ready summaries
```

### Key Components
- **README.md**: Primary knowledge base with curated links organized by category
- **Crawler System**: Downloads external resources for offline access
- **Summary Generator**: Creates condensed AI-optimized summaries
- **Multi-Editor Support**: Config files for Claude, Kiro, Cursor, Windsurf, Antigravity
- **Templates**: Reusable configs for integrating into other projects

## Entry Points
- **Knowledge Base**: README.md
- **Setup**: `./scripts/quick-start.sh`
- **Crawler**: `python3 scripts/crawler/crawl.py`
- **Search**: `python3 scripts/crawler/search.py "query"`

## Development Commands
- **Setup**: `./scripts/quick-start.sh --minimal`
- **Full Setup**: `./scripts/quick-start.sh --full`
- **Crawl**: `python3 scripts/crawler/crawl.py [--category X] [--limit N]`
- **Search**: `python3 scripts/crawler/search.py "term"`
- **Summaries**: `python3 scripts/crawler/generate_summaries.py`

## Code Conventions
- Markdown for all documentation
- Python for tooling (PEP 8 style)
- Bash for automation scripts
- Resource format: `* [Resource Title](URL) — *@author or description*`

## Important Notes
- This is primarily a documentation/knowledge repo, not an application
- README.md is the core deliverable (~1000+ lines)
- Crawler and tools are supplementary for offline/AI use
- Supports 5+ AI coding editors via config files
