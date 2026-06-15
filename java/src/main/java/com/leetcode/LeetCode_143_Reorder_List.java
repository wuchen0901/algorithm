package com.leetcode;

import com.leetcode.common.ListNode;

public class LeetCode_143_Reorder_List {
    public void reorderList(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        // 1 2 3
        //   s f

        // 1 2 3 4
        //     s   f

        // 1 2 3 4 5
        //     s   f

        // Then I split the list into two parts at the slow pointer.
        ListNode list1 = head;
        ListNode list2 = slow.next;
        slow.next = null;

        // Next, I reverse the second half of the list.
        ListNode prev = null;
        ListNode curr = list2;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        list2 = prev;

        // Finally, I merge the two lists.
        ListNode dummy = new ListNode();
        ListNode pointer = dummy;

        while (list1 != null && list2 != null) {
            pointer.next = list1;
            pointer = pointer.next;
            list1 = list1.next;
            pointer.next = list2;
            pointer = pointer.next;
            list2 = list2.next;
        }

        pointer.next = (list1 == null) ? list2 : list1;
    }
}
