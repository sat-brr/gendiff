import json


def to_json(diff):
    return json.dumps(diff, sort_keys=True, indent=4)
