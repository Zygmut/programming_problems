import sys

sys.path.append("..")

from typing import Tuple, List, Any


def fn(days: List[int], costs: List[int]) -> int:
    memo = [0] * (days[-1] + 1)
    travel_days = set(days)

    for day in range(1, len(memo)):
        if day not in travel_days:
            memo[day] = memo[day - 1]
            continue

        memo[day] = min(
            memo[day - 1] + costs[0],
            memo[max(0, day - 7)] + costs[1],
            memo[max(0, day - 30)] + costs[2],
        )

    return int(memo[-1])


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (([1, 4, 6, 7, 8, 20], [2, 7, 15]), 11),
        (([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]), 17),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
