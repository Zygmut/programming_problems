from dataclasses import dataclass
from typing import Any, Optional, Iterable, Generator, List
from functools import reduce


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    @staticmethod
    def from_list(values: List[Any]) -> Optional["TreeNode"]:
        if not values:
            return None

        LEN = len(values)

        def rec(idx: int) -> Optional["TreeNode"]:
            if idx >= LEN:
                return None

            if not values[idx]:
                return None

            return TreeNode(values[idx], rec(2 * idx + 1), rec(2 * idx + 2))

        return rec(0)


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
