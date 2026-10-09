# QA record (Oct 9 2026, final run on the `build` branch)

All commands run from the repo root against the production build in dist/.

| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 53 pages built; 77 planned photos listed in docs/image-list.md (each page shows an existing photo meanwhile, never a broken image) |
| Rules and SEO | `python3 scripts/check.py` | 53 pages checked, **0 errors, 0 warnings** (banned phrases and INTAKE words to avoid, dashes, places outside the Phoenix metro, DIY chemical/gas/electrical wording, forms, eyebrow labels, exact quote bar, footer credit, referral disclosure, handwritten marker in the first 4KB, one H1, unique titles and descriptions, canonical, OG tags, one valid JSON-LD block, 3 to 6 FAQs visible and in FAQPage JSON-LD, hero plus 2 in-body images with lazy loading, alt/width/height, internal links, sitemap, _redirects targets) |
| Old URLs | `python3 scripts/check_old_urls.py` | **83 old URLs checked, 0 would 404** (table below) |
| CLAUDE.md grep | `python3 scripts/grep_check.py` | **0 hits** for em/en dashes, "we clean", "we repair", "our technicians", "licensed and insured", "free estimate", "same-day", "same day", "Houston", "Texas", "Tucson", "Yuma", "CenterPoint", "(832)", "(903)", "903-636" in visible text, titles, meta and alt text |
| Duplication | `python3 scripts/similarity.py --other ../houston-hvac-pro/dist` | Town pairs max **4.0%**, service pairs max **1.9%** (limit 15%); no Phoenix page shares an 8-word run with any Houston page (table below) |
| Browser | `node scripts/responsive_check.js` (dist served on :8765, Chromium) | 218 page loads: every page at 1440, 1024, 768 and 390 px plus samples at 1920 and 2560: **0 problems** (no horizontal overflow, no JS errors, no broken images, hero edge to edge, hero at most 700px tall with the call button above the fold, headline on the left rail) |
| Fact-check | 9 independent sub-agents plus coordinator follow-up | 726 claims checked; 65 corrected, 81 softened, 83 removed (docs/fact-check.md) |

Not verified here (needs the live site): Netlify's 404 status and redirect behavior in production, the
Google Translate ES toggle on the real domain, and the phone line's routing.

## Duplication (Jaccard on 5-word shingles, page copy and FAQ answers; shared template parts excluded)

| Group | Pairs | Max | Mean | Min |
|---|---:|---:|---:|---:|
| area | 300 | 4.0% | 1.0% | 0.0% |
| guide | 21 | 2.5% | 0.5% | 0.1% |
| legal | 1 | 1.2% | 1.2% | 1.2% |
| mixed | 943 | 3.5% | 0.4% | 0.0% |
| page | 6 | 1.4% | 0.5% | 0.0% |
| service | 55 | 1.9% | 0.6% | 0.1% |

Top 15 pairs:

| Jaccard | Page | Page |
|---:|---|---|
| 4.0% | /apache-junction-pool-service.html | /tempe-pool-service.html |
| 3.5% | /faq/ | / |
| 3.2% | /glendale-pool-service.html | /surprise-pool-service.html |
| 3.1% | /fountain-hills-pool-service.html | /scottsdale-pool-service.html |
| 2.9% | /goodyear-pool-service.html | /litchfield-park-pool-service.html |
| 2.8% | /litchfield-park-pool-service.html | /surprise-pool-service.html |
| 2.7% | /ahwatukee-pool-service.html | /north-phoenix-pool-service.html |
| 2.7% | /avondale-pool-service.html | /surprise-pool-service.html |
| 2.5% | / | /pool-repair.html |
| 2.5% | /how-often-to-clean-pool-filter/ | /monsoon-pool-care/ |
| 2.5% | /fountain-hills-pool-service.html | /paradise-valley-pool-service.html |
| 2.5% | /how-often-to-clean-pool-filter/ | /pool-filter-cleaning/ |
| 2.4% | /paradise-valley-pool-service.html | /scottsdale-pool-service.html |
| 2.3% | /faq/ | /surprise-pool-service.html |
| 2.3% | /avondale-pool-service.html | /faq/ |

## Old URLs

| Old URL | Result | How |
|---|---|---|
| / | 200 | served by a rebuilt page or file at the same path |
| /about/ | 200 | served by a rebuilt page or file at the same path |
| /algae-treatment/ | 301 | redirect to /green-pool-cleanup/ (rule /algae-treatment/) |
| /apache-junction-pool-service | 200 | served by a rebuilt page or file at the same path |
| /apache-junction-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /blog | 301 | redirect to / (rule /blog) |
| /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785937746524 | 301 | redirect to /monsoon-pool-care/ (rule /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785937746524) |
| /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785937746524.html | 301 | redirect to /monsoon-pool-care/ (rule /blog/how-desert-heat-and-dust-affect-pool-chemistry-1785937746524.html) |
| /blog/how-desert-heat-and-dust-affect-pool-chemistry-1786192357663 | 301 | redirect to /monsoon-pool-care/ (rule /blog/how-desert-heat-and-dust-affect-pool-chemistry-1786192357663) |
| /blog/how-desert-heat-and-dust-affect-pool-chemistry-1786192357663.html | 301 | redirect to /monsoon-pool-care/ (rule /blog/how-desert-heat-and-dust-affect-pool-chemistry-1786192357663.html) |
| /blog/how-often-should-a-pool-be-cleaned-in-phoenix-1786278887291 | 301 | redirect to /pool-cleaning-maintenance (rule /blog/how-often-should-a-pool-be-cleaned-in-phoenix-1786278887291) |
| /blog/how-often-should-a-pool-be-cleaned-in-phoenix-1786278887291.html | 301 | redirect to /pool-cleaning-maintenance (rule /blog/how-often-should-a-pool-be-cleaned-in-phoenix-1786278887291.html) |
| /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024073700 | 301 | redirect to /why-is-my-pool-green/ (rule /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024073700) |
| /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024073700.html | 301 | redirect to /why-is-my-pool-green/ (rule /blog/how-to-keep-algae-out-of-a-pool-in-summer-1786024073700.html) |
| /blog/pool-chemical-balancing-explained-simply-1786970619332 | 301 | redirect to /pool-cleaning-maintenance (rule /blog/pool-chemical-balancing-explained-simply-1786970619332) |
| /blog/pool-chemical-balancing-explained-simply-1786970619332.html | 301 | redirect to /pool-cleaning-maintenance (rule /blog/pool-chemical-balancing-explained-simply-1786970619332.html) |
| /blog/pool-equipment-repairs-you-should-never-diy-1785851617952 | 301 | redirect to /pool-equipment-repair/ (rule /blog/pool-equipment-repairs-you-should-never-diy-1785851617952) |
| /blog/pool-equipment-repairs-you-should-never-diy-1785851617952.html | 301 | redirect to /pool-equipment-repair/ (rule /blog/pool-equipment-repairs-you-should-never-diy-1785851617952.html) |
| /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786366238746 | 301 | redirect to /pool-cleaning-maintenance (rule /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786366238746) |
| /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786366238746.html | 301 | redirect to /pool-cleaning-maintenance (rule /blog/saltwater-vs-chlorine-pools-which-is-easier-to-maintain-1786366238746.html) |
| /blog/signs-your-pool-pump-is-about-to-fail-1785707665609 | 301 | redirect to /pump-repair (rule /blog/signs-your-pool-pump-is-about-to-fail-1785707665609) |
| /blog/signs-your-pool-pump-is-about-to-fail-1785707665609.html | 301 | redirect to /pump-repair (rule /blog/signs-your-pool-pump-is-about-to-fail-1785707665609.html) |
| /blog/what-weekly-pool-service-actually-includes-1786106809258 | 301 | redirect to /pool-service/ (rule /blog/what-weekly-pool-service-actually-includes-1786106809258) |
| /blog/what-weekly-pool-service-actually-includes-1786106809258.html | 301 | redirect to /pool-service/ (rule /blog/what-weekly-pool-service-actually-includes-1786106809258.html) |
| /blog/why-your-pool-turns-green-and-how-to-fix-it-1786452568911 | 301 | redirect to /why-is-my-pool-green/ (rule /blog/why-your-pool-turns-green-and-how-to-fix-it-1786452568911) |
| /blog/why-your-pool-turns-green-and-how-to-fix-it-1786452568911.html | 301 | redirect to /why-is-my-pool-green/ (rule /blog/why-your-pool-turns-green-and-how-to-fix-it-1786452568911.html) |
| /chandler-pool-service | 200 | served by a rebuilt page or file at the same path |
| /chandler-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /contact/ | 200 | served by a rebuilt page or file at the same path |
| /faq/ | 200 | served by a rebuilt page or file at the same path |
| /favicon.ico | 200 | served by a rebuilt page or file at the same path |
| /favicon.svg | 200 | served by a rebuilt page or file at the same path |
| /gilbert-pool-service | 200 | served by a rebuilt page or file at the same path |
| /gilbert-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /glendale-pool-service | 200 | served by a rebuilt page or file at the same path |
| /glendale-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /images/img-01.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/logo.svg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/brush-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/chem-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/dusk-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/equip-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/green-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-1-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-1.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-2-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-2.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-3-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/hero-3.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/repair-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/skim-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/test-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/pool/vac-wide.jpg | 200 | served by a rebuilt page or file at the same path |
| /mesa-pool-service | 200 | served by a rebuilt page or file at the same path |
| /mesa-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /north-phoenix-pool-service | 200 | served by a rebuilt page or file at the same path |
| /north-phoenix-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /peoria-pool-service | 200 | served by a rebuilt page or file at the same path |
| /peoria-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /pool-chemical-balancing/ | 301 | redirect to /pool-cleaning-maintenance (rule /pool-chemical-balancing/) |
| /pool-cleaning-maintenance | 200 | served by a rebuilt page or file at the same path |
| /pool-cleaning-maintenance.html | 200 | served by a rebuilt page or file at the same path |
| /pool-cleaning-near-me/ | 301 | redirect to /services/ (rule /pool-cleaning-near-me/) |
| /pool-cleaning-service/ | 301 | redirect to /pool-cleaning-maintenance (rule /pool-cleaning-service/) |
| /pool-equipment-repair/ | 200 | served by a rebuilt page or file at the same path |
| /pool-maintenance/ | 301 | redirect to /pool-cleaning-maintenance (rule /pool-maintenance/) |
| /pool-repair | 200 | served by a rebuilt page or file at the same path |
| /pool-repair.html | 200 | served by a rebuilt page or file at the same path |
| /privacy-policy.html | 200 | served by a rebuilt page or file at the same path |
| /pump-repair | 200 | served by a rebuilt page or file at the same path |
| /pump-repair.html | 200 | served by a rebuilt page or file at the same path |
| /robots.txt | 200 | served by a rebuilt page or file at the same path |
| /scottsdale-pool-service | 200 | served by a rebuilt page or file at the same path |
| /scottsdale-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /services/ | 200 | served by a rebuilt page or file at the same path |
| /sitemap.xml | 200 | served by a rebuilt page or file at the same path |
| /surprise-pool-service | 200 | served by a rebuilt page or file at the same path |
| /surprise-pool-service.html | 200 | served by a rebuilt page or file at the same path |
| /swimming-pool-service/ | 301 | redirect to /pool-service/ (rule /swimming-pool-service/) |
| /terms.html | 200 | served by a rebuilt page or file at the same path |
| /tile-cleaning | 200 | served by a rebuilt page or file at the same path |
| /tile-cleaning.html | 200 | served by a rebuilt page or file at the same path |
| /weekly-pool-cleaning/ | 301 | redirect to /pool-cleaning-maintenance (rule /weekly-pool-cleaning/) |

83 old URLs checked, 0 would 404.
