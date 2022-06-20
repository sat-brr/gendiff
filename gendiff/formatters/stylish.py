def to_str(value, indent):
    result = ''
    indent += '    '
    if isinstance(value, dict):
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}  {k}: {to_str(v, indent)}\n'
        result += f'{indent[:-2]}}}'
    elif isinstance(value, int):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value
    return result


def build_by_status(status, key, value, indent):
    if status == 'unchanged':
        return f'{indent}  {key}: {to_str(value, indent)}\n'
    if status == 'added':
        return f'{indent}+ {key}: {to_str(value, indent)}\n'
    if status == 'removed':
        return f'{indent}- {key}: {to_str(value, indent)}\n'
    if status == 'updated':
        result = ''
        old, new = value[0], value[1]
        result += f'{indent}- {key}: {to_str(old, indent)}\n'
        result += f'{indent}+ {key}: {to_str(new, indent)}\n'
        return result


def walk_on_diff(diff, level=0):
    level_indent = '    ' * level
    indent = '  ' + level_indent
    result = '{\n'
    for key, item in tuple(sorted(diff.items())):
        status = item[0]
        values = item[1:]
        value = values[0]
        if status == 'nested':
            result += f'{indent}  {key}: '
            result += walk_on_diff(value, level + 1)
        else:
            result += build_by_status(status, key, value, indent)
    result += f'{indent[:-2]}}}\n'
    return result


def to_stylish(diff):
    result = walk_on_diff(diff)
    return result.rstrip()
