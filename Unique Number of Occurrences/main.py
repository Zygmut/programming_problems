import sys

sys.path.append("..")

from collections import Counter
from typing import Tuple, List, Any


def uniqueOccurrences(arr: List[int]) -> bool:
    freq = Counter(arr)
    return len(set(freq.values())) == len(freq.values())


if __name__ == "__main__":
    testcases: List[Tuple[List[Any], bool]] = [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ]

    assert all(uniqueOccurrences(values) == expected for values, expected in testcases)
