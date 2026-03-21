# 012 — foculoom.github.io: Plan

---

## Overview

The site is a static HTML hub hosted on GitHub Pages at `foculoom.com`. All products are
pre-launch: no Steam App IDs exist, no App Store listings are live. The goal is awareness,
wishlist capture (placeholder), and SEO readiness — not sales conversion.

Build tool: `scripts/build_site.py` (copies source into `_site/`).
Validation tool: `scripts/validate_site.py` (checks links and page inventory).
Deployment: GitHub Actions → Pages artifact from `_site/`.

---

## Phase 1 — Audit + Template (T001–T002)

- Audit which product pages already exist vs. which need creation.
- Create a shared HTML partial/template for product pages so all 8 follow a consistent structure.
- Outcome: a template file and a written gap list to drive T003–T011.

## Phase 2 — Product Pages (T003–T014)

- Create individual product landing pages for all 7 Steam games and BubblePop iOS (T003–T010).
- Create Focus & Tasks teaser page (T011).
- Add Steam wishlist widget placeholder comment markers per game page (T012).
- Embed mailing list signup form (Buttondown or Mailchimp) fleet-wide or per-page (T013).
- Add Steam Next Fest awareness section to relevant pages (T014).
- All pages link from the site index and respect the navigation pattern from existing pages.

## Phase 3 — SEO + Validation (T015–T020)

- Add Open Graph `<meta>` tags (og:title, og:description, og:image) to all pages (T015).
- Update `sitemap.xml` to include all new product pages (T016).
- Verify `robots.txt` allows all crawlers — no changes expected (T017).
- Extend `scripts/validate_site.py` to assert all product pages are present and internal links resolve (T018).
- Extend `scripts/build_site.py` to copy all new product page directories into `_site/` (T019).
- Run end-to-end build + validate locally to confirm the full pipeline is green (T020).
