import sys

sys.path.append("..")

from typing import Tuple, List, Dict


def findDuplicate(nums: List[int]) -> int:
    counter: Dict[int, int] = {}

    for num in nums:
        counter_val = counter.get(num, 0)

        if counter_val != 0:
            return num

        counter[num] = 1

    # This cannot be possible as per problem restrictions
    return -1


if __name__ == "__main__":
    testcases: List[Tuple[List[int], int]] = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),
    ]

    assert all(findDuplicate(values) == expected for values, expected in testcases)
