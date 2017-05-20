"""
CodeWars tests:

Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
Test.assert_equals(high_and_low("1 -1"), "1 -1");
Test.assert_equals(high_and_low("1 1"), "1 1");
Test.assert_equals(high_and_low("-1 -1"), "-1 -1");
"""
import pytest

code_wars_tests = [
    ("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6", "542 -214"),
    ("1 -1", "1 -1"),
    ("1 1", "1 1"),
    ("-1 -1", "-1 -1")
]

my_tests = [
    ('65 34 8 4 4 77 5', '77 4'),
    ('878 44 555 632 45', '878 44'),
    ('78 333 97 6 44 71', '333 6'),
    ('454 45 23 203 -4545 99', '454 -4545'),
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_wars_highest_and_lowest(entered, result):
    from highest_and_lowest import high_and_low
    assert high_and_low(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_highest_an_lowest(entered, result):
    from highest_and_lowest import high_and_low
    assert high_and_low(entered) == result
