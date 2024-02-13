#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


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


# @lc code=end
