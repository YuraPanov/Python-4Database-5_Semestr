import json
from jsonschema import validate

file = 'error.json.json'
schema = 'schema.json'
try:
    with open(file) as file_json, open(schema) as schema:
        validate(json.load(file_json), json.load(schema))
        print("Valid")
except:
    print("Invalid")
