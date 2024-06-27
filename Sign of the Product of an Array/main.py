class Solution:

    def arraySign(self, nums: List[int]) -> int:
        POSITIVE = 1
        NEGATIVE = -1

        def sign_func(num: int) -> int:
            return 0 if num == 0 else POSITIVE if num > 0 else NEGATIVE

        return functools.reduce(lambda acc, next: acc * sign_func(next), nums, POSITIVE)
