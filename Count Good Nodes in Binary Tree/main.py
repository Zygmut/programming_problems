#https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_count = 0
        node_stack = [(root, root.val)]

        while len(node_stack) != 0:
            parent = node_stack.pop()
            if not parent[0]:
                continue

            if parent[0].val >= parent[1]:
                good_node_count += 1


            weight = max(parent[0].val, parent[1])
            node_stack.append((parent[0].left, weight))
            node_stack.append((parent[0].right, weight))


        return good_node_count
