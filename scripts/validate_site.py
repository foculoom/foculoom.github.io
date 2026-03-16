#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE_CSS = ROOT / 'assets' / 'site.css'
SITE_MANIFEST = ROOT / 'assets' / 'site.webmanifest'
EXPECTED_PAGE_URLS = {
    ROOT / 'index.html': 'https://foculoom.com/',
    ROOT / 'focus-tasks' / 'index.html': 'https://foculoom.com/focus-tasks/',
    ROOT / 'support.html': 'https://foculoom.com/support.html',
    ROOT / 'privacy.html': 'https://foculoom.com/privacy.html',
    ROOT / 'terms.html': 'https://foculoom.com/terms.html',
    ROOT / 'accessibility.html': 'https://foculoom.com/accessibility.html',
    ROOT / '404.html': 'https://foculoom.com/404.html',
}
HTML_FILES = [
    ROOT / 'index.html',
    ROOT / 'focus-tasks' / 'index.html',
    ROOT / 'support.html',
    ROOT / 'privacy.html',
    ROOT / 'terms.html',
    ROOT / 'accessibility.html',
    ROOT / '404.html',
]
SCHEMA_REQUIRED_FILES = [path for path in HTML_FILES if path != ROOT / '404.html']
OTHER_REQUIRED = [
    SITE_CSS,
    ROOT / 'assets' / 'favicon.svg',
    ROOT / 'assets' / 'apple-touch-icon.png',
    ROOT / 'assets' / 'icon-192.png',
    ROOT / 'assets' / 'icon-512.png',
    ROOT / 'assets' / 'og-foculoom.png',
    ROOT / 'assets' / 'og-focus-tasks.png',
    SITE_MANIFEST,
    ROOT / 'robots.txt',
    ROOT / 'sitemap.xml',
]
EXPECTED_URLS = set(EXPECTED_PAGE_URLS.values()) - {'https://foculoom.com/404.html'}
REQUIRED_PUBLIC_TOKENS = {
    'Foculoom LLC': 'company legal name',
    '2108 N ST STE N, Sacramento, CA 95816': 'company address',
    'tel:+13102701918': 'company phone link',
    'mailto:support@foculoom.com': 'support email',
    'mailto:hello@foculoom.com': 'general contact email',
}
BILLING_REQUIRED_FILES = [path for path in HTML_FILES if path != ROOT / '404.html']
PUBLIC_TEXT_FILES = [
    ROOT / 'README.md',
    ROOT / '.github' / 'workflows' / 'pages.yml',
    ROOT / '.gitignore',
    ROOT / 'CNAME',
    ROOT / 'robots.txt',
    ROOT / 'sitemap.xml',
    ROOT / 'assets' / 'site.css',
    ROOT / 'assets' / 'site.webmanifest',
    ROOT / 'scripts' / 'build_site.py',
    *HTML_FILES,
]
FORBIDDEN_PUBLIC_REFERENCES = {
    '../foculoomllc': 'internal sibling repo reference',
    '../ai-foculoom': 'internal sibling repo reference',
    '../scratch/': 'internal scratch repo reference',
    '/Users/': 'absolute local filesystem path',
    '.copilot/session-state': 'session-state path',
}
HREF_PATTERN = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']")
LANG_PATTERN = re.compile(r'<html\b[^>]*\blang=["\'][^"\']+["\']', re.IGNORECASE)
TITLE_PATTERN = re.compile(r'<title>.+?</title>', re.IGNORECASE | re.DOTALL)
META_DESCRIPTION_PATTERN = re.compile(r'<meta\b[^>]*name=["\']description["\']', re.IGNORECASE)
ROBOTS_PATTERN = re.compile(r'<meta\b[^>]*name=["\']robots["\'][^>]*content=["\']([^"\']+)["\']', re.IGNORECASE)
CANONICAL_PATTERN = re.compile(r"rel=[\"']canonical[\"']", re.IGNORECASE)
CANONICAL_HREF_PATTERN = re.compile(r'<link\b[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\']', re.IGNORECASE)
MAIN_PATTERN = re.compile(r'<main\b', re.IGNORECASE)
MAIN_ID_PATTERN = re.compile(r'<main\b[^>]*\bid=["\']main["\']', re.IGNORECASE)
H1_PATTERN = re.compile(r'<h1\b', re.IGNORECASE)
SKIP_LINK_PATTERN = re.compile(
    r'<a\b(?=[^>]*href=["\']#main["\'])(?=[^>]*class=["\'][^"\']*\bskip-link\b[^"\']*["\'])[^>]*>',
    re.IGNORECASE,
)
MANIFEST_PATTERN = re.compile(r"rel=[\"']manifest[\"']", re.IGNORECASE)
APPLE_TOUCH_ICON_PATTERN = re.compile(r"rel=[\"']apple-touch-icon[\"']", re.IGNORECASE)
OG_TITLE_PATTERN = re.compile(r'property=["\']og:title["\']', re.IGNORECASE)
OG_DESCRIPTION_PATTERN = re.compile(r'property=["\']og:description["\']', re.IGNORECASE)
OG_URL_PATTERN = re.compile(r'<meta\b[^>]*property=["\']og:url["\'][^>]*content=["\']([^"\']+)["\']', re.IGNORECASE)
OG_LOCALE_PATTERN = re.compile(r'property=["\']og:locale["\']', re.IGNORECASE)
OG_IMAGE_PATTERN = re.compile(r"property=[\"']og:image[\"']", re.IGNORECASE)
OG_IMAGE_ALT_PATTERN = re.compile(r'property=["\']og:image:alt["\']', re.IGNORECASE)
TWITTER_CARD_PATTERN = re.compile(r"name=[\"']twitter:card[\"']", re.IGNORECASE)
TWITTER_TITLE_PATTERN = re.compile(r'name=["\']twitter:title["\']', re.IGNORECASE)
TWITTER_DESCRIPTION_PATTERN = re.compile(r'name=["\']twitter:description["\']', re.IGNORECASE)
TWITTER_IMAGE_PATTERN = re.compile(r'name=["\']twitter:image["\']', re.IGNORECASE)
TWITTER_IMAGE_ALT_PATTERN = re.compile(r'name=["\']twitter:image:alt["\']', re.IGNORECASE)
JSON_LD_PATTERN = re.compile(r'<script\b[^>]*type=["\']application/ld\+json["\']', re.IGNORECASE)
JSON_LD_CONTENT_PATTERN = re.compile(
    r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
FOCUS_VISIBLE_PATTERN = re.compile(r':focus-visible')
SKIP_LINK_CSS_PATTERN = re.compile(r'\.skip-link')
REDUCED_MOTION_PATTERN = re.compile(r'@media\s*\(\s*prefers-reduced-motion\s*:\s*reduce\s*\)', re.IGNORECASE)


def resolve_local_target(source: Path, target: str) -> Path | None:
    clean_target = target.split('#', 1)[0].split('?', 1)[0]
    if not clean_target or clean_target.startswith(('http://', 'https://', 'mailto:', 'tel:')):
        return None

    if clean_target.startswith('/'):
        candidate = ROOT / clean_target.lstrip('/')
    else:
        candidate = (source.parent / clean_target).resolve()

    if candidate.is_dir() or clean_target.endswith('/'):
        return candidate / 'index.html'

    return candidate


failures: list[str] = []

for path in HTML_FILES + OTHER_REQUIRED:
    if not path.exists():
        failures.append(f'Missing required file: {path.relative_to(ROOT)}')

for text_path in PUBLIC_TEXT_FILES:
    if not text_path.exists():
        continue

    text = text_path.read_text(encoding='utf-8')
    rel = text_path.relative_to(ROOT)
    for snippet, label in FORBIDDEN_PUBLIC_REFERENCES.items():
        if snippet in text:
            failures.append(f'{rel} contains forbidden public reference ({label}): {snippet}')

for html_path in HTML_FILES:
    if not html_path.exists():
        continue

    text = html_path.read_text(encoding='utf-8')
    rel = html_path.relative_to(ROOT)
    for token, label in REQUIRED_PUBLIC_TOKENS.items():
        if token not in text:
            failures.append(f'{rel} is missing required public {label}: {token}')
    if html_path in BILLING_REQUIRED_FILES and 'mailto:billing@foculoom.com' not in text:
        failures.append(f'{rel} is missing the billing contact email: mailto:billing@foculoom.com')
    if 'DBA Foculoom' in text and 'd/b/a Foculoom' in text:
        failures.append(f'{rel} mixes DBA and d/b/a forms for the company name.')
    if not LANG_PATTERN.search(text):
        failures.append(f'{rel} is missing an html lang attribute.')
    if not TITLE_PATTERN.search(text):
        failures.append(f'{rel} is missing a <title>.')
    if not META_DESCRIPTION_PATTERN.search(text):
        failures.append(f'{rel} is missing a meta description.')
    robots_match = ROBOTS_PATTERN.search(text)
    if not robots_match:
        failures.append(f'{rel} is missing a robots meta tag.')
    else:
        robots_values = {part.strip().lower() for part in robots_match.group(1).split(',') if part.strip()}
        if html_path == ROOT / '404.html':
            if 'noindex' not in robots_values:
                failures.append(f'{rel} must be marked noindex.')
        elif not {'index', 'follow'}.issubset(robots_values):
            failures.append(f'{rel} must be marked index,follow.')
    if not CANONICAL_PATTERN.search(text):
        failures.append(f'{rel} is missing a canonical link.')
    else:
        canonical_match = CANONICAL_HREF_PATTERN.search(text)
        expected_url = EXPECTED_PAGE_URLS.get(html_path)
        if not canonical_match:
            failures.append(f'{rel} is missing a canonical href.')
        elif expected_url and canonical_match.group(1) != expected_url:
            failures.append(f'{rel} has the wrong canonical URL: {canonical_match.group(1)}')
    if not MAIN_PATTERN.search(text):
        failures.append(f'{rel} is missing a <main> element.')
    if not MAIN_ID_PATTERN.search(text):
        failures.append(f'{rel} is missing id="main" on the <main> element.')
    if not H1_PATTERN.search(text):
        failures.append(f'{rel} is missing an <h1>.')
    if not SKIP_LINK_PATTERN.search(text):
        failures.append(f'{rel} is missing a skip link to #main.')
    if not MANIFEST_PATTERN.search(text):
        failures.append(f'{rel} is missing a web manifest link.')
    if not APPLE_TOUCH_ICON_PATTERN.search(text):
        failures.append(f'{rel} is missing an apple-touch-icon link.')
    if not OG_TITLE_PATTERN.search(text):
        failures.append(f'{rel} is missing an og:title meta tag.')
    if not OG_DESCRIPTION_PATTERN.search(text):
        failures.append(f'{rel} is missing an og:description meta tag.')
    og_url_match = OG_URL_PATTERN.search(text)
    if not og_url_match:
        failures.append(f'{rel} is missing an og:url meta tag.')
    else:
        expected_url = EXPECTED_PAGE_URLS.get(html_path)
        if expected_url and og_url_match.group(1) != expected_url:
            failures.append(f'{rel} has the wrong og:url value: {og_url_match.group(1)}')
    if not OG_LOCALE_PATTERN.search(text):
        failures.append(f'{rel} is missing an og:locale meta tag.')
    if not OG_IMAGE_PATTERN.search(text):
        failures.append(f'{rel} is missing an og:image meta tag.')
    if not OG_IMAGE_ALT_PATTERN.search(text):
        failures.append(f'{rel} is missing an og:image:alt meta tag.')
    if not TWITTER_CARD_PATTERN.search(text):
        failures.append(f'{rel} is missing a twitter:card meta tag.')
    if not TWITTER_TITLE_PATTERN.search(text):
        failures.append(f'{rel} is missing a twitter:title meta tag.')
    if not TWITTER_DESCRIPTION_PATTERN.search(text):
        failures.append(f'{rel} is missing a twitter:description meta tag.')
    if not TWITTER_IMAGE_PATTERN.search(text):
        failures.append(f'{rel} is missing a twitter:image meta tag.')
    if not TWITTER_IMAGE_ALT_PATTERN.search(text):
        failures.append(f'{rel} is missing a twitter:image:alt meta tag.')
    if html_path in SCHEMA_REQUIRED_FILES:
        if not JSON_LD_PATTERN.search(text):
            failures.append(f'{rel} is missing structured data.')
        else:
            for block in JSON_LD_CONTENT_PATTERN.findall(text):
                try:
                    json.loads(block)
                except json.JSONDecodeError as exc:
                    failures.append(f'{rel} contains invalid JSON-LD: {exc}')

    for target in HREF_PATTERN.findall(text):
        local_target = resolve_local_target(html_path, target)
        if local_target is None:
            continue
        if not local_target.exists():
            failures.append(f'{rel} references missing local target: {target}')

if SITE_CSS.exists():
    css_text = SITE_CSS.read_text(encoding='utf-8')
    if not FOCUS_VISIBLE_PATTERN.search(css_text):
        failures.append('assets/site.css is missing a :focus-visible rule.')
    if not SKIP_LINK_CSS_PATTERN.search(css_text):
        failures.append('assets/site.css is missing skip-link styles.')
    if not REDUCED_MOTION_PATTERN.search(css_text):
        failures.append('assets/site.css is missing a prefers-reduced-motion override.')

if SITE_MANIFEST.exists():
    try:
        manifest = json.loads(SITE_MANIFEST.read_text(encoding='utf-8'))
    except json.JSONDecodeError as exc:
        failures.append(f'assets/site.webmanifest is not valid JSON: {exc}')
    else:
        lang = manifest.get('lang')
        if not isinstance(lang, str) or not lang.strip():
            failures.append('assets/site.webmanifest is missing a non-empty lang value.')

if (ROOT / 'sitemap.xml').exists():
    sitemap_text = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
    found_urls = set(re.findall(r'<loc>(.+?)</loc>', sitemap_text))
    missing_urls = sorted(EXPECTED_URLS - found_urls)
    if missing_urls:
        failures.append('sitemap.xml is missing expected URLs: ' + ', '.join(missing_urls))

if failures:
    for failure in failures:
        print(f'ERROR: {failure}')
    sys.exit(1)

print('Static site validation passed.')
