#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left_idx, acc, min_len = 0, 0, float("inf")

        for right_idx in range(len(nums)):
            acc += nums[right_idx]
            while acc >= target:
                min_len = min(min_len, right_idx - left_idx + 1)
                acc -= nums[left_idx]
                left_idx += 1

        return 0 if min_len == float("inf") else min_len


# @lc code=end

assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert Solution().minSubArrayLen(4, [1, 4, 4]) == 1
assert Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
