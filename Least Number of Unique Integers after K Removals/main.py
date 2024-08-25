from collections import Counter


def findLeastNumOfUniqueInts(arr: list[int], k: int) -> int:
    freq_mat = Counter(arr)
    sorted_freq = sorted(freq_mat.items(), key=lambda x: x[1])

    for num, freq in sorted_freq:
        if k < freq:
            break

        k -= freq
        del freq_mat[num]

    return len(freq_mat)


def findLeastNumOfUniqueInts2(arr: list[int], k: int) -> int:
    freq_mat = Counter(arr)
    sorted_freq = sorted(freq_mat.items(), key=lambda x: x[1])

    tmp = []
    for key, value in sorted_freq:
        tmp.extend([key] * value)

    return len(set(tmp[k:]))


if __name__ == "__main__":
    testcases = (
        ([5, 5, 4], 1, 1),
        ([4, 3, 1, 1, 3, 3, 2], 3, 2),
        ([2, 4, 1, 8, 3, 5, 1, 3], 3, 3),
        (
            [
                24,
                119,
                157,
                446,
                251,
                117,
                22,
                168,
                374,
                373,
                323,
                311,
                441,
                213,
                120,
                412,
                200,
                236,
                328,
                24,
                164,
                104,
                331,
                32,
                19,
                223,
                89,
                114,
                152,
                82,
                456,
                381,
                355,
                343,
                157,
                245,
                443,
                368,
                229,
                49,
                82,
                16,
                373,
                142,
                240,
                125,
                8,
            ],
            41,
            3,
        ),
    )

    assert all(
        all(
            (
                findLeastNumOfUniqueInts(arr, k) == expected,
                findLeastNumOfUniqueInts2(arr, k) == expected,
            )
        )
        for arr, k, expected in testcases
    )
