from multiprocessing.sharedctypes import Value
from typing import List


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(values: tuple[int]) -> ListNode:
    """Creates a linked list given a tuple of integers

    Args:
        values (tuple[int]): Values to be inside the linked list

    Raises:
        ValueError: If necessary

    Returns:
        ListNode: Linked list with args values
    """


    if not isinstance(values, tuple):
        raise ValueError("Values need to be in a tuple")

    if len(values) == 0:
        raise ValueError("Tuple needs to have at least one value")

    if len(values) > 100:
        raise ValueError("Tuple length cannot exceed 100 values")

    listnode = ListNode()
    iter = listnode

    if not isinstance(values[0], int):
        raise ValueError("All values mustbe numeric")
    if values[0] < 0 or values[0] > 9:
        raise ValueError("Tuple can only contain values between 0 and 9. 0<=value<=9")
    iter.val = values[0]

    for value in values[1::]:
        if not isinstance(value, int):
            raise ValueError("All values mustbe numeric")
        if value < 0 or value > 9:
            raise ValueError(
                "Tuple can only contain values between 0 and 9. 0<=value<=9"
            )
        iter.next = ListNode()
        iter = iter.next
        iter.val = value

    return listnode


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not isinstance(l1, ListNode):
            raise ValueError("First parameter is not a ListNode object")

        if not isinstance(l2, ListNode):
            raise ValueError("Second parameter is not a ListNode object")

        result = ListNode()
        iter = result
        carry = 0

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            carry, out = divmod(val_1 + val_2 + carry, 10)

            iter.next = ListNode(out)
            iter = iter.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
