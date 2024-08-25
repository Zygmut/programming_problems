import sys

sys.path.append("..")

from modules.data import ListNode


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
