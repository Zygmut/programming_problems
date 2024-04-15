def longestConsecutive(self, nums: List[int]) -> int:
    num_set = set(nums)
    length = 0
    for start in num_set:
        if start - 1 in num_set:
            continue

        end = start + 1

        while end in num_set:
            end += 1

        length = max(length, end - start)

    return length        
