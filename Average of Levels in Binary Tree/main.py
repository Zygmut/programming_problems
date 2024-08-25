import sys

sys.path.append("..")

from modules.data import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        queue = [root]

        res = []
        while queue:
            length = len(queue)
            sum = 0
            for _ in range(length):
                node = queue.pop(0)

                sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(sum / length)
        return res
