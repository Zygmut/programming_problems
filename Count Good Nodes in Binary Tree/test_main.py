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
    "input,expected", (([3, 1, 4, 3, None, 1, 5], 4), ([3, 3, None, 4, 2], 3), ([1], 1))
)
def test_count(input, expected):
    sol = Solution()
    assert sol.goodNodes(create_tree(input)) is expected
