# https://leetcode.com/problems/spiral-matrix


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        arr = []

        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        top, left = 0, 0

        if bottom < 1:
            raise ValueError("m should be greater than 1")

        if right + 1 > 10:
            raise ValueError("n should be less than 10")

        while True:
            if left > right:
                break

            # top row
            for i in range(left, right + 1):
                arr.append(matrix[top][i])
            top += 1

            if top > bottom:
                break

            # right column
            for i in range(top, bottom + 1):
                arr.append(matrix[i][right])
            right -= 1

            if left > right:
                break

            # bottom row
            for i in range(right, left - 1, -1):
                arr.append(matrix[bottom][i])
            bottom -= 1

            if top > bottom:
                break

            # left column
            for i in range(bottom, top - 1, -1):
                arr.append(matrix[i][left])
            left += 1

        return arr
