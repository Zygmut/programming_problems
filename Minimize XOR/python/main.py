from typing import Tuple, List, Any


def fn(num1: int, num2: int) -> int:

    diff = num2.bit_count() - num1.bit_count()

    if diff > 0:

        # replace 0 to 1 from the least significat bit from nb1 as many times as nb2 - nb1
        for _ in range(diff):
            num1 |= (num1 + 1)

    else:

        # Replace 1 to 0 from the least significant bit from nb1 as many times as nb1 - nb2
        for _ in range(-diff):
            num1 &= (num1 - 1)

    return num1

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
