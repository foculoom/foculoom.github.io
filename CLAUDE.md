# foculoom.github.io — AI Context

This file provides context for AI coding agents working on the Foculoom website.

## Site Overview

**foculoom.com** is the public marketing website for Foculoom LLC. It centers on
**Foculoom Dash** — a colorful endless runner for kids. Static HTML deployed via
GitHub Pages.

## Tech Stack

- **Static HTML** — No framework, no build step for HTML
- **CSS** — Custom styles in `assets/site.css`
- **Build:** `python3 scripts/build_site.py` → `_site/` (gitignored)
- **Validate:** `python3 scripts/validate_site.py` (checks links, meta tags, structure)
- **Deploy:** Push to `master` → GitHub Pages auto-deploy
- **Domain:** foculoom.com (custom domain via CNAME)

## Site Structure

```
index.html                  — Homepage centered on Foculoom Dash
dash/index.html             — Foculoom Dash product page
one-clear-path/index.html   — Redirect to Steam store listing
privacy.html                — Privacy policy (covers Foculoom Dash + website)
terms.html                  — Terms of service
accessibility.html          — Accessibility statement
support.html                — Support/contact page
404.html                    — Custom 404 page
assets/                     — CSS, OG images, favicons
scripts/                    — Build and validation scripts
templates/                  — Product page template (reference only)
```

## Constraints

1. Keep copy public-facing, narrow, accurate — no internal repo paths or implementation details
2. No medical/wellness framing without explicit user consent
3. No "addictive" or "compelling" language in marketing copy
4. No manufactured urgency (no "limited time" framing)
5. No dark patterns in CTAs
6. Privacy-first: no third-party analytics or tracking scripts
7. Foculoom Dash is for kids ages 6+ — COPPA-compliant, no data collection

## Code Quality

- Conventional Commits: `feat|fix|docs|chore(scope): message`
- Feature branches from `master`
- Always run `python3 scripts/validate_site.py` before committing
- Rebuild `_site/` with `python3 scripts/build_site.py` after changes
