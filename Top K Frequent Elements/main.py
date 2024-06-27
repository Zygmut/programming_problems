class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [
            pair[0]
            for pair in sorted(list(Counter(nums).items()), key=lambda x: -x[1])[:k]
        ]
