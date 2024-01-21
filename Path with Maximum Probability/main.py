#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

from collections import deque

# @lc code=start
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start: int,
        end: int,
    ) -> float:
        adj: list[list[tuple(int, int), ...], ...] = [[] for _ in range(n)]

        for [source, target], cost in zip(edges, succProb):
            adj[source].append((target, cost))
            adj[target].append((source, cost))

        max_probability: list[float, ...] = [0.0] * n
        max_probability[start] = 1.0

        queue: Deque[int] = deque([start])

        while queue:
            current_node: int = queue.popleft()

            for connection, prob in adj[current_node]:
                path_probability: float = max_probability[current_node] * prob
                if path_probability > max_probability[connection]:
                    max_probability[connection] = path_probability
                    queue.append(connection)

        return max_probability[end]
# @lc code=end