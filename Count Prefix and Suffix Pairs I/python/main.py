import sys

sys.path.append("..")

from typing import Tuple, List, Any

def naive(words: List[str]) -> int:
    def isPrefixAndSuffix(a: str, b: str) -> bool:
        long_enough = len(b) >= len(a)
        prefix = b[:len(a)] == a
        sufix = b[-len(a):] == a

        return long_enough and prefix and sufix


    sol = 0
    for idx, word1 in enumerate(words):
        for word2 in words[idx + 1:]:
            sol += isPrefixAndSuffix(word1, word2)

    return sol

def naiveplus(words: List[str]) -> int:
    def isPrefixAndSuffix(a: str, b: str) -> bool:
        long_enough = len(b) >= len(a)
        prefix = b[:len(a)] == a
        sufix = b[-len(a):] == a

        return long_enough and prefix and sufix

    return sum(
        isPrefixAndSuffix(word1, word2)
        for idx, word1 in enumerate(words)
        for word2 in words[idx + 1:]
    )

def fn(words: List[str]) -> int:
        return sum(
            word2.startswith(word1) and word2.endswith(word1)
            for idx, word1 in enumerate(words)
            for word2 in words[idx + 1:]
        )

if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        (["a","aba","ababa","aa"], 4),
        (["pa","papa","ma","mama"], 2),
    ]

    assert all(fn(values) == expected for values, expected in testcases)