# 012 — foculoom.github.io: Tasks

> All file paths relative to the repo root (`foculoom.github.io/`).

---

## T001 — Audit existing product coverage

**Status:** pending
**Depends on:** —
**Spec refs:** FR-01, FR-02, FR-03
**Description:** Audit which product pages currently exist in the site vs. what's needed for all 8 products (7 Steam games + BubblePop iOS) plus the Focus & Tasks teaser.
**Done when:** A written list of "exists" vs. "needs creation" per product page is produced in a comment at the top of this task, and the gap list is confirmed accurate against the repo's current directory structure.

---

## T002 — Create product page template (shared HTML partial)

**Status:** pending
**Depends on:** T001
**Spec refs:** FR-01, FR-02, FR-04
**Description:** Create a shared HTML template file (e.g., `templates/product-page.html`) that all 8 product pages derive from. The template includes: `<head>` with placeholder OG meta tags, consistent `<nav>`, product name H1, tagline, description paragraph, CTA button section (placeholder), Steam widget comment marker, mailing list form embed placeholder, Steam Next Fest section placeholder, and footer.
**Done when:** Template file exists and renders correctly in a browser. It includes all structural placeholders (Steam widget comment, mailing list embed, OG tags) so each product page only needs to fill in content.

---

## T003 — One Clear Path product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `one-clear-path/index.html` for the One Clear Path Steam game. Include: game name, 1-line tagline, 1-paragraph description, disabled placeholder Steam wishlist button, `<!-- STEAM_WIDGET: one-clear-path -->` comment marker, mailing list embed, Steam Next Fest section, and Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/one-clear-path/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T004 — Stillwater product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `stillwater/index.html` for the Stillwater Steam game. Same structure as T003: name, tagline, description, disabled Steam wishlist button, `<!-- STEAM_WIDGET: stillwater -->` comment marker, mailing list embed, Steam Next Fest section, Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/stillwater/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T005 — Sortable product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `sortable/index.html` for the Sortable Steam game. Same structure: name, tagline, description, disabled Steam wishlist button, `<!-- STEAM_WIDGET: sortable -->` comment marker, mailing list embed, Steam Next Fest section, Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/sortable/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T006 — Inkwell product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `inkwell/index.html` for the Inkwell Steam game. Same structure: name, tagline ("Restore lost words. Recover meaning."), description, disabled Steam wishlist button, `<!-- STEAM_WIDGET: inkwell -->` comment marker, mailing list embed, Steam Next Fest section, Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/inkwell/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T007 — Tidekeeper product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `tidekeeper/index.html` for the Tidekeeper Steam game. Same structure: name, tagline, description, disabled Steam wishlist button, `<!-- STEAM_WIDGET: tidekeeper -->` comment marker, mailing list embed, Steam Next Fest section, Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/tidekeeper/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T008 — Quiet Room product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `quiet-room/index.html` for the Quiet Room Steam game. Same structure: name, tagline, description, disabled Steam wishlist button, `<!-- STEAM_WIDGET: quiet-room -->` comment marker, mailing list embed, Steam Next Fest section, Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/quiet-room/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T009 — Lantern Walk product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-01, FR-05, FR-06, FR-07, FR-08
**Description:** Create `lantern-walk/index.html` for the Lantern Walk Steam game. Same structure: name, tagline, description, disabled Steam wishlist button, `<!-- STEAM_WIDGET: lantern-walk -->` comment marker, mailing list embed, Steam Next Fest section, Open Graph meta tags. Add to site navigation.
**Done when:** Page exists at `/lantern-walk/`, renders correctly, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T010 — BubblePop iOS product page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-02, FR-08
**Description:** Create `bubblepop/index.html` for the BubblePop iOS app. Include: app name, tagline, description, age appropriateness note, placeholder App Store badge (disabled/greyed until listing is live), and Open Graph meta tags. No Steam widget — this is an iOS app. Add to site navigation.
**Done when:** Page exists at `/bubblepop/`, renders correctly with placeholder App Store badge, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T011 — Focus & Tasks teaser page

**Status:** pending
**Depends on:** T002
**Spec refs:** FR-03, FR-08
**Description:** Update or create `focus-tasks/index.html` with "coming soon / discovery phase" status. Copy must not include pricing, launch dates, AI claims, or medical claims. Include Open Graph meta tags. Confirm it links correctly from the site index.
**Done when:** Page exists at `/focus-tasks/`, copy is accurate and pre-launch-safe, passes `validate_site.py`, and is included in `_site/` after `build_site.py`.

---

## T012 — Steam wishlist widget placeholder markers

**Status:** pending
**Depends on:** T003, T004, T005, T006, T007, T008, T009
**Spec refs:** FR-05
**Description:** Verify that all 7 Steam game pages (T003–T009) contain the correct HTML comment marker `<!-- STEAM_WIDGET: [game-slug] -->` in the CTA section, positioned where the Steam embed iframe will go once an App ID is registered. Document the activation steps in a comment in each file.
**Done when:** All 7 game pages contain the correct `STEAM_WIDGET` comment marker in the correct location and a nearby `<!-- TO ACTIVATE: replace this comment with the Steam widget iframe once App ID is assigned -->` note.

---

## T013 — Mailing list signup form embed

**Status:** pending
**Depends on:** T003, T004, T005, T006, T007, T008, T009, T010, T011
**Spec refs:** FR-06
**Description:** Add a mailing list signup form to all product pages (fleet-wide embed preferred, or per-page if the provider requires it). Use Buttondown or Mailchimp embed code. If no live embed exists yet, add a `<!-- MAILING_LIST_EMBED -->` placeholder comment with a note on which provider to use. The form or placeholder must appear above the fold or in a clearly visible section.
**Done when:** All product pages contain either a live mailing list embed or the `<!-- MAILING_LIST_EMBED -->` placeholder comment with a provider note.

---

## T014 — Steam Next Fest section

**Status:** pending
**Depends on:** T003, T004, T005, T006, T007, T008, T009
**Spec refs:** FR-07
**Description:** Add a Steam Next Fest awareness section to all 7 Steam game pages. Copy: "We'll be at Steam Next Fest — add to wishlist to get notified." Section must link to (or reference) the Steam wishlist placeholder. Include a `<!-- STEAM_NEXT_FEST -->` HTML comment marker so the section can be toggled or updated easily.
**Done when:** All 7 Steam game pages contain the Steam Next Fest section with the correct copy and the HTML comment marker.

---

## T015 — Open Graph meta tags for all pages

**Status:** pending
**Depends on:** T003, T004, T005, T006, T007, T008, T009, T010, T011
**Spec refs:** FR-08
**Description:** Audit and update `<head>` on all product pages to include `<meta name="description">`, `og:title`, `og:description`, `og:image`, and `og:url` tags. Use consistent og:image placeholder (e.g., site logo or a per-product placeholder image). Verify the home page (`index.html`) and existing pages (privacy, support, accessibility, terms) also have at minimum `<meta name="description">`.
**Done when:** All product pages have complete OG tag sets. Running a social preview checker against local HTML shows correct title and description.

---

## T016 — sitemap.xml update

**Status:** pending
**Depends on:** T003, T004, T005, T006, T007, T008, T009, T010, T011
**Spec refs:** FR-09
**Description:** Update `sitemap.xml` to include `<url>` entries for all new product pages. Use `https://foculoom.com/[slug]/` URL format. Set `<changefreq>monthly</changefreq>` and a current `<lastmod>` date. Validate the XML is well-formed.
**Done when:** `sitemap.xml` includes all 9 new product pages (7 Steam + bubblepop + focus-tasks), XML is valid, and the file is included in `_site/` after `build_site.py`.

---

## T017 — robots.txt validation

**Status:** pending
**Depends on:** —
**Spec refs:** FR-10
**Description:** Verify `robots.txt` in the repo root allows all crawlers (`User-agent: *` / `Disallow:` empty or absent). No changes expected. Confirm the file is copied to `_site/` by `build_site.py`. Document the check result in a comment here.
**Done when:** `robots.txt` is confirmed to allow all crawlers and is present in `_site/` after a build.

---

## T018 — validate_site.py update for new pages

**Status:** pending
**Depends on:** T001, T003, T004, T005, T006, T007, T008, T009, T010, T011
**Spec refs:** FR-11
**Description:** Extend `scripts/validate_site.py` to assert: (1) all 9 product page `index.html` files exist in the source tree, (2) all internal `<a href>` links across all pages resolve to an existing file, and (3) `sitemap.xml` contains entries for all product pages. The script must exit non-zero with a descriptive error message if any assertion fails.
**Done when:** `python3 scripts/validate_site.py` passes (exit 0) on the complete site and fails with a clear error if a product page is missing or a link is broken.

---

## T019 — build_site.py update for new pages

**Status:** pending
**Depends on:** T003, T004, T005, T006, T007, T008, T009, T010, T011
**Spec refs:** FR-12
**Description:** Extend `scripts/build_site.py` to copy all new product page directories (`one-clear-path/`, `stillwater/`, `sortable/`, `inkwell/`, `tidekeeper/`, `quiet-room/`, `lantern-walk/`, `bubblepop/`, `focus-tasks/`) into `_site/`. Verify the script preserves directory structure and copies all assets (CSS, images) referenced from product pages.
**Done when:** `python3 scripts/build_site.py` exits 0 and `_site/` contains all product page directories with their `index.html` files.

---

## T020 — End-to-end test: build + validate locally

**Status:** pending
**Depends on:** T018, T019
**Spec refs:** FR-11, FR-12
**Description:** Run `python3 scripts/build_site.py && python3 scripts/validate_site.py` locally and confirm both exit 0 with no errors. Optionally serve `_site/` with `python3 -m http.server --directory _site 8000` and manually spot-check 3 product pages and the home page.
**Done when:** Both scripts exit 0. Spot-check confirms product pages load correctly and navigation links work.

---

## T021 — Visual validation: full site screenshot review

**Status:** pending
**Depends on:** T020
**Spec refs:** FR-01–FR-12 (012-A spec increment)

Build the site, serve it locally, capture screenshots of all key pages, and examine for layout issues, broken links, placeholder accuracy, and SEO meta correctness.

**Steps:**
1. `mkdir -p .specify/validation/`
2. Build and serve:
   ```bash
   python3 scripts/build_site.py
   python3 -m http.server --directory _site 8000 &
   SERVER_PID=$!
   sleep 2
   ```
3. Open index page in browser and capture (see `/foculoom/games/CAPTURE.md` §2 for Quartz window-detection recipe; substitute your browser process name for "godot"):
   ```bash
   open http://localhost:8000
   sleep 3
   # Detect browser window position via Quartz, then:
   screencapture -R lx,ly,w,h -x ".specify/validation/T021-index-$(date +%Y%m%d-%H%M).png"
   ```
   Do NOT use `screencapture -x` alone — captures full 4112×2658 Retina screen, not the browser window.
4. For each product page that exists (check `_site/` for subdirectories), navigate browser and capture:
   `screencapture -R lx,ly,w,h -x ".specify/validation/T021-[product]-$(date +%Y%m%d-%H%M).png"`
5. Stop the server: `kill $SERVER_PID 2>/dev/null || true`
6. View each screenshot and check for:
   - All product pages render with correct layout (no overflow, no missing CSS)
   - Steam wishlist button placeholders are visually disabled/greyed out (no active links to non-existent Steam pages)
   - App Store badge for BubblePop is placeholder (no live link yet)
   - "Coming Soon" / discovery state messaging for Focus & Tasks is present and accurate
   - Navigation links work across pages (no 404 destinations visible)
   - Steam Next Fest section present on relevant page(s)
   - Mailing list form embed placeholder visible
   - No internal links pointing to pages that don't exist in `_site/`
   - Open Graph meta tags present in HTML (check page source): og:title, og:description, og:image
7. Also validate HTML: `python3 scripts/validate_site.py`
8. Fix any P0 issues (broken layout, live links to non-existent store pages) before marking done

**Done when:**
- Screenshots of index + at least 3 product pages saved to `.specify/validation/`
- `python3 scripts/validate_site.py` passes with no errors
- No live/active store links (Steam or App Store) pointing to non-existent listings
- Open Graph meta tags verified in at least one page's HTML source
- A 3–5 sentence validation note appended describing what was verified
