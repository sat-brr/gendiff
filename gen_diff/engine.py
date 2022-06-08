import json
import os
import yaml
from gen_diff.formatter.f_stylish import to_stylish
from gen_diff.formatter.plain import to_plain
from gen_diff.formatter.f_json import to_json


UPDATE, ADD, REMOVE = 'updated', 'added', 'removed'
COMMON, NESTED = 'common', 'nested'


def open_file(path):
    type_file = os.path.splitext(path)
    if type_file[1] == '.yaml' or type_file[1] == '.yml':
        file = yaml.safe_load(open(path))
        return file
    elif type_file[1] == '.json':
        file = json.load(open(path))
        return file


def get_diff(file1, file2):
    common = file1.keys() & file2.keys()
    before = file1.keys() - file2.keys()
    after = file2.keys() - file1.keys()
    result = {}
    for k in common:
        value1 = (file1[k])
        value2 = (file2[k])
        if value1 == value2:
            result[k] = (COMMON, value1)
        else:
            if type(value1) == dict and type(value2) == dict:
                result[k] = (NESTED, get_diff(value1, value2))
            else:
                result[k] = (UPDATE, (value1, value2))
    for k in before:
        result[k] = (REMOVE, (file1[k]))
    for k in after:
        result[k] = (ADD, (file2[k]))
    return result


def generate_diff(path1, path2, format='stylish'):
    file1 = open_file(path1)
    file2 = open_file(path2)
    diff = get_diff(file1, file2)
    if format == 'stylish':
        return to_stylish(diff)
    elif format == 'plain':
        return to_plain(diff)
    elif format == 'json':
        return to_json(diff)
