# Ústí nad Labem – neevidované drobné památky a válečné hroby (ÚAP, ORP Ústí nad Labem)

| Field | Value |
|---|---|
| publisher | Statutární město Ústí nad Labem, Magistrát (ArcGIS Online organisation "Statutární město Ústí nad Labem", owner `gismmu`); item https://www.arcgis.com/home/item.html?id=06f0e5413ccd4389b53955229aa5692f |
| url | https://services5.arcgis.com/UoXZ3ybZw6nsLfcp/arcgis/rest/services/Válečné_hroby_a_drobné_neevidované_památky/FeatureServer (layer 0 Válečné hroby, layer 1 Neevidované drobné památky) |
| format | ArcGIS FeatureServer (JSON/GeoJSON, `outSR=4326` works) |
| coords | yes (GPS survey, points) |
| records | 177 unregistered small monuments (KAT: kříž 106, kaple 34, pomník 16, ostatní 10, kostel 6, socha 4, objekt 1) + 92 war graves / memorial sites (pietní místo – objekt 57, válečný hrob s ostatky 22, pietní místo – deska 13) |
| osm_tags | historic=wayside_cross; historic=wayside_shrine (výklenková kaple, boží muka); historic=memorial + memorial=war_memorial / plaque / stone; amenity=place_of_worship + building=chapel for walk-in chapels (wiki Tag:historic=wayside_cross, Tag:historic=wayside_shrine, Tag:historic=memorial, Key:memorial) |
| osm_count_cz | historic=wayside_cross 34,885; historic=memorial 30,273; historic=wayside_shrine 9,375; memorial=war_memorial 2,899 (taginfo CZ 2026-09-28) |
| license | CC BY-SA 4.0 |
| license_url | https://creativecommons.org/licenses/by-sa/4.0/legalcode.cs |
| license_status | needs_waiver |
| update_freq | one-off survey for ÚAP (PASPORT_ID 2017/2018, war graves 2014); item republished 2026-08 |
| impact | 1 |
| verified | yes |

## Try it
- **Map preview:** [samples/usti-drobne-pamatky.geojson](../samples/usti-drobne-pamatky.geojson): all 269 points (both layers) with category, name, description, cadastral area and an `osm_nearest` field (distance class to the nearest OSM historic/artwork/place_of_worship object).
- **QGIS:** *Layer → Add Layer → Add ArcGIS REST Server Layer → New*, URL `https://services5.arcgis.com/UoXZ3ybZw6nsLfcp/arcgis/rest/services/Válečné_hroby_a_drobné_neevidované_památky/FeatureServer`, connect, add layer 1 (*Neevidované drobné památky B*) and layer 0 (*Válečné hroby B*). Or *Add Vector Layer* with the URL `…/FeatureServer/1/query?where=1=1&outFields=*&outSR=4326&f=geojson`.

## Notes
- **Found by:** ArcGIS Online anonymous search sweep (see `research/platform-sweeps.md`), `licenseinfo:"CC BY"` in the CZ bbox.
- **What it is:** a field inventory of small monuments that are *not* in the heritage register (ÚSKP), surveyed with GPS by one surveyor (MERENI_PROVEDL) in 2017–2018 for the ÚAP of ORP Ústí nad Labem (jev A119 "další dostupné informace"). Covers 18 municipalities (Ústí nad Labem 53, Chlumec 17, Petrovice 11, Povrly 10, Libouchec 10 …). Each point has category, name, short description (with dating for chapels) and the parcel number. It is not in NPÚ data, so it complements `candidates/npu-uskp-pamatky.md`.
- **Gap (local match against the 2026-09-27 Czechia extract, any historic=*, tourism=artwork, amenity=place_of_worship, man_made=cross within 75 m):** small monuments: 138 of 177 have an OSM object within 30 m, 11 within 30–75 m, **28 have nothing within 75 m**: 13 crosses/torsos, 13 chapels, 1 boží muka, 1 monument torso. The extract does not contain `building=chapel` without other tags, so some of the 13 chapels may already exist as plain buildings. War graves: 77 of 92 within 30 m, 8 with nothing within 75 m. Nearest matches are mostly historic=wayside_cross (99) and historic=memorial (70), so OSM mapping here is already good.
- **Value for OSM:** a few dozen missing crosses/chapels plus names and construction years ("kaple z r. 1812" in Krásný Les) for existing objects. Low impact; worth it only as a local task, or bundled with other ÚAP "drobné památky" layers if more cities publish them.
- Suggested ref: none stable (OBJECTID only; PASPORT_ID is a survey batch id). Match by position.
- **Licence:** CC BY-SA 4.0 on the item → needs a written consent from Magistrát města Ústí nad Labem (odbor územního plánování / GIS, account `gismmu`).
- The war-grave layer likely overlaps the war-graves data covered by `candidates/known-valecne-hroby-kraje.md`.

## Wiki entry
```
===Ústí nad Labem – neevidované drobné památky===
* dataset: Válečné hroby a drobné neevidované památky v ORP Ústí nad Labem
* gestor: [https://www.arcgis.com/home/item.html?id=06f0e5413ccd4389b53955229aa5692f Statutární město Ústí nad Labem]
* licence: CC BY-SA 4.0 [https://creativecommons.org/licenses/by-sa/4.0/legalcode.cs]
* datové primitivy: body
* odkaz: https://services5.arcgis.com/UoXZ3ybZw6nsLfcp/arcgis/rest/services/Válečné_hroby_a_drobné_neevidované_památky/FeatureServer
* navržený tag {{tag|historic|wayside_cross}}, {{tag|historic|wayside_shrine}}, {{tag|historic|memorial}}
* poznámka: 177 neevidovaných křížů, kaplí a pomníků z terénního průzkumu 2017–2018; 28 z nich v OSM do 75 m nic nemá; nutný souhlas (CC BY-SA)
```
