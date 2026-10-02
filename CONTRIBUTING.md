# Authoring and releases

Use UTF-8 Markdown, LF line endings, descriptive filenames, normal links, and YAML frontmatter. Avoid MDX, wiki links, and embedded application logic. Use one page title, meaningful headings, and descriptive link text. Cite primary authorities in substantive work; distinguish normative requirements from commentary.

Frontmatter requires `title`, `description`, `status` (`placeholder`, `draft`, or `published`), and numeric `order`. Optional `version` identifies a document version. All documents in `src/content` are publicly rendered, including drafts: keep private research outside this repository. A draft label does not prevent publication.

Use short branches such as `content/student-eligibility` or `site/navigation`, and review a pull request before merging to `main`. Main is the production branch; Cloudflare should create branch previews. Keep commits focused and describe the outcome in their subject. Do not commit secrets, dependencies, or generated output.

Use `site-vX.Y.Z` for site releases and `standard-vX.Y.Z` for formally approved standard releases. Never move an existing release tag. A standard release requires an explicit approved text, source commit, version/date, changelog, and durable downloadable Markdown archive with checksums. Do not turn a working draft number into an adopted standard release. Preserve earlier releases and describe substantive changes. Site releases do not imply standard adoption.

Newton Prep’s original publication contributions are licensed under CC BY 4.0 as specified in LICENSE.md and the site’s Copyright and reuse page. Identify third-party quotations and adaptations with source references; do not apply Newton Prep’s license to underlying third-party rights. Record image-specific rights in captions. Website software and branding are excluded from the publication license.
