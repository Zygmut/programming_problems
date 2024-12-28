import sys
from typing import List
from functools import cache

sys.path.append("..")

def fn(nums: List[int], target: int) -> int:

    @cache
    def recursion(idx: int, current_sum: int):
        if idx < len(nums):
            return recursion(idx + 1, current_sum + nums[idx]) + recursion(idx + 1, current_sum - nums[idx])

        return current_sum == target

    return recursion(0,0)

if __name__ == "__main__":
    testcases = [
        (([1,1,1,1,1], 3), 5),
        (([1], 1), 1),
        (([42,16,31,11,36,19,9,3,25,0,27,29,35,29,45,15,35,42,35,23], 39), 6232)
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
