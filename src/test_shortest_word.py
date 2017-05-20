"""
CodeWars tests:

test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
"""
import pytest

code_wars_tests = [
    ("bitcoin take over the world maybe who knows perhaps", 3),
    ("turns out random test cases are easier than writing out basic ones", 3),
    ("lets talk about javascript the best language", 3),
    ("i want to travel the world writing code one day", 1),
    ("Lets all go on holiday somewhere very cold", 2)
]

my_tests = [
    ('Hello hi there nice to meet you', 2),
    ('Very long words are hard to come by', 2),
    ('longer longest something something', 6),
    ('python challenging katas', 5)
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_shortest_word(entered, result):
    from shortest_word import find_short
    assert find_short(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_my_shortest_word(entered, result):
    from shortest_word import find_short
    assert find_short(entered) == result
