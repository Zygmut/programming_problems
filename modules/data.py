from dataclasses import dataclass
from typing import Any, Optional, Iterable, Generator
from functools import reduce

@dataclass
class ListNode:
    val: int = 0
    next: Optional['ListNode'] = None

def iter_to_ln(col: Iterable[Any]) -> Optional[ListNode]:
    if not col:
        return None

    return reduce(lambda acc, val: ListNode(val, acc), reversed(list(col)), None)

def ln_iter(head: ListNode) -> Generator[int, None, None]:
    node: Optional[ListNode] = head

    while node:
        yield node.val
        node = node.next

@dataclass
class KListNode(ListNode):
    @staticmethod
    def from_iterable(col: Iterable[Any]) -> Optional[ListNode]:
        if not col:
            return None

        return reduce(lambda acc, val: ListNode(val, acc), reversed(list(col)), None)

    def __iter__(self) -> Any:
        node: Optional[ListNode] = self
        while node:
            yield node.val
            node = node.next

    def __str__(self) -> str:
        return str(list(self))
