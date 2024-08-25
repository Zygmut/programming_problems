def buddyStrings(s: str, goal: str) -> bool:
    if s == goal:
        return len(set(s)) < len(goal)

    n = len(s)

    # Start a pointer from the start
    i = 0
    while i < n and s[i] == goal[i]:
        i += 1

    # Start a pointer from the end
    j = n - 1
    while j >= 0 and s[j] == goal[j]:
        j -= 1

    # Check if j found another change different than i
    if i < j:
        tmp = list(s)
        tmp[i], tmp[j] = tmp[j], tmp[i]
        s = "".join(tmp)

    return s == goal


assert buddyStrings("ab", "ba")
assert not buddyStrings("ab", "ab")
assert buddyStrings("aa", "aa")
