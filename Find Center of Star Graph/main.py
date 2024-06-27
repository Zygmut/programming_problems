from typing import List
from collections import Counter
from functools import reduce
from operator import iconcat

def findCenter1(edges: List[List[int]]) -> int:
    if edges[0][0] in (edges[1]):
        return edges[0][0]
    return edges[0][1]

def findCenter2(edges: List[List[int]]) -> int:
    freq: Counter = Counter(reduce(iconcat, edges, []))
    center_item: int= max(list(freq.items()), key=lambda x: x[1])[0]
    return center_item