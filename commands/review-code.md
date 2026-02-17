---
description: Review code against industry best practices and style guides
---

Review the code in the current file or provided context against industry best practices.

Steps:
1. Detect the language/framework being used
2. Apply the relevant style guide (Airbnb for JS, Uber for Go, bbatsov for Ruby, etc.)
3. Check for Clean Code principle violations
4. Check for security issues using OWASP guidelines
5. Check for performance anti-patterns

For each issue found, provide:
- The specific violation
- Which style guide or resource it violates (with link)
- A suggested fix

Focus on actionable, high-impact feedback. Don't nitpick formatting if a linter can handle it.

$ARGUMENTS
