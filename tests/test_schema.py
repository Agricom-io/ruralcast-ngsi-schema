"""Validate the draft schemas and the sample payload against them."""
import json, pathlib
import jsonschema

ROOT = pathlib.Path(__file__).resolve().parents[1]

def load(p): return json.loads((ROOT / p).read_text())

def test_schemas_are_valid_jsonschema():
    for name in ["PriceObservation", "MarketForecast", "ForecastBulletin"]:
        schema = load(f"schema/{name}.json")
        jsonschema.Draft202012Validator.check_schema(schema)

def test_sample_output_validates():
    sample = load("examples/sample_output.json")
    jsonschema.validate(sample["observation"], load("schema/PriceObservation.json"))
    jsonschema.validate(sample["forecast"], load("schema/MarketForecast.json"))
    jsonschema.validate(sample["bulletin"], load("schema/ForecastBulletin.json"))

def test_provenance_links_resolve_within_sample():
    sample = load("examples/sample_output.json")
    assert sample["forecast"]["sourceRefs"][0] == sample["observation"]["id"]
    assert sample["bulletin"]["signals"][0]["forecastRef"] == sample["forecast"]["id"]
