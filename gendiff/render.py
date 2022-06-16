from gendiff.formatters.stylish import to_stylish
from gendiff.formatters.plain import to_plain
from gendiff.formatters.json import to_json


def rendering(diff, format):
    if format == 'stylish':
        return to_stylish(diff)
    elif format == 'plain':
        return to_plain(diff)
    elif format == 'json':
        return to_json(diff)
