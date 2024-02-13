def firstPalindrome(words: list[str]) -> str:
    return next(filter(lambda word: word == word[::-1], words), "")


if __name__ == "__main__":
    assert all(
        (
            firstPalindrome(words) == expected
            for words, expected in (
                (["abc", "car", "ada", "racecar", "cool"], "ada"),
                (["notapalindrome", "racecar"], "racecar"),
                (["def", "ghi"], ""),
            )
        )
    )
