import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_zero():
    try:
        all_division(1, 0)
    except ZeroDivisionError:
        assert True


@pytest.mark.smoke
def test_albert01():
    assert all_division(2) == 2


def test_albert02():
    assert all_division(50, 5) == 10


def test_vakhitov03():
    assert all_division(-10, 10) == -1


def test_vakhitov04():
    assert all_division(0, 2) == 0
