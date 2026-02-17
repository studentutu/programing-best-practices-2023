<h1 align="center">🌟 Programming Best Practices</h1>

<p align="center">
    <strong>Your comprehensive guide to writing better code across 30+ languages and frameworks</strong>
</p>
<p align="center">
    <em>Curated resources from industry leaders • Production-ready practices • Always updated</em>
</p>

<div align="center">
    <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome Badge"/>
    <img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=flat&color=BC4E99" alt="Star Badge"/>
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/dereknguyen269/programing-best-practices" />
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/dereknguyen269/programing-best-practices" />
    <img alt="Github license" src="https://img.shields.io/github/license/dereknguyen269/programing-best-practices" />
</div>

<div align="center">
    <h3>🔗 Quick Links</h3>
    <a href="#-backend-development">Backend</a> •
    <a href="#-frontend-development">Frontend</a> •
    <a href="#️-database--data">Database</a> •
    <a href="#-mobile-development">Mobile</a> •
    <a href="#️-devops--infrastructure">DevOps</a> •
    <a href="#-ai--data-science">AI/ML</a> •
    <a href="#️-development-tools--practices">Tools</a> •
    <a href="#-featured-resources">Featured</a>
</div>


---

## 📖 Introduction

This repository is a **curated collection of programming best practices** across multiple languages, frameworks, and tools.

It is not an exhaustive list but rather a practical resource containing articles, guidelines, and style guides that have proven helpful in real-world development.

The focus is primarily on **Web Development** (Ruby, Rails, JavaScript, etc.), but it also covers **databases, DevOps, cloud practices, AI tools, and career growth**.

With this collection, I hope to support developers in writing **cleaner, more maintainable code** and growing in their careers.

**Status:** 🚧 *Work in Progress — continuously updated*

---

## 🎯 Why This Repository?

✨ **Curated Quality** — Hand-picked resources from industry leaders and experienced developers  
🚀 **Production-Ready** — Practices that work in real-world applications, not just theory  
🌍 **Multi-Language** — Covers 30+ programming languages and frameworks  
📚 **Comprehensive** — From code style to architecture, security to performance  
🔄 **Always Updated** — Regularly maintained with the latest best practices  
💡 **Community-Driven** — Open to contributions from developers worldwide  

---

## 🚀 Quick Start Setup

### 🎯 Automated Setup (Recommended)

The fastest way to get started is using our automated setup script:

```bash
# Clone the repository
git clone https://github.com/dereknguyen269/programing-best-practices.git
cd programing-best-practices

# Run the interactive setup script
./scripts/quick-start.sh
```

The script will guide you through different setup options:

| Mode | Time | What's Included |
|------|------|-----------------|
| **Minimal** | ~1 min | Dependencies only, no crawling |
| **Test** | ~2-3 min | Dependencies + 20 sample resources |
| **Full** | ~10-15 min | Everything + all 150+ resources + AI summaries |
| **Custom** | Varies | Choose specific categories to crawl |

**Quick Options:**

```bash
# Minimal setup (just dependencies)
./scripts/quick-start.sh --minimal

# Full setup (everything)
./scripts/quick-start.sh --full

# Test with 20 resources
./scripts/quick-start.sh --limit 20

# Crawl only Python resources
./scripts/quick-start.sh --category python
```

📖 **For detailed documentation and troubleshooting**, see the [Quick Start Guide](./docs/QUICK_START_GUIDE.md)


---

### 📋 Manual Setup (Alternative)

Prefer to set up manually? Follow these steps:

#### Step 1: Clone the Repository

```bash
git clone https://github.com/dereknguyen269/programing-best-practices.git
cd programing-best-practices
```

#### Step 2: Install Crawler Dependencies (Optional but Recommended)

The crawler downloads all external resources locally for offline access:

```bash
# Create virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r scripts/crawler/requirements.txt
```

#### Step 3: Crawl Resources (Optional)

Download all best practices content locally:

> **Note**: Make sure your virtual environment is activated before running these commands:
> ```bash
> source .venv/bin/activate  # On Windows: .venv\Scripts\activate
> ```
> 
> Or use the venv Python directly: `.venv/bin/python3` instead of `python3`

```bash
# Crawl all resources (~150+ links, takes 10-15 minutes)
python3 scripts/crawler/crawl.py

# Or crawl specific categories
python3 scripts/crawler/crawl.py --category python
python3 scripts/crawler/crawl.py --category javascript

# Or crawl a limited number for testing
python3 scripts/crawler/crawl.py --limit 20

# Update existing content
python3 scripts/crawler/crawl.py --update
```

#### Step 4: Generate AI Summaries (Optional)

Create condensed summaries optimized for AI assistants:

```bash
python3 scripts/crawler/generate_summaries.py
```

#### Step 5: Use with Your AI Coding Editor

The repository is now ready! Your AI coding editor will automatically detect:

| AI Editor | Config File | Auto-Detected |
|-----------|-------------|---------------|
| **Claude Code** | `CLAUDE.md` | ✅ |
| **Kiro** | `.kiro/project.md` | ✅ |
| **Antigravity** | `.agent/instructions.md` | ✅ |
| **Cursor** | `.cursorrules` | ✅ |
| **Windsurf** | `.windsurfrules` | ✅ |

---

## 📁 Repository Structure

After setup, your repository will look like:

```
programing-best-practices/
├── README.md                   # Main knowledge base (curated links)
├── CLAUDE.md                   # Claude Code instructions
├── AGENTS.md                   # Universal AI agent instructions
├── .claude-plugin/             # 🔌 Claude Code plugin manifest
│   └── plugin.json
├── skills/                     # 🧠 Claude Code auto-invoked skills
│   ├── best-practices/         # Language & framework best practices
│   │   └── SKILL.md
│   └── security-review/        # Security audit skill
│       └── SKILL.md
├── commands/                   # ⚡ Claude Code slash commands
│   ├── best-practices.md       # /best-practices [language]
│   ├── review-code.md          # /review-code
│   └── setup-standards.md      # /setup-standards [stack]
├── .agent/                     # Antigravity config
│   ├── config.json
│   └── instructions.md
├── .kiro/                      # Kiro config
│   └── project.md
├── .cursorrules                # Cursor AI rules
├── .windsurfrules              # Windsurf AI rules
├── content/                    # � Crawled content (after running crawler)
│   ├── index.json              # Master index of all resources
│   ├── metadata.yaml           # Crawl statistics
│   ├── backend_development/    # Content organized by category
│   ├── frontend_development/
│   └── ...
├── summaries/                  # 📝 AI-ready summaries (after generate_summaries.py)
│   ├── SUMMARY.md              # Master overview
│   └── [category].md           # Category summaries
├── scripts/
│   ├── crawler/                # 🕷️ Crawler tools
│   │   ├── crawl.py            # Main crawler
│   │   ├── search.py           # Search tool
│   │   ├── generate_summaries.py
│   │   └── requirements.txt
│   └── setup-kb.sh             # Quick setup script
├── templates/                  # 📋 Templates for your projects
│   ├── CLAUDE.template.md
│   ├── agent/
│   ├── kiro/
│   └── cursorrules.template
└── docs/
    └── INTEGRATION.md          # Integration guide
```

---

## 🔍 Searching the Knowledge Base

After crawling, you can search locally:

```bash
# Search for JavaScript content
python3 scripts/crawler/search.py "javascript style guide"

# Search within a specific category
python3 scripts/crawler/search.py "best practices" --category python

# Get results as JSON
python3 scripts/crawler/search.py "security" --json
```

---

## 📚 How to Use This Repository

### For Beginners
1. **Start with your primary language** — Navigate to your language section in the Table of Contents
2. **Read style guides first** — Understanding code style is fundamental
3. **Practice with examples** — Apply the practices in your own projects
4. **Bookmark for reference** — Keep this as a go-to resource when coding

### For Experienced Developers
1. **Explore new languages** — Learn best practices before starting a new tech stack
2. **Code review reference** — Use during code reviews to maintain quality standards
3. **Team onboarding** — Share relevant sections with new team members
4. **Stay updated** — Check back regularly for new resources and practices

### For Team Leads
1. **Establish standards** — Use these guides to create team coding standards
2. **Training resource** — Assign relevant sections for team learning
3. **Quality benchmarks** — Set expectations for code quality
4. **Architecture decisions** — Reference system design and scalability sections

---

## 🤖 Use for Existing Projects

Want to integrate this knowledge base into your existing project? We provide multiple options:

### Option 1: Quick Setup Script

```bash
# Run the setup script in your project directory
curl -sSL https://raw.githubusercontent.com/dereknguyen269/programing-best-practices/main/scripts/setup-kb.sh | bash
```

### Option 2: Git Submodule

```bash
# Add as a submodule in your project
cd your-project
git submodule add https://github.com/dereknguyen269/programing-best-practices.git .kb/best-practices
```

### Option 3: Copy Templates

Download the templates from the [`/templates`](./templates) directory and customize for your project:

| Template | Copy To | Purpose |
|----------|---------|---------|
| `CLAUDE.template.md` | `CLAUDE.md` | Claude Code |
| `agent/instructions.template.md` | `.agent/instructions.md` | Antigravity |
| `agent/config.template.json` | `.agent/config.json` | Antigravity |
| `kiro/project.template.md` | `.kiro/project.md` | Kiro |
| `cursorrules.template` | `.cursorrules` | Cursor |

📖 **Full integration guide**: See [`docs/INTEGRATION.md`](./docs/INTEGRATION.md)

### Option 4: Claude Code Plugin (Recommended for Claude Code users)

Install directly as a Claude Code plugin for automatic best practices guidance:

```bash
# Install the plugin
/plugin install dereknguyen269/programing-best-practices
```

Once installed, you get:

| Feature | How to Use |
|---------|-----------|
| Auto best practices | Claude automatically references style guides when you write code |
| Security reviews | Claude applies OWASP/security checklists during code review |
| `/programming-best-practices:best-practices [language]` | Look up best practices for any language |
| `/programming-best-practices:review-code` | Review current code against industry standards |
| `/programming-best-practices:setup-standards [stack]` | Generate linter/formatter configs for your stack |

The plugin includes two skills that Claude invokes automatically:
- **best-practices** — Activated when writing or reviewing code in any of 30+ languages
- **security-review** — Activated when reviewing code for vulnerabilities or security concerns

---

## ⭐ Featured Resources

Here are some standout resources that every developer should know:

### 🏆 Must-Read Guides
- **[Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)** — The gold standard for JavaScript coding
- **[Clean Code JavaScript](https://github.com/ryanmcdermott/clean-code-javascript)** — Software engineering principles for JavaScript
- **[System Design 101](https://github.com/ByteByteGoHq/system-design-101)** — Essential system design concepts
- **[The Twelve-Factor App](https://12factor.net/)** — Methodology for building modern cloud-native apps
- **[OWASP Top 10](https://owasp.org/www-project-top-ten/)** — Critical security awareness for developers

### 🎨 Design Patterns
- **[Design Patterns in Python](https://refactoring.guru/design-patterns/python)** — Comprehensive pattern guide
- **[Design Patterns in Go](https://refactoring.guru/design-patterns/go)** — Go-specific implementations
- **[Design Patterns in Swift](https://github.com/ochococo/Design-Patterns-In-Swift)** — Swift pattern examples

### 🔧 Language-Specific Gems
- **[Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)** — Production-grade Go practices
- **[Ruby Style Guide](https://github.com/bbatsov/ruby-style-guide)** — Community-driven Ruby standards
- **[Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html)** — Google's web standards

---

## 📂 Table of Contents

### 🔹 Backend Development

#### Systems Programming
* [C](#c-best-practices)
* [C++](#c-best-practices-1)
* [Rust](#rust-best-practices)

#### Enterprise & JVM Languages
* [Java](#java-best-practices)
* [Kotlin](#kotlin-best-practices)
* [Scala](#scala-best-practices)
* [C#](#c-best-practices-2)

#### Web Backend
* [Node.js](#nodejs-best-practices)
* [Python](#python-best-practices)
* [Ruby](#ruby-best-practices)
* [Rails](#rails-best-practices)
* [PHP](#php-best-practices)
* [Laravel](#laravel-best-practices)
* [NestJS](#nestjs-best-practices)

#### Functional & Specialized
* [Elixir](#elixir-best-practices)
* [Go](#go-golang-best-practices)
* [Swift](#swift-best-practices)
* [Objective-C](#objective-c-best-practices)
* [Perl](#perl-best-practices)
* [Lua](#lua-best-practices)

### 🔹 Frontend Development

#### Core Technologies
* [HTML](#html-best-practices)
* [CSS](#css-best-practices)
* [SASS](#sass-best-practices)
* [JavaScript](#javascript-best-practices)
* [TypeScript](#typescript-best-practices)

#### Frameworks & Libraries
* [React](#reactjs-best-practices)
* [React Native](#react-native-best-practices)
* [Vue](#vue-best-practices)
* [Angular](#angular-best-practices)
* [Next.js](#nextjs-best-practices)
* [Nuxt](#nuxt-best-practices)

#### Performance
* [Frontend Performance](#frontend-performance-best-practices)

### 🔹 Database & Data

#### SQL Databases
* [SQL](#sql-best-practices)
* [PostgreSQL](#postgresql-best-practices)
* [MySQL](#mysql-best-practices)

#### NoSQL & Big Data
* [NoSQL](#nosql-best-practices)

### 🔹 Mobile Development
* [Flutter](#flutter-best-practices)
* [Dart](#dart-best-practices)
* [React Native](#react-native-best-practices)

### 🔹 DevOps & Infrastructure

#### Cloud & Deployment
* [AWS](#aws-best-practices)
* [Microservices & Cloud-Native](#microservices--cloud-native-best-practices)

#### Security
* [API Security](#api-security-best-practices)
* [DevSecOps](#devsecops--security-best-practices)

### 🔹 AI & Data Science
* [AI/ML Engineering](#aiml-engineering-best-practices)
* [AI Tools for Developers](#ai-tools-for-developers)

### 🔹 Development Tools & Practices

#### Version Control & Collaboration
* [Code Review](#code-review-best-practices)
* [Team Collaboration](#team--collaboration-best-practices)

#### Scripting & Automation
* [Bash](#bash-script-best-practices)

#### Performance & Architecture
* [System Design](#system-design-best-practices)
* [Performance & Scalability](#performance--scalability-best-practices)

### 🔹 Specialized Languages
* [R](#r-best-practices)

---

# 🔹 Backend Development

## Systems Programming

### 🖥️ C Best Practices

* [C Programming Best Practices – Must know to become an Expert](https://data-flair.training/blogs/c-programming-best-practices/)
* [c-style](https://github.com/mcinglis/c-style) — *@mcinglis*

---

### 🖥️ C++ Best Practices

* [3 Coding Best Practices for C++](https://www.perforce.com/blog/qac/3-coding-best-practices-cpp)
* [Collaborative Collection of C++ Best Practices](https://github.com/lefticus/cppbestpractices) — *@lefticus*
* [The C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines) — *@isocpp*
* [C++ Best Practices (CppCon)](https://cppcon.org/cpp-best-practices/)
* [C++ Best Practices by Puppet Labs](https://github.com/puppetlabs/cppbestpractices) — *@puppetlabs*
* [Modern C++ Exception Handling](https://docs.microsoft.com/en-us/cpp/cpp/errors-and-exception-handling-modern-cpp) — *Microsoft*
* [Top Ten Tips for Correct C++ Coding](https://www.informit.com/articles/article.aspx?p=1712962)

---

### 🦀 Rust Best Practices

* [Rust Style Guide](https://github.com/ubsan/style/blob/master/guide.md) — *@ubsan*
* [Rust Design Patterns](https://rust-unofficial.github.io/patterns/)
* [Design Patterns in Rust](https://refactoring.guru/design-patterns/rust) — *Refactoring.Guru*

---

## Enterprise & JVM Languages

### ☕ Java Best Practices

* [Java Best Practices](https://github.com/in28minutes/java-best-practices) — *@in28minutes*
* [Selenium Best Practices](https://github.com/previousdeveloper/Selenium-best-practices) — *@previousdeveloper*
* [Java Style Guide (Ray Wenderlich)](https://github.com/raywenderlich/java-style-guide) — *@raywenderlich*
* [Java Best Practices Guide](https://howtodoinjava.com/java-best-practices/)
* [30 Java Programming Tips for Beginners](https://www.javacodegeeks.com/2015/06/java-programming-tips-best-practices-beginners.html)

---

### 🌀 Kotlin Best Practices

* [Best Practices in Kotlin](https://github.com/JackyAndroid/kotlin-best-practices) — *@JackyAndroid*
* [Kotlin Style Guide](https://github.com/yole/kotlin-style-guide) — *@yole*
* [Kotlin Style Guide (Ray Wenderlich)](https://github.com/raywenderlich/kotlin-style-guide) — *@raywenderlich*

---

### 🌀 Scala Best Practices

* [Scala Best Practices](https://github.com/alexandru/scala-best-practices) — *@alexandru*
* [Databricks Scala Guide](https://github.com/databricks/scala-style-guide) — *@databricks*

---

### 🖥️ C# Best Practices

* [C# Coding Best Practices – Conventions with Examples](https://www.freecodecamp.org/news/coding-best-practices-in-c-sharp/)
* [22 C# Best Practices](https://code-maze.com/csharp-22-best-practices/)

---

## Web Backend

### 🟢 Node.js Best Practices

* [Node.js Style Guide](https://github.com/felixge/node-style-guide) — *@felixge*
* [RisingStack Node.js Style Guide](https://github.com/RisingStack/node-style-guide) — *@RisingStack*

---

### 🐍 Python Best Practices

* [Python Best Practices – Become an Expert](https://data-flair.training/blogs/python-best-practices/)
* [Best of the Best Practices (BOBP) Guide](https://gist.github.com/sloria/7001839) — *@sloria*
* [Python Best Practices (Toptal)](https://www.toptal.com/python/tips-and-practices)
* [Python Code Style Guide](https://docs.python-guide.org/writing/style/)
* [11 Tips to Write Better Python Code](https://www.python-engineer.com/posts/11-tips-to-write-better-python-code/)
* [Python Tutorial: Best Practices & Mistakes](https://jaxenter.com/python-tutorial-best-practices-145959.html)
* [Design Patterns in Python](https://refactoring.guru/design-patterns/python) — *Refactoring.Guru*

---

### 💎 Ruby Best Practices

* [Ruby Style Guide](https://github.com/airbnb/ruby) — *@airbnb*
* [Ruby Tricks & Best Practices](https://github.com/franzejr/best-ruby) — *@franzejr*
* [Best Practice Patterns in Ruby](https://github.com/avdi/sbpprb) — *@avdi*
* [Ruby Best Practices (Gregory Brown)](https://github.com/practicingruby/rbp-book) — *@practicingruby*
* [The Ruby Style Guide](https://github.com/bbatsov/ruby-style-guide) — *@bbatsov*
* [Shopify Ruby Style Guide](https://github.com/Shopify/ruby-style-guide) — *@Shopify*
* [53 Ruby on Rails Interview Questions](https://medium.com/ruby-daily/53-ruby-on-rails-interview-questions-and-answers-eb99eed1aeb7)
* [Ruby Best Practices (Toptal)](https://www.toptal.com/ruby/tips-and-practices)
* [Ruby Best Practices for Beginners](https://deepsource.io/blog/ruby-dev-best-practices-for-beginners/)
* [Ruby Timeouts Guide](https://github.com/ankane/the-ultimate-guide-to-ruby-timeouts) — *@ankane*
* [Design Patterns in Ruby](https://refactoring.guru/design-patterns/ruby) — *Refactoring.Guru*
* [Best Practices for Writing Ruby](https://reintech.io/blog/best-practices-for-writing-ruby)
* [6 Ruby Best Practices for Beginners](https://www.codementor.io/ruby-on-rails/tutorial/6-ruby-best-practices-beginners-should-know)

---

### 🚂 Rails Best Practices

* [Rails Style Guide](https://github.com/bbatsov/rails-style-guide) — *@bbatsov*
* [rails_best_practices](https://github.com/flyerhzm/rails_best_practices) — *@flyerhzm*
* [RSpec Style Guide](https://github.com/reachlocal/rspec-style-guide) — *@reachlocal*
* [RSpec Best Practices](https://github.com/abinoda/rspec-best-practices) — *@abinoda*
* [Rails Database Best Practices](https://blog.carbonfive.com/rails-database-best-practices/)
* [Active Record Query Optimization Tips](https://medium.com/@User3141592/active-record-query-performance-tips-a3c3947b968)
* [ActiveRecord SQL Query Optimization](https://phrase.com/blog/posts/activerecord-speed-up-your-sql-queries/)
* [Arel Cheatsheet](https://devhints.io/arel)
* [Production Rails](https://github.com/ankane/production_rails) — *@ankane*
* [Securing Sensitive Data in Rails](https://ankane.org/sensitive-data-rails) — *@ankane*
* [Toptal Rails Best Practices](https://www.toptal.com/ruby-on-rails/tips-and-practices)

---

### 🐘 PHP Best Practices

* [PHP: The Right Way](https://github.com/codeguy/php-the-right-way) — *@codeguy*
* [PHP Knowledge](https://github.com/php-earth/php-knowledge) — *@php-earth*
* [PHP Coding Standards](https://github.com/maxdmyers/php-style-guide) — *@maxdmyers*

---

### 🎯 Laravel Best Practices

* [Laravel: The Right Way](https://github.com/laraveltherightway/laraveltherightway.github.io) — *@laraveltherightway*
* [Laravel Best Practices](https://github.com/uonick/laravel-best-practices) — *@uonick*

---

### 🟣 NestJS Best Practices

* [Best NestJS Practices and Advanced Techniques](https://dev.to/drbenzene/best-nestjs-practices-and-advanced-techniques-9m0)

---

## Functional & Specialized

### 🧪 Elixir Best Practices

* [The Elixir Style Guide](https://github.com/christopheradams/elixir_style_guide) — *@christopheradams*
* [Elixir Style Guide](https://github.com/lexmag/elixir-style-guide) — *@lexmag*
* [Credo's Elixir Style Guide](https://github.com/rrrene/elixir-style-guide) — *@rrrene*
* [10 Killer Elixir Tips #1](https://medium.com/blackode/10-killer-elixir-tips-2a9be1bec9be)
* [10 Killer Elixir Tips #2](https://medium.com/blackode/10-killer-elixir-tips-2-c5f87f8a70c8)
* [10 Killer Elixir Tips #3](https://medium.com/blackode/10-killer-elixir-tips-3-5c196eaec376)
* [Elixir Cheatsheet](https://devhints.io/elixir)
* [Elixir Metaprogramming Cheatsheet](https://devhints.io/elixir-metaprogramming)

---

### 🐹 Go (Golang) Best Practices

* [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md) — *@uber-go*
* [Go Best Practices](https://github.com/mehrdadrad/GoBestPractices) — *@mehrdadrad*
* [Go Style Guide](https://github.com/AgtLucas/go-style-guide) — *@AgtLucas*
* [Golang Tutorial Series](https://golangbot.com/learn-golang-series/)
* [Golang Cheat Sheet (Golang Dojo)](https://products.golangdojo.com/golang-cheat-sheet-by-golang-dojo)
* [Soham Kamani – Golang](https://www.sohamkamani.com/golang/)
* [Design Patterns in Go](https://refactoring.guru/design-patterns/go) — *Refactoring.Guru*

---

### 🍎 Swift Best Practices

* [Swift Style Guide (Eure)](https://github.com/eure/swift-style-guide) — *@eure*
* [Design Patterns in Swift](https://github.com/ochococo/Design-Patterns-In-Swift) — *@ochococo*
* [Swift Style Guide (Ray Wenderlich)](https://github.com/raywenderlich/swift-style-guide) — *@raywenderlich*

---

### 🍏 Objective-C Best Practices

* [NYTimes Objective-C Style Guide](https://github.com/NYTimes/objective-c-style-guide) — *@NYTimes*
* [Objective-C Style Guide (Ray Wenderlich)](https://github.com/raywenderlich/objective-c-style-guide) — *@raywenderlich*
* [GitHub Objective-C Style Guide](https://github.com/github/objective-c-style-guide) — *@github*
* [Code Style & Best Practices for Objective-C](https://github.com/wangshengjia/-Code-Style---Best-Practise-for-Objective-C) — *@wangshengjia*

---

### 🐪 Perl Best Practices

* [Effective Perl Programming: Idiomatic Perl](https://www.effectiveperlprogramming.com/)
* [Perl Style Guide](https://perldoc.perl.org/perlstyle) — *Perl.org*

---

### 🪶 Lua Best Practices

* [Lua Best Practices (Lua.org)](https://www.lua.org/gems/sample.pdf)
* [Lua Style Guide](http://lua-users.org/wiki/LuaStyleGuide)

---

# 🎨 Frontend Development

## Core Technologies

### 🌐 HTML Best Practices

* [HTML Best Practices](https://github.com/hail2u/html-best-practices) — *@hail2u*
* [HTML5 (and Some CSS) Best Practice](https://www.codeproject.com/Tips/666578/HTML-and-Some-CSS-Best-Practice)
* [Frontend Guidelines](https://github.com/bendc/frontend-guidelines) — *@bendc*
* [Google HTML Style Guide](https://google.github.io/styleguide/htmlcssguide.html#HTML) — *@google*

---

### 🎨 CSS Best Practices

* [Airbnb CSS / Sass Styleguide](https://github.com/airbnb/css) — *@airbnb*
* [Dropbox (S)CSS Style Guide](https://github.com/dropbox/css-style-guide) — *@dropbox*
* [CSS Coding Standards & Best Practices](https://github.com/stevekwan/best-practices/blob/master/css/best-practices.md) — *@stevekwan*
* [Google CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#CSS) — *@google*

---

### 🎨 SASS Best Practices

* [Sass Coding Guidelines](https://github.com/bigcommerce/sass-style-guide) — *@bigcommerce*
* [Sass-Guidelines](https://github.com/blackfalcon/Sass-Guidlines/blob/master/SASS-Guidelines.md) — *@blackfalcon*
* [Sass-lang Style Rules](https://sass-lang.com/documentation/style-rules)

---

### 📜 JavaScript Best Practices

* [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) — *@airbnb*
* [ES6 Cheatsheet](https://github.com/DrkSephy/es6-cheatsheet) — *@DrkSephy*
* [Common JavaScript "Gotchas"](https://github.com/stevekwan/best-practices/blob/master/javascript/gotchas.md) — *@stevekwan*
* [Pragmatic JavaScript Standards](https://github.com/stevekwan/best-practices/blob/master/javascript/best-practices.md) — *@stevekwan*
* [JavaScript 规范](https://github.com/adamlu/javascript-style-guide) — *@adamlu*
* [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html) — *@google*
* [JavaScript The Right Way](https://jstherightway.org/) — *@braziljs*
* [MDN JavaScript Guidelines](https://developer.mozilla.org/en-US/docs/MDN/Guidelines/Code_guidelines/JavaScript) — *@mozilla*
* [W3C JavaScript Best Practices](https://www.w3.org/wiki/JavaScript_best_practices) — *@w3c*
* [Clean Code JavaScript](https://github.com/ryanmcdermott/clean-code-javascript) — *@ryanmcdermott*

---

### 🟦 TypeScript Best Practices

* [TypeScript Best Practices](https://github.com/BestCoderDotInfo/TypeScript-best-practices) — *@BestCoderDotInfo*

---

## Frameworks & Libraries

### ⚛️ ReactJS Best Practices

* [Advanced ReactJS Patterns](https://github.com/kentcdodds/advanced-react-patterns-v2) — *@kentcdodds*
* [React Interview Questions & Answers](https://github.com/sudheerj/reactjs-interview-questions) — *@sudheerj*

---

### 📱 React Native Best Practices

* [React Native Guide](https://github.com/reactnativecn/react-native-guide) — *@reactnativecn*

---

### 🖼️ Vue Best Practices

* [Tips & Best Practices (Vue 0.12)](https://012.vuejs.org/guide/best-practices.html)
* [10 Good Practices for Large Vue.js Projects](https://www.telerik.com/blogs/10-good-practices-building-maintaining-large-vuejs-projects)
* [12 VueJS Best Practices for Pro Developers](https://learnvue.co/2020/01/12-vuejs-best-practices-for-pro-developers/)

---

### 🅰️ Angular Best Practices

* [AngularJS Style Guide](https://github.com/mgechev/angularjs-style-guide) — *@mgechev*
* [Angular 2 Style Guide](https://github.com/mgechev/angular2-style-guide) — *@mgechev*
* [Angular.js Advanced Design Patterns](https://github.com/trochette/Angular-Design-Patterns-Best-Practices) — *@trochette*

---

### ⚡ Next.js Best Practices

* [Best Practices for Clean React/Next.js Projects](https://blogs.perficient.com/2023/04/25/best-practices-for-building-and-sustaining-a-clean-react-next-js-project/)
* [10 Tips for Optimal Next.js Performance](https://www.fronttribe.com/stories/next-js-best-practices-10-tips-for-optimal-performance)
* [Best Practices to Increase Next.js Speed](https://stackoverflow.blog/2022/12/20/best-practices-to-increase-the-speed-for-next-js-apps/)

---

### ⚡ Nuxt Best Practices

* [10 Nuxt Best Practices](https://climbtheladder.com/10-nuxt-best-practices/)

---

## Performance

### 🚀 Frontend Performance Best Practices

* [Frontend Performance Best Practices (Roadmap.sh)](https://roadmap.sh/best-practices/frontend-performance)
* [Web Vitals Best Practices (Google)](https://web.dev/vitals/)
* [High Performance Web Apps (MDN)](https://developer.mozilla.org/en-US/docs/Learn/Performance)

---

# 🗄️ Database & Data

## SQL Databases

### 📊 SQL Best Practices

* [SQL Style Guide](https://www.sqlstyle.guide)
* [Best Practices for Writing SQL Queries](https://www.metabase.com/learn/sql-questions/sql-best-practices)
* [SQL Performance Explained (Markus Winand)](https://use-the-index-luke.com/)
* [GitLab SQL Style Guide](https://about.gitlab.com/handbook/business-technology/data-team/platform/sql-style-guide/)

---

### 🐘 PostgreSQL Best Practices

* [PostgreSQL Performance Best Practices](https://www.adservio.fr/post/postgresql-performance-best-practices)
* [Best Practices for PostgreSQL Database](https://www.e2enetworks.com/blog/best-practices-for-postgresql-database)
* [Run ANALYZE, Run ANALYZE, Run ANALYZE](https://ottertune.com/blog/run-postgresql-analyze-to-fix-a-slowdow-in-db/)
* [Best Practices for Designing PostgreSQL Databases](https://appmaster.io/blog/best-practices-for-designing-postgresql-databases)

---

### 🐬 MySQL Best Practices

* [MySQL Performance Best Practices](https://dev.mysql.com/doc/refman/8.0/en/optimization.html)
* [MySQL Security Best Practices](https://dev.mysql.com/doc/refman/8.0/en/security-guidelines.html)

---

## NoSQL & Big Data

### 📦 NoSQL Best Practices

* [10 NoSQL Data Modeling Best Practices](https://climbtheladder.com/10-nosql-data-modeling-best-practices/)
* [MongoDB Schema Design Best Practices](https://www.mongodb.com/developer/products/mongodb/mongodb-schema-design-best-practices/)
* [11 MongoDB Security Features & Best Practices](https://satoricyber.com/mongodb-security/11-mongodb-security-features-and-best-practices/)

---

# 📱 Mobile Development

## 📱 Flutter Best Practices

* [Performance Best Practices](https://flutter.dev/docs/perf/rendering/best-practices)
* [Flutter: Best Practices and Tips](https://medium.com/flutter-community/flutter-best-practices-and-tips-7c2782c9ebb5) — *Kinjal Dhamat*
* [Flutter Development Best Practices](https://heartbeat.fritz.ai/flutter-development-best-practices-3e162765340a) — *Derrick Mwiti*

---

## 🎯 Dart Best Practices

* [Dart & Flutter Best Practices](https://lazebny.io/flutter-best-practices/)
* [Performance Best Practices](https://docs.flutter.dev/perf/best-practices)
* [Writing Clean Code in Dart: Best Practices & Design Patterns](https://clouddevs.com/dart/clean-code/)

---

# ☁️ DevOps & Infrastructure

## Cloud & Deployment

### ☁️ AWS Best Practices

* [AWS Best Practices (Roadmap.sh)](https://roadmap.sh/best-practices/aws)
* [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)

---

### 📦 Microservices & Cloud-Native Best Practices

* [12 Factors for Building Cloud-Native Apps](https://12factor.net/)
* [Microservices Best Practices (Microsoft)](https://learn.microsoft.com/en-us/azure/architecture/microservices/)
* [Cloud-Native Patterns (CNCF)](https://github.com/cncf/presentations)

---

## Security

### 🔐 API Security Best Practices

* [API Security Best Practices (Roadmap.sh)](https://roadmap.sh/best-practices/api-security)
* [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist)

---

### 🔐 DevSecOps & Security Best Practices

* [OWASP Top 10 (2024)](https://owasp.org/www-project-top-ten/)
* [Zero Trust Security Model](https://www.microsoft.com/security/blog/zero-trust/)
* [Best Practices for Secure CI/CD](https://snyk.io/blog/devsecops-best-practices/)

---

# 🤖 AI & Data Science

## 🤖 AI/ML Engineering Best Practices

* [MLOps Best Practices (Google Cloud)](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)
* [Responsible AI Practices (Google)](https://ai.google/responsibilities/responsible-ai-practices/)
* [Best Practices for LLM Applications](https://www.promptingguide.ai/)
* [IBM Data Science – Best Practices](https://github.com/IBM/data-science-best-practices)
* [AI Best Practices (XenonStack Blog)](https://www.xenonstack.com/blog/ai-best-practices)
* [Best Practices for Deep Learning in Julia (FastAI.jl)](https://github.com/FluxML/FastAI.jl)
* [ETL Best Practices with Airflow](https://github.com/gtoonstra/etl-with-airflow)

---

## 🤖 AI Tools for Developers

* [9 of the Best AI Tools for Software Developers in 2024](https://www.stepsize.com/blog/best-ai-tools-for-software-developers)
* [The Best AI Tools for Developers in 2024](https://daily.dev/blog/the-best-ai-tools-for-developers-in-2024)
* [Awesome AI Tools](https://github.com/mahseema/awesome-ai-tools) — *@mahseema*
* [Awesome AI-Powered Developer Tools](https://github.com/jamesmurdza/awesome-ai-devtools) — *@jamesmurdza*
* [Best Practices for Coding with AI (2024)](https://blog.codacy.com/best-practices-for-coding-with-ai)
* [AI Tools for Developers: 5 Types of Tools & How to Choose](https://swimm.io/learn/ai-tools-for-developers/ai-tools-for-developers-5-types-of-tools-and-how-to-choose)
* [The Do's and Don'ts of Using AI in Software Development](https://www.kodeco.com/41989083-the-do-s-and-don-ts-of-using-ai-in-software-development)
* [10 Best Practices for Secure AI Development](https://snyk.io/blog/10-best-practices-for-securely-developing-with-ai/)
* [AI Hacks to Maximize Productivity in 2024](https://www.smarttrick.org/post/work-smarter-not-harder-ai-hacks-to-maximize-your-productivity-in-2024)

---

# 🛠️ Development Tools & Practices

## Version Control & Collaboration

### 🔎 Code Review Best Practices

* [Code Review Best Practices (Roadmap.sh)](https://roadmap.sh/best-practices/code-review)

---

### 🧑‍🤝‍🧑 Team & Collaboration Best Practices

* [Remote Engineering Best Practices](https://about.gitlab.com/remote/)
* [Agile Development Best Practices](https://www.atlassian.com/agile)
* [Effective Pair Programming](https://martinfowler.com/articles/on-pair-programming.html)

---

## Scripting & Automation

### 🐚 Bash Script Best Practices

* [Bash Best Practices](https://bertvv.github.io/cheat-sheets/Bash.html)
* [progrium/bashstyle](https://github.com/progrium/bashstyle)
* [Best Practices for Bash Scripts](https://hyperskill.org/learn/step/19230)
* [Best Practices for Writing Bash Scripts](https://expeditor.chef.io/docs/patterns/bash-scripts/)

---

## Performance & Architecture

### 🏗️ System Design Best Practices

* [System Design 101](https://github.com/ByteByteGoHq/system-design-101#system-design-101) — *@ByteByteGoHq*

---

### ⚡ Performance & Scalability Best Practices

* [Scaling Applications (Netflix Tech Blog)](https://netflixtechblog.com/)

---

# 🌍 Specialized Languages

## 📊 R Best Practices

* [Beyond Basic R – Introduction & Best Practices](https://waterdata.usgs.gov/blog/intro-best-practices/)
* [R Code – Best Practices](https://www.r-bloggers.com/r-code-best-practices/)
* [Best Practices for Writing R Code](https://swcarpentry.github.io/r-novice-inflammation/06-best-practices-R.html) — *@swcarpentry*
* [R Coding Style Best Practices](https://www.datanovia.com/en/blog/r-coding-style-best-practices/)
* [Good Practices in R Programming (ETH Zürich)](https://stat.ethz.ch/Teaching/maechler/R/useR_2014/Maechler-2014-pr.pdf)

---

# 🆕 What's New

Stay updated with the latest additions to this repository:

### Recent Updates
- ✅ **Enhanced README** — Added quick navigation, featured resources, and usage guides
- ✅ **AI/ML Section** — Expanded with LLM best practices and MLOps resources
- ✅ **Security Focus** — Added DevSecOps and API security best practices
- ✅ **Performance Guides** — New frontend performance and scalability resources
- ✅ **Modern Frameworks** — Added Next.js, Nuxt, and NestJS best practices

### Coming Soon
- 🔜 **Video Tutorials** — Curated video resources for visual learners
- 🔜 **Code Examples** — Practical code snippets demonstrating best practices
- 🔜 **Interactive Checklists** — Ready-to-use checklists for code reviews
- 🔜 **Language Comparison** — Side-by-side best practices across languages
- 🔜 **Community Picks** — Top-voted resources from contributors

---

# 🌟 Community & Support

## 💬 Get Involved

We believe in the power of community! Here's how you can participate:

### 🤝 Ways to Contribute
- **📝 Submit Resources** — Found a great article or guide? Share it!
- **🐛 Report Issues** — Broken links or outdated content? Let us know!
- **💡 Suggest Improvements** — Ideas for better organization or new sections?
- **⭐ Star the Repo** — Show your support and help others discover this resource
- **🔄 Share** — Spread the word on social media, blogs, or with your team

### 📢 Discussions
- **Questions?** Open a [GitHub Discussion](https://github.com/dereknguyen269/programing-best-practices/discussions)
- **Ideas?** Share your thoughts in the [Ideas category](https://github.com/dereknguyen269/programing-best-practices/discussions/categories/ideas)
- **Showcase** — Share how you're using these best practices in your projects

### 🏆 Contributors

A huge thank you to all our contributors! 🙏

<a href="https://github.com/dereknguyen269/programing-best-practices/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dereknguyen269/programing-best-practices" />
</a>

---

# 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=dereknguyen269/programing-best-practices&type=Date)](https://star-history.com/#dereknguyen269/programing-best-practices&Date)

---

# 💡 Related Resources

Looking for more? Check out these complementary resources:

- **[Awesome Lists](https://github.com/sindresorhus/awesome)** — Curated lists of awesome things
- **[Developer Roadmaps](https://roadmap.sh/)** — Step-by-step guides for different tech careers
- **[Free Programming Books](https://github.com/EbookFoundation/free-programming-books)** — Extensive collection of free learning resources
- **[Design Resources for Developers](https://github.com/bradtraversy/design-resources-for-developers)** — Design and UI resources
- **[The Book of Secret Knowledge](https://github.com/trimstray/the-book-of-secret-knowledge)** — Collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more

---

# 🎯 Repository Stats

<div align="center">
    <img src="https://img.shields.io/github/last-commit/dereknguyen269/programing-best-practices?style=for-the-badge" alt="Last Commit"/>
    <img src="https://img.shields.io/github/contributors/dereknguyen269/programing-best-practices?style=for-the-badge" alt="Contributors"/>
    <img src="https://img.shields.io/github/forks/dereknguyen269/programing-best-practices?style=for-the-badge" alt="Forks"/>
    <img src="https://img.shields.io/github/watchers/dereknguyen269/programing-best-practices?style=for-the-badge" alt="Watchers"/>
</div>

---

# 🤝 Contributing

Contributions are always welcome! 🎉
Before contributing, please read the [Contribution Guidelines](contributing.md).

---

# � Support This Project

If you find this repository helpful, here are some ways you can show your support:

### ⭐ Star This Repository
Click the ⭐ button at the top of this page — it helps others discover this resource!

### 🔄 Share With Others
- Share on [Twitter](https://twitter.com/intent/tweet?text=Check%20out%20this%20awesome%20collection%20of%20programming%20best%20practices!&url=https://github.com/dereknguyen269/programing-best-practices)
- Share on [LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/dereknguyen269/programing-best-practices)
- Share on [Reddit](https://reddit.com/submit?url=https://github.com/dereknguyen269/programing-best-practices&title=Programming%20Best%20Practices)
- Mention it in your blog posts or tech talks

### 🤝 Contribute
See our [Contributing Guidelines](contributing.md) to add your favorite resources!

### ☕ Sponsor
If this project has saved you time or helped your career, consider [sponsoring](https://github.com/sponsors/dereknguyen269) to support continued maintenance and updates.

---

# �📜 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
This project is licensed under **Creative Commons Zero v1.0 Universal (CC0 1.0)** — *Public Domain Dedication*.

---

# ❓ Frequently Asked Questions

### How often is this repository updated?
This repository is actively maintained and updated regularly. We add new resources as they emerge and remove outdated ones. Check the [What's New](#-whats-new) section for recent updates.

### Can I suggest a resource?
Absolutely! We welcome contributions. Please read our [Contributing Guidelines](contributing.md) and submit a pull request with your suggestions.

### Are these practices suitable for beginners?
Yes! We've organized resources for all skill levels. Beginners should start with the [How to Use](#-how-to-use-this-repository) section and focus on style guides first.

### How do I know which resources to prioritize?
Check out our [Featured Resources](#-featured-resources) section for must-read guides. Also, resources from well-known organizations (Google, Airbnb, etc.) are generally excellent starting points.

### Can I use this for my team?
Definitely! Many teams use this repository as a reference for establishing coding standards. Feel free to share relevant sections with your team or use them in onboarding materials.

### Is this repository language-specific?
No, we cover 30+ programming languages and frameworks. Use the [Table of Contents](#-table-of-contents) or [Quick Links](#-quick-links) to navigate to your preferred technology.

### How can I stay updated with new additions?
- ⭐ Star and Watch this repository on GitHub
- Check the [What's New](#-whats-new) section periodically
- Follow the repository for notifications

---

# 📜 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
This project is licensed under **Creative Commons Zero v1.0 Universal (CC0 1.0)** — *Public Domain Dedication*.

---

<div align="center">
    <p><strong>Made with ❤️ by developers, for developers</strong></p>
    <p>
        <a href="#-programming-best-practices">⬆ Back to Top</a>
    </p>
</div>
