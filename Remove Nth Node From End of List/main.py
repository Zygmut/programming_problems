import sys
sys.path.append("..")

from typing import Optional, Generator
from modules.data import ListNode, iter_to_ln

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def _iter(head: Optional[ListNode]) -> Generator[int, None, None]:
        node = head
        while node:
            yield node.val
            node = node.next

    if not head:
        return None

    node = None
    for idx, val in enumerate(reversed(list(_iter(head)))):
        if idx == (n - 1):
            continue

        node = ListNode(val, node)

    return node

if __name__ == "__main__":
    testcases: list[tuple[ListNode, int, ListNode]] = [
        (iter_to_ln([1,2,3,4,5]), 2, iter_to_ln([1,2,3,5])), # type: ignore
        (iter_to_ln([1]), 1, iter_to_ln([])), # type: ignore
        (iter_to_ln([1,2]), 1, iter_to_ln([1])), # type: ignore
    ]

    assert all(
        removeNthFromEnd(head, n) == expected
        for head, n, expected in testcases
    )