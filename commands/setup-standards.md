---
description: Generate coding standards config files for your project's tech stack
---

Help set up coding standards for this project based on the tech stack: $ARGUMENTS

Steps:
1. Identify the languages and frameworks mentioned (or detect from project files)
2. Recommend the most appropriate style guides from the knowledge base
3. Suggest linter/formatter configurations that enforce those guides
4. Generate a CLAUDE.md or .cursorrules file tailored to this stack

Common setups:
- JavaScript/TypeScript → ESLint (Airbnb config) + Prettier
- Python → Ruff or Flake8 + Black (PEP 8)
- Go → golangci-lint (Uber style)
- Ruby → RuboCop (bbatsov style)
- Rust → clippy + rustfmt
- PHP → PHP_CodeSniffer (PSR-12)

Include links to the relevant best practices resources for the team to reference.
