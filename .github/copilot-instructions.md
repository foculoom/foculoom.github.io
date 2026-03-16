# .github/copilot-instructions.md — foculoom.github.io

## Project Overview

`foculoom.github.io` is a public static website for `foculoom.com`.

- Treat everything in this repo as public.
- Keep public copy narrow, accurate, and customer-facing while products may still be coming soon.
- Do not add internal repo paths, private notes, draft operational details, or secrets.
- Avoid medical, diagnosis, treatment, therapy, or wellness framing.

Use `README.md` as the human source of truth for site scope and public guardrails.
Use `.github/instructions/website-copy.instructions.md` for copy tone and status-language rules.
Use `.github/instructions/website-publish.instructions.md` before merging public-site edits.

## Commands

```bash
# Required validation
python3 scripts/validate_site.py

# Build the publishable artifact
python3 scripts/build_site.py

# Local preview
python3 -m http.server --directory _site 8000
```

## How to Work in This Repo

- Keep edits surgical and repo-specific.
- Prefer precise public-facing copy over aspirational or speculative messaging.
- Assume any new text may be read by end users.
- Prefer end-product language over planning, rollout, or launch-sequence language.
- Keep references public-safe and avoid internal filesystem paths or sibling-repo notes.
- Preserve the existing validation/build workflow and use it after changes.

## Guardrails

- Do not introduce medical, diagnosis, treatment, therapy, or wellness framing.
- Do not expose internal repo paths, private planning notes, or secrets.
- Do not widen product claims unless they are explicitly confirmed.
- Do not describe a product as live unless the page has the real live store or platform link.
- Validate with `python3 scripts/validate_site.py && python3 scripts/build_site.py`.
- Do not modify CI workflows.
