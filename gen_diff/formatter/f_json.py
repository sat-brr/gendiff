import json
from gen_diff.formatter.f_stylish import to_str


def to_list(source):
    result = []
    for key, item in (sorted(source.items())):
        new_dict = {}
        flag = item[0]
        values = item[1:]
        value = values[0]
        new_dict['name'] = key
        new_dict['status'] = flag
        if flag == 'nested':
            new_dict[flag] = to_list(value)
        elif flag == 'added':
            new_dict['value'] = to_str(value)
        elif flag == 'removed':
            new_dict['value'] = to_str(value)
        elif flag == 'updated':
            new_dict['old_value'] = to_str(value[0])
            new_dict['new_value'] = to_str(value[1])
        else:
            new_dict['value'] = to_str(value)
        result.append(new_dict)
    return result


def to_json(source):
    result = to_list(source)
    return json.dumps(result, indent=4)
