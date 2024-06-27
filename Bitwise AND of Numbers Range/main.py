def rangeBitwiseAnd(left: int, right: int) -> int:
    while right > left:
        right &= right - 1

    return right


def rangeBitwiseAnd2(left: int, right: int) -> int:
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    return left << shift


if __name__ == "__main__":
    testcases = [
        (5, 7, 4),
        (0, 0, 0),
        (600000000, 2147483645, 0),
    ]

    assert all(
        all(
            (
                rangeBitwiseAnd(left, right) == expected,
                rangeBitwiseAnd2(left, right) == expected,
            )
        )
        for left, right, expected in testcases
    )
