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
    result = ''
    if isinstance(old, dict) and type(new) != dict:
        result += f". From [complex value] to {format_value(new)}\n"
    elif isinstance(new, dict) and type(old) != dict:
        result += f". From {format_value(old)} to [complex value]\n"
    elif isinstance(old, dict) and isinstance(new, dict):
        result += ". From [complex value] to [complex value]\n"
    elif not isinstance(old, dict) and not isinstance(new, dict):
        result += f". From {format_value(old)} to {format_value(new)}\n"
    return result


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


def build_str(source, level=''):
    result = ''
    for key, item in tuple(sorted(source.items())):
        status = item[0]
        values = item[1:]
        value = values[0]
        if status == 'nested':
            result += build_str(value, level=level + key + '.')
        else:
            result += build_by_status(status, key, value, level)
    return result


def to_plain(source):
    result = build_str(source)
    return result.rstrip()
