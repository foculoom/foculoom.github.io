#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [
    ROOT / 'index.html',
    ROOT / 'focus-tasks' / 'index.html',
    ROOT / 'support.html',
    ROOT / 'privacy.html',
    ROOT / 'terms.html',
    ROOT / 'accessibility.html',
    ROOT / '404.html',
]
OTHER_REQUIRED = [
    ROOT / 'assets' / 'site.css',
    ROOT / 'assets' / 'favicon.svg',
    ROOT / 'robots.txt',
    ROOT / 'sitemap.xml',
]
EXPECTED_URLS = {
    'https://foculoom.com/',
    'https://foculoom.com/focus-tasks/',
    'https://foculoom.com/support.html',
    'https://foculoom.com/privacy.html',
    'https://foculoom.com/terms.html',
    'https://foculoom.com/accessibility.html',
}
HREF_PATTERN = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']")
TITLE_PATTERN = re.compile(r'<title>.+?</title>', re.IGNORECASE | re.DOTALL)
CANONICAL_PATTERN = re.compile(r"rel=[\"']canonical[\"']", re.IGNORECASE)
MAIN_PATTERN = re.compile(r'<main\b', re.IGNORECASE)


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

for html_path in HTML_FILES:
    if not html_path.exists():
        continue

    text = html_path.read_text(encoding='utf-8')
    rel = html_path.relative_to(ROOT)
    if not TITLE_PATTERN.search(text):
        failures.append(f'{rel} is missing a <title>.')
    if not CANONICAL_PATTERN.search(text):
        failures.append(f'{rel} is missing a canonical link.')
    if not MAIN_PATTERN.search(text):
        failures.append(f'{rel} is missing a <main> element.')

    for target in HREF_PATTERN.findall(text):
        local_target = resolve_local_target(html_path, target)
        if local_target is None:
            continue
        if not local_target.exists():
            failures.append(f'{rel} references missing local target: {target}')

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
