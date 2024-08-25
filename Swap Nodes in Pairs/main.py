from typing import Optional
import sys

sys.path.append("..")

from modules.data import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node: ListNode = head

        while current_node and current_node.next:
            current_node.val, current_node.next.val = (
                current_node.next.val,
                current_node.val,
            )

            current_node = current_node.next.next

        return head
