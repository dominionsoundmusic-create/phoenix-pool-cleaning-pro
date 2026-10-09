# Independent fact-check (Oct 8 to 9 2026)

**What was run.** After all 53 pages were written, nine separate fact-check sub-agents (fc1 to fc9)
checked the factual claims and cited sources on every page. None of them wrote any page it checked.
Each checker followed docs/fact-check/BRIEF.md: list every non-obvious claim (numbers, dates, rules,
phone numbers, fees, providers, programs, statutes, history, prices), verify it, then correct, soften
or remove it in place, re-run build.py, check.py and similarity.py on its pages, and log every claim.
The coordinator then checked the items the checkers flagged as unsearched and settled two judgment
calls (docs/fact-check/coordinator.md). Claim-by-claim tables: docs/fact-check/fc1.md to fc9.md.

**Method limit (read this).** This environment's network policy blocks direct page fetches (WebFetch
and curl fail for phoenix.gov, roc.az.gov, weather.gov, cdc.gov, epcor.com and nearly every other
source). Claims were verified against WebSearch result summaries of the named official or credible
page, usually restricted to that source's domain, not by opening the page. WebSearch is also capped at
200 calls per turn shared by all agents, so each checker had about 25 to 34 searches; where the budget
ran out, checkers removed or softened what they could not confirm, and the few low-risk lines kept
without a fresh search are marked "not searched" in their logs. To re-verify by opening every source,
allow those domains in the environment's network settings and re-run the checkers.

| Checker | Pages | Claims checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc1 | /, /services/, /service-areas/, /how-it-works/, /about/, /faq/, /contact/, privacy, terms, 404, plus all 25 town summaries in site.json | 70 | 59 | 4 | 4 | 3 |
| fc2 | /pool-service/, /pool-cleaning-maintenance, /pool-service-cost/, /choosing-a-pool-company/ | 63 | 54 | 2 | 5 | 0 |
| fc3 | /pool-repair, /pump-repair, /pool-equipment-repair/, /pool-heater-repair/ | 51 | 41 | 1 | 7 | 1 |
| fc4 | /tile-cleaning, /pool-leak-repair/, /pool-resurfacing/, /repair-or-resurface-pool/ | 56 | 37 | 8 | 9 | 2 |
| fc5 | /pool-filter-cleaning/, /how-often-to-clean-pool-filter/, /monsoon-pool-care/, /green-pool-cleanup/, /why-is-my-pool-green/, /how-often-to-drain-pool-arizona/ | 107 | 48 | 18 | 17 | 22 |
| fc6 | North Phoenix, Scottsdale, Paradise Valley, Fountain Hills, Cave Creek, Carefree, Anthem | 91 | 57 | 8 | 7 | 15 |
| fc7 | Tempe, Mesa, Chandler, Gilbert, Ahwatukee, Queen Creek | 116 | 69 | 13 | 12 | 22 |
| fc8 | San Tan Valley, Apache Junction, Maricopa, Laveen, Glendale, Peoria | 60 | 42 | 5 | 2 | 11 |
| fc9 | Surprise, Sun City, Litchfield Park, Goodyear, Avondale, Buckeye | 103 | 67 | 5 | 15 | 6 |
| Coordinator | follow-ups and judgment calls | 9 | 4 | 1 | 3 | 1 |
| **Total** | 53 pages | **726** | **478** | **65** | **81** | **83** |

(Counts are as each checker reported them; a few rows include claims kept without a fresh search,
which are listed in that checker's log.)

**Most important fixes.**
- The site-wide claim that routine cleaning is "generally not treated as contracting" in Arizona had no
  source and was replaced everywhere with careful ROC wording (repairs, equipment and resurfacing
  generally need a licensed contractor; ask the ROC about cleaning-only service).
- Chandler's pool barrier rule was wrong (6-foot fence, gaps limited to 1 3/4 inches); Scottsdale's drain
  advice (pH and timing) and Fountain Hills' pool code were corrected; Phoenix's 12 gpm is a maximum.
- A July 2024 heat figure on /pump-repair came from the wrong weather station and was corrected.
- Leak detection prices re-matched to the cited Angi guide; derived monthly figures labeled as derived.
- Brand names (equipment and chemical makers) removed from copy and sources; neutral trade sources used.
- Unverified local history, population, neighborhood and utility claims removed from many town pages
  (for example Morrison Ranch, the Carefree ownership claim, Ahwatukee's annexation date, Harquahala).
- Glendale's hardness figure re-attributed to the correct City of Phoenix report.
