import sys

sys.path.append("..")

from typing import Tuple, List, Any


def fn(nums: List[int]) -> int:
    sol = 0
    sum_left = nums[0]
    sum_right = sum(nums[1:])

    for idx in range(1, len(nums)):
        if sum_left >= sum_right:
            sol += 1

        sum_left += nums[idx]
        sum_right -= nums[idx]

    return sol


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        ([10, 4, -8, 7], 2),
        ([2, 3, 1, 0], 2),
    ]

    assert all(fn(values) == expected for values, expected in testcases)
