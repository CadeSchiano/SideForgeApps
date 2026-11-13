"""Check shipped pages, local links, assets, metadata, and business email CTAs."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote, parse_qs
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parent.parent / 'dist'
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.meta = path, set(), [], {}
        self.tags, self.emails = [], 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append(tag)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate ID: {self.path}: {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'html': assert a.get('lang') == 'en'
        if tag == 'img':
            assert all(k in a for k in ('alt', 'width', 'height')), f'Image attributes: {self.path}'
        if tag == 'meta': self.meta[a.get('name', a.get('property'))] = a.get('content')
        for key in ('href', 'src'):
            if key in a: self.links.append(a[key])
        assert tag != 'form', 'Launch site and demos must not collect data'

pages = {p.resolve(): Page(p) for p in root.rglob('*.html')}
assert len(pages) == 3
for path, page in pages.items():
    assert all(t in page.tags for t in ('title', 'main', 'h1', 'nav', 'footer'))
    assert all(page.meta.get(k) for k in ('description', 'viewport', 'og:title', 'og:description', 'og:type', 'twitter:card'))
    for link in page.links:
        u = urlsplit(link)
        if u.scheme == 'mailto':
            assert u.path == 'sideforgeapps@gmail.com'
            assert parse_qs(u.query)['subject'] == ['Website inquiry for my business']
            page.emails += 1
        elif u.scheme:
            assert link == 'https://cadeschiano.github.io/portfolio/', f'Unexpected external asset or link: {link}'
        else:
            target = (path.parent / unquote(u.path)).resolve() if u.path else path
            if target.is_dir(): target /= 'index.html'
            assert target.is_file(), f'Broken target: {path}: {link}'
            if u.fragment:
                assert target in pages and u.fragment in pages[target].ids, f'Broken anchor: {link}'
    print(f'PASS {path.relative_to(root)}: local links, anchors, image attributes, semantic landmarks, metadata')
assert pages[(root/'index.html').resolve()].emails == 6
for p in (root/'assets').glob('*.svg'): ET.parse(p)
print('PASS: all 6 email CTAs use the correct address and subject; all SVG assets parse')
print(f'Total deployment size: {sum(p.stat().st_size for p in root.rglob("*") if p.is_file()):,} bytes')
