"""
CodeWars tests:

Test.assert_equals(series_sum(1), "1.00")
Test.assert_equals(series_sum(2), "1.25")
Test.assert_equals(series_sum(3), "1.39")
"""
import pytest

code_wars_tests = [
    (1, '1.00'),
    (2, '1.25'),
    (3, '1.39')
]

my_tests = [
    (17, '1.99'),
    (5, '1.57'),
    (7, '1.68'),
    (11, '1.84')
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_wars_sum_series(entered, result):
    from sum_of_nth_term import series_sum
    assert series_sum(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_my_sum_series(entered, result):
    from sum_of_nth_term import series_sum
    assert series_sum(entered) == result
