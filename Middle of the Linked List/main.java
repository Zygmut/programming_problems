public ListNode middleNode(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while (fast != null) {
        fast = fast.next;
        if (fast != null){
            slow = slow.next;
            fast = fast.next;
        }
    }

    return slow;
}
