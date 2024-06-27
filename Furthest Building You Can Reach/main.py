from heapq import heappop, heappush


def furthestBuilding(heights: list[int], bricks: int, ladders: int) -> int:
    brick_history: list[int] = []
    tmp_bricks = bricks
    tmp_ladders = ladders

    for idx in range(1, len(heights)):
        height_diff = heights[idx] - heights[idx - 1]

        if height_diff <= 0:
            continue

        heappush(brick_history, -height_diff)
        tmp_bricks -= height_diff

        if tmp_bricks < 0:
            tmp_ladders -= 1
            tmp_bricks -= heappop(brick_history)

        if tmp_ladders < 0:
            return idx - 1

    return len(heights) - 1


if __name__ == "__main__":
    testcases = [
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([14, 3, 19, 3], 17, 0, 3),
    ]

    assert all(
        furthestBuilding(heights, bricks, ladders) == expected
        for heights, bricks, ladders, expected in testcases
    )
