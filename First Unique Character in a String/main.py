import sys

sys.path.append("..")

from typing import List, Tuple
from collections import Counter


def firstUniqChar(s: str) -> int:
    freq = Counter(s)
    for idx, c in enumerate(s):
        if freq.get(c) == 1:
            return idx

    return -1


def firstUniqCharGen(s: str) -> int:
    freq = Counter(s)
    return next((idx for idx, c in enumerate(s) if freq.get(c) == 1), -1)


if __name__ == "__main__":
    testcases: List[Tuple[str, int]] = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
    ]

    assert all(
        all(fn(s) == expected for fn in [firstUniqChar, firstUniqCharGen])
        for s, expected in testcases
    )
