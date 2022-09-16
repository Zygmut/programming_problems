import pytest


@pytest.mark.parametrize(
    "problem,expected",
    ((([1,2,3], [3,2,1]), 14),
    (([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]), 102)),
)
def test_main(problem, expected):
    pass


@pytest.mark.parametrize(
    "problem,expected",
    ((([1,2], []), ValueError),
    (([0]*105, [0]*104), ValueError),
    (([1], [1,2]), ValueError),
    ),
)
def test_exceptions_main(problem, expected):
    with pytest.raises(expected):
        pass
