from gendiff.file_parser import get_data_from_file
from gendiff.formatter import format_diff


UPDATE, ADD, REMOVE = 'updated', 'added', 'removed'
UNCHANGED, NESTED = 'unchanged', 'nested'


def build_diff(data1, data2):
    unchanged_keys = data1.keys() & data2.keys()
    removed_keys = data1.keys() - data2.keys()
    added_keys = data2.keys() - data1.keys()
    result = {}
    for current_key in unchanged_keys:
        value1 = (data1[current_key])
        value2 = (data2[current_key])
        if value1 == value2:
            result[current_key] = (UNCHANGED, value1)
        else:
            if type(value1) == dict and type(value2) == dict:
                result[current_key] = (NESTED, build_diff(value1, value2))
            else:
                result[current_key] = (UPDATE, (value1, value2))
    for current_key in removed_keys:
        result[current_key] = (REMOVE, (data1[current_key]))
    for current_key in added_keys:
        result[current_key] = (ADD, (data2[current_key]))
    return result


def generate_diff(path1, path2, format='stylish'):
    data1 = get_data_from_file(path1)
    data2 = get_data_from_file(path2)
    diff = build_diff(data1, data2)
    return format_diff(diff, format)
