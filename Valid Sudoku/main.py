def isValidSudoku(self, board: List[List[str]]) -> bool:
    number_iter = (
        (board[col][row], col, row)
        for col in range(9) 
        for row in range(9)
        if board[col][row] != '.'
    )

    registry = []
    for elem, col, row in number_iter:
        registry += [(elem, row), (col, elem), (elem, row // 3, col // 3)]


    return len(registry) == len(set(registry))
