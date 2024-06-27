import sys

sys.path.append("..")

from typing import Tuple, List


def minRemoveToMakeValid(s: str) -> str:
    sol: List[str] = []
    paren_pos: List[int] = []

    for idx, character in enumerate(s):
        if character == "(":
            paren_pos.append(idx)
            sol.append("(")
            continue

        if character == ")":
            if paren_pos:
                paren_pos.pop()
                sol.append(")")
            continue

        sol.append(character)

    for unmatched_paren in paren_pos:
        sol.pop(unmatched_paren)

    return "".join(sol)


if __name__ == "__main__":
    testcases: List[Tuple[str, str]] = [
        ("lee(t(c)o)de)", "lee(t(c)o)de"),
        ("a)b(c)d", "ab(c)d"),
        ("))((", ""),
    ]

    assert all(
        minRemoveToMakeValid(values) == expected for values, expected in testcases
    )
