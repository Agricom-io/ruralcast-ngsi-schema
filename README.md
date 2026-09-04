# ruralcast-ngsi-schema

NGSI-LD–compatible data models for **RURALCAST** — community-governed demand-and-price
market intelligence for rural regions (SMART ERA 2nd Open Call, Followers Micro-Pilot;
Goričko, Slovenia).

This repository holds the draft entity types RURALCAST uses to expose forecasts and
non-personal aggregate indicators for mapping with the SMART ERA Data Platform and
Dashboard. Exact field mapping is agreed with the SMART ERA technical partners at
On-boarding (M1–M2); the schema is published in final form at M12.

## Entity types (draft v0.1)

| Entity | File | Purpose |
|---|---|---|
| `PriceObservation` | `schema/PriceObservation.json` | One observed market price for a product/market/date, with source, source date and true source frequency |
| `MarketForecast` | `schema/MarketForecast.json` | One forecast for a product/horizon, with calibrated interval (lower/upper), method version and provenance reference |
| `ForecastBulletin` | `schema/ForecastBulletin.json` | One published weekly bulletin: the set of signals it carried, each with source date and refresh status |

Design rules (fixed for RURALCAST): every published signal carries its **true source
frequency and source date** — frequency is never upgraded by interpolation; forecasts
carry **calibrated intervals**, not just point values; only **non-personal aggregate**
outputs are exposed.

## Validation

```
pip install jsonschema
python -m pytest tests/
```

`examples/sample_output.json` validates against the draft schemas and shows the shape of
a bulletin payload.

## Licence and governance

Code and schemas: **Apache 2.0** (see `LICENSE`). Documentation: **CC BY 4.0**.
Maintainer: Jonas Westphal (Agricom). Deputy: Maria Abdallah (Agricom).

Part of the RURALCAST open-source track: `ruralcast-market-adapters`,
`ruralcast-opendata-export`, `ruralcast-handover` (M5); `ruralcast-ngsi-schema`,
`ruralcast-bulletin`, `ruralcast-eval` (M12).

*This work is planned under the SMART ERA project's 2nd Open Call. SMART ERA has
received funding from the European Union's Horizon Europe research and innovation
programme.*
