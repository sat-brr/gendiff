from gendiff.formatter.stylish import to_stylish
from gendiff.formatter.plain import to_plain
from gendiff.formatter.json import to_json


def del_last_char(source):
    res = source.rstrip()
    return res


def rendering(diff, format):
    if format == 'stylish':
        res = to_stylish(diff)
        return del_last_char(res)
    elif format == 'plain':
        res = to_plain(diff)
        return del_last_char(res)
    elif format == 'json':
        return to_json(diff)
