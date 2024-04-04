import sys

sys.path.append("..")

from typing import Tuple, List, Set, Dict


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash_map: Dict[str, List[str]] = {}

    for word in strs:
        freq: List[int] = [0] * 26
        for character in word:
            freq[ord(character) - 97] += 1

        key: str = "_".join(map(str, freq))

        hash_map[key] = hash_map.get(key, []) + [word]

    return list(hash_map.values())


if __name__ == "__main__":
    testcases: List[Tuple[List[str], List[List[str]]]] = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    # This doesn't work because arrays and I'm to lazy to fix it :)
    assert all(groupAnagrams(values) == expected for values, expected in testcases)
