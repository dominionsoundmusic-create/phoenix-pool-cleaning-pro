# Fact-check fc9: West Valley town pages (Oct 9 2026)

Checker: fc9 (did not write these pages). Method: WebSearch restricted to official domains (surpriseaz.gov / content.civicplus.com, epcor.com, maricopa.gov, litchfieldpark.gov, arizona.libertyutilities.com, census.gov, swgas.com, goodyearaz.gov, avondaleaz.gov, buckeyeaz.gov), with search-result summaries of the cited official documents as evidence. Searches used: 34 of 34.
Validation: `build.py --out /tmp/fc9/dist` built 53 pages; `check.py --only` 0 errors, 0 warnings for all six pages; `similarity.py` area max 3.2%, Houston max 0.3%, no shared 8-word runs.

## /surprise-pool-service
| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Not every Surprise resident is on city water | surpriseaz.gov/water | confirmed | |
| EPCOR one of several utilities serving some residents, ACC certificate (CC&N) | surpriseaz.gov EPCOR Franchise Extension Election | confirmed | Reworded so the ACC claim rests on the city page |
| "EPCOR treats Surprise as its own rate district" | epcor.com | removed | EPCOR's rate table maps Surprise to its Sonoran districts; EPCOR wastewater-bill source removed |
| Mountain Vista 2022 report: total hardness 43 to 91 ppm (5.3 gpg high) | 2022 Mountain Vista CCR (civicplus) | confirmed | |
| Calcium hardness 23 to 50 ppm | same | confirmed | Report lists calcium hardness 50; calcium 9.4 to 20 ppm, consistent with 23 to 50 as CaCO3 |
| TDS 226 to 300 ppm | same | confirmed | |
| Mountain Vista is groundwater, serves about 40,000 people | TapSafetyReport | removed | No official source found; TapSafetyReport source removed |
| Pool water barred from street, curb, sidewalk, neighbors, off property | Surprise draining brochure | confirmed | |
| Backwash never to street, curb, sidewalk, retention basin, adjacent property | same | confirmed | |
| Option 1 soak into own yard without runoff; option 2 sewer cleanout | same | confirmed | |
| Cleanout "black threaded cap with raised square nut" | same | corrected | Brochure: usually in front yard near home, often near a spigot, capped access port |
| Retention basins health risk to children and pets | same | confirmed | |
| Phone 623.222.6200 | same | confirmed | |
| Drinking Water Quality Reports page | surpriseaz.gov/634 | confirmed | |
| ROC R-6 classification, contractor search | shared fact (WRITING-GUIDE) | confirmed | Not re-searched |
Totals: 15 claims, 10 confirmed, 1 corrected, 0 softened, 2 removed (plus 2 shared-fact items kept).

## /sun-city-pool-service
| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| EPCOR runs Sun City water, PWS AZ0407099, yearly report | epcor.com 2020 to 2025 Sun City CCRs | confirmed | |
| (added) 2025 report hardness 7 to 11 gpg; EPCOR does not treat for hardness | 2025 Sun City CCR | confirmed, added | Also added to FAQ |
| (added) Unincorporated Maricopa County community | WTTW Sun City; Maricopa County P&D | confirmed, added | |
| (added) Opened 1960 as retirement community | WTTW, multiple histories | confirmed, added | |
| (added) County Senior Citizens overlay: at least one occupant 55 or older | Maricopa County Board of Adjustment report TU2022041 | confirmed, added | |
| Electric provider APS | aps.com | not added | APS service area not confirmed for Sun City; FAQ stays generic ("your bill names your utility") |
| Gas leak advice (911 or gas company on bill) | general safety | confirmed | |
Totals: 7 claims, 5 confirmed (4 added), 0 corrected, 0 softened, 0 removed, 1 not added.

## /litchfield-park-pool-service
| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Established 1916, incorporated 1987 | litchfieldpark.gov history, general plan | confirmed | |
| Goodyear cotton town, Paul Litchfield led land purchases, World War I | litchfieldpark.gov history | confirmed | "for tire cords" softened to "to reinforce its tires" (city wording) |
| Name official 1926 | same | confirmed | |
| Wigwam began as guest quarters, public resort 1929 | same | confirmed | |
| Palm and orange tree motif as trademark | general plan; mayor quote in Tree City release | confirmed | |
| 2025 Tree City USA | litchfieldpark.gov news (Apr 2026) | confirmed | |
| 2020 Census 6,847 | census.gov QuickFacts | confirmed | |
| Liberty Utilities (formerly Litchfield Park Service Co.), not a city department | litchfieldpark.gov Utility Services | confirmed | |
| Homes outside city limits with LP address get a different private provider | New Resident FAQ | softened | City says county island, "private water service"; reworded |
| Western Valley Salt River Aquifer, 200 to 600 ft | Liberty 2026 and 2021 CCRs | confirmed | |
| 2026 report (2025 data) hardness 150 to 360, avg 233 ppm; 8.8 to 21.1 gpg avg 13.6 | Liberty 2026 CCR | confirmed | |
| Sodium 65 to 210, avg 120 ppm | same | confirmed | |
| City Code 9-5-4(M) public nuisance, street/sidewalk/gutter/alley/easement/parking/neighbor | LP drainage pamphlet | confirmed | |
| Storm drains separate, discharge untreated | same | confirmed | |
| Clean-out 3 or 4 inch threaded cap; wall-type clean-out risky | same | confirmed | |
| 12 gpm maximum recommended, lower depending on line | same | confirmed | |
| Submersible pump at or below 700 gph with garden hose | same | confirmed | |
| Backwash to irrigate landscaping, only when needed | same | confirmed | |
| Liberty curtailment Stage 2 may request voluntary cuts | Liberty curtailment tariff notice | confirmed | |
| Barrier 5 ft from outside, 4-inch sphere, 2-inch bottom gap | LP barrier page | confirmed | |
| Gates outward, self-closing/latching, latch 54 in | same | confirmed | |
| Doors self-closing/latching | same | confirmed | |
| "City also asks for an alarm or closer" | LP Interactive Property Improvement Diagram | softened | Not on current barrier page; attributed to the diagram, source added |
| Pet door cannot breach barrier | LP 2017 Pools and Spas brochure | softened | Attributed to older brochure, source added |
| Barrier statute 36-1681 vs 32-1681 | LP barrier page vs 2017 brochure | n/a | Page cites no statute number; nothing changed (the city's current page itself shows 32-1681, brochure 36-1681) |
| APS, Southwest Gas, Liberty listed by city | Utility Services / FAQ | confirmed | |
| Southwest Gas 877-860-6020 | swgas.com | confirmed | |
| Monsoon June 15 to Sept 30 | shared fact (NWS) | confirmed | Not re-searched |
| Building permit and Design Review Board for fences | LP pages | not searched | Low risk, cited official pages; kept |
Totals: 29 claims, 23 confirmed, 0 corrected, 3 softened (incl. tire cords), 0 removed, 1 n/a, 1 not searched (kept, official source).

## /goodyear-pool-service
| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| 16,000 acres bought 1917 for Goodyear Tire, cotton, WWI | goodyearaz.gov history | confirmed | |
| WWII aircraft plant built parts and blimps for the Navy | same | softened | City: 1941 aircraft plant run by Goodyear Aircraft; blimps/Navy not confirmed |
| Name chosen 1944, incorporated 1946 | same | confirmed | |
| "About 400 homes and apartments and one grocery store" | same | removed | City timeline gives 151 homes, 250 apartments, several shops, undated |
| Census 65,275 (2010), 95,294 (2020), 125,359 (July 2025 est.) | census.gov QuickFacts | confirmed | |
| 2021 announcement: among 10 fastest growing | goodyearaz.gov | softened | Now "describes itself as one of the fastest growing"; source swapped to the found city article |
| HOA map neighborhoods (Estrella, Palm Valley, PebbleCreek, Canyon Trails) | city HOA map | not searched | Real Goodyear communities; kept |
| Estrella Mountain Regional Park 19,840 acres, 2nd largest county park | goodyearaz.gov regional parks | confirmed | |
| City water south of I-10, Liberty north | goodyearaz.gov backflow page | confirmed (writer flag) | Not re-searched beyond writer's citation; consistent with Liberty CCR naming Goodyear |
| Surface Water Treatment Plant opened early 2022 | goodyearaz.gov news | corrected | "opened in 2022"; exact month not found |
| 8 MGD, growth to 16, Colorado River via SRP canals | goodyearaz.gov news | confirmed | |
| "For decades ran entirely on wells" | goodyearaz.gov | softened | Now "cut the city's reliance on groundwater" (city wording) |
| Desalting groundwater | goodyearaz.gov news | removed | Not confirmed within budget; source removed |
| Hardness varies, no federal/state standard | Water Services FAQs | confirmed | |
| Public Works 623-932-3010 water quality technician | goodyearaz.gov | corrected | Number confirmed as Water Services line; "technician" wording removed |
| Liberty 233 ppm avg | Liberty 2026 CCR | confirmed | |
| Pool Drain Authorization via GOODYEAR311, free, 24 to 48 hrs, expires 20 days after approval | goodyearaz.gov application page | confirmed | |
| Discharge on property or private sewer clean-out; illegal to other property/ROW/open space | Water Services FAQs | confirmed | |
| Backwash into street or alley unlawful | goodyearaz.gov storm drain news | softened | Reworded: keep backwash on site or to clean-out, never street, common area or storm drain |
| Unattended running water is water waste | goodyearaz.gov | removed | Not found |
| Barrier: 18 in deep, over 8 ft, 5 ft tall, 4-inch sphere, chain link/fabric not approved | Goodyear pool fencing doc (12/2022) | confirmed | |
| Gates generally swing outward | same | corrected | Replaced with confirmed self-closing, self-latching, latch 54 in |
| Children under six extra requirements | same | confirmed | |
| Petty offense, no fine if barrier in 45 days plus safety course | same | confirmed | |
| Permit for new pool or wall over 6 ft | same | not searched | Kept, official source |
| Backwash 250 to 1,000 gallons; cartridge or hose-down alternative | Indoor and Pool Water Use | confirmed | |
| Sun can empty a pool in a year; blanket stretches swim season | same | softened/removed | Now: evaporation even on warm winter afternoons; shade, windscreen, blanket or liquid cover (confirmed) |
| Sewer based on Jan to Mar use, appeal | same; Sewer Appeal Q&A | confirmed | |
| Bucket test 3 to 4 days | same | confirmed | |
| Stage 1 water advisory, 5% goal, postpone pool draining | Curtailment Status Stage 1 | confirmed | |
| APS and Southwest Gas franchises | 2025 special election page | removed | Not verified within budget; sentence and source removed |
| Southwest Gas 877-860-6020 | swgas.com | confirmed | |
Totals: 32 claims, 19 confirmed, 3 corrected, 5 softened, 4 removed, 2 not searched (kept, official source). (Row "sun empties pool" counted as softened.)

## /avondale-pool-service
| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Colorado River (CAP) water via agreement with Phoenix, Phoenix pipelines | avondaleaz.gov Water Quality / Water Resources | confirmed | |
| Groundwater from city wells, West Salt River Valley Sub-Basin | same | confirmed | |
| CCR covering Jan to Dec 2025 posted June 2026 | avondaleaz.gov news (June 10 2026) | confirmed | |
| Paper copies at City Hall and libraries; archive | same | confirmed | |
| Utility billing FAQ: pool filler floats can stick; turn off and repeat meter test | avondaleaz.gov FAQ | confirmed | |
| New rates effective Jan 1 2026; 7.5% treatment and 6.2% resource fee on total water bill | FY2026 fee schedule, Utility Rates page | confirmed | |
| AviWise service portal | avondaleaz.gov AviWise pages | confirmed | |
| FAQ: cleaning "generally not" licensed | WRITING-GUIDE shared fact | corrected | Guide forbids implying cleaning is exempt; now matches standard ROC wording |
| APS or SRP depending on address | shared fact | confirmed | Generic |
Totals: 9 claims, 8 confirmed, 1 corrected, 0 softened, 0 removed.

## /buckeye-pool-service
| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| 33 active wells, about 11,970 acre-feet (3.9 billion gallons) | buckeyeaz.gov FAQ / Water Facts | confirmed | City pages vary (29 wells on rate page) |
| Groundwater the only delivered supply | buckeyeaz.gov | softened | City: almost entirely groundwater; lead, intro, FAQ updated |
| Hassayampa sub-basin source of all of it (ABC15) | ADWR/Buckeye model page | softened | Now "much of the planning area sits over the Hassayampa sub-basin, west of the White Tank Mountains"; ABC15 source replaced with city model page |
| Colorado River mostly used for recharge | buckeyeaz.gov | softened | Now "holds a Colorado River allocation and recharges water into the aquifer" |
| Three providers: city, EPCOR Water, Arizona Water Company | buckeyeaz.gov Utility Rates | softened | City confirms "two additional providers"; names not confirmed, removed throughout; Utility Rates source added |
| January 2023 model, 15% short of 100-year AWS | ADWR, Buckeye response, KTAR | confirmed | Attributed to ADWR model and city's description |
| About $80M, 5,926 acre-feet a year for 100 years, Harquahala | ABC15, KTAR, city flyer | softened | Harquahala removed (outside metro); 100 vs 110 years conflicts, duration removed; "in 2023" added |
| Nearly all homes belong to CAGRD | buckeyeaz.gov | softened | Membership share not confirmed; generic CAGRD description |
| Minerals calcium, sodium, magnesium; TDS secondary guideline | Water Facts | not searched | Kept, official source; "meets federal standards" removed |
| Much groundwater poor quality, wells sited for better water | 2025 Water Rate Adjustment | not searched | Kept, official source (budget exhausted) |
| CCR covers Jan 1 to Dec 31 2024 | Environmental Compliance | softened | Likely outdated by Oct 2026; now "each year's report covers the year before" |
Totals: 11 claims, 2 confirmed, 0 corrected, 7 softened, 0 removed (Harquahala and provider names removed inside softened rows), 2 not searched (kept, official sources).

## Overall
| Page | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---|---|---|---|
| surprise | 15 | 10 | 1 | 0 | 2 |
| sun-city | 7 | 5 (4 added) | 0 | 0 | 0 |
| litchfield-park | 29 | 23 | 0 | 3 | 0 |
| goodyear | 32 | 19 | 3 | 5 | 4 |
| avondale | 9 | 8 | 1 | 0 | 0 |
| buckeye | 11 | 2 | 0 | 7 | 0 |
| Total | 103 | 67 | 5 | 15 | 6 |
Remaining shared facts (ROC, NWS monsoon dates) and a handful of low-risk official-page claims were not re-searched (noted above). Searches used: 34.
