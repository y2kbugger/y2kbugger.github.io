---
title: blog.y2kbugger.com How To
date: 2017-12-15 23:12:30
modified: 2026-06-17
tags: testing, meta
author: zak kohler
summary: A note to myself on how to write these blog articles and use the features a standardized way.
status: draft
---

A note to myself on how to write articles.

**Articles are Markdown** with images hosted locally under `content/img/`.

## Quick start

Running the dev server, publishing, initial setup, and the repo's branch layout
all live in the [README](../README.md). The notes below are about the
day-to-day *writing* loop.

- Add or edit files in `content/CATEGORY/slug-of-the-page.md`.
- The folder name becomes the category.
- **Every new article starts as `status: draft`** — reset it to draft the
  moment you begin, even before the content exists. The post shows under
  `/drafts` until you flip it to `published`.

## Style guide

- Article titles use `Title Case`; all other headings use `Sentence case like this`.
- No blank line between a heading and its first paragraph is unnecessary in
  Markdown, but keep headings tight and meaningful.
- Favor figures with captions over bare images — every image's alt text renders
  as its caption (see [Images](#images)), so always write a real caption.
- When in doubt, reference this article (e.g. which link style to use).

## Metadata

Every article opens with a YAML front matter block. The block at the very top
of *this* file's source is a live example — refer to it instead of duplicating
one here. The fields:

- `title` — displayed title, `Title Case`.
- `date` / `modified` — `YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`. Both are
  **mandatory**. `date` is the original publish date and never changes. Set
  `modified` equal to `date` when the article is first written, then bump it
  only when the *content* meaningfully changes — new sections, revised steps,
  corrected facts, added images, reworked conclusions. Do **not** bump it for
  cosmetic or mechanical work that leaves the meaning intact: copy editing,
  fixing typos, reformatting, restyling, re-slugging, translating the source
  format (e.g. the reStructuredText → Markdown migration), or moving an image to
  a local path. When in doubt, ask "would a returning reader find something new
  to read?" — if not, leave `modified` alone. The "last modified" line is hidden
  on the rendered page whenever `modified` still equals `date`, so keeping the
  field present-but-equal costs nothing and saves churning the key in and out.
- `tags` — comma-separated.
- `author` — usually `zak kohler`.
- `summary` — one-line description for listings and meta tags.
- `status` — `draft` or `published`; defaults to `draft` (see above).
- `cover` — optional local image, site-absolute path (`/img/...`).

The URL comes from the file basename (`SLUGIFY_SOURCE = 'basename'`); rename the
file to change the slug. The containing folder sets the category.

## Content

Common patterns are below. For everything else:

- Pelican content guide: <https://docs.getpelican.com/en/stable/content.html>
- Python-Markdown reference: <https://python-markdown.github.io/>

Enabled Markdown extensions: `admonition`, `codehilite`, `extra` (tables,
attribute lists, footnotes, definition lists), `meta`, and `captions`.

### Linking

Link to a section *within* this article by its anchor — for example, jump back
to [the metadata fields](#metadata) or down to [recipe ingredients](#recipe-ingredients).

Link to *another* article by its source path with `{filename}` — here's a live
link to the [naan recipe]({filename}/food/naan.md) and one to the
[baguette recipe]({filename}/food/baguette.md).

External inline link: [Jungle Jim's](https://junglejims.com/). Bare URLs also
render: <http://google.com>.

### Comments

To leave a note in the source, use a standard HTML comment:

```text
<!-- a note to self about this section -->
```

This blog is open source, so there's nothing to hide — HTML comments are
readable in the repo and pass through into the published page source, which is
fine. They're stripped from the *visible* page. Keep each comment on its own
line with a blank line above and below.

For a note meant for *readers*, don't use a comment at all — use a `note`
admonition (see [Inline styles](#inline-styles)).

### Images

**All new images are stored locally** in `content/img/` and committed to the
repo. Name them with the convention:

```text
YYYY-MM-DD__slug__description.ext
```

For example: `2024-11-24__pollo-arancia-gremolata__plated.png`.

Reference an inline image with a path relative to the article. The
`markdown-captions` extension wraps every image in a `<figure>` and turns the
alt text into a visible `<figcaption>`, so **write the alt text as a real
caption**, not a terse description:

![Plated pollo all'arancia, finished with gremolata and pan sauce.](../img/2024-11-24__pollo-arancia-gremolata__plated.png)

Keep captions **short — one plain line**. Say what the photo shows; don't
restate the surrounding step or pile on adjectives.

Use a site-absolute path for the `cover` metadata:

```yaml
cover: /img/2024-11-24__pollo-arancia-gremolata__cover2.jpg
```

Image metadata (EXIF/GPS/device info) is stripped automatically — a pre-commit
hook blocks any commit that stages a photo carrying GPS, serial, or device
metadata. If it trips, run `make exif-strip`, re-stage, and commit again. See
the [README](../README.md) for details.

### Recipe ingredients

Wrap the ingredient list in an `ingredients` admonition. The block's own title
bar shows "Ingredients", so no inner `## Ingredients` heading is needed. Use a
**bulleted list** — never a table — and group ingredients with `##` sub-headings,
italicizing prep notes:

!!! ingredients "Ingredients"
    ## Gremolata
    - zest of 2 oranges
    - 1 bunch parsley, _minced_
    - 5 cloves garlic, _minced_
    - olive oil
    - salt
    ## Pan Sauce
    - 1 cup stock
    - olive oil
    - garlic, _minced_
    - Fig Jam

or without sub-headings

!!! ingredients "Ingredients"
    - 2 oreo
    - 2 gallons buffalo milk
    - olive oil
    - garlic, _minced_

This has specific and custom CSS rules.


### Inline styles

- `*italics*` → *italics*
- `**bold**` → **bold**
- `` `inline literal` `` → `inline literal`

Admonitions (notes, warnings, etc.) render live like this:

!!! note
    Body text indented under the admonition. For notes it is BLUE. Indent everything that belongs
    inside it by four spaces.

!!! warning
    Warning text indented under the admonition is RED.

!!! Any "others are just grey"
    This is grey.
    This is also grey.

### Footnotes

Place the reference inline with `[^label]` and the definition anywhere in the body (typically the end):

This sentence has a footnote[^fn-demo] attached to it.

[^fn-demo]: The footnote body renders at the bottom of the article and auto-links back to the reference.

### Code blocks

Fenced blocks with a language hint:

```python
from htooze import world

def test_planet_exists():
    p = world.Planet()
    assert isinstance(p, world.Planet)
```

### Git clone to a tag

```bash
git clone --branch 2019-07-28-PyOhio https://github.com/y2kbugger/sapy.git
```

