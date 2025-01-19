from typing import Tuple, List, Any

def fn(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])

    is_inside = lambda row, col: 0 <= row < rows and 0 <= col < cols

    cost = [[float("inf")] * cols for _ in range(rows)]
    cost[0][0] = 0

    queue = [(0, 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        row, col = queue.pop(0)

        direction = grid[row][col]

        for idx, (dcol, drow) in enumerate(directions):

            # Semantically the same as additional cost
            diff_direction = (idx + 1) != direction
            new_row, new_col = row + drow, col + dcol

            if (
                is_inside(new_row, new_col)
                and cost[row][col] + diff_direction < cost[new_row][new_col]
            ):
                cost[new_row][new_col] = cost[row][col] + diff_direction

                queue.insert(diff_direction * len(queue) , (new_row, new_col))

    return int(cost[rows - 1][cols - 1])


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (([[1, 1, 3], [3, 2, 2], [1, 1, 4]],), 0),
        (([[1, 2], [4, 3]],), 1),
        (([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]],), 3),
    ]

    for idx, (values, expected) in enumerate(testcases):
        result = fn(*values)

        if result != expected:
            print(f"Failed Test {idx}")
            print(f"Got      {result}")
            print(f"Expected {expected}")
            print()
