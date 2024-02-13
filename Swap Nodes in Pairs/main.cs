/*
 * @lc app=leetcode id=24 lang=csharp
 *
 * [24] Swap Nodes in Pairs
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode SwapPairs(ListNode head) {

	    ListNode iterator = head;
		int swap_tmp;

		while(iterator != null && iterator.next != null){
			swap_tmp = iterator.val;
			iterator.val = iterator.next.val;
			iterator.next.val = swap_tmp;

			iterator = iterator.next.next;
		}
    }
}
// @lc code=end
