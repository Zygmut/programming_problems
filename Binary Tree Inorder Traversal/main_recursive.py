# https://leetcode.com/problems/binary-tree-inorder-traversal/


import sys

sys.path.append("..")

from modules.data import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        res = []

        def inorder(node: TreeNode) -> None:
            if node.val > 100 or node.val < -100:
                raise ValueError("Node values must be between [-100, 100]")
            if len(res) > 100:
                raise ValueError(
                    "number of nodes in the tree must be in range of [0, 100]"
                )

            if node.left:
                inorder(node.left)
            res.append(node.val)
            if node.right:
                inorder(node.right)

        inorder(root)
        return res
