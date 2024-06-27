import pytest
from main import Solution


@pytest.mark.parametrize(
    "input,expected",
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ),
)
def test_spiral(input, expected):
    sol = Solution()
    assert sol.spiralOrder(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    (
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11],
            ],
            ValueError,
        ),
        ([[]], ValueError),
    ),
)
def test_exceptions_spiral(input, expected):
    with pytest.raises(expected):
        sol = Solution()
        sol.spiralOrder(input)
    pass
