import sys

sys.path.append("..")

from typing import Tuple, List, Any, Dict


def fn(s: str) -> int:
    isEven: Dict[str, bool] = {}

    for char in s:
        isEven[char] = not isEven.get(char, True)

    return len(isEven) + sum(isEven.values())


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (("abaacbcbb",), 5),
        (("aa",), 2),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
