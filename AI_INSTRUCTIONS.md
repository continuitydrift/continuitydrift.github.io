# AI Instructions for Continuity Drift Website

This repository hosts the [Continuity Drift](https://continuitydrift.github.io/) website, a static site built with [MkDocs](https://www.mkdocs.org/).

## Project Structure
- **`docs/`**: Source code. All content edits happen here.
  - `docs/index.md`: Homepage.
  - `docs/images/`, `docs/sounds/`: Asset directories.
- **`mkdocs.yml`**: Main configuration file.
- **`site/`**: Build artifact. **IGNORED** in git. Do not edit or commit this folder.
- **`gh-pages` branch**: Deployment target. Contains the built HTML.

## Workflow
1.  **Edit**: Modify Markdown files in `docs/`.
2.  **Preview**: Run `mkdocs serve` to view changes at `http://127.0.0.1:8000`.
3.  **Commit**: Stage and commit changes to `master` (or `main`).
4.  **Deploy**: Run `mkdocs gh-deploy` to build and push to `gh-pages`.

## Rules for AI Agents
1.  **Never commit `site/`**: It is in `.gitignore`.
2.  **Content First**: Focus on editing Markdown in `docs/`.
3.  **Relative Links**: Use relative links for internal navigation (e.g., `[Link](path/to/file.md)`).
4.  **No Frontmatter**: Unless explicitly requested, standard Markdown files do not require YAML frontmatter.
