class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles edge cases like removing the head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right pointer n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Skip the nth node from the end
        left.next = left.next.next

        # Return the updated list starting from dummy.next
        return dummy.next
