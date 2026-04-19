class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to anchor the result list
        cur = dummy
        carry = 0

        while l1 or l2 or carry:  # Continue while nodes remain or carry exists
            v1 = l1.val if l1 else 0  # Get value from l1 or 0 if null
            v2 = l2.val if l2 else 0  # Get value from l2 or 0 if null

            val = v1 + v2 + carry     # Sum the digits and carry
            carry = val // 10         # Update carry for next digit
            val = val % 10            # Current digit value

            cur.next = ListNode(val)  # Append to result list
            cur = cur.next            # Move result pointer forward

            # Move input pointers forward if available
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return head of the new list (skipping dummy)