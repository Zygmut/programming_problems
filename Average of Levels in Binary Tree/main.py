# https://leetcode.com/problems/average-of-levels-in-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        queue = [root]

        res = []
        while queue:
            l = len(queue)
            sum = 0
            for _ in range(l):
                node = queue.pop(0)

                sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(sum / l)
        return res
