import sys

sys.path.append("..")

from typing import Tuple, List, Any

def fn(k: int) -> str:
    word = "a"

    while len(word) < k:

        for char in word:
            asci = ord(char) + 1

            if asci > 122:
                asci = 97

            word += chr(asci)

    return word[k - 1]


if __name__ == "__main__":
    testcases: List[Tuple[Any, str]] = [
        ((5, ), "b"),
        ((8, ), "d"),
        ((10, ), "c"),
        ((6, ), "c"),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)

