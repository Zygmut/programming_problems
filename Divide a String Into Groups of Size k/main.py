import sys

sys.path.append("..")

from typing import Tuple, List


def fn(s: str, k: int, fill: str) -> List[str]:
    res = [
        s[idx : idx+k]
        for idx in range(0, len(s), k)
    ]

    res[-1] += fill * (k - len(res[-1]))
    return res


if __name__ == "__main__":
    testcases: List[Tuple[Tuple[str, int, str], List[str]]] = [
        (("abcdefghi", 3, "x"), ["abc","def","ghi"]),
        (("abcdefghij", 3, "x"), ["abc","def","ghi", "jxx"]),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
