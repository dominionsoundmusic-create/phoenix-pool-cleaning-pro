# Phoenix Pool Cleaning Pro (phoenixpoolcleaningpro.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding a LIVE static lead-generation website for Maurice Johnson by running
Dominic & Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full.
The site is live and indexed, so the rebuild must keep every URL Google knows.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. The only reason to stop early is if something would require paying money, deploying,
or changing a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over anything else. UNKNOWN means leave it off the site.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/Phoenix-Pool-Keywords.xlsx: Ubersuggest, United States, pulled Oct 8 2026. 550 unique
  keywords, 11 service seeds plus 28 town seeds, a tab per seed plus an ALL tab, each row typed
  Suggestion or Question. Every Phoenix-area keyword must be assigned to a page as a target or
  supporting keyword, or listed in docs/keyword-plan.md as deliberately unused with a one-line
  reason. "Near me" terms are national volume: supporting keywords only. Public-pool searches
  ("pool gilbert az", "surprise pool hours", city aquatic centers) and off-topic rows go in the
  unused list.
- The current live site (this repo's main branch). Read every page before writing. Keep useful
  verified facts, but do NOT copy its paragraphs: every page is written fresh. Reuse its photos in
  images/ first.

## Copy the build system from Houston Air & Heating (NOT its words)
The repository dominionsoundmusic-create/houston-hvac-pro, branch `build`, holds the newest version
of the build system: a Playbook 2.0 referral-line site rebuilt and checked on Oct 8 2026, including
the full-width text fix (body text, photos, cards and color bands share one left and right edge).
Clone it and copy its BUILD SYSTEM: build.py, scripts/check.py, scripts/similarity.py if present,
src/templates/, src/static/css/site.css and JS, the macros, the site.json structure, netlify.toml
(publish = "dist") and the docs/playbook/ document set as a pattern. Adapt every Houston and HVAC
value to Phoenix and pool service.
NEVER copy page text, paragraphs, FAQs or sentence runs from Houston. No Texas places, no
CenterPoint, no Gulf Coast facts. Research Phoenix equivalents instead (Arizona Public Service and
Salt River Project for power, City of Phoenix and each city's water hardness and pool draining or
backwash rules, Maricopa County, monsoon dust storms and the extreme heat, calcium scale, high
evaporation, UV and stabilizer).
Keep the speed fix exactly (WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority
high, self-hosted woff2 font) and keep the full-width text layout.

## URLs: keep every live URL (this is a rebuild of an indexed site)
Every URL in main's sitemap.xml and every page file on main must still resolve on the new site,
either as a rebuilt page at the SAME path or a 301 to the closest new page (record each in
docs/decisions.md). That includes the 9 town pages (*-pool-service.html), pool-cleaning-maintenance,
pool-repair, pump-repair, tile-cleaning, about/, contact/, faq/, services/, privacy-policy.html and
terms.html. Keep the existing _redirects rules that still make sense and copy _redirects into dist/.
If you build a real page at a path an old rule redirects (for example /pool-equipment-repair/),
remove that rule. Write a script that checks every old URL and record the result in docs/qa.md.

## Pages to build (decide the exact list from the keywords, then follow it)
- Home, services overview, service areas overview, how it works, about, FAQ, contact, privacy,
  terms, 404.
- Service pages: one per real service with Phoenix demand: pool service, pool cleaning and weekly
  maintenance, pool repair, pool pump repair, pool equipment repair, pool heater repair, pool tile
  cleaning, pool resurfacing (260/mo at SEO difficulty 14, an easy win), pool filter cleaning, green
  pool cleanup, plus anything else the data shows.
- Guide pages for the strongest question keywords (cost of pool service, how often to clean a
  filter, why a pool turns green, repair or resurface, monsoon and dust storm care), each researched
  and sourced.
- Town pages: Maurice's rule for this site is ANY town with 10 or more searches a month gets its
  own page. From the data that is 25 towns: Scottsdale, Surprise, Mesa, Gilbert, Peoria, Queen Creek,
  Chandler, Tempe, Litchfield Park, Goodyear, Cave Creek, Glendale, Buckeye, North Phoenix, Avondale,
  Anthem, Fountain Hills, Maricopa, San Tan Valley, Laveen, Ahwatukee, Paradise Valley, Sun City,
  Carefree, Apache Junction. Keep the 9 existing town URLs and add the rest. Sun City West, El
  Mirage and Tolleson showed zero and get no page.
- Write SERVICES.md (every page, URL, target keyword with volume/SEO difficulty) and
  docs/keyword-plan.md before writing pages.

## Hard rules for every page
1. Never "our technicians", "our trucks", "we clean", "we repair", "we are licensed/insured" or
   anything implying the line does pool work.
2. Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business,
   team members, job counts, guarantees, awards or statistics. Research and state accurately what
   Arizona requires (the Registrar of Contractors licenses pool contractors for some work; check
   which work needs a license and say so correctly), and tell readers how to look a company up on
   the Arizona ROC search.
3. Never name a specific pool company.
4. Only Phoenix-metro places. No other Arizona metros (no Tucson, no Yuma) and no other states.
5. No em dashes or en dashes in visible copy. No eyebrow labels. American spelling.
6. No DIY chemical-mixing instructions beyond safe basics, no electrical or gas work. Safety first:
   never mix pool chemicals, keep children away from an unfenced pool, a pool heater gas smell means
   leave the area and call the gas utility or 911.
7. No prices presented as the line's prices. Cost guides cite published, sourced ranges and say
   real quotes vary.
8. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD.
9. Every page has a full-width hero image plus at least two in-body images, each with filename,
   alt, width, height and loading="lazy" (hero eager). Reuse this repo's images first.
10. Facts must be real and current. Research each page on the web and cite every source in the
    page's sources list. If you cannot verify a fact, leave it out.
11. Each page is written for its own keyword. Never reuse paragraphs between pages with names
    swapped. Measure: Jaccard similarity on 5-word shingles between every pair of pages; any pair
    of town pages or service pages above 15% gets rewritten. Record the numbers in docs/qa.md.
    Town pages must be researched for THAT town: its water provider and hardness, HOA patterns,
    typical lot and pool age, its neighborhoods, its monsoon and dust exposure.
12. The referral disclosure appears on every page (wording in INTAKE.md).
13. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
    excellence", "we've got you covered", plus the WORDS TO AVOID in INTAKE.md.
14. Mark every page with the HTML comment `dwdp:handwritten 2026-10-08` in the first 4KB.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color, never dull gray. EN/ES language toggle in the header on
  every page (Google Translate widget, top right, lazy-loaded, as the Houston build does).
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right scrim behind
  the headline, logo/headline/buttons aligned to the left rail at 1440, 1920 and 2560 wide. Hero
  stays above the fold (max-height about 700px) with the call button visible.
- Body text, photos and cards share the same left and right edge as the header and color bands
  (the Houston build's full-width layout). Do not box text into a narrow center strip.
- Mostly WHITE sections broken by occasional bold color bands (hero, white, brand-blue band, white,
  a second band in a warm desert color). Never pale off-white tints. Never every section tinted.
- No white text or white boxes on white. Every card, box and button has clear contrast.
- Logo: keep the site's existing logo.svg unless it is broken; favicon too.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- Every old URL resolves on the built site or has a 301 in dist/_redirects (script, result in
  docs/qa.md).
- Grep the built site for: em/en dashes in visible text, "we clean", "we repair", "our technicians",
  "licensed and insured", "free estimate", "same-day", "Houston", "Texas", "Tucson", "Yuma",
  "CenterPoint", "(832)", "(903)". Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px wide.
- Independent fact-check: start separate sub-agents that did not write the pages, have them check
  every factual claim and source on every page, and fix what they find. Record it in
  docs/fact-check.md. Never say "fact-checked" unless this was actually run.
- docs/image-list.md lists every image still needed: File name, Size, then an Artistly prompt
  (bright, clearly visible, Phoenix-area homes and backyard pools, desert landscaping, no text, no
  logos, no recognizable faces, "wide cinematic landscape shot, subject positioned on right third of
  frame, well lit"). Missing images must never show as broken: pages use an existing photo until
  the new one arrives.

## Git
- Work on the branch `build`. Commit as you go with clear messages.
- Push to origin `build` ONCE, at the very end.
- Do NOT merge to main, do NOT deploy, do NOT touch Netlify settings, do NOT pay for anything.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, duplication range, fact-check result, and how many
images still need Artistly.
