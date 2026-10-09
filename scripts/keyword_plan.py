#!/usr/bin/env python3
"""Assign every keyword in keywords/Phoenix-Pool-Keywords.xlsx to a page (target or supporting)
or to the deliberately-unused list with a one-line reason. Writes docs/keyword-plan.md.

Usage: python3 scripts/keyword_plan.py   (exit code 1 if any row is left unclassified)
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "areas": "/service-areas/",
    "service": "/pool-service/", "cleaning": "/pool-cleaning-maintenance", "repair": "/pool-repair",
    "pump": "/pump-repair", "equipment": "/pool-equipment-repair/", "heater": "/pool-heater-repair/",
    "tile": "/tile-cleaning", "resurface": "/pool-resurfacing/", "filter": "/pool-filter-cleaning/",
    "green": "/green-pool-cleanup/", "leak": "/pool-leak-repair/",
    "g-cost": "/pool-service-cost/", "g-filter": "/how-often-to-clean-pool-filter/",
    "g-green": "/why-is-my-pool-green/", "g-resurface": "/repair-or-resurface-pool/",
    "g-monsoon": "/monsoon-pool-care/", "g-drain": "/how-often-to-drain-pool-arizona/",
    "g-choose": "/choosing-a-pool-company/",
}
TOWNS = {
    "north-phoenix": "north phoenix|85028|85020|85085|85053", "scottsdale": "scottsdale",
    "paradise-valley": "paradise valley", "fountain-hills": "fountain hills", "cave-creek": "cave creek",
    "carefree": "carefree", "anthem": r"anthem|85086", "tempe": "tempe", "mesa": r"\bmesa\b|85212",
    "chandler": "chandler", "gilbert": "gilbert", "ahwatukee": r"ahwatukee|85048", "queen-creek": "queen creek",
    "san-tan-valley": "san tan valley", "apache-junction": "apache junction", "maricopa": r"\bmaricopa\b(?! county)",
    "glendale": r"glendale|85308", "peoria": "peoria", "surprise": "surprise", "sun-city": r"sun city(?! west| center| grand)",
    "litchfield-park": "litchfield", "goodyear": r"goodyear|estrella mountain", "avondale": "avondale",
    "buckeye": "buckeye", "laveen": "laveen",
}

# Primary target keyword of each page (the rest of its assigned keywords are supporting).
TARGETS = {
    "pool cleaning phoenix": "home", "pool service and repair phoenix": "services", "pool service arizona": "areas",
    "pool service in phoenix": "service", "pool cleaning service phoenix az": "cleaning", "pool repair phoenix": "repair",
    "pool pump repair phoenix": "pump", "pool equipment repair phoenix": "equipment",
    "pool heater repair phoenix": "heater", "pool tile cleaning phoenix az": "tile",
    "pool resurfacing phoenix": "resurface", "pool filter cleaning phoenix": "filter", "green pool phoenix": "green",
    "pool leak repair phoenix": "leak", "how much does pool service cost in phoenix": "g-cost",
    "how often to clean pool filter": "g-filter", "will phosphate remover clear a green pool": "g-green",
    "how often do you resurface a pool": "g-resurface", "when is pool season in phoenix": "g-monsoon",
    "how often should i drain my pool in arizona": "g-drain", "pool companies in phoenix": "g-choose",
    "pool service north phoenix": "town:north-phoenix", "pool service scottsdale az": "town:scottsdale",
    "pool service paradise valley az": "town:paradise-valley", "pool service fountain hills az": "town:fountain-hills",
    "pool service cave creek az": "town:cave-creek", "carefree pool service": "town:carefree",
    "pool service anthem az": "town:anthem", "pool service tempe az": "town:tempe", "pool service mesa az": "town:mesa",
    "pool service chandler az": "town:chandler", "pool service gilbert az": "town:gilbert",
    "pool maintenance ahwatukee": "town:ahwatukee", "pool maintenance queen creek az": "town:queen-creek",
    "pool service san tan valley az": "town:san-tan-valley", "pool service apache junction az": "town:apache-junction",
    "pool service maricopa az": "town:maricopa", "pool service glendale az": "town:glendale",
    "pool service peoria az": "town:peoria", "surprise az pool service": "town:surprise",
    "pool service sun city az": "town:sun-city", "pool service litchfield park az": "town:litchfield-park",
    "pool service goodyear az": "town:goodyear", "pool service avondale az": "town:avondale",
    "pool service buckeye az": "town:buckeye", "pool service laveen az": "town:laveen",
}

U_PUBLIC = "a public pool, aquatic center or pool-hours search (CLAUDE.md: public pools go in the unused list)"
U_BRAND = "names a specific pool company or equipment brand (CLAUDE.md rule 3: never name a pool company)"
U_PLACE = "a place outside the Phoenix metro (rule 4)"
U_NOPAGE = "a town that showed zero searches and gets no page (Sun City West, El Mirage, Tolleson; CLAUDE.md)"
U_JOBS = "jobs, pay or business insurance for pool workers, not a homeowner service"
U_SUPPLY = "pool supply stores, parts or cleaning products (shopping, not a service)"
U_OFF = "off-topic: not about caring for or repairing a home pool"
U_BUILD = "pool construction, setbacks or building code (INTAKE.md: building new pools and fencing are not offered)"

RULES = [  # first match wins
    (r"\bjobs?\b|make an hour|\bpay\b|job description|insurance cost", ("unused", U_JOBS)),
    (r"tucson|temecula|el dorado|lake elsinore|kingman|green valley|\bvail\b|phenix city|phoenixville|phoenix md|"
     r"lake havasu|sun city center|paradise ca|sonora ca|carlsbad|cache creek|golden valley", ("unused", U_PLACE)),
    (r"maytronics|zodiac|pentair|pebble tec|gorilla glue|shasta|\bace pool|aaa pool|bestway|mccallum|pristine|pool shop service|"
     r"\bbpc\b|superior pool|overflow pool|bullfrog|beyond pool|meh pool|phoenix pool service inc|jesus pool|redline|amenity pool|"
     r"priority pool|flores pool|ironman|picture perfect|hollywood pools|arizona tile clean|love pool care|k&k|blue phoenix|"
     r"blue marlin|fowlers|phoenix pro pool|prestige pool|on demand pool|chandler pool service pro|\bllc\b|pool service inc\b|"
     r"mirage pool|az mirage|great valley|valley pool service|paradise valley spa|paradise valley pools|paradise pools|"
     r"blue pool services|anthem coverage|anthem payment|carefree pool and spa|& supply", ("unused", U_BRAND)),
    (r"^pool service in paradise$", ("unused", "ambiguous: \"paradise\" could be Paradise, California, not Paradise Valley")),
    (r"sun city west|sun city grand|el mirage|tolleson", ("unused", U_NOPAGE)),
    (r"hours|is the .* open|pool open|pools open|pools close|pool close|pool closes|when does .* pool|public pool|"
     r"community center|water park|heated pools|^pool (gilbert|surprise|apache junction|buckeye|glendale|goodyear|queen creek|"
     r"fountain hills)|^mesa az pool$|^pool buckeye( az)?$|^goodyear arizona pool$|^avondale (az pool|pool az)$|^anthem az pool$|"
     r"^san tan valley pool$|^fountain hills az pool$|^pool near|^pools near|^pool in tolleson|^sun city west az pools$|"
     r"^pool (near )?(san tan valley|tempe)|swimming pool hours", ("unused", U_PUBLIC)),
    (r"supply stores|supplies|repair parts|repair kit|pump repair store|filter cleaning solutions", ("unused", U_SUPPLY)),
    (r"setback|county pool code|cost of pool in phoenix|pool remodel", ("unused", U_BUILD)),
    (r"is .* safe$|cost of living|events|fountain schedule|fountain history|where is the fountain|where is the cave|"
     r"caves|expensive$|pool table|^pool with service$|pool fountain hills$|anthem pool care", ("unused", U_OFF)),
]
TOPIC = [
    (r"filter pressure low|filter not working|which pool filter|what pool filter|pool filter is the best|filter to buy|"
     r"why pool filters|will pool filter|are pool filters safe|filter system", "filter"),
    (r"filter", None),  # decided below: how-often questions to the guide, the rest to the service page
    (r"clarifier|phosphate", "g-green"),
    (r"green", "green"),
    (r"heater", "heater"),
    (r"tile", "tile"),
    (r"resurfac|deck", None),
    (r"patch|leak|crack", "leak"),
    (r"pump", "pump"),
    (r"equipment|motor|fountain", "equipment"),
    (r"cost|how much|price|per month|monthly|quote|call cost|worth having", "g-cost"),
    (r"drain|change pool water", "g-drain"),
    (r"pool season", "g-monsoon"),
    (r"license|companies|best pool|reviews|az best|pool guy", "g-choose"),
    (r"warranty|broken pool|emergency|commercial pool repair|pool repair|phoenix pool repairs|arizona pool repair", "repair"),
    (r"how often|how many times|how long does pool cleaning|include chemicals|services in my area|pool service in|"
     r"pool service phoenix|pool service near phoenix|pool service companies near me", "service"),
    (r"east valley|pool service arizona|pool services az|pool companies in arizona", "areas"),
    (r"clean|maintenance|vacuum|cleaners", "cleaning"),
    (r"service and repair", "services"),
]


HOME_SUPPORT = {"phoenix pool cleaning", "phoenix pool cleaners", "pool service companies near me"}


def classify(kw):
    k = kw.lower()
    if k in HOME_SUPPORT:
        return ("page", "home")
    if k in TARGETS:
        t = TARGETS[k]
        return ("town", t[5:]) if t.startswith("town:") else ("page", t)
    for pat, res in RULES:
        if re.search(pat, k):
            return res
    for slug, pat in TOWNS.items():
        if re.search(pat, k):
            if slug == "queen-creek" and "barrier" in k:
                return ("town", slug)
            return ("town", slug)
    for pat, page in TOPIC:
        if re.search(pat, k):
            if page is None and "filter" in k:
                return ("page", "g-filter" if re.search(r"how often|when|how many times|why clean|can you clean|steps|schedule", k) else "filter")
            if page is None:
                return ("page", "g-resurface" if re.search(r"how often|how long|last", k) else "resurface")
            return ("page", page)
    if re.search(r"^pool service$|pool service (phoenix|companies)", k):
        return ("page", "service")
    return None


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Phoenix-Pool-Keywords.xlsx", read_only=True)
    rows = list(wb["ALL"].iter_rows(values_only=True))[1:]
    seen, assigned, unused, missing = set(), defaultdict(list), [], []
    for seed, kw, typ, vol, sd, *_ in rows:
        if kw in seen:
            continue
        seen.add(kw)
        c = classify(kw)
        if c is None:
            missing.append(kw)
            continue
        kind, val = c
        if kind == "unused":
            unused.append((kw, vol, sd, typ, val))
            continue
        url = PAGES[val] if kind == "page" else f"/{val}-pool-service"
        role = "TARGET" if kw.lower() in TARGETS else "supporting"
        if role == "supporting" and re.search(r"near me\b|in my area", kw):
            role = "supporting (near me: national volume, supporting only)"
        assigned[url].append((kw, vol, sd, typ, role))
    if missing:
        print("UNCLASSIFIED:", missing)
        return 1
    n_as = sum(len(v) for v in assigned.values())
    out = ["# Keyword plan (Phoenix Pool Cleaning Pro, Oct 8 2026)", "",
           "Source: keywords/Phoenix-Pool-Keywords.xlsx (Ubersuggest, United States, pulled Oct 8 2026), ALL tab,",
           f"{len(seen)} unique keywords. Generated by `python3 scripts/keyword_plan.py`; every keyword is either assigned to",
           "one page (as its TARGET or a supporting keyword) or listed as deliberately unused with a reason.", "",
           "Rules applied:",
           "- \"Near me\" and \"in my area\" terms carry national volume. They are supporting keywords only and are never",
           "  read as proof of Phoenix demand.",
           "- Town pages: Maurice's rule for this site is that any town with 10 or more searches a month gets its own page.",
           "  That gives 25 towns (9 existing URLs kept, 16 new). Sun City West, El Mirage and Tolleson showed zero for",
           "  pool service and get no page; their rows are unused.",
           "- Public-pool searches (\"pool gilbert az\", \"surprise pool hours\", city aquatic centers), company and brand",
           "  names, supply shopping, jobs and places outside the Phoenix metro are unused.",
           "- Volume / SD = monthly searches / Ubersuggest SEO difficulty.", "",
           f"Assigned: {n_as}. Unused: {len(unused)}.", "", "## Assigned keywords by page", ""]
    order = list(PAGES.values()) + sorted(u for u in assigned if u not in PAGES.values())
    for url in order:
        if url not in assigned:
            continue
        out += [f"### {url}", "", "| Keyword | Volume | SD | Type | Role |", "|---|---:|---:|---|---|"]
        for kw, vol, sd, typ, role in sorted(assigned[url], key=lambda r: (r[4] != "TARGET", -(r[1] or 0), r[0])):
            out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {role} |")
        out.append("")
    out += ["## Deliberately unused", "", "| Keyword | Volume | SD | Type | Reason |", "|---|---:|---:|---|---|"]
    for kw, vol, sd, typ, why in sorted(unused, key=lambda r: (r[4], -(r[1] or 0), r[0])):
        out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {why} |")
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    for url in order:
        if url in assigned:
            t = [r for r in assigned[url] if r[4] == "TARGET"]
            print(f"{url:40s} {len(assigned[url]):3d} kws  target={t[0][0] if t else 'NONE'}")
    print(f"assigned {n_as}, unused {len(unused)}, total {len(seen)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
