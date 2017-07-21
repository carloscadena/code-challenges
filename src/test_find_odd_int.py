"""
CodeWars tests:

test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
"""
import pytest

code_wars_tests = [
    ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5)
]

my_tests = [
    ([-2, 20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2], -2),
    ([20, 20, 1, 5, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 20),
    ([5, 1, -1, 2, -2, 3, 3, 1, 2, 4, 4, -1, -2, 5, 1], 1),
    ([20, 1, -1, 2, 3, 3, 1, 2, 4, 20, 3, 4, -1, 5], 3)
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_cw_find_odd_int(entered, result):
    from find_odd_int import find_it
    assert find_it(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_find_odd_int(entered, result):
    from find_odd_int import find_it
    assert find_it(entered) == result
