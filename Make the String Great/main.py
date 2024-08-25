import sys

sys.path.append("..")

from typing import Tuple, List


def makeGood(s: str) -> str:
    stack: List[str] = []

    for character in s:
        if stack and abs(ord(stack[-1]) - ord(character)) == 32:
            stack.pop()
            continue

        stack.append(character)

    return "".join(stack)


if __name__ == "__main__":
    testcases: List[Tuple[str, str]] = [
        ("leEeetcode", "leetcode"),
        ("abBAcC", ""),
        ("pP", ""),
    ]

    assert all(makeGood(values) == expected for values, expected in testcases)
