# foculoom.github.io — AI Context

This file provides context for AI coding agents working on the Foculoom website.

## Site Overview

**foculoom.com** is the public marketing website for Foculoom LLC. It hosts product pages
for 7 Steam games and 1 iOS app, plus legal/support pages. Static HTML deployed via
GitHub Pages.

## Tech Stack

- **Static HTML** — No framework, no build step for HTML
- **CSS** — Custom styles in `assets/style.css`
- **Build:** `python3 scripts/build_site.py` → `_site/` (gitignored)
- **Validate:** `python3 scripts/validate_site.py` (checks links, meta tags, structure)
- **Deploy:** Push to `master` → GitHub Pages auto-deploy
- **Domain:** foculoom.com (custom domain via CNAME)

## Site Structure

```
index.html                  — Homepage with product cards for all 8 games/apps
one-clear-path/index.html   — OCP product page (Steam App ID 4547350)
stillwater/index.html       — Stillwater product page
sortable/index.html         — Sortable product page
inkwell/index.html          — Inkwell product page
quiet-room/index.html       — Quiet Room product page
tidekeeper/index.html       — Tidekeeper product page
lantern-walk/index.html     — Lantern Walk product page
bubblepop/index.html        — BubblePop iOS product page
focus-tasks/index.html      — Focus & Tasks (in research)
privacy.html                — Privacy policy
terms.html                  — Terms of service
accessibility.html          — Accessibility statement
support.html                — Support/contact page
404.html                    — Custom 404 page
assets/                     — CSS, OG images, favicons
scripts/                    — Build and validation scripts
templates/                  — Product page template (reference only)
```

## Tagline Source of Truth

Each game's tagline comes from its spec.md. Current correct taglines:
- One Clear Path: "See less. Think more. Find the way."
- Lantern Walk: "Carry the light. Find the quiet."
- Quiet Room: "Notice what changed."
- Stillwater: "Place stones. Guide water. Grow gardens."
- Inkwell: "Restore lost words. Recover meaning."
- Sortable: "Put things where they belong."
- Tidekeeper: "Tend the light. Read the sea."
- BubblePop: "Pop, tap, have fun."

## Constraints

1. Keep copy public-facing, narrow, accurate — no internal repo paths or implementation details
2. No medical/wellness framing without explicit user consent
3. No "addictive" or "compelling" language in marketing copy
4. No manufactured urgency (no "limited time" framing)
5. No dark patterns in CTAs
6. Privacy-first: no third-party analytics or tracking scripts

## Code Quality

- Conventional Commits: `feat|fix|docs|chore(scope): message`
- Feature branches from `master`
- Always run `python3 scripts/validate_site.py` before committing
- Rebuild `_site/` with `python3 scripts/build_site.py` after changes
