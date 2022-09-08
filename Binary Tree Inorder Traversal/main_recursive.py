# https://leetcode.com/problems/binary-tree-inorder-traversal/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:

        res = []

        def inorder(node: TreeNode) -> None:
            if node.left:
                inorder(node.left)
            res.append(node)
            if node.right:
                inorder(node.right)

        inorder(root)
        return res
