#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result: str = ""
        carry: bool = False
        iter_a, iter_b = len(a) - 1, len(b) - 1

        while iter_a >= 0 or iter_b >= 0:
            sum = carry

            if iter_a >= 0:
                sum += ord(a[iter_a]) - ord("0")
            if iter_b >= 0:
                sum += ord(b[iter_b]) - ord("0")

            carry = sum > 1
            iter_a, iter_b = iter_a - 1, iter_b - 1

            result += str(sum % 2)

        if carry:
            result += "1"
        return result[::-1]


# @lc code=end
