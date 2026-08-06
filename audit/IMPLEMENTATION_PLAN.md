# IMPLEMENTATION PLAN

**Version**: 1.0
**Date**: 2026-08-06
**Principle**: Non-destructive — preserve every existing repository and live deployment.

---

## Phase 0: Pre-Flight (COMPLETED)

- [x] Full org scan — all 29 repos identified
- [x] Pages configuration audited — source repo/branch confirmed
- [x] Live URL verification — 16 of 18 Pages URLs confirmed working
- [x] Broken Pages identified: open-london-3d-drive, salesflow-crm-showcase
- [x] Empty placeholder repos identified: 9 category repos
- [x] Duplicate repo identified: studio-public-demos
- [x] 6 audit documents produced

---

## Phase 1: Catalogue Data (Non-destructive)

**Goal**: Replace the speculative demo-inventory.json with a verified catalogue of only existing demos.

### Step 1.1 — Build verified catalogue.json
- Source from REPOSITORY_INVENTORY.csv and PROJECT_CLASSIFICATION_MATRIX.csv
- Include ONLY the 18 substantive repos (exclude planned/placeholder demos)
- Each entry: verified pages_url, repo_url, classification, tags
- No data loss — the old demo-inventory.json remains as `demo-inventory-legacy.json`

### Step 1.2 — Verify all live URLs
- Curl each pages_url to confirm 200 response
- Verify index.html loads correctly
- Flag any demos that fail

### Step 1.3 — Screenshot capture (optional)
- Capture thumbnail screenshots for project detail pages
- Store in `screenshots/` directory

---

## Phase 2: Central Catalogue Website (Non-destructive)

**Goal**: Rebuild index.html to serve as the single central catalogue, driven by verified catalogue.json.

### Step 2.1 — Rewrite index.html
- Replace demo-inventory.json loading with catalogue.json
- Remove all 29 "planned" demo entries
- Add project detail page rendering (URL hash or path-based)
- Add proper URL parameter support (`?category=`, `?technology=`, `?industry=`)
- Add "Back to Catalogue" navigation from detail pages
- Keep existing design: nebulacloud.studio style, Inter/Cinzel fonts, Three.js hero

### Step 2.2 — Catalogue data binding
- Primary category → determined by classification matrix
- Live URLs → verified from deployment audit
- Maturity → determined by repo content assessment
- Tags → from classification matrix

### Step 2.3 — Project detail pages
- Client-side rendered (no build step)
- Route: `?demo={repo-name}` or hash-based `#demo/{repo-name}`
- Shows: screenshot, description, live link, repo link, classification, related demos

---

## Phase 3: Deploy & Verify

### Step 3.1 — Push to studio-public-demos.github.io
- Commit catalogue.json + updated index.html
- Push to main branch
- GitHub Pages auto-deploys

### Step 3.2 — Smoke test
- Visit https://studio-public-demos.github.io/
- Verify all 4 navigation paths work
- Click through to 2-3 live demos
- Verify search filters work
- Verify URL parameters work

### Step 3.3 — Link audit
- Every demo card links to correct pages_url
- Every demo card links to correct repo_url
- No broken links
- Back navigation works from demo detail to catalogue

---

## Phase 4: Repository Housekeeping (APPROVAL REQUIRED)

**DO NOT EXECUTE without explicit approval.**

### Step 4.1 — Archive duplicate repo
- Archive `studio-public-demos/studio-public-demos` (duplicate of .github.io)
- First verify no external links point to `/studio-public-demos/` subpath

### Step 4.2 — Fix broken Pages
- `open-london-3d-drive`: Rename default branch from `feature/open-london-3d-drive` to `main`, enable Pages
- `salesflow-crm-showcase`: Switch Pages source to correct branch

### Step 4.3 — Category repos decision
- **Option A**: Keep empty — use as organizational containers for future demos
- **Option B**: Archive — remove unnecessary repos
- **Option C**: Populate — add README with category overview + links to demos
- **Recommendation**: Option C (populate with READMEs) — creates useful landing pages

### Step 4.4 — Standardize repo documentation
- Add LICENSE to repos missing it (seaplane-outpost, vlm-aero, geovision, nefertiti, sponza, salesflow-crm-deploy)
- Add ATTRIBUTIONS.md where missing
- Standardize README format across repos

---

## Phase 5: Enhancements (Future)

- Screenshot thumbnails for every demo
- OpenGraph meta tags for social sharing
- RSS/JSON feed for new demos
- Demo submission workflow
- Automated Pages health monitoring

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Breaking existing Pages deployments | None | — | Only modifying studio-public-demos.github.io repo |
| Losing planned demo data | None | Low | Preserved in demo-inventory-legacy.json |
| Broken links after deploy | Low | Medium | Full link audit in Phase 3 |
| Category repo confusion | Low | Low | Add READMEs explaining their purpose |

---

## Files Modified (this plan)

| File | Action | Impact |
|------|--------|--------|
| `studio-public-demos.github.io/index.html` | Rewrite | Updates catalogue to verified data |
| `studio-public-demos.github.io/catalogue.json` | Create | New verified data source |
| `studio-public-demos.github.io/demo-inventory.json` | Rename | Preserved as legacy |
| No other repos modified | — | Zero impact |
