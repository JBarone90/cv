# Jacopo Barone's CV

XeLaTeX source for Jacopo Barone's CV, built with [Awesome-CV](https://github.com/posquit0/Awesome-CV). Single-column, one-page layout for Data Science and Neuroscience roles.

---

## CV structure

The CV is written in XeLaTeX and split across focused files:

| File | Contents |
|---|---|
| `Jacopo_cv.tex` | Root document — personal info, packages, section order |
| `cv/summary.tex` | Profile paragraph |
| `cv/experience.tex` | Work history |
| `cv/skills.tex` | Skills table |
| `cv/education.tex` | Education entries |
| `cv/publications.tex` | Publications list (commented out by default) |

`main` is the master branch — all content is present, with sections and bullets that aren't needed for a given role kept as commented-out blocks rather than deleted. This makes it easy to restore content without digging through git history.

### Build

Requires Docker:

```powershell
docker compose run --rm latex
```

Outputs `Jacopo_cv.pdf`. GitHub Actions also builds and uploads the PDF artifact on every push to `main`.

---

## Application workflow

Each job application gets a short-lived `draft` branch. The branch is deleted after submission; a git tag preserves the exact state of what was sent.

### Step by step

```bash
# 1. Start from the master
git checkout main
git checkout -b draft

# 2. Tailor the CV (see below)

# 3. Build and review
docker compose run --rm latex

# 4. Tag before sending (local only — no need to push)
git tag -a sent/<company>-<role>-<YYYY-MM> -m "applied <date>"

# 5. Clean up
git checkout main && git branch -d draft
```

This keeps the branch list clean while preserving a permanent, rebuildable snapshot of every submission.

### Tailoring tools

Two Claude Code agents assist with the process:

**`/jd-parser`** — point it at a job posting (URL, PDF, Word file, or pasted text) and it extracts the role details and key requirements into a structured format ready for tailoring.

**`/writing-coach`** — reads the active CV files and flags AI-voice patterns (filler adverbs, clichés, verb monotony, nominalisation) with suggested rewrites. Run it before every submission.

The Python tooling (`tools/parse_jd.py`) handles file extraction; dependencies are managed with `uv` (`uv sync` to set up).

See `CLAUDE.md` for authoring conventions, content integrity rules, and the full list of toggleable content.
