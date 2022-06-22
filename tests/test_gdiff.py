import pytest
import os
from gendiff.diff_generator import generate_diff


TEST_PATH = os.path.dirname(os.path.abspath(__file__))
FIXTURE_PATH = f'{TEST_PATH}/fixtures'


@pytest.mark.parametrize('file1, file2, res_file, format',
                         [('file5.json', 'file6.json',
                          'complete_stylish.txt', 'stylish'),
                          ('file5.yaml', 'file6.yaml',
                          'complete_plain.txt', 'plain'),
                          ('file5.json', 'file6.yaml',
                          'complete_json.txt', 'json')])
def test_generate_diff(file1, file2, res_file, format):
    path_file1 = f'{FIXTURE_PATH}/{file1}'
    path_file2 = f'{FIXTURE_PATH}/{file2}'
    result_path = f'{FIXTURE_PATH}/{res_file}'
    result_gendiff = generate_diff(path_file1, path_file2, format)
    with open(result_path) as file_res:
        correct_result = file_res.read()
        assert result_gendiff == correct_result
