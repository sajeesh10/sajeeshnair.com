# Banner options

Original SVG banners drawn for the home page in September 2026. Nothing in this folder is published; the live banner is `content/banner.svg`, which `build.py` inlines into the home page.

- `round2-c-flamegraph-chosen.svg`: the one in use.
- `round1-*`: converge lines, p99 latency chart and a first flame graph.
- `round2-*`: the reworked flame graph, a distributed trace, a `top` screen and a git graph.
- `options-round2.html`: the round 2 comparison page (paste it into a page with a body to preview).
- `gen_round1.py`, `gen_round2.py`: the scripts that drew them. Run one and it writes `banners.json` (or `banners2.json`) with the SVG markup.

The SVGs use CSS classes coloured from the site's tokens. Each file here carries its own copy of those styles so it opens on its own in a browser.
