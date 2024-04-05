import sys

sys.path.append("..")

from typing import Tuple, List


def maxDepth(s: str) -> int:
    n_paren = 0
    sol = 0

    for character in s:
        if character == "(":
            n_paren += 1
            sol = max(sol, n_paren)
            continue

        if character == ")":
            n_paren -= 1

    return sol


if __name__ == "__main__":
    testcases: List[Tuple[str, int]] = [
        ("(1+(2*3)+((8)/4))+1", 3),
        ("(1)+((2))+(((3)))", 3),
    ]

    assert all(maxDepth(values) == expected for values, expected in testcases)
