# TARGET INFORMATION ARCHITECTURE

**Version**: 1.0
**Date**: 2026-08-06

---

## 1. Site Structure

```
https://studio-public-demos.github.io/          ← Central catalogue (homepage)
├── /                                           ← Home: hero, stats, featured demos
├── /?category={key}                            ← Category filtered view
├── /?technology={key}                          ← Technology filtered view
├── /?industry={key}                            ← Industry filtered view
├── /search?q={query}                           ← Search results
├── /demo/{repo-name}/                          ← Project detail page
│
├── Subpath demos (existing, preserved):
├── /open-london-3d-showcase/                   ← Live demo
├── /nexustwin-industrial-digital-twin/         ← Live demo
├── /circato-ocean-plastic-tfw-dashboard/       ← Live demo
├── /factory-bim/                               ← Live demo
├── /car-concept-3d-dashboard/                  ← Live demo
├── /guntur-change-detection-dashboard/         ← Live demo
├── /3d-gis-globe/                              ← Live demo
├── /metro-station-simulator/                   ← Live demo
├── /stadium-digital-twin/                      ← Live demo
├── /seaplane-outpost-showcase/                 ← Live demo
├── /vlm-aerodynamics-demo/                     ← Live demo
├── /geovision-pro-showcase/                    ← Live demo
├── /nefertiti-viewer/                          ← Live demo
├── /sponza-viewer/                             ← Live demo
├── /royal-biryani/                             ← Live demo
```

## 2. Category Architecture (9 primary technology categories)

| # | Category | Key | Live Demos |
|---|----------|-----|------------|
| 1 | Agentic AI & Autonomous Workflows | agentic-ai | 0 (planned only) |
| 2 | Physical AI & Engineering | physical-ai | 2 (seaplane-outpost, vlm-aerodynamics) |
| 3 | Digital Twins & Spatial Intelligence | digital-twins | 8 (open-london, nexustwin, factory-bim, car-concept, metro, stadium, nefertiti, sponza) |
| 4 | GeoAI & Earth Intelligence | geoai | 2 (guntur-change, 3d-gis-globe) |
| 5 | Computer Vision & Visual Intelligence | computer-vision | 1 (geovision-pro) |
| 6 | Industrial AI & Predictive Operations | industrial-ai | 0 (planned only) |
| 7 | Defence & Aerospace | defence | 0 (planned only) |
| 8 | Climate, Environment & Sustainability | climate | 1 (circato) |
| 9 | Enterprise Applications & Decision Intelligence | enterprise | 3 (royal-biryani, salesflow-crm-showcase, salesflow-crm-deploy) |

## 3. Industry Cross-Reference (10 industry sectors)

| # | Industry | Related Demos |
|---|----------|--------------|
| 1 | Defence & Aerospace | seaplane-outpost, vlm-aerodynamics |
| 2 | Geospatial & Smart Cities | open-london-3d, guntur-change, 3d-gis-globe, geovision-pro |
| 3 | Manufacturing | nexustwin, factory-bim, car-concept |
| 4 | Climate & Environment | circato, guntur-change |
| 5 | Transportation | open-london-3d, car-concept, metro-station, seaplane-outpost, vlm-aero |
| 6 | Energy & Utilities | nexustwin |
| 7 | Construction & Infrastructure | factory-bim, metro-station, stadium, sponza |
| 8 | Government | guntur-change, 3d-gis-globe, geovision-pro, nefertiti |
| 9 | Enterprise | royal-biryani, stadium, nefertiti, sponza, salesflow-crm |
| 10 | Marine & Circular Economy | circato |

## 4. Technology Filters (9 capability dimensions)

| # | Technology | Demos Matching |
|---|-----------|---------------|
| 1 | Agentic AI | — |
| 2 | Physical AI | seaplane-outpost, vlm-aerodynamics |
| 3 | Digital Twins | open-london-3d, nexustwin, factory-bim, metro, stadium |
| 4 | Computer Vision | geovision-pro, guntur-change |
| 5 | GeoAI | guntur-change, 3d-gis-globe, circato |
| 6 | Simulation | metro-station, stadium, seaplane-outpost, vlm-aero |
| 7 | Multimodal AI | — |
| 8 | Document Intelligence | salesflow-crm |
| 9 | IoT & Edge AI | nexustwin, stadium |

## 5. Project Detail Page Schema

Each `/demo/{repo-name}/` page serves:

```
┌─────────────────────────────────────┐
│ ← Back to Catalogue                  │
├─────────────────────────────────────┤
│ Project Name + Maturity Badge        │
│ Primary Category | Industry Tags     │
│ ┌─────────────────────────────────┐ │
│ │ Screenshot / Live Preview Frame │ │
│ └─────────────────────────────────┘ │
│ Description                          │
│ Capability Tags (pill row)           │
│ Technology Stack                     │
│ ┌─────────────────────────────────┐ │
│ │ Quick Links:                    │ │
│ │ [Live Demo] [GitHub Repo]       │ │
│ └─────────────────────────────────┘ │
│ Data Provenance                      │
│ Related Demos                        │
└─────────────────────────────────────┘
```

## 6. Data Architecture

Single machine-readable catalogue file drives all views:

**`catalogue.json`** — Source of truth
- All 18 verified demos (no planned/placeholder entries)
- Keyed by repo_name
- Fields: name, repo_url, pages_url, description, primary_category, industry[], tags[], technology_stack[], maturity, screenshots[], related_demos[]

**No database required** — static JSON, served from GitHub Pages CDN.

## 7. Navigation Patterns

Four discovery paths:
1. **Category cards** (homepage grid) → filtered view
2. **Technology chips** → filtered view
3. **Industry chips** → filtered view
4. **Search** → instant filter across name, description, tags

Plus direct access:
5. **URL parameters** (`?category=digital-twins`) → shareable filtered views
6. **Project detail** (`/demo/open-london-3d-showcase/`) → dedicated page per demo
