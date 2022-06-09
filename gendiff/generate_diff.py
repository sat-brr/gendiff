from gendiff.parsing_file import get_dict
from gendiff.formatter.rendering import rendering


UPDATE, ADD, REMOVE = 'updated', 'added', 'removed'
UNCHANGED, NESTED = 'unchanged', 'nested'


def get_diff(file1, file2):
    common = file1.keys() & file2.keys()
    before = file1.keys() - file2.keys()
    after = file2.keys() - file1.keys()
    result = {}
    for k in common:
        value1 = (file1[k])
        value2 = (file2[k])
        if value1 == value2:
            result[k] = (UNCHANGED, value1)
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
    dict_file1 = get_dict(path1)
    dict_file2 = get_dict(path2)
    diff = get_diff(dict_file1, dict_file2)
    return rendering(diff, format)
