import pytest
from main import Solution


@pytest.mark.parametrize(
    "input,expected",
    (("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("", 0), (" ", 1), ("au", 2)),
)
def test_longest(input, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(input) is expected


@pytest.mark.parametrize(
    "input,expected",
    (("".join("x" for i in range(5 * 105)), ValueError), (tuple(), ValueError)),
)
def test_exceptions_longest(input, expected):
    with pytest.raises(expected):
        solution = Solution()
        solution.lengthOfLongestSubstring(input)
