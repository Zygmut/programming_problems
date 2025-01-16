from typing import Tuple, List, Any
from functools import reduce


def xor(a, b):
    return a ^ b


def f(nums1: List[int], nums2: List[int]) -> int:
    a = reduce(xor, nums1) if len(nums2) & 1 else 0
    b = reduce(xor, nums2) if len(nums1) & 1 else 0

    return a ^ b


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (
            (
                [2, 1, 3],
                [10, 2, 5, 0],
            ),
            13,
        ),
        (
            (
                [1, 2],
                [3, 4],
            ),
            0,
        ),
    ]

    assert all(f(*values) == expected for values, expected in testcases)
