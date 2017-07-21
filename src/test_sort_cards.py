"""Tests for Code Wars Sort Cards"""
import pytest


code_wars_tests = [
    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    (list('Q286JK395A47T'), list('A23456789TJQK')),
    (list('54TQKJ69327A8'), list('A23456789TJQK'))
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_sort_cards(entered, result):
    from sort_cards import sort_cards
    assert sort_cards(entered) == result
