import sys

sys.path.append("..")

from typing import Tuple, List, Dict


def maxSubarrayLength(nums: List[int], k: int) -> int:
    freq: Dict[int, int] = {}
    sol = 0
    left = right = 0
    N = len(nums)

    while right < N:
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        # We overshoot this item, so we move the left index untill we no longer overshoot
        # This is the left pointer controller
        while freq[nums[right]] > k:
            freq[nums[left]] -= 1
            left += 1

        right += 1

        sol = max(sol, right - left)

    return sol


if __name__ == "__main__":
    testcases: List[Tuple[List[int], int, int]] = [
        ([1, 2, 3, 1, 2, 3, 1, 2], 2, 6),
        ([1, 2, 1, 2, 1, 2, 1, 2], 1, 2),
        ([5, 5, 5, 5, 5, 5, 5], 4, 4),
        ([1, 11], 2, 2),
        ([1], 1, 1),
    ]

    assert all(
        maxSubarrayLength(nums, k) == expected for nums, k, expected in testcases
    )
