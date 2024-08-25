import sys

sys.path.append("..")

from modules.data import TreeNode
from typing import Optional, List


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        leaf_nodes: List[int] = []

        nodes = [(root, 0)]

        while nodes:
            node, path = nodes.pop()
            current_path = path * 10 + node.val

            if not (node.left or node.right):
                leaf_nodes.append(current_path)
                continue

            if node.left:
                nodes.append((node.left, current_path))

            if node.right:
                nodes.append((node.right, current_path))

        return sum(leaf_nodes)
