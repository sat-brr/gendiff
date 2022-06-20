import json
import os
import yaml


def parsing_file(file, file_type):
    if file_type == '.yaml' or file_type == '.yml':
        return yaml.safe_load(file)
    if file_type == '.json':
        return json.load(file)


def load_file(path):
    file_type = os.path.splitext(path)[1]
    with open(path, 'r') as file:
        content = parsing_file(file, file_type)
    return content
