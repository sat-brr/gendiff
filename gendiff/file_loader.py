import json
import os
import yaml


def parsing_file(path, parse):
    with open(path, 'r') as file:
        content = parse(file)
    return content


def load_file(path):
    file_type = os.path.splitext(path)[1]
    if file_type == '.yaml' or file_type == '.yml':
        parse = yaml.safe_load
    elif file_type == '.json':
        parse = json.load
    return parsing_file(path, parse)
