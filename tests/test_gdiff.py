import pytest
import sys
sys.path.append('/home/sat/python-project-lvl2')
from gen_diff import generate_d


A = "{\n- follow: false\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}"


def result_open():
    with open('/home/sat/python-project-lvl2/tests/fixtures/result1') as fi:
        intro = fi.read()
        return intro

def test_generate_diff():   
    assert generate_d.generate_diff('file1.json', 'file2.json') == result_open()



print(result_open())

