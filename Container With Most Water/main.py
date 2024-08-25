import sys

sys.path.append("..")

from typing import Tuple, List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(max_area, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == "__main__":
    testcases: List[Tuple[List[int], int]] = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ]

    assert all(maxArea(values) == expected for values, expected in testcases)
