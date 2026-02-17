---
name: security-review
description: Use when reviewing code for security vulnerabilities, auditing API endpoints, checking authentication/authorization logic, or when asked about security best practices. Provides OWASP Top 10 guidance, API security checklists, and DevSecOps practices.
allowed-tools: Read, Grep, Glob, Bash
---

# Security Review Skill

When reviewing code for security, apply these authoritative resources:

## Primary References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — The standard for web application security
- [API Security Checklist](https://github.com/shieldfy/API-Security-Checklist) — Comprehensive API security guide
- [AWS Well-Architected Security Pillar](https://aws.amazon.com/architecture/well-architected/)

## Security Checklist

### Authentication & Authorization
- [ ] Passwords hashed with bcrypt/argon2 (never MD5/SHA1)
- [ ] JWT tokens have expiration and proper validation
- [ ] Session management follows OWASP guidelines
- [ ] Role-based access control properly enforced
- [ ] No hardcoded credentials or API keys

### Input Validation
- [ ] All user input sanitized and validated
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] Command injection prevention
- [ ] File upload validation (type, size, content)

### API Security
- [ ] Rate limiting implemented
- [ ] CORS properly configured
- [ ] HTTPS enforced
- [ ] API versioning in place
- [ ] Input size limits set
- [ ] Sensitive data not in URLs or logs

### Data Protection
- [ ] PII encrypted at rest and in transit
- [ ] Sensitive data not logged
- [ ] Database credentials in environment variables
- [ ] Secrets managed via vault/secrets manager
- [ ] Backup encryption enabled

### Dependencies
- [ ] No known vulnerable dependencies
- [ ] Dependencies regularly updated
- [ ] Lock files committed
- [ ] Minimal dependency footprint

## Process

1. Identify the language/framework in use
2. Check against the relevant security checklist above
3. Reference OWASP Top 10 for any web-facing code
4. Flag issues with severity (Critical/High/Medium/Low)
5. Provide specific remediation with code examples
6. Cite the relevant security resource for each finding
