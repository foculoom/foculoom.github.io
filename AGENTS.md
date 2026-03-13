# AGENTS.md — foculoom.github.io

> This file follows the [AGENTS.md open specification](https://agents.md).
> It provides cross-agent repository guidance for AI coding assistants.

## Project Overview

`foculoom.github.io` is the public static website for Foculoom.

- Treat everything in this repo as public.
- Keep public copy narrow, accurate, and appropriate for a pre-launch site.
- Avoid internal repo paths, private notes, secrets, and any other non-public operational details.
- Avoid medical, diagnosis, treatment, therapy, or wellness framing unless the user explicitly confirms it belongs in public copy.

## Commands

```bash
# Validate required files, links, and public-content guardrails
python3 scripts/validate_site.py

# Build the publishable artifact into _site/
python3 scripts/build_site.py

# Preview the built site locally
python3 -m http.server --directory _site 8000
```

## Tech Stack

- Static HTML pages
- Shared CSS and image assets
- Python 3 validation and build scripts
- GitHub Pages deployment

## Project Structure

```text
index.html, *.html  Public site pages
focus-tasks/        Product-specific public landing page content
assets/             Public CSS, icons, images, and manifest files
scripts/            Local validation and build helpers
_site/              Generated publishable artifact
.github/            GitHub config and Copilot instructions
README.md           Human-readable source of truth for public-site guardrails
```

## Working Rules

- Use `README.md` as the source of truth for site scope and public guardrails.
- Treat all repository content, filenames, logs, and generated output as public-facing.
- Keep copy intentionally narrow while the site is pre-launch.
- Avoid medical/diagnosis/treatment/therapy/wellness framing.
- Prefer specific, factual copy over speculative launch messaging.
- Validate with `python3 scripts/validate_site.py` and `python3 scripts/build_site.py` after changes.
- Use `python3 -m http.server --directory _site 8000` to preview the built site when needed.

## Boundaries

- ✅ Safe: tighten public copy, guardrails, and repo-local AI instructions
- ✅ Safe: update static-site docs to match current scripts and site behavior
- ⚠️ Ask first: changes that broaden launch claims, product positioning, or public policy language in a meaningful way
- ⚠️ Ask first: changes to `.github/workflows/` or deployment behavior
- 🚫 Never: add secrets, internal repo paths, private notes, or unpublished operational details
- 🚫 Never: modify CI workflows as part of this task
