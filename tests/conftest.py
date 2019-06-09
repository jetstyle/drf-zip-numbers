"""
Fixtures
"""
import pytest


@pytest.fixture
def no_zipped():
    """
    No-zipped strings
    """
    return [
        ('', []),
        ('123', [123]),
        ('123,456', [123, 456])
    ]


@pytest.fixture
def ranges():
    """
    Strings with ranges
    """
    return [
        ('1-3', [1, 2, 3]),
        ('1-3,5-9', [1, 2, 3, 5, 6, 7, 8, 9]),
    ]


@pytest.fixture
def zipped():
    """
    Zipped strings
    """
    return [
        ('120(0,3,5,8,9)', [120, 123, 125, 128, 129]),
        ('12(1,4),140(0,2,5)', [13, 16, 140, 142, 145])
    ]


@pytest.fixture
def mixed():
    """
    Strings with zipped data and ranges
    """
    return [
        ('120(0,3,6),130-132', [120, 123, 126, 130, 131, 132]),
        ('120(0-6)', [120, 121, 122, 123, 124, 125, 126])
    ]


@pytest.fixture
def bases():
    """
    Strings with base of numbers
    """
    return [
        ('x16;3,f', [3, 15]),
        ('x2;11,101', [3, 5]),
    ]


@pytest.fixture
def greater_10():
    """
    For test limit 10
    """
    return [
        '1-20',
        '1,2,3,4,5,6,7,8,9,10,11',
        '1,2,3,5,6,8-16',
        '14(1-15)',
    ]


@pytest.fixture
def less_10():
    """
    For test limit 10
    """
    return [
        ('1-10', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ('1,2,5,7-13', [1, 2, 5, 7, 8, 9, 10, 11, 12, 13]),
        ('14(0-8,18)', [14, 15, 16, 17, 18, 19, 20, 21, 22, 32])
    ]


@pytest.fixture
def field_zipped():
    """
    For test making string
    """
    return [
        ([], ''),
        ([1], '1'),
        ([1, 2], '1,2'),
        ([1, 2, 3], '1(0-2)'),
        ([1, 2, 3, 4], '1(0-3)'),
        ([1, 3, 5, 7], '1(0,2,4,6)'),
        ([1, 2, 3, 5, 6, 7], '1(0-2,4-6)'),
        ([1, 2, 3, 5, 6, 7, 9], '1(0-2,4-6,8)'),
    ]
