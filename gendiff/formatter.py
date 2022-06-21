from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json


def format_diff(diff, format):
    if format == 'stylish':
        return to_stylish(diff)
    if format == 'plain':
        return to_plain(diff)
    if format == 'json':
        return to_json(diff)
    else:
        raise Exception('Incorrect formatting style!')
