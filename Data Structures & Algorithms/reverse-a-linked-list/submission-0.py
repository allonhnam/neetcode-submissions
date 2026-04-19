# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head  # prev will eventually become the new head

        while curr:
            temp = curr.next      # Save the next node
            curr.next = prev      # Reverse the current node's pointer
            prev = curr           # Move prev and curr one step forward
            curr = temp

        return prev  # New head of the reversed list
