# AGENTS.md

Instructions for AI agents working in this blog repository.

## Remove a TODO when you _start_ it, not when you finish

The `# TODO` list in `README.md` tracks work that has not been picked up yet.
When you begin working on a TODO item, delete it from the list in the same
change — don't wait until the work is finished. Work in progress lives in the
git diff (e.g. `git diff write`), so the README only needs to list what hasn't
been started. A TODO that's still present means nobody has touched it.

## Make it RIGHT, not just WORKING

Fix root causes, not symptoms. When something is broken, find and repair the
underlying defect instead of routing around it with a one-off workaround.

A concrete example: when `uv sync` failed to parse `pyproject.toml`, the
*workaround* was to install the package separately into the existing `.venv`;
the *right* fix was to repair the malformed `name = ""` field (and the stale
`uv.lock` that mirrored it) so the normal `uv sync` workflow works for everyone,
every time. Prefer the latter.

Applied generally:

- Treat a failing standard workflow (build, sync, lint, test) as a bug to fix,
  not an obstacle to bypass.
- Don't disable checks, pin around breakage, hardcode, or special-case to make
  output appear correct — fix the thing that is actually wrong.
- If the proper fix is genuinely out of scope, say so explicitly and flag it
  rather than quietly shipping a workaround.

## Always verify articles against the How To

[content/howto.md](content/howto.md) is the canonical guide for how articles are
authored (Markdown, front matter, links, images, recipe ingredient blocks,
draft status, naming conventions, etc.).

Also referenced and compare against the last 3 most recent articles to ensure consistency with the How To.
It will help you draft, but it will also help me keep the howto consistent and up-to-date with what I am actually writing.

**After every change to an article**, re-read the relevant parts of
`content/howto.md` and verify the article follows *all* of its rules. Do this
check on every edit, not just the first.

In your end-of-turn summary, report:

- **Non-trivial conflicts** between the article and `content/howto.md` — e.g. a
  recipe that does not use the `!!! ingredients "Ingredients"` block, a published article still on a
  Google-hosted image, an `# H1` title instead of a `title:` front-matter field,
  a wrong slug/category, or a missing required metadata field. Skip purely
  cosmetic nits, and fix trivial or even moderately straight forward violations.
- **Problems in `content/howto.md` itself** — ambiguities, contradictions, or
  possible correctness errors such as invalid or deprecated syntax, links that
  no longer resolve, or guidance that conflicts with `pelicanconf.py` or the
  installed Markdown extensions. Flag these rather than silently following them.

Do not auto-"fix" the How To or force an article to comply when the rule itself
looks wrong — surface it for review instead.

## Fixing pasted images

When I paste a screenshot into an article, the `markdown.copyFiles.destination`
setting (in [.vscode/settings.json](.vscode/settings.json)) drops it straight
into `content/img/` already named with the article basename and a throwaway
suffix — e.g. `baguette__image.png` / `baguette__image-1.png` — and writes a
`![alt text](../img/baguette__image.png)` reference. So it's already in the
right folder with the right relative path; it just needs a real date-stamped
name and a caption. Fix every one of these as part of the edit, without being
asked:

1. **Look at the image first.** Open the file (e.g. in the integrated browser)
   and actually view it — never caption blind. The caption must describe what
   the photo really shows.
2. **Rename** it in place under `content/img/` to the full convention from
   [content/howto.md](content/howto.md): `YYYY-MM-DD__slug__description.ext`.
   Add the article's `date` prefix and replace the throwaway `image` suffix with
   a short `description` of the shot (e.g. `cold-bulk`, `cooling`). Match the
   image to the section it sits under.
3. **Rewrite the reference** to the renamed `../img/...` path with a real,
   **short one-line caption** (see the captions rule above) — never leave
   `![alt text]`.
4. **Privacy/EXIF:** these are real photos. Flag anything sensitive visible in
   the frame (faces, addresses, prescription labels, screens) for review, and
   remember the pre-commit hook strips EXIF/GPS — run `make exif-strip` if it
   trips.

## New articles start as drafts

Every new article must be created with `status: draft` in its front matter, even
before the content exists. Only flip to `status: published` when explicitly asked.

When creating or templating a new article, always set both `date` and `modified`
to **today's date** — never copy a date from another article or leave a
placeholder.

## Keep image captions short

Image alt text renders as a visible `<figcaption>` (see
[content/howto.md](content/howto.md)), so write a real caption — but keep it to
**one short plain line**. Say what the photo shows; don't restate the
surrounding step or pile on adjectives.

## Check for dangling/orphaned images on every article edit

After editing an article, check that no images in `content/img/` belonging to
that article are unreferenced. A dangling image is any file whose slug prefix
matches the article's slug but that does not appear in the article's Markdown
source. To check: grep `content/img/` for files matching the article slug, then
confirm each one appears in the article. Delete or flag any that are not
referenced — don't leave orphaned images silently accumulating.

## Keep `date` and `modified` honest

Both `date` and `modified` are mandatory front-matter fields (see
[content/howto.md](content/howto.md)). Enforce these automatically — do them as
part of the relevant edit, without being asked:

- **Publishing (`draft` → `published`):** when you flip `status` to `published`,
  set `date` to the current date (the article is being published *now*; the
  original `date` of a never-published draft is just a placeholder). Set
  `modified` equal to the new `date` at the same time. Sometimes a historical
  `date` is intended and should be preserved, so just ask about it.
- **Content changes to a published article:** whenever you make a *substantial
  content* change (new sections, revised steps, corrected facts, added images,
  reworked conclusions — the same bar `content/howto.md` uses), bump `modified`
  to the current date. Do **not** touch `modified` for cosmetic or mechanical
  edits (copy editing, typos, reformatting, restyling, re-slugging, format
  migration, moving images) — leave it equal to whatever it was.

When `modified` equals `date` the rendered page hides the "last modified" line,
so always keep `modified` present (matching `date` when there has been no
post-publish content update) rather than adding and removing the key.

## Triage spelling problems on every edit

First, open each changed file in the editor, this allows CSpell to detect spelling problems in context.

The cSpell extension reports misspellings as **Information**-level problems (see
`.vscode/settings.json`, `cSpell.diagnosticLevel`). After editing any content,
check the Problems panel and resolve **every** spelling problem you introduced or
touched — do not leave them outstanding. For each one, do exactly one of:

1. **Correct it** if it is a genuine typo.
2. **Add it to the dictionary** if it is a correct domain term or proper noun
   (a false positive). Add the word to [.cspell/blog-words.txt](.cspell/blog-words.txt)
   (one word per line), which is the workspace dictionary configured with
   `addWords: true`. The `cSpell.words` array in `.vscode/settings.json` is the
   legacy location; prefer the dictionary file for new words.

Never suppress a real misspelling by adding it to the dictionary, and never
leave a genuine domain term flagged.
