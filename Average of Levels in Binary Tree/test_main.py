import pytest
from main import Solution, TreeNode


def create_tree(values: list[int]) -> TreeNode:
    n = len(values)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or values[index] is None:
            return None

        node = TreeNode(values[index], inner(2 * index + 1), inner(2 * index + 2))
        return node

    return inner()


@pytest.mark.parametrize(
    "input,expected",
    (
        ([3, 9, 20, None, None, 15, 7], [3, 14.5, 11]),
        ([3, 9, 20, 15, 7], [3, 14.5, 11]),
    ),
)
def test_main(input, expected):
    sol = Solution()
    assert sol.averageOfLevels(create_tree(input)) == expected
