#!/usr/bin/env python3
"""Build sajeeshnair.com from content/ into public/.

Usage:  pip install markdown && python3 build.py
Posts live in content/posts/<slug>.md and are served at /posts/<slug>/.
"""
import datetime, html, math, pathlib, re, shutil
import markdown

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "public"
SITE = "https://sajeeshnair.com"
NAME = "Sajeesh Nair"
INTRO = "I build fast systems and good teams, and write down what I learn."
INTRO_SUB = "Engineering leader. Performance and systems engineer at heart; these days I write about that and about leading engineers."
NOW = "Rebuilding this site from scratch and getting back to writing."
CUR = ' aria-current="page"'
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600'
         '&family=IBM+Plex+Mono:wght@400;500&family=Manrope:wght@400;500;600&display=swap">')


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    meta = dict(line.split(":", 1) for line in m.group(1).splitlines() if ":" in line)
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    body = m.group(2)
    # python-markdown needs a blank line before a list that follows a paragraph
    body = re.sub(r"(?m)^(?!\s*$)(?!\s*([-*+]|\d+\.)\s)(.+)\n(?=\s*([-*+]|\d+\.)\s)", r"\2\n\n", body)
    meta["slug"] = path.stem
    meta["md"] = body
    meta["date"] = datetime.date.fromisoformat(meta["date"])
    return meta


def render_md(src):
    out = markdown.markdown(src, extensions=["extra", "sane_lists"])
    out = out.replace("<img ", '<img loading="lazy" ')
    return out


def fmt(d, day=True):
    return (f"{d.day} " if day else "") + f"{MONTHS[d.month - 1]} {d.year}"


def page(title, body, *, desc="", path="/", current=""):
    full = NAME if title == NAME else f"{title} · {NAME}"
    nav = "".join(
        f'<a href="{href}"{CUR if current == key else ""}>{label}</a>'
        for key, href, label in [("writing", "/", "writing"), ("about", "/about/", "about"), ("rss", "/index.xml", "rss")])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}{path}">
<link rel="alternate" type="application/rss+xml" title="{NAME}" href="/index.xml">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta name="theme-color" content="#fafafa" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f0f0f" media="(prefers-color-scheme: dark)">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/style.css">
</head>
<body>
<a class="skip" href="#content">Skip to content</a>
<main class="wrap" id="content">
<header class="site"><a class="logo" href="/">sajeeshnair<i>.</i>com</a><nav>{nav}</nav></header>
{body}
<footer><span>&copy; {datetime.date.today().year} {NAME}</span><nav><a href="/index.xml">rss</a><a href="https://www.linkedin.com/in/sajeesh-nair/">linkedin</a></nav></footer>
</main>
</body>
</html>
"""


def excerpt(md_src, n=180):
    txt = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md_src)
    txt = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", txt)
    txt = re.sub(r"[*_`#>]", "", txt)
    txt = " ".join(txt.split())
    return txt if len(txt) <= n else txt[:n].rsplit(" ", 1)[0] + "…"


def index_list(posts):
    rows = []
    for i, p in enumerate(posts, 1):
        rows.append(f'<li><a href="/posts/{p["slug"]}/"><span class="n">{i:02d}</span>'
                    f'<span class="t">{html.escape(p["title"])}</span>'
                    f'<time datetime="{p["date"].isoformat()}">{fmt(p["date"], False)}</time></a></li>')
    return '<ul class="rows">' + "".join(rows) + "</ul>"


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT)
    posts = sorted((parse(f) for f in (ROOT / "content/posts").glob("*.md")), key=lambda p: p["date"], reverse=True)

    for p in posts:
        p["html"] = render_md(p["md"])
        words = len(re.sub(r"<[^>]+>", " ", p["html"]).split())
        p["words"], p["mins"] = words, max(1, math.ceil(words / 230))
        p["desc"] = excerpt(p["md"])

    series = sorted([p for p in posts if p.get("series")], key=lambda p: p["date"])

    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        pn = ""
        if older:
            pn += f'<a class="older" href="/posts/{older["slug"]}/"><small>Older</small><b>{html.escape(older["title"])}</b></a>'
        if newer:
            pn += f'<a class="newer" href="/posts/{newer["slug"]}/"><small>Newer</small><b>{html.escape(newer["title"])}</b></a>'
        box = ""
        if p.get("series"):
            items = "".join(
                f'<li><a href="/posts/{s["slug"]}/"{CUR if s is p else ""}>{html.escape(s["title"].split(", ", 1)[-1])}</a></li>'
                for s in series)
            box = f'<nav class="series" aria-label="Series"><b>{html.escape(p["series"])} &middot; series</b><ol>{items}</ol></nav>'
        wide = " wide" if "<img" in p["html"] else ""
        body = f"""<a class="back" href="/">&larr; all writing</a>
<div class="post-head">
<span class="kicker">{html.escape(p["topic"])}</span>
<h1>{html.escape(p["title"])}</h1>
<div class="meta"><time datetime="{p["date"].isoformat()}">{fmt(p["date"])}</time><span>{p["words"]:,} words</span><span>{p["mins"]} min read</span></div>
</div>
{box}<article class="post{wide}">
{p["html"]}
</article>
<nav class="pn" aria-label="More posts">{pn}</nav>"""
        d = OUT / "posts" / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(p["title"], body, desc=p["desc"], path=f"/posts/{p['slug']}/", current="writing"), encoding="utf-8")

    home = f"""<section class="hello"><h1>{INTRO}</h1><p>{INTRO_SUB}</p></section>
<div class="now"><b>Now</b><span>{NOW}</span></div>
{index_list(posts)}"""
    (OUT / "index.html").write_text(page(NAME, home, desc=INTRO_SUB, current="writing"), encoding="utf-8")
    (OUT / "posts").mkdir(exist_ok=True)
    (OUT / "posts/index.html").write_text(
        page("Writing", '<section class="hello"><h1>Writing</h1></section>' + index_list(posts), desc="All posts", path="/posts/", current="writing"),
        encoding="utf-8")

    for name in ("about", "podcast"):
        src = (ROOT / "content" / f"{name}.html").read_text(encoding="utf-8")
        title = re.search(r"<!--\s*title:\s*(.*?)\s*-->", src).group(1)
        d = OUT / name
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(title, src, desc=f"{title} · {NAME}", path=f"/{name}/", current=name), encoding="utf-8")

    (OUT / "404.html").write_text(page("Not found", '<section class="hello"><h1>That page isn\'t here.</h1><p><a href="/">Back to all writing</a></p></section>', desc="Not found"), encoding="utf-8")

    # RSS (old Hugo feed lived at /index.xml; keep it there and at /posts/index.xml)
    items = "".join(f"""<item><title>{html.escape(p["title"])}</title><link>{SITE}/posts/{p["slug"]}/</link><guid>{SITE}/posts/{p["slug"]}/</guid>
<pubDate>{datetime.datetime.combine(p["date"], datetime.time()).strftime("%a, %d %b %Y 00:00:00 +0000")}</pubDate><description>{html.escape(p["html"])}</description></item>
""" for p in posts)
    rss = f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>
<title>{NAME}</title><link>{SITE}/</link><description>{html.escape(INTRO_SUB)}</description><language>en-us</language>
<atom:link href="{SITE}/index.xml" rel="self" type="application/rss+xml"/>
{items}</channel></rss>
"""
    (OUT / "index.xml").write_text(rss, encoding="utf-8")
    (OUT / "posts/index.xml").write_text(rss, encoding="utf-8")

    urls = ["/", "/about/", "/podcast/", "/posts/"] + [f"/posts/{p['slug']}/" for p in posts]
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="utf-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                     + "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls) + "</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
    print(f"built {len(posts)} posts into {OUT}")


if __name__ == "__main__":
    build()
