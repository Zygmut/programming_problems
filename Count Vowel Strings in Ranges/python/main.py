import sys

sys.path.append("..")

from typing import Tuple, List, Any, Set
from itertools import accumulate

VOWELS: Set[str] = {"a", "e", "i", "o", "u"}


def isValid(string: str) -> bool:
    return string[0] in VOWELS and string[-1] in VOWELS


def fn(words: List[str], queries: List[List[int]]) -> List[int]:
    prefix = [0] + list(accumulate(map(int, map(isValid, words))))

    return [prefix[query[1] + 1] - prefix[query[0]] for query in queries]


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        ((["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]), [2, 3, 0]),
        ((["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]), [3, 2, 1]),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
