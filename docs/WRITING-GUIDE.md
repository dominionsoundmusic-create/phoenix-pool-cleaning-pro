# Writing guide for phoenixpoolcleaningpro.com pages (Playbook 2.0 rebuild, Oct 8 2026)

Repo: /home/user/phoenix-pool-cleaning-pro (branch `build`). Read these first, in full:
1. `CLAUDE.md` (the hard rules) and `INTAKE.md` (the facts; it wins over everything; read "WHAT THE
   BUSINESS ACTUALLY IS" twice).
2. `SERVICES.md` and `docs/keyword-plan.md` (your page's URL, TARGET keyword and supporting keywords,
   including the Question rows to turn into FAQs).
3. `src/data/site.json` (names and URLs of services, guides and areas).
4. `src/templates/macros.html` (service_cards, guide_cards, area_pills, related, call_box,
   how_it_works_short, disclosure, license_check, sources).
5. STRUCTURE MODELS ONLY: pages of the sister site Houston Air & Heating, built with the same system:
   `/home/user/dominionsoundmusic-create/houston-hvac-pro/src/pages/furnace-repair.html` (service),
   `.../ac-repair-cost.html` (guide), `.../ac-repair/katy-tx.html` (area). Match their depth, section rhythm
   and component use. NEVER copy their wording, sentences, FAQs or facts (it is an HVAC site in Texas).
   `scripts/similarity.py` compares every Phoenix page with every Houston page and FAILS on any shared run
   of 8 words. Write from scratch.
6. The old Phoenix page for your URL in `docs/old-site/` (if any) for research leads only. Its numbers
   (for example "300 to 900 ppm calcium", "chemicals included") are UNVERIFIED and partly in contractor
   voice. Keep a fact only after you verify it with a real source; never copy or lightly reword its text.

## The business, in one paragraph
Phoenix Pool Cleaning Pro is a free phone line and website, NOT a pool company. An automated assistant
answers (623) 240-0428 any hour, asks briefly what is going on with the pool, then transfers the call to
an independent, locally owned Phoenix-area pool service company. That company hears a short summary before
it picks up. If it cannot answer, the caller's name, callback number, area and pool problem are passed
along for a call back. The company looks at the pool, quotes, does the work and is paid directly by the
customer. The line never cleans, repairs, quotes or schedules anything, holds no license, never charges the
caller, and may be paid a referral fee by the companies. Write "the pool company you are put through to",
"the pool service company", "a careful pool technician". Never "our technicians", "our trucks", "we clean",
"we repair", "we are licensed/insured", "we'll send someone". Never say the connected companies are
licensed, insured, certified, rated or reviewed. Tell readers to ASK for the company's Arizona ROC license
number (for repair, equipment, resurfacing and leak work) and look it up on the ROC contractor search
(https://roc.az.gov/contractor-search). Never name any pool company. Avoid equipment brand names.
Never write the phone number by hand: use `{{ site.business.phone_display }}` (tel link:
`tel:{{ site.business.phone_tel }}`).

## Hard rules (scripts/check.py enforces most of them)
- No em dashes or en dashes anywhere (copy, titles, descriptions, FAQs, alt text). Use commas, colons,
  periods or "to" ("105 to 110 degrees"). American spelling. No eyebrow labels or badges.
- Only Phoenix-metro places (Maricopa County, plus San Tan Valley, Apache Junction and the city of Maricopa
  in Pinal County). Never Tucson, Yuma, Flagstaff, Prescott, Sedona, Lake Havasu, Casa Grande or any other
  Arizona area, never another state (no California, Nevada, Utah, New Mexico, Texas), not even as a
  comparison and not even when explaining the Colorado River. Say "the Colorado River" and "the Central
  Arizona Project (CAP)" without listing other states.
- Never invent licenses, insurance, reviews, ratings, prices, years in business, team members, job
  counts, statistics, response times, guarantees or awards. Public statistics are fine with the source
  named and listed. Prices: explain what drives price; a published range only with its source named on
  the page and a note that real quotes vary. Never present a price as the line's price.
- Banned (checker fails): "free estimate(s)", "same-day", "guarantee(d)", "best price", "cheapest",
  "top-rated", "years of experience", "#1", "number one", "licensed and insured", "chemicals included",
  "flat monthly price", "your trusted partner", "one-stop solution", "look no further", "unmatched
  excellence", "we've got you covered", response-time promises ("within 2 hours"), and any of "HVAC",
  "Houston", "Texas", "CenterPoint", "Gulf Coast".
- Safety first, no DIY beyond safe basics:
  - Never give chemical-mixing or dosing instructions (no "add X pounds of shock", no acid washing steps,
    no muriatic acid dilution). Say plainly: never mix pool chemicals with each other, store them apart,
    dry and shaded, out of children's reach, follow the label, and leave acid work to a professional.
  - No electrical work (motors, wiring, breakers beyond noting a tripped breaker; a breaker that trips again
    means stop and call), no gas work. Pool heater gas smell: leave the area, do not operate switches or
    the heater, and from a safe distance call Southwest Gas (verify its emergency number on swgas.com for
    your page) or 911.
  - Children: keep them away from an unfenced or uncovered pool, never leave a child unsupervised near
    water, and a green or murky pool is a drowning hazard because the bottom cannot be seen.
  - Safe homeowner checks only: skimmer and pump baskets, the filter pressure gauge reading, the timer or
    automation schedule, water level at the skimmer, visible leaks or drips at the equipment pad, a tripped
    GFCI or breaker (reset once), debris around the equipment, testing water with a home test kit.
- Every fact that is not common knowledge carries a source in the page's Sources list with a real URL.
  If you cannot verify it, leave it out.

## Shared facts already checked (Oct 8 2026, from search results; re-verify anything you lean on)
- ROC: Arizona's Registrar of Contractors licenses contractors. Residential classifications include R-6
  Swimming Pool Service and Repair; B-5 covers residential swimming pool construction (building and
  repairing pools). Contractor search: https://roc.az.gov/contractor-search (search by name, license number;
  shows status, classification, bond and complaint history). ROC phone 1-877-692-9762 (verify before using).
  A.R.S. 32-1121 has a "handyman" exemption for small jobs under a dollar limit that does not apply to work
  needing a building permit; do NOT state the dollar figure unless you verify the current statute text,
  since bills have proposed changing it. Routine cleaning and water care are generally not treated as
  contracting. Say this carefully ("generally"), never claim the line checks licenses.
- Electricity: APS (Arizona Public Service) and SRP (Salt River Project) serve most of the metro; which
  one depends on the address (and a few areas have other providers). Verify for your town.
- Natural gas: Southwest Gas serves most of the metro. Verify for your town.

## Voice
Plain, specific, warm, Phoenix-local. Second person. Short paragraphs, roughly 7th to 8th grade reading
level; explain a technical word the first time (cyanuric acid, total dissolved solids, calcium hardness,
LSI). Explain why. No filler, no superlatives, no keyword stuffing. The target keyword appears naturally in
the title, H1, first paragraph, one H2 and the meta description. Say "the Valley" as well as "Phoenix".

## Page file format
`src/pages/<file>.html` with YAML front matter, then `{% block content %}...{% endblock %}`.
File names: service and guide pages with a trailing-slash URL use `src/pages/<slug>.html` (URL /<slug>/,
no `url:` needed). Flat URLs need `url:` and the file name `src/pages/<name>.html`, for example
`src/pages/pool-repair.html` with `url: "/pool-repair"`, `src/pages/mesa-pool-service.html` with
`url: "/mesa-pool-service"`. Every town page uses `url: "/<slug>-pool-service"` (see site.json areas).

```yaml
---
type: service            # service | guide | area
url: "/mesa-pool-service"   # ONLY for flat URLs (old pages and all town pages)
title: "..."             # 50 to 65 chars, unique, keyword near the front
description: "..."       # 120 to 160 chars, unique, no dashes
h1: "..."                # one H1, unique
crumb: "Mesa"
keyword: "pool service mesa az"
city_name: "Mesa"        # area pages only (for North Phoenix, Ahwatukee and Laveen use "Phoenix")
published: "2026-10-08"  # guides only
hero:
  image: mesa-pool-hero.jpg      # PLANNED 1920x1080 photo (see Images)
  alt: "..."
  desc: "Artistly prompt for the planned photo."
  fallback: pool/hero-2.jpg      # existing photo shown until the planned one exists
  fallback_alt: "..."            # accurate alt for the fallback photo
  lead: "One or two sentences under the H1."
  secondary_label: "..."         # optional, a real page or an in-page anchor, never a form
  secondary_href: "/..."
schema_service:          # service and area pages
  name: "Free connection to a local pool service company in Mesa, Arizona"
  type: "Pool service referral"
cta_title: "..."         # short, specific to the page
faqs:                    # 3 to 6 (never more), phrased the way people ask (use the Question rows)
  - q: "..."
    a: "<p>...</p>"
---
```
Quote YAML strings that contain a colon. Inside FAQ answers use `&amp;` or the word "and" for "&".

## Building blocks (existing classes only; do not edit CSS, templates, build.py, check.py or site.json)
- Reading column: `<section class="prose">...</section>`. Plain paragraphs, h2, h3, lists. Text runs the
  full width between the page rails (Maurice's full-width layout); do not add wrappers that narrow it.
- Color band: `<section class="band band--tint"><div class="wide">...</div></section>`. The build turns
  these into bold pool-blue / desert-terracotta bands with white text. Use ONE (at most two) per page, with
  white prose sections between; never two bands in a row; the FAQ band and the final call band are added
  automatically after your content, so do not end your content with a band.
- Two columns, text and photo: inside `.prose`, `<div class="split"><div>text</div>{{ img(...) }}</div>`.
- `<ol class="steps">` numbered process; `<ul class="checks">` checklist; `<div class="grid-2">` /
  `<div class="grid-3">` of `<div class="panel">` (add `panel--do` / `panel--dont`); `<ul class="facts">`
  of `<li><strong>label</strong>text</li>`; tables in `<div class="table-wrap"><table>` with
  `<caption class="sr">`, `<thead>`, `scope` on th; `<div class="note">` callout,
  `<div class="note note--orange">` warning.
- Macros: `{{ m.how_it_works_short() }}`, `{{ m.disclosure() }}`, `{{ m.license_check() }}`,
  `{{ m.call_box('text') }}`, `{{ m.service_cards(['slug', ...]) }}`, `{{ m.guide_cards(['slug']) }}`,
  `{{ m.area_pills(exclude='mesa') }}`, `{{ m.related(['slug','guide:slug','area:slug'], 'Title') }}`,
  `{{ m.sources([{'label': '...', 'url': '...'}, ...]) }}` (always last, inside the last prose section).
  Slugs are the `slug` values in site.json (services: pool-service, pool-cleaning-maintenance, pool-repair,
  pump-repair, pool-equipment-repair, pool-heater-repair, tile-cleaning, pool-resurfacing,
  pool-filter-cleaning, green-pool-cleanup, pool-leak-repair; guides: pool-service-cost,
  how-often-to-clean-pool-filter, why-is-my-pool-green, repair-or-resurface-pool, monsoon-pool-care,
  how-often-to-drain-pool-arizona, choosing-a-pool-company; areas: north-phoenix, scottsdale,
  paradise-valley, fountain-hills, cave-creek, carefree, anthem, tempe, mesa, chandler, gilbert, ahwatukee,
  queen-creek, san-tan-valley, apache-junction, maricopa, glendale, peoria, surprise, sun-city,
  litchfield-park, goodyear, avondale, buckeye, laveen).
- Links: use the `url` values in site.json exactly (flat ones have no slash or .html: `/pool-repair`,
  `/pump-repair`, `/tile-cleaning`, `/pool-cleaning-maintenance`, `/mesa-pool-service`; new ones end in a
  slash: `/pool-heater-repair/`). Core: `/how-it-works/`, `/service-areas/`, `/services/`, `/about/`,
  `/faq/`, `/contact/`. Link to 3+ related pages naturally in the copy.

## Images
Call: `{{ img('file.jpg', 'alt', 1200, 800, desc='prompt', fallback='pool/x.jpg', fallback_alt='...') }}`.
An existing photo used directly needs no desc/fallback: `{{ img('pool/chem-wide.jpg', 'alt', 1200, 500) }}`.
Every content page: a hero plus at least two in-body images; no photo repeated within one page (count the
hero's fallback too). Alt text with a worker must not imply they work for the line.

Existing photos in src/static/images (all are bright Phoenix-style desert backyards or pool close-ups):
- Heroes 1920x800: `pool/hero-1.jpg` (curved pool, stucco house with covered patio, lounge chairs, desert
  plants, a saguaro, rocky mountains), `pool/hero-2.jpg` (free-form turquoise pool, flagstone deck and boulder
  edge, adobe-style covered patio with dining table, palms, cacti, mountains), `pool/hero-3.jpg` (long
  rectangular pool with a row of white lounge chairs, palms, desert trees and boulders, distant mountains).
  1344x768: `img-01.jpg` (curving pool at golden hour, tall palms, a saguaro, warm-toned deck).
- 1200x500 (wide crops): `pool/hero-1-wide.jpg`, `pool/hero-2-wide.jpg`, `pool/hero-3-wide.jpg` (same scenes
  as the heroes), `pool/brush-wide.jpg` (hand pushing a blue pool brush under clear water),
  `pool/chem-wide.jpg` (two white chemical jugs and a test cup on a pool deck at sunset, lounge chairs
  behind), `pool/dusk-wide.jpg` (lit pool at dusk, string lights, stone patio, covered patio, cacti),
  `pool/equip-wide.jpg` (pool pump with plumbing beside a tall filter tank against a sunlit stucco wall),
  `pool/green-wide.jpg` (neglected pool with green water and leaves, block wall, desert trees),
  `pool/repair-wide.jpg` (two hands turning a wrench on an old cast pump, workshop),
  `pool/skim-wide.jpg` (a man standing in a pool skimming with a leaf net, saguaro and block wall behind,
  face not shown), `pool/test-wide.jpg` (hand holding a water sample vial at the pool surface),
  `pool/vac-wide.jpg` (robotic pool cleaner on a sunlit pool floor).

Planned new photos (Maurice generates them in Artistly later). Each needs a unique descriptive filename, a
`desc=` prompt and a `fallback=` existing photo. Prompt style: start with "Wide cinematic landscape shot,
subject positioned on right third of frame, well lit," then a specific, bright, realistic Phoenix-area
scene (that town's real housing and landscape: stucco and tile-roof homes, block walls, desert
landscaping with gravel, palo verde and mesquite trees, saguaros where they really grow, citrus trees in
older areas, the mountains or buttes actually visible from that town), then "realistic photo, no text, no
logos, no house numbers, no recognizable faces". Never use the word "penetration" (Artistly blocks it).
- Town pages: hero = PLANNED `<slug>-pool-hero.jpg` (1920x1080) with the fallback given in your brief,
  plus ONE planned in-body local photo `<slug>-<scene>.jpg` 1200x800 (with an existing fallback) and at
  least one existing photo used directly.
- Service and guide pages: hero = PLANNED `<slug>-hero.jpg` 1920x1080 with the topical existing fallback
  given in your brief. In-body: existing photos; at most ONE planned in-body photo (with fallback).

## Content each page needs
Service and guide pages (Prompt 9): what it is; who it is for; common problems; what a careful pool
technician does and why; what to expect; options; Phoenix-specific context (verified only: extreme heat
and UV, high evaporation, hard water and calcium scale from the Colorado River / CAP, Salt and Verde river
and groundwater supplies, total dissolved solids, monsoon season (June 15 to September 30 is the National
Weather Service's official monsoon period) and haboobs, chlorine loss in sun and the role of cyanuric acid
(stabilizer), city rules on draining and backwashing, Maricopa County Environmental Services and mosquito
control for neglected pools, ROC licensing for repair work, APS/SRP and Southwest Gas); safe homeowner
checks where relevant; what to ask; related pages; 3 to 6 FAQs; at least one distinctive design treatment
(symptom table, decision panels, timeline, checklist, comparison table). About 1,500 to 2,200 words of
page-specific copy. Sources list at the end.

Area pages (Prompt 11): hero; FIRST H2 names the town ("Mesa: ..."), with two local paragraphs and a
photo beside them (split); services genuinely relevant there (`m.service_cards([...])`); a section
titled "Why [Town] homeowners call the line" with FOUR distinct local reasons as
`<div class="grid-2">` of four `<div class="panel"><h3>..</h3><p>..</p></div>`, built only from facts on
that page plus what the line truly does (free, 24/7, transfers to an independent local company, caller
pays the company not the line, the site explains the ROC license check); verified local context, researched
for THAT town: its water provider(s) and source water (CAP / Colorado River, SRP surface water from the
Salt and Verde, groundwater wells) and the hardness or TDS its own water quality report gives (quote the
figure and year only from the report you found); its electric provider (APS or SRP or other) and gas
provider; county; HOA patterns and housing age (master-planned communities, typical decade the homes were
built, from Census or city data); typical lots and pools where a source says so; named neighborhoods; its
monsoon and dust exposure (open desert, farmland, construction dust where sourced); that city's rules on
draining pools or backwashing (where pool water may and may not go) and pool barrier rules if the city
publishes them; any city water conservation rebate that touches pools. Area FAQs; `m.how_it_works_short()`;
nearby areas (`m.area_pills(exclude='<slug>')`); sources. Never claim an office, address, job history,
customer count or travel time. Each town page must be built around what is actually different there.
Two town pages must not share paragraphs: the checker fails any pair above 15% overlap (5-word shingles).

## Research standard
- Research each page on the web BEFORE writing. Direct page fetches are blocked by the environment's
  network policy for most hosts (curl and often WebFetch fail); use WebSearch (restrict with
  allowed_domains to official domains such as phoenix.gov, mesaaz.gov, azroc.gov, maricopa.gov,
  azwater.gov, weather.gov, census.gov, srpnet.com, aps.com, swgas.com, energy.gov, cdc.gov, epa.gov,
  azdhs.gov, extension.arizona.edu) and try WebFetch on the official URL; cite the official URL whose
  content the search result showed. Prefer primary sources. Today's date is Oct 8 2026: check facts are
  current.
- Every number, date, rule, phone number, fee and named program comes from a source you saw; that source
  goes in the Sources list with its real URL. If you cannot verify it, leave it out.
- Facts shared by many pages (CAP water, monsoon dates, ROC): say them in your own words, only where they
  matter to that page, never the same paragraph twice.

## Validation (from the repo root; NEVER a plain `python3 build.py`, it writes dist/ and docs/)
```
python3 build.py --out /tmp/<your-name>/dist
python3 scripts/check.py --dist /tmp/<your-name>/dist --skip-links --only <your page URL>
python3 scripts/similarity.py --dist /tmp/<your-name>/dist --other /home/user/dominionsoundmusic-create/houston-hvac-pro/dist --only <your page URL as similarity prints it>
```
(similarity prints flat pages as `/mesa-pool-service.html`, folder pages as `/pool-heater-repair/`.)
build.py may print FAILED for other writers' half-finished pages; ignore those, fix your own. Fix every
ERROR and FAIL for your pages. A WARN about word count under 1500 (which includes the template) means
the page is thin: add substance, not filler. Do not edit shared files or anyone else's pages. Do not
commit or push.

When done, report: files written, word counts, for area pages a one-sentence factual summary of the town
(max 22 words, no dashes, for the service-areas page), and any fact you could not verify and therefore left
out.
