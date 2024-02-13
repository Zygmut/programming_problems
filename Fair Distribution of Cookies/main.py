#
# @lc app=leetcode id=2305 lang=python3
#
# [2305] Fair Distribution of Cookies
#


# @lc code=start
class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        min_unfair: int = 800001
        dist: list[int, ...] = [0 for _ in range(k)]

        def back(curr_cookie_index: int):
            nonlocal min_unfair, dist

            if curr_cookie_index == len(cookies):
                min_unfair = min(min_unfair, max(dist))
                return

            if min_unfair <= max(dist):
                return

            for j in range(k):
                dist[j] += cookies[curr_cookie_index]
                back(curr_cookie_index + 1)
                dist[j] -= cookies[curr_cookie_index]

        cookies.sort(reverse=True)
        back(0)
        return min_unfair


# @lc code=end

assert Solution().distributeCookies([8, 15, 10, 20, 8], 2) == 31
assert Solution().distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3) == 7
