#!/usr/bin/env python3
"""Build the five dependency-free GitHub Pages entry points from localized content."""
import json
from html import escape as e
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTENT = json.loads((ROOT / 'content.json').read_text())
LANGUAGES = {'en': 'EN', 'ru': 'RU', 'es': 'ES', 'fr': 'FR', 'zh': '中文'}
PROJECTS = [
    ('AICOM', 'build', 'https://magic-ai-factory.com/'),
    ('AIMarket', 'trade', 'https://modelmarket.dev/'),
    ('HESTIA', 'build', 'https://github.com/alexar76/hestia'),
    ('METIS', 'trust', 'https://metis.modelmarket.dev/'),
    ('AttestedMemory', 'trust', 'https://attestedmemory.net/'),
    ('WARDEN', 'trust', 'https://github.com/alexar76/warden'),
    ('THEMIS', 'trust', 'https://github.com/alexar76/themis'),
    ('GAIA', 'data', 'https://github.com/alexar76/gaia'),
    ('LOGOS', 'data', 'https://logos.modelmarket.dev/'),
]
CATEGORIES = ['all', 'build', 'trade', 'trust', 'data']
DOCS = 'https://github.com/alexar76/aicom/blob/main/docs/ecosystem/knowledge-base.md'

def route(locale):
    return '/' if locale == 'en' else f'/{locale}/'

def render(locale, c):
    url = 'https://alexar76.github.io' + route(locale)
    docs = DOCS if locale == 'en' else DOCS.replace('knowledge-base.md', f'knowledge-base-{locale}.md')
    alternates = ''.join(f'<link rel="alternate" hreflang="{l}" href="https://alexar76.github.io{route(l)}">' for l in LANGUAGES)
    lang_links = ''.join(f'<a href="{route(l)}" lang="{l}" hreflang="{l}" {"aria-current=page" if l == locale else ""}>{name}</a>' for l, name in LANGUAGES.items())
    role_links = [PROJECTS[0][2], PROJECTS[1][2], PROJECTS[2][2]]
    roles = ''.join(f'<a class="role" href="{role_links[i]}"><span class="mono">0{i+1} / {e(role)}</span><h3>{e(name)}<span>↗</span></h3><p>{e(desc)}</p></a>' for i, (name, role, desc) in enumerate(c['roles']))
    steps = ''.join(f'<article><span class="step-no">0{i+1}</span><h3>{e(title)}</h3><p>{e(desc)}</p></article>' for i, (title, desc) in enumerate(c['steps']))
    filters = ''.join(f'<button type="button" data-filter="{key}" aria-pressed="{str(i == 0).lower()}">{e(c["filters"][i])}</button>' for i, key in enumerate(CATEGORIES))
    projects = ''.join(f'<a class="project" data-category="{category}" href="{href}"><span class="project-symbol" aria-hidden="true">{["▧","↗","◇","✳","◎","⊞","⋈","◒","∿"][i]}</span><span class="mono">{e(c["filters"][CATEGORIES.index(category)])}</span><h3>{e(name)}</h3><p>{e(c["descriptions"][i])}</p><span class="project-open">{e(c["open"])} <b>↗</b></span></a>' for i, (name, category, href) in enumerate(PROJECTS))
    return f'''<!doctype html>
<html lang="{locale}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#e8eee9">
<title>{e(c['title'])} — AICOM Ecosystem</title><meta name="description" content="{e(c['intro'])}"><link rel="canonical" href="{url}">{alternates}<link rel="alternate" hreflang="x-default" href="https://alexar76.github.io/">
<meta property="og:type" content="website"><meta property="og:title" content="{e(c['title'])}"><meta property="og:description" content="{e(c['intro'])}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://alexar76.github.io/assets/social.png"><meta name="twitter:card" content="summary">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/fonts/fonts.css"><link rel="stylesheet" href="/assets/site.css"><script type="module" src="/assets/site.js"></script><script type="module" src="/assets/scene.js"></script></head>
<body><a class="skip" href="#main">{e(c['skip'])}</a><header class="wrap"><a class="brand" href="{route(locale)}"><span class="brand-mark">✳</span><span>AICOM<span class="brand-sub">ECOSYSTEM</span></span></a><nav class="primary"><a href="#explore">{e(c['nav'][0])}</a><a href="#exchange">{e(c['nav'][1])}</a><a href="https://github.com/alexar76">{e(c['nav'][2])} ↗</a></nav><nav class="languages" aria-label="{e(c['language'])}">{lang_links}</nav></header>
<main id="main"><section class="hero wrap"><div class="hero-copy"><p class="eyebrow">{e(c['eyebrow'])}</p><h1>{e(c['title'])}</h1><p class="intro">{e(c['intro'])}</p><div class="actions"><a class="button" href="#explore">{e(c['cta'])}<span>↗</span></a><a class="text-link" href="{PROJECTS[0][2]}">{e(c['factory'])} ↗</a></div></div>
<div class="atlas"><div class="atlas-top mono"><span>ATLAS / 01</span><button class="motion" type="button" aria-label="{e(c['pause'])}" data-pause="{e(c['pause'])}" data-play="{e(c['play'])}">Ⅱ</button></div><machine-scene mode="atlas"><div class="fallback" aria-hidden="true"><i></i><i></i><i></i><b>✳</b></div></machine-scene><span class="map-label label-1">AICOM <small>01</small></span><span class="map-label label-2">AIMarket <small>02</small></span><span class="map-label label-3">HESTIA <small>03</small></span><div class="atlas-caption"><span>+</span><p>{e(c['caption'])}</p><span>XYZ ↗</span></div></div></section>
<section class="roles-section wrap"><div class="section-heading"><h2>{e(c['roleTitle'])}</h2><p>{e(c['roleIntro'])}</p></div><div class="roles">{roles}</div></section>
<section id="exchange" class="exchange"><div class="wrap"><p class="eyebrow">01 / {e(c['nav'][1])}</p><div class="section-heading"><h2>{e(c['flowTitle'])}</h2><p>{e(c['flowIntro'])}</p></div><div class="steps">{steps}</div><p class="limit">{e(c['limit'])}</p></div></section>
<section id="explore" class="directory wrap"><p class="eyebrow">02 / {e(c['nav'][0])}</p><div class="section-heading"><h2>{e(c['directory'])}</h2><p>{e(c['directoryIntro'])}</p></div><div class="filter-bar"><div class="filters" role="group" aria-label="{e(c['nav'][0])}">{filters}</div><span class="count mono" aria-live="polite"><span id="project-count">9</span> {e(c['projectLabel'])}</span></div><div class="projects">{projects}</div></section>
<section class="closing wrap"><span class="closing-star" aria-hidden="true">✳</span><h2>{e(c['endTitle']).replace(chr(10), '<br>')}</h2><p>{e(c['endText'])}</p><div class="actions"><a class="button" href="{PROJECTS[0][2]}">{e(c['endCta'])}<span>↗</span></a><a class="text-link" href="{PROJECTS[1][2]}">{e(c['endSecond'])} ↗</a></div></section></main>
<footer class="wrap"><div class="footer-brand">AICOM ECOSYSTEM<p>{e(c['footer'])}</p></div><a href="{docs}">{e(c['docs'])} ↗</a><a href="https://github.com/alexar76/alexar76.github.io">GitHub ↗</a><span class="mono">OPEN / CONNECTED</span></footer></body></html>'''

if __name__ == '__main__':
    for locale, content in CONTENT.items():
        destination = ROOT / ('' if locale == 'en' else locale)
        destination.mkdir(exist_ok=True)
        (destination / 'index.html').write_text(render(locale, content))
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>https://alexar76.github.io{route(l)}</loc></url>' for l in LANGUAGES) + '</urlset>')
    (ROOT / 'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://alexar76.github.io/sitemap.xml\n')
    print('Built five localized ecosystem pages.')
