# Standard migration

Existing repository: https://github.com/newtonprep/interscholastic-standard
Existing publication: https://newtonprep.github.io/interscholastic-standard/
Source commit: `524f5f1ddedf78fe5a2c2cbb3b521993dd15bedf`
Snapshot captured: 2026-09-26.

`migration/github-pages/` preserves all 30 source files byte for byte, with SHA-256 hashes in `migration/source-sha256.json`. The full original history remains in the source repository; the local clone is retained outside this repository. Synced ChatGPT project references were read only and remain untouched.

Before migration:

1. Initial comparison confirmed all 30 files match the synced project mirror byte for byte. Recheck upstream before cutover. The reference includes HS-BASE v0.5; do not assume an older conversation summary is authoritative.
2. Resolve any differences with the author. Preserve wording and version/status labels. Do not synthesize missing text from discussion summaries.
3. Move reviewed publication copies into the content folders, add metadata, and adapt links without changing substantive wording. Keep the original snapshot immutable.
4. Map every old page and heading anchor to its new location. Check citations, internal links, tables, and downloadable files in the built output. Create explicit redirects for migrated old paths on the new domain where useful.
5. Review the pages.dev preview. Keep the old GitHub Pages site available until the new domain and all migration links are verified.
6. Add a migration notice on the old site only after the new publication works. Never delete its history or move old release tags.

The policy paper, standalone profiles, crosswalk, and Robeson background have placeholders until their exact publishable text is available. The earlier identity decision requested a Paul Robeson introduction and photo; obtain the approved text, operator identification, and a rights-verified image before that fuller homepage is published. The initial infrastructure site deliberately contains no invented biography or policy text.

## Migration execution — 2026-09-26

Upstream main still matched source commit 524f5f1ddedf78fe5a2c2cbb3b521993dd15bedf. Imported all 28 Markdown files: 15 proposed standard chapters, 9 supporting notes, 2 authority files, overview, and project README. `migration/routes.json` records source hashes, destination paths, and each changed link target. Only frontmatter and link destinations changed; original Markdown bodies, headings, version numbers, and whitespace are preserved. `scripts/verify-migration.py` checks this initial migration baseline and all built local links and fragments. After intentional substantive revisions, use Git diffs rather than treating this one-time fidelity check as a permanent prohibition on editing.

Source discrepancy retained: the original README describes Eligibility v0.2 while the actual chapter is titled v0.3. No editorial correction or policy update was made during migration. Metadata follows each chapter’s actual heading. External authority URLs are preserved, not reinterpreted or fact-checked as part of this publishing migration.

The new site distinguishes proposed text from supporting notes and displays the not-adopted status. Old `.html` paths on the new origin redirect to their matching chapter; existing heading IDs are verified. The old site will receive a site-wide relocation notice after production verification.
