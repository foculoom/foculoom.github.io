# foculoom.github.io

Static website for Foculoom.

This repo hosts a small, static GitHub Pages site for `foculoom.com`. The current goal is a narrow pre-launch site with a flagship product page, support URL, and legal/supporting pages that can grow with the first app release.

## Content guardrails

- Use `../foculoomllc` as the source of truth for public website copy.
- Do not reuse `../ai-foculoom/Strategy.md` as publishable product strategy.
- Do not copy wording from `../scratch/websites/emtosa.github.io` without re-verifying it against current `foculoomllc` docs.
- Avoid exact pricing, medical claims, wellness framing, AI claims, collaboration claims, and child-directed launch framing for the flagship unless those details are explicitly confirmed.

## Local workflow

Validate the static site:

```bash
python3 scripts/validate_site.py
```

Build the publishable artifact into `_site/`:

```bash
python3 scripts/build_site.py
```

Preview the built site locally:

```bash
python3 -m http.server --directory _site 8000
```

## Deployment

GitHub Actions builds and deploys the Pages artifact from `_site/`.

This repo intentionally does not commit a `CNAME` file because the site is designed to deploy through a custom GitHub Pages workflow. Configure the approved custom domain in the repository's Pages settings and DNS after the repository is connected to GitHub.
