# Attribution and Evidence Provenance

The project is an **independent engineering research demonstration**, not a delivered customer project, a finished standards-certified tool, or an endorsement by any manufacturer.

## Primary manufacturer and standard references

- Trinity Touch, [16 In 1 Out Combiner Box](https://www.trinitytouch.co.uk/backup/solution/16-in-1-out-combiner-box/) — 16 strings, 1000 V DC, 26 A maximum monitoring-channel current, 400 A maximum disconnector rating and exterior dimensions 1210 × 748 × 250 mm including mounting clamp. These published specifications do **not** constitute an actual populated BOM.
- ETI, [Photovoltaic CH gPV 20 A 1000 V fuse family](https://www.fuse.etigroup.eu/products-and-solutions/fuse-links-d-d0-c/photovoltaic-fuse-links-ch-gpv) — 1.3 W at 0.7 × 20A (14 A), 3.2 W at 20 A; interpolation is used only within 14–20 A in private calculations. These are **candidate third-party parts**, not the manufacturer's declared installed fuses.
- Trinity Touch, [DC SCB TRICHECK 16 Input](https://www.trinitytouch.com/solution/dc-scb-tricheck-16-input/) — a different product variant with monitoring electronics consuming **less than 3 W**; used only as an explicitly labeled illustrative allowance, not evidence of a BOM item fitted in the selected product.
- [IEC TR 60890:2022 official publication page](https://webstore.iec.ch/en/publication/66007) — descriptive scope only; no paid standard text or algorithms reproduced.

- Socomec, [60PV0020 20A gPV](https://emea.socomec.com/en/reference/60pv0020) — nominal 20A fuse power loss 3.2 W.
- Legrand, [414630 20A/1000V gPV](https://www.legrand.co.ug/en/catalog/products/cartridge-fuse-for-photovoltaic-application-1000v-20a-414630) — nominal 20A fuse power loss 1.09 W; manufacturer operating/setting temperature range -25 to 40°C. A possible thermal benefit is NOT an approval to substitute parts.

## Open-source research references (no copied implementation)

- [FreeCAD PanelWB](https://github.com/QuakeString/FreeCAD-PanelWB), LGPL-2.1-or-later: electrical cabinet CAD, BOM and preliminary thermal workflow. The repository's roadmap identifies a full IEC 60890 curve method as future work.
- [ThermalPath](https://github.com/flash631/thermalpath), MIT: thermal-resistance/network solver research reference.

The public presentation contains only original text, HTML/CSS and **precomputed displayed output values** from an internal calculation engine. It includes no proprietary calculation engine, APIs, runtime architecture, internal prompts, customer datasets, licensed libraries, or deployment configuration.

**Operating scenarios are author-defined, not customer supplied:** 14–20 A/string, two fused polarities, copper conductor lengths/sizes, 40°C ambient and 55°C illustrative limit. No claim of certified temperature rise, compliance or enclosure rating.
