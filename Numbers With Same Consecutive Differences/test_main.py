import pytest
from main import Solution


@pytest.mark.parametrize(
    "input,expected",
    (
        ((3, 7), [181, 292, 707, 818, 929]),
        ((2, 1), [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]),
    ),
)
def test_numbers(input, expected):
    sol = Solution()
    assert sorted(sol.numsSameConsecDiff(input[0], input[1])) == sorted(expected)


@pytest.mark.parametrize(
    "input,expected",
    (
        ((1, 0), ValueError),
        ((10, 0), ValueError),
        ((2, -1), ValueError),
        ((2, 10), ValueError),
    ),
)
def test_exceptions_numbers(input, expected):
    with pytest.raises(expected):
        sol = Solution()
        sol.numsSameConsecDiff(input[0], input[1])
