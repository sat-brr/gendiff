def to_str(value, indent):
    result = ''
    indent += '    '
    if isinstance(value, dict):
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}  {k}: {to_str(v, indent)}\n'
        result += f'{indent[:-2]}}}'
    elif isinstance(value, int):
        result += str(value).lower()
    elif value is None:
        result += 'null'
    else:
        result += value
    return result


def build_by_status(status, key, value, indent):
    result = ''
    if status == 'unchanged':
        result += f'{indent}  {key}: {to_str(value, indent)}\n'
    elif status == 'added':
        result += f'{indent}+ {key}: {to_str(value, indent)}\n'
    elif status == 'removed':
        result += f'{indent}- {key}: {to_str(value, indent)}\n'
    elif status == 'updated':
        old, new = value[0], value[1]
        result += f'{indent}- {key}: {to_str(old, indent)}\n'
        result += f'{indent}+ {key}: {to_str(new, indent)}\n'
    return result


def building_str(source, level=0):
    level_indent = '    ' * level
    indent = '  ' + level_indent
    result = '{\n'
    for key, item in tuple(sorted(source.items())):
        status = item[0]
        values = item[1:]
        value = values[0]
        if status == 'nested':
            result += f'{indent}  {key}: '
            result += building_str(value, level + 1)
        else:
            result += build_by_status(status, key, value, indent)
    result += f'{indent[:-2]}}}\n'
    return result


def to_stylish(source):
    result = building_str(source)
    return result.rstrip()
