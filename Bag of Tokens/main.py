from typing import List


def bagOfTokensScore(tokens: List[int], power: int) -> int:
    score = 0
    values = sorted(tokens)
    low, high = 0, len(values) - 1
    while low <= high:
        if values[low] <= power:
            power -= values[low]
            low += 1
            score += 1
        elif score and low != high:
            power += values[high]
            high -= 1
            score -= 1
        else:
            break

    return score


if __name__ == "__main__":
    testcases: List[tuple[List[int], int, int]] = [
        ([100], 50, 0),
        ([200, 100], 150, 1),
        ([100, 200, 300, 400], 200, 2),
    ]

    assert all(
        bagOfTokensScore(tokens, power) == expected
        for tokens, power, expected in testcases
    )
