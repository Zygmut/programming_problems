import sys

sys.path.append("..")

from typing import List, Tuple, Optional
from modules.data import ListNode, listnode_from_iter


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = slow = head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next  # type: ignore

    return slow


if __name__ == "__main__":
    testcases: List[Tuple[Optional[ListNode], Optional[ListNode]]] = [
        (listnode_from_iter([1, 2, 3, 4, 5]), listnode_from_iter([3, 4, 5])),
        (listnode_from_iter([1, 2, 3, 4, 5, 6]), listnode_from_iter([4, 5, 6])),
    ]
    assert all(middleNode(llist) == expected for llist, expected in testcases)
