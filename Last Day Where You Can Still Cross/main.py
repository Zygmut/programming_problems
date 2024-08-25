#
# @lc app=leetcode id=1970 lang=python3
#
# [1970] Last Day Where You Can Still Cross
#

from collections import deque
from bisect import bisect


# @lc code=start
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        tup_cells = list(map(tuple, cells))

        def has_solution(step: int) -> int:
            visited = set(tup_cells[:step])
            queue = deque([(1, col) for col in range(1, col + 1)])

            while queue:
                curr_y, curr_x = queue.popleft()

                if not (1 <= curr_y <= row and 1 <= curr_x <= col):
                    continue

                if (curr_y, curr_x) in visited:
                    continue

                if curr_y == row:
                    return 0

                visited.add((curr_y, curr_x))

                for delta_x, delta_y in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    queue.append((curr_y + delta_y, curr_x + delta_x))

            return 1

        return bisect(range(1, len(cells)), 0, key=has_solution)


# @lc code=end

assert Solution().latestDayToCross(2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]) == 2
assert Solution().latestDayToCross(2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]) == 1
assert (
    Solution().latestDayToCross(
        3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]
    )
    == 3
)
