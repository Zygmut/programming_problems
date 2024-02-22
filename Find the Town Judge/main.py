def findJudge(n: int, trust: list[list[int]]) -> int:
    dp = [0] * (n + 1)

    for trusting, trusted in trust:
        dp[trusting] -= 1
        dp[trusted] += 1

    for idx in range(1, n + 1):
        if dp[idx] == (n - 1):
            return idx

    return -1


if __name__ == "__main__":
    testcases = [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
        (1, [], 1),
    ]

    assert all(findJudge(n, trust) == expected for n, trust, expected in testcases)
