# Continuity Drift Website

This is the source code for the [Continuity Drift](https://continuitydrift.github.io/) website, built with [MkDocs](https://www.mkdocs.org/).

## How to Update the Site

### 1. Make Changes
Edit the Markdown files in the `docs/` folder.

### 2. Preview Locally (Recommended)
To see your changes before publishing, run:
```bash
mkdocs serve
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser. Press `Ctrl+C` in the terminal to stop the server.

### 3. Save Your Work (Git)
Save your changes to the history of your project:
```bash
git add .
git commit -m "Describe your changes here"
git push origin master
```

### 4. Publish (Deploy)
To update the live website:
```bash
mkdocs gh-deploy
```
This builds the site and pushes it to the `gh-pages` branch, which GitHub uses to serve the website.
