from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return max(freq, key=freq.get)
