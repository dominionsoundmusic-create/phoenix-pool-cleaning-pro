# Fact-check fc3 (independent, Oct 9 2026)

Pages: /pool-repair, /pump-repair, /pool-equipment-repair/, /pool-heater-repair/. Checker did not write these pages.
Method: WebSearch restricted to the official domain where possible (search result summaries of the cited pages; WebFetch and curl to energy.gov were blocked). Searches used: 32 of 34.
Validation after edits: `build.py --out /tmp/fc3/dist` OK; `check.py --only` 0 errors, 0 warnings on all four pages; `similarity.py` no FAIL (max vs Houston 2.2%, 0 pages sharing an 8-word run).

## /pool-repair

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| NWS Phoenix: 70 days at or above 110 in 2024 | weather.gov/psr/yearinreview2024 | confirmed | "DAYS MAX >= 110 70" |
| 113 days in a row at 100+, May 27 to Sept 16, 2024 | weather.gov/psr/ExtremeTemps | confirmed | |
| Phoenix sources: Salt, Verde, Colorado via CAP, groundwater | phoenix.gov water quality FAQ | confirmed | city says very little well water; wording ok |
| 2023 report total hardness 148 to 288 ppm | phoenix.gov wsdprimarywqr2023.pdf | confirmed | 8.6 to 16.8 gpg |
| ROC licenses contractors; R-6 Swimming Pool Service and Repair; B-5 builds and repairs pools and spas | roc.az.gov/license-classifications, R4-9-103 (Cornell) | confirmed | |
| Cleaning/water care generally not contracting; repair, equipment, resurfacing generally are | ROC classifications (fc2 found no source for the cleaning half) | softened | coordinator request: now says repair, equipment replacement and resurfacing generally call for a licensed contractor; whether cleaning-only service needs a license is not spelled out, ask the ROC |
| License required over $1,000 (labor and materials) or when a permit is needed | roc.az.gov/before-hire, azleg.gov 32-1121 | confirmed, softened | Current statute text on azleg.gov still shows $1,000; 2023 SB1715 proposed raising it, enactment not found. FAQ now adds "check the ROC site for the current rule" (body already did) |
| Complaint process and Residential Recovery Fund only for licensed contractors | roc.az.gov/before-hire, recovery-fund | confirmed | |
| Contractor search by name or number; shows status, classification, bond, complaints | roc.az.gov contractor search consumer guide PDF | confirmed | |
| Class must allow the work in the contract; call number on license record | roc.az.gov/before-hire | confirmed | |
| ROC phone 1-877-692-9762 | roc.az.gov | confirmed | |
| Written contract: contractor, license number, work description, price, dates | roc.az.gov/before-hire, A.R.S. 32-1158 | confirmed | |
| ROC advises no cash and no large up-front payments | roc.az.gov/before-hire | confirmed | |
| FTC: check coverage, length, who pays labor/shipping, how to claim | consumer.ftc.gov/articles/warranties | confirmed | |
| HO-3 excludes wear and tear, deterioration, mechanical breakdown, rust or corrosion | iii.org HO3_sample.pdf | confirmed | 2000 edition sample |
| NAIC: in-ground pool may need additional coverage | content.naic.org homeowners page | confirmed | added NAIC homeowners page as a source (statement is there, not clearly in the PDF) |

Totals: 15 checked, 12 confirmed, 0 corrected, 2 softened, 0 removed (plus 1 source added).

## /pump-repair

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| July 2024: average high 110.3, hottest July on record, peak 117 on July 8 | NWS yearinreview2024, July2024Climate.pdf | corrected | Those figures belong to another station's table. Phoenix: average high 112.3, peak 118 (5th and 8th), 2nd warmest July by average temperature. Text corrected; July 2024 summary added as source |
| DPPP standards, July 19, 2021, weighted energy factor | eCFR 10 CFR 431.465 | confirmed, softened | integral filter pumps get a timer rule instead of WEF; now "most new pool pump types" |
| 1.15 to 5 THP motors made on/after Sept 29, 2025 need variable-speed control | Federal Register 2023-20343, energy.gov DPPPM page | confirmed | |
| 0.5 to under 1.15 THP from Sept 28, 2027 | same | confirmed | FR synopsis table typo says 2025; codified text says 2027 |
| Motor rule covers motors sold by themselves (replacement motors) | 2023 final rule | confirmed | DOE: covered "regardless of how the equipment is sold" |
| April 2026 enforcement policy, no penalties before March 26, 2029, "citing limited models" | energy.gov/gc DPPPM enforcement policy (Apr 24, 2026) | softened | Policy delays enforcement for small-size motors made on/after Sept 28, 2027 and before March 26, 2029. Reason ("limited models") and "penalties" wording not confirmed; reworded to "delay enforcement," noted standard unchanged |
| Rules do not require removing a working pump | rule scope (manufacture dates) | confirmed | |
| APS tip: run pool pump off-peak on time-of-use plans | aps.com Energy Saving Tips | confirmed | |
| SRP residential pool pump rebate no longer offered | srpnet.com residential rebates FAQ | confirmed | source swapped from Trade Ally FAQ to SRP's live residential rebates page |
| APS/SRP serve most Valley homes depending on address | general, writing guide | confirmed | |

Totals: 10 checked, 7 confirmed, 1 corrected, 2 softened, 0 removed.

## /pool-equipment-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| 143 days at or above 100 in 2024 | NWS yearinreview2024 | confirmed | |
| City: hardness from calcium and magnesium picked up from soils | phoenix.gov water quality FAQ 2024 | confirmed | |
| City says hard water causes scaling | phoenix.gov | softened | City only ties hardness to cooler pad buildup; attribution removed, scale stated as general fact |
| PHTA: scale forms in cell even when water balanced | PHTA ECG fact sheet 2021 | confirmed | |
| PHTA: low salt lowers output, shortens plate life | same | confirmed | |
| PHTA: CO2 escaping pushes pH up, more with high alkalinity | PHTA total alkalinity / fact sheets | confirmed | link to aeration is general chemistry; wording ok |
| CPSC: faulty underwater lighting, old wiring among main concerns | cpsc.gov Don't Swim with Shocks | confirmed | |
| CPSC: test permanently installed GFCIs monthly | cpsc.gov GFCI fact sheet | confirmed | |
| NEC GFCI for underwater pool lighting since 1968; code applies to new work | cpsc.gov 099_0.pdf | confirmed | |
| Pressure cleaner booster pumps a separate DPPP class since July 19, 2021 | eCFR 431.465 | confirmed | WEF 0.42 |
| ROC R-6 class; contractor search | roc.az.gov | confirmed | |

Totals: 11 checked, 10 confirmed, 0 corrected, 1 softened, 0 removed.

## /pool-heater-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Southwest Gas emergency 877-860-6020, day or night, customers or not | swgas.com report-a-leak, safety brochure | confirmed | |
| Mercaptan added, rotten-egg smell | swgas.com safety | confirmed | |
| Hissing or roaring sound is a leak sign | swgas.com report-a-leak | confirmed | |
| Do not operate switches/controls, leave, call from a safe place | swgas.com | confirmed | |
| DOE: follow owner's manual, tune-up probably annually | energy.gov/energysaver/gas-pool-heaters | confirmed | |
| DOE: scale in burner or heat exchanger lowers efficiency | same | confirmed | |
| DOE: gas heaters last five or more years with proper install/maintenance | same | confirmed | |
| DOE: some gas pool heaters 89 to 95% efficient | same | confirmed | |
| 82% federal minimum for gas pool heaters made on/after April 16, 2013 | DOE appliance standards | confirmed | newer TEI standard due May 30, 2028, not mentioned (not needed) |
| DOE: gas heaters may not be most cost effective depending on climate | Energy Saver | removed | could not confirm wording; replaced with uncontroversial statement (no air-temp dependence, fuel cost trade-off) |
| DOE: heat pumps efficient above roughly 45 to 50 degrees | energy.gov heat pump pool heaters | softened | search summaries of the DOE page say works best above about 50 degrees, loses efficiency below; text changed to "above about 50 degrees" and "dip below that mark" |
| NWS 1991 to 2020 January normals: high about 68 (67.6), low about 46 (46.0) | NWS January climate summaries | confirmed | |
| Solar: pool pump pushes water through collectors, pool stores heat | DOE "Heat Your Water with the Sun" (34279.pdf) | confirmed | "almost no running cost" softened to pump doing the circulating |
| 2025 report total hardness 172 to 302 ppm | phoenix.gov wsdprimarywqr.pdf | confirmed | |
| R-6 covers service and minor repair; excludes gas lines, potable water connections, gas chlorine, electrical beyond first disconnect | roc.az.gov/license-classifications, R4-9-103 | confirmed | |

Totals: 15 checked, 12 confirmed, 0 corrected, 2 softened, 1 removed.

## Grand totals
51 claims checked: 41 confirmed, 1 corrected, 7 softened, 1 removed (per page: 12/0/2/0, 7/1/2/0, 10/0/1/0, 12/0/2/1). Searches used: 32.
