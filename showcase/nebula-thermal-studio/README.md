# Solar DC Combiner Thermal Engineering — Real Reference Use Case

> **Notice**  
> This repository is a public project showcase created using NebulaCloud Studio.  
> The proprietary source code, implementation details, prompts, workflows, datasets, infrastructure, and deployment configuration are intentionally not included.

## 1. Project Title
**Nebula Thermal Studio: Evidence-Led Solar String Combiner Thermal Engineering**

## 2. Overview
A **working private engineering application** studies a publicly documented 16-input / 1-output solar string combiner box and constructs a traceable, preliminary heat-loss assessment. The public website provides curated, precomputed engineering results and source citations—not the proprietary calculation engine.

## 3. Business Problem
Electrical engineering teams must quantify losses from PV fuse links, conductors, disconnects and auxiliary equipment, and evaluate enclosure heat rise subject to real manufacturer data and correct IEC methodologies. Attractive dashboards without evidence can mislead safety decisions.

## 4. Solution Overview
Our private application calculates what can reasonably be supported by published manufacturer fuse loss data and explicitly entered conductor geometry, while flagging rating conflicts and documenting missing thermal validation data.

## 5. Live Demo
[**Explore the published case study and five precomputed operating scenarios**](https://studio-public-demos.github.io/showcase/nebula-thermal-studio/). The public interface is a **results explorer**, not an interactive publicly hosted engineering engine. Private real-time demo by request.

## 6. Demo Video
A private application walkthrough can be provided during a product demonstration. No public video is claimed or linked here.

## 7. Project Screenshots
The published engineering case includes an original **conceptual circuit visualization** and interactive presentation of precomputed real calculation outputs. Authentic private-app screenshots remain in the internal delivery package and are not misrepresented as a public screenshot.

## 8. Generated Outputs
At an **assumed 15 A/string**, the real-source case produces **240 A combined input**, **51.733 W fuse loss**, **9.577 W branch copper**, **13.306 W output copper**, and **3.0 W monitoring allowance**, totaling **77.616 W of modeled but incomplete heat-loss contributions**. For **20 A/string**, the same assumptions yield **146.081 W incomplete modeled subtotal**. Real application can produce a PDF report listing assumptions and missing evidence; report is available during private demo.

## 9. Key Features
Real product reference; manufacturer-linked fuse loss; conductor I²R; controllable voltage/current/branch geometry assumptions; what-if scenario comparisons; source/evidence classification; current/rating guards; blocked compliance gate; private PDF reporting.

## 10. Intended Users
Solar PV OEMs, combiner-box designers, electrical equipment manufacturers, EPC engineers, LV panel designers, product engineering and quality teams.

## 11. Example Use Cases
- Compare published 20 A / 1000 V gPV fuse power loss from ETI (3.2 W), Socomec (3.2 W), and Legrand (1.09 W): 67.52 W nominal difference for an assumed 32 links, without claiming electrical interchangeability.
- Compare partial heat contributions at 14, 15, 16, 18 and 20 A per string.
- Identify when 20 A example gPV fuses can no longer be modeled from available manufacturer data.
- Prepare the missing-evidence checklist for an IEC design review.
- Evaluate which cable cross-sections materially impact I²R losses before confirming actual installed configurations.

## 12. Technical Highlights (High-Level Only)
Deterministic private numerical computation, source-to-input traceability, documented scenario assumptions, source-linked component catalogue references, browser UX and PDF output.

## 13. Architecture Overview (Conceptual Only)
Public reference product + assumed engineering scenario → traceable loss estimate → missing-evidence review → private documented output.

## 14. Technical Scope & Limitations
The cited Trinity Touch product, its precise internal BOM and actual operating circuit are **not** claimed to be identical to this example scenario. ETI fuses are **third-party evaluation components**, not confirmed as installed. Copper dimensions, temperature, polarity count and ambient are assumptions; the TRICHECK <3 W allowance is published for **another product variant**. The public enclosure external size includes a mounting clamp and cannot be used to infer effective UA. Disconnect, joint, busbar, fuse-holder, SPD and auxiliary losses are incomplete. **No enclosure temperature is calculated without calibrated heat transfer properties; there is no IEC TR 60890/IEC 61439 compliance or thermal certification.**

## 15. Performance Summary (Verified Only)
Private implementation passed **23 unit/integration checks**, plus Chromium desktop/mobile interaction testing on representative cases. No scientific accuracy benchmark, IEC validation, OEM endorsement or production uptime claim.

## 16. Attribution
Additional sources: [Socomec 60PV0020](https://emea.socomec.com/en/reference/60pv0020) and [Legrand 414630](https://www.legrand.co.ug/en/catalog/products/cartridge-fuse-for-photovoltaic-application-1000v-20a-414630), manufacturer nominal 20A dissipation only.
[Trinity Touch 16 In 1 Out product reference](https://www.trinitytouch.co.uk/backup/solution/16-in-1-out-combiner-box/), [ETI CH10x38 gPV fuse data](https://www.fuse.etigroup.eu/products-and-solutions/fuse-links-d-d0-c/photovoltaic-fuse-links-ch-gpv), [Trinity Touch TRICHECK monitoring reference](https://www.trinitytouch.com/solution/dc-scb-tricheck-16-input/), [IEC TR 60890 scope](https://webstore.iec.ch/en/publication/66007). Research references: [FreeCAD PanelWB](https://github.com/QuakeString/FreeCAD-PanelWB) (LGPL-2.1+), [ThermalPath](https://github.com/flash631/thermalpath) (MIT). No third-party code or IEC protected text distributed.

## 17. Built with NebulaCloud Studio
Part of Nebula Cloud Studio's IP-protected specialist engineering case-study portfolio. Original proprietary implementations remain private.

## 18. Related Project Showcases
[Studio Public Demos](https://studio-public-demos.github.io/) · [Nebula Cloud Studio](https://nebulacloud.studio/).

## 19. Call to Action
[Request a private demonstration or discuss a manufacturer-specific engineering proof of concept](https://nebulacloud.studio/).

**Legal and engineering notice:** Independent public-reference case study. No actual customer project data, and no implied manufacturer endorsement. The public case explorer is deliberately presentation-only and does not expose numerical calculation algorithms.
