# Brief for independent fact-checkers (Oct 2026)

You did not write the pages you check. Repo: /home/user/phoenix-pool-cleaning-pro (branch build). Read
CLAUDE.md, INTAKE.md and docs/WRITING-GUIDE.md first (rules: no em/en dashes, no banned phrases, no
places outside the Phoenix metro, never imply the line does pool work, no invented facts).

For each page in your group (src/pages/<file>.html):
1. List every factual claim that is not common knowledge or business fact from INTAKE.md: numbers,
   dates, rules, phone numbers, fees, providers, names of programs, statutes, history, prices, and
   every source in the page's sources list.
2. Verify each with WebSearch (restrict allowed_domains to the official or named source domain).
   WebFetch and curl cannot reach most hosts; a search result summary of the cited official page is
   acceptable evidence. Check that each cited URL plausibly holds the claim (domain and page topic match).
3. Fix the page in place: CORRECT a wrong fact, SOFTEN a claim the evidence only partly supports, REMOVE
   a claim you cannot confirm (and its source if nothing else uses it). Rewrite in your own words; keep
   the page's structure, FAQs (3 to 6), images and macros. Never add an unsourced fact.
4. SEARCH BUDGET: WebSearch is capped at 200 calls per turn shared by all agents. Respect the cap in your
   task prompt. Verify the riskiest claims first (numbers, rules, phone numbers, prices, legal claims,
   anything the writer flagged). If the budget runs out, REMOVE or SOFTEN claims you could not confirm
   rather than leaving them unverified, and say so.
5. Validate: `python3 build.py --out /tmp/<you>/dist`, then
   `python3 scripts/check.py --dist /tmp/<you>/dist --skip-links --only <url>` for each page (0 errors,
   0 warnings) and `python3 scripts/similarity.py --dist /tmp/<you>/dist --other
   /home/user/dominionsoundmusic-create/houston-hvac-pro/dist --only <url as similarity prints it>` (no
   FAIL). Never run plain `python3 build.py`. Do not commit. Do not edit other pages or shared files.
6. Write docs/fact-check/<you>.md: a per-page table | Claim | Source checked | Verdict
   (confirmed/corrected/softened/removed) | Note |, then totals per page (claims checked, confirmed,
   corrected, softened, removed) and the number of searches you used. Report the totals back.
