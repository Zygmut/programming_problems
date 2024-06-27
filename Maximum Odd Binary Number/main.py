def maximumOddBinaryNumber(s: str) -> str:
    return "1" * (s.count("1") - 1) + "0" * s.count("0") + "1"


if __name__ == "__main__":
    testcases: list[tuple[str, str]] = [
        ("010", "001"),
        ("0101", "1001"),
    ]

    assert all(maximumOddBinaryNumber(num) == expected for num, expected in testcases)
