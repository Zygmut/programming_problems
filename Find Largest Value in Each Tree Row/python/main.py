import sys

sys.path.append("../..")

from typing import List, Optional
from collections import deque
from modules.data import TreeNode

LEAST_VALUE = pow(-2, 31) - 1

def fn(node: Optional[TreeNode]) -> List[int]:
    if not node:
        return []

    to_process: deque[TreeNode] = deque([])
    row: deque[TreeNode] = deque([node])

    sol: List[int] = []

    while row:
        to_process = row
        row = deque([])

        curr_max_val = float('-inf')

        while to_process:

            curr_node = to_process.pop()
            curr_max_val = max(curr_max_val, curr_node.val)

            if curr_node.left:
                row.append(curr_node.left)

            if curr_node.right:
                row.append(curr_node.right)

        sol.append(int(curr_max_val))

    return sol


if __name__ == "__main__":
    testcases = [
        (TreeNode.from_list([1,3,2,5,3,None,9]), [1,3,9]),
        (TreeNode.from_list([1,2,3]), [1,3])
    ]

    assert all(fn(values) == expected for values, expected in testcases)
