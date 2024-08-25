# https://leetcode.com/problems/numbers-with-same-consecutive-differences/


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> list[int]:
        if n < 2 or n > 9:
            raise ValueError("n in [2,9]")

        if k < 0 or k > 9:
            raise ValueError("k in [0,9]")

        nums = []

        # base case
        base_case = int("".join([str(0) if i % 2 else str(k) for i in range(n)]))
        if k != 0:
            nums.append(base_case)

        sum_ammount = int("".join(["1" for _ in range(n)]))

        # All other cases
        for i in range(9 - k):
            # generate num
            num = base_case + (i + 1) * sum_ammount
            nums.append(num)

            if k == 0:
                continue

            # shift
            num = list(map(int, str(num)))
            nums.append(
                int(
                    "".join(
                        str(val) for val in ([num[-1 if n == 2 else -2]] + num[0:-1])
                    )
                )
            )
        return nums
