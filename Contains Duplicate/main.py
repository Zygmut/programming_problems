import sys

sys.path.append("..")

from typing import List, Tuple


def containsDuplicate_1(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


def containsDuplicate_2(nums: List[int]) -> bool:
    unique = set()
    for n in nums:
        if n in unique:
            return True
        unique.add(n)

    return False


if __name__ == "__main__":
    testcases: List[Tuple[List[int], bool]] = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    assert all(
        all(fn(nums) == expected for fn in [containsDuplicate_1, containsDuplicate_2])
        for nums, expected in testcases
    )
