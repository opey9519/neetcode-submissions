# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count Nodes
        counter = 0
        cur = head
        while cur:
            counter += 1
            cur = cur.next
        
        removeIdx = counter - n
        curIdx = 1

        # Edge Case: need to remove 1 node w/ len(LL) == 1
        if removeIdx == 0:
            return head.next

        # Find node to remove
        cur = head
        for i in range(counter - 1):
            # Iterate until right before node, then skip
            if (i + 1) == removeIdx:
                cur.next = cur.next.next
                break
            cur = cur.next
        
        return head
        
