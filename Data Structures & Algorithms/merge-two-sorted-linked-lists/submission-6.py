# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create new LL + Node Pointer
        newList = nodeP = ListNode()

        # Iterate through
        while list1 and list2:
            # Comparison
            if list1.val < list2.val:
                nodeP.next = list1
                list1 = list1.next
            else:
                nodeP.next = list2
                list2 = list2.next
            
            # Assign new new and advance
            nodeP = nodeP.next
        
        # If still nodes, append
        nodeP.next = list1 or list2

        return newList.next