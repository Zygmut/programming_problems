from dataclasses import dataclass
from typing import Any, Optional, Iterable, Generator
from functools import reduce


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


def listnode_from_iter(col: Iterable[Any]) -> Optional[ListNode]:
    if not col:
        return None

    return reduce(lambda acc, val: ListNode(val, acc), reversed(list(col)), None)


def listnode_iter(node: ListNode) -> Generator[Any, None, None]:
    head: Optional[ListNode] = node
    while head:
        yield head
        head = head.next


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
