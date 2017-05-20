"""
CodeWars tests:

test.assert_equals(filter_list([1,2,'a','b']),[1,2])
test.assert_equals(filter_list([1,'a','b',0,15]),[1,0,15])
test.assert_equals(filter_list([1,2,'aasf','1','123',123]),[1,2,123])
"""
import pytest

code_wars_tests = [
    ([1, 2, 'a', 'b'], [1, 2]),
    ([1, 'a', 'b', 0, 15], [1, 0, 15]),
    ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123])
]

my_tests = [
    ([12, 3, 'df', 67, 'tside', 'thidetoo'], [12, 3, 67]),
    ([233, 56, 'a', 'b', 6, 7, 7], [233, 56, 6, 7, 7]),
    (['asj', 13, 44, 6, 'lsaksjfda', 6], [13, 44, 6, 6]),
    (['ls', 5, 5, 'lksajglskgjalskjga', 56, 99], [5, 5, 56, 99]),
]


@pytest.mark.parametrize('entered, result', code_wars_tests)
def test_code_wars_list_filtering(entered, result):
    from list_filtering import filter_list
    assert filter_list(entered) == result


@pytest.mark.parametrize('entered, result', my_tests)
def test_list_filtering(entered, result):
    from list_filtering import filter_list
    assert filter_list(entered) == result
