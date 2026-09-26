# Cloudflare Pages deployment

Target: the Newton Prep Cloudflare account, with a separate Robeson Pages project and domain. The user selected a separate GitHub organization owned by johnrharris; the chosen handle is `robeson-org`, which passed GitHub’s availability check. Organization creation awaits the user’s Terms acceptance. No deployment or DNS change has been performed.

Connect the GitHub repository through Cloudflare’s Pages Git integration. Set production branch `main`, root directory `/`, build command `npm run build`, output directory `dist`, and `NODE_VERSION=24.19.0`. Use the lockfile. No adapter, server, database, or environment secrets are needed for this static site.

Verify the pages.dev deployment before attaching `robeson.org`. Inspect current nameservers and all DNS records first. Add the custom domain inside Pages; do not simply point a DNS record at an unregistered custom domain. If nameserver changes are needed, preserve mail and verification records. Verify HTTPS and both intended hostnames before redirecting anything. Preview deployments should not replace the canonical production URL.

Current documentation: https://developers.cloudflare.com/pages/framework-guides/deploy-an-astro-site/ and https://developers.cloudflare.com/pages/configuration/custom-domains/.

Account login and any GitHub integration authorization must be completed using the user’s account. Do not put tokens in this repository.
