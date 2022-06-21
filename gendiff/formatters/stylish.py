TAB = '    '


def to_str(value, indent):
    if isinstance(value, int):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent += TAB
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}    {k}: {to_str(v, indent)}\n'
        result += f'{indent}}}'
        return result
    return value


def build_line_by_status(status, key, value, indent):
    if status == 'unchanged':
        return f'{indent}    {key}: {to_str(value, indent)}\n'
    if status == 'added':
        return f'{indent}  + {key}: {to_str(value, indent)}\n'
    if status == 'removed':
        return f'{indent}  - {key}: {to_str(value, indent)}\n'
    if status == 'updated':
        result = ''
        old, new = value
        result += f'{indent}  - {key}: {to_str(old, indent)}\n'
        result += f'{indent}  + {key}: {to_str(new, indent)}\n'
        return result
    raise Exception('Invalid status!')


def walk(diff, level=0):
    indent_level = TAB * level
    result = '{\n'
    for key, item in tuple(sorted(diff.items())):
        status, value = item
        if status == 'nested':
            result += f'{indent_level}    {key}: '
            result += walk(value, level + 1)
        else:
            result += build_line_by_status(status, key, value, indent_level)
    result += f'{indent_level}}}\n'
    return result


def to_stylish(diff):
    result = walk(diff)
    return result.rstrip()
