import json
import os
import yaml


def parsing_file(data, format_name):
    if format_name == 'yaml' or format_name == 'yml':
        return yaml.safe_load(data)
    if format_name == 'json':
        return json.load(data)
    else:
        raise Exception('Invalid file format name!')


def get_data_from_file(path):
    format_name = os.path.splitext(path)[1][1:]
    with open(path, 'r') as data:
        return parsing_file(data, format_name)
