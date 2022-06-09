import json
import os
import yaml


def get_dict(path):
    file_type = os.path.splitext(path)[1]
    return parsing_file(path, file_type)


def parsing_file(path, file_type):
    if file_type == '.yaml' or file_type == '.yml':
        pars = yaml.safe_load(open(path))
        return pars
    elif file_type == '.json':
        pars = json.load(open(path))
        return pars
