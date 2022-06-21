import json
import os
import yaml


def parse(data, format_name):
    if format_name == 'yaml' or format_name == 'yml':
        return yaml.safe_load(data)
    if format_name == 'json':
        return json.load(data)
    raise Exception('Invalid file format name!')


def get_data_from_file(path):
    format_name = os.path.splitext(path)[1][1:]
    with open(path, 'r') as data:
        return parse(data, format_name)
