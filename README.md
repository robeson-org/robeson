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

- `src/content/standard/`: canonical standard after migration review.
- `src/content/conformance/`: UIL profile.
- `src/content/crosswalks/`: TAPPS crosswalk.
- `src/content/shadow-uil/`: selected public research.
- `src/content/papers/`: policy papers.
- `src/content/robeson/`: background material.
- `migration/github-pages/`: unchanged source snapshot, excluded from the website.
- `docs/`: authoring, deployment, and migration procedures.

The initial site contains labeled placeholders. Existing substantive text remains on the current GitHub Pages site until migration is verified. Newton Prep is the first/reference implementation, not the owner of the general standard’s identity.
