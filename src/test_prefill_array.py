"""
Code Wars tests:

Test.assert_equals(prefill(3,1), [1,1,1])
Test.assert_equals(prefill(2,'abc'), ['abc','abc'])
Test.assert_equals(prefill('1',1), [1])
Test.assert_equals(prefill(3, prefill(2,'2d')), [['2d','2d'],['2d','2d'],['2d','2d']])
"""
import pytest
from prefill_array import prefill


code_wars_tests = [
    ((3, 1), [1, 1, 1]),
    ((2, 'abc'), ['abc', 'abc']),
    (('1', 1), [1]),
    ((3, prefill(2, '2d')), [['2d', '2d'], ['2d', '2d'], ['2d', '2d']])
]

my_tests = [
    ((4, 'carlos'), ['carlos', 'carlos', 'carlos', 'carlos']),
    ((3, None), [None, None, None]),
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_wars_prefill_array(entered, result):
    assert prefill(entered[0], entered[1]) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_prefill_array_my_tests(entered, result):
    assert prefill(entered[0], entered[1]) == result
