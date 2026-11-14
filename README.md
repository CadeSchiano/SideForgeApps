# SideForgeApps

A static, dependency-free site for Cade Schiano with two clearly labeled fictional concept demos. The separate personal portfolio stays at https://cadeschiano.github.io/portfolio/.

## Local preview

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000/. Stop the server with Ctrl+C. The relative asset and demo links also work at the case-sensitive GitHub Pages path, `https://cadeschiano.github.io/SideForgeApps/`.

## Edit

Edit copy, $500 pricing, and email links in `index.html`; demo content in `demos/`; colors and responsive layouts in `assets/style.css`. `assets/main.js` updates the copyright year and handles copying the business email. Re-run the build after changes. The generated `dist/` is ignored by Git.

The Fieldstone demo uses one locally saved sample photo. `assets/lawn-mowing.jpg` is [a photo by Gustavo Fring on Pexels](https://www.pexels.com/photo/man-mowing-the-lawn-5163424/) under the [Pexels License](https://www.pexels.com/license/). It illustrates a service type and is not Fieldstone client work. Other images are original local concept illustrations.

## Deployment

This repository's remote points to `CadeSchiano/SideForgeApps`. Publishing is not configured in this checkout. To deploy with GitHub Pages, copy the **contents** of `dist/` to a dedicated publishing branch, push it, and select that branch with `/ (root)` in Settings → Pages. Keep `assets/` and `demos/` beside `index.html`. Do not alter the separate `portfolio` repository. The public URL responded with HTTP 200 during development, but these local changes are not live until published.

## Checks

`python3 scripts/check.py` validates built links and anchors, metadata, SVGs, semantic landmarks, email CTAs, and absence of forms. Browser-based responsive and clipboard checks should be completed at 375px, 768px, and desktop widths before publishing.
