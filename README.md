# Jacopo Barone — CV

XeLaTeX source for Jacopo Barone's CV, built with [Awesome-CV](https://github.com/posquit0/Awesome-CV). Single-column, one-page layout targeting Data Science and Neuroscience roles.

## Build

Requires Docker:

```powershell
docker compose run --rm latex
```

Outputs `Jacopo_cv.pdf`. GitHub Actions builds and uploads the PDF artifact on every push to `main`.

## Applying for a role

`main` holds the master CV — all content available via commented-out blocks. For each application:

1. `git checkout -b draft`
2. Use the Claude Code agents to tailor:
   - `/jd-parser` — paste or point to the job posting; get structured keywords and requirements
   - `/writing-coach` — review the CV text for AI-voice patterns before submitting
3. Build and review: `docker compose run --rm latex`
4. Tag the submission: `git tag sent/<company>-<role>-<YYYY-MM>`
5. `git checkout main && git branch -d draft`

See `CLAUDE.md` for full authoring conventions, toggleable content, and content integrity rules.
