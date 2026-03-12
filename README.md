# foculoom.github.io

Static website for Foculoom.

This repo hosts a small, static GitHub Pages site for `foculoom.com`. The current goal is a narrow pre-launch site with a flagship product page, support URL, and legal/supporting pages that can grow with the first app release.

## Public repo guardrails

- Treat everything in this repo as public, including files, commit messages, workflow configuration, and workflow logs.
- Do not add secrets, internal repo paths, private draft links, or private operational notes.
- Keep public copy accurate and intentionally narrow while the site is still pre-launch.
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

This repo commits a `CNAME` file for `foculoom.com`. Keep the committed `CNAME`, the repository's Pages settings, and DNS aligned whenever the site's domain configuration changes.
