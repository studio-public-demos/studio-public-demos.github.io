# CURRENT SHOWCASE AUDIT

**Date**: 2026-08-06
**Organization**: github.com/studio-public-demos
**Auditor**: NebulaCloud Studio automated audit

---

## 1. Organization Overview

| Metric | Value |
|--------|-------|
| Total repositories | 29 |
| Repos with GitHub Pages enabled | 18 |
| Repos with Pages built & live | 16 |
| Repos with substantive content (>1 file) | 18 |
| Empty category repos (placeholder only) | 9 |
| Duplicate repos identified | 1 |

---

## 2. Pages Discrepancy — RESOLVED

**Issue**: The public URL `https://studio-public-demos.github.io/` is live and active, but the nominal Pages repository `studio-public-demos.github.io` appeared empty through repository metadata.

**Resolution**: Two repos serve GitHub Pages at the org level:

| Repository | Pages URL | Status | Branch | Content |
|------------|-----------|--------|--------|---------|
| `studio-public-demos.github.io` | https://studio-public-demos.github.io/ | built | main | Portfolio showcase (recently deployed) |
| `studio-public-demos` | https://studio-public-demos.github.io/studio-public-demos/ | built | main | Older portfolio (duplicate) |

The `studio-public-demos.github.io` repo is the canonical org-level Pages source. The root URL `https://studio-public-demos.github.io/` serves from this repo's `main` branch, `/` path. The `studio-public-demos` repo (org-name/repo-name) also has Pages at the subpath `/studio-public-demos/` — this is a legacy duplicate that was created before the `.github.io` repo.

**Current state**: Both repos are populated. The `studio-public-demos.github.io` repo contains the showcase built in this session. No pre-existing content was overwritten because the repo was newly created during this session.

---

## 3. Repository Inventory Summary

### 3.1 Substantive Demo Repos (with live GitHub Pages)

| # | Repository | Pages URL | Branch | Size | Language |
|---|-----------|-----------|--------|------|----------|
| 1 | open-london-3d-showcase | https://studio-public-demos.github.io/open-london-3d-showcase/ | gh-pages | 1.9MB | HTML |
| 2 | nexustwin-industrial-digital-twin | https://studio-public-demos.github.io/nexustwin-industrial-digital-twin/ | master | 3.0MB | — |
| 3 | circato-ocean-plastic-tfw-dashboard | https://studio-public-demos.github.io/circato-ocean-plastic-tfw-dashboard/ | main | 1.0MB | — |
| 4 | royal-biryani | https://studio-public-demos.github.io/royal-biryani/ | main | 744KB | JavaScript |
| 5 | factory-bim | https://studio-public-demos.github.io/factory-bim/ | main | 661KB | HTML |
| 6 | car-concept-3d-dashboard | https://studio-public-demos.github.io/car-concept-3d-dashboard/ | main | 9.5MB | HTML |
| 7 | guntur-change-detection-dashboard | https://studio-public-demos.github.io/guntur-change-detection-dashboard/ | main | 1.7MB | HTML |
| 8 | 3d-gis-globe | https://studio-public-demos.github.io/3d-gis-globe/ | main | 1.6MB | HTML |
| 9 | metro-station-simulator | https://studio-public-demos.github.io/metro-station-simulator/ | main | 92KB | HTML |
| 10 | stadium-digital-twin | https://studio-public-demos.github.io/stadium-digital-twin/ | main | 2.2MB | HTML |
| 11 | seaplane-outpost-showcase | https://studio-public-demos.github.io/seaplane-outpost-showcase/ | master | 106MB | HTML |
| 12 | vlm-aerodynamics-demo | https://studio-public-demos.github.io/vlm-aerodynamics-demo/ | master | 467KB | HTML |
| 13 | geovision-pro-showcase | https://studio-public-demos.github.io/geovision-pro-showcase/ | master | 228KB | HTML |
| 14 | nefertiti-viewer | https://studio-public-demos.github.io/nefertiti-viewer/ | main | 1.5MB | HTML |
| 15 | sponza-viewer | https://studio-public-demos.github.io/sponza-viewer/ | main | 42MB | HTML |

### 3.2 Repos WITHOUT Live Pages

| # | Repository | Reason | Branch | Notes |
|---|-----------|--------|--------|-------|
| 1 | open-london-3d-drive | Pages returns 404 | feature/open-london-3d-drive | Implementation repo, unusual branch name, no main/master |
| 2 | salesflow-crm-showcase | Pages returns 404 | master | Static assets only, no index.html served |
| 3 | salesflow-crm-deploy | Pages returns 404 | master | FastAPI backend, not a static site |

### 3.3 Empty Category Repos (Placeholders)

| # | Repository | Status |
|---|-----------|--------|
| 1 | agentic-ai-autonomous-workflows | Empty — no commits |
| 2 | physical-ai-engineering | Empty — no commits |
| 3 | digital-twins-spatial-intelligence | Empty — no commits |
| 4 | geoai-earth-intelligence | Empty — no commits |
| 5 | computer-vision-visual-intelligence | Empty — no commits |
| 6 | industrial-ai-predictive-operations | Empty — no commits |
| 7 | defence-aerospace | Empty — no commits |
| 8 | climate-environment-sustainability | Empty — no commits |
| 9 | enterprise-applications-decision-intelligence | Empty — no commits |

### 3.4 Duplicate Repo

| Repository | Issue |
|-----------|-------|
| studio-public-demos | Duplicate of studio-public-demos.github.io. Serves at `/studio-public-demos/` subpath. Has live Pages. Should be archived after verification. |

---

## 4. Content Audit

### 4.1 Repository Documentation Completeness

| Standard File | Repos with file | Missing from |
|---------------|-----------------|--------------|
| README.md | 18/18 substantive repos | None |
| LICENSE | 6/18 | open-london-3d-drive, nexustwin, circato, vlm-aero, geovision, seaplane |
| ATTRIBUTIONS.md | 9/18 | Various |
| .gitignore | 11/18 | Various |

### 4.2 Common Patterns
- Most demo repos use single-page HTML with embedded Three.js/MapLibre
- Live demos serve via GitHub Pages on `main` or `master` branch
- `open-london-3d-showcase` is the only repo using `gh-pages` branch
- Assets (3D models, GeoJSON, textures) are committed directly to repos
- Several repos are large (seaplane-outpost: 106MB, sponza-viewer: 42MB) due to embedded binary assets

---

## 5. Current Homepage Assessment

The current homepage (`studio-public-demos.github.io`) serves the portfolio showcase built in this session. Key characteristics:

- Single-page application, loads data from `demo-inventory.json`
- 9 technology categories, 4 navigation views
- 47 cataloged demos (mix of real + planned)
- Three.js wireframe globe hero animation
- Per-section wireframe geometry backgrounds
- GitHub Pages status: built, branch `main`, path `/`

---

## 6. Critical Findings

1. **Pages source confirmed**: `studio-public-demos.github.io` repo, `main` branch — serves root URL
2. **Duplicate repo exists**: `studio-public-demos` serves at subpath — should be archived
3. **3 repos lack live Pages**: `open-london-3d-drive` (branch issue), `salesflow-crm-showcase`, `salesflow-crm-deploy`
4. **9 empty category repos**: Created as organizational placeholders, no content
5. **No cross-repository navigation**: Each demo repo operates independently with no links to sibling demos
6. **Catalog JSON references planned demos**: 15 conceptual/planned demos in catalogue.json have no corresponding repository
