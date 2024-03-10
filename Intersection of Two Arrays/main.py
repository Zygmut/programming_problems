import sys

sys.path.append("..")

from typing import Tuple, List, Any


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    left = sorted(set(nums1))
    right = sorted(set(nums2))

    union = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            left_idx += 1
        elif left[left_idx] > right[right_idx]:
            right_idx += 1
        else:
            union.append(left[left_idx])
            left_idx += 1
            right_idx += 1

    return union


if __name__ == "__main__":
    testcases: List[Tuple[List[int], List[int], List[int]]] = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
    ]

    assert all(
        intersection(left, right) == expected for left, right, expected in testcases
    )
