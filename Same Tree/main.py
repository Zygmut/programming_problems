from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    queue = [(p, q)]

    while queue:
        left, right = queue.pop()

        if left is None and right is None:
            continue

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        queue.extend([(left.left, right.left), (left.right, right.right)])

    return True
