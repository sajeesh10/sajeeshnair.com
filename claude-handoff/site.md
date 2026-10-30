# The site

## Where it lives
- Live: https://sajeeshnair.com (went live 2026-09-24).
- Repo: https://github.com/sajeesh10/sajeeshnair.com, branch `main`.
- Hosting: Netlify site **"sajeeshnair"** (app.netlify.com/projects/sajeeshnair). Production branch `main`, publish dir `public`, build command empty (see `netlify.toml`, which also has 301 redirects for old Hugo `/page/*` URLs). Pushing to `main` deploys in a minute or two.
- The old Hugo site in `sajeesh84/sajeeshnair.com` is retired. Leave it alone; he chose not to transfer it.
- From the cloud container, sajeeshnair.com and api.netlify.com were blocked by the network proxy. Check live pages with WebFetch, and deploys with the Netlify connector if the new login adds it (it can read deploys but could not change the linked repo).

## Repo layout
```
build.py              generator: content/ -> public/
content/posts/*.md    one file per post, served at /posts/<slug>/
content/about.html    About page (raw HTML, first line is <!-- title: About -->)
content/podcast.html  old podcast page (no longer linked from nav)
content/banner.svg    flame graph banner, inlined on the home page
static/style.css      all styles
static/images/        images, referenced as /images/<file>
design/banners/       banner options and generator scripts (not published)
claude-handoff/       this folder (not published)
public/               generated output, committed
```

## Build
```
pip install markdown
python3 build.py
```
Then commit `public/` together with the source change and push to `main`. Check the changed page in light and dark mode before pushing.

## Post front matter
```
---
title: Engineering Management in 2026
date: 2026-10-06
topic: Leadership, 0 to 1
---
```
- `topic:` is the tag line shown in red above the title. Several tags go comma-separated and render as `LEADERSHIP · 0 TO 1`. Any text works; no setup needed. Tags in use: **Leadership, 0 to 1, Sales, Performance engineering, Cloud**.
- Tags are labels only; there are no per-tag listing pages (offered, never requested).
- `archive: yes` is only for the old 2014-2018 technical posts. Never put it on new posts.
- `series:` groups the "Path to Performance Engineering" parts.
- The slug is the file name.

## Home page, top to bottom
1. **Flame graph banner** (`content/banner.svg`), inside the 44rem column, no box or border. Systems side grey, teams side pale red, hot path main > teams > trust > feedback > one_on_ones > coaching > growth in Signal red, `main` frame charcoal.
2. **Intro** (`INTRO` in build.py), his own words with minimal grammar fixes, styled as a quote: IBM Plex Sans italic 300, .88rem, muted grey, 2px red left rule. It ends on "human slop" having a new meaning in a world of AI slop.
3. A rule, then a red mono **"WRITING · N posts"** label and the post list (Index style): leadership posts plus the Druva essay.
4. A link to **/archive/** ("Earlier technical writing"): the 9 old performance/AWS posts, dated 2014-2018.

There is no "Now" row (he asked to remove it) and no Product Pupil podcast link (removed).

## Every post
- Ends with the footer note: **"Written by a human. Expect the odd typo and grammar slip."** (`HUMAN_NOTE` in build.py; added automatically).
- Gets GoatCounter scroll-depth events (below).

## About page
`content/about.html`. Photo appears **only** here. It ends with the links **LinkedIn · Twitter · RSS** in red (LinkedIn /in/sajeesh-nair, Twitter/X @sajeesh84, RSS /index.xml).

## Analytics
- GoatCounter, dashboard **https://sajeesh.goatcounter.com**, on every page via `page()` in build.py.
- Posts also load `SCROLL_JS`, which sends one event per view at 25/50/75/100% of `article.post`, as paths `scroll-25/<slug>` … `scroll-100/<slug>`.
- Claude has **never had API or network access** to GoatCounter (the proxy blocked it, and no token was set up). To get stats, ask him for a CSV export: GoatCounter → Settings → Export, then attach the file. Build views, top referrers and scroll completion (scroll-100 ÷ views) per post from it.
