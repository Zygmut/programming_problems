def fizz_buzz(
    n,
    conditions: list = [(lambda x: x % 3 == 0, "Fizz"), (lambda x: x % 5 == 0, "Buzz")],
):
    for i in range(1, n + 1):
        tmp = ""

        for cause, effect in conditions:
            if cause(i) == True:
                tmp += effect

        if not tmp:
            tmp += str(i)

        yield tmp


if __name__ == "__main__":
    assert (
        ", ".join(fizz_buzz(35))
        == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz"
    )
