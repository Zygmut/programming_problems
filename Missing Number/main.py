def missingNumber(nums: list[int]) -> int:
    return ((len(nums) * (len(nums) + 1)) // 2) - sum(nums)


if __name__ == "__main__":
    testcases = (([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8))
    assert all(missingNumber(values) == expected for values, expected in testcases)
