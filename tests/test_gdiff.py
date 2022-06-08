import pytest
import os
from gen_diff.engine import generate_diff


PATH = './tests/fixtures/'
RESULT_STYLISH = os.path.join(PATH, 'complete_stylish.txt')
RESULT_PLAIN = os.path.join(PATH, 'complete_plain.txt')
RESULT_JSON = os.path.join(PATH, 'complete_json.txt')

TEMP_JSON = os.path.join(PATH, 'temp_json.txt')
TEMP_YAML = os.path.join(PATH, 'temp_yaml.txt')


file1_json, file2_json = (os.path.join(PATH, 'file5.json'), 
             os.path.join(PATH, 'file6.json'))
file1_yaml, file2_yaml = (os.path.join(PATH, 'file5.yaml'), 
             os.path.join(PATH, 'file6.yaml'))


def test_generate_diff_stylish():
    with open(RESULT_STYLISH) as file:
        result = file.read()
    with open(TEMP_JSON, 'w') as t_j:
        gd_j = generate_diff(file1_json, file2_json)
        t_j.write(gd_j)
    with open(TEMP_YAML, 'w') as t_y:
        gd_y = generate_diff(file1_yaml,file2_yaml)
        t_y.write(gd_y)
    j = open(TEMP_JSON, 'r')
    s_j = j.read()
    y = open(TEMP_YAML, 'r')
    s_y = y.read()
    assert s_j == result
    assert s_y == result


def test_generate_diff_plain():
    with open(RESULT_PLAIN) as file:
        result = file.read()
    with open(TEMP_JSON, 'w') as t_j:
        gd_j = generate_diff(file1_json, file2_json, 'plain')
        t_j.write(gd_j)
    with open(TEMP_YAML, 'w') as t_y:
        gd_y = generate_diff(file1_yaml,file2_yaml, 'plain')
        t_y.write(gd_y)
    j = open(TEMP_JSON, 'r')
    s_j = j.read()
    y = open(TEMP_YAML, 'r')
    s_y = y.read()
    assert s_j == result
    assert s_y == result


def test_generate_diff_json():
    with open(RESULT_JSON) as file:
        result = file.read()
    with open(TEMP_JSON, 'w') as t_j:
        gd_j = generate_diff(file1_json, file2_json, 'json')
        t_j.write(gd_j)
    with open(TEMP_YAML, 'w') as t_y:
        gd_y = generate_diff(file1_yaml,file2_yaml, 'json')
        t_y.write(gd_y)
    j = open(TEMP_JSON, 'r')
    s_j = j.read()
    y = open(TEMP_YAML, 'r')
    s_y = y.read()
    assert s_j == result
    assert s_y == result

    
    
test_generate_diff_json()