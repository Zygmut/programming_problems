from typing import Tuple, List, Any


def fn(A: List[int], B: List[int]) -> List[int]:
    sol = [0] * len(A)
    freq = [0] * (len(A) + 1)

    for idx, (a, b) in enumerate(zip(A, B)):
        freq[a] += 1
        if freq[a] == 2:
            sol[idx] += 1

        freq[b] += 1
        if freq[b] == 2:
            sol[idx] += 1

        sol[idx] += sol[idx - 1] if idx > 0 else 0

    return sol


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (
            (
                [1, 3, 2, 4],
                [3, 1, 2, 4],
            ),
            [0, 2, 3, 4],
        ),
        (
            (
                [2, 3, 1],
                [3, 1, 2],
            ),
            [0, 1, 3],
        ),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
