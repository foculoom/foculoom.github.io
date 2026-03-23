#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / '_site'
FILES = [
    'CNAME',
    'index.html',
    'support.html',
    'privacy.html',
    'terms.html',
    'accessibility.html',
    '404.html',
    'robots.txt',
    'sitemap.xml',
]
DIRECTORIES = [
    'assets',
    'focus-tasks',
    'one-clear-path',
    'stillwater',
    'sortable',
    'inkwell',
    'tidekeeper',
    'quiet-room',
    'lantern-walk',
    'bubblepop',
]
REQUIRED_OUTPUTS = [*FILES, '.nojekyll']

if DEST.exists():
    shutil.rmtree(DEST)
DEST.mkdir()

for file_name in FILES:
    shutil.copy2(ROOT / file_name, DEST / file_name)

for directory_name in DIRECTORIES:
    shutil.copytree(ROOT / directory_name, DEST / directory_name)

(DEST / '.nojekyll').write_text('', encoding='utf-8')

missing_outputs = [name for name in REQUIRED_OUTPUTS if not (DEST / name).exists()]
if missing_outputs:
    missing_list = ', '.join(missing_outputs)
    raise FileNotFoundError(f'Built site is missing required artifact files: {missing_list}')

print(f'Built site into {DEST}')
