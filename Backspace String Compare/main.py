import sys
sys.path.append("..")

from typing import List, Tuple

def backspaceCompare(s: str, t: str) -> bool:
    def _trim(s: str) -> str:
        stack = ""
        for c in s:
            if c != "#":
                stack += c
                continue

            if stack:
                stack = stack[:-1]

        return stack

    return _trim(s) == _trim(t)

if __name__ == "__main__":
    testcases: List[Tuple[str,str, bool]]= [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a#c", "b", False),
    ]

    assert all(
        backspaceCompare(s,t) == expected
        for s, t, expected in testcases
    )