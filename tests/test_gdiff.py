import pytest
import os
from gendiff.diff_generator import generate_diff

TEST_PATH = os.path.dirname('/home/sat/python-project-lvl2/tests/test_gdiff.py')
FIXTURE_PATH = f'{TEST_PATH}/fixtures'
RESULT_STYLISH = f'{FIXTURE_PATH}/complete_stylish.txt'
RESULT_PLAIN = f'{FIXTURE_PATH}/complete_plain.txt'
RESULT_JSON = f'{FIXTURE_PATH}/complete_json.txt'
TEMP_FIXTURE = f'{FIXTURE_PATH}/temp.txt'


@pytest.mark.parametrize('file1, file2, path, format',
                         [('file5.json', 'file6.json', FIXTURE_PATH, 'stylish'),
                          ('file5.yaml', 'file6.yaml', FIXTURE_PATH, 'plain'),
                          ('file5.json', 'file6.yaml', FIXTURE_PATH, 'json')])
def test_generate_diff(file1, file2, path, format):
    path_file1 = f'{path}/{file1}'
    path_file2 = f'{path}/{file2}'
    with open(TEMP_FIXTURE, 'w') as temp_file:
        gd = generate_diff(path_file1, path_file2, format)
        temp_file.write(gd)
    load_temp = open(TEMP_FIXTURE, 'r')
    res = load_temp.read()
    if format == 'stylish':
        with open(RESULT_STYLISH) as file:
            result_stylish = file.read()
        assert res == result_stylish
    elif format == 'plain':
        with open(RESULT_PLAIN) as file:
            result_plain = file.read()
        assert res == result_plain
    elif format == 'json':
        with open(RESULT_JSON) as file:
            result_json = file.read()
        assert res == result_json
