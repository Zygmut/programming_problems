def islandPerimeter(self, grid: List[List[int]]) -> int:
    def _get_adj(matrix, row, col) -> tuple:
        return (
            matrix[row][col - 1] if (col - 1) >= 0 else 0,
            matrix[row][col + 1] if (col + 1) <= (len(grid[0]) - 1) else 0,
            matrix[row - 1][col] if (row - 1) >= 0 else 0,
            matrix[row + 1][col] if (row + 1) <= (len(grid) - 1) else 0,
        )

    island_tiles = (
        (row_idx, col_idx)
        for row_idx, row in enumerate(grid)
        for col_idx, elem in enumerate(row)
        if elem != 0
    )

    sol = 0
    for row_idx, col_idx in island_tiles:
        sol += _get_adj(grid, row_idx, col_idx).count(0)
        
    return sol
        
