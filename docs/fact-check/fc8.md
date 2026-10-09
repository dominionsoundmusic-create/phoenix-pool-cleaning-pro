# Fact-check fc8: south and west town pages (Oct 9 2026)

Checker fc8 did not write these pages. Evidence came from WebSearch result summaries of the cited or
official domains (pinal.gov, epcor.com, ajwaterdistrict.org, apachejunctionaz.gov, azwater.com,
maricopa-az.gov, gwresources.com, phoenix.gov, azdot.gov, peoriaaz.gov, Glendale council packets on
destinyhosted.com, plus news coverage). curl to epcor.com was refused by the proxy (403), so no PDFs were
read directly. Searches used: 34 of 34.

Validation: `build.py --out /tmp/fc8/dist` built 53 pages; `check.py --skip-links --only` gave 0 errors and
0 warnings for each of the 6 pages; `similarity.py` showed no FAIL (Houston max 0.6%, 0 shared 8-word runs;
highest town pair for these pages 4.0%, Apache Junction; Glendale 3.2%, Peoria 1.0%).

## /san-tan-valley-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Aug 5 2025 Prop 495 vote, about 66% yes in early returns | KJZZ, Fox10, Axios | confirmed | |
| 12,343 ballots counted | news reports | removed | Reports give 12,338; count dropped |
| Town from July 1 2026 | pinal.gov notice | corrected | Board of Supervisors approved incorporation Sept 2025; county notice sets July 1 2026 as the official start, county services until then. Timeline step added |
| "Arizona's 92nd municipality" | news, campaign chair | removed | Only campaign and secondary sources |
| Largest incorporation in Arizona history, over 100,000 people | pinal.gov, Ballotpedia, ABC15 (123,000 Census est.) | confirmed | Now "largest by population"; pinal.gov source added |
| 10,641 signatures accepted, 6,107 required | pinal.gov CivicAlert 1696 | confirmed | Source switched to the county |
| 2022 law: only Gilbert and Mesa had to approve | Ballotpedia (HB 2455), KGUN, ABC15 | confirmed | |
| Gilbert Aug 2024, Mesa weeks later | Ballotpedia: Aug 6 and Aug 19 2024 | corrected | "about two weeks later" |
| EPCOR San Tan: groundwater only, inside Phoenix AMA (2025 report) | epcor.com 2024 San Tan report | corrected | 2025 report is listed but its text could not be read; page and source now cite the 2024 report |
| NWS monsoon June 15 to Sept 30 | shared, confirmed by fc2/fc3/fc6 | confirmed | |
| Sources: CDC, Southwest Gas, ROC | domain/topic match | confirmed | |

Totals: 11 claims; 6 confirmed, 3 corrected, 0 softened, 2 removed.

## /apache-junction-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| City lies in Maricopa and Pinal counties, mostly Pinal | Census BAS map, city plan | confirmed (not re-searched) | Well-established fact |
| 2020 census 38,499 | census.gov QuickFacts | confirmed | |
| Census 2025 estimate 45,672 | only citypopulation.de | removed | Not found on census.gov |
| 2008 study: nearly 50,000 winter visitors, 20,000 in RV parks | searched | removed | Study not found; replaced with a general, number-free line about seasonal residents; source removed |
| Two water providers by address (AJWD, Arizona Water Co.) | apachejunctionaz.gov Utility Services | confirmed | |
| AJWD blend: groundwater (arsenic treated) plus CAP water treated at Superstition Area Water Plant (2017) | AJWD report, KJZZ 2017 | confirmed | |
| Hard water above 10.5 gpg; 232 mg/L at Well No. 5 | ajwaterdistrict.org hardness FAQ | softened | 10.5 is the classification threshold for the blend; 232 mg/L (13.5 gpg) is a single 2014 well test. Wording now says so |
| Arizona Water Co. supply incl. AJWD water (2025 report) | azwater.com 2024 report | corrected | 2024 report: groundwater from area wells. Source switched to 2024 report |
| AWC sodium 170 ppm avg, 150 to 190, 2021 samples | azwater.com 2022 report | confirmed | |
| Electric SRP, gas Southwest Gas | apachejunctionaz.gov | confirmed | |
| ADWR 4 to 6 ft yearly evaporation | azwater.gov (confirmed by fc2/fc3) | confirmed | |
| July 1 2025: AJ monitor AQI 208, unhealthy | pinal.gov draft 2025 exceedances | softened | Kept AQI 208 (marked draft); 15 to 25 mph morning winds and 40 to 50 mph haboob narrative removed (not tied to that date in the excerpt) |
| ADEQ includes AJ in Phoenix forecast | not checked | removed | Out of budget; source removed |
| Lost Dutchman SP on SR 88, summers above 100 | azstateparks.com | confirmed (not re-searched) | Common knowledge |
| City Code 7-4: owner keeps enclosure, gates, latches in working order; no alteration except to repair | apachejunctionaz.gov Pools and Pool Barriers | confirmed | |
| Pet door over 4 inches counts as a door | apachejunctionaz.gov | removed | Not found; also removed from FAQ |
| City does not make older pools meet new rules at sale | apachejunctionaz.gov | removed | Not found |
| Rules in force when pool was built still apply; re-plastering needs no permit | apachejunctionaz.gov FAQ | confirmed | |
| 2018 ISPSC adopted 2019 | not checked | removed | Out of budget; source removed |
| Stormwater: pool water allowed only if no chemicals for 3 days | AJ 2022 Stormwater Management Plan | confirmed | |
| Civil fine up to $2,500, repeat = misdemeanor | AJ Floodplain and Stormwater Standards brochure | confirmed | |
| Engineering Division (480) 474-5084 | apachejunctionaz.gov | confirmed | Source URL corrected to /154/Stormwater-Information |

Totals: 22 claims; 13 confirmed, 1 corrected, 2 softened, 6 removed.

## /maricopa-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Incorporated Oct 15 2003, 88th municipality | maricopa-az.gov | confirmed | |
| 1,040 in 2000; 15,934 in Dec 2005 special census | maricopa-az.gov, Wikipedia | confirmed | |
| 58,125 in 2020; city estimate about 73,300 (about 25% more) | maricopa-az.gov, housing study | confirmed | |
| City is in Pinal County | maricopa-az.gov | confirmed | |
| Global Water Santa Cruz Water Co. report for Maricopa, AZ04-11-131 | gwresources.com CCR | confirmed | Report says groundwater from wells |
| Monsoon dates; CDC, SW Gas, ROC sources | shared | confirmed | |

Totals: 6 claims; 6 confirmed, 0 corrected, 0 softened, 0 removed.

## /laveen-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Partly Phoenix's Laveen Village, partly unincorporated | Wikipedia, phoenix.gov | confirmed | |
| Village between South Mountain and the Salt River | phoenix.gov | confirmed | |
| Council districts 7 and 8 | Wikipedia; phoenix.gov Laveen VPC case numbers end in -7 and -8 | confirmed | |
| 1884 settlement, Salt River year round until Roosevelt Dam 1911, Central Ave bridge 6+ miles | Wikipedia | confirmed | |
| Laveen School 1913, Walter Laveen postmaster March 1918, store near 51st Ave and Dobbins | Wikipedia | confirmed | |
| City fact sheet projects 70,450 residents by 2030 | phoenix.gov | removed | Not found; replaced by a confirmed fact from the same city document (about 5,778 acres under county jurisdiction) |
| Phoenix 2025 hardness 172 to 302 mg/L (10 to 17.6 gpg), TDS 464 to 716 | phoenix.gov (confirmed by fc6 and others) | confirmed | |
| Loop 202 South Mountain: voter approval 1985 and 2004, opened end of 2019, I-10 at 59th Ave | azdot.gov | confirmed | ADOT anniversary source added |
| Monsoon dates | shared | confirmed | |

Totals: 9 claims; 8 confirmed, 0 corrected, 0 softened, 1 removed.

## /glendale-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Three sources: SRP (Salt and Verde), CAP (Colorado River), city wells | glendaleaz.gov Your Water | confirmed | |
| Reclaimed water used only for irrigation, not drinking | glendaleaz.gov | removed | Not seen in results |
| ADEQ database lists Pyramid Peak, Cholla, Oasis as active sources | not checked | removed | Out of budget; ADEQ source removed |
| Pyramid Peak in north Phoenix, shared with Peoria, Glendale owns 77% and operates it, serves north of both cities | Peoria Times, WaterTech | confirmed | |
| CAP supply 22,582 acre-feet a year, delivered to Pyramid Peak, usable citywide | Glendale council water updates 2024, June and Oct 2025 | confirmed | |
| Hardness 153 to 309 ppm (about 9 to 18 gpg) in 2023, attributed to City of Phoenix "Glendale Hedgepeth" report | phoenix.gov 2023 report | corrected | It is a City of Phoenix report for the Phoenix Hedgepeth Hills system that Glendale supplied and operated; it states Glendale's drinking water hardness 153 to 309 ppm, average 229. Attribution reworded and source URL fixed (old URL was a guess) |
| Hardness not a health standard | same report | confirmed | |
| ROC licensing wording | shared writing-guide facts | confirmed | |
| Electric provider and pool drain rules (optional additions) | not searched | not added | Out of budget; nothing unsourced was added |

Totals: 8 claims; 5 confirmed, 1 corrected, 0 softened, 2 removed.

## /peoria-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Shared CAP water with Glendale since late 1990s | WaterTech 2015 | confirmed | Plant built 1985, first expansion 1999 |
| Joint Pyramid Peak ownership, Glendale larger share and operates, serves north of both cities incl. Vistancia | Peoria Times | confirmed | |
| City looked to expand the plant for growth | WaterTech | confirmed | |
| ADDED: hardness by source, Greenway about 13 gpg, Pyramid Peak about 17, wells 2 to 8 | peoriaaz.gov Water FAQ | confirmed (added) | Added to the body and the water FAQ, with the city FAQ and reports pages as sources |

Totals: 4 claims; 4 confirmed (1 of them newly added), 0 corrected, 0 softened, 0 removed.

## Grand totals
60 claims checked: 42 confirmed, 5 corrected, 2 softened, 11 removed (one fact added to Peoria and one to
Laveen, both sourced). Searches used: 34.
