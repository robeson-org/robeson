# Robeson

A Texas Interscholastic Competition Project.

Markdown is the canonical source. Astro produces a static site for Cloudflare Pages. This repository is independent of Newton Prep’s site.

## Local use

Install Node.js 24 LTS, then run:

```sh
npm ci
npm run dev
```

Open the address printed by Astro. Before publishing, run `npm run build` and `npm run format:check`.

## Structure

- `src/content/standard/`: proposed standard, supporting notes, and authority references.
- `src/content/conformance/`: UIL profile.
- `src/content/crosswalks/`: TAPPS crosswalk.
- `src/content/shadow-uil/`: selected public research.
- `src/content/papers/`: policy papers.
- `src/content/robeson/`: background material.
- `migration/github-pages/`: unchanged source snapshot, excluded from the website.
- `docs/`: authoring, deployment, and migration procedures.

The standard’s 28 Markdown documents have been migrated, preserving substantive wording and draft status. Other publication areas remain labeled placeholders. The original GitHub Pages site remains an archive. Newton Prep is the first/reference implementation, not the owner of the general standard’s identity.
