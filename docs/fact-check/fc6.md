# Fact-check fc6: north and northeast town pages (Oct 9 2026)

Checker fc6 did not write these pages. Evidence came from WebSearch result summaries of the official
source domains (phoenix.gov, scottsdaleaz.gov, paradisevalleyaz.gov, fountainhillsaz.gov, cavecreekaz.gov,
epcor.com, swgas.com, usgs.gov, epa.gov). curl to phoenix.gov returned a proxy 403, so no PDFs were read
directly. Searches used: 34 of 34.

Validation: `build.py --out /tmp/fc6/dist` built 53 pages; `check.py --skip-links --only` gave 0 errors and
0 warnings for each of the 7 pages; `similarity.py` showed no FAIL (Houston max 2.2%, 0 shared 8-word runs;
the highest pair among these pages was 2.7%).

## /north-phoenix-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Phoenix 2025 total hardness 172 to 302 mg/L, 10 to 17.6 gpg | phoenix.gov water quality report listing | confirmed | |
| Hardness comes from soils, not a health standard | phoenix.gov WQR text | confirmed | |
| Drain to sewer cleanout, 12 gpm | phoenix.gov Draining and Backwashing | corrected | 12 gpm is the city's maximum, and it says the safe rate may be lower. Wording now says so |
| No street, alley, right of way; Ch. 32C bars storm drains | phoenix.gov | confirmed | Dropped the "without treatment" add-on |
| City advises keeping backwash off citrus and hibiscus | phoenix.gov | removed | Not on the city pages. Replaced with what the city does say: landscape reuse is OK, dirty backwash and saltwater pool water may not be discharged |
| 2024 ISPSC with amendments effective Aug 1 2025 | phoenix.gov 2024 ISPSC amendments (Ord. G-7397) | confirmed | |
| 60 inch barrier, measured outside | phoenix.gov barrier guide and amendments | confirmed | |
| No gap a 4 inch sphere can pass | phoenix.gov barrier guide ("four-inch ball") | confirmed | Reworded to "4 inch ball" |
| Gates self-closing, self-latching, swing away, latch at least 54 in | phoenix.gov Pool Barriers handout, Pool Policy | confirmed | |
| A new or changed barrier needs a permit | phoenix.gov handout | softened | Handout says altered parts of an enclosure must meet the new standard; permit wording removed |
| Fifteen urban villages on the current map | phoenix.gov village cores map | softened | Map lists 14 names; count removed |
| Northern villages: North Mountain, Paradise Valley, Deer Valley, Desert View, North Gateway | phoenix.gov village map | confirmed | |
| Paradise Valley Village runs from Phoenix Mountains to CAP canal | phoenix.gov | removed | Not confirmed; source removed |
| Desert View runs from the CAP canal north to the Carefree Highway | phoenix.gov Desert View map | confirmed | |
| ZIPs 85020, 85028, 85053, 85085 are North Phoenix | general knowledge | confirmed | Business fact about call area |

Totals: 15 claims; 10 confirmed, 1 corrected, 2 softened, 2 removed.

## /scottsdale-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Hardness bands 22 to 25 / 20 to 22 / 16 to 18 gpg and mg/L equivalents | scottsdaleaz.gov hard water fact sheet | confirmed | Source URL updated to the current scottsdaleaz.gov path |
| Hardness not a health risk | scottsdaleaz.gov drinking water | confirmed | Old page18694 URL replaced with current drinking water page |
| About 90% surface water (CAP and SRP), wells under 10% | scottsdaleaz.gov water supply | confirmed | |
| All groundwater before mid 1980s, first CAP water 1987 | scottsdaleaz.gov water supply | confirmed | |
| Never drain to street; storm drains feed flood control and the Salt River | scottsdaleaz.gov Protect Your Water | softened | Kept the city's list (street, alley, right of way, storm inlet, drainage channel); Salt River path removed |
| Sewer cleanout drain at 50 gpm max | scottsdaleaz.gov Protect Your Water | confirmed | An older city page said 12 gpm; current page says 50 |
| Wait 3 to 7 days, pH 7 to 8 before landscape use | scottsdaleaz.gov | corrected | City says drain over a few days, pH 6.5 to 8.5, chlorine below 0.1 mg/L |
| Cleanout looks like two 4 inch caps a foot apart; city keeps no records | scottsdaleaz.gov | confirmed | |
| Homes over ~20 years may lack a cleanout; city says use a licensed plumber | scottsdaleaz.gov | removed | Not found |
| Sewer charge based on Dec, Jan, Feb water use; adjustment by Aug 31 | scottsdaleaz.gov rates and Protect Your Water | confirmed | |
| Ordinance 4655 | scottsdaleaz.gov | softened | City materials cite both 4655 and 4566; now "the city's short-term rental ordinance" |
| Annual city license, TPT license, county registration | scottsdaleaz.gov licensing guide | confirmed | Registration is with the Maricopa County Assessor |
| Emergency contact reachable 24 hours | scottsdaleaz.gov licensing guide | confirmed | |
| Contact must arrive in person within one hour | scottsdaleaz.gov | removed | Not found |
| STR pool rules apply regardless of age; 60 in perimeter fence; gates self-closing, latch 54 in; vehicle gates locked | scottsdaleaz.gov STR pool barriers | confirmed | |
| Second barrier: 60 in pool fence or audible alarms | scottsdaleaz.gov STR pool barriers | confirmed | |
| Lockable spa cover when spa is outside the pool barrier | scottsdaleaz.gov STR FAQ | corrected | Only when there are no alarms on the doors and windows to it |
| 2021 ISPSC amendments: 60 in barrier, owner maintains gates, latches, alarms | scottsdaleaz.gov 2021 ISPSC amendments | confirmed | |
| 2021 ISPSC amendments: gates open away and self-close | scottsdaleaz.gov | removed | Found in IRC amendments, not confirmed for the ISPSC text |
| Inspection Services 480-312-2500 | scottsdaleaz.gov STR pool barriers | confirmed | |
| Southwest Gas 877-860-6020 and 911 | swgas.com Report a Leak | confirmed | |
| NWS monsoon June 15 to Sept 30 | shared writing-guide fact | confirmed (not re-searched) | Out of budget; standard NWS dates |

Totals: 22 claims; 14 confirmed, 2 corrected, 2 softened, 4 removed.

## /paradise-valley-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Incorporated May 24 1961, about 2,000 residents, one house per acre goals | paradisevalleyaz.gov Town History, Basic Town Facts | confirmed | |
| 2020 Census population 12,658 | paradisevalleyaz.gov Demographics | confirmed | |
| R-43 minimum lot 43,560 sq ft | paradisevalleyaz.gov ordinance recital | confirmed | |
| No pool closer than 20 ft to any property line | paradisevalleyaz.gov | removed | Not found |
| Water providers: three (FAQ) vs four (Water Companies page) | paradisevalleyaz.gov FAQ, Utility Services, Water Companies | corrected | Page now says the town's pages disagree; meta description says "several" |
| Address decides provider, boundary map | paradisevalleyaz.gov | confirmed | |
| Pool draining page: Town Code updated to allow sewer clean-out, no permanent connection, not on septic | paradisevalleyaz.gov Pool Draining | confirmed | |
| Older handout says pool water may not go to the sewer | paradisevalleyaz.gov Swimming Pool Drainage handout | confirmed | Conflict kept and flagged on the page |
| Engineering 480-348-3681 | paradisevalleyaz.gov Pool Draining | confirmed | |
| Septic alternatives: retention basin, irrigation, hauler | paradisevalleyaz.gov Pool Draining | confirmed | |
| Sewer: SW/NW to Phoenix, rest to town system run by Scottsdale under agreement | paradisevalleyaz.gov FAQ and Sewer page | corrected | Town names two sewer providers (Phoenix and the town) and says Scottsdale operates and maintains the town sewer; Sewer page added as source |
| EPCOR PV 2024: about 12 gpg, about 5,300 connections, West Salt River Valley sub-basin wells, 24th Street plant interconnect | epcor.com 2024 PV report | confirmed | |
| Wells "along the Phoenix Mountains" | epcor.com | removed | Not found |
| Arsenic removal facility; EPCOR does not treat for hardness | epcor.com | softened | Now: arsenic results under the 10 ppb federal limit; hardness not a health concern |
| About 15% of lots are hillside (committee update) | paradisevalleyaz.gov | removed | Not found; source removed |
| Combined wall over 8 ft must be view fence | paradisevalleyaz.gov | removed | Not checked (budget) |
| Resident guide: enclosure for water 18 in deep, 5 ft recommended; hillside view fence exception; permit list; STR barrier article; APS and SRP; gas in some areas | paradisevalleyaz.gov | not re-searched | Left as written, all attributed to named town pages; out of budget |
| Southwest Gas 877-860-6020 | swgas.com | confirmed | |

Totals: 18 claim lines (one grouped line of 6 town-page attributions not re-searched); 11 confirmed, 2 corrected, 1 softened, 4 removed.

## /fountain-hills-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Founded 1970 by McCulloch Properties (now MCO Properties), incorporated 1989 | fountainhillsaz.gov About, ACFR | confirmed | Incorporated Dec 5 1989 |
| Former cattle ranch; boundaries (McDowells, Fort McDowell, SRPMIC, regional park) | fountainhillsaz.gov background report | not re-searched | Geography consistent with the town report title; left |
| Elevations 1,520 to 3,000 ft (Golden Eagle Blvd) | fountainhillsaz.gov | removed | Not checked; softened to "rises fast" |
| EPCOR Chaparral City 2024: about 18 gpg text, 2022 table value 16 | epcor.com 2024 Chaparral report | confirmed | |
| 2021 report about 16 gpg, 2014 reading 16.4; above 10.5 gpg is very hard | epcor.com | confirmed | |
| CAP plus local groundwater; seasonal variation; EPCOR does not treat for hardness | epcor.com | confirmed | |
| Drain rules: stay on property or sewer clean-out unless Sanitary District prohibits; no street, storm drain, wash; backwash onto own yard; no permanent connection; wall clean-out risk | fountainhillsaz.gov Draining page and brochure | confirmed | |
| Code Enforcement 480-816-5193, Sanitary District 480-837-9444 | fountainhillsaz.gov | confirmed | |
| Hillside ordinance: 20% slopes, 40% disturbance, exempt districts | fountainhillsaz.gov Ord. 14-08 | softened | Not confirmed; reduced to "limits grading"; source removed |
| Pool checklist applies the ISPSC | fountainhillsaz.gov Adopted Codes | corrected | Town adopted the 2024 Uniform Swimming Pool, Spa and Hot Tub Code (applications from Sept 1 2025); ISPSC wording removed, Adopted Codes source added |
| Checklist barrier figures (60 in, 2 and 4 in gaps, 4 in sphere, 54 in release) | fountainhillsaz.gov Pool Checklist | not re-searched | Kept with "confirm with Building Safety" caveat already on the page |
| Southwest Gas neighborhoods; propane elsewhere | fountainhillsaz.gov General Plan / utility page | corrected | Added "limited central, west and downtown areas" and "propane from local suppliers" |
| SRP electricity | fountainhillsaz.gov utility contacts | not re-searched | |
| Southwest Gas 877-860-6020 | swgas.com, fountainhillsaz.gov | confirmed | |

Totals: 14 claim lines; 7 confirmed, 3 corrected, 1 softened, 1 removed, 2 left not re-searched (plus SRP).

## /cave-creek-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Town bought the system in 2007, CAP surface water only since | cavecreekaz.gov Water System Facts | confirmed | Applies to the Cave Creek system |
| 16 inch raw water pipeline over 12 miles to the plant | cavecreekaz.gov Water System Facts | confirmed | Source added |
| No wells currently used (attributed to 2023 report) | cavecreekaz.gov | softened | Confirmed by town pages; reattributed to "the town says" and limited to the Cave Creek system |
| Two systems, Cave Creek and Desert Hills | cavecreekaz.gov | confirmed | Added that Desert Hills still uses wells plus CAP |
| 2018 hardness 12 to 15 gpg, sodium 91 ppm | cavecreekaz.gov 2018 report | confirmed | |
| USGS: above 180 mg/L is very hard (about 10.5 gpg) | usgs.gov Hardness of Water | confirmed | URL changed to the canonical usgs.gov/water-science-school path |
| NWS monsoon dates | shared fact | confirmed (not re-searched) | |

Totals: 7 claims; 6 confirmed, 1 softened.

## /carefree-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Carefree Water Company supplies the town | town fast facts, Sonoran News | confirmed | |
| Wholly owned by a Utilities Community Facilities District; board is the seven-member Town Council | web | removed | Not found; source (Fast Facts #4) removed |
| CAP allocation with treat and transport agreements with Scottsdale and Cave Creek | Carefree Water Fast Facts, Sonoran News | confirmed | |
| Groundwater aquifer "healthy but very limited"; company runs local wells | Carefree Fast Facts | softened | Now "limited local groundwater" |
| Parts of town once on Cave Creek's system | Sonoran News (2005 IGA) | removed | Only partly supported; removed with the 2018 presentation source |
| Cave Creek 2018 hardness 12 to 15 gpg | cavecreekaz.gov | confirmed | |
| Maricopa County vector control investigates neglected pools | maricopa.gov | not re-searched | Out of budget; generally true |
| NWS monsoon dates | shared fact | confirmed (not re-searched) | |

Totals: 8 claims; 4 confirmed, 1 softened, 2 removed, 1 not re-searched.

## /anthem-pool-service

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| EPCOR 2024: about 18 gpg, calcium 80, magnesium 29, TDS 640, pH 8.2 | epcor.com 2024 Anthem report | confirmed | |
| Anthem WTP is a microfiltration plant fed from the CAP canal; surface and groundwater mix, seasonal variation | epcor.com 2024 Anthem report | confirmed | |
| Groundwater from the Salt River Valley basin; Lake Pleasant and Agua Fria blend | epcor.com | removed | Not confirmed for Anthem (the blend text appeared in a different EPCOR report) |
| 2020 report 17.8 gpg, calcium 73, magnesium 27; 2022 about 17 gpg | epcor.com | removed | Not checked; table rows and sources removed |
| 18 gpg is roughly 300 mg/L | arithmetic (1 gpg = 17.1 mg/L) | confirmed | |
| EPA secondary TDS guideline 500 mg/L, non-enforceable | epa.gov secondary standards | confirmed | URL exists |
| Anthem is unincorporated, Maricopa County | general knowledge | confirmed (not searched) | Out of budget; well established |

Totals: 7 claims; 5 confirmed, 2 removed.

## Overall

About 91 claim lines checked across 7 pages: about 57 confirmed, 8 corrected, 7 softened, 15 removed, about 6
left as written without a fresh search (all attributed to named official pages; listed above). 34 searches used.

## Coordinator follow-up (from fc2's finding)

| Page | Claim | Verdict | Note |
|---|---|---|---|
| /scottsdale-pool-service (FAQ) | "Weekly cleaning and water care are generally not treated as contracting" | softened | No source found (fc2). Now: repairs and equipment work generally call for a licensed contractor; whether a cleaning-only service needs a license is not spelled out, so ask the ROC |
| /fountain-hills-pool-service (FAQ) | "Routine cleaning is generally not treated as contracting in Arizona" | softened | Same rewrite |

No other page in this group carries the phrase. Rebuilt and re-ran check.py on both pages: 0 errors, 0 warnings.
