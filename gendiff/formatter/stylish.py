def to_str(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif type(value) == int:
        return str(value)
    else:
        return value


def get_value(value, indent):
    result = ''
    indent += '    '
    if isinstance(value, dict):
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}  {k}: {get_value(v, indent)}\n'
        result += f'{indent[:-2]}}}'
    else:
        result += to_str(value)
    return result

# flake8: noqa: C901
def to_stylish(source, level=0):
    level_indent = '    ' * level
    indent = '  ' + level_indent
    result = '{\n'
    for key, item in tuple(sorted(source.items())):
        flag = item[0]
        values = item[1:]
        value = values[0]
        if flag == 'unchanged':
            result += f'{indent}  {key}: {get_value(value, indent)}\n'
        elif flag == 'added':
            result += f'{indent}+ {key}: {get_value(value, indent)}\n'
        elif flag == 'removed':
            result += f'{indent}- {key}: {get_value(value, indent)}\n'
        elif flag == 'updated':
            old, new = value[0], value[1]
            result += f'{indent}- {key}: {get_value(old, indent)}\n'
            result += f'{indent}+ {key}: {get_value(new, indent)}\n'
        elif flag == 'nested':
            result += f'{indent}  {key}: '
            result += to_stylish(value, level + 1)
    result += f'{indent[:-2]}}}\n'
    return result
