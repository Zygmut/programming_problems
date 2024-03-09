import sys

sys.path.append("..")

from typing import Tuple, List
from collections import Counter


def maxFrequencyElements(nums: List[int]) -> int:
    freqs = list(Counter(nums).values())
    max_val = max(freqs)
    return max_val * freqs.count(max_val)


if __name__ == "__main__":
    testcases: List[Tuple[List[int], int]] = [
        ([1, 2, 2, 3, 1, 4], 4),
        ([1, 2, 3, 4, 5], 5),
    ]

    assert all(
        maxFrequencyElements(values) == expected for values, expected in testcases
    )
