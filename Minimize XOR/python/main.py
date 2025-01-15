from typing import Tuple, List, Any
from functools import reduce


def fn(num1: int, num2: int) -> int:
    diff = num2.bit_count() - num1.bit_count()

    if diff == 0:
        return num1

    if diff > 0:
        # replace 0 to 1 from the least significat bit from nb1 as many times as nb2 - nb1
        return reduce(lambda acc, _: acc | acc + 1, range(diff), num1)

    # Replace 1 to 0 from the least significant bit from nb1 as many times as nb1 - nb2
    return reduce(lambda acc, _: acc & acc - 1, range(-diff), num1)


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (
            (
                3,
                5,
            ),
            3,
        ),
        (
            (
                1,
                12,
            ),
            3,
        ),
        (
            (
                12,
                1,
            ),
            8,
        ),
        (
            (
                25,
                72,
            ),
            24,
        ),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
