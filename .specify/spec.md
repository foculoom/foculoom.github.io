# 012-A — foculoom.github.io: Spec

> **⚠️ DEPRECATED** — This spec is a historical artifact from the SpecKit era.
> New specs and issues are tracked on [foculoom/foculoom-project GitHub Issues](https://github.com/foculoom/foculoom-project/issues).
> Do not add new requirements here.

> **Type:** Static marketing website (GitHub Pages)
> **Domain:** foculoom.com
> **Status:** Pre-launch — no products are in any store yet
> **Spec prefix:** 012

---

## Public Repo Guardrails

| Constraint | How This Spec Satisfies It |
|---|---|
| No secrets or private paths | All links use placeholder text; no internal paths or staging URLs in HTML |
| Accurate, intentionally narrow copy | No launch dates, no pricing, no store claims until App IDs/listings exist |
| No medical, AI, or child-directed claims | Product descriptions are factual and descriptive only |
| No exact pricing or launch claims | Steam and App Store buttons are placeholders — disabled until live |
| Everything is public | Commit messages, workflows, and HTML content treated as fully public |

---

## User Stories

### US1 — Product Discovery (P1)

**As a** prospective player or press contact,
**I want to** find a dedicated page for each Foculoom product,
**so that** I can learn what the game is, get excited, and know when/where to find it.

**Acceptance Criteria:**

1. Each of the 7 Steam games has an individual HTML page at a stable URL (e.g., `/one-clear-path/`).
2. BubblePop iOS has its own page at `/bubblepop/`.
3. Focus & Tasks has a teaser page at `/focus-tasks/` indicating discovery/coming-soon status.
4. Each page shows: product name, 1-line tagline, 1-paragraph description, and a CTA (placeholder until live).
5. All product pages are linked from the site index and accessible via consistent navigation.

### US2 — Wishlist Capture (P1)

**As a** player who wants to follow a Foculoom game on Steam,
**I want to** click a wishlist button or sign up for email updates on a game's page,
**so that** I am notified when the game launches.

**Acceptance Criteria:**

1. Each Steam game page includes a Steam wishlist widget placeholder (HTML comment marker `<!-- STEAM_WIDGET: [game] -->`) that can be activated once an App ID is assigned.
2. A mailing list signup (Buttondown or Mailchimp embed) is present — either per-game or fleet-wide — so users can opt in for pre-launch updates before Steam pages exist.
3. A Steam Next Fest awareness blurb appears on applicable pages: "We'll be at Steam Next Fest — add to wishlist to get notified."

### US3 — SEO Discoverability (P2)

**As a** search engine crawler or social media platform,
**I want to** find structured metadata on all pages,
**so that** Foculoom products surface correctly in search results and social previews.

**Acceptance Criteria:**

1. All product pages have a `<meta name="description">` tag with an accurate, concise summary.
2. All product pages have Open Graph tags: `og:title`, `og:description`, `og:image`, `og:url`.
3. `sitemap.xml` includes all product pages.
4. `robots.txt` allows all crawlers (already in place — verified, no changes needed).

### US4 — Build Integrity (P1)

**As a** developer or CI pipeline,
**I want to** run `build_site.py` and `validate_site.py` and have them cover all product pages,
**so that** broken links and missing pages are caught before deployment.

**Acceptance Criteria:**

1. `scripts/build_site.py` copies all new product page directories into `_site/`.
2. `scripts/validate_site.py` asserts all 8 product pages (+ focus-tasks) are present and that no internal `<a href>` links are broken.
3. Both scripts exit with code 0 on a clean build and non-zero on failure.

---

## Functional Requirements

| ID | Requirement | Story |
|---|---|---|
| FR-01 | Individual product landing page for each of the 7 Steam games: One Clear Path, Stillwater, Sortable, Inkwell, Tidekeeper, Quiet Room, Lantern Walk — each with game name, 1-line tagline, 1-paragraph description, and a placeholder Steam wishlist button (disabled until App ID exists) | US1 |
| FR-02 | BubblePop iOS product page with App Store badge (placeholder until live), description, and age appropriateness note | US1 |
| FR-03 | Focus & Tasks product teaser page — "Coming soon" / discovery phase status only; no pricing | US1 |
| FR-04 | Consistent navigation component across all product pages (links back to home and to other products) | US1 |
| FR-05 | Steam wishlist widget embed placeholder per Steam game page via HTML comment `<!-- STEAM_WIDGET: [game] -->` so it can be activated once an App ID is assigned | US2 |
| FR-06 | "Notify me" mailing list signup (Buttondown or Mailchimp form embed) for pre-launch updates — one per game page or fleet-wide | US2 |
| FR-07 | Steam Next Fest landing section on applicable game pages: "We'll be at Steam Next Fest — add to wishlist to get notified" | US2 |
| FR-08 | `<meta name="description">` and Open Graph tags (`og:title`, `og:description`, `og:image`, `og:url`) on all product pages | US3 |
| FR-09 | `sitemap.xml` updated to include all new product page URLs | US3 |
| FR-10 | `robots.txt` allows all crawlers — verify only, no changes expected | US3 |
| FR-11 | `scripts/validate_site.py` extended to assert all product pages are present and internal `<a href>` links resolve | US4 |
| FR-12 | `scripts/build_site.py` extended to copy all new product page directories into `_site/` | US4 |

---

## Pre-Launch Constraints

| Constraint | Detail |
|---|---|
| **No Steam App IDs** | All Steam links are placeholder. Do not embed live Steam widgets until App IDs are registered (tracked as T009 in foculoomllc tasks.md). |
| **No App Store listing** | BubblePop App Store badge must be placeholder until the listing is live. |
| **No pricing** | Do not mention price on any page until the game is in a store. |
| **No launch date claims** | Use "coming soon" or "in development" language only. |
| **No AI or medical claims** | Focus & Tasks copy must not make medical, wellness, or AI claims. |
| **Site is public** | Treat all page content, commit messages, and filenames as publicly visible. |

---

## Success Criteria

1. All 8 product pages (7 Steam games + BubblePop) are live on the site with correct name, tagline, and description.
2. Focus & Tasks teaser page is accessible and clearly conveys "coming soon / discovery phase."
3. Every page passes `validate_site.py` with no broken internal links.
4. `build_site.py` produces `_site/` containing all product pages without errors.
5. All product pages have Open Graph tags sufficient for a correct social preview.
6. `sitemap.xml` includes all new product page URLs.
7. Steam wishlist widget placeholder comment markers are present on all 7 Steam game pages, ready to activate when App IDs are registered.

---

## Phase 2: Post-Launch Improvements (012-B)

> Added: 2026-03-23

### FR-13: Mailing List Integration
The mailing list signup forms on all product pages must be wired to an email service provider.
Currently all forms have `action="#"` (non-functional). Provider selection deferred — document
the integration point and mark ready for wiring when provider is chosen.

### FR-14: Game Screenshot Galleries
Each product page should include 1–3 gameplay screenshots from the game's `qa/screenshots/`
directory. Screenshots provide visual context that pure text descriptions cannot convey.

### FR-15: Steam Widget Activation
When OCP's Steam store page is publicly accessible, embed the Steam widget iframe on the
OCP product page. The widget placeholder comment already exists in the HTML.

### FR-16: Status Badge Accuracy
Product page status indicators must accurately reflect each game's state:
- OCP: "Available on Steam" or "Coming to Steam" (based on store page status)
- Focus & Tasks: "In Research" (not implied as a developed product)
- Other games: "Coming to Steam"

### FR-17: Homepage Card Accuracy
The "Utility apps" card on the homepage is a placeholder with no link. Either remove it
or replace with a meaningful card when a utility app product is ready.
