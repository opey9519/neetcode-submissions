# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create newList + Pointer
        newList = node = ListNode()

        # Loop through each list
        while list1 and list2:
            # Compare values, update newList
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            # Move newList pointer
            node = node.next
        
        # Append rest of nodes if one list is Null
        node.next = list1 or list2

        # Return newList
        return newList.next
        