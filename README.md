# sajeeshnair.com

Plain HTML/CSS blog, hosted on Netlify.

- Write posts in `content/posts/<slug>.md` (front matter: `title`, `date`, `topic`, optional `series`). `topic` is the tag shown above the post title; give several with commas, e.g. `topic: Leadership, 0 to 1`. A post is served at `/posts/<slug>/`.
- Images go in `static/images/` and are referenced as `/images/<file>`.
- About and Podcast pages are `content/about.html` and `content/podcast.html`.
- Styles are in `static/style.css`.

Build with `pip install markdown && python3 build.py`, which regenerates `public/`. Commit `public/` along with the sources; Netlify serves it as is.

Live at https://sajeeshnair.com (Netlify site "sajeeshnair", production branch `main`).
