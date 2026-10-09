# Prompts 1 to 3: fact brief, architecture, baseline (Oct 8 2026)

## 1 Client fact brief
Source: INTAKE.md (Maurice Johnson's statements, filled Oct 8 2026), CLAUDE.md, the live site on main.

| Item | Value | Status |
|---|---|---|
| Name | Phoenix Pool Cleaning Pro, d/b/a of Dominion Digital Group | Confirmed |
| Category | Free phone line that transfers pool callers to independent local pool service companies | Confirmed |
| Services | 11 service pages and 7 guides from the Oct 8 keyword data | Confirmed (SERVICES.md) |
| Areas | Phoenix metro: 25 town pages (any town with 10+ searches a month) | Confirmed |
| Address / email | Not displayed / none | Confirmed |
| Phone | (623) 240-0428, tel:+16232400428, only in src/data/site.json; the East Texas number never shown | Confirmed |
| Hours | Answered 24/7 by an automated assistant | Confirmed |
| CTA | Call; secondary links to real pages (How it works, guides); no forms (old contact form retired) | Confirmed |
| Brand | Keep the live site's pool blue #1a4d7a, logo and favicons; add a desert terracotta band color | Decided (docs/decisions.md) |
| Owner name | Not shown | Confirmed |
| Licenses, insurance, reviews, team, awards | None; never claimed for the line or its partner companies | Confirmed rule |
| Analytics, social, GBP | None yet; slots hidden | Missing, deferrable |
| Domain | https://phoenixpoolcleaningpro.com | Confirmed |

Contradictions: the live site used contractor voice ("the technician follows the same checklist",
"chemicals included", "same technician every week") that INTAKE forbids; all of it is gone. Launch
blockers: none in content; going live needs Netlify to publish this branch (not done: no deploys allowed).
Deferred: 77 planned photos (pages show existing photos until they exist).

## 2 Architecture
Not an SSR framework: a static pre-rendered site (Python + Jinja2 build.py, YAML front matter, central
src/data/site.json), the same system as the Houston Air & Heating build. Every title, canonical,
heading, body and JSON-LD block is in the raw HTML; no client rendering. Commands: `python3 build.py`,
`python3 scripts/check.py`, `python3 scripts/similarity.py`, `python3 scripts/check_old_urls.py`,
`python3 scripts/grep_check.py`, `node scripts/responsive_check.js`. The playbook's AI Studio, TanStack
and form-embed steps do not apply and were mapped to this build system.

## 3 Baseline and route matrix
The old live site (repo root on main) was moved to docs/old-site/ as the reference; its photos moved to
src/static/images/ at the same paths. Pre-existing state: hand-written HTML, no build or checks, a
Netlify contact form, unverified water figures and contractor-voice claims. All 83 old URLs (sitemap,
file tree, extensionless and .html forms, photos and retired redirects) are kept or redirected (docs/qa.md).

| Route | Type | Source | Nav | Sitemap | Indexable | Status |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo | yes | yes | rebuilt |
| /services/, /about/, /faq/, /contact/ | core | src/pages/*.html | header | yes | yes | rebuilt |
| /service-areas/, /how-it-works/ | core | src/pages/*.html | header | yes | yes | new |
| /pool-cleaning-maintenance, /pool-repair, /pump-repair, /tile-cleaning | service | src/pages (url: flat) | Services menu, footer | yes | yes | rebuilt at the same URL |
| /pool-service/, /pool-equipment-repair/, /pool-heater-repair/, /pool-resurfacing/, /pool-filter-cleaning/, /green-pool-cleanup/, /pool-leak-repair/ | service | src/pages/<slug>.html | Services menu, footer | yes | yes | new (/pool-equipment-repair/ replaces an old 301) |
| 7 guides (/pool-service-cost/ etc.) | guide | src/pages/<slug>.html | Guides menu, footer | yes | yes | new |
| /<town>-pool-service x 25 | area | src/pages (url: flat) | Service Areas menu, footer | yes | yes | 9 rebuilt, 16 new |
| /privacy-policy.html, /terms.html | legal | src/pages | footer | yes | yes | rewritten |
| /404.html | error | src/pages/404.html | none | no | noindex | new |
| retired stubs and blog posts | 301 | src/static/_redirects | none | no | n/a | kept, several re-pointed |
