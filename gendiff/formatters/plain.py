def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f"'{value}'"


def build_line_by_status(status, key, value, path):
    result = ''
    if status == 'unchanged':
        return result
    result += f"Property '{path}{key}' was {status}"
    if status == 'added':
        result += f" with value: {to_str(value)}\n"
        return result
    if status == 'removed':
        result += '\n'
        return result
    if status == 'updated':
        old, new = value
        result += f". From {to_str(old)} to {to_str(new)}\n"
        return result
    else:
        raise Exception('Invalid status!')


def walk(diff, path=''):
    result = ''
    for key, item in tuple(sorted(diff.items())):
        status, value = item
        if status == 'nested':
            result += walk(value, path=path + key + '.')
        else:
            result += build_line_by_status(status, key, value, path)
    return result


def to_plain(diff):
    result = walk(diff)
    return result.rstrip()
