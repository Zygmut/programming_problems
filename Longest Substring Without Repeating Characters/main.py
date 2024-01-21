# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not isinstance(s, str):
            raise ValueError("s must be a string")

        if len(s) > 5 * 104:
            raise ValueError("s must have a maximum length of 5*104")

        sol = 0
        used_chars = {}
        left = 0

        for right, char in enumerate(s):
            if char in used_chars:
                left = max(used_chars[char], left)

            sol = max(sol, right - left + 1)
            used_chars[char] = right + 1
        return sol
