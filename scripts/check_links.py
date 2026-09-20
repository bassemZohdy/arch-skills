#!/usr/bin/env python3
"""Check repository Markdown links offline; optionally probe public HTTP links.

Supports inline/reference links, autolinks, ATX/Setext headings and HTML IDs.
Code fences and inline code are examples, not Markdown dependency declarations.
External probes report reachability only, never the truth/freshness of content.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import html
import json
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urldefrag, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '.cache', '__pycache__', 'node_modules', '.venv'}


def prose(text):
    """Remove fenced examples while preserving line numbers."""
    output, fence = [], None
    for line in text.splitlines():
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            output.append('')
        elif marker:
            fence = marker[1]
            output.append('')
        else:
            output.append(line)
    return '\n'.join(output)


def anchors(text):
    text = prose(text)
    values = set(re.findall(r'<[^>]+\b(?:id|name)=["\']([^"\']+)', text))
    used = set()
    lines = text.splitlines()
    for index, line in enumerate(lines):
        heading = re.match(r'^ {0,3}#{1,6}\s+(.+?)(?:\s+#+\s*)?$', line)
        if heading:
            title = heading[1]
        elif index + 1 < len(lines) and line.strip() and re.fullmatch(r' {0,3}(?:=+|-+)\s*', lines[index + 1]):
            title = line.strip()
        else:
            continue
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        title = html.unescape(re.sub(r'<[^>]+>', '', title)).lower()
        slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        candidate, suffix = slug, 0
        while candidate in used:
            suffix += 1
            candidate = f'{slug}-{suffix}'
        used.add(candidate)
        values.add(candidate)
    return values


def links(text):
    text = prose(text)
    text = re.sub(r'(`+)(.*?)\1', '', text)
    definitions = {}
    normalize = lambda value: ' '.join(value.split()).casefold()
    for match in re.finditer(r'^ {0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', text, re.M):
        definitions[normalize(match[1])] = match[2].strip('<>')
    # Balanced parentheses in destinations, e.g. Wikipedia pages.
    for match in re.finditer(r'!?\[[^\]\n]*\]\(', text):
        start, end, depth = match.end(), match.end(), 1
        while end < len(text) and depth:
            if text[end] == '\\':
                end += 2
                continue
            if text[end] == '(':
                depth += 1
            elif text[end] == ')':
                depth -= 1
            end += 1
        if depth:
            continue
        value = text[start:end - 1].strip()
        dest = re.match(r'<([^>]+)>|([^\s]+)', value)
        if dest:
            yield text.count('\n', 0, match.start()) + 1, dest[1] or dest[2]
    for match in re.finditer(r'(?<!!)\[([^\]\n]+)\](?:\[([^\]\n]*)\])?', text):
        if text[match.end():match.end() + 1] in {'(', ':'}:
            continue
        key = normalize(match[2] or match[1])
        if key in definitions:
            yield text.count('\n', 0, match.start()) + 1, definitions[key]
        elif match[2] is not None:
            yield text.count('\n', 0, match.start()) + 1, f'UNDEFINED-REFERENCE:{key}'
    for match in re.finditer(r'<(https?://[^<>\s]+)>', text):
        yield text.count('\n', 0, match.start()) + 1, match[1]


def check_local(root):
    root = Path(root).resolve()
    errors, external, count = [], {}, 0
    for document in sorted(root.rglob('*.md')):
        if any(part in IGNORED for part in document.relative_to(root).parts):
            continue
        content = document.read_text(encoding='utf-8')
        count += 1
        for line, target in links(content):
            location = f'{document.relative_to(root).as_posix()}:{line}'
            if target.startswith('UNDEFINED-REFERENCE:'):
                errors.append(f'{location}: {target}')
                continue
            parsed = urlsplit(html.unescape(target))
            if parsed.scheme in {'http', 'https'}:
                external.setdefault(urldefrag(target)[0], []).append(location)
                continue
            if parsed.scheme or parsed.netloc:
                continue
            candidate = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
            if not candidate.is_relative_to(root):
                errors.append(f'{location}: link escapes root: {target}')
            elif not candidate.exists():
                errors.append(f'{location}: missing target: {target}')
            elif parsed.fragment and candidate.is_file() and candidate.suffix == '.md':
                if unquote(parsed.fragment) not in anchors(candidate.read_text(encoding='utf-8')):
                    errors.append(f'{location}: missing anchor: {target}')
    return {'documents': count, 'errors': errors, 'external': external}


def probe(url, timeout=10):
    """403/429/network failures remain unverified, not broken links."""
    result = {'url': url, 'status': 'unverified'}
    try:
        request = Request(url, headers={'User-Agent': 'arch-skills-link-check/1.0'})
        with urlopen(request, timeout=timeout) as response:
            result.update(status='reachable', http_status=response.status, final_url=response.url)
    except HTTPError as exc:
        result.update(status='broken' if exc.code in {404, 410} else 'unverified', http_status=exc.code)
    except (URLError, TimeoutError, OSError, ValueError) as exc:
        result['error'] = str(exc)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--external', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = check_local(args.root)
    if args.external:
        with ThreadPoolExecutor(max_workers=12) as pool:
            report['probes'] = list(pool.map(probe, sorted(report['external'])))
        report['checked_at'] = datetime.now(timezone.utc).isoformat()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    for error in report['errors']:
        print(error)
    print(f"{report['documents']} documents; {len(report['errors'])} local errors; {len(report['external'])} external URLs.")
    for result in report.get('probes', []):
        if result['status'] != 'reachable':
            print(f"{result['status']}: {result['url']} ({result.get('http_status', result.get('error'))})")
    return int(bool(report['errors']) or any(r['status'] == 'broken' for r in report.get('probes', [])))


if __name__ == '__main__':
    raise SystemExit(main())
