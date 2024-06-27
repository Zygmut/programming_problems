# https://leetcode.com/problems/find-original-array-from-doubled-array/


class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if not (1 <= len(changed) <= 10**5):
            raise ValueError("Length of the array must be within [1, 10**5]")

        if len(changed) % 2:
            return []

        sol = []
        changed.sort(reverse=True)

        def rev_binary_search(arr: list[int], val: int) -> int | None:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                # change arr[mid] < val to ">" to port func to reverse ordered arrays
                if arr[mid] > val:
                    lo = mid + 1
                else:
                    hi = mid

            if lo != len(arr) and arr[lo] == val:
                return lo
            else:
                return None

        while changed:
            val = changed.pop()

            if not (0 <= val <= 10**5):
                raise ValueError("Values of the array must be within [0, 10**5]")

            loc = rev_binary_search(changed, val * 2)

            if loc is not None:
                sol.append(val)
                changed.pop(loc)
            else:
                return []

        return sol
