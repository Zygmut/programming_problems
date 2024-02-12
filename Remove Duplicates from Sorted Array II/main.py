def remove_duplicates(nums: list[int]) -> int:
    anchor = 1
    freq = 1

    for idx in range(1, len(nums)):
        if nums[idx] != nums[idx - 1]:
            freq = 1
        else:
            freq += 1

        if freq <= 2:
            nums[anchor] = nums[idx]
            anchor += 1

    return anchor