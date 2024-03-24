import sys

sys.path.append("..")

from typing import Tuple, List, Any


def fn(n: int):
    return n


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (1, 1),
    ]

    assert all(fn(values) == expected for values, expected in testcases)
