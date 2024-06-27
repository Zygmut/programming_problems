def isPowerOfTwo(n: int) -> bool:
    return n != 0 and not (n & n - 1)


if __name__ == "__main__":
    testcases = [
        (1, True),
        (16, True),
        (3, False),
    ]

    assert all(isPowerOfTwo(n) == expected for n, expected in testcases)
