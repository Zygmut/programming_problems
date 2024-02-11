def fibonacci(n):
    tmp1, tmp2 = 0, 1

    yield tmp2

    for _ in range(n):
        tmp1, tmp2 = tmp2, tmp1 + tmp2
        yield tmp2


if __name__ == "__main__":
    assert (
        ", ".join(map(str, fibonacci(11)))
        == "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144"
    )
