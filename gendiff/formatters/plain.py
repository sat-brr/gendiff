def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    else:
        return f"'{value}'"


def build_update(old, new):
    if isinstance(old, dict) and type(new) != dict:
        return f". From [complex value] to {format_value(new)}\n"
    if isinstance(new, dict) and type(old) != dict:
        return f". From {format_value(old)} to [complex value]\n"
    if isinstance(old, dict) and isinstance(new, dict):
        return ". From [complex value] to [complex value]\n"
    if not isinstance(old, dict) and not isinstance(new, dict):
        return f". From {format_value(old)} to {format_value(new)}\n"


def build_by_status(status, key, value, level):
    result = ''
    if status != 'unchanged':
        result += f"Property '{level}{key}' was {status}"
    if status == 'added':
        if isinstance(value, dict):
            result += " with value: [complex value]\n"
        else:
            result += f" with value: {format_value(value)}\n"
    if status == 'removed':
        result += '\n'
    if status == 'updated':
        old, new = value[0], value[1]
        result += build_update(old, new)
    return result


def walk_on_diff(diff, level=''):
    result = ''
    for key, item in tuple(sorted(diff.items())):
        status = item[0]
        values = item[1:]
        value = values[0]
        if status == 'nested':
            result += walk_on_diff(value, level=level + key + '.')
        else:
            result += build_by_status(status, key, value, level)
    return result


def to_plain(diff):
    result = walk_on_diff(diff)
    return result.rstrip()
