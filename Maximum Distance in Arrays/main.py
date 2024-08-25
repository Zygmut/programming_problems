from typing import Tuple, List


def maxDistance(arrays: List[List[int]]) -> int:
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_distance = 0

    for arr in arrays[1:]:
        max_distance = max(max_distance, abs(arr[0] - max_val), abs(arr[-1] - min_val))
        min_val = min(min_val, arr[0])
        max_val = max(max_val, arr[-1])

    return max_distance


if __name__ == "__main__":
    testcases: List[Tuple[List[List[int]], int]] = [
        ([[1, 2, 3], [4, 5], [1, 2, 3]], 4),
        ([[1], [1]], 0),
    ]

    assert all(maxDistance(values) == expected for values, expected in testcases)
