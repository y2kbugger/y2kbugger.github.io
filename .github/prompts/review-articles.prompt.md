---
description: "Review the article(s) currently being edited (uncommitted, staged or unstaged) against the blog's sources of truth: content/howto.md, README.md, and AGENTS.md. Use before publishing or committing article changes."
name: "Review changed articles"
argument-hint: "Optionally name an article; otherwise all uncommitted .md articles are reviewed"
agent: "agent"
tools: [search, execute/runInTerminal, edit/editFiles]
---

Review every blog article currently being edited and report findings. The
canonical rules live in three files — treat them as the sources of truth and
link to the specific section for each check:

- [content/howto.md](../../content/howto.md) — how articles are authored
- [README.md](../../README.md) — dev workflow, publishing, EXIF guard
- [AGENTS.md](../../AGENTS.md) — agent behavior rules for this repo

### 0. META
- [ ] Make sure this prompt file is harmonious with all three sources of truth:
    - [content/howto.md](../../content/howto.md) — how articles are authored
    - [README.md](../../README.md) — dev workflow, publishing, EXIF guard
    - [AGENTS.md](../../AGENTS.md) — agent behavior rules for this repo

## 1. Detect the articles under review

Articles being edited are the **uncommitted** changes — staged *and* unstaged.
There may be more than one; review each independently.

```sh
git status --porcelain -- 'content/**/*.md'
```

If the user named a specific article, scope to that one instead. Skip
`content/howto.md` itself (it is a guide, not an article).

## 2. Per-article checklist

For **each** changed article, walk this checklist. Each item links to the rule
that governs it — open the linked section if you are unsure of the exact
requirement.

### Front matter & metadata
- [ ] All required metadata fields present and well-formed — [howto › Metadata](../../content/howto.md#metadata)
- [ ] `title:` front-matter field used (not an `# H1`) — [howto › Metadata](../../content/howto.md#metadata)
- [ ] Slug/category correct for the file's path — [howto › Metadata](../../content/howto.md#metadata)
- [ ] `date` and `modified` honest for the change made — [AGENTS › Keep date and modified honest](../../AGENTS.md#keep-date-and-modified-honest)
- [ ] New/unfinished articles are `status: draft` — [AGENTS › New articles start as drafts](../../AGENTS.md#new-articles-start-as-drafts)

### Content & structure
- [ ] Follows the style guide — [howto › Style guide](../../content/howto.md#style-guide)
- [ ] Internal/external/`{filename}` links resolve — [howto › Linking](../../content/howto.md#linking)
- [ ] Source comments use the standard form — [howto › Comments](../../content/howto.md#comments)
- [ ] Recipes use the `!!! ingredients "Ingredients"` block — [howto › Recipe ingredients](../../content/howto.md#recipe-ingredients)
- [ ] Inline styles / admonitions used correctly — [howto › Inline styles](../../content/howto.md#inline-styles)
- [ ] Code blocks have a language hint — [howto › Code blocks](../../content/howto.md#code-blocks)

### Images
- [ ] Images live in `content/img/` with the `YYYY-MM-DD__slug__description.ext` name — [howto › Images](../../content/howto.md#images)
- [ ] No throwaway pasted names left behind, e.g. `<slug>__image.png` or `![alt text](...)` — [AGENTS › Fixing pasted images](../../AGENTS.md#fixing-pasted-images)
- [ ] Captions are real and **one short line** — [AGENTS › Keep image captions short](../../AGENTS.md#keep-image-captions-short)
- [ ] No dangling/orphaned images for this slug (cross-reference filenames, don't open them) — [AGENTS › Check for dangling/orphaned images](../../AGENTS.md#check-for-danglingorphaned-images-on-every-article-edit)
- [ ] `cover:` points at a real `/img/...` file — [howto › Metadata](../../content/howto.md#metadata)
- [ ] No sensitive content / EXIF concerns in photos — [README › Image metadata (EXIF) guard](../../README.md#image-metadata-exif-guard)

### Spelling & consistency
- [ ] No outstanding cSpell problems; real terms added to the dictionary — [AGENTS › Triage spelling problems](../../AGENTS.md#triage-spelling-problems-on-every-edit)
- [ ] Consistent with the howto and the 3 most recent articles — [AGENTS › Always verify articles against the How To](../../AGENTS.md#always-verify-articles-against-the-how-to)

## 3. Report

For each article, list which items pass and which fail. Fix trivial and
moderate violations directly; surface non-trivial conflicts for review. Then
report, per [AGENTS › Always verify articles against the How To](../../AGENTS.md#always-verify-articles-against-the-how-to):

- **Article ↔ howto conflicts** worth a human's attention.
- **Problems in `content/howto.md` itself** — ambiguous, contradictory, or
  outdated guidance. Flag; do not silently "fix" the howto.
