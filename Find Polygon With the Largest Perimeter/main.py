from itertools import accumulate


def largestPerimeter1(nums: list[int] | tuple[int, ...]) -> int:
    sol = -1
    tmp = sorted(nums)
    cumm_sum = list(accumulate(tmp))

    for idx in reversed(range(len(tmp))):
        if idx < 2:
            break

        # this CANNOT go out of bounds as we early stop when there are at least
        # two more items
        if tmp[idx] < cumm_sum[idx - 1]:
            sol = cumm_sum[idx]
            break

    return sol


def largestPerimeter2(nums: list[int] | tuple[int, ...]) -> int:
    sol = -1
    tmp = reversed(sorted(nums))
    summatory = sum(nums)

    for num in tmp:
        summatory -= num

        if num < summatory:
            sol = summatory + num
            break

    return sol


if __name__ == "__main__":
    testcases = {(5, 5, 5): 15, (1, 12, 1, 2, 5, 50, 3): 12, (5, 5, 50): -1}

    assert all(
        next(iter(set((largestPerimeter1(values), largestPerimeter2(values)))))
        == expected
        for values, expected in testcases.items()
    )
