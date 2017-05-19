"""
CodeWars tests:

from random import randint, shuffle


def test(lst, res):
    Test.assert_equals(min_max(lst), res, "tested on " + str(lst));

Test.describe("min_max")
Test.it("should work for some examples")
test([1, 2, 3, 4, 5], [1, 5])
test([2334454, 5], [5, 2334454])

for i in xrange(0, 20):
    r = randint(0, 100)
    test([r], [r, r])

"""
import pytest

code_wars_tests = [
    ([1, 2, 3, 4, 5], [1, 5]),
    ([2334454, 5], [5, 2334454])
]

my_tests = [
    ([334, 345, 66, 43, 901], [43, 901]),
    ([45, 5, 66, 43], [5, 66]),
    ([3394, 33457, 66, 4343, 45666], [66, 45666]),
    ([4, 565656, 6, 42, 9561], [4, 565656])
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_wars_highest_profit(entered, result):
    from highest_profit import min_max
    assert min_max(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_my_tests_highest_profit(entered, result):
    from highest_profit import min_max
    assert min_max(entered) == result
