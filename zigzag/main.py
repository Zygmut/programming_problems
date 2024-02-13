# https://www.geeksforgeeks.org/convert-array-into-zig-zag-fashion/


def is_zigzag(values: list[int]) -> bool:
    for idx in range(1, len(values)):
        if idx % 2 != 0:
            if values[idx] < values[idx - 1]:
                return False
        else:
            if values[idx] > values[idx - 1]:
                return False

    return True


def zigzag(values: list[int]) -> list[int]:
    tmp = sorted(values)

    for idx in range(2, len(values), 2):
        tmp[idx - 1], tmp[idx] = tmp[idx], tmp[idx - 1]

    return tmp


if __name__ == "__main__":
    assert all(map(is_zigzag, map(zigzag, ([4, 3, 6, 7, 5, 2, 1], [1, 4, 3, 2]))))
