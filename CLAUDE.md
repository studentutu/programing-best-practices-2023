# Programming Best Practices - Knowledge Base

This repository is a **curated collection of programming best practices** across 30+ languages, frameworks, and tools. It serves as a comprehensive reference guide for developers at all skill levels.

## 📚 Repository Purpose

This knowledge base provides:
- **Style Guides** - Coding conventions and standards from industry leaders (Airbnb, Google, Uber, etc.)
- **Best Practices** - Production-ready patterns and practices
- **Design Patterns** - Language-specific implementations
- **Security Guidelines** - OWASP, DevSecOps, and API security
- **Performance Tips** - Optimization and scalability resources

## 🗂️ Repository Structure

```
programing-best-practices/
├── README.md                # Main knowledge base document with all curated resources
├── .claude-plugin/          # Claude Code plugin manifest
│   └── plugin.json
├── skills/                  # Claude Code auto-invoked skills
│   ├── best-practices/      # Language & framework best practices
│   │   └── SKILL.md
│   └── security-review/     # Security audit skill
│       └── SKILL.md
├── commands/                # Claude Code slash commands
│   ├── best-practices.md    # /best-practices [language]
│   ├── review-code.md       # /review-code
│   └── setup-standards.md   # /setup-standards [stack]
├── contributing.md          # Contribution guidelines
├── LICENSE                  # CC0 1.0 Universal License
└── .github/
    └── FUNDING.yml          # GitHub sponsorship config
```

## 🔌 Claude Code Plugin

This repository is a Claude Code plugin. Install it with:

```
/plugin marketplace add dereknguyen269/programing-best-practices
/plugin install programming-best-practices@programming-best-practices
```

### Skills (Auto-Invoked)
- **best-practices** — Claude automatically references style guides when writing or reviewing code in 30+ languages
- **security-review** — Claude applies OWASP/security checklists during security-related code review

### Slash Commands
- `/programming-best-practices:best-practices [language]` — Look up best practices for any language
- `/programming-best-practices:review-code` — Review current code against industry standards
- `/programming-best-practices:setup-standards [stack]` — Generate linter/formatter configs for your stack

## 🎯 Coverage Areas

### Backend Development
- **Systems Programming**: C, C++, Rust
- **JVM Languages**: Java, Kotlin, Scala, C#
- **Web Backend**: Node.js, Python, Ruby, Rails, PHP, Laravel, NestJS
- **Functional/Specialized**: Elixir, Go, Swift, Objective-C, Perl, Lua

### Frontend Development
- **Core**: HTML, CSS, SASS, JavaScript, TypeScript
- **Frameworks**: React, Vue, Angular, Next.js, Nuxt

### Database & Data
- **SQL**: PostgreSQL, MySQL, General SQL
- **NoSQL**: MongoDB, General NoSQL patterns

### DevOps & Infrastructure
- **Cloud**: AWS, Cloud-Native patterns
- **Security**: API Security, DevSecOps, OWASP

### AI & Data Science
- **MLOps**: Machine learning operations best practices
- **AI Tools**: Developer productivity with AI

### Development Tools
- **Collaboration**: Code review, team practices
- **Scripting**: Bash automation
- **Architecture**: System design, scalability

## 📖 How to Use This Knowledge Base

When referencing this repository:

1. **For Style Questions**: Navigate to the specific language section in README.md
2. **For Architecture Guidance**: Check System Design and Performance sections
3. **For Security Reviews**: Reference the DevSecOps and API Security sections
4. **For Code Reviews**: Use the featured resources as quality benchmarks

## 🔗 Key Resources by Language

### JavaScript/TypeScript
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- [Clean Code JavaScript](https://github.com/ryanmcdermott/clean-code-javascript)

### Python
- [Best of the Best Practices (BOBP) Guide](https://gist.github.com/sloria/7001839)
- [Design Patterns in Python](https://refactoring.guru/design-patterns/python)

### Go
- [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)
- [Design Patterns in Go](https://refactoring.guru/design-patterns/go)

### Ruby
- [Ruby Style Guide (Airbnb)](https://github.com/airbnb/ruby)
- [Ruby Style Guide (bbatsov)](https://github.com/bbatsov/ruby-style-guide)

### System Design
- [System Design 101](https://github.com/ByteByteGoHq/system-design-101)
- [The Twelve-Factor App](https://12factor.net/)

## 🛠️ Using with AI Coding Assistants

This repository is optimized for use with AI coding editors. When working on a project:

1. **Reference for Code Reviews**: Ask the AI to check code against relevant style guides
2. **Architecture Decisions**: Use as reference for design pattern selection
3. **Learning Resources**: Direct developers to specific sections for upskilling
4. **Team Standards**: Establish coding conventions based on curated resources

## 📋 Quick Reference Commands

When asking about best practices:
- "What are the JavaScript best practices?" → See JavaScript section
- "How should I structure my Go code?" → See Go section + Uber Style Guide
- "What security practices should I follow?" → See API Security and DevSecOps sections
- "How to design scalable systems?" → See System Design section + 12 Factor App

## 📂 Crawled Content

If the `content/` directory exists, it contains **locally crawled versions** of all external resources:

```
content/
├── index.json              # Master index of all resources
├── metadata.yaml           # Crawl statistics
├── backend_development/    # Categorized content
├── frontend_development/
└── ...
```

### Using Crawled Content

1. **Search by category**: Check subdirectories matching the topic
2. **Read index.json**: Find resources by title, URL, or category
3. **Load summaries**: Check `summaries/` for condensed overviews

### Summaries Directory

If crawling has been run with `generate_summaries.py`:

```
summaries/
├── SUMMARY.md              # Master overview
├── backend_development.md  # Category summaries
├── frontend_development.md
└── ...
```

These summaries are optimized for quick AI context loading.

## 🔄 Keeping Content Updated

```bash
# Re-crawl all content
cd scripts/crawler
python crawl.py --update

# Regenerate summaries
python generate_summaries.py
```
