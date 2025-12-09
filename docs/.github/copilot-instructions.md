(# Copilot instructions — continuitydrift.github.io
 # Copilot instructions — continuitydrift.github.io

This repo is a content-first static site: the `docs/` tree contains the Markdown source that is (most likely) published directly by GitHub Pages or served as static files. The guidance below is intentionally narrow and practical so an AI agent can make safe, useful edits without guessing owner intent.

## Quick summary / contract
- Inputs: edits to files under `docs/` (Markdown, images, sounds).
- Outputs: small, focused content changes that preserve style and links; new pages when requested.
- Error modes: don't add build tools or opaque config; avoid changing link styles or mass restructuring without approval.

## What to read first
- `docs/index.md` — homepage and canonical link style (directory-style links with trailing slash).
- `docs/words/index.md`, `docs/images/index.md`, `docs/sounds/index.md` — examples of how content pages are structured.
- `docs/.github/copilot-instructions.md` — this file (update it if conventions evolve).

## Discoverable conventions (follow these exactly)
- Keep files as plain Markdown. Examples do not use YAML frontmatter — do not add frontmatter unless explicitly requested.
- Internal links use relative paths to directories with trailing slashes. Example: use the directory path `words/` in your link target.
- Use HTML comments for inline notes when needed: `<!-- comment -->`.
- New content pages should mirror existing layout: a single top-level heading, short paragraphs, and relative links. Example file: `docs/words/new-word.md` beginning with `# Title`.

## Developer workflow (how to preview / sanity-check locally)
- No build or CI config is present under `docs/`; assume GitHub Pages or a plain static host.
- To preview locally, serve the `docs/` folder as static files, for example:

```bash
python3 -m http.server --directory docs 8000
```

Open `http://localhost:8000/` in a browser to sanity-check links and basic layout.

## What to avoid (project-specific)
- Do NOT add site generators, bundlers, package manifests, or other repo-level tooling without owner approval.
- Avoid bulk refactors of link style or mass renames — small, targeted edits are preferred.

## Integration and assets
- Media lives under `docs/images/` and `docs/sounds/`. Keep paths relative and avoid embedding large binary data directly in PRs when unnecessary.

## When to ask the human
- Before introducing a site generator (Jekyll/Hugo/MkDocs) or adding CI/publishing workflows.
- If you find Markdown files that include YAML frontmatter, a config file, or any `Gemfile`/`package.json` — stop and confirm intent.

## Examples (concrete)
- Preserving a link: edit `docs/index.md` but keep the directory-style link target `words/` (relative path with trailing slash).
- Adding a page: create `docs/words/new-word.md` with `# Title` then body text; add a link from `docs/words/index.md`.

If anything here is unclear or you want more prescriptive rules (frontmatter schema, CI steps, publishing details), tell me which area to expand and I will iterate.
