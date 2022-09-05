# https://leetcode.com/problems/n-ary-tree-level-order-traversal/


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:

        res = []
        queue = [(root, 0)]

        while queue:
            parent, level = queue.pop(0)

            if not parent:
                continue

            if len(res) < level + 1:
                res.append([])

            res[level].append(parent.val)

            for node in parent.children:
                if not node:
                    continue

                queue.append((node, level + 1))

        return res
