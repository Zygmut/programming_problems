import sys

sys.path.append("..")

from typing import Tuple, List


def fn(values: List[int]) -> int:
    max_score: int = 0
    candidate: int = values[0]

    for idx in range(1, len(values)):
        max_score = max(max_score, candidate + values[idx]- idx)
        candidate = max(candidate, values[idx] + idx)

    return max_score

if __name__ == "__main__":
    testcases: List[Tuple[List[int], int]] = [
        ([8,1,5,2,6], 11),
        ([1,2], 2),
    ]

    assert all(fn(values) == expected for values, expected in testcases)
