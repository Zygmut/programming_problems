from typing import Optional
import sys

sys.path.append("..")

from modules.data import TreeNode
from collections import deque


def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    queue = deque([(root, 1)])
    max_depth: int = 1

    while queue:
        node, current_depth = queue.popleft()
        if node.left is not None:
            queue.append((node.left, current_depth + 1))
        if node.right is not None:
            queue.append((node.right, current_depth + 1))

        max_depth = max(max_depth, current_depth)

    return max_depth
