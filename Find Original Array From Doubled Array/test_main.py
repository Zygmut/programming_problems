import pytest
from main import Solution


@pytest.mark.parametrize(
    "problem,expected",
    (([1, 3, 4, 2, 6, 8], [1, 3, 4]), ([6, 3, 0, 1], []), ([1], [])),
)
def test_main(problem, expected):
    sol = Solution()
    assert sorted(sol.findOriginalArray(problem)) == sorted(expected)


@pytest.mark.parametrize(
    "problem,expected",
    (
        ([], ValueError),
        ([0] * (10**5 + 1), ValueError),
        ([-1, -2], ValueError),
        ([1 + 10**5, 2 * (1 + 10**5)], ValueError),
    ),
)
def test_exceptions_main(problem, expected):
    with pytest.raises(expected):
        sol = Solution()
        sol.findOriginalArray(problem)
