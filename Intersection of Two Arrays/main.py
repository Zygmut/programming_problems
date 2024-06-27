import sys

sys.path.append("..")

from typing import Tuple, List, Set


# Two pointers
def intersection(nums1: List[int], nums2: List[int]) -> Set[int]:
    left = sorted(set(nums1))
    right = sorted(set(nums2))

    union = set()
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            left_idx += 1
        elif left[left_idx] > right[right_idx]:
            right_idx += 1
        else:
            union.add(left[left_idx])
            left_idx += 1
            right_idx += 1

    return union


# Using set theory
def intersection2(nums1: List[int], nums2: List[int]) -> Set[int]:
    left, right = set(nums1), set(nums2)
    return left - (left - right)


# Using in-built functions
def intersection3(nums1: List[int], nums2: List[int]) -> Set[int]:
    return set(nums1).intersection(set(nums2))


if __name__ == "__main__":
    testcases: List[Tuple[List[int], List[int], Set[int]]] = [
        ([1, 2, 2, 1], [2, 2], set([2])),
        ([4, 9, 5], [9, 4, 9, 8, 4], set([9, 4])),
    ]

    assert all(
        all(
            (
                intersection(left, right) == expected,
                intersection2(left, right) == expected,
            )
        )
        for left, right, expected in testcases
    )
