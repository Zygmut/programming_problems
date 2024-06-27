def rotate(nums: list[int], k: int):
    k = k % len(nums)
    return [nums[idx] for idx in range(-k, len(nums) - k)]


if __name__ == "__main__":
    assert all(
        map(
            lambda values: rotate(values[0], values[1]) == values[2],
            (
                ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
                ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
                ([1], 0, [1]),
                ([1, 2], 0, [1, 2]),
                ([-1], 2, [-1]),
            ),
        )
    )
