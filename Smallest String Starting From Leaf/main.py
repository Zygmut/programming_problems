import sys

sys.path.append("..")

from modules.data import TreeNode
from typing import Optional


def smallestFromLeaf(root: Optional[TreeNode]) -> str:
    queue = [(root, "")]
    sol = ""

    while queue:
        node, path = queue.pop()

        new_path = chr(node.val + ord("a")) + path

        if not (node.left or node.right):
            if sol is None or new_path < sol:
                sol = new_path
            continue

        if node.left:
            queue.append((node.left, new_path))

            if node.right:
                queue.append((node.right, new_path))

    return sol
