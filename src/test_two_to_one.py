"""
CodeWars tests:

Test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
Test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
Test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
"""
import pytest

code_wars_tests = [
    ("aretheyhere", "yestheyarehere", "aehrsty"),
    ("loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu"),
    ("inmanylanguages", "theresapairoffunctions", "acefghilmnoprstuy")
]

my_tests = [
    ('thisside', 'thissidetoo', 'dehiost'),
    ('whattimeisit', 'bonesawtime', 'abehimnostw'),
    ('asjfalskjgag', 'lsakjfalksjfda', 'adfgjkls'),
    ('lsjgaskjgajwoigjobinz', 'lksajglskgjalskjga', 'abgijklnoswz'),
    ('lsjgaskjgajwoigjobinzq', 'lksajglskgjalskjga', 'abgijklnoqswz')
]


@pytest.mark.parametrize('entered1, entered2, result', code_wars_tests)
def test_code_wars_two_to_one(entered1, entered2, result):
    from two_to_one import longest
    assert longest(entered1, entered2) == result


@pytest.mark.parametrize('entered1, entered2, result', my_tests)
def test_two_to_one(entered1, entered2, result):
    from two_to_one import longest
    assert longest(entered1, entered2) == result
