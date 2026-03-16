---
applyTo: "*.html,focus-tasks/**/*.html,README.md,AGENTS.md,.github/copilot-instructions.md"
---

# Website Publish Checklist

Use this checklist before merging public-site copy or structure changes.

## Content checks

- [ ] The headline and opening paragraph explain the company or product clearly to a new visitor.
- [ ] No roadmap, rollout, or launch-order language remains.
- [ ] No product is described as live unless the page includes the actual live store or platform link.
- [ ] Any unreleased product is clearly marked `Coming soon`.
- [ ] Any new platform, pricing, or availability statement is explicitly confirmed.

## Trust checks

- [ ] No internal repo paths, planning notes, draft links, or private operational details are exposed.
- [ ] No medical, wellness, AI, collaboration, or child-directed claims are widened unless explicitly confirmed for public copy.
- [ ] Support, privacy, accessibility, and terms still match the public scope after the change.
- [ ] Legal name, contact details, and availability wording stay consistent across touched pages.

## Validation checks

- [ ] Run `python3 scripts/validate_site.py`
- [ ] Run `python3 scripts/build_site.py`
- [ ] Preview the changed pages from `_site/` when the copy or structure change is meaningful.
- [ ] Read the changed copy once as a cold visitor before publishing.

## Optional review pass

- [ ] If the change is mostly copy, run a `website-editor` review pass before merge.
