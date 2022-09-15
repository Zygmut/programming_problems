# https://leetcode.com/problems/find-original-array-from-doubled-array/
from bisect import bisect_left


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if not (1 <= len(changed) <= 10**5):
            raise ValueError("Length of the array must be within [1, 10**5]")

        sol = []
        changed.sort()

        def binary_search(arr: list[int, ...], val: int) -> int | None:
            i = bisect_left(arr, val)
            if i != len(arr) and arr[i] == val:
                return i
            else:
                return None

        while changed:

            val = changed.pop(0)
            if not (0 <= val <= 10**5):
                raise ValueError("Values of the array must be within [0, 10**5]")

            loc = binary_search(changed, val * 2)
            if loc is not None:
                sol.append(val)
                changed.pop(loc)
            else:
                return []
        return sol
