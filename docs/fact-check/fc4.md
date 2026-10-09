# Fact-check fc4 (independent, Oct 9 2026)

Pages: /tile-cleaning, /pool-leak-repair/, /pool-resurfacing/, /repair-or-resurface-pool/. Checker did not write these pages.
Method: WebSearch restricted to the official or named domain (search result summaries of the cited pages). Searches used: 25 of 34.
Validation after edits: `build.py --out /tmp/fc4/dist` OK (53 pages); `check.py --skip-links --only <url>` 0 errors, 0 warnings for all four; `similarity.py` (full run, `--only` crashes on an empty selection) no FAIL, max vs Houston 2.2%, 0 pages sharing an 8-word run, service max 1.9%.
Checker flag "our repair" / "Our weekly" on /pool-resurfacing/: confirmed fixed (no hit in the source; remaining "our guide" links only).

## /tile-cleaning

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| ADWR: Phoenix average evaporation about six feet a year, mostly summer | azwater.gov conservation technologies | confirmed | Source URL corrected to the indexed path new.azwater.gov/conservation/technologies |
| ADWR: covers save 90 to 95% of evaporation | azwater.gov Pool&Spas_2015_1.pdf | confirmed | |
| Scottsdale table, 400 sq ft pool: 10.8 in June, 2.6 in January | scottsdaleaz.gov water conservation for homeowners | confirmed | December (2.4) is actually lowest; page does not say January is lowest |
| Phoenix 2025 report total hardness 172 to 302 ppm | phoenix.gov 2025 water quality report | confirmed | |
| Hardness from calcium and magnesium picked up from soils en route to plants | phoenix.gov water_quality_faq_2024.pdf | confirmed | |
| Warm water drops calcium scale more readily | Aqua Tech Notes June 2018 (phta.org) | confirmed | Reworded to the source's point (scale shows first at sunny tile lines, spas); source added |
| Carbonate vs silicate table (looks, feel, formation, removal) | Orenda blog, Aqua Magazine, misc. | softened | Carbonate dissolves in acid, silicate largely immune to acid and poorly understood (Orenda). Removed unsourced "builds slowly over years on unremoved scale", "fingernail" and "glassy ridges" detail, and "many Valley pools have a mix of both" |
| Media blasting with glass beads; gentler than sandblasting; test spot first | Aqua "Scale does tile an injustice" | confirmed / softened | "Water lowered a few inches" changed to "below the tile line"; risks reworded generally |
| Pumice "softer than most glazed tile" | Aqua article | corrected | Source says pumice can take a little glaze off with the scale |
| Chemical descalers; lower water to tile line so acid stays off plaster | Aqua article | confirmed | "chelating" removed |
| Melamine sponge mild abrasive; can dull glossy/glass tile | Trouble Free Pool wiki and forum | softened | Evidence is anecdotal: now "very mild abrasive when wet", "some owners warn it can leave a haze" |
| Muriatic acid hazards; never mix acid with chlorine (toxic gas); store apart | CDC pool chemical safety poster | confirmed | CDC source added |
| LSI factors: pH, alkalinity, calcium hardness, temperature, TDS; near zero balanced, + scale, - etch | PHTA water balance fact sheet; Orenda LSI | confirmed | PHTA source added |
| Balanced in March can scale in July (temperature) | Aqua Tech Notes via PHTA | confirmed | |
| City of Phoenix "directs pool drain water to the sewer cleanout" | phoenix.gov Water Services FAQ, draining page | corrected | City: never the storm drain; to the sanitary sewer cleanout or irrigation |
| Phoenix says draining should be infrequent | phoenix.gov Water Services FAQ | confirmed | |
| "Some Valley pools need descaling every year or two" | none found | removed | |
| ROC license classifications, contractor search | roc.az.gov | confirmed | |

Totals: 18 claims checked; 11 confirmed, 3 corrected (pumice, Phoenix drain rule, source URL), 3 softened, 1 removed.

## /pool-leak-repair/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| ADWR six feet a year | azwater.gov | confirmed | URL corrected as above |
| Mesa chart 400 sq ft: about 79 in a year, about 20,000 gal | mesaaz.gov Pool-Leaks | confirmed | 79 in, 19,664 gal |
| Scottsdale 10.8 in June (about a third of an inch a day), 2.6 in January | scottsdaleaz.gov | confirmed | |
| Mesa: up to 30% of pools may have a leak | mesaaz.gov Pool-Leaks | confirmed | |
| Autofill can hide a leak | mesaaz.gov Pool-Leaks | confirmed | |
| Bucket test, 2 to 3 days, rain/wind can skew | scottsdaleaz.gov, mesaaz.gov | confirmed | |
| Pump on vs off: pressure side vs shell/suction | mesaaz.gov Pool-Leaks | corrected | Mesa: more loss with pump on = plumbing likely; about the same = shell/liner/fittings. Now attributed to Mesa (24 h each) |
| Dye, pressure testing, listening equipment | Aqua "Troubleshooting pool leaks"; Mesa (sonar, thermography, ultrasound) | confirmed | Added that dye must be very close to the leak; sources added |
| Underwater two-part epoxy patches for small cracks and fittings | Pool & Spa News "Tracking down cracks"; Aqua | confirmed / softened | Removed unsourced "swimming and water balance barely affected" |
| Check cracks/crazing cosmetic; structural movement cracks need cause fixed | NPC pool plaster FAQ | confirmed | Reworded and attributed; soil-movement/washout example removed |
| R-6 scope: excludes potable plumbing connections, gas, electrical past first disconnect, complete plaster/pebble interior and deck replacement | roc.az.gov license classifications, R4-9-103 | confirmed | |
| Phoenix asks residents to drain rarely | phoenix.gov FAQ | confirmed | |

Totals: 12 claims checked; 9 confirmed, 1 corrected, 2 softened, 0 removed (example sentence trimmed).

## /pool-resurfacing/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| Angi Phoenix average about $11,363; most $6,198 to $15,495 | angi.com Phoenix resurfacing | confirmed | |
| Angi: heat, sun, hard water, mineral buildup wear Phoenix finishes | same | confirmed | |
| Angi tile several times plaster per sq ft | same ($4.13 plaster, $25.83 tile) | confirmed | |
| HomeGuide 2026: plaster $6,000 to $8,000, quartz $7,000 to $10,000, pebble $7,000 to $15,000 | homeguide.com | confirmed | Added "based on about 1,000 sq ft" |
| HomeGuide life: plaster 7 to 12, quartz 10 to 15, pebble 15 to 20+ | homeguide.com | confirmed | |
| Angi: ceramic tile up to 50 years well kept | angi.com pool-finishes | confirmed | |
| Angi: plaster "around 10 years when applied properly" | angi.com pool-finishes | corrected | Angi says "up to 10 years" |
| White plaster = cement and marble dust | NPC white cement page | corrected | white cement, white marble aggregate and water |
| "Delamination" as hollow/peeling finish | NPC FAQ | corrected | NPC separates debonding and delamination; bullet reworded |
| Etching "often worst on steps and benches" | none found | removed | |
| Poor prep a common cause of early failure | NPC FAQ | softened | Now attributed: poor bond a main cause; delaminated material must be removed |
| Refill "usually soon after" finish applied | NPC FAQ (too-early filling is a listed mistake); PHTA startup | corrected | Now: follow the startup plan; filling too early is a listed mistake |
| Startup dust; frequent brushing | PHTA fresh fill start-up | confirmed | Now: brush at least twice a day until dust clears |
| ROC: three written estimates; reconcile with contract; payments not ahead of work; signed change orders | roc.az.gov before-hire | confirmed | |
| R-6 excludes complete plaster/pebble interiors and decks; B-5 builds and repairs pools and spas | roc.az.gov license classifications | confirmed | Page correctly sends full resurfacing to B-5 or similar |
| "our repair" / "Our weekly" wording | source grep | confirmed fixed | |

Totals: 16 claims checked; 10 confirmed, 4 corrected, 1 softened, 1 removed (the "our repair" wording flag is confirmed fixed).

## /repair-or-resurface-pool/

| Claim | Source checked | Verdict | Note |
|---|---|---|---|
| HomeGuide life spans (plaster, quartz, pebble) | homeguide.com | confirmed | |
| Angi tile up to 50 years | angi.com pool-finishes | confirmed | |
| Angi Phoenix: heat, sun, hard water wear finishes | angi.com Phoenix | confirmed | |
| Prep: poorly prepared surface lets go early | NPC FAQ | softened | Attributed to NPC (poor bond a main cause) |
| Aggressive water (low pH, alkalinity, calcium) etches cement finish | NPC tech bulletin 03 and FAQ | confirmed | Reworded and attributed; "steps and benches first" removed |
| Scaling water (high pH, TA, CH, warm) leaves crust | Aqua Tech Notes via PHTA | confirmed | "white or gray" trimmed to white |
| LSI components and sign convention; temperature shifts it | PHTA fact sheet; Aqua Tech Notes | confirmed | Sources added |
| Cosmetic vs structural cracks | NPC FAQ | confirmed | Source added |
| R-6 excludes complete interior replacement | roc.az.gov | confirmed | |
| "Two pools a decade apart"; "steps and benches wear first"; "patches rarely match" | none | softened | Generalized wording |

Totals: 10 claims checked; 7 confirmed, 0 corrected, 3 softened, 0 removed.

## Summary

| Page | Checked | Confirmed | Corrected | Softened | Removed |
|---|---|---|---|---|---|
| /tile-cleaning | 18 | 11 | 3 | 3 | 1 |
| /pool-leak-repair/ | 12 | 9 | 1 | 2 | 0 |
| /pool-resurfacing/ | 16 | 10 | 4 | 1 | 1 |
| /repair-or-resurface-pool/ | 10 | 7 | 0 | 3 | 0 |
| Total | 56 | 37 | 8 | 9 | 2 |

Searches used: 25 of 34. Note: industry sources added (NPC, PHTA, Aqua Magazine, Pool & Spa News, Trouble Free Pool wiki, and one Orenda Technologies chemistry blog for calcium silicate, labeled as a chemical maker, not a pool service company). Phoenix FAQ URL phoenix.gov/waterservices/resourcesconservation/faqs left as cited; the indexed FAQ lives at phoenix.gov/waterservices/faqs, so the coordinator may want to align it site-wide.
