# Cloudflare Pages deployment

Target: the Newton Prep Cloudflare account, with a separate Robeson Pages project and domain. The user selected a separate GitHub organization owned by johnrharris; the organization is `robeson-org`, administered by johnrharris and institutionally part of Newton Prep. Repository: https://github.com/robeson-org/robeson. Initial deployment succeeded on 2026-09-26 at https://robeson.pages.dev/ from commit a19ebde. Git integration deploys main automatically. The free robeson.org DNS zone was created and its scanned records imported; registrar delegation and Pages custom-domain activation remain pending.

Connect the GitHub repository through Cloudflare’s Pages Git integration. Set production branch `main`, root directory `/`, build command `npm run build`, output directory `dist`, and `NODE_VERSION=24.19.0`. Use the lockfile. No adapter, server, database, or environment secrets are needed for this static site.

Verify the pages.dev deployment before attaching `robeson.org`. Inspect current nameservers and all DNS records first. Add the custom domain inside Pages; do not simply point a DNS record at an unregistered custom domain. If nameserver changes are needed, preserve mail and verification records. Verify HTTPS and both intended hostnames before redirecting anything. Preview deployments should not replace the canonical production URL.

Current documentation: https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/ and https://developers.cloudflare.com/pages/configuration/custom-domains/.

Account login and any GitHub integration authorization must be completed using the user’s account. Do not put tokens in this repository.

## Domain activation handoff — 2026-09-26

At Dynadot replace `ns1.dyna-ns.net` and `ns2.dyna-ns.net` with:

- `aarav.ns.cloudflare.com`
- `kenia.ns.cloudflare.com`

Cloudflare imported A records for `@`, `www`, and `*`, each pointing to `185.53.179.128`. Public checks found no apex MX, TXT, or DS records. The automatic scan is not a complete registrar inventory. Pages will only attach the apex after delegation activates. Then replace the apex parking address through the Pages custom-domain flow and configure www. Check for any obsolete wildcard parking behavior before final cutover.

The initial site contains publication placeholders and a link to the unchanged existing standard. No substantive standard text has been migrated into public Astro pages yet.

## Custom domain connection — 2026-09-26

After the user completed Dynadot delegation and Cloudflare marked the zone active, both `robeson.org` and `www.robeson.org` were attached through Pages. Cloudflare replaced each parking A record with a CNAME to `robeson.pages.dev`. The apex successfully rendered the Robeson homepage over HTTPS in the browser. The www hostname initially returned 522 while Pages verification was pending; a DNS recheck was triggered. The imported wildcard parking record remains unchanged.
