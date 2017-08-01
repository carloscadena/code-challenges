"""Test suite for forbes kata."""
from forbes import info
from forbes import forbes


def test_forbes_returns_correct_information():
    """Test original information returns correct results."""
    assert forbes() == ('oldest: ', 'Phil Knight', 24400000000, 'Nike',
                        'youngest: ', 'Mark Zuckerberg', 44600000000, 'Facebook')


def test_without_previous_two():
    """Test diffrent information returns correct results."""
    info.remove(info[5])
    info.remove(info[-17])
    assert forbes() == ('oldest: ', 'Carlos Slim Helu', 50000000000, 'telecom',
                        'youngest: ', 'Sergey Brin', 34400000000, 'Google')
