from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left_heap = costs[:candidates]
        left_threshold: int = candidates
        heapify(left_heap)

        right_heap = costs[max(candidates, len(costs) - candidates) :]
        right_threshold: int = len(costs) - candidates - 1
        heapify(right_heap)

        sol: int = 0

        for _ in range(k):
            if not right_heap or left_heap and left_heap[0] <= right_heap[0]:
                sol += heappop(left_heap)
                if left_threshold <= right_threshold:
                    heappush(left_heap, costs[left_threshold])
                    left_threshold += 1
            else:
                sol += heappop(right_heap)
                if left_threshold <= right_threshold:
                    heappush(right_heap, costs[right_threshold])
                    right_threshold -= 1
        return sol
