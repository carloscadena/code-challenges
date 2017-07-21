"""Test for Proper Parenthetics extra credit challenge."""
import pytest


PARAMS_TABLE = [
    ('()((()))', 0),
    ('()(())(((())))', 0),
    ('()((()))(((()))', 1),
    ('()(((())()))(((())())()', 1),
    ('())((((()))(()()(()((()()()(()()))))))))', -1),
    ('()((()))(((()))))', -1)
]


@pytest.mark.parametrize('entered, result', PARAMS_TABLE)
def test_proper_parenthetics(entered, result):
    from parenthetics import parens
    assert parens(entered) == result
