import pytest
from main_recursive import Solution
from main_recursive import TreeNode


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
    "problem,expected", (([1, None, 2, None, None, 3], [1, 3, 2]), ([], []), ([1], [1]))
)
def test_recursive(problem, expected):
    sol = Solution()
    assert sol.inorderTraversal(create_tree(problem)) == expected


@pytest.mark.parametrize(
    "problem,expected",
    (([-101], ValueError), ([101], ValueError), ([0] * 102, ValueError)),
)
def test_exceptions_recursive(problem, expected):
    with pytest.raises(expected):
        sol = Solution()
        sol.inorderTraversal(create_tree(problem))
