package com.leetcode;

import com.leetcode.common.ListNode;
import org.w3c.dom.NodeList;

/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
public class LeetCode_143_Reorder_List {
    // Time complexity: O(n) — finding the middle, reversing the second half, and merging each take O(n). Sequential operations add: O(n) + O(n) + O(n) = O(n).
    // Auxiliary space: O(1) — you only use a fixed number of pointers and modify the list in place.
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
        while (list1 != null && list2 != null) {
            ListNode next1 = list1.next;
            ListNode next2 = list2.next;
            list1.next = list2;
            list1 = next1;
            list2.next = list1;
            list2 = next2;
        }
    }
}
