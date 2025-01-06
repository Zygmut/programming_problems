import sys

sys.path.append("..")

from typing import Tuple, List, Any, Set

def fn(boxes: str) -> List[int]:
    N = len(boxes)

    left = [0] * N
    ball_count = 0

    for idx in range(1, N):
        ball_count += (boxes[idx - 1] == '1')
        left[idx] = left[idx - 1] + ball_count

    ball_count = 0
    right = [0] * N

    for idx in range(N - 2, -1, -1):
        ball_count += (boxes[idx + 1] == '1')
        right[idx] = right[idx + 1] + ball_count

    return [ a + b for a, b in zip(left, right)]

if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (("110"), [1,1,3]),
        (("001011"), [11,8,5,4,3,4]),
    ]

    assert all(fn(values) == expected for values, expected in testcases)