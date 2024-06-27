def rearrange(values: list[int]) -> list[int]:
    positive_numbers = filter(lambda item: item > 0, values)
    negative_numbers = filter(lambda item: item < 0, values)

    return [
        next(positive_numbers) if idx % 2 == 0 else next(negative_numbers)
        for idx in range(len(values))
    ]


if __name__ == "__main__":
    assert all(
        rearrange(values) == expected
        for values, expected in (
            ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
            ([-1, 1], [1, -1]),
        )
    )
