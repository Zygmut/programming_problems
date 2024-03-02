def sortedSquares(nums: list[int]) -> list[int]:
    return sorted([num**2 for num in nums])

if __name__ == "__main__":
    testcases: list[tuple[list[int], list[int]]] = [
        ([-4,-1,0,3,10],[0,1,9,16,100]),
        ([-7,-3,2,3,11], [4,9,9,49,121]),
    ]

    assert all(
        sortedSquares(nums) == expected
        for nums, expected in testcases
    )