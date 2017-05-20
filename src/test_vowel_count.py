"""
CodeWars tests:

test.assert_equals(getCount("abracadabra"), 5)
"""
import pytest

code_wars_tests = [
    ("abracadabra", 5)
]

my_tests = [
    ('hello my name is carlos', 7),
    ('it was sunny today', 5),
    ('i would like to ride my bicycle', 10),
    ('python challenging katas', 6)
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_vowel_count(entered, result):
    from vowel_count import get_count
    assert get_count(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_my_vowel_count(entered, result):
    from vowel_count import get_count
    assert get_count(entered) == result
