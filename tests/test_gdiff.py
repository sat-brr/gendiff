import pytest
from gendiff.diff_generator import generate_diff

TEST_PATH = './tests'
FIXTURE_PATH = f'{TEST_PATH}/fixtures'
RESULT_STYLISH = f'{FIXTURE_PATH}/complete_stylish.txt'
RESULT_PLAIN = f'{FIXTURE_PATH}/complete_plain.txt'
RESULT_JSON = f'{FIXTURE_PATH}/complete_json.txt'
TEMP_FIXTURE = f'{FIXTURE_PATH}/temp_file.txt'


@pytest.mark.parametrize('file1, file2, res_path, format',
                         [('file5.json', 'file6.json', RESULT_STYLISH, 'stylish'),
                          ('file5.yaml', 'file6.yaml', RESULT_PLAIN, 'plain'),
                          ('file5.json', 'file6.yaml', RESULT_JSON, 'json')])
def test_generate_diff(file1, file2, res_path, format):
    path_file1 = f'{FIXTURE_PATH}/{file1}'
    path_file2 = f'{FIXTURE_PATH}/{file2}'
    with open(TEMP_FIXTURE, 'w') as temp_file:
        gd = generate_diff(path_file1, path_file2, format)
        temp_file.write(gd)
    load_temp = open(TEMP_FIXTURE, 'r')
    result_diff = load_temp.read()
    with open(res_path) as file_res:
        correct_result = file_res.read()
    assert result_diff == correct_result
