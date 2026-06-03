# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

XeLaTeX source for Jacopo Barone's CV, built with the [Awesome-CV](https://github.com/posquit0/Awesome-CV) class (`awesome-cv.cls`). Single-column layout, one page, targeting Data Science and Neuroscience roles.

## Building

**Locally (requires Docker):**
```powershell
docker compose run --rm latex
```
This runs `xelatex Jacopo_cv.tex` twice inside `texlive/texlive:latest-full` and writes `Jacopo_cv.pdf`. Use this command directly — `build.ps1` has encoding issues.

**CI:** GitHub Actions (`.github/workflows/build.yml`) builds on every push/PR to `main` using `xu-cheng/latex-action@v3` with XeLaTeX and uploads the PDF as an artifact named `Jacopo_CV` (retained 30 days).

## File layout

| File/Dir | Purpose |
|---|---|
| `Jacopo_cv.tex` | Root document — personal info, packages, two-column structure |
| `cv/experience.tex` | Work history (`\cvsection{Experience}`) |
| `cv/skills.tex` | Skills table (`\cvsection{Skills}`) |
| `cv/education.tex` | Education (`\cvsection{Education}`) |
| `cv/publications.tex` | Publications (currently not included in the main doc) |
| `awesome-cv.cls` | Upstream class file — avoid editing |
| `fonts/` | Bundled fonts referenced via `\fontdir[fonts/]` |
| `logos/` | Institution/company logos used in entries |
| `references.bib` | BibTeX entries (biblatex wiring is commented out) |

## Content integrity

- **Never fabricate** — do not invent metrics, achievements, tools, or responsibilities Jacopo did not perform. Reframing and emphasising real work is encouraged; crossing into fiction is not.
- Adapt existing bullet text creatively (stronger verbs, sharper framing, JD-mirrored language) but only if the underlying claim remains true.
- If a JD requires a skill or experience genuinely absent from the CV, flag the gap explicitly rather than papering over it.

## ATS compatibility

This CV must remain parseable by Applicant Tracking Systems. Always maintain:
- Single-column layout (no `paracol` or multi-column environments for content)
- Real text for all CV content — no text embedded in images or graphics
- Standard section headings (Experience, Education, Skills, etc.)
- No text boxes, headers/footers carrying substantive content, or decorative tables

**If the user requests a design change that would break ATS readability** (e.g. two-column layout, graphical skill bars, infographic elements), warn them before implementing and suggest an ATS-safe alternative.

## Application workflow

`main` is the **master branch** — all content available (all bullets, publications, BSc, full education). Never strip content from main; only add.

### Branching strategy (keep the repo clean)

Use a single reusable `draft` branch for active tailoring. The full history is preserved via tags, not branches.

```
# Start a new application
git checkout main && git checkout -b draft

# Tailor, build, review…

# When ready to submit — tag the state, then delete the branch
git tag sent/<company>-<role-slug>-<YYYY-MM>
git checkout main && git branch -d draft
```

The branch list stays clean (`main` only). Tags are the permanent record of every submission.

### Tailoring steps
1. **Profile summary** (`cv/summary.tex`) — rewrite to mirror the JD's language; this is the highest-leverage change
2. **Bullet selection** — comment in/out bullets in `cv/experience.tex` to match what the role values
3. **Position title** (`Jacopo_cv.tex`) — adjust `\position{}` if the framing differs (e.g. "Computational Neuroscientist" for research roles)
4. **Section order** — for research/academic roles, move education before experience and restore `\input{cv/publications.tex}`
5. **Page budget** — one page for industry; two pages acceptable for academic/research roles
6. Build and review: `docker compose run --rm latex`

### How to present a job description

Paste the JD using this format so keywords and priorities can be extracted cleanly:

```
Role: <title>
Company: <name>
Type: industry | academic | government
---
<full JD text or bullet-point requirements>
---
Notes: <any angle you want to emphasise, optional>
```

### When given a job description
- Extract the 5–8 most distinctive keywords/phrases from the JD
- Check each against the current profile summary and active bullets
- Rewrite the profile summary first, then swap bullets to match
- Prefer the JD's exact phrasing over synonyms where natural
- Flag any genuine skill gaps rather than obscuring them

### Toggleable content
| Content | File | How to restore |
|---|---|---|
| Publications | `Jacopo_cv.tex` | Uncomment `\input{cv/publications.tex}` |
| BSc entry | `cv/education.tex` | Uncomment the `\cvedu{BSc…}` block |
| 3rd bullet per role | `cv/experience.tex` | Uncomment the `% \item {…}` lines |
| Great Expectations bullet (DBT) | `cv/experience.tex` | Uncomment |
| SLURM/HPC bullet (PhD) | `cv/experience.tex` | Uncomment |

## Authoring conventions

- Each section lives in its own file under `cv/` and is pulled in via `\input{}` from the root.
- Unused content (alternative bullet points, commented-out sections) is kept as `% …` comments rather than deleted, so variants can be restored easily.
- The `\jobstyle{}` + inner `itemize` pattern is used in experience entries to get bullet-indented sub-items inside `cventries`.
- `\columnratio{0.6,0.4}` and `\setlength{\columnsep}{1cm}` control the two-column split and gap — tweak these in `Jacopo_cv.tex` to rebalance the layout.
- The biblatex/`references.bib` pipeline is fully wired but commented out; uncomment the three lines in the bibliography config block and `\input{cv/publications.tex}` to re-enable it.
