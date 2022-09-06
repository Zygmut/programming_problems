# https://leetcode.com/problems/binary-tree-pruning/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        if root.left:
            root.left = self.pruneTree(root.left)

        if root.right:
            root.right = self.pruneTree(root.right)

        if not (root.left or root.right):
            return root if root.val == 1 else None

        return root
