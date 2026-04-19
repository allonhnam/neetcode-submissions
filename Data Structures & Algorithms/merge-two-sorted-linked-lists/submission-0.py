# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()  # Dummy node to simplify edge cases

        while list1 and list2:
            # Pick the smaller node and attach it to the merged list
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next  # Move to the newly added node

        # Attach any remaining nodes
        node.next = list1 or list2

        return dummy.next  # Return the merged list, skipping dummy