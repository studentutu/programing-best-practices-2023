import glob
import re

# Known replacements for broken or changed links
replacements = {
    "https://docs.anthropic.com/en/docs/build-with-claude/agentic": "https://docs.anthropic.com/en/docs/build-with-claude",
    "https://docs.anthropic.com/en/docs/build-with-claude/develop-with-claude": "https://docs.anthropic.com/en/docs/build-with-claude",
    "https://docs.deno.com/runtime/fundamentals/best-practices/": "https://docs.deno.com/",
    "https://docs.deno.com/runtime/fundamentals/style-guide/": "https://docs.deno.com/",
    "https://bun.sh/docs/install": "https://bun.sh/docs",
    "https://bun.sh/docs/runtime/best-practices": "https://bun.sh/docs",
    "https://svelte.dev/docs/kit/best-practices": "https://svelte.dev/docs",
    "https://svelte.dev/docs/svelte/guide": "https://svelte.dev/docs",
    "https://svelte.dev/docs/svelte/performance": "https://svelte.dev/docs",
    "https://svelte.dev/docs/svelte/rules": "https://svelte.dev/docs",
    "https://nuxt.com/docs/guide/conventions": "https://nuxt.com/docs",
    "https://docs.solidjs.com/guides/best-practices": "https://docs.solidjs.com/",
    "https://docs.solidjs.com/guides/style-guide": "https://docs.solidjs.com/",
    "https://docs.solidjs.com/solid-start/best-practises": "https://docs.solidjs.com/",
}

updated_files = 0
for md in glob.glob("/home/ubuntu/repo/**/*.md", recursive=True):
    with open(md, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    modified = False
    for old_url, new_url in replacements.items():
        if old_url in content:
            content = content.replace(old_url, new_url)
            modified = True
            print(f"Updated {old_url} -> {new_url} in {md}")
            
    if modified:
        with open(md, "w", encoding="utf-8") as f:
            f.write(content)
        updated_files += 1

print(f"Total files updated: {updated_files}")
