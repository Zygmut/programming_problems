# https://leetcode.com/problems/construct-string-from-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if 1000 < root.val < -1000:
            raise ValueError("Tree nodes values mustbe between -1000 and 1000")

        result = str(root.val)

        if root.left:
            result += f"({self.tree2str(root.left)})"

        if root.right:
            if not root.left:
                result += "()"
            result += f"({self.tree2str(root.right)})"

        return result
