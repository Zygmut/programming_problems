import sys

sys.path.append("..")

from typing import Tuple, List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    sol: List[List[int]] = []
    idx = 0
    N = len(intervals)

    # Move up to the newInterval range
    while idx < N and intervals[idx][1] < newInterval[0]:
        sol.append(intervals[idx])
        idx += 1

    # Colapse / merge the intersection with newInterval
    while idx < N and intervals[idx][0] <= newInterval[1]:
        newInterval = [
            min(intervals[idx][0], newInterval[0]),
            max(intervals[idx][1], newInterval[1]),
        ]
        idx += 1

    sol.append(newInterval)

    # Add the remaining elements to the array
    sol.extend(intervals[idx:])

    return sol


def insert2(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res: List[List[int]] = []

    for idx, (left, right) in enumerate(intervals):
        if left > newInterval[1]:
            # Next values cannot be merged. Add the remaining elements to it
            res.append(newInterval)
            return res + intervals[idx:]

        if right < newInterval[0]:
            # Not yet on the domain of values of newInterval
            res.append([left, right])
        else:
            # Merge tuples that maximize domain length
            newInterval = [min(newInterval[0], left), max(newInterval[1], right)]

    res.append(newInterval)
    return res


if __name__ == "__main__":
    testcases: List[Tuple[List[List[int]], List[int], List[List[int]]]] = [
        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]],
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
    ]

    assert all(
        all(
            (
                insert(values, new) == expected,
                insert2(values, new) == expected,
            )
        )
        for values, new, expected in testcases
    )
