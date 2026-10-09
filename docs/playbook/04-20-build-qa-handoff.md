# Prompts 4 to 20 (Oct 8 to 9 2026)

**4 Business data.** Every shared value lives in src/data/site.json: name, d/b/a, phone in display and
tel formats (the number appears in no page source; the call label is built from it), 24/7 hours, CTA
labels, origin, disclosures, ROC search URL, empty social and analytics slots, and the service, guide
and area lists with their URLs and town summaries.
**5 Brand.** Tokens in site.css: pool blue #1a4d7a header and first band, desert terracotta #a34a26
second band, navy #0e3654/#0a2238 call band and footer, sun amber #eaa64f buttons with navy text. Logo
and favicons kept; apple-touch-icon rendered from favicon.svg. White text on all bands, dark text on
amber, no white boxes on white (panels and cards carry colored edges), breadcrumbs on white.
**6 Navigation.** Services, Service Areas (three-column menu of 25 towns), Guides, How It Works, About,
FAQ, Contact; EN/ES toggle (Google Translate, loaded only when chosen) and call button top right;
keyboard-operable submenus; quote bar and footer disclosure on every page.
**7 Homepage.** Full-width hero (pool/hero-1.jpg), H1 "Pool Cleaning in Phoenix: One Free Phone Line to a
Local Pool Company", two CTAs. No video exists, so the hero is a preloaded photo.
**8 Services overview.** /services/ with a problem-to-page table, cleaning and repair groups, guides.
**9 Services and guides (18 pages).** Each researched and written for its own keyword by a separate
writer agent, validated with check.py and similarity.py.
**10 Service areas overview.** /service-areas/ grouped North, East and West Valley, with a sourced
one-line summary of each town and the coverage model (no offices).
**11 Town pages (25).** Each built around that town's water provider and hardness, pool drain and
barrier rules and local context, with a "Why [Town] homeowners call the line" section.
**12 About, FAQ, how it works, privacy, terms.** About names no owner; FAQ keeps 6 FAQPage questions plus
more as headings; legal pages rewritten for a phone-only referral line.
**13 Contact and forms.** Phone only. No forms anywhere (check.py fails any form).
**14 Reviews and social.** None exist; none added; icon slots hidden until URLs are set.
**15 Media.** 16 existing photos reused; 77 planned photos in docs/image-list.md with Artistly prompts;
each page shows an existing fallback photo meanwhile. WebP srcsets; heroes preloaded and eager, body
images lazy.
**16 SEO.** check.py: 53 pages, 0 errors, 0 warnings (unique titles and descriptions, canonicals on the
production origin, OG and Twitter tags with absolute images, one H1, one JSON-LD graph per page with
Organization, WebPage, BreadcrumbList, Service, Article and FAQPage as relevant; sitemap.xml lists 52
indexable URLs; 404 is noindex and not in the sitemap; robots.txt points to the sitemap).
**17 Remnant sweep.** Houston, Texas, CenterPoint, HVAC, old phone numbers, other Arizona metros, other
states, company and brand names, placeholders, forms: none found (grep_check.py, check.py).
**Independent fact-check.** Nine separate agents re-checked 726 claims (docs/fact-check.md): 65
corrected, 81 softened, 83 removed. Limitation: source pages could not be opened directly because of the
environment's network policy; verification used search-result summaries.
**18 Responsive.** Chromium via Playwright, every page at 1440/1024/768/390 and samples at 1920/2560: no
horizontal overflow, hero edge to edge and on the left rail, call button above the fold.
**19 Functional.** All internal links and _redirects targets resolve; every phone link is
tel:+16232400428; FAQ accordions are native details elements; no JS errors. 83 old URLs resolve.
Not verified: live 404 status, translation on the real domain, phone routing.
**20 Handoff.** Code and content are on `build`, pushed once; NOT merged and NOT deployed. To go live,
Maurice merges or points Netlify at the branch (publish "dist", already in netlify.toml). Remaining: 77
photos to generate; optionally re-run the fact-check with full web access.
