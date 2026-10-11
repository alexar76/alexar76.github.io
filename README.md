# AICOM Ecosystem — machine economy atlas

Standalone, multilingual GitHub Pages site at **https://alexar76.github.io/**.
The AICOM product factory lives at **https://magic-ai-factory.com/**.
This site explains the ecosystem's roles and projects; it no longer redirects to modeldev.

## Edit and preview

Canonical source: `scripts/github-io/` in [alexar76/aicom](https://github.com/alexar76/aicom).

```sh
python3 build.py
python3 validate.py
python3 -m http.server 3408 --bind 127.0.0.1
```

Open `http://127.0.0.1:3408/` (English), `/ru/`, `/es/`, `/fr/` or `/zh/`.
Edit `content.json` for copy, `build.py` for page structure and project links,
`assets/site.css` for layout, and `assets/site.js` for filtering and pause controls.
All five HTML pages are generated and committed, so GitHub Pages needs no build dependencies.
No analytics, third-party font requests, authentication, or backend are required.

`assets/scene.js` and `assets/vendor/` contain a self-hosted Three.js illustration.
It supports pointer parallax, reduced motion, pause, offscreen suspension, and an HTML/CSS fallback.
The illustration is conceptual, not telemetry. All navigation and content work without WebGL or JavaScript.
Three.js licensing is retained in `assets/vendor/LICENSE`.

## Publishing

Review the generated files before publishing. From the monorepo,
`./scripts/publish_github_io.sh` mirrors this directory to the user-site repository.
An ordinary pull request in this repository is also supported. GitHub Pages serves `main` at `/`;
project Pages such as `/gaia/` are separate repositories and are unaffected.
Do not edit generated HTML without updating `content.json` or `build.py`.
