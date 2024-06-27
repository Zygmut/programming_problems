import sys

sys.path.append("..")

from typing import Tuple, List, Dict


def firstMissingPositive(nums: List[int]) -> int:

    nums_hash: Dict[int, int] = {n: 0 for n in nums}

    for n in range(1, len(nums) + 1):
        if nums_hash.get(n, -1) != 0:
            return n

    return len(nums) + 1


def firstMissingPositive2(nums: List[int]) -> int:
    nums_set = set(nums)

    ans = 1

    while ans <= len(nums) and ans in nums_set:
        ans += 1

    return ans


def firstMissingPositive3(nums: List[int]) -> int:
    nums_set = set(nums)
    best_sols = set(range(1, len(nums) + 2))

    best_sols.difference_update(nums_set)

    return min(best_sols)


def firstMissingPositive4(nums: List[int]) -> int:
    nums_set = set(nums)
    return next(
        (x for x in range(1, len(nums) + 1) if x not in nums_set), len(nums) + 1
    )


if __name__ == "__main__":
    testcases: List[Tuple[List[int], int]] = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
    ]

    assert all(
        all(
            (
                firstMissingPositive(values) == expected,
                firstMissingPositive2(values) == expected,
                firstMissingPositive3(values) == expected,
                firstMissingPositive4(values) == expected,
            )
        )
        for values, expected in testcases
    )
