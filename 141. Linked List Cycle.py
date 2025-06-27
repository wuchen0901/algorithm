# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's Cycle Detection Algorithm:
        # Use two pointers: slow moves one step at a time, fast moves two steps.
        # If there is a cycle, the fast pointer will eventually meet the slow pointer.
        # If there is no cycle, the fast pointer will reach the end (None).

        fast = head
        slow = head
        while True:
            for _ in range(2):
                if fast is None:
                    return False
                fast = fast.next

            slow = slow.next
            if fast == slow:
                return True
