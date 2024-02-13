#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#


# @lc code=start
class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n: int = len(grid)
        nodes_to_visit: list[tuple[int, int]] = [
            (y, x) for x in range(n) for y in range(n) if grid[y][x]
        ]

        if len(nodes_to_visit) in (0, n * n):
            return -1

        distance_matrix: list[list[int]] = grid[:]
        max_distance = 0

        while nodes_to_visit:
            origin_y, origin_x = nodes_to_visit.pop(0)
            for displacement_x, displacement_y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                destination_x = origin_x + displacement_x
                destination_y = origin_y + displacement_y

                if (
                    0 <= destination_x < n
                    and 0 <= destination_y < n
                    and not distance_matrix[destination_y][destination_x]
                ):
                    nodes_to_visit.append((destination_y, destination_x))
                    distance_matrix[destination_y][destination_x] = (
                        distance_matrix[origin_y][origin_x] + 1
                    )
                    max_distance = max(
                        max_distance, distance_matrix[destination_y][destination_x]
                    )

        return max_distance - 1


# @lc code=end
