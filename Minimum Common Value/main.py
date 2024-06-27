import sys

sys.path.append("..")

from typing import Tuple, List


def getCommon(nums1: List[int], nums2: List[int]) -> int:
    left = right = 0

    while left < len(nums1) and right < len(nums2):
        if nums1[left] < nums2[right]:
            left += 1
        elif nums1[left] > nums2[right]:
            right += 1
        else:
            return nums1[left]

    return -1


if __name__ == "__main__":
    testcases: List[Tuple[List[int], List[int], int]] = [
        ([1, 2, 3], [2, 4], 2),
        ([1, 2, 3, 6], [2, 3, 4, 5], 2),
        ([1, 2, 3, 6], [7, 8, 9], -1),
    ]

    assert all(
        getCommon(nums1, nums2) == expected for nums1, nums2, expected in testcases
    )
