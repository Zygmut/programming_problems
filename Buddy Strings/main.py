#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#


# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            return len(set(s)) < len(goal)

        n = len(s)

        # Start a pointer from the start
        i = 0
        while i < n and s[i] == goal[i]:
            i += 1

        # Start a pointer from the end
        j = n - 1
        while j >= 0 and s[j] == goal[j]:
            j -= 1

        # Check if j found another change different than i
        if i < j:
            tmp = list(s)
            tmp[i], tmp[j] = tmp[j], tmp[i]
            s = "".join(tmp)

        return s == goal


# @lc code=end

assert Solution().buddyStrings("ab", "ba") == True
assert Solution().buddyStrings("ab", "ab") == False
assert Solution().buddyStrings("aa", "aa") == True
