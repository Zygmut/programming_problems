import sys

sys.path.append("..")

from typing import Tuple, List, Any
from functools import reduce

MOD = 1000000007


def fn(low: int, high: int, zero: int, one: int) -> int:
    memo = [0 for _ in range(high + 1)]
    memo[0] = 1

    for idx in range(1, high + 1):
        if idx >= zero:
            memo[idx] += memo[idx - zero]

        if idx >= one:
            memo[idx] += memo[idx - one]

        memo[idx] %= MOD

    return reduce(lambda acc, val: (acc + val) % MOD, memo[low : high + 1], 0)


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        ((3, 3, 1, 1), 8),
        ((2, 3, 1, 2), 5),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
