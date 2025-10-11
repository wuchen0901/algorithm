# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break
        else:
            return None

        # Move one pointer to head, keep the other at meeting point.
        # They will meet at the cycle start.
        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
