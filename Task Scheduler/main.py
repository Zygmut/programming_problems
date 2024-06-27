import sys

sys.path.append("..")

from typing import Tuple, List
from collections import Counter


def leastInterval(tasks: List[str], n: int) -> int:
    freqs = tuple(Counter(tasks).values())
    max_freq: int = max(freqs)
    max_val_count: int = sum([1 for freq in freqs if freq == max_freq])

    # hypotesis
    interval_len: int = (max_freq - 1) * (n + 1) + max_val_count

    return max(interval_len, len(tasks))


if __name__ == "__main__":
    testcases: List[Tuple[List[str], int, int]] = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "C", "A", "B", "D", "B"], 1, 6),
        (["A", "A", "A", "B", "B", "B"], 3, 10),
    ]

    assert all(
        leastInterval(tasks, cooldown) == expected
        for tasks, cooldown, expected in testcases
    )
