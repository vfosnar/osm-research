# Open data for OpenStreetMap in Czechia

Which open datasets would help the Czech OpenStreetMap map the most — and aren't
already being imported?

This repository collects candidate data sources, each checked by hand: does the data
really exist, what licence it has, and how much of it is already in OSM.

> **Status:** first research round in progress (September 2026). The ranked shortlist
> below will be filled in when it finishes.

## Shortlist

_Coming soon._

## What's already covered

Everything already imported, in the [Sync](https://codeberg.org/osmcz/sync) tool, with a
granted permission, or under negotiation is listed in [`covered.md`](covered.md) — for
example the ZABAGED POI import, AllThePlaces brand spiders, Zásilkovna, post boxes and
RÚIAN addresses. These are deliberately left out.

## Reading a candidate

Each file in [`candidates/`](candidates/) describes one source:

- **Licence status**
  - ✅ **ok** — can be used in OSM (CC0, ODbL, or explicit permission)
  - ✍️ **needs waiver** — attribution licence such as CC BY 4.0; the publisher has to
    give OSM explicit consent first
  - ❌ **incompatible** — can't be used
  - ❓ **unclear** — no licence found; someone has to ask
- **Impact 1–5** — how much it would improve the map: how many features are missing in
  OSM and how useful they are.
- **OSM count** — how many such features OSM in Czechia has today.

For how the research is done, see [`AGENTS.md`](AGENTS.md).
