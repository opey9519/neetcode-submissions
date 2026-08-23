# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge Case: No lists
        if not lists: return None
        
        # While there is at least 1 list, we continue algorithm
        while len(lists) > 1:
            mergedLists = []
            # Merge lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeTwoLL(l1, l2))
            lists = mergedLists
        
        return lists[-1]

    # Merge Two Sorted Linked Lists and return Head
    def mergeTwoLL(self, head1, head2):
        list1, list2 = head1, head2
        newHead = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2

        return newHead.next
            
    
    