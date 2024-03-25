import sys

sys.path.append("..")

from typing import Tuple, List
from collections import Counter


def findDuplicates(nums: List[int]) -> List[int]:
    return [num for num, freq in Counter(nums).items() if freq > 1]


if __name__ == "__main__":
    testcases: List[Tuple[List[int], List[int]]] = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 1, 2], [1]),
        ([3], []),
    ]

    assert all(findDuplicates(values) == expected for values, expected in testcases)
