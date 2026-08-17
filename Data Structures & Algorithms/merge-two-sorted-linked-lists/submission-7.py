# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # New list & pointer
        newHead = node = ListNode()

        while list1 and list2:
            # Compare to find value to append
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
            
        # Append rest of nodes if applicable
        node.next = list1 or list2
        
        # Return the first node of new list
        return newHead.next