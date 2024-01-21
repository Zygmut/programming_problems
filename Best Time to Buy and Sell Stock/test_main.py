from multiprocessing.sharedctypes import Value
import pytest
from main import Solution


@pytest.mark.parametrize(
    "problem,expected",
    (([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)),
)
def test_main(problem, expected):
    sol = Solution()
    assert sol.maxProfit(problem) == expected


@pytest.mark.parametrize(
    "problem,expected",
    (([0] * (10**5 + 1), ValueError), ([-1], ValueError)),
)
def test_exceptions_main(problem, expected):
    with pytest.raises(expected):
        sol = Solution()
        sol.maxProfit(problem)
