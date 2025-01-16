import sys

sys.path.append("..")

from typing import Tuple, List, Any
from collections import Counter


def fn(words1: List[str], words2: List[str]) -> List[str]:
    sol = []

    letter_freq: dict[str, int] = dict({})

    for word in words2:
        for letter, freq in Counter(word).items():
            letter_freq[letter] = max(letter_freq.get(letter, 0), freq)

    for word in words1:
        word_counter = Counter(word)

        if all(
            word_counter.get(letter, None) and word_counter[letter] >= freq
            for letter, freq in letter_freq.items()
        ):
            sol.append(word)

    return sol


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (
            (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]),
            ["facebook", "google", "leetcode"],
        ),
        (
            (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]),
            ["apple", "google", "leetcode"],
        ),
        (
            (["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"]),
            ["google", "leetcode"],
        ),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
