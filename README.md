# tianyizhou.github.io

Personal academic website of [Tianyi Zhou](https://tianyizhou.github.io), built on the
[al-folio](https://github.com/alshedivat/al-folio) Jekyll theme (v1.x).

## Where things live

| What | File(s) |
| --- | --- |
| Bio / homepage | `_pages/about.md` |
| **Publications (single source of truth)** | `_bibliography/papers.bib` — one BibTeX entry per paper. Extra fields: `abbr` (venue badge), `pdf`, `code`, `website`, `supp`, `slides`, `poster`, `video`, `arxiv`, `award` + `award_name`, `selected = {true}` (shows on homepage), `preview` (thumbnail in `assets/img/publication_preview/`), `keywords = {topic:<slug>;}` (drives the Research page) |
| Research-by-topic page | `_pages/research.md` — each section is a `{% bibliography --query @*[keywords ~= topic:<slug>;] %}` |
| News | one file per item in `_news/` (`YYYY-MM-DD-*.md`); homepage shows the latest 8 |
| Group | `_data/group.yml` (rendered by `_pages/group.md`) |
| Co-author links in paper lists | `_data/coauthors.yml` |
| Venue badge colours | `_data/venues.yml` |
| CV | `_data/cv.yml` (RenderCV format). Put a PDF at `assets/pdf/cv.pdf` and set `cv_pdf` in `_pages/cv.md` |
| Teaching | `_teachings/*.md` + `_pages/teaching.md` |
| Social links | `_data/socials.yml` |
| Accent colour | `_sass/_themes.scss` (overrides the theme default) |

## Adding a paper

Append a BibTeX entry to `_bibliography/papers.bib`, e.g.

```bibtex
@inproceedings{li2027example,
  abbr      = {ICLR},
  title     = {Paper title},
  author    = {Li, Ming and Zhou, Tianyi},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2027},
  pdf       = {https://arxiv.org/pdf/2701.00001},
  code      = {https://github.com/tianyi-lab/example},
  award_name = {Oral}, award = {Oral (top 1.5%)},
  keywords  = {topic:llm__post-training-and-reasoning;},
  selected  = {true}
}
```

Commit and push — GitHub Actions builds the site and deploys it to the `gh-pages` branch.

## Local preview

```bash
bundle install && bundle exec jekyll serve   # http://localhost:4000
# or: docker compose up
```

`scripts/migration/` contains the one-off converters used to migrate the old academicpages markdown lists into `papers.bib` and `_news/`.
