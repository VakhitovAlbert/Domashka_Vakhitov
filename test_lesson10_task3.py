import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("params, result", [((1, 0), ZeroDivisionError),
                                            pytest.param((2,), 2, marks=pytest.mark.smoke),
                                            pytest.param((50, 5), 10, marks=pytest.mark.skip('Skip')),
                                            ((-10, 10), -1),
                                            ((0, 2), 0)])
def test_albert(params, result):1
    if result == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            all_division(*params)
    else:
        assert all_division(*params) == result
