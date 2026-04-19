# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head  # Initialize two pointers

        while fast and fast.next:
            slow = slow.next            # Move slow by 1
            fast = fast.next.next       # Move fast by 2

            if slow == fast:
                return True             # Cycle detected

        return False                    # No cycle
