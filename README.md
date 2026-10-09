# phoenix-pool-cleaning-pro

Static site for phoenixpoolcleaningpro.com (Phoenix Pool Cleaning Pro, a free pool service phone line).

- Edit pages in `src/pages/`, shared data in `src/data/site.json`, templates in `src/templates/`.
- Build: `python3 build.py` (writes `dist/` and `docs/image-list.md`). Netlify publishes `dist/`.
- Checks: `python3 scripts/check.py`, `python3 scripts/similarity.py`, `python3 scripts/check_old_urls.py`,
  `python3 scripts/grep_check.py`, `node scripts/responsive_check.js` (with dist served on :8765).
- Records: `SERVICES.md`, `docs/keyword-plan.md`, `docs/decisions.md`, `docs/qa.md`, `docs/fact-check.md`,
  `docs/image-list.md`, `docs/playbook/`. The old live site is kept in `docs/old-site/`.
