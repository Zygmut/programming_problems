def truncate(string: str, k: int) -> str:
    return " ".join(string.split(" ")[:k])


assert "Hello how are you" == truncate("Hello how are you Contestant", 4)
assert "What is the solution" == truncate("What is the solution to this problem", 4)
assert "chopper is not a tanuki" == truncate("chopper is not a tanuki", 5)
