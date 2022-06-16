import json


def sorted_dict(source):
    temp_dict = {}
    for key, item in (sorted(source.items())):
        new_dict = {}
        flag = item[0]
        values = item[1:]
        value = values[0]
        if flag == 'nested':
            new_dict[key] = (flag, sorted_dict(value))
        else:
            new_dict[key] = item
        temp_dict.update(new_dict)
    return temp_dict


def to_json(source):
    result = sorted_dict(source)
    return json.dumps(result, indent=4)
