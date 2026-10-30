# Design decisions

## Locked (2026-09-23)
- **Mono paper** (neutral grey, faint dot-grid) with **Signal red** accent (#d42a1e, dark mode #ff6a5a).
- **IBM Plex Sans** for UI, **IBM Plex Mono** for dates, labels and nav.
- **Manrope** for post body, at the "Smaller" size (.94rem, 1.78 line height, ~31rem column).
- **Index** post list. Single ~44rem column, mono wordmark, small footer.
- Post page: red kicker (tags), bold sans title, mono meta row.
- Numbered lists use `1.` markers in the accent colour; bullets are accent dots.
- Photo only on the About page.

## Rejected, and why
- Warm cream + terracotta: "looks like the Anthropic website". Avoid cream/beige grounds and orange-ish reds. He wants grey with a shade of red.
- Editorial (big serif): "too loud, big fonts". Quiet: "too dry". Engineer's log with charts: "very boring". Sidebar: "looks like a resume". Covers: "too colorful".
- Highlighter marks everywhere: use emphasis for key things only.
- Serif post fonts (Plex Serif, Source Serif, Literata, Newsreader): "very rounded" / too big. He wants a technical font.
- Banners: converge lines (felt like a copy of a Tim Urban diagram), p99 chart (says nothing about teams), a full-width flame graph ("too loud"), boxed card, tall white band.
- A home intro written by Claude: he only wants his own words.
- Auto-generated diagrams on posts.

## Taste references
manuelmoreale.com (minimalism) and leerob.com (short bio, a few personal touches). He likes seeing options side by side with switchers, rather than separate mockups.

## Visuals
He wants visuals that carry engineering and leadership ideas together (hence the flame graph of team practices). Banner sources and options are in `design/banners/`.
