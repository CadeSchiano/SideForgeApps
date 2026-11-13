# SideForgeApps

A standalone, dependency-free business website for Cade Schiano, with two fictional responsive concept demos. This repository does not modify the personal portfolio.

## Preview locally

From this directory, with Python 3 installed:

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. Stop the server with Ctrl+C. There is no package installation or JavaScript build step.

## Edit

- `index.html`: main copy, $500 pricing, scope, payment terms, and email links. Search for `mailto:` when updating the email; there are six links.
- `assets/style.css`: shared layout, colors, responsive rules, and focus states.
- `demos/fieldstone.html` and `demos/oak-and-thread.html`: concept pages.
- `assets/lawn.svg` and `assets/gifts.svg`: lightweight local illustrations used in both demos and main-page previews.
- `assets/main.js`: current copyright year. All content and navigation work without JavaScript.

Run the build again after editing; `dist/` is generated. No analytics, remote assets, forms, backend, or secrets are required. Email buttons open the visitor's mail application, and the email is also displayed for copying.

## Deploy

No deployment is configured or performed. The ready-to-upload website is in `dist/`.

The simplest launch path is to upload **the contents of `dist/`** to your static host's public directory. Keep `assets/` and `demos/` beside `index.html`. Relative links support either a domain root or a subdirectory such as `/BusinessPortfolio/`.

For GitHub Pages on this separate `BusinessPortfolio` repository: copy the contents of `dist/` to a publishing branch, push that branch, then choose it with the `/ (root)` folder in **Settings → Pages → Deploy from a branch**. Do not change the separate personal portfolio repository or its Pages settings. No domain purchase is needed to use a host-provided address. Hosting terms and fees must be checked with the selected provider.

Once the public deployment URL is confirmed, add canonical and `og:url` tags to the three HTML pages using their individual public URLs, then rebuild and upload. No production URL has been invented.

## Validation

`python3 scripts/check.py` checks all three built pages for local file links, section anchors, SVG validity, image dimensions and alt attributes, basic metadata, semantic landmarks, and all six business email CTAs. It also disallows forms and unexpected external assets.

**Remaining prelaunch check:** browser access was unavailable in the implementation session, so rendered visual verification could not be performed. Open the main page and both demos at **375px, 768px, and desktop widths**, checking overflow, text readability, preview composition, and keyboard focus. Click both demo links and return links; test the email CTA with a configured mail application. These checks are not replaced by the static check script.
