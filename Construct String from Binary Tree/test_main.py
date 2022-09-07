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
    "problem,expected",
    (([1, 2, 3, 4], "1(2(4))(3)"), ([1, 2, 3, None, 4], "1(2()(4))(3)")),
)
def test_main(problem, expected):
    sol = Solution()
    assert sol.tree2str(create_tree(problem)) == expected
