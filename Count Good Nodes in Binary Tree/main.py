# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


import sys

sys.path.append("..")

from modules.data import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0
        node_stack = [(root, root.val)]

        while len(node_stack) != 0:
            parent, max_curr_val = node_stack.pop()
            if not parent:
                continue

            if parent.val >= max_curr_val:
                good_node_count += 1

            weight = max(parent.val, max_curr_val)

            if parent.left:
                node_stack.append((parent.left, weight))
            if parent.right:
                node_stack.append((parent.right, weight))

        return good_node_count
