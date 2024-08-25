from typing import Optional, List, Tuple
import sys

sys.path.append("..")

from modules.data import TreeNode


def addOneRow(root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    if depth == 1:
        new_root = TreeNode(val, left=root)
        return new_root

    queue: List[Tuple[Optional[TreeNode], int]] = [(root, 1)]

    while queue:
        node, cur_depth = queue.pop()

        if cur_depth == depth - 1:
            left = TreeNode(val, left=node.left)
            right = TreeNode(val, right=node.right)
            node.left = left
            node.right = right

        queue.append((node.left, cur_depth + 1)) if node.left else None
        queue.append((node.right, cur_depth + 1)) if node.right else None

    return root
