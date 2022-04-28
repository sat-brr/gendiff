import pytest
import sys
sys.path.append('/home/sat/python-project-lvl2')
from gen_diff.generate import generate_diff

@pytest.fixture
def file1():
    return './test/file1.json'


@pytest.fixture
def file2():
    return './test/file2.json'


def test_gendiff(file1, file2):
    generate_diff(file1, file2)
    assert None == None



