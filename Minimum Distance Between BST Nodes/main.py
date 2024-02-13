#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        flattened_tree: list = []
        nodes_to_process = deque([root])
        while nodes_to_process:
            node = nodes_to_process.popleft()

            if node.left is None and node.right is None:
                continue

            if node.left is not None:
                nodes_to_process.append(node.left)
                flattened_tree.append(node.left.val)

            if node.right is not None:
                nodes_to_process.append(node.right)
                flattened_tree.append(node.right.val)

        return abs(flattened_tree[-1] - flattened_tree[-2])


# @lc code=end
