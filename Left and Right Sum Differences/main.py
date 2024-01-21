from typing import List
from itertools import accumulate
from operator import add


def shift(arr: List, n: int, default=0):
    return [default] * n + arr[:-n]


def left_right_diff(nums: List[int]) -> List[int]:
    gen_list = list(map(lambda x: shift(list(accumulate(x)), 1), [nums, nums[::-1]]))
    return [abs(a - b) for a, b in zip(gen_list[0], reversed(gen_list[1]))]


assert left_right_diff([10, 4, 8, 3]) == [15, 1, 11, 22]
assert left_right_diff([1]) == [0]
