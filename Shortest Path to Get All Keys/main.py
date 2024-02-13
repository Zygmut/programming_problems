#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#

from functools import reduce
from collections import deque


# @lc code=start
class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])

        total_keys: int = reduce(
            lambda acc, keys: acc + len(list(keys)),
            map(lambda row: filter(lambda col: col in "abcdef", row), grid),
            0,
        )

        movements: list[tuple(int, int), ...] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        start_row, start_col = next(
            (
                (row_idx, row.index("@"))
                for row_idx, row in enumerate(grid)
                if any(char == "@" for char in row)
            ),
            None,
        )

        visited_positions = set([(start_row, start_col, ".@abcdef")])

        queue = deque([(start_row, start_col, ".@abcdef", 0, 0)])

        while queue:
            curr_row, curr_col, valid_tiles, steps, keys = queue.popleft()

            curr_state = grid[curr_row][curr_col]
            if curr_state in "abcdef" and curr_state.upper() not in valid_tiles:
                valid_tiles += curr_state.upper()
                keys += 1

            if keys == total_keys:
                return steps

            for delta_row, delta_col in movements:
                # Check if new movement is out of bounds
                updated_row, updated_col = curr_row + delta_row, curr_col + delta_col

                if (
                    not (0 <= updated_row < num_rows and 0 <= updated_col < num_cols)
                    or grid[updated_row][updated_col] not in valid_tiles
                ):
                    continue

                if (updated_row, updated_col, valid_tiles) in visited_positions:
                    continue

                visited_positions.add((updated_row, updated_col, valid_tiles))
                queue.append((updated_row, updated_col, valid_tiles, steps + 1, keys))

        return -1


# @lc code=end
