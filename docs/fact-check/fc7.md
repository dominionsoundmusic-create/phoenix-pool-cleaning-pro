# Fact-check fc7 (Oct 9 2026)

Independent checker, did not write these pages. Pages: /tempe-pool-service, /mesa-pool-service,
/chandler-pool-service, /gilbert-pool-service, /ahwatukee-pool-service, /queen-creek-pool-service.
Method: WebSearch restricted to the official domain (tempe.gov, mesaaz.gov, chandleraz.gov, gilbertaz.gov,
phoenix.gov, queencreekaz.gov, srpnet.com, swgas.com, weather.gov); search result summaries of the cited pages
taken as evidence. Searches used: 34 of 34.

Validation after edits: `python3 build.py --out /tmp/fc7/dist` (53 pages), `scripts/check.py --only <url>`
0 errors 0 warnings for all six pages; `scripts/similarity.py` no FAIL (max area pair 4.0%, 0 pages sharing an
8-word run with Houston).

## /tempe-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Typical year 87% SRP, 7% groundwater, 6% CAP | tempe.gov drought plan (Sept 2025) | corrected | Figure is from the drought plan, not the FAQ (another city page says about 90% SRP). Attribution changed to the drought plan and that PDF added as a source. |
| Salt higher in TDS and chlorides, Verde higher in hardness; blend shifts seasonally | tempe.gov water FAQ | confirmed | |
| 2016 report: hardness avg 226 ppm, 13.2 gpg, range 5.8 to 26.3 gpg (100 to 450 ppm) | tempe.gov 2016 WQR | confirmed | |
| Divide mg/L by 17.1 for gpg; no primary or secondary standard for hardness | tempe.gov water FAQ | confirmed | |
| Annual report posted before July 1 | not found | removed | Sentence and source label reworded. |
| Sec. 21-3(b): 5 ft fence, self-closing/self-latching or padlocked gates, 4 inch sphere | tempe.gov code compliance | confirmed | |
| Same section: deteriorated pool / health hazard / insects is a violation | tempe.gov code compliance | confirmed | |
| Green pool source URL (.../health-safety/green-pool) | tempe.gov | corrected | Live page is .../building-structure/green-pool. |
| No pool water in alleys (ground unstable or uneven) | tempe.gov AMP FAQ | confirmed | |
| Water waste ordinance excludes periodic pool and spa draining | tempe.gov water waste | confirmed | |
| Report illegal storm drain discharge at (480) 350-4311 | tempe.gov stormwater | confirmed | Tempe 311 line. |
| Storm drains carry water untreated to parks, basins, washes, canals, lakes; pool discharge sheet on tips page | tempe.gov stormwater / tips | confirmed (partly) | Tips page lists a Pool Discharge PDF; untreated-runoff wording not quoted in results, kept as cited page topic matches. |
| 2024 ICC codes (incl. ISPSC) required for permit applications from Jan 1 2027 | tempe.gov building codes | confirmed | |
| Certified Water Efficient Home names a pool cover as a practice | tempe.gov CWEH | confirmed | |
| Grass rebate $0.50/sq ft up to $2,000 per home per fiscal year, pre-approval | tempe.gov rebates | confirmed | One older page says 25 cents; current pages say $0.50. |
| High-efficiency irrigation rebate up to $500 incl. smart controllers | tempe.gov rebates | confirmed | |
| Tempe Fire "layers of protection: supervision, fence, alarms" | not searched | softened | Now just points to the department's water safety page. |

Totals: 17 claims, 12 confirmed, 3 corrected, 1 softened, 1 removed.

## /mesa-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| 2025 CCR (issued 2026): City Zone about 12 gpg, Eastern and Southern 16 gpg | mesaaz.gov 2025 CCR | confirmed | |
| Citywide 12 to 22 gpg | mesaaz.gov Common Water Quality Concerns | confirmed | |
| 1 gpg = 17.1 ppm; surface water and wells; wells vary | mesaaz.gov 2025 CCR | confirmed | |
| Report has a map and hardness table; Water Quality Services 480-644-6461 | mesaaz.gov | confirmed | |
| "In the 85212 ZIP code or nearby" | none | removed | Not supported. |
| No notification or permit to drain to own sewer cleanout; use the one nearest the house | mesaaz.gov drain/backwash | confirmed | |
| "Usually a black threaded cap" | none | removed | |
| Mesa treats cleanout water and reuses it for irrigation or recharge | mesaaz.gov drain/backwash | confirmed | |
| 12 gpm | mesaaz.gov | softened | It is the maximum recommended rate, worded that way now. |
| pH 6 to 8 | mesaaz.gov | softened | City pages differ (6 to 8 vs 7 to 8); now "close to neutral pH". |
| Watch shower and tub drains; no solids | mesaaz.gov | confirmed | |
| Street/storm drain "may violate city code"; permanent drain line off limits | mesaaz.gov | corrected | City "discourages" storm drain disposal; code-violation and permanent-line claims not found. Replaced with the confirmed reasons (untreated, washes, basins, parks) and the confirmed street-manhole warning. |
| Pool repair (acid wash, replaster) wastewater barred from storm and sanitary sewers; owner responsible | mesaaz.gov | confirmed | |
| Filling Dec to March can affect sewer fee; April to Nov does not | mesaaz.gov | confirmed | |
| Pool water more salt and chlorine than tap; landscape caution | mesaaz.gov | corrected | Rewritten to the city's actual guidance: yard draining allowed, wait days for chlorine, drain slowly, salt-tolerant plants, keep water on your lot. |

Totals: 15 claims, 9 confirmed, 2 corrected, 2 softened, 2 removed.

## /chandler-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Founded 1912; incorporated Feb 16 1920 | chandleraz.gov "Then and Now" blog, history page | confirmed | City blog gives Feb 16 1920 legal incorporation (history page mentions a May 1920 vote). |
| 1950 about 3,800; Williams AFB 1941; about 30,000 in 1980 | Wikipedia | confirmed | |
| 1990 = 90,769, 2000 = 176,240 | not found | removed | Not confirmed; "grew sixfold in twenty years" reworded. |
| 2020 census 275,987 | Wikipedia / Census | confirmed | |
| 57% Salt and Verde, 37% Colorado, 6% groundwater | chandleraz.gov Colorado River shortage | confirmed | |
| Surface plant fed from Consolidated Canal; Santan Vista shared with Gilbert; recharge basins and injection wells | chandleraz.gov | confirmed | |
| Hardness 5 to 20 gpg, average 16.5; no EPA limit | chandleraz.gov WQ FAQ | confirmed | |
| 2023 report 163 to 340 mg/L = 9.5 to 19.9 gpg | chandleraz.gov 2023 WQR | confirmed | |
| No permit to drain to cleanout or on property; hard pipes to street, alley, right of way = direct connection, prohibited; street exception if cleanout cannot be found | chandleraz.gov pool drainage | confirmed | Added: alleys never allowed even with exception; HOA basin needs HOA consent. Exception page added to sources. |
| 12 gpm; shut off if backup | chandleraz.gov | confirmed | Softened to note the city says safe rate varies and a plumber may be needed. |
| Cleanout "3 or 4 inch black pipe", "city keeps no records", "never use a cleanout set in a wall" | not found | removed | |
| Fence: masonry, concrete or decorative; no hand/foot holds; wood fence replaced; gates self-closing, outward, latch over 54 in; gates over 4 ft locked | chandleraz.gov pool fencing, Pool Barrier Guidelines | confirmed | |
| "4 inch ball" openings | chandleraz.gov guidelines | corrected | Chandler limits spacing to 1 3/4 inches. Also added the confirmed 6 ft minimum height (FAQ and body). |
| Building permit required for pool fencing; applies whether or not children live there; Development Services 480-782-3000 | not found | removed | |
| Grass rebate $1.50/sq ft up to $2,000 vs older higher rate | chandleraz.gov news release | corrected | Made specific: cut from $2.00 and $3,000 cap as of Jan 1 2026; notice to proceed needed. Release added as source. |
| Water Conservation Office 480-782-3583 | chandleraz.gov rebate policy | confirmed | |
| No pools or fountains allowed in converted area | not found | removed | |
| Smart controller rebate up to $250 | chandleraz.gov residential rebates | confirmed | 50% of price up to $250. |
| SRP and APS both serve Chandler; Southwest Gas | chandleraz.gov connectivity page | confirmed | |
| SRP residential 24/7 line (602) 236-8888 | srpnet.com | confirmed | |

Totals: 20 claims, 14 confirmed, 2 corrected, 0 softened, 4 removed (plus a softened detail inside the 12 gpm row).

## /gilbert-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| H1 and H2 "largest town in America" | gilbertaz.gov | softened | Town self-description only. H1 now "From the Hay Capital to Today"; H2 now "a town of more than 260,000"; body keeps "the town describes itself as". |
| 1902 siding, Bobby Gilbert, Arizona Eastern Railway, incorporated July 6 1920, Hay Capital until late 1920s, 1,971 in 1970 | gilbertaz.gov history | confirmed | |
| 53 sq mi strip annexation "in 1970" | gilbertaz.gov history | corrected | Town says "during the 1970s". |
| 2010 208,453; 2020 267,918; housing 74,907 to 93,230 | gilbertaz.gov open data | confirmed | |
| Census estimate 288,790 for July 2024 | not confirmed | removed | Town sources give 292,116 and 289,260; dropped. |
| Nearing build out | gilbertaz.gov | confirmed | Now "build out within about a decade". |
| 2003 to 2007 permits clustered east and south | not found | removed | |
| 8 to 10 gpg; softener 10 to 12 | gilbertaz.gov water FAQ | confirmed | |
| 40% SRP, 41% CAP, 15% reclaimed, 4% groundwater | gilbertaz.gov | confirmed | |
| Santan Vista shared with Chandler treats CAP water | chandleraz.gov / gilbertaz.gov | confirmed | |
| 14 mile, 48 inch pipeline; Eastern Canal | not searched | removed | |
| North WTP rebuild into 2028, more than 70% | gilbertaz.gov | softened | "scheduled to finish by winter 2028", "about 70 percent" (pages vary). |
| Morrison Ranch 2,000 acres with reclaimed water | not searched | removed | Source removed. |
| Storm runoff raises canal turbidity, operators adjust | not searched | removed | Source removed. |
| NWS monsoon June 15 to Sept 30; 1 to 3 dust storms a year, mostly from southeast | weather.gov | confirmed | |
| HHW facility at 2224 E. Queen Creek Road; no pool chemicals in trash | not searched | softened | Address removed; now "check the town's household hazardous waste options". Source removed. |
| Southwest Gas 877-860-6020 | swgas.com | confirmed | |
| Drain: yard first, cleanout next (also for saltwater and high chemical water), street last | gilbertaz.gov pool draining | confirmed | |
| Saltwater never to street; backwash never to street; lake communities and flooding streets | gilbertaz.gov | softened | Lake-community and flooding limits are in the guidance but which method they attach to was unclear; worded as "the town's guidance flags". |
| No permit needed to drain | not found on page | removed | |
| Cleanout "black cap and square nut" | not found | corrected | Replaced with confirmed guidance: nearest cleanout, watch shower and tub drains. Added confirmed rule that a permanent pipe to cleanout or curb violates town code. |
| Maricopa County Environmental Services 602-506-6616 | not searched | removed | |
| Code Compliance (480) 503-6879 for pool water in street | gilbertaz.gov code FAQ | confirmed | |
| Fence 5 to 6 ft, house walls or solid wall, chain link or wrought iron; gates same height self-closing/latching; 4 inch sphere; permit may be required; renumbered code | gilbertaz.gov LDC FAQ | confirmed | |
| Fire: keep chairs and tables away from fence | gilbertaz.gov | confirmed | Door locks and alarms advice removed (not checked). |
| Utilities page lists SRP and APS with maps | not searched | softened | Now "SRP or APS depending on the address". Source removed. |
| Grass rebate up to $2,000 plus $1,000; pre-approval; no pools or fountains in converted area; smart controller $250 | gilbertaz.gov | confirmed | |
| 90% growth 2000 to 2010 (added to replace "built in a rush" card) | gilbertaz.gov | confirmed | |

Totals: 28 claims, 14 confirmed, 2 corrected, 5 softened, 7 removed.

## /ahwatukee-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| 1970 purchase of about 2,080 acres | Wikipedia | confirmed | |
| County approval Nov 1971; 17 model homes 1973 near 50th St and Elliot; 1984 peak over one house a day | not confirmed | removed | Also removed the "first model-home streets" mention in the why-call card. |
| Truck testing ground sold for development 1983 | single non-official source | removed | |
| Annexation complete by 1987 | search results | corrected | Sources say annexed in stages from 1978 to 1987; FAQ and body now say so. |
| Village 35.8 sq mi; 76,194 in 2000; about 85,000 today | not searched | removed | 2004 profile source removed. |
| Phoenix 2025 WQR hardness 172 to 302 mg/L (10 to 17.6 gpg); TDS 464 to 716 ppm | phoenix.gov 2025 WQR | confirmed | |
| Hardness not regulated as a health standard | phoenix.gov | confirmed | |
| 58% Salt and Verde, 40% CAP, 2% groundwater | phoenix.gov news release | confirmed | |
| NWS: 70 days at or above 110 and 143 days at 100+ in 2024 | not searched (budget) | softened | Now "2024 was one of its hottest years on record, according to the NWS". |
| Monsoon June 15 to Sept 30 | weather.gov | confirmed | |
| Loop 202 opening 2019 (writer flag) | n/a | n/a | Not present on the page. |

Totals: 10 claims, 5 confirmed, 1 corrected, 1 softened, 3 removed.

## /queen-creek-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Rittenhouse railroad spur near Rittenhouse and Ellsworth roads | queencreekaz.gov | confirmed | |
| Rittenhouse wells about 400 ft; cotton gin 1920s; families farming cotton, corn, potatoes | not confirmed | removed | |
| 1928 sale to Leo Ellsworth; Ellsworth Brothers Farms cotton, produce, cattle, sheep, dairy | queencreekaz.gov | confirmed | Reworded to match. |
| Citrus, pecans, vegetables still grown along Queen Creek Wash | not searched | removed | |
| Incorporated September 5 1989 | queencreekaz.gov | confirmed | |
| Just over 2,500 in 1990; 2024 estimate 83,781 | not searched | removed | |
| 2010 census 26,361; 2020 census 59,519 | not searched (budget) | softened | Now "more than doubled between the 2010 and 2020 censuses". |
| In both Maricopa and Pinal counties | queencreekaz.gov About | confirmed | |
| 2018 report: 20 active wells | not searched | removed | Source removed. |
| 100 year assured water supply based on groundwater | queencreekaz.gov | confirmed | |
| Hardness 6 to 17 gpg | queencreekaz.gov water FAQ | confirmed | |
| "In 2018" bought 2,033 acre feet of Colorado River water | queencreekaz.gov water transfer | corrected | 2,033 AF/yr Cibola Valley transfer via CAP confirmed; the 2018 date was not, now "through a water transfer from the Cibola Valley". |
| CAP canal along eastern edge; about 10% river reliance | queencreekaz.gov | confirmed | |
| 1980 GMA replenishment; 89% in CAGRD; all effluent offsets pumping | queencreekaz.gov | confirmed | District named. |
| Barrier: Ordinance 479-10, effective June 19 2010; 5 ft on all sides, or 5 ft on three sides plus cover, self-closing door or 4 ft barrier; above and in-ground | queencreekaz.gov pool barrier, permits | confirmed | |
| Pools and spas need a permit; fences have own permit with site plan and design | queencreekaz.gov | softened | Permit list confirmed; fence permit detail now "the town publishes separate fencing requirements". |
| Fire: latches out of children's reach, climbables away from fence | queencreekaz.gov | corrected | Release says fences 5 ft and gates self-closing and self-latching; worded to that. |
| Drain order: own property, clean-out (salt, green, shocked, acid washed, backwash only), curb last with de-chlorination, no flooding street, hose to curb, no flooding neighbors; no permit at this time | queencreekaz.gov pool draining policy, FAQ | confirmed | |
| Clean-out "in front of the house"; only on public sewer, not septic | 2011 town Q&A | softened | Location removed; septic now "the town has advised against this route". 48 hour notice (2011 source) is not on the page. |
| Owners responsible for sewer line to main | not found | removed | |
| Sewer fee from three winter billing cycles (about Nov to Feb); pool fill can be a qualifying event; fill outside that period | queencreekaz.gov sewer rates | confirmed | |
| SRP 602-236-8888; Southwest Gas; propane providers listed | queencreekaz.gov resident resources | confirmed | |
| Southwest Gas emergency 877-860-6020 | swgas.com | confirmed | |
| 2013 purchase of the H2O system expanded water service east into unincorporated Pinal County | queencreekaz.gov | confirmed | |
| Ironwood Crossing (south of Pima Rd) and Encanterra (south of Combs Rd) "sit on the Pinal side" | queencreekaz.gov utility exchange | corrected | Town confirms it became their wastewater provider in a 2023 exchange; locations removed. |
| Monsoon dates; 1 to 3 dust storms mostly from southeast | weather.gov | confirmed | |

Totals: 26 claims, 15 confirmed, 3 corrected, 3 softened, 5 removed.

## Grand totals

116 claims checked: 69 confirmed, 13 corrected, 12 softened, 22 removed (one unverified low-risk claim on
Tempe storm drains kept, cited page topic matches). Searches used: 34.
