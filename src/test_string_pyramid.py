"""Tests for string pyramid code kata."""

import pytest


SIDE_VIEW_PARAMS = [
    ('abc', '  c  \n bbb \naaaaa'),
    ('abcde', '    e    \n   ddd   \n  ccccc  \n bbbbbbb \naaaaaaaaa'),
    ('', '')
]

ABOVE_VIEW_PARAMS = [
    ('abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa'),
    ('abcde', 'aaaaaaaaa\nabbbbbbba\nabcccccba\nabcdddcba\nabcdedcba\nabcdddcba\nabcccccba\nabbbbbbba\naaaaaaaaa'),
    ('', '')
]

VISIBLE_COUNT_PARAMS = [
    ('abc', 25),
    ('abcde', 81),
    ('', -1)
]

TOTAL_COUNT_PARAMS = [
    ('abc', 35),
    ('abcde', 165),
    ('', -1)
]


@pytest.mark.parametrize('entered, result', SIDE_VIEW_PARAMS)
def test_code_side_view(entered, result):
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(entered) == result


@pytest.mark.parametrize('entered, result', ABOVE_VIEW_PARAMS)
def test_my_above_view(entered, result):
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(entered) == result


@pytest.mark.parametrize('entered, result', VISIBLE_COUNT_PARAMS)
def test_my_visible_count(entered, result):
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(entered) == result


@pytest.mark.parametrize('entered, result', TOTAL_COUNT_PARAMS)
def test_my_total_count(entered, result):
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(entered) == result
