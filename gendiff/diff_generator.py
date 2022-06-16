from gendiff.file_loader import load_file
from gendiff.render import rendering


UPDATE, ADD, REMOVE = 'updated', 'added', 'removed'
UNCHANGED, NESTED = 'unchanged', 'nested'


def find_difference(dict1, dict2):
    unchanged_keys = dict1.keys() & dict2.keys()
    removed_keys = dict1.keys() - dict2.keys()
    added_keys = dict2.keys() - dict1.keys()
    result = {}
    for current_key in unchanged_keys:
        value1 = (dict1[current_key])
        value2 = (dict2[current_key])
        if value1 == value2:
            result[current_key] = (UNCHANGED, value1)
        else:
            if type(value1) == dict and type(value2) == dict:
                result[current_key] = (NESTED, find_difference(value1, value2))
            else:
                result[current_key] = (UPDATE, (value1, value2))
    for current_key in removed_keys:
        result[current_key] = (REMOVE, (dict1[current_key]))
    for current_key in added_keys:
        result[current_key] = (ADD, (dict2[current_key]))
    return result


def generate_diff(path1, path2, format='stylish'):
    dict_file1 = load_file(path1)
    dict_file2 = load_file(path2)
    diff = find_difference(dict_file1, dict_file2)
    return rendering(diff, format)
