# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root, 1)])
        max_depth: int = 1

        while queue:
            node, current_depth = queue.popleft()
            if node.left is not None:
                queue.append((node.left, current_depth + 1))
            if node.right is not None:
                queue.append((node.right, current_depth + 1))

            max_depth = max(max_depth, current_depth)

        return max_depth
