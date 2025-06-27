# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        # Fast pointer moves two steps at a time.
        # Slow pointer moves one step at a time.
        # When fast reaches the end, slow will be in the middle.
        # This ensures the correct result for both even and odd-length lists.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
