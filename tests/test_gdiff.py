import pytest
import os
from gendiff.generate_diff import generate_diff


PATH = './tests/fixtures/'
RESULT_STYLISH = os.path.join(PATH, 'complete_stylish.txt')
RESULT_PLAIN = os.path.join(PATH, 'complete_plain.txt')
RESULT_JSON = os.path.join(PATH, 'complete_json.txt')
TEMP = os.path.join(PATH, 'temp.txt')


file1_json, file2_json = (os.path.join(PATH, 'file5.json'), 
             os.path.join(PATH, 'file6.json'))
file1_yaml, file2_yaml = (os.path.join(PATH, 'file5.yaml'), 
             os.path.join(PATH, 'file6.yaml'))


@pytest.mark.parametrize('path1', [file1_json, file1_yaml])
@pytest.mark.parametrize('path2', [file2_json, file2_yaml])
@pytest.mark.parametrize('format', ['json', 'plain', 'stylish'])
def test_generate_diff(path1, path2, format):
    with open(TEMP, 'w') as temp_file:
        gd = generate_diff(path1, path2, format)
        temp_file.write(gd)
    load_temp = open(TEMP, 'r')
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
