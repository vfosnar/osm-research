# Služby pre ľudí bez domova v Bratislave (services for homeless people, Bratislava)

| Field | Value |
|---|---|
| publisher | Hlavné mesto SR Bratislava (IČO 00603481) |
| url | https://data.bratislava.sk/api/download/v1/items/5242099b24bc4bf68ea766ca55162a08/csv?layers=0 (catalogue dataset https://data.gov.sk/set/9afb671bc19a46116507584d06ba1a1d) |
| format | CSV (ArcGIS Hub), comma-separated, decimal comma in `Latitude`/`Longitude` |
| coords | yes |
| records | 36 (2026-02-19): services tagged strava 13, sociálne poradenstvo 12, kontaktné centrum pre užívateľov drog a ľudí zo sexbiznisu 9, nocľah a ubytovanie 7, hygiena a ošatenie 6+, zdravotné ošetrenie 6, kultúra 1, pouličný časopis 1 |
| osm_tags | amenity=social_facility + social_facility=shelter (nocľah) / soup_kitchen (strava) / outreach (poradenstvo, kontaktné centrum) + social_facility:for=homeless / drug_addicted; amenity=shower where hygiene is offered; healthcare=* for Equita-type clinics; opening_hours from the free-text fields |
| osm_count_sk | social_facility=* 450 in SK; in the sample 7 of 36 have a social facility within 50 m (Postpass, 2026-09-30) |
| license | CC BY 4.0 (catalogue database licence) |
| license_url | https://creativecommons.org/licenses/by/4.0/ |
| license_status | needs_waiver |
| update_freq | as needed (catalogue `AS_NEEDED`; last change 2026-02-19) |
| impact | 2 |
| sync_fit | MapRoulette — 36 points with 1:N tag choices (one address often offers meals, showers and counselling); too small and varied for Sync |
| verified | yes |

## Try it
- **Map preview:** [../samples/social-bratislava-homeless-services.geojson](../samples/social-bratislava-homeless-services.geojson): all 36 records with service columns and `osm_social_facility_within_50m` (7 true, 29 false).
- **QGIS:** *Layer → Add Layer → Add Delimited Text Layer*, file name = the CSV URL above, delimiter comma, X = `Longitude`, Y = `Latitude`, CRS EPSG:4326, and tick "Decimal separator is comma".
- **Web:** the city's app "Mapa služieb pre ľudí v núdzi": https://experience.arcgis.com/experience/d2a2d09777d74ca39be6212f9d559895 (named in the dataset description).

## Notes
- **Gap:** 29 of 36 places have no `social_facility` in OSM within 50 m (Postpass, 2026-09-30). These are the kind of POI that matter most to their users and that no national register covers: soup kitchens of Komunita Sant'Egidio, Kresťania v meste, DEPAUL and Domov pre každého shelters, Dom Betlehem, DOMEC day centre, Equita medical care, harm-reduction contact points of OZ Odyseus and OZ Prima.
- **Attributes:** provider, address, city district, public-transport directions (`Navigacia`), service-specific opening times in free text (`Strava` "pondelok 9:00 – 14:00", `Socialne_pravne_poradenstvo` …), phone, e-mail, web.
- **Caveats:** no stable ID beyond ArcGIS `ObjectId`; several "Kontaktné miesto" rows are street outreach points of harm-reduction NGOs (5 for Odyseus, 2 for Prima) — check with the NGO whether a public fixed location should be mapped at all. Some services run in rotation at different places (Sant'Egidio has 3 rows).
- **Relation to the national register:** registered social services among these (nocľahárne, nízkoprahové centrá) also appear in the MPSVR register ([social-services-register-mpsvr.md](social-services-register-mpsvr.md)); soup kitchens, clothing points, the street magazine and NGO medical care do not, which is what this dataset adds.
- **ZBGIS:** nothing comparable (only the building-use code "Sociálne zariadenie").
- **Contact:** Bratislava city open data team (data.bratislava.sk); the city's social department maintains the underlying map. Bratislava already publishes most of its data as CC BY 4.0, so one city-wide consent for OSM would cover this and other city datasets.

## Wiki entry
```
=== Služby pre ľudí bez domova v Bratislave ===
* dataset: Služby pre ľudí bez domova v Bratislave
* správca: [https://data.bratislava.sk/ Hlavné mesto SR Bratislava]
* licencia: CC BY 4.0 [https://creativecommons.org/licenses/by/4.0/]
* dátové primitívy: body
* odkaz: https://data.bratislava.sk/api/download/v1/items/5242099b24bc4bf68ea766ca55162a08/csv?layers=0
* navrhované značky: {{tag|amenity|social_facility}}, {{tag|social_facility|soup_kitchen}}, {{tag|social_facility|shelter}}, {{tag|social_facility|outreach}}, {{tag|social_facility:for|homeless}}
* poznámka: 36 miest (výdaj stravy, nocľahárne, hygiena, zdravotné ošetrenie, kontaktné centrá); 29 z nich nemá v OSM sociálne zariadenie do 50 m.
```
