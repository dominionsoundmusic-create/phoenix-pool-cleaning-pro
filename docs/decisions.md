# Decisions log (Playbook 2.0 rebuild, Oct 8 2026)

Maurice was not available to approve anything during this run (CLAUDE.md: run straight through). Each
decision below was made from INTAKE.md, CLAUDE.md, the keyword data and the live site, and can be
reversed later.

## Build system and structure
1. **Build system copied from Houston Air & Heating (branch `build`), words not copied.** build.py,
   scripts/check.py, similarity.py, check_old_urls.py, grep_check.py, keyword_plan.py,
   responsive_check.js, the Jinja templates and macros, site.css, site.js, the self-hosted Inter woff2
   font, the site.json structure and netlify.toml (`publish = "dist"`) came from
   dominionsoundmusic-create/houston-hvac-pro. The speed work is unchanged: WebP srcset at
   480/800/1200/1600/1920, preloaded hero with fetchpriority high, woff2 font. The full-width text layout
   (text, photos, cards and bands share one left and right rail) is unchanged. Every shared template
   sentence (how-it-works strip, license note, call band, call box, disclosure) was rewritten for a pool
   line, and scripts/similarity.py fails any Phoenix page that shares an 8-word run with any Houston page.
2. **Old live site moved to docs/old-site/.** It stays in the repo as the reference for every old URL
   (scripts/check_old_urls.py reads it). Its photos moved to src/static/images/ at the same paths
   (/images/img-01.jpg, /images/pool/*.jpg), so old image URLs still resolve. Netlify publishes dist/.
3. **URLs.** The live site served flat files at extensionless URLs (/pool-repair, /mesa-pool-service).
   Those pages keep that exact URL: build.py writes `url: "/pool-repair"` to dist/pool-repair.html, which
   Netlify serves at /pool-repair and /pool-repair.html. Canonicals and the sitemap use the extensionless
   form the old sitemap used. The 16 new town pages follow the same /<town>-pool-service pattern so all 25
   towns match. New service, guide and core pages use folder URLs (/pool-heater-repair/), the style the
   live site used for /services/, /about/ etc. Privacy and terms keep /privacy-policy.html and /terms.html.
4. **Redirects (src/static/_redirects, copied to dist/).** Kept every Sep 24 and Sep 25 rule. Removed
   both `/pool-equipment-repair/` rules (it is a real page again). Re-pointed targets to the closer new
   page: /algae-treatment/ to /green-pool-cleanup/; /swimming-pool-service/ to /pool-service/; the
   retired posts on green pools and summer algae to /why-is-my-pool-green/, on desert heat and dust to
   /monsoon-pool-care/, on what weekly service includes to /pool-service/, on DIY equipment repairs to
   /pool-equipment-repair/. The old contact form had no thank-you URL, so no rule was needed.
5. **Phone only.** The old Netlify contact form is retired; /contact/ is a phone page. check.py fails any
   `<form>`.
6. **Phone number in one place.** (623) 240-0428 lives only in src/data/site.json (`phone_display`,
   `phone_tel`); the call button label is built from it (`Call {phone}`), and pages use
   `{{ site.business.phone_display }}`.

## Pages
7. **Service pages (11).** From the 11 service seeds in the keyword file: pool service (480/mo), pool
   cleaning and weekly maintenance (existing URL), pool repair (existing URL), pump repair (existing URL),
   equipment repair, heater repair, tile cleaning (existing URL), resurfacing (260/mo at SD 14), filter
   cleaning, green pool cleanup, plus pool leak and crack repair, added from the data ("how to patch a
   pool" 170/mo, "can you patch a pool with water in it" 110/mo). Salt cells, lights, automation and
   fountains have no rows of their own and are covered on the equipment page.
8. **Pool service and pool cleaning are separate pages.** Both have real Phoenix volume and different
   intent: /pool-service/ covers the service arrangement (what a plan covers, frequency, agreements);
   /pool-cleaning-maintenance covers the hands-on weekly routine and water chemistry.
9. **Guides (7).** Cost of pool service, how often to clean a filter, why a pool turns green, repair or
   resurface, monsoon and dust storm care, how often to drain a pool in Arizona (hard water and city
   drain rules), and how to choose a pool company (target "pool companies in phoenix" 390/mo, with the
   ROC lookup).
10. **Home page target.** "pool cleaning phoenix" (390/mo), which matches the business name; the cleaning
    page targets "pool cleaning service phoenix az" (390/mo at SD 22) so the two do not compete head on.
11. **Town pages (25).** Maurice's rule: any town with 10+ searches a month. All 9 existing town URLs
    kept and rebuilt; 16 added. Sun City West, El Mirage and Tolleson showed zero and get no page.
    North Phoenix, Ahwatukee and Laveen are parts of the City of Phoenix, so their structured data names
    Phoenix as the city.
12. **New core pages:** /service-areas/ (Prompt 10 hub) and /how-it-works/ (the secondary call to action
    target on most pages).
13. **FAQ page.** CLAUDE.md caps FAQs at 3 to 6 per page, so /faq/ has 6 in the FAQ block (visible and in
    FAQPage JSON-LD) and the rest as ordinary question headings in the body.
14. **ROC wording.** The site never says a partner company is licensed. It says, generally and carefully,
    that Arizona's ROC licenses contractors, that residential classifications include R-6 Swimming Pool
    Service and Repair, that routine cleaning and water care are generally not treated as contracting
    while repair, equipment replacement and resurfacing generally call for a licensed contractor, and it
    links the ROC contractor search. The handyman exemption's dollar figure is not stated because
    bills have proposed changing it and the current statute text could not be opened.

## Brand and media
15. **Palette.** Kept the live site's pool blue #1a4d7a for the header and first color band and the logo's
    navy #0e3654 / #0a2238 for headings, the call band and the footer; sun amber #eaa64f (from the logo's
    sun) for call buttons with navy text; desert terracotta #a34a26 for the second color band. Sections
    stay white between bands; breadcrumbs sit on white (no pale tinted strips). All bands carry white text;
    panels and cards on white carry a colored edge.
16. **Logo and favicons kept** (images/logo.svg, favicon.svg, favicon.ico). An apple-touch-icon.png was
    rendered from favicon.svg.
17. **Photos.** The 16 existing photos are reused first. Pages that need a photo that does not exist list
    it in docs/image-list.md with an Artistly prompt and show an existing photo until it arrives (never a
    broken image).

## Research limits
18. **Network.** The environment blocks direct page fetches (curl and WebFetch fail for phoenix.gov,
    roc.az.gov, weather.gov and nearly every source). Facts were verified through WebSearch result
    summaries of the named official pages, then re-checked by separate fact-check agents
    (docs/fact-check.md). WebSearch is also capped at 200 calls per turn shared by every agent, which
    shaped how the research was spread across turns.
