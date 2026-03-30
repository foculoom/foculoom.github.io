# AGENTS.md — foculoom.github.io

> This file follows the [AGENTS.md open specification](https://agents.md).
> It provides cross-agent repository guidance for AI coding assistants.

## Project Overview

`foculoom.github.io` is the public static website for Foculoom.

- Treat everything in this repo as public.
- Keep public copy narrow, accurate, and customer-facing while some products are still marked as coming soon.
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
index.html, *.html  Public site pages (homepage, 404, privacy, support, terms, accessibility)
skiplet/            Skiplet by Foculoom product page (the primary product)
dash/               Redirect stub → /skiplet/
one-clear-path/     Redirect page to Steam store listing
assets/             Public CSS, icons, images, and manifest files
scripts/            Local validation and build helpers (validate_site.py, build_site.py)
_site/              Generated publishable artifact (output of build_site.py)
.specify/           Internal planning: spec.md, tasks.md, plan.md (⚠️ DEPRECATED — use GitHub Issues on foculoom-project)
.github/            GitHub config, instructions, agents, and Copilot guidance
README.md           Human-readable source of truth for public-site guardrails
```

## Issue Tracking

Work items for this repo are tracked as **GitHub Issues on [foculoom/foculoom-project](https://github.com/foculoom/foculoom-project/issues)**.
The `.specify/` directory is deprecated — do not create new tasks or specs there.

Every PR in this repo must include `Closes foculoom/foculoom-project#N` in the body to auto-close the tracked issue.

## Working Rules

- Use `README.md` as the source of truth for site scope and public guardrails.
- Use `.github/instructions/website-copy.instructions.md` for public-site tone, status, and anti-roadmap wording.
- Use `.github/instructions/website-publish.instructions.md` as the merge checklist for customer-facing edits.
- Treat all repository content, filenames, logs, and generated output as public-facing.
- Keep copy intentionally narrow and customer-facing while products may still be coming soon.
- Avoid medical/diagnosis/treatment/therapy/wellness framing.
- Prefer specific, factual product copy over speculative rollout or launch messaging.
- Validate with `python3 scripts/validate_site.py` and `python3 scripts/build_site.py` after changes.
- Use `python3 -m http.server --directory _site 8000` to preview the built site when needed.
- For copy-heavy tasks, prefer the optional `website-editor` agent for a rewrite or review pass.

## Boundaries

- ✅ Safe: tighten public copy, guardrails, and repo-local AI instructions
- ✅ Safe: update static-site docs to match current scripts and site behavior
- ⚠️ Ask first: changes that broaden product-positioning claims, add new live availability claims, or materially change public policy language
- ⚠️ Ask first: changes to `.github/workflows/` or deployment behavior
- 🚫 Never: add secrets, internal repo paths, private notes, or unpublished operational details
- 🚫 Never: modify CI workflows as part of this task

## QA Capture

For visual validation of this repo's website, always capture the browser window region — never the full screen.

**Rules:**
- Open site in browser (`open http://localhost:8000`), detect window bounds via Quartz (`kCGWindowOwnerName` matches your browser process name), then: `screencapture -R lx,ly,w,h -x FILE.png`
- **Never** use `screencapture -x FILE` alone — captures full 4112×2658 Retina screen, not the browser window
- Full Quartz window-detection recipe: `/foculoom/games/CAPTURE.md` §2 (substitute browser process name for "godot")
