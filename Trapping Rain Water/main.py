import sys

sys.path.append("..")

from typing import Tuple, List


def trap(height: List[int]) -> int:
    # We know that there is a maximum element that is the "top" of the terrain
    max_elem = max(height)

    # Main idea is to subtract the current terrain to the "flattened" terrain
    terrain = sum(height)
    flattened_terrain = 0

    # We'll iterate from the left until we find the maximum, "flattening" the terrain
    # Safe where we ended up
    left = 0
    left_max = 0
    for idx, element in enumerate(height):
        if element == max_elem:
            left = idx - 1
            break

        left_max = max(left_max, element)
        flattened_terrain += left_max

    # We'll iterate from the right until we find the maximum, "flattening" the terrain
    # Safe where we ended up
    right = 0
    right_max = 0
    for idx, element in enumerate(height[::-1]):
        if element == max_elem:
            right = len(height) - idx
            break

        right_max = max(right_max, element)
        flattened_terrain += right_max

    # There might be some terrain between the maximums, so we need to "flatten" the terrain between them
    flattened_terrain += max_elem * ((right - left) - 1)

    return flattened_terrain - terrain


if __name__ == "__main__":
    testcases: List[Tuple[List[int], int]] = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ]

    assert all(trap(values) == expected for values, expected in testcases)
