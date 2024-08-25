from typing import List
from collections import Counter


def topKFrequent(nums: List[int], k: int) -> List[int]:
    return [
        pair[0] for pair in sorted(list(Counter(nums).items()), key=lambda x: -x[1])[:k]
    ]
