from typing import Tuple, List, Any
from functools import reduce


def f(derived: List[int]) -> bool:
    return reduce(lambda acc, val: acc ^ val, derived) == 0


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (
            ([1, 1, 0],),
            True,
        ),
        (
            ([1, 1],),
            True,
        ),
        (
            ([1, 0],),
            False,
        ),
    ]

    for idx, (values, expected) in enumerate(testcases):
        result = f(*values)

        if result != expected:
            print(f"Failed Test {idx}")
            print(f"Got      {result}")
            print(f"Expected {expected}")
            print()
