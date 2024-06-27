def isValid(s: str) -> bool:
    match_map = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in s:
        if char in match_map.values():
            stack.append(char)
            continue

        if stack and stack[-1] == match_map.get(char, None):
            stack.pop()
        else:
            return False

    return not stack


if __name__ == "__main__":
    assert all(
        [
            isValid(value) == expected
            for value, expected in (
                ("()", True),
                ("()[]{}", True),
                ("(]", False),
                (")[", False),
                ("(([{}])([]))", True),
            )
        ]
    )
