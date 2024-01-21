/*
 * @lc app=leetcode id=2130 lang=csharp
 *
 * [2130] Maximum Twin Sum of a Linked List
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
using System;
using System.Collections.Generic;
public class Solution
{
	public int PairSum(ListNode head)
	{
		int maxPairSum = 0;
		Stack<int> nodeStack = new Stack<int>();
		ListNode slowPointer = head;
		ListNode fastPointer = head;

		// Get slowPointer to the midpoint of the linked list
		while (fastPointer.next.next != null)
		{
			nodeStack.Push(slowPointer.val);
			slowPointer = slowPointer.next;
			fastPointer = fastPointer.next.next;
		}
		nodeStack.Push(slowPointer.val);
		slowPointer = slowPointer.next;


		while (slowPointer != null)
		{
			maxPairSum = Math.Max(maxPairSum, slowPointer.val + nodeStack.Pop());
			slowPointer = slowPointer.next;
		}

		return maxPairSum;
	}
}
// @lc code=end

