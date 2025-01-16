import sys

sys.path.append("..")

from typing import Tuple, List, Any


def fn(words: List[str], pref: str) -> int:
    sol = 0
    PREF_LEN = len(pref)

    for word in words:
        if len(word) < PREF_LEN:
            continue

        if pref == word[:PREF_LEN]:
            sol += 1

    return sol


def one_liner(words: List[str], pref: str) -> int:
    return sum(
        map(lambda word: len(word) >= len(pref) and pref == word[: len(pref)], words)
    )


if __name__ == "__main__":
    testcases: List[Tuple[Any, Any]] = [
        ((["pay", "attention", "practice", "attend"], "at"), 2),
        ((["leetcode", "win", "loops", "success"], "code"), 0),
        (
            (
                [
                    "jqclbnvrbpdivpsrnlziatmqxxezmcalpnzuczafqpdpdcyuckdddylevyemabynhxrvnjakjlsglcfnylldll",
                    "wzpsyqbydaaqyhjmbwfdvkgeyu",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmurkreyfyvraojedbdoxec",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmutmjfwmcammqvodenwxatsouojdgdpkxsabgve",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmuzsndtnkhdzrcgtkzeafa",
                    "cciaewsuyzccnzziczcmuaohsnudsuptlgrdzzryajluaxghxbwf",
                    "amtodzsovkmgdlw",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmuiqvnsluuynyblohrhhlqhakkcdabwklwsk",
                    "cqgytlphkffnmmmahesxelsicqyjyfullvymoqceemtnpyfgejcnabjeinljtfespnwvftldcholuujys",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmunyockixnilatozvfkyqpbzcfnkpexbghjsklu",
                    "wqhngwactepbsbmqahnjannhssnyazgbnrfygfqdpddqpotffkcgvepfmfmjvinpayfgkeimywrdfiisndvavkuuzdydvd",
                    "gtahklmdpknhtzdxfxherktwctnwvrjudmmtyqtqxohzeziimvbus",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmunbzcuaekqqhwozxdnldfb",
                    "egfkuytqptzqewpweeokurqmnqiyqdyeihucxzmgdu",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmutcgvtqoxgmwjmqdckyksnpgqbncsljzbpkpdy",
                    "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmuhzxpkltm",
                    "kbvytpxvmuojitddvttknckrtbxhkobijobcv",
                ],
                "kwrxrkemzzrftxzyxrnsiybqnlvmljljcpokfngosdyekhqaftmhjmixsytepmu",
            ),
            8,
        ),
    ]

    assert all(fn(*values) == expected for values, expected in testcases)
