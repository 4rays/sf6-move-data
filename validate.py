#!/usr/bin/env python3

import json
import os
import jsonschema


def validate_json(json_data):
    """Validate JSON data against schema"""
    # Load schema
    schema_path = os.path.join(os.path.dirname(__file__), "schema.json")
    with open(schema_path) as schema_file:
        schema = json.load(schema_file)

    # Validate json data
    try:
        jsonschema.validate(json_data, schema)
    except jsonschema.exceptions.ValidationError as err:
        print("❗ Validation error: {} on instance {}".format(err.message, err.instance))
        return False
    return True


# Load all character moves
moves_path = os.path.join(os.path.dirname(__file__), "moves")

for filename in os.listdir(moves_path):
    if filename.endswith(".json"):
        with open(os.path.join(moves_path, filename)) as move_file:
            move = json.load(move_file)
            print("Validating {}...".format(filename))
            if not validate_json(move):
                exit(1)
            else:
                print("✅ Validated {}".format(filename))
