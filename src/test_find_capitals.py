"""
CodeWars tests:

Test.assert_equals( capitals('CodEWaRs'), [0,3,4,6] )
"""
import pytest

code_wars_tests = [
    ('CodEWaRs', [0,3,4,6])
]

my_tests = [
    ('This is A TesT', [0, 8, 10, 13]),
    ('capitalS are GREAt', [7, 13, 14, 15, 16]),
    ('thiS is MY lasT kATA for the DaY', [3, 8, 9, 14, 17, 18, 19, 29, 31]),
    ('I am AnXIOUS to get out of herE', [0, 5, 7, 8, 9, 10, 11, 30]),
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_wars_find_capitals(entered, result):
    from find_capitals import capitals
    assert capitals(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_find_capitals(entered, result):
    from find_capitals import capitals
    assert capitals(entered) == result
